"""Busca precursores de subidas repentinas con velas de 1 h (histórico Kraken USD, 42 activos líquidos, 2018-2026).

Objetivo: ¿hay señales medibles ANTES de una subida? Etiqueta: rentabilidad de la apertura de la hora siguiente al
cierre de la hora +4 (close[t+4]/open[t+1]-1) >= UMBRAL (5 % y 10 %). Los rasgos de la hora t solo usan datos hasta el
cierre de t (sin mirar hacia delante). Validación con corte temporal: entrena 2018-2021, ajusta umbral en 2022, TEST 2023-2026
(no se toca). Se mide AUC, precisión en el 0,5 % de horas más puntuadas frente a la tasa base y, sobre todo, la rentabilidad
neta de entrar en esas horas (entrada apertura t+1, salida cierre t+4, coste 1,1 % y 0,5 %, sin solapes por activo, t agrupado
por día). Modelo: HistGradientBoosting; referencia simple: regla 'volumen y volatilidad disparados'.
Uso: python3 tools/precursores_subidas.py  -> datos/eventos/precursores_informe.txt
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score
from sklearn.inspection import permutation_importance

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_historico import load_panel, cluster_t  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "datos" / "eventos"
HZ = 4


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


def build(panel):
    btc = panel["BTC"].close
    parts = []
    for a, d in panel.items():
        d = d[d.index >= d.close.first_valid_index() + pd.Timedelta(days=60)]
        f = features(d, btc)
        f["fwd"] = 100 * (d.close.shift(-HZ) / d.open.shift(-1) - 1)
        f["activo"] = a
        parts.append(f)
    X = pd.concat(parts)
    X["breadth3"] = X.groupby(level=0).ret3.transform(lambda s: (s > 0).mean())
    return X.dropna(subset=["ret72", "vol_z", "range_ratio6", "rv_ratio", "dist_hi168", "btc6", "fwd"])


def econ(sub, score_col, top, cost_list=(1.1, 0.5)):
    """Rentabilidad de entrar en las horas de mayor puntuación (sin solapes: 1 entrada por activo cada HZ horas)."""
    thr = sub[score_col].quantile(1 - top)
    s = sub[sub[score_col] >= thr].sort_values(["activo"]).copy()
    s["ts"] = s.index
    keep = []
    for a, g in s.groupby("activo"):
        last = None
        for t in g.sort_values("ts").ts:
            if last is None or (t - last) >= pd.Timedelta(hours=HZ):
                keep.append((a, t))
                last = t
    idx = pd.MultiIndex.from_tuples(keep)
    e = s.set_index(["activo", "ts"]).loc[idx]
    day = e.index.get_level_values(1).strftime("%Y-%m-%d")
    m, t = cluster_t(e.fwd, day)
    return len(e), m, t, e.fwd.median(), (e.fwd > 0).mean() * 100


def main():
    panel, _ = load_panel("USD")
    X = build(panel)
    cols = [c for c in X.columns if c not in ("fwd", "activo")]
    X["y5"] = (X.fwd >= 5).astype(int)
    X["y10"] = (X.fwd >= 10).astype(int)
    tr = X[X.index < "2022-01-01"]
    va = X[(X.index >= "2022-01-01") & (X.index < "2023-01-01")]
    te = X[X.index >= "2023-01-01"]
    L = [f"Filas: {len(X):,} (train {len(tr):,} · val {len(va):,} · test {len(te):,}) · activos {X.activo.nunique()}",
         f"Tasa base test: >= 5 % en 4 h: {te.y5.mean()*100:.2f} % · >= 10 % en 4 h: {te.y10.mean()*100:.3f} %",
         f"Rentabilidad media de una hora cualquiera del test (+4 h, entrada apertura siguiente): {te.fwd.mean():+.3f} % (mediana {te.fwd.median():+.3f})", ""]
    imp_out = None
    for lab in ("y5", "y10"):
        rng = np.random.RandomState(0)
        trn = tr[(tr[lab] == 1) | (rng.rand(len(tr)) < 0.15)]
        m = HistGradientBoostingClassifier(max_depth=4, learning_rate=0.06, max_iter=250, l2_regularization=1.0, random_state=0)
        m.fit(trn[cols], trn[lab])
        for nm, sub in (("val", va), ("test", te)):
            sub = sub.copy()
            sub["p"] = m.predict_proba(sub[cols])[:, 1]
            auc = roc_auc_score(sub[lab], sub.p)
            L.append(f"== Modelo {lab} · {nm}: AUC {auc:.3f} ==")
            for top in (0.02, 0.005, 0.001):
                k = sub[sub.p >= sub.p.quantile(1 - top)]
                prec = k[lab].mean() * 100
                base = sub[lab].mean() * 100
                n, mm, t, med, pos = econ(sub, "p", top)
                L.append(f"  top {top*100:.1f} % horas: precisión {prec:.2f} % vs base {base:.2f} % (x{prec/base:.1f}) · entradas sin solape {n} · "
                         f"bruto medio {mm:+.2f} % (mediana {med:+.2f}, {pos:.0f} % >0, t {t:+.1f}) · neto1,1 {mm-1.1:+.2f} · neto0,5 {mm-0.5:+.2f}")
            if nm == "test" and lab == "y5":
                s5 = sub.sample(60000, random_state=1)
                pi = permutation_importance(m, s5[cols], s5[lab], scoring="roc_auc", n_repeats=3, random_state=0)
                imp_out = sorted(zip(cols, pi.importances_mean), key=lambda z: -z[1])[:8]
        L.append("")
    L.append("== Rasgos más importantes (test, modelo 5 %; caída de AUC al barajar) ==")
    L += [f"  {c}: {v:.4f}" for c, v in imp_out]
    # referencia simple
    L += ["", "== Regla simple en TEST: volumen >= 5x mediana y rango de la hora >= 3x el normal y cierre en el 25 % superior de la vela =="]
    r = te[(te.vol_z >= 5) & (te.range_last >= 3) & (te.close_pos >= 0.75)].copy()
    r["s"] = 1.0
    if len(r) > 20:
        n, mm, t, med, pos = econ(r, "s", 1.0)
        L.append(f"  entradas sin solape {n}: bruto {mm:+.2f} % (mediana {med:+.2f}, {pos:.0f} % >0, t {t:+.1f}) · neto1,1 {mm-1.1:+.2f} · neto0,5 {mm-0.5:+.2f}")
    txt = "\n".join(L)
    (OUT / "precursores_informe.txt").write_text(txt)
    print(txt)


if __name__ == "__main__":
    main()
