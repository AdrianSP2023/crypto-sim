"""Genera datos/eventos/horas_modelo.csv: horas de TEST (2023-2026) que el modelo de precursores puntúa por encima del umbral
del 0,5 % superior de VALIDACIÓN (2022), sin solapes por activo (4 h). Selección hecha solo con información previa a la hora.
Columnas: asset, quote, t_utc (inicio de la vela de 1 h que dispara), p, fwd_4h_pct (resultado, solo para análisis)."""
import sys
sys.path.insert(0, "tools")
import numpy as np, pandas as pd
import precursores_subidas as P
from sklearn.ensemble import HistGradientBoostingClassifier

panel, _ = P.load_panel("USD")
X = P.build(panel)
cols = [c for c in X.columns if c not in ("fwd", "activo")]
X["y5"] = (X.fwd >= 5).astype(int)
tr = X[X.index < "2022-01-01"]; va = X[(X.index >= "2022-01-01") & (X.index < "2023-01-01")].copy(); te = X[X.index >= "2023-01-01"].copy()
rng = np.random.RandomState(0); trn = tr[(tr.y5 == 1) | (rng.rand(len(tr)) < 0.15)]
m = HistGradientBoostingClassifier(max_depth=4, learning_rate=0.06, max_iter=250, l2_regularization=1.0, random_state=0).fit(trn[cols], trn.y5)
va["p"] = m.predict_proba(va[cols])[:, 1]; te["p"] = m.predict_proba(te[cols])[:, 1]
thr = va.p.quantile(0.995)
s = te[te.p >= thr].copy(); s["ts"] = s.index
rows = []
for a, g in s.groupby("activo"):
    last = None
    for t, p, f in zip(g.ts, g.p, g.fwd):
        if last is None or (t - last) >= pd.Timedelta(hours=4):
            rows.append((a, "USD", t.strftime("%Y-%m-%d %H:%M"), round(p, 3), round(f, 2))); last = t
df = pd.DataFrame(rows, columns=["asset", "quote", "t_utc", "p", "fwd_4h_pct"]).sort_values("t_utc")
df.to_csv("datos/eventos/horas_modelo.csv", index=False)
print(len(df), df.asset.nunique(), "umbral", round(thr, 3))
