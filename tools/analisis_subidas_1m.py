"""Subidas >= 12 % en 4 h vistas con velas de 1 min (datos/ventanas_1m_subidas, t-10 h .. t+8 h).

AVISO DE SESGO: las ventanas se eligieron porque la subida ya ocurrió (>= 12 % en 4 h). Cualquier disparo dentro de ellas
está condicionado a que la subida llegue: los resultados son un TECHO, no una expectativa. Sirve para medir cuánto recorrido
queda a cada nivel de disparo y cuánto cuesta el retraso. La prueba sin sesgo requiere ventanas elegidas SIN mirar al futuro.
Disparo: primer minuto en que el cierre está >= X % sobre el mínimo de los 240 min anteriores (X = 3, 5, 8, 10 %).
Entrada: apertura del minuto siguiente + retraso (0, 1, 5, 15 min). Salida: a +30, +60, +120, +240 min; TP/SL simulados minuto a minuto.
Uso: python3 tools/analisis_subidas_1m.py -> datos/eventos/subidas_1m_informe.txt
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_historico import cluster_t  # noqa: E402
from analisis_ventanas import simulate  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
VDIR = ROOT / "datos" / "ventanas_1m_subidas"
EV = ROOT / "datos" / "eventos" / "subidas_4h_12pct.csv"
XS = [0.03, 0.05, 0.08, 0.10]
DELAYS = [0, 1, 5, 15]
HZ = [30, 60, 120, 240]


def main():
    ev = pd.read_csv(EV)
    ev["ts"] = ((pd.to_datetime(ev.t, utc=True) - pd.Timestamp("1970-01-01", tz="UTC")) // pd.Timedelta(seconds=1)).astype("int64")
    ev = ev.sort_values(["asset", "ts"])
    keep, last = [], {}
    for k, r in ev.iterrows():
        if r.asset in last and r.ts < last[r.asset] + 24 * 3600:
            continue
        last[r.asset] = r.ts
        keep.append(k)
    ev = ev.loc[keep]
    rows, cache = [], {}
    for _, r in ev.iterrows():
        f = VDIR / f"{r.quote}_{r.asset}.csv.gz"
        if not f.exists():
            continue
        if f not in cache:
            cache[f] = pd.read_csv(f)
        d = cache[f]
        t0, t1 = int(r.ts) - 10 * 3600, int(r.ts) + 8 * 3600
        w = d[(d.time >= t0) & (d.time < t1)]
        if len(w) < 60:
            continue
        idx = np.arange(t0, t1, 60)
        w = w.set_index("time").reindex(idx)
        c = w.close.ffill().to_numpy(float)
        o = w.open.fillna(w.close.ffill().shift(1)).fillna(w.close.ffill()).to_numpy(float)
        h = w.high.fillna(w.close.ffill()).to_numpy(float)
        l = w.low.fillna(w.close.ffill()).to_numpy(float)
        if np.isnan(c).any():
            c = pd.Series(c).bfill().to_numpy()
            o, h, l = [pd.Series(x).bfill().to_numpy() for x in (o, h, l)]
        runmin = pd.Series(l).rolling(240, min_periods=60).min().shift(1).to_numpy()
        base = {"asset": r.asset, "quote": r.quote, "t": r.t, "day": str(r.t)[:10]}
        for X in XS:
            trig = np.where(c / runmin - 1 >= X)[0]
            trig = trig[trig >= 240]
            if len(trig) == 0:
                continue
            m = int(trig[0])
            for dl in DELAYS:
                i0 = m + 1 + dl
                if i0 + 240 >= len(o):
                    continue
                e = o[i0]
                row = dict(base, X=X, delay=dl, min_desde_t=(t0 + m * 60 - r.ts) / 60, ya_subido=100 * (e / runmin[m] - 1))
                for hz in HZ:
                    row[f"r{hz}"] = 100 * (c[i0 + hz] / e - 1)
                for tp, sl in ((0.03, 0.02), (0.05, 0.03), (0.08, 0.04), (0.05, None), (0.08, None)):
                    g, _, _ = simulate(o, h, l, c, i0, tp, sl, 240)
                    row[f"tp{int(tp*100)}_sl{'x' if sl is None else int(sl*100)}"] = 100 * g
                rows.append(row)
    df = pd.DataFrame(rows)
    df.to_csv(ROOT / "datos" / "eventos" / "subidas_1m_eventos.csv", index=False)
    L = [f"Eventos usados: {ev.shape[0]} tras cooldown 24 h/activo · filas de disparo: {len(df)}",
         "TECHO por sesgo de selección (las ventanas se eligieron porque la subida ocurrió).", ""]
    for X in XS:
        g0 = df[(df.X == X) & (df.delay == 0)]
        L.append(f"== Disparo +{int(X*100)} % sobre el mínimo de 4 h · n={len(g0)} · ya subido al entrar (retraso 0): mediana {g0.ya_subido.median():.1f} % ==")
        L.append(f"{'retraso':>8s} " + " ".join(f"{'+'+str(h)+'m':>24s}" for h in HZ))
        for dl in DELAYS:
            g = df[(df.X == X) & (df.delay == dl)]
            cells = []
            for hz in HZ:
                m, t = cluster_t(g[f"r{hz}"], g.day)
                cells.append(f"{m:+6.2f} | {g[f'r{hz}'].median():+6.2f} | t{t:+5.1f}")
            L.append(f"{dl:>6d} m " + " ".join(f"{c:>24s}" for c in cells))
        L.append("  TP/SL (retraso 0, neto 1,1 % | 0,5 %): " + " · ".join(
            f"{k}: {g0[k].mean()-1.1:+.2f}|{g0[k].mean()-0.5:+.2f}" for k in ("tp3_sl2", "tp5_sl3", "tp8_sl4", "tp5_slx", "tp8_slx")))
        L.append("")
    txt = "\n".join(L)
    (ROOT / "datos" / "eventos" / "subidas_1m_informe.txt").write_text(txt)
    print(txt)


if __name__ == "__main__":
    main()
