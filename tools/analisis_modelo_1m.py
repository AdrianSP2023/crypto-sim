"""Horas elegidas SIN sesgo por el modelo de precursores (datos/eventos/horas_modelo.csv) vistas con velas de 1 min
(datos/ventanas_1m_modelo, t-2 h .. t+8 h; t = inicio de la vela de 1 h que dispara; el modelo decide al cierre de esa hora, t+60 min).
Compara formas de ENTRAR y SALIR dentro de la hora usando solo información previa a cada decisión:
 - referencia: comprar a la apertura de t+60 min y vender a +240 min (equivale al +1,8 % bruto del estudio horario)
 - retraso 1/5/15 min
 - limit de compra a -p % de la apertura, válido 30/60 min (si no se ejecuta, no hay operación; se informa el % de ejecución)
 - confirmación: comprar cuando el precio supera el máximo de los primeros k minutos
 - TP/SL minuto a minuto, tiempo máximo 240 min
Neto de 1,1 % y 0,5 %; t agrupado por día; por año; sin los 10 mejores días.
Uso: python3 tools/analisis_modelo_1m.py -> datos/eventos/modelo_1m_informe.txt
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_historico import cluster_t  # noqa: E402
from analisis_ventanas import simulate  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
VDIR = ROOT / "datos" / "ventanas_1m_modelo"
EV = ROOT / "datos" / "eventos" / "horas_modelo.csv"
HOLD = 240


def load_events():
    ev = pd.read_csv(EV)
    ev["ts"] = ((pd.to_datetime(ev.t_utc, utc=True) - pd.Timestamp("1970-01-01", tz="UTC")) // pd.Timedelta(seconds=1)).astype("int64")
    return ev


def arrays(d, t0, t1):
    w = d[(d.time >= t0) & (d.time < t1)]
    if len(w) < 30:
        return None
    w = w.set_index("time").reindex(np.arange(t0, t1, 60))
    c = w.close.ffill().bfill()
    o = w.open.fillna(c.shift(1)).fillna(c)
    h = w.high.fillna(c); l = w.low.fillna(c)
    return [x.to_numpy(float) for x in (o, h, l, c)]


def main():
    ev = load_events()
    cache, rows = {}, []
    for _, r in ev.iterrows():
        f = VDIR / f"{r.quote}_{r.asset}.csv.gz"
        if not f.exists():
            continue
        if f not in cache:
            cache[f] = pd.read_csv(f)
        t0, t1 = int(r.ts), int(r.ts) + 8 * 3600      # desde el inicio de la hora que dispara
        A = arrays(cache[f], t0, t1)
        if A is None:
            continue
        o, h, l, c = A
        i_dec = 60                                       # minuto de decisión: cierre de la hora del disparo
        if i_dec + 1 + HOLD + 15 >= len(o):
            continue
        row = {"asset": r.asset, "t": r.t_utc, "day": r.t_utc[:10], "year": int(r.t_utc[:4]), "hor_fwd": r.fwd_4h_pct}
        for dl in (0, 1, 5, 15):
            e = o[i_dec + dl]
            row[f"ref_d{dl}"] = 100 * (c[i_dec + dl + HOLD] / e - 1)
        e0 = o[i_dec]
        for p in (0.005, 0.01, 0.02):
            for win in (30, 60):
                seg = l[i_dec:i_dec + win]
                hit = np.where(seg <= e0 * (1 - p))[0]
                if len(hit):
                    k = i_dec + int(hit[0])
                    e = min(o[k], e0 * (1 - p))
                    row[f"lim{int(p*1000)}_{win}"] = 100 * (c[i_dec + HOLD] / e - 1)   # sale en el mismo instante que la referencia
                else:
                    row[f"lim{int(p*1000)}_{win}"] = np.nan
        for kk in (5, 15):
            mx = h[i_dec:i_dec + kk].max()
            seg = h[i_dec + kk:i_dec + 60]
            hit = np.where(seg > mx)[0]
            if len(hit):
                k = i_dec + kk + int(hit[0])
                e = max(o[k], mx)
                row[f"brk{kk}"] = 100 * (c[i_dec + HOLD] / e - 1)
            else:
                row[f"brk{kk}"] = np.nan
        for tp, sl in ((0.03, 0.02), (0.05, 0.03), (0.08, 0.04), (0.05, None), (0.08, None), (None, 0.03), (None, 0.05)):
            g, _, _ = simulate(o, h, l, c, i_dec, tp, sl, HOLD)
            row[f"tp{'x' if tp is None else int(tp*100)}_sl{'x' if sl is None else int(sl*100)}"] = 100 * g
        rows.append(row)
    df = pd.DataFrame(rows)
    df.to_csv(ROOT / "datos" / "eventos" / "modelo_1m_eventos.csv", index=False)

    def line(name, x, day, yrs):
        ok = x.notna()
        m, t = cluster_t(x[ok], day[ok])
        by = " ".join(f"{y}:{x[ok & (yrs == y)].mean():+.1f}" for y in sorted(yrs.unique()))
        best = day[ok].to_frame().assign(x=x[ok]).groupby("day").x.sum().sort_values(ascending=False)
        x2 = x[ok & ~day.isin(best.index[:10])]
        return (f"{name:<14s} n={ok.sum():4d} ({100*ok.mean():3.0f}% ejec.) bruto {m:+6.2f} (med {x[ok].median():+6.2f}, t {t:+4.1f}) "
                f"neto1,1 {m-1.1:+6.2f} neto0,5 {m-0.5:+6.2f} | sin 10 mejores días {x2.mean():+5.2f} | años {by}")

    L = [f"Horas del modelo con datos de 1 min: {len(df)} de {len(ev)} · retorno horario original (referencia +4 h): media {df.hor_fwd.mean():+.2f} %", ""]
    cols = [c for c in df.columns if c.startswith(("ref_", "lim", "brk", "tp"))]
    for c_ in cols:
        L.append(line(c_, df[c_], df.day, df.year))
    txt = "\n".join(L)
    (ROOT / "datos" / "eventos" / "modelo_1m_informe.txt").write_text(txt)
    print(txt)


if __name__ == "__main__":
    main()
