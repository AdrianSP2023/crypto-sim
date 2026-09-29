"""Decisión determinista de paso a P7 (dinero real) y cálculo por ciclos de 24 h.

Uso:
  python3 tools/decide_p7.py            # tabla por ciclo + decisión
  python3 tools/decide_p7.py --json out.json   # además guarda el informe (con el commit)

Lee state/state.json y config.json del repo. No usa red ni hora actual: el
resultado depende solo de los datos, así que es reproducible (plan-trading.md,
criterio de P7 y salvaguardas 1-8).

Ciclo = 24 h entre dos fotos horarias del estado (state["snapshots"]) que
guardan precios y patrimonio de cada estrategia valorando lo abierto a mercado
y descontando comisiones de entrada y salida. Así el PnL de un ciclo incluye
lo realizado y lo no realizado (salvaguarda 1).

Un ciclo de una estrategia "pasa" si cumple TODO:
  - PnL neto del ciclo >= +1 % de la caja inicial (tras comisión por tramos y
    spread de los cierres del ciclo);
  - >= 30 cierres en el ciclo;
  - todos esos cierres son de la versión actual de la estrategia (fuera de muestra);
  - el motor estuvo sano: ningún hueco > 15 min entre vueltas dentro del ciclo;
  - quitando la mejor operación cerrada, el PnL sigue siendo > 0;
  - quitando el mejor activo, el PnL sigue siendo > 0;
  - supera a la cesta equiponderada de los activos (mantener), y la cesta no
    subió más de BASKET_MAX (si sube más, el ciclo es no concluyente).
Vía diaria: 2 ciclos consecutivos que pasan.
Vía semanal: en 7 ciclos consecutivos, >= 4 pasan, media diaria > 0.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CYCLE = 24 * 3600
GOAL_PCT = 1.0
MIN_CLOSES = 30
MAX_GAP_MIN = 15
BASKET_MAX = 2.0   # % [Suposición]: cesta que sube más de esto => ciclo no concluyente


def load():
    state = json.loads((ROOT / "state" / "state.json").read_text())
    cfg = json.loads((ROOT / "config.json").read_text())
    return state, cfg


def basket_return(s0, s1):
    r = [s1["prices"][a] / s0["prices"][a] - 1 for a in s0["prices"] if a in s1["prices"] and s0["prices"][a] > 0]
    return 100 * sum(r) / len(r) if r else 0.0


def boundaries(snaps):
    """Fotos que delimitan ciclos completos: la primera y la primera con ts >= anterior + 24 h."""
    if not snaps:
        return []
    out = [snaps[0]]
    for s in snaps[1:]:
        if s["ts"] >= out[-1]["ts"] + CYCLE - 600:
            out.append(s)
    return out


def evaluate(state, cfg):
    snaps = state.get("snapshots", [])
    bounds = boundaries(snaps)
    gaps = state.get("loop_gaps", [])
    cash0 = cfg["initial_cash"]
    res = {}
    for name, st in state["strategies"].items():
        ver = cfg["version"]
        rows = []
        for k in range(len(bounds) - 1):
            a, b = bounds[k], bounds[k + 1]
            cl = [c for c in st["closed"] if a["ts"] < c["exit_ts"] <= b["ts"]]
            eq0, eq1 = a["equity"].get(name), b["equity"].get(name)
            if eq0 is None or eq1 is None:
                continue
            spread_cost = sum(c["qty"] * (c["net_spread_pct"] - c["net_pct"]) / 100 for c in cl)
            pnl = eq1 - eq0 + spread_cost
            pct = 100 * pnl / cash0
            best_trade = max((c["pnl_eur"] for c in cl), default=0.0)
            by_asset = {}
            for c in cl:
                by_asset[c["asset"]] = by_asset.get(c["asset"], 0.0) + c["pnl_eur"]
            best_asset = max(by_asset.values(), default=0.0)
            bk = basket_return(a, b)
            chk = {
                "objetivo_1pct": pct >= GOAL_PCT,
                "cierres_min": len(cl) >= MIN_CLOSES,
                "version_actual": bool(cl) and all(c["version"] == ver for c in cl),
                "motor_sano": not any(a["ts"] < g[0] <= b["ts"] for g in gaps if g[1] > MAX_GAP_MIN),
                "sin_mejor_operacion": pnl - best_trade > 0,
                "sin_mejor_activo": pnl - best_asset > 0,
                "supera_cesta": pct > bk,
                "cesta_no_concluyente": bk > BASKET_MAX,
            }
            chk = {k_: bool(v_) for k_, v_ in chk.items()}
            ok = all(v for key, v in chk.items() if key != "cesta_no_concluyente") and not chk["cesta_no_concluyente"]
            rows.append({"ciclo": k + 1, "desde": a["ts"], "hasta": b["ts"], "cierres": len(cl),
                         "pnl_eur": round(float(pnl), 2), "pnl_pct": round(float(pct), 3), "cesta_pct": round(float(bk), 3),
                         "comprobaciones": chk, "pasa": ok})
        res[name] = {"ciclos": rows, "diaria": daily(rows), "semanal": weekly(rows)}
    return res


def daily(rows):
    return any(rows[i]["pasa"] and rows[i + 1]["pasa"] for i in range(len(rows) - 1))


def weekly(rows):
    for i in range(len(rows) - 6):
        w = rows[i:i + 7]
        if sum(1 for r in w if r["pasa"]) >= 4 and sum(r["pnl_eur"] for r in w) > 0:
            return True
    return False


def report(state, cfg):
    res = evaluate(state, cfg)
    try:
        commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    except Exception:
        commit = "?"
    return {"commit": commit, "version": cfg["version"], "phase": cfg["phase"],
            "ultima_vuelta": state.get("last_loop"), "estrategias": res,
            "pasan_diaria": [n for n, r in res.items() if r["diaria"]],
            "pasan_semanal": [n for n, r in res.items() if r["semanal"]]}


def print_report(rep):
    print(f"Decisión P7 · fase {rep['phase']} · {rep['version']} · commit {rep['commit'][:8]} · última vuelta {rep['ultima_vuelta']}")
    print(f"{'estrategia':28s} {'ciclos':>6s} {'últ.ciclo: cierres':>18s} {'PnL%':>7s} {'cesta%':>7s}  pasa  diaria semanal")
    for n, r in rep["estrategias"].items():
        if r["ciclos"]:
            u = r["ciclos"][-1]
            print(f"{n:28s} {len(r['ciclos']):6d} {u['cierres']:18d} {u['pnl_pct']:+7.2f} {u['cesta_pct']:+7.2f}  {'SÍ' if u['pasa'] else 'no':4s}  {'SÍ' if r['diaria'] else 'no':6s} {'SÍ' if r['semanal'] else 'no'}")
        else:
            print(f"{n:28s} {0:6d} {'(sin ciclo completo)':>18s}")
    print("Pasan por vía diaria:", rep["pasan_diaria"] or "ninguna")
    print("Pasan por vía semanal:", rep["pasan_semanal"] or "ninguna")


if __name__ == "__main__":
    st, cf = load()
    rep = report(st, cf)
    print_report(rep)
    if "--json" in sys.argv:
        Path(sys.argv[sys.argv.index("--json") + 1]).write_text(json.dumps(rep, ensure_ascii=False, indent=1))
