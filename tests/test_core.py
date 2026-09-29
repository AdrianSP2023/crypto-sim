"""Pruebas del núcleo con velas sintéticas (sin red).

1. Sin mirar al futuro: la señal de entrada/salida en la vela i es la misma
   calculando con datos hasta i que con todo el histórico (todas las estrategias).
2. Referencia independiente de las salidas genéricas (SL/TP/timeout/señal)
   para c_banda_atr, escrita como bucle simple.
3. Incremental == de golpe: ejecuciones troceadas, repetidas y con huecos,
   guardando/cargando JSON, dan exactamente el mismo resultado.
4. Todas las estrategias generan operaciones con estos datos (las pruebas las ejercitan).
"""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import core
from strategies import REGISTRY

CFG_RAW = json.loads((Path(__file__).resolve().parents[1] / "config.json").read_text())
import copy as _copy
CFG = _copy.deepcopy(CFG_RAW)          # modo "clasico" (entrada al cierre, comision fija) para las pruebas antiguas
CFG["entry_fill"] = "close"
CFG.pop("fee_tiers", None)

def synth(seed, n=700, start=1_760_000_000):
    rng = np.random.default_rng(seed)
    seg = n // 5
    drift = np.concatenate([np.full(seg, 0.0), np.full(seg, 0.0012), np.full(seg, -0.0012), np.full(seg, 0.0), np.full(n - 4 * seg, 0.0008)])
    vol = 0.004 * (1 + (rng.random(n) < 0.03) * 4)       # a veces velas violentas
    r = drift + rng.normal(0, 1, n) * vol
    close = 50 * np.exp(np.cumsum(r))
    op = np.concatenate([[50], close[:-1]])
    hi = np.maximum(op, close) * (1 + np.abs(rng.normal(0, 0.002, n)))
    lo = np.minimum(op, close) * (1 - np.abs(rng.normal(0, 0.002, n)))
    volume = rng.lognormal(3, 0.6, n) * (1 + (np.abs(r) > 0.008) * 3)
    return pd.DataFrame({"time": start + 300 * np.arange(n), "open": op, "high": hi, "low": lo, "close": close, "volume": volume})

def test_no_lookahead():
    df = synth(1)
    for name, p in CFG["strategies"].items():
        prep, entry, ex = REGISTRY[p.get("base", name)]
        full = prep(df, p)
        for i in range(CFG["warmup"], len(df), 7):
            part = prep(df.iloc[: i + 1].reset_index(drop=True), p)
            assert entry(full, i, p) == entry(part, i, p), (name, i)
            assert ex(full, i, p) == ex(part, i, p), (name, i)
    print("sin mirar al futuro OK")

def reference_c(df, p, warmup, csec=300):
    prep, entry, ex = REGISTRY["c_banda_atr"]
    d = prep(df, p)
    out, pos = [], None
    for i in range(len(d)):
        if pos:
            e, ei = pos
            px = None
            if d.low[i] <= e * (1 - p["sl"]): px = min(d.open[i], e * (1 - p["sl"]))
            elif d.high[i] >= e * (1 + p["tp"]): px = max(d.open[i], e * (1 + p["tp"]))
            elif ex(d, i, p): px = d.close[i]
            elif i - ei >= p["max_hold"]: px = d.close[i]
            if px is not None:
                out.append(round((px / e - 1) * 100, 3)); pos = None
            continue
        if i >= warmup and entry(d, i, p):
            pos = (d.close[i], i)
    return out

def run_batch(frames, cfg):
    st = core.new_state(cfg)
    for a, df in frames.items():
        st["last_candle"][a] = int(df.time.iat[cfg["warmup"] - 1])
    core.process_frames(st, frames, cfg, [])
    return st

def test_reference_and_coverage():
    counts = {k: 0 for k in CFG["strategies"]}
    for seed in range(25):
        df = synth(seed)
        st = run_batch({"X": df}, CFG)
        got = [t["gross_pct"] for t in st["strategies"]["c_banda_atr"]["closed"]]
        ref = reference_c(df, CFG["strategies"]["c_banda_atr"], CFG["warmup"])
        # el motor abre desde warmup; la referencia igual: deben coincidir
        assert got == ref, (seed, got[:5], ref[:5])
        for k in counts:
            counts[k] += len(st["strategies"][k]["closed"])
    assert all(v >= 5 for k, v in counts.items() if not k.endswith("_regimen")), counts
    print("referencia c_banda_atr OK · operaciones por estrategia:", counts)

def test_incremental_equals_batch():
    frames = {a: synth(40 + k) for k, a in enumerate("ABCD")}
    batch = run_batch(frames, CFG)
    st = core.new_state(CFG)
    for a, df in frames.items():
        st["last_candle"][a] = int(df.time.iat[CFG["warmup"] - 1])
    rng = np.random.default_rng(7)
    n = len(frames["A"]); cut = CFG["warmup"] + 1
    while True:
        core.process_frames(st, {a: df.iloc[:cut].reset_index(drop=True) for a, df in frames.items()}, CFG, [])
        st = json.loads(json.dumps(st))
        if cut == n: break
        cut = min(n, cut + int(rng.choice([0, 1, 1, 1, 2, 5, 12])))
    for k in CFG["strategies"]:
        a, b = batch["strategies"][k], st["strategies"][k]
        assert a["closed"] == b["closed"] and a["positions"] == b["positions"] and abs(a["cash"] - b["cash"]) < 1e-9, k
    print("incremental == de golpe OK")

def test_market_filter():
    """Variante filtrada = misma estrategia base, pero solo entra con amplitud >= umbral."""
    frames = {a: synth(60 + k) for k, a in enumerate("ABCDEF")}
    st = run_batch(frames, CFG)
    for base in ["c_banda_atr", "ruptura_volumen", "macd_momentum"]:
        pv = CFG["strategies"][base + "_regimen"]
        br = core.market_breadth(frames, CFG, pv["market_filter_ema"])
        f = st["strategies"][base + "_regimen"]
        thr = pv["market_filter"]
        for t in f["closed"]:
            assert br[t["entry_ts"] - 300] >= thr, (base, t)
        assert f["blocked_filter"] > 0, base
    print("filtro de regimen OK:", {b: st["strategies"][b]["blocked_filter"] for b in st["strategies"] if b.endswith("_regimen")})

def test_max_open():
    """Variante con tope: nunca hay mas de max_open posiciones simultaneas y se registran los bloqueos."""
    frames = {a: synth(80 + k) for k, a in enumerate("ABCDEFGHIJKLMNOP")}
    import copy
    cfg = copy.deepcopy(CFG)
    for p in cfg["strategies"].values():
        if p.get("max_open"):
            p["max_open"] = 1  # tope muy bajo para que los datos sinteticos lo alcancen
    st = run_batch(frames, cfg)
    csec = cfg["candle_minutes"] * 60
    for name, p in cfg["strategies"].items():
        mo = p.get("max_open")
        if not mo:
            continue
        s = st["strategies"][name]
        iv = [(c["entry_ts"], c["exit_ts"]) for c in s["closed"]]
        iv += [(x["entry_candle"] + csec, 10**12) for x in s["positions"].values()]
        for t0, _ in iv:
            n = sum(1 for a, b in iv if a <= t0 < b)
            assert n <= mo, (name, n, mo)
        base = st["strategies"][p["base"]]
        assert s["blocked_exposure"] > 0, name
        print("tope de exposicion OK:", name, "bloqueadas", s["blocked_exposure"], "cierres", len(s["closed"]), "frente a base", len(base["closed"]))

def reference_c_next(df, p, warmup):
    """Referencia independiente con entrada a la APERTURA de la vela siguiente a la señal."""
    prep, entry, ex = REGISTRY["c_banda_atr"]
    d = prep(df, p)
    out, pos, pend = [], None, False
    for i in range(len(d)):
        if pend and pos is None:
            pos = (d.open[i], i - 1)
        pend = False
        if pos:
            e, ei = pos
            px = None
            if d.low[i] <= e * (1 - p["sl"]): px = min(d.open[i], e * (1 - p["sl"]))
            elif d.high[i] >= e * (1 + p["tp"]): px = max(d.open[i], e * (1 + p["tp"]))
            elif ex(d, i, p): px = d.close[i]
            elif i - ei >= p["max_hold"]: px = d.close[i]
            if px is not None:
                out.append(round((px / e - 1) * 100, 3)); pos = None
            continue
        if i >= warmup and entry(d, i, p):
            pend = True
    return out

def cfg_next():
    import copy
    c = copy.deepcopy(CFG_RAW)
    c["entry_fill"] = "next_open"
    return c

def test_next_open_reference():
    cfg = cfg_next()
    total = 0
    for seed in range(25):
        df = synth(seed)
        st = run_batch({"X": df}, cfg)
        got = [t["gross_pct"] for t in st["strategies"]["c_banda_atr"]["closed"]]
        ref = reference_c_next(df, cfg["strategies"]["c_banda_atr"], cfg["warmup"])
        assert got == ref, (seed, got[:5], ref[:5])
        total += len(got)
        # la entrada se ejecuta a la apertura de la vela siguiente a la señal
        for t in st["strategies"]["c_banda_atr"]["closed"]:
            row = df[df.time == t["entry_ts"]].iloc[0]
            assert abs(t["entry"] - row.open) < 1e-6 * row.open + 1e-9, (seed, t)
    assert total > 40, total
    print("entrada a apertura siguiente: referencia OK,", total, "operaciones")

def test_fee_tiers_and_volume():
    cfg = cfg_next()
    cfg["fee_tiers"] = [{"from": 0, "side": 0.0055}, {"from": 150, "side": 0.0025}, {"from": 600, "side": 0.0021}]
    frames = {a: synth(90 + k) for k, a in enumerate("ABCDEFGH")}
    st = run_batch(frames, cfg)
    ok = {round(a + b, 3) for a in (0.55, 0.25, 0.21) for b in (0.55, 0.25, 0.21)}
    for name, s in st["strategies"].items():
        if not s["closed"]:
            continue
        for c in s["closed"]:
            assert round(c["fee_pct"], 3) in ok, (name, c["fee_pct"])
            assert abs(c["net_pct"] - (c["gross_pct"] - c["fee_pct"])) < 0.002, (name, c)
        # el primer cierre paga mas que los ultimos (el volumen sube de tramo)
        assert s["closed"][0]["fee_pct"] >= s["closed"][-1]["fee_pct"], name
        # volumen registrado = entradas (cerradas + abiertas) + salidas
        vol = sum(v for _, v in s["volume_log"])
        exp = sum(c["qty"] * (1 + 1 + c["gross_pct"] / 100) for c in s["closed"]) + sum(p["qty"] for p in s["positions"].values())
        assert abs(vol - exp) < 0.06 * (len(s["closed"]) * 2 + len(s["positions"]) + 1), (name, vol, exp)
    n_low = sum(1 for s in st["strategies"].values() for c in s["closed"] if c["fee_pct"] < 1.0)
    assert n_low > 50, n_low
    print("comision por tramos y volumen OK · cierres con tramo reducido:", n_low)

def test_incremental_next_open():
    cfg = cfg_next()
    cfg["fee_tiers"] = [{"from": 0, "side": 0.0055}, {"from": 300, "side": 0.0025}]
    frames = {a: synth(140 + k) for k, a in enumerate("ABCD")}
    batch = run_batch(frames, cfg)
    st = core.new_state(cfg)
    for a, df in frames.items():
        st["last_candle"][a] = int(df.time.iat[cfg["warmup"] - 1])
    rng = np.random.default_rng(11)
    n = len(frames["A"]); cut = cfg["warmup"] + 1
    while True:
        core.process_frames(st, {a: df.iloc[:cut].reset_index(drop=True) for a, df in frames.items()}, cfg, [])
        st = json.loads(json.dumps(st))
        if cut == n: break
        cut = min(n, cut + int(rng.choice([0, 1, 1, 1, 2, 5, 12])))
    for k in cfg["strategies"]:
        a, b = batch["strategies"][k], st["strategies"][k]
        assert a["closed"] == b["closed"] and a["positions"] == b["positions"] and a["pending"] == b["pending"] and abs(a["cash"] - b["cash"]) < 1e-9, k
    print("incremental == de golpe (entrada a apertura siguiente + tramos) OK")

if __name__ == "__main__":
    test_next_open_reference(); test_fee_tiers_and_volume(); test_incremental_next_open()
    test_max_open()
    test_market_filter()
    test_no_lookahead(); test_reference_and_coverage(); test_incremental_equals_batch()
