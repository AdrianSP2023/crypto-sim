"""Estrategia propuesta por Maestro (29/09), probada SIN sesgo sobre TODAS las horas (velas 1 h Kraken USD, 42 activos, 2018-2026):
 1) Entrada: el cierre está >= R (5 %) sobre el mínimo de las 4 h previas -> compra a la apertura siguiente.
 2) Salida: trailing stop de x % bajo el máximo desde la entrada (stop antes que máximo dentro de la misma vela; hueco = apertura).
 3) Tras vender a s: espera a que caiga otro x % (mínimo <= s(1-x)); cuando rebota x % desde ese mínimo (cierre >= mínimo(1+x))
    recompra a la apertura siguiente y repite (trailing x %). Si en 24 h no ha caído x % extra, vuelve a esperar disparo 1).
Se mide rentabilidad por operación (bruta y neta de 1,1 %/0,5 % por ida y vuelta), nº de operaciones, y la curva compuesta
por activo (reparto igual entre activos: media de las rentabilidades compuestas). Las variantes son x = 1, 2, 3, 5 %; R = 5 %.
Uso: python3 tools/simula_trailing.py -> datos/eventos/trailing_informe.txt
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_historico import load_panel, cluster_t  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def run(o, h, l, c, rmin, R, x, wait=24, reentry=True):
    n = len(o)
    trades = []          # (i_entrada, i_salida, entrada, salida)
    st, i = 0, 1
    while i < n - 1:
        if st == 0:
            if not np.isnan(rmin[i]) and c[i] / rmin[i] - 1 >= R and not np.isnan(o[i + 1]):
                e, ei, peak, st = o[i + 1], i + 1, o[i + 1], 1
                i += 1
                continue
        elif st == 1:
            stop = peak * (1 - x)
            if l[i] <= stop:
                s = min(o[i], stop)
                trades.append((ei, i, e, s)); st, last_s, trough, t0 = 2, s, l[i], i
                i += 1
                continue
            peak = max(peak, h[i])
            if c[i] <= peak * (1 - x):
                s = c[i]
                trades.append((ei, i, e, s)); st, last_s, trough, t0 = 2, s, l[i], i
        elif st == 2:
            trough = min(trough, l[i])
            if trough <= last_s * (1 - x):
                if c[i] >= trough * (1 + x) and not np.isnan(o[i + 1]):
                    e, ei, peak, st = o[i + 1], i + 1, o[i + 1], 1
                    i += 1
                    continue
            elif i - t0 >= wait:
                st = 0
        i += 1
    if st == 1 and not np.isnan(c[-1]):
        trades.append((ei, n - 1, e, c[-1]))
    return trades


XS = tuple(float(v) for v in sys.argv[1].split(",")) if len(sys.argv) > 1 else (0.01, 0.02, 0.03, 0.05)


def main():
    panel, _ = load_panel("USD")
    L = ["Disparo de entrada: cierre >= +5 % sobre el mínimo de 4 h. Todas las horas, 42 activos USD, 2018-2026 (desde 60 días tras el listado).", ""]
    res = {}
    for x in XS:
        allr, per = [], []
        years = {}
        for a, d in panel.items():
            d = d[d.index >= d.close.first_valid_index() + pd.Timedelta(days=60)]
            o, h, l, c = [d[k].to_numpy(float) for k in ("open", "high", "low", "close")]
            rmin = d.low.rolling(4).min().shift(1).to_numpy()
            tr = run(o, h, l, c, rmin, 0.05, x)
            if not tr:
                continue
            g = np.array([100 * (s / e - 1) for (_, _, e, s) in tr])
            days = [d.index[j].strftime("%Y-%m-%d") for (_, j, _, _) in tr]
            allr += list(zip(g, days, [d.index[j].year for (_, j, _, _) in tr], [a] * len(g)))
            span = (d.index[-1] - d.index[0]).days
            per.append((a, len(g), span))
        df = pd.DataFrame(allr, columns=["g", "day", "year", "a"])
        m, t = cluster_t(df.g, df.day)
        tot_days = sum(p[2] for p in per)
        L.append(f"== Trailing x = {int(x*100)} % · operaciones {len(df)} ({len(df)/tot_days:.2f} por activo-día) ==")
        L.append(f"  por operación: bruto medio {m:+.3f} % (mediana {df.g.median():+.2f}, {100*(df.g>0).mean():.0f} % ganadoras, t agrupado {t:+.1f}) · neto 1,1 % {m-1.1:+.3f} · neto 0,5 % {m-0.5:+.3f}")
        L.append(f"  retorno bruto sumado por activo y año (media, %): " + " ".join(f"{y}: {g.g.sum()/g.a.nunique():+.0f}" for y, g in df.groupby('year')))
        L.append(f"  neto 0,5 % sumado por activo y año: " + " ".join(f"{y}: {(g.g-0.5).sum()/g.a.nunique():+.0f}" for y, g in df.groupby('year')))
        L.append("")
    L.append("Nota: 'sumado' = suma simple de rentabilidades por operación entre activos (sin reinversión), como orden de magnitud.")
    txt = "\n".join(L)
    (ROOT / "datos" / "eventos" / ("trailing_informe.txt" if len(XS) == 4 else "trailing_informe_amplio.txt")).write_text(txt)
    print(txt)


if __name__ == "__main__":
    main()
