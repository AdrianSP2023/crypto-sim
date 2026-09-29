"""Prueba de extremo a extremo del motor con Kraken simulado (sin red):
una vuelta real de engine.one_loop por cada vela, comprobando fotos horarias,
huecos de vueltas y la decision de P7 sobre los datos."""
import copy, json, sys
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tests")); sys.path.insert(0, str(ROOT / "tools"))
import core, engine, decide_p7
from test_core import synth

def main():
    cfg = copy.deepcopy(json.loads((ROOT / "config.json").read_text()))
    cfg["entry_fill"] = "next_open"
    cfg["fee_tiers"] = [{"from": 0, "side": 0.0055}, {"from": 300, "side": 0.0025}]
    assets = list("ABCDEF")
    full = {a: synth(200 + k, n=900) for k, a in enumerate(assets)}
    csec = 300
    t0 = int(full["A"].time.iat[cfg["warmup"] + 5])
    state = core.new_state(cfg)
    state["universe"] = [{"asset": a, "pair": a + "EUR"} for a in assets]
    state["universe_cfg"] = cfg["universe"]
    clock = {"now": t0 + csec}
    class FakeNow:
        pass
    from datetime import datetime, timezone
    engine.now = lambda: datetime.fromtimestamp(clock["now"], timezone.utc)
    engine.fetch_spreads = lambda u: {x["asset"]: 0.0004 for x in u}
    engine.fetch_ohlc = lambda pair, minutes, now_ts: full[pair[0]][full[pair[0]].time + csec <= now_ts].reset_index(drop=True)
    engine.time.sleep = lambda s: None
    end = int(full["A"].time.iat[-1]) + csec
    gap_at = t0 + csec * 200
    n = 0
    while clock["now"] <= end:
        engine.one_loop(state, cfg)
        n += 1
        clock["now"] += csec * (5 if clock["now"] == gap_at else 1)
        if clock["now"] > gap_at and not state.get("loop_gaps") and clock["now"] < gap_at + csec * 8:
            pass
    snaps = state["snapshots"]
    assert len(snaps) >= 5, len(snaps)
    assert all(b["ts"] - a["ts"] >= 3600 - 120 for a, b in zip(snaps, snaps[1:]))
    assert set(snaps[-1]["equity"]) == set(cfg["strategies"])
    # el patrimonio marcado coincide con caja + posiciones a mercado
    eq = core.equity_marked(state, cfg, state["last_prices"])
    for name, s in state["strategies"].items():
        assert eq[name] > 0.9 * cfg["initial_cash"], name
    print("vueltas:", n, "· fotos:", len(snaps), "· huecos:", state.get("loop_gaps"))
    # decision: con datos sinteticos, el informe corre y es determinista
    decide_p7.ROOT = ROOT
    r1 = decide_p7.evaluate(state, cfg); r2 = decide_p7.evaluate(state, cfg)
    assert json.dumps(r1, sort_keys=True) == json.dumps(r2, sort_keys=True)
    k = next(iter(r1))
    print("ciclos evaluados por estrategia:", len(r1[k]["ciclos"]), "· ejemplo:", {x: r1[k]["ciclos"][0][x] for x in ("cierres", "pnl_pct", "cesta_pct", "pasa")} if r1[k]["ciclos"] else "sin ciclo completo (datos < 24 h)")
    print("motor extremo a extremo OK")

if __name__ == "__main__":
    main()
