"""Rasgos del modelo de precursores (idénticos a tools/precursores_subidas.py; tests/test_modelo.py comprueba que coinciden).
Entrada: DataFrame de velas de 1 h con índice = INICIO de la vela (UTC) y columnas open, high, low, close, volume, trades.
Todos los rasgos de la hora t usan solo datos hasta el cierre de t."""
import numpy as np
import pandas as pd

COLS = ["ret1", "ret3", "ret6", "ret12", "ret24", "ret72", "vol_z", "trades_z", "range_ratio6", "range_last", "rv_ratio",
        "dist_hi24", "dist_hi168", "dist_lo72", "close_pos", "btc1", "btc6", "rel6", "hsin", "hcos", "dow", "breadth3"]
REQ = ["ret72", "vol_z", "range_ratio6", "rv_ratio", "dist_hi168", "btc6"]


def features(d, btc):
    c, o, h, l, v, n = d.close, d.open, d.high, d.low, d.volume, d.trades
    f = pd.DataFrame(index=d.index)
    for k in (1, 3, 6, 12, 24, 72):
        f[f"ret{k}"] = c / c.shift(k) - 1
    f["vol_z"] = v / v.rolling(168, min_periods=100).median()
    f["trades_z"] = n / n.rolling(168, min_periods=100).median()
    rng = (h - l) / c
    f["range_ratio6"] = rng.rolling(6).mean() / rng.rolling(168, min_periods=100).mean()
    f["range_last"] = rng / rng.rolling(168, min_periods=100).mean()
    r1 = c.pct_change()
    f["rv_ratio"] = r1.rolling(24).std() / r1.rolling(168, min_periods=100).std()
    f["dist_hi24"] = c / h.rolling(24).max() - 1
    f["dist_hi168"] = c / h.rolling(168, min_periods=100).max() - 1
    f["dist_lo72"] = c / l.rolling(72).min() - 1
    f["close_pos"] = (c - l) / (h - l).replace(0, np.nan)
    f["btc1"] = btc.reindex(d.index).pct_change(1)
    f["btc6"] = btc.reindex(d.index).pct_change(6)
    f["rel6"] = f["ret6"] - f["btc6"]
    hr = d.index.hour
    f["hsin"], f["hcos"] = np.sin(2 * np.pi * hr / 24), np.cos(2 * np.pi * hr / 24)
    f["dow"] = d.index.dayofweek
    return f


def panel_features(panel):
    """panel: dict activo -> DataFrame de velas de 1 h (reindexadas por hora, huecos = NaN). Devuelve DataFrame largo con 'activo'."""
    btc = panel["BTC"].close
    parts = []
    for a, d in panel.items():
        f = features(d, btc)
        f["activo"] = a
        parts.append(f)
    X = pd.concat(parts)
    X["breadth3"] = X.groupby(level=0).ret3.transform(lambda s: (s > 0).mean())
    return X
