"""Subidas repentinas en ventanas de 1, 3, 6, 9, 12, 15 y 18 h (velas de 1 h Kraken, datos/historico_1h).

Evento: retorno de W horas (cierre t / cierre t-W) en el 0,5 % superior (p99,5) de ese activo y esa ventana (desde 2018).
Un evento por activo y ventana cada 24 h (sin solapes). Se ignoran los primeros 60 días de cada activo (listados nuevos con
picos irreales) y las rentabilidades se recortan al [0,1 %; 99,9 %] de TODAS las horas del mismo activo y horizonte
(evita que un solo dato extremo domine la media; el control se recorta igual). Ojo: las 7 ventanas comparten eventos
(un mismo pico aparece en varias ventanas): no son 7 pruebas independientes. Entrada: APERTURA de la hora siguiente al cierre que dispara
(el primer precio realista con velas de 1 h). Se mide la rentabilidad hasta +1, +3, +6, +12, +24 h (cierres) y se
compara con el control del mismo activo (media de TODAS las horas). Comisiones ida y vuelta 1,1 % y 0,5 %.
t agrupado por día (los activos suben a la vez). Se hacen 7 ventanas x 5 horizontes = 35 contrastes: con |t| < 3 hay
que asumir ruido. Resultados: datos/eventos/subidas_ventanas_informe.txt y subidas_ventanas_eventos.csv.
Uso: python3 tools/analisis_subidas.py [USD|EUR]
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_historico import load_panel, cluster_t  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "datos" / "eventos"
WIN = [1, 3, 6, 9, 12, 15, 18]
HOR = [1, 3, 6, 12, 24]
Q = 0.995
COSTS = (1.1, 0.5)


def events_for(d, W, q=Q):
    c = d.close
    r = c / c.shift(W) - 1
    thr = r.quantile(q)
    cond = (r >= thr) & r.notna()
    idx = np.flatnonzero(cond.to_numpy())
    keep, last = [], -10 ** 9
    for i in idx:
        if i - last >= 24:
            keep.append(i)
            last = i
    return keep, r.to_numpy(), thr


def forward(d, i, H):
    o = d.open.to_numpy(); cl = d.close.to_numpy()
    if i + 1 + H >= len(d):
        return np.nan
    e = o[i + 1]
    if np.isnan(e) or np.isnan(cl[i + H]):
        return np.nan
    return 100 * (cl[i + H] / e - 1)


def build(panel):
    rows, ctrl, bounds = [], {}, {}
    for a, d in panel.items():
        d = d[d.index >= d.close.first_valid_index() + pd.Timedelta(days=60)]
        c = d.close.to_numpy(); o = d.open.to_numpy()
        for H in HOR:
            f = 100 * (pd.Series(c).shift(-H) / pd.Series(o).shift(-1) - 1)
            lo, hi = f.quantile(0.001), f.quantile(0.999)
            bounds[(a, H)] = (lo, hi)
            ctrl[(a, H)] = f.clip(lo, hi).mean()
        for W in WIN:
            keep, r, thr = events_for(d, W)
            for i in keep:
                row = {"activo": a, "W": W, "t_utc": d.index[i].strftime("%Y-%m-%d %H:%M"), "ret_W_pct": 100 * r[i],
                       "umbral_pct": 100 * thr, "anio": d.index[i].year}
                for H in HOR:
                    lo, hi = bounds[(a, H)]
                    row[f"h{H}"] = float(np.clip(forward(d, i, H), lo, hi))
                    row[f"ctrl{H}"] = ctrl[(a, H)]
                rows.append(row)
    return pd.DataFrame(rows)


def report(df):
    L = []
    P = L.append
    P(f"Eventos totales: {len(df)} · activos: {df.activo.nunique()} · p{Q*100:.1f} por activo y ventana, cooldown 24 h")
    P("Contrastes: 7 ventanas x 5 horizontes = 35; con |t| < 3 tratar como ruido.\n")
    P("== Umbral mediano (retorno en W h que define 'subida repentina') y nº de eventos ==")
    for W in WIN:
        g = df[df.W == W]
        P(f"W={W:>2d} h: umbral mediano {g.umbral_pct.median():5.1f} % · eventos {len(g):4d} · retorno medio del evento {g.ret_W_pct.mean():5.1f} %")
    for label, sub in (("TODO 2018-2026", df), ("2018-2021", df[df.anio <= 2021]), ("2022-2026", df[df.anio >= 2022])):
        P(f"\n== {label}: rentabilidad tras entrar a la apertura siguiente, EXCESO sobre el control (% medio | mediana | t agrupado) ==")
        P(f"{'W':>4s} {'n':>5s} " + " ".join(f"{'+'+str(h)+'h':>26s}" for h in HOR))
        for W in WIN:
            g = sub[sub.W == W]
            day = pd.to_datetime(g.t_utc).dt.strftime("%Y-%m-%d")
            cells = []
            for H in HOR:
                x = g[f"h{H}"] - g[f"ctrl{H}"]
                m, t = cluster_t(x, day)
                cells.append(f"{m:+6.2f} | {x.median():+6.2f} | t{t:+5.1f}")
            P(f"{W:>3d}h {len(g):>5d} " + " ".join(f"{c:>26s}" for c in cells))
    P("\n== Rentabilidad BRUTA y NETA (1,1 % / 0,5 %) por ventana, horizonte +6 h y +24 h (media | t agrupado) ==")
    for W in WIN:
        g = df[df.W == W]
        day = pd.to_datetime(g.t_utc).dt.strftime("%Y-%m-%d")
        parts = []
        for H in (6, 24):
            m, t = cluster_t(g[f"h{H}"], day)
            parts.append(f"+{H}h bruta {m:+5.2f} (t{t:+4.1f}) neta1,1 {m-1.1:+5.2f} neta0,5 {m-0.5:+5.2f}")
        P(f"W={W:>2d}h: " + " · ".join(parts))
    P("\n== Continuación vs reversión: % de eventos con retorno >0 a +6 h y a +24 h ==")
    for W in WIN:
        g = df[df.W == W]
        P(f"W={W:>2d}h: +6h {100*(g.h6>0).mean():3.0f} % · +24h {100*(g.h24>0).mean():3.0f} % (control: ~50 %)")
    return "\n".join(L)


def main(quote="USD"):
    panel, dropped = load_panel(quote)
    df = build(panel)
    OUT.mkdir(exist_ok=True)
    df.to_csv(OUT / "subidas_ventanas_eventos.csv", index=False)
    txt = f"Panel {quote}: {len(panel)} activos líquidos (descartados: {len(dropped)})\n" + report(df)
    (OUT / "subidas_ventanas_informe.txt").write_text(txt)
    print(txt)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "USD")
