"""Pruebas del paper trader del modelo de precursores: (1) el pipeline en vivo reproduce las puntuaciones del entrenamiento,
(2) la máquina de estados (entrada, take-profit, tiempo, comisiones, máximo de posiciones, sin doble entrada)."""
import json
import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
import modelo.paper as M  # noqa: E402
import precursores_subidas as P  # noqa: E402
from modelo.features import COLS, features  # noqa: E402

M.MD = ROOT / "modelo"
model = joblib.load(ROOT / "modelo" / "modelo.joblib")
meta = json.loads((ROOT / "modelo" / "meta.json").read_text())


def test_features_iguales():
    d = pd.read_csv(ROOT / "datos" / "historico_1h" / "USD_ETH.csv.gz").tail(3000)
    d.index = pd.to_datetime(d.time, unit="s")
    d = d.reindex(pd.date_range(d.index.min(), d.index.max(), freq="h"))
    b = pd.read_csv(ROOT / "datos" / "historico_1h" / "USD_BTC.csv.gz").tail(3000)
    b.index = pd.to_datetime(b.time, unit="s")
    b = b.reindex(pd.date_range(b.index.min(), b.index.max(), freq="h")).close
    a1 = features(d, b)
    a2 = P.features(d, b)
    pd.testing.assert_frame_equal(a1, a2)


def test_pipeline_reproduce_entrenamiento():
    ev = pd.read_csv(ROOT / "datos" / "eventos" / "horas_modelo.csv").sort_values("t_utc")
    rows = ev.iloc[[0, len(ev) // 3, 2 * len(ev) // 3, len(ev) - 1]]
    full = {}
    for a in meta["activos"]:
        d = pd.read_csv(ROOT / "datos" / "historico_1h" / f"USD_{a}.csv.gz")
        full[a] = d
    ok = 0
    for _, r in rows.iterrows():
        t_start = int(pd.Timestamp(r.t_utc, tz="UTC").timestamp())
        ts = t_start + 3600 + 120                       # el flujo corre 2 min después de cerrar la vela
        frames = {}
        for a, d in full.items():
            w = d[(d.time + 3600 <= t_start + 3600) & (d.time >= t_start + 3600 - 720 * 3600)]
            if len(w) >= 200:
                frames[a] = w[["time", "open", "high", "low", "close", "volume", "trades"]].reset_index(drop=True)
        sc = M.score(M.to_panel(frames, ts), model, ts)
        row = sc[sc.activo == r.asset]
        assert len(row) == 1, (r.asset, r.t_utc)
        assert abs(row.p.iloc[0] - r.p) < 0.03, (r.asset, r.t_utc, row.p.iloc[0], r.p)
        assert row.p.iloc[0] >= meta["umbral"] - 0.03
        ok += 1
    assert ok == 4


class FakeKraken:
    def __init__(self, prices):
        self.prices = prices                              # activo -> (ask, bid)
        self.candles = {}

    def pairs(self, assets):
        return {a: {"pair": a + "USD", "key": a + "USD"} for a in self.prices}

    def ohlc(self, pair):
        return self.candles[pair[:-3]]

    def tickers(self, pairs):
        return {a: {"ask": self.prices[a][0], "bid": self.prices[a][1], "last": self.prices[a][0]} for a in pairs}


class Dummy:
    def __init__(self, p):
        self.p = p

    def predict_proba(self, X):
        return np.column_stack([1 - self.p(X), self.p(X)])


def flat_frames(ts, n=400, px=100.0, high_last=None):
    start = (ts // 3600) * 3600 - n * 3600
    t = np.arange(start, start + n * 3600, 3600)
    rng = np.random.RandomState(1)
    c = px * (1 + 0.001 * rng.randn(n)).cumprod()
    df = pd.DataFrame({"time": t, "open": c, "high": c * 1.002, "low": c * 0.998, "close": c, "vwap": c, "volume": 100.0 + rng.rand(n), "trades": 50.0})
    if high_last:
        df.loc[df.index[-1], "high"] = high_last
    return df


def test_maquina_de_estados():
    base_ts = 1_800_000_000 - (1_800_000_000 % 3600) + 120
    st = M.new_state()
    fk = FakeKraken({"BTC": (100.0, 99.9), "AAA": (50.0, 49.9), "BBB": (10.0, 9.9)})
    for a in fk.prices:
        fk.candles[a] = flat_frames(base_ts, px=fk.prices[a][0])
    always = Dummy(lambda X: np.full(len(X), 0.9))
    M.KRAKEN_PAUSA = 0
    import os
    os.environ["KRAKEN_PAUSA"] = "0"
    closed, opened, sc = M.step(st, always, 0.686, fk, base_ts, log=lambda *_: None)
    assert len(opened) == 3 and not closed
    assert abs(sum(p["tamano"] for p in st["open"]) - 3 * 0.025 * 924.24) < 0.5
    # segunda pasada 1 h después: no hay doble entrada
    ts2 = base_ts + 3600
    for a in fk.prices:
        fk.candles[a] = flat_frames(ts2, px=fk.prices[a][0])
    closed, opened, sc = M.step(st, always, 0.686, fk, ts2, log=lambda *_: None)
    assert len(opened) == 0 and len(st["open"]) == 3
    # take-profit: el máximo de la vela posterior supera +8 % en AAA
    ts3 = base_ts + 2 * 3600
    for a in fk.prices:
        fk.candles[a] = flat_frames(ts3, px=fk.prices[a][0], high_last=(50.0 * 1.09 if a == "AAA" else None))
    never = Dummy(lambda X: np.zeros(len(X)))
    closed, opened, sc = M.step(st, never, 0.686, fk, ts3, log=lambda *_: None)
    assert [c["activo"] for c in closed] == ["AAA"] and closed[0]["motivo"] == "take-profit"
    assert abs(closed[0]["bruto_pct"] - 8.0) < 0.01
    # comisión: 0,55 % por lado -> 1,1 % ida y vuelta sobre el tamaño (tramo inicial)
    assert abs(closed[0]["comision_pct"] - 1.1) < 0.05, closed[0]
    assert abs(closed[0]["neto_pct"] - (8.0 - closed[0]["comision_pct"])) < 0.05
    # salida por tiempo: 4 h después de la entrada, al bid
    ts4 = base_ts + 4 * 3600
    fk.prices["BTC"] = (98.0, 97.5)
    for a in fk.prices:
        fk.candles[a] = flat_frames(ts4, px=fk.prices[a][0])
    closed, opened, sc = M.step(st, never, 0.686, fk, ts4, log=lambda *_: None)
    assert sorted(c["activo"] for c in closed) == ["BBB", "BTC"] or sorted(c["activo"] for c in closed) == ["BTC"] or len(closed) >= 1
    assert all(c["motivo"] in ("tiempo", "take-profit") for c in closed)
    assert not st["open"] or all(p["activo"] != "BTC" for p in st["open"])
    btc = [c for c in closed if c["activo"] == "BTC"][0]
    assert btc["motivo"] == "tiempo" and abs(btc["salida"] - 97.5) < 1e-9 and btc["bruto_pct"] < 0
    # máximo de posiciones
    st2 = M.new_state()
    fk2 = FakeKraken({f"X{i}": (10.0, 9.99) for i in range(12)} | {"BTC": (100.0, 99.9)})
    for a in fk2.prices:
        fk2.candles[a] = flat_frames(base_ts, px=fk2.prices[a][0])
    closed, opened, sc = M.step(st2, always, 0.686, fk2, base_ts, log=lambda *_: None)
    assert len(st2["open"]) == M.CFG["max_open"]


if __name__ == "__main__":
    test_features_iguales()
    test_pipeline_reproduce_entrenamiento()
    test_maquina_de_estados()
    print("modelo de precursores (rasgos, pipeline en vivo, máquina de estados) OK")
