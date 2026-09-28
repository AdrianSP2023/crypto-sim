#!/usr/bin/env python3
"""
Resúmenes del estado: STATUS.md (lo genera el motor en cada vuelta) y un
análisis por consola para los check-ins y las fases de análisis.

Uso:  python report.py            -> análisis acumulado de la fase
      python report.py --hours 1  -> solo operaciones cerradas en la última hora
"""

import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


def stats(trades):
    n = len(trades)
    if not n:
        return dict(n=0, win=0.0, gross=0.0, net=0.0, net_sp=0.0, pnl=0.0)
    return dict(
        n=n,
        win=sum(t["net_pct"] > 0 for t in trades) / n * 100,
        gross=sum(t["gross_pct"] for t in trades) / n,
        net=sum(t["net_pct"] for t in trades) / n,
        net_sp=sum(t["net_spread_pct"] for t in trades) / n,
        pnl=sum(t["pnl_eur"] for t in trades),
    )


def mark_value(st, prices):
    v = 0.0
    for a, p in st["positions"].items():
        px = prices.get(a)
        v += p["qty"] * (px / p["entry_price"]) if px else p["qty"]
    return v


def status_md(state, cfg, warnings, log):
    prices = state.get("last_prices", {})
    L = [f"# Simulación {state['phase']} (sin dinero real)", ""]
    L.append(f"Config `{cfg['version']}` · inicio {state['started_at'][:16].replace('T', ' ')} UTC · "
             f"última vuelta {state['last_loop'][:16].replace('T', ' ')} UTC · vueltas {state['loops']} · "
             f"{len(state['universe'])} activos · velas {cfg['candle_minutes']} min · comisión {cfg['fee_round_trip']*100:.1f}% ida+vuelta")
    L.append("")
    if warnings:
        L += ["**Avisos:** " + " · ".join(warnings), ""]
    L.append("| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    total_eq = 0.0
    for name, st in state["strategies"].items():
        s = stats(st["closed"])
        eq = st["cash"] + mark_value(st, prices)
        total_eq += eq
        init = cfg["initial_cash"]
        L.append(f"| {name} | {eq:.2f} € ({(eq/init-1)*100:+.2f}%) | {s['n']} | {len(st['positions'])} | "
                 f"{s['win']:.0f}% | {s['gross']:+.3f}% | {s['net']:+.3f}% | {s['net_sp']:+.3f}% | {s['pnl']:+.2f} € |")
    L.append("")
    allc = [t for st in state["strategies"].values() for t in st["closed"]]
    if allc:
        L += ["## Últimas 15 operaciones cerradas", "",
              "| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |", "|---|---|---|---|---|---|---|"]
        for t in sorted(allc, key=lambda t: t["exit_ts"])[-15:][::-1]:
            L.append(f"| {t['exit_t']} | {t['strategy']} | {t['asset']} | {t['reason']} | "
                     f"{t['gross_pct']:+.2f}% | {t['net_pct']:+.2f}% | {t['pnl_eur']:+.2f} |")
        L.append("")
    if log:
        L += ["## Eventos de la última vuelta", "", *[f"- {x}" for x in log], ""]
    L.append("Universo: " + ", ".join(x["asset"] for x in state["universe"]))
    return "\n".join(L) + "\n"


def analyze(state, hours=None):
    cut = None
    if hours:
        cut = datetime.now(timezone.utc).timestamp() - hours * 3600
    out = []
    head = f"Fase {state['phase']} · vueltas {state['loops']} · última {state['last_loop']}"
    if state.get("last_warnings"):
        head += f" · avisos: {state['last_warnings']}"
    out.append(head)
    out.append(f"{'estrategia':22} {'n':>4} {'acierto':>7} {'bruto':>8} {'neto':>8} {'neto+sp':>8} {'PnL€':>8} {'abiertas':>8} {'sin caja':>8} {'filtradas':>9}")
    for name, st in state["strategies"].items():
        tr = [t for t in st["closed"] if cut is None or t["exit_ts"] >= cut]
        s = stats(tr)
        out.append(f"{name:22} {s['n']:>4} {s['win']:>6.0f}% {s['gross']:>+7.3f}% {s['net']:>+7.3f}% "
                   f"{s['net_sp']:>+7.3f}% {s['pnl']:>+8.2f} {len(st['positions']):>8} {st['skipped_no_cash']:>8} {st.get('blocked_filter', 0):>9}")
    # desglose por motivo de salida y por versión (acumulado)
    out.append("")
    for name, st in state["strategies"].items():
        tr = [t for t in st["closed"] if cut is None or t["exit_ts"] >= cut]
        if not tr:
            continue
        by_r = defaultdict(list)
        by_v = defaultdict(list)
        for t in tr:
            by_r[t["reason"]].append(t)
            by_v[t["version"]].append(t)
        rs = " · ".join(f"{r}: {len(v)} ({stats(v)['gross']:+.2f}%)" for r, v in sorted(by_r.items()))
        vs = " · ".join(f"{k}: {len(v)} ops, bruto {stats(v)['gross']:+.3f}%" for k, v in sorted(by_v.items()))
        out.append(f"{name}: salidas [{rs}] | versiones [{vs}]")
    return "\n".join(out)


if __name__ == "__main__":
    hours = None
    if "--hours" in sys.argv:
        hours = float(sys.argv[sys.argv.index("--hours") + 1])
    st = json.loads((Path(__file__).parent / "state" / "state.json").read_text())
    print(analyze(st, hours))
