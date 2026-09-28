"""
Estrategias de P1 (velas de 5 min). Cada estrategia define:

  prep(df, p)          -> DataFrame con las columnas de indicadores que necesita
  entry(d, i, p)       -> True si hay señal de compra al cierre de la vela i
  exit_signal(d, i, p) -> motivo (str) si hay que salir por señal propia, o None

El take-profit, el stop-loss y el timeout son genéricos (core.py) y se
leen de los parámetros tp / sl / max_hold de cada estrategia.

Todos los indicadores son causales: el valor en la vela i solo usa datos
hasta la vela i (sin mirar al futuro).
"""

import numpy as np
import pandas as pd


# ---------------------------------------------------------------- indicadores

def ema(s, n):
    return s.ewm(span=n, adjust=False).mean()


def rsi(s, n):
    delta = s.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    roll_up = up.ewm(alpha=1 / n, adjust=False).mean()
    roll_down = down.ewm(alpha=1 / n, adjust=False).mean()
    rs = roll_up / roll_down.replace(0, np.nan)
    return (100 - (100 / (1 + rs))).fillna(50)


def atr(df, n=14):
    h, l, c = df["high"], df["low"], df["close"]
    pc = c.shift(1)
    tr = pd.concat([h - l, (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


def adx(df, n=14):
    h, l, c = df["high"], df["low"], df["close"]
    up = h.diff()
    down = -l.diff()
    plus_dm = np.where((up > down) & (up > 0), up, 0.0)
    minus_dm = np.where((down > up) & (down > 0), down, 0.0)
    tr = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(axis=1)
    a = tr.ewm(alpha=1 / n, adjust=False).mean()
    pdi = 100 * pd.Series(plus_dm, index=df.index).ewm(alpha=1 / n, adjust=False).mean() / a
    mdi = 100 * pd.Series(minus_dm, index=df.index).ewm(alpha=1 / n, adjust=False).mean() / a
    dx = 100 * (pdi - mdi).abs() / (pdi + mdi).replace(0, np.nan)
    return dx.ewm(alpha=1 / n, adjust=False).mean().fillna(0)


# ------------------------------------------- S1: Candidata C (banda ATR) en 5m

def prep_c(df, p):
    d = df.copy()
    d["ef"] = ema(d.close, p["fast"])
    d["es"] = ema(d.close, p["slow"])
    d["r"] = rsi(d.close, p["rsi_n"])
    d["atr"] = atr(d, p["atr_n"])
    return d


def entry_c(d, i, p):
    return bool(
        d.ef.iat[i - 1] <= d.es.iat[i - 1] and d.ef.iat[i] > d.es.iat[i]
        and p["rsi_lo"] <= d.r.iat[i] <= p["rsi_hi"]
        and abs(d.ef.iat[i] - d.es.iat[i]) > p["atr_mult"] * d.atr.iat[i]
    )


def exit_c(d, i, p):
    if d.ef.iat[i - 1] >= d.es.iat[i - 1] and d.ef.iat[i] < d.es.iat[i]:
        return "cruce bajista"
    return None


# ------------------------------- S2: reversión a la media (Bollinger + ADX)

def prep_rev(df, p):
    d = df.copy()
    d["sma"] = d.close.rolling(p["bb_n"]).mean()
    d["lb"] = d.sma - p["bb_k"] * d.close.rolling(p["bb_n"]).std()
    d["r"] = rsi(d.close, p["rsi_n"])
    d["adx"] = adx(d, p["adx_n"])
    return d


def entry_rev(d, i, p):
    lb = d.lb.iat[i]
    return bool(
        lb == lb  # no NaN
        and d.adx.iat[i] < p["adx_max"]
        and d.close.iat[i] < lb
        and d.r.iat[i] < p["rsi_max"]
    )


def exit_none(d, i, p):
    return None


# -------------------------------------- S3: ruptura de máximos con volumen

def prep_brk(df, p):
    d = df.copy()
    n = p["lookback"]
    d["hh"] = d.high.shift(1).rolling(n).max()
    d["vma"] = d.volume.shift(1).rolling(n).mean()
    d["et"] = ema(d.close, p["ema_trend"])
    return d


def entry_brk(d, i, p):
    hh, vma = d.hh.iat[i], d.vma.iat[i]
    return bool(
        hh == hh and vma == vma and vma > 0
        and d.close.iat[i] > hh
        and d.volume.iat[i] > p["vol_mult"] * vma
        and d.close.iat[i] > d.et.iat[i]
    )


# ---------------------------------- S4: rebote tras caída fuerte (RSI extremo)

def prep_reb(df, p):
    d = df.copy()
    d["r"] = rsi(d.close, p["rsi_n"])
    d["drop"] = d.close / d.close.shift(p["drop_lookback"]) - 1
    return d


def entry_reb(d, i, p):
    dr = d["drop"].iat[i]
    return bool(dr == dr and d.r.iat[i] < p["rsi_max"] and dr <= -p["drop_min"])


# ----------------------------------- S5: retroceso a la EMA20 en tendencia

def prep_pb(df, p):
    d = df.copy()
    d["e1"] = ema(d.close, p["ema_fast"])
    d["e2"] = ema(d.close, p["ema_mid"])
    d["e3"] = ema(d.close, p["ema_slow"])
    return d


def entry_pb(d, i, p):
    return bool(
        d.e1.iat[i] > d.e2.iat[i] > d.e3.iat[i]
        and d.close.iat[i - 1] > d.e1.iat[i - 1]
        and d.low.iat[i] <= d.e1.iat[i]
        and d.close.iat[i] > d.e1.iat[i]
    )


def exit_pb(d, i, p):
    if d.close.iat[i] < d.e2.iat[i]:
        return "rotura de tendencia"
    return None


# ------------------------------------------------------------------ registro

REGISTRY = {
    "c_banda_atr": (prep_c, entry_c, exit_c),
    "reversion_bb": (prep_rev, entry_rev, exit_none),
    "ruptura_volumen": (prep_brk, entry_brk, exit_none),
    "rebote_extremo": (prep_reb, entry_reb, exit_none),
    "pullback_tendencia": (prep_pb, entry_pb, exit_pb),
}
