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

CFG = json.loads((Path(__file__).resolve().parents[1] / "config.json").read_text())

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
    assert all(v >= 5 for v in counts.values()), counts
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
    br = core.market_breadth(frames, CFG)
    for base in ["c_banda_atr", "ruptura_volumen", "macd_momentum", "pullback_tendencia"]:
        f = st["strategies"][base + "_filtro"]
        thr = CFG["strategies"][base + "_filtro"]["market_filter"]
        for t in f["closed"]:
            assert br[t["entry_ts"] - 300] >= thr, (base, t)
        assert f["blocked_filter"] > 0, base
    print("filtro de mercado OK:", {b: st["strategies"][b]["blocked_filter"] for b in st["strategies"] if b.endswith("_filtro")})

if __name__ == "__main__":
    test_market_filter()
    test_no_lookahead(); test_reference_and_coverage(); test_incremental_equals_batch()
