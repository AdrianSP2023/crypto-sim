"""Contraste de hipótesis con el histórico de Kraken (velas de 1 h, datos/historico_1h/).

Uso: python3 tools/analisis_historico.py [USD|EUR]

Reglas para no engañarnos:
 - Solo desde 2018 y solo activos líquidos (mediana de trades por hora suficiente).
 - No hay relleno de huecos: las horas sin trades son NaN y ningún evento las cruza.
 - Rentabilidades hacia delante desde el CIERRE de la vela que dispara el evento (optimista: en la práctica se
   entra algo después); se restan al final la comisión de ida y vuelta de 0,5 % y 1,1 %.
 - Cada evento se compara con el control del mismo activo y del mismo año (media de TODAS las horas).
 - Un evento por activo cada 24 h (sin solapes) y errores estándar agrupados por día (los activos caen a la vez).
 - Comparaciones múltiples: se avisa de cuántos contrastes se hacen.
"""
import glob
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
H = [1, 2, 4, 8, 24]


def load_panel(quote, start="2018-01-01", min_years=2.0, min_med_trades=30):
    out, dropped = {}, []
    for f in sorted(glob.glob(str(ROOT / "datos" / "historico_1h" / f"{quote}_*.csv.gz"))):
        base = os.path.basename(f).split("_", 1)[1].split(".")[0]
        d = pd.read_csv(f)
        d["t"] = pd.to_datetime(d.time, unit="s")
        d = d.set_index("t")
        d = d[d.index >= start]
        if len(d) < min_years * 8760 * 0.6 or d.trades.median() < min_med_trades:
            dropped.append(base)
            continue
        idx = pd.date_range(d.index.min(), d.index.max(), freq="h")
        out[base] = d.reindex(idx)
    return out, dropped


def cluster_t(e, groups):
    """t agrupado por día: media de e y su error estándar robusto a correlación dentro del grupo."""
    e = pd.Series(np.asarray(e, float))
    groups = pd.Series(np.asarray(groups))
    ok = e.notna()
    e, groups = e[ok].reset_index(drop=True), groups[ok].reset_index(drop=True)
    n = len(e)
    if n < 5:
        return np.nan, np.nan
    m = e.mean()
    g = (e - m).groupby(groups).sum()
    se = np.sqrt((g ** 2).sum()) / n
    return m, (m / se if se > 0 else np.nan)


def build_events(panel, kind, x, window, delay=0):
    rows = []
    for a, d in panel.items():
        c = d.close
        r = c / c.shift(window) - 1
        cond = (r <= -x / 100) if kind == "down" else (r >= x / 100)
        cond &= d.trades >= 10
        idx = np.flatnonzero(cond.to_numpy())
        last = -10 ** 9
        keep = []
        for i in idx:
            if i - last >= 24:
                keep.append(i)
                last = i
        if not keep:
            continue
        allfw = {k: (c.shift(-(delay + k)) / c.shift(-delay) - 1) for k in H}
        fw = {k: allfw[k].to_numpy() for k in H}
        yr_mean = {k: allfw[k].groupby(allfw[k].index.year).mean() for k in H}
        for i in keep:
            t = c.index[i]
            row = {"asset": a, "t": t, "year": t.year, "day": t.strftime("%Y-%m-%d"), "drop": r.iloc[i] * 100}
            ok = True
            for k in H:
                v = fw[k][i]
                row[f"f{k}"] = v * 100
                row[f"x{k}"] = (v - yr_mean[k].get(t.year, np.nan)) * 100
            rows.append(row)
    return pd.DataFrame(rows)


def table(ev, title):
    print(f"\n{title}")
    print(f"  eventos {len(ev)} · días distintos {ev.day.nunique()} · activos {ev.asset.nunique()}")
    print("  horizonte | media % | exceso vs control % | t (por día) | mediana exceso % | % >0 | exceso - 0,5 % | exceso - 1,1 %")
    for k in H:
        e = ev[f"x{k}"].dropna()
        m, t = cluster_t(e, ev.loc[e.index, "day"])
        print(f"  +{k:>2} h     | {ev[f'f{k}'].mean():7.2f} | {m:9.2f}           | {t:6.2f}      | {e.median():7.2f}          | {100*(ev[f'f{k}']>0).mean():4.0f} | {m-0.5:8.2f}       | {m-1.1:8.2f}")


def robustez(quote="USD"):
    panel, _ = load_panel(quote)
    med = {a: d.trades.median() for a, d in panel.items()}
    liquid = sorted(med, key=med.get, reverse=True)[:10]
    print(f"Panel {quote}: {len(panel)} activos. Los 10 más líquidos (trades/hora medianos): " + ", ".join(f"{a} {med[a]:.0f}" for a in liquid))
    btc = panel["BTC"]
    sma = btc.close.resample("D").last().rolling(200).mean()
    dclose = btc.close.resample("D").last()
    for x in (8, 12, 20):
        print(f"\n################ caída >= {x} % en 4 h ################")
        base = build_events(panel, "down", x, 4)
        table(base, "A) base (entrada al cierre del evento)")
        for dl in (1, 2):
            table(build_events(panel, "down", x, 4, delay=dl), f"B) entrada con {dl} h de retraso (más realista)")
        liq = base[base.asset.isin(liquid)]
        if len(liq) >= 8:
            table(liq, "C) solo los 10 activos más líquidos")
        rest = base[~base.asset.isin(liquid)]
        if len(rest) >= 8:
            table(rest, "C2) resto de activos")
        print("\nD) por año (exceso a +4 h / +24 h, media %, n):")
        print("   " + " · ".join(f"{y}: n={len(g)} {g.x4.mean():+.2f}/{g.x24.mean():+.2f}" for y, g in base.groupby("year")))
        days = pd.to_datetime(base.day).dt.normalize()
        base = base.assign(reg=[(dclose.get(d, np.nan) > sma.get(d, np.nan)) if not np.isnan(sma.get(d, np.nan)) else np.nan for d in days])
        for lab, g in base.dropna(subset=["reg"]).groupby("reg"):
            m4, t4 = cluster_t(g.x4, g.day)
            m24, t24 = cluster_t(g.x24, g.day)
            print(f"E) BTC {'sobre' if lab else 'bajo'} su SMA200: n={len(g)} · +4 h {m4:+.2f} (t {t4:.1f}) · +24 h {m24:+.2f} (t {t24:.1f})")
        f4 = base.f4.dropna()
        print(f"F) cola +4 h (retorno bruto, %): p5 {f4.quantile(.05):.1f} · p25 {f4.quantile(.25):.1f} · mediana {f4.median():.1f} · p75 {f4.quantile(.75):.1f} · media del peor 10 % {f4[f4<=f4.quantile(.10)].mean():.1f}")
        nd = base.day.nunique()
        alld = (panel["BTC"].index.max() - panel["BTC"].index.min()).days
        print(f"G) frecuencia: {len(base)} eventos en {alld/365.25:.1f} años ({len(base)/(alld/365.25):.0f} al año, en {nd/alld*100:.1f} % de los días)")
        top = base.sort_values("drop").head(8)
        print("H) los 8 mayores desplomes (fecha, activo, caída 4 h %, retorno a +4 h %, +24 h %): " + "; ".join(f"{r.day} {r.asset} {r.drop:.0f}/{r.f4:+.0f}/{r.f24:+.0f}" for r in top.itertuples()))


def main(quote="USD"):
    panel, dropped = load_panel(quote)
    print(f"Panel {quote}: {len(panel)} activos líquidos desde 2018: {', '.join(sorted(panel))}")
    print(f"Descartados por historia/liquidez: {len(dropped)}")
    btc = panel["BTC"]

    # ---------------- H3: autocorrelación
    print("\n=== H3 autocorrelación de retornos (log) por horizonte ===")
    res = {}
    for a, d in panel.items():
        r = np.log(d.close).diff()
        for lag in (1, 2, 3, 4):
            res.setdefault(lag, {})[a] = r.corr(r.shift(lag))
    for lag in (1, 2, 3, 4):
        s = pd.Series(res[lag])
        print(f"  lag {lag} h: media entre activos {s.mean():+.4f} · BTC {s['BTC']:+.4f} · activos con signo negativo {int((s<0).sum())}/{len(s)}")
    yr = []
    for y in range(2018, 2027):
        b = np.log(btc.close[btc.index.year == y]).diff()
        yr.append((y, b.corr(b.shift(1)), b.corr(b.shift(2)), b.corr(b.shift(4))))
    print("  BTC por año (lag 1, 2, 4):", "  ".join(f"{y}: {a:+.3f}/{b_:+.3f}/{c_:+.3f}" for y, a, b_, c_ in yr))
    r4 = np.log(btc.close).diff(4)[::4]
    print(f"  BTC retornos de 4 h no solapados: lag 1 = {r4.corr(r4.shift(1)):+.4f}")

    # ---------------- H1 / H2 caídas y subidas
    print("\n=== H1 caídas rápidas (retorno de 4 h <= -X %) → qué pasa después (desde el cierre del evento) ===")
    print("(contrastes: 5 umbrales x 5 horizontes x 2 lados = 50 → con 0,05 exige |t| > 3 para no contar el azar)")
    keep = {}
    for x in (3, 5, 8, 12, 20):
        ev = build_events(panel, "down", x, 4)
        keep[x] = ev
        if len(ev) >= 5:
            table(ev, f"-- caída >= {x} % en 4 h")
    print("\n=== H1b caída medida contra el máximo de 24 h (más parecida a 'cae un 20-30 %') ===")
    for x in (10, 20, 30):
        rows = []
        for a, d in panel.items():
            c, hi = d.close, d.high.rolling(24, min_periods=20).max()
            dd = c / hi - 1
            cond = (dd <= -x / 100) & (d.trades >= 10)
            last, idx = -10 ** 9, np.flatnonzero(cond.to_numpy())
            fwd = {k: (c.shift(-k) / c - 1) for k in H}
            ym = {k: fwd[k].groupby(fwd[k].index.year).mean() for k in H}
            for i in idx:
                if i - last >= 24:
                    last = i
                    t = c.index[i]
                    row = {"asset": a, "day": t.strftime("%Y-%m-%d"), "year": t.year, "drop": dd.iloc[i] * 100}
                    for k in H:
                        v = fwd[k].iloc[i]
                        row[f"f{k}"] = v * 100
                        row[f"x{k}"] = (v - ym[k].get(t.year, np.nan)) * 100
                    rows.append(row)
        ev = pd.DataFrame(rows)
        if len(ev) >= 5:
            table(ev, f"-- caída >= {x} % desde el máximo de 24 h")
    print("\n=== H2 subidas rápidas (retorno de 4 h >= +X %) ===")
    for x in (5, 8, 12):
        ev = build_events(panel, "up", x, 4)
        if len(ev) >= 5:
            table(ev, f"-- subida >= {x} % en 4 h")

    # por año y régimen para caída >= 5 %
    ev = keep[5]
    print("\n=== H1 por año: caída >= 5 % en 4 h, exceso a +4 h y +24 h (media %, n) ===")
    for y, g in ev.groupby("year"):
        print(f"  {y}: n={len(g):4d} · +4 h {g.x4.mean():6.2f} · +24 h {g.x24.mean():6.2f}")
    sma = btc.close.resample("D").last().rolling(200).mean()
    reg = btc.close.resample("D").last() > sma
    ev = ev.copy()
    ev["reg"] = [bool(reg.get(pd.Timestamp(d), np.nan)) if pd.Timestamp(d) in reg.index and not np.isnan(sma.get(pd.Timestamp(d), np.nan)) else None for d in ev.day]
    print("\n=== H6 régimen (BTC sobre su media de 200 días) — caída >= 5 % en 4 h ===")
    for lab, g in ev.groupby("reg"):
        m4, t4 = cluster_t(g.x4, g.day)
        m24, t24 = cluster_t(g.x24, g.day)
        print(f"  {'sobre SMA200' if lab else 'bajo SMA200'}: n={len(g)} · +4 h exceso {m4:.2f} (t {t4:.1f}) · +24 h exceso {m24:.2f} (t {t24:.1f})")

    # ---------------- H4 estacionalidad
    print("\n=== H4 estacionalidad BTC (UTC) 2018-2026: retorno medio por hora y por día, t simple ===")
    r = btc.close.pct_change().dropna() * 100
    by_h = r.groupby(r.index.hour).agg(["mean", "std", "count"])
    by_h["t"] = by_h["mean"] / (by_h["std"] / np.sqrt(by_h["count"]))
    top = by_h.sort_values("t")
    print("  peores horas:", "; ".join(f"{h:02d}h {row['mean']:+.4f} % (t {row['t']:+.1f})" for h, row in top.head(3).iterrows()))
    print("  mejores horas:", "; ".join(f"{h:02d}h {row['mean']:+.4f} % (t {row['t']:+.1f})" for h, row in top.tail(3).iterrows()))
    by_d = r.groupby(r.index.dayofweek).agg(["mean", "std", "count"])
    by_d["t"] = by_d["mean"] / (by_d["std"] / np.sqrt(by_d["count"]))
    print("  por día (0=lun): " + "; ".join(f"{d} {row['mean']:+.4f} % (t {row['t']:+.1f})" for d, row in by_d.iterrows()))
    vol = (r.abs()).groupby(r.index.hour).mean()
    print(f"  volatilidad media por hora: mín {vol.min():.3f} % a las {int(vol.idxmin()):02d}h · máx {vol.max():.3f} % a las {int(vol.idxmax()):02d}h")
    print("  (24 horas + 7 días = 31 contrastes: |t| < 3,2 es compatible con azar)")

    # ---------------- H5 agrupación de volatilidad
    d1 = btc.close.resample("D").last().pct_change().dropna() * 100
    print(f"\n=== H5 volatilidad agrupada (BTC diario): corr(|r_t|, |r_t-1|) = {d1.abs().corr(d1.abs().shift(1)):.3f} · tras día |r|>5 %: |r| medio siguiente {d1.abs()[d1.abs().shift(1)>5].mean():.2f} % frente a {d1.abs().mean():.2f} % normal (n={(d1.abs().shift(1)>5).sum()})")

    # ---------------- H7 cascada: caída fuerte en 1 h con volumen anómalo
    print("\n=== H7 caída >= 3 % en 1 h con volumen >= 3x su media de 24 h ===")
    rows = []
    for a, d in panel.items():
        c = d.close
        r1 = c / c.shift(1) - 1
        vm = d.volume.rolling(24, min_periods=12).mean().shift(1)
        cond = (r1 <= -0.03) & (d.volume >= 3 * vm) & (d.trades >= 10)
        last, idx = -10 ** 9, np.flatnonzero(cond.to_numpy())
        fwd = {k: (c.shift(-k) / c - 1) for k in H}
        ym = {k: fwd[k].groupby(fwd[k].index.year).mean() for k in H}
        for i in idx:
            if i - last >= 24:
                last = i
                t = c.index[i]
                row = {"asset": a, "day": t.strftime("%Y-%m-%d"), "year": t.year}
                for k in H:
                    v = fwd[k].iloc[i]
                    row[f"f{k}"] = v * 100
                    row[f"x{k}"] = (v - ym[k].get(t.year, np.nan)) * 100
                rows.append(row)
    ev = pd.DataFrame(rows)
    if len(ev) >= 5:
        table(ev, "-- eventos tipo cascada")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "robustez":
        robustez(sys.argv[1])
    else:
        main(sys.argv[1] if len(sys.argv) > 1 else "USD")
