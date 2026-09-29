"""Entrena el modelo de precursores con la MISMA receta validada (entrena 2018-2021, umbral = p99,5 de 2022) y lo guarda en
modelo/modelo.joblib y modelo/meta.json. Se ejecuta fuera de Actions (necesita datos/historico_1h). Uso: python3 modelo/entrenar.py"""
import json
import sys
from pathlib import Path

import joblib
import numpy as np
import sklearn
from sklearn.ensemble import HistGradientBoostingClassifier

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT))
import precursores_subidas as P  # noqa: E402
from modelo.features import COLS  # noqa: E402


def main():
    panel, _ = P.load_panel("USD")
    X = P.build(panel)
    assert [c for c in X.columns if c not in ("fwd", "activo")] == COLS, "las columnas del entrenamiento no coinciden con modelo/features.py"
    X["y5"] = (X.fwd >= 5).astype(int)
    tr = X[X.index < "2022-01-01"]
    va = X[(X.index >= "2022-01-01") & (X.index < "2023-01-01")]
    rng = np.random.RandomState(0)
    trn = tr[(tr.y5 == 1) | (rng.rand(len(tr)) < 0.15)]
    m = HistGradientBoostingClassifier(max_depth=4, learning_rate=0.06, max_iter=250, l2_regularization=1.0, random_state=0)
    m.fit(trn[COLS], trn.y5)
    thr = float(np.quantile(m.predict_proba(va[COLS])[:, 1], 0.995))
    joblib.dump(m, ROOT / "modelo" / "modelo.joblib", compress=3)
    meta = {"sklearn": sklearn.__version__, "umbral": thr, "columnas": COLS, "activos": sorted(panel.keys()),
            "entrenado_hasta": "2021-12-31", "umbral_de": "p99,5 de 2022", "filas_train": int(len(trn))}
    (ROOT / "modelo" / "meta.json").write_text(json.dumps(meta, indent=1))
    print(meta["umbral"], len(meta["activos"]), meta["sklearn"])


if __name__ == "__main__":
    main()
