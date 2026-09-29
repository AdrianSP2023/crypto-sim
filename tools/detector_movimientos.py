"""Detector automático de los mayores movimientos de 24 h por activo (histórico Kraken USD, velas de 1 h).

Para cada activo: los N mayores retornos de 24 h al alza y a la baja, sin solapes (±72 h entre movimientos del mismo
sentido y activo), desde 2018 o desde 30 días tras la primera vela del activo. El 'cierre de ventana' es el instante en
que se completa el movimiento; la noticia que lo causó suele estar en las 24 h ANTERIORES a esa hora.
Uso: python3 tools/detector_movimientos.py [N=8]  -> datos/eventos/detector_top_movimientos.csv
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ["BTC", "ETH", "XRP", "SOL", "DOGE", "ADA", "LINK", "LTC", "XLM", "DOT"]


def top_moves(s, n, start):
    r = (s / s.reindex(s.index - pd.Timedelta(hours=24)).to_numpy() - 1).dropna()
    r = r[r.index >= start]
    out = []
    for sign in (1, -1):
        cand = r[r * sign > 0].abs().sort_values(ascending=False)
        chosen = []
        for t, _ in cand.items():
            if all(abs((t - c).total_seconds()) > 72 * 3600 for c in chosen):
                chosen.append(t)
            if len(chosen) == n:
                break
        out += [(t, float(r[t] * 100)) for t in chosen]
    return out


def load(a, quote="USD"):
    """Cierres horarios indexados por el instante de cierre de la vela (inicio + 1 h)."""
    d = pd.read_csv(ROOT / "datos" / "historico_1h" / f"{quote}_{a}.csv.gz", usecols=["time", "close"])
    s = pd.Series(d.close.to_numpy(float), index=pd.to_datetime(d.time + 3600, unit="s"))
    return s[~s.index.duplicated()].sort_index()


def main(n=8):
    P = {a: load(a) for a in ASSETS}
    cat = pd.read_csv(ROOT / "datos" / "eventos" / "catalogo_eventos.csv")
    rows = []
    for a in ASSETS:
        s = P[a]
        start = max(pd.Timestamp("2018-01-01"), s.index[0] + pd.Timedelta(days=30))
        for k, (t, ret) in enumerate(sorted(top_moves(s, n, start), key=lambda x: -abs(x[1]))):
            near = cat[(pd.to_datetime(cat.fecha_utc) - t.normalize()).abs() <= pd.Timedelta(days=3)]
            rows.append({"activo": a, "cierre_ventana_utc": t.strftime("%Y-%m-%d %H:%M"),
                         "inicio_ventana_utc": (t - pd.Timedelta(hours=24)).strftime("%Y-%m-%d %H:%M"),
                         "ret_24h_pct": round(ret, 1), "sentido": "subida" if ret > 0 else "bajada",
                         "precio_cierre_usd": float(s.loc[t]), "en_catalogo": bool(len(near)),
                         "evento_catalogo": "; ".join(sorted(set(near.evento))[:2])})
    df = pd.DataFrame(rows)
    (ROOT / "datos" / "eventos").mkdir(exist_ok=True)
    df.to_csv(ROOT / "datos" / "eventos" / "detector_top_movimientos.csv", index=False)
    print(df.groupby("activo").size().to_dict(), "· con evento del catálogo cerca:", int(df.en_catalogo.sum()), "de", len(df))
    return df


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 8)
