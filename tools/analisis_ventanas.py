"""Estudio de ventanas de 1 min alrededor de los desplomes (>= 12 % en 4 h).

Datos: datos/ventanas_1m/<QUOTE>_<ACTIVO>.csv.gz (velas de 1 min desde t-4 h hasta t+9 h de cada evento; t = inicio de
la vela de 1 h del evento) y datos/eventos/desplomes_4h_12pct.csv.

Qué mide (un bot que mira la vela de 1 min, no la de 1 h):
 - Minuto de disparo: primer minuto cuyo cierre está >= 12 % por debajo del precio de referencia (cierre 4 h antes).
 - Entrada al ABRIR el minuto siguiente + un retraso d (0, 1, 5, 15, 30, 60 min) -> precio de entrada realista.
 - Rentabilidad a +1, +2, +4 y +6 h desde la entrada, sin salida activa.
 - Rejilla de take-profit / stop-loss simulada minuto a minuto (stop antes que TP dentro de un minuto: conservador;
   si el minuto abre ya más allá del nivel, se sale a la apertura).
 - Se restan comisiones de ida y vuelta 1,1 % (tramo inicial de Bit2Me [Suposición]) y 0,5 % (tramo alto).
Reglas: un evento por activo cada 24 h (se prefiere EUR), errores estándar agrupados por día, sin relleno de huecos
salvo arrastrar el último cierre dentro de la ventana (un minuto sin trades no tiene precio nuevo).

Uso: python3 tools/analisis_ventanas.py
"""
import glob
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_historico import cluster_t  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
EV = ROOT / "datos" / "eventos" / "desplomes_4h_12pct.csv"
VDIR = ROOT / "datos" / "ventanas_1m"
OUTDIR = ROOT / "datos" / "eventos"
DELAYS = [0, 1, 5, 15, 30, 60]
HORIZ = [60, 120, 240, 360]           # minutos
TPS = [0.02, 0.03, 0.05, 0.08, 0.12]
SLS = [None, 0.02, 0.03, 0.05, 0.08]
COSTS = (0.011, 0.005)
TRIGGER = -0.12


def simulate(o, h, l, c, i0, tp, sl, n_max):
    """Compra al ABRIR la vela i0; recorre hasta n_max velas. Devuelve (rentabilidad bruta, motivo, velas)."""
    e = o[i0]
    end = min(len(o) - 1, i0 + n_max)
    for j in range(i0, end + 1):
        if sl is not None and l[j] <= e * (1 - sl):
            return min(o[j], e * (1 - sl)) / e - 1, "stop", j - i0
        if tp is not None and h[j] >= e * (1 + tp):
            return max(o[j], e * (1 + tp)) / e - 1, "tp", j - i0
    return c[end] / e - 1, "timeout", end - i0


def events(path=EV):
    ev = pd.read_csv(path)
    ev["ts"] = ((pd.to_datetime(ev.t_utc, utc=True) - pd.Timestamp("1970-01-01", tz="UTC")) // pd.Timedelta(seconds=1)).astype("int64")
    ev["pref"] = (ev.quote != "EUR").astype(int)
    ev = ev.sort_values(["asset", "ts", "pref"]).reset_index(drop=True)
    keep, last = [], {}
    for k, r in ev.iterrows():
        if r.asset in last and r.ts < last[r.asset] + 24 * 3600:
            continue
        last[r.asset] = r.ts
        keep.append(k)
    return ev.loc[keep].reset_index(drop=True)


def analyse(vdir=VDIR, evpath=EV, pre=4 * 3600, post=9 * 3600):
    ev = events(evpath)
    rows, checks, skipped = [], [], 0
    cache = {}
    for _, r in ev.iterrows():
        f = Path(vdir) / f"{r.quote}_{r.asset}.csv.gz"
        if not f.exists():
            skipped += 1
            continue
        if f not in cache:
            cache[f] = pd.read_csv(f)
        d = cache[f]
        t0, t1 = int(r.ts) - pre, int(r.ts) + post
        w = d[(d.time >= t0) & (d.time < t1)]
        if w.empty:
            skipped += 1
            continue
        idx = np.arange(t0, t1, 60)
        w = w.set_index("time").reindex(idx)
        c = w.close.ffill().to_numpy(float)
        o = w.open.fillna(w.close.ffill().shift(1)).fillna(w.close.ffill()).to_numpy(float)
        h = w.high.fillna(w.close.ffill()).to_numpy(float)
        l = w.low.fillna(w.close.ffill()).to_numpy(float)
        if np.isnan(c).all():
            skipped += 1
            continue
        # comprobación cruzada: el cierre de la vela de 1 h del evento debe coincidir con close_evento
        k_end = int((r.ts + 3600 - t0) // 60) - 1
        checks.append(c[k_end] / r.close_evento - 1)
        ref = r.close_pre4h
        k_from = int((r.ts - 3 * 3600 - t0) // 60)
        trig = np.where(c[k_from:] / ref - 1 <= TRIGGER)[0]
        if len(trig) == 0:
            skipped += 1
            continue
        m = k_from + int(trig[0])
        row = {"quote": r.quote, "asset": r.asset, "t_utc": r.t_utc, "drop_4h_pct": r.drop_4h_pct,
               "disparo_min_desde_t": int((t0 + m * 60 - r.ts) // 60), "precio_disparo": c[m],
               "cierre_hora": r.close_evento}
        for dl in DELAYS:
            i0 = m + 1 + dl
            if i0 + HORIZ[-1] >= len(o):
                for k in ("entrada", "vs_hora"):
                    row[f"d{dl}_{k}"] = np.nan
                continue
            e = o[i0]
            row[f"d{dl}_entrada"] = e
            row[f"d{dl}_vs_hora"] = 100 * (e / r.close_evento - 1)
            for hz in HORIZ:
                row[f"d{dl}_ret{hz}"] = 100 * (c[i0 + hz] / e - 1)
            row[f"d{dl}_mae"] = 100 * (l[i0:i0 + HORIZ[-1] + 1].min() / e - 1)
            row[f"d{dl}_mfe"] = 100 * (h[i0:i0 + HORIZ[-1] + 1].max() / e - 1)
            for tp in TPS:
                for sl in SLS:
                    g, why, _ = simulate(o, h, l, c, i0, tp, sl, HORIZ[-1])
                    row[f"d{dl}_tp{int(tp*100)}_sl{'x' if sl is None else int(sl*100)}"] = 100 * g
        rows.append(row)
    return pd.DataFrame(rows), np.array(checks), skipped, len(ev)


def rep(df):
    L = []
    P = L.append
    n = len(df)
    P(f"Eventos analizados: {n}")
    if n == 0:
        return "\n".join(L)
    day = pd.to_datetime(df.t_utc).dt.strftime("%Y-%m-%d")
    P(f"Minuto de disparo respecto al inicio de la hora del evento: mediana {df.disparo_min_desde_t.median():.0f} min "
      f"(p10 {df.disparo_min_desde_t.quantile(.1):.0f}, p90 {df.disparo_min_desde_t.quantile(.9):.0f}); antes de la hora en punto: "
      f"{(df.disparo_min_desde_t < 0).mean()*100:.0f} %")
    P("")
    P("== Entrada realista y rebote sin salida activa (rentabilidad % desde la entrada, media | mediana | t agrupado) ==")
    P(f"{'retraso':>8s} {'entrada vs cierre 1h':>21s} " + " ".join(f"{'+'+str(h//60)+'h':>26s}" for h in HORIZ))
    for dl in DELAYS:
        vs = df[f"d{dl}_vs_hora"].dropna()
        parts = []
        for hz in HORIZ:
            x = df[f"d{dl}_ret{hz}"]
            m, t = cluster_t(x, day)
            parts.append(f"{x.mean():+6.2f} | {x.median():+6.2f} | t {t:+5.1f}")
        P(f"{dl:>6d} m {vs.mean():+10.2f}% (med {vs.median():+6.2f}) " + " ".join(f"{p:>26s}" for p in parts))
    P("")
    P("== Riesgo tras la entrada (adverso máximo MAE, favorable máximo MFE en 6 h; medianas %) ==")
    for dl in DELAYS:
        P(f"retraso {dl:>2d} m: MAE mediana {df[f'd{dl}_mae'].median():+6.2f} (p10 {df[f'd{dl}_mae'].quantile(.1):+6.2f}) · MFE mediana {df[f'd{dl}_mfe'].median():+6.2f} (p90 {df[f'd{dl}_mfe'].quantile(.9):+6.2f})")
    TPSL = "TP/SL"
    for cost in COSTS:
        P("")
        P(f"== Rejilla TP/SL, retraso 0-1 min y 5 min, NETO de comisión {cost*100:.1f} % (media % | %acierto | t agrupado) ==")
        for dl in (0, 5):
            P(f"-- retraso {dl} min --")
            P(f"{TPSL:>6s} " + " ".join(f"{('sin' if s is None else str(int(s*100))+'%'):>24s}" for s in SLS))
            for tp in TPS:
                cells = []
                for sl in SLS:
                    x = df[f"d{dl}_tp{int(tp*100)}_sl{'x' if sl is None else int(sl*100)}"] - cost * 100
                    m, t = cluster_t(x, day)
                    cells.append(f"{x.mean():+6.2f} | {100*(x>0).mean():3.0f}% | t{t:+5.1f}")
                P(f"{int(tp*100):>5d}% " + " ".join(f"{c:>24s}" for c in cells))
    P("")
    P("== Solo desplomes >= 20 % (retraso 0 y 5 min, sin salida activa, neto 1,1 %) ==")
    big = df[df.drop_4h_pct <= -20]
    dbig = pd.to_datetime(big.t_utc).dt.strftime("%Y-%m-%d")
    P(f"n = {len(big)}")
    for dl in (0, 5, 15):
        parts = []
        for hz in HORIZ:
            x = big[f"d{dl}_ret{hz}"] - 1.1
            m, t = cluster_t(x, dbig)
            parts.append(f"+{hz//60}h {x.mean():+6.2f} (med {x.median():+6.2f}, t {t:+4.1f})")
        P(f"retraso {dl:>2d} m: " + " · ".join(parts))
    return "\n".join(L)


def main():
    df, checks, skipped, nev = analyse()
    OUTDIR.mkdir(exist_ok=True)
    df.to_csv(OUTDIR / "ventanas_eventos.csv", index=False)
    head = [f"Estudio de ventanas 1 min · eventos tras cooldown 24 h/activo: {nev} · sin datos o sin disparo: {skipped}"]
    if len(checks):
        head.append(f"Comprobación cruzada (cierre 1 min de la hora vs cierre 1 h del CSV): mediana |dif| {np.median(np.abs(checks))*100:.4f} %, "
                    f"máx {np.abs(checks).max()*100:.3f} %, coinciden (<0,01 %): {(np.abs(checks) < 1e-4).mean()*100:.0f} %")
    txt = "\n".join(head) + "\n\n" + rep(df)
    (OUTDIR / "ventanas_informe.txt").write_text(txt)
    print(txt)


if __name__ == "__main__":
    main()
