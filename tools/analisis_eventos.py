"""Catálogo de eventos y estudio de grandes movimientos (histórico de Kraken, velas de 1 h en USD).

Uso: python3 tools/analisis_eventos.py     (escribe datos/eventos/catalogo_eventos.csv y eventos_informe.txt)

Tres partes:
 A. Ciclos de BTC (zigzag de >= 30 %): fechas y precios reales de los máximos y mínimos, para contrastar cifras "de memoria".
 B. Mayores movimientos de 24 h de BTC/ETH/XRP/DOGE detectados automáticamente, con el evento del catálogo más cercano (±3 días).
 C. Cada evento del catálogo: rentabilidad de 24 h antes, 24 h, 3 d y 7 d después (respecto al día 0 a las 00:00 UTC) y su
    "rareza" (percentil del movimiento de 24 h frente a TODAS las ventanas de 24 h de ese activo).

Límites que hay que tener presentes (no adornar los resultados):
 - Los eventos están fechados por DÍA (a veces la noticia salió a media jornada): las ventanas mezclan antes y después.
 - Las fechas [Seguro] son hechos muy conocidos o comprobados en fuentes; [Probable] son de memoria y hay que verificarlas.
 - Se ve QUÉ pasó tras cada noticia, no si se podía anticipar: el bot no lee noticias, y un patrón "a posteriori" no es una estrategia.
 - LUNA/FTT y SHIB antes de 30/11/2021 no están en Kraken USD: esos eventos se miden en los activos que sí hay.
"""
import csv
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "datos" / "eventos"
ASSETS = ["BTC", "ETH", "XRP", "DOGE", "LTC", "ADA", "SOL", "SHIB", "DOT", "LINK", "BCH", "XMR", "TRX", "PEPE", "POL"]

# fecha (UTC, día), activos afectados, dirección esperada de la noticia (+1/-1/0), evento, confianza, fuente
E = [
    ("2017-12-18", "BTC", 0, "CME lanza futuros de Bitcoin", "Seguro", "conocimiento general"),
    ("2018-01-16", "BTC,ETH,XRP", -1, "Rumores de prohibición del trading cripto en Corea del Sur", "Probable", "conocimiento general (fecha por verificar)"),
    ("2019-04-02", "BTC,ETH", 0, "Subida súbita de BTC (~+18 %) sin noticia clara", "Probable", "conocimiento general (fecha por verificar)"),
    ("2019-06-18", "BTC,ETH,XRP", 1, "Facebook anuncia Libra", "Probable", "conocimiento general (fecha por verificar)"),
    ("2020-03-12", "BTC,ETH,XRP", -1, "Jueves negro del COVID: caída global de activos de riesgo", "Seguro", "conocimiento general"),
    ("2020-05-11", "BTC", 0, "Halving de Bitcoin (recompensa 12,5 -> 6,25 BTC)", "Seguro", "conocimiento general"),
    ("2020-10-21", "BTC,ETH", 1, "PayPal anuncia compra/venta de cripto", "Seguro", "conocimiento general"),
    ("2020-12-22", "XRP,BTC", -1, "La SEC demanda a Ripple (XRP)", "Seguro", "https://www.ccn.com/education/crypto/ripple-vs-sec-timeline-and-outcomes/"),
    ("2021-01-29", "BTC,DOGE", 1, "Musk pone #bitcoin en su biografía de Twitter", "Probable", "conocimiento general (fecha por verificar)"),
    ("2021-02-04", "DOGE,BTC", 1, "Musk: «Dogecoin is the people's crypto»", "Seguro", "https://news.bitcoin.com/doge-token-pumps-after-elon-musk-tweets-dogecoin-is-the-peoples-crypto/"),
    ("2021-02-08", "BTC,ETH", 1, "Tesla anuncia compra de 1.500 M$ en BTC", "Seguro", "conocimiento general"),
    ("2021-04-14", "BTC,ETH", 0, "Coinbase sale a bolsa (salida directa)", "Seguro", "conocimiento general"),
    ("2021-04-28", "DOGE,BTC", 1, "Tuits de Musk y Mark Cuban sobre Dogecoin", "Seguro", "https://www.cnbc.com/2021/04/28/dogecoin-price-surges-after-tweets-from-elon-musk-and-mark-cuban.html"),
    ("2021-05-08", "DOGE,BTC", -1, "Musk en Saturday Night Live llama a Dogecoin «hustle»", "Seguro", "https://www.fortune.com/2021/05/09/dogecoin-price-stock-buy-elon-musk-snl-host"),
    ("2021-05-12", "BTC,DOGE", -1, "Tesla suspende pagos con Bitcoin (minería y energía)", "Seguro", "conocimiento general"),
    ("2021-05-19", "BTC,ETH,DOGE,XRP", -1, "China refuerza prohibición cripto a bancos y frena la minería: caída del 30 %", "Seguro", "conocimiento general (fecha exacta por verificar)"),
    ("2021-06-18", "BTC", -1, "Sichuan ordena cerrar mineros de Bitcoin (salida de hashrate de China)", "Probable", "conocimiento general (fecha por verificar)"),
    ("2021-09-24", "BTC,ETH", -1, "China declara ilegales todas las transacciones con cripto", "Probable", "conocimiento general (fecha por verificar)"),
    ("2021-11-10", "BTC,ETH", 0, "IPC de EE. UU. de 6,2 %; BTC marca máximo histórico de 2021 (~69 k$)", "Probable", "conocimiento general (fecha por verificar)"),
    ("2022-05-09", "BTC,ETH", -1, "Colapso de TerraUSD/LUNA (LUNA no está en Kraken USD)", "Seguro", "conocimiento general"),
    ("2022-06-13", "BTC,ETH", -1, "Celsius congela retiros; miedo a contagio (3AC)", "Seguro", "conocimiento general"),
    ("2022-09-15", "ETH", 0, "The Merge de Ethereum (paso a prueba de participación)", "Seguro", "conocimiento general"),
    ("2022-10-28", "DOGE,BTC", 1, "Musk cierra la compra de Twitter; DOGE se dispara", "Probable", "conocimiento general (fecha por verificar)"),
    ("2022-11-08", "BTC,ETH,SOL,XRP", -1, "Colapso de FTX (SOL muy ligada a FTX/Alameda)", "Seguro", "conocimiento general"),
    ("2023-03-11", "BTC,ETH", 1, "Quiebra de Silicon Valley Bank y desanclaje de USDC; BTC sube como refugio", "Seguro", "conocimiento general"),
    ("2023-06-05", "BTC,ETH,SOL,ADA", -1, "La SEC demanda a Binance y, al día siguiente, a Coinbase", "Seguro", "conocimiento general"),
    ("2023-06-15", "BTC,ETH", 1, "BlackRock solicita un ETF de Bitcoin al contado", "Seguro", "conocimiento general"),
    ("2023-07-13", "XRP,BTC", 1, "Sentencia Torres: XRP no es valor en ventas públicas", "Seguro", "https://www.ccn.com/education/crypto/ripple-vs-sec-timeline-and-outcomes/"),
    ("2023-08-29", "BTC,ETH", 1, "Grayscale gana a la SEC (camino a los ETF)", "Seguro", "conocimiento general"),
    ("2023-10-16", "BTC,ETH", 1, "Falsa noticia de aprobación del ETF de BlackRock; se desmiente", "Seguro", "conocimiento general"),
    ("2024-01-10", "BTC,ETH", 1, "La SEC aprueba los ETF de Bitcoin al contado (¿vender la noticia?)", "Seguro", "conocimiento general"),
    ("2024-04-20", "BTC", 0, "Halving de Bitcoin (recompensa 6,25 -> 3,125 BTC)", "Seguro", "conocimiento general"),
    ("2024-05-20", "ETH,BTC", 1, "Giro sorpresa: la SEC admitirá ETF de Ethereum", "Seguro", "conocimiento general"),
    ("2024-08-05", "BTC,ETH,SOL", -1, "Caída global por el cierre del carry trade del yen", "Seguro", "conocimiento general"),
    ("2024-11-06", "BTC,ETH,DOGE,XRP", 1, "Trump gana las elecciones de EE. UU.", "Seguro", "conocimiento general"),
    ("2024-12-05", "BTC,ETH,XRP", 1, "BTC supera los 100.000 $", "Seguro", "conocimiento general"),
    ("2025-01-18", "BTC,SOL,DOGE", 0, "Lanzamiento de la memecoin de Trump (drenó liquidez del resto)", "Seguro", "conocimiento general"),
    ("2025-02-21", "BTC,ETH", -1, "Hackeo de Bybit (~1.500 M$ en ETH)", "Seguro", "conocimiento general"),
    ("2025-03-02", "XRP,SOL,ADA,BTC", 1, "Trump anuncia una reserva estratégica cripto que cita XRP, SOL y ADA", "Seguro", "conocimiento general"),
    ("2025-03-19", "XRP", 1, "La SEC abandona su apelación contra Ripple", "Probable", "https://www.ccn.com/ripple-vs-sec-lawsuit-decision-xrp-court-ruling-timing-details-in-full/ (fecha por verificar)"),
    ("2025-04-03", "BTC,ETH,SOL", -1, "Aranceles del «Día de la Liberación» de Trump", "Seguro", "conocimiento general"),
    ("2025-04-09", "BTC,ETH,SOL", 1, "Trump pausa 90 días los aranceles", "Seguro", "conocimiento general"),
    ("2025-10-10", "BTC,ETH,SOL,DOGE,XRP,ADA", -1, "Arancel del 100 % a China: mayor liquidación de la historia (~19.000 M$)", "Seguro", "https://www.cnn.com/2025/10/11/business/trump-tariffs-crypto-selloff"),
]


def load(quote="USD"):
    """Cierres por hora indexados por el INSTANTE DE CIERRE de la vela (inicio + 1 h)."""
    out = {}
    for a in ASSETS:
        f = ROOT / "datos" / "historico_1h" / f"{quote}_{a}.csv.gz"
        if not f.exists():
            continue
        d = pd.read_csv(f, usecols=["time", "close", "trades"])
        d = d[d.time >= 1_451_606_400]                       # desde 2016 (halving de 07/2016)
        s = pd.Series(d.close.to_numpy(float), index=pd.to_datetime(d.time + 3600, unit="s"))
        s = s[~s.index.duplicated()]
        out[a] = s
    return out


def px(s, t, max_gap_h=6):
    """Precio en el instante t: último cierre disponible como mucho `max_gap_h` horas antes."""
    i = s.index.searchsorted(t, side="right") - 1
    if i < 0 or (t - s.index[i]) > pd.Timedelta(hours=max_gap_h) or s.index[-1] < t:
        return np.nan
    return float(s.iloc[i])


def zigzag(daily, thr=0.30):
    """Máximos y mínimos alternos con un movimiento mínimo `thr` (el último punto queda marcado con *)."""
    v = daily.to_numpy()
    pts, mode, ext, hi, lo = [], None, 0, 0, 0
    for i in range(1, len(v)):
        if mode is None:
            hi = i if v[i] > v[hi] else hi
            lo = i if v[i] < v[lo] else lo
            if v[i] / v[lo] - 1 >= thr:
                pts.append((lo, "mín")); mode, ext = "up", i
            elif v[i] / v[hi] - 1 <= -thr:
                pts.append((hi, "máx")); mode, ext = "down", i
        elif mode == "up":
            if v[i] > v[ext]:
                ext = i
            elif v[i] / v[ext] - 1 <= -thr:
                pts.append((ext, "máx")); mode, ext = "down", i
        else:
            if v[i] < v[ext]:
                ext = i
            elif v[i] / v[ext] - 1 >= thr:
                pts.append((ext, "mín")); mode, ext = "up", i
    pts.append((ext, "máx*" if mode == "up" else "mín*"))
    return [(daily.index[i], k, float(v[i])) for i, k in pts]


def fmt(x):
    return "   n/d" if x != x else f"{100*x:+6.1f}"


def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    P = load("USD")
    L = []
    W = L.append
    btc = P["BTC"]
    W(f"Catálogo de eventos y grandes movimientos · datos Kraken USD 1 h · BTC {btc.index[0].date()} -> {btc.index[-1].date()}")
    W("Activos disponibles y desde cuándo: " + ", ".join(f"{a} {s.index[0].date()}" for a, s in P.items()))
    W("")
    # ---------------------------------------------------------------- A
    daily_all = btc.resample("1D").last().dropna()
    daily = daily_all[daily_all.index >= "2017-01-01"]
    W("== A. Ciclos de BTC (movimientos de al menos 30 %, cierres diarios UTC) ==")
    zz = zigzag(daily, 0.30)
    for k, (t, kind, v) in enumerate(zz):
        chg = "" if k == 0 else f"  ({100*(v/zz[k-1][2]-1):+.0f} % desde el anterior, {(t-zz[k-1][0]).days} días)"
        W(f"  {t.date()}  {kind:4s} {v:>10,.0f} $" + chg)
    W("")
    # ---------------------------------------------------------------- B
    W("== B. Mayores movimientos de 24 h detectados automáticamente (cierre de la ventana; sin solapes ±72 h) ==")
    cat_dates = [(pd.Timestamp(e[0]), e[3]) for e in E]
    for a in ("BTC", "ETH", "XRP", "DOGE"):
        s = P[a]
        s24 = s.copy()
        r = s24 / s24.reindex(s24.index - pd.Timedelta(hours=24)).to_numpy() - 1
        r = r.dropna()
        r = r[r.index >= "2018-01-01"]
        order = r.abs().sort_values(ascending=False)
        chosen = []
        for t, _ in order.items():
            if all(abs((t - c).total_seconds()) > 72 * 3600 for c in chosen):
                chosen.append(t)
            if len(chosen) == 8:
                break
        W(f"  -- {a}: 8 mayores movimientos de 24 h --")
        for t in sorted(chosen):
            near = min(cat_dates, key=lambda x: abs((x[0] - t.normalize()).days))
            nd = abs((near[0] - t.normalize()).days)
            tag = f"≈ {near[1]} ({near[0].date()})" if nd <= 3 else "sin evento del catálogo cercano"
            W(f"     {t:%Y-%m-%d %H:%M}  {100*r[t]:+6.1f} %   {tag}")
    W("")
    # ---------------------------------------------------------------- C
    W("== C. Cada evento: rentabilidad % antes y después (t0 = 00:00 UTC del día; dir = efecto esperado de la noticia) ==")
    W(f"{'fecha':10s} {'activo':5s} {'dir':>3s} {'-24h':>7s} {'+24h':>7s} {'+3d':>7s} {'+7d':>7s} {'rareza24':>8s}  evento [confianza]")
    rows = []
    stats = {}
    for date, assets, d, name, conf, src in E:
        t0 = pd.Timestamp(date)
        for a in assets.split(","):
            if a not in P or P[a].index[0] > t0 - pd.Timedelta(days=8):
                continue
            s = P[a]
            p0 = px(s, t0)
            v = {}
            for k, h in (("pre24", -24), ("post24", 24), ("post72", 72), ("post168", 168)):
                t1 = t0 + pd.Timedelta(hours=h)
                v[k] = (p0 / px(s, t1) - 1) if h < 0 else (px(s, t1) / p0 - 1)
            allr = (s / s.reindex(s.index - pd.Timedelta(hours=24)).to_numpy() - 1).dropna()
            allr = allr[allr.index >= "2018-01-01"].abs()
            rare = float((allr < abs(v["post24"])).mean()) if v["post24"] == v["post24"] else np.nan
            W(f"{date:10s} {a:5s} {d:+3d} {fmt(v['pre24'])} {fmt(v['post24'])} {fmt(v['post72'])} {fmt(v['post168'])} {('%7.0f%%' % (100*rare)) if rare == rare else '     n/d'}  {name} [{conf}]")
            rows.append({"fecha_utc": date, "activo": a, "direccion_esperada": d, "ret_pre24h_pct": round(100 * v["pre24"], 2),
                         "ret_24h_pct": round(100 * v["post24"], 2), "ret_3d_pct": round(100 * v["post72"], 2),
                         "ret_7d_pct": round(100 * v["post168"], 2), "rareza_24h_pct": round(100 * rare, 1),
                         "evento": name, "confianza": conf, "fuente": src})
            if d != 0 and a == assets.split(",")[0]:
                stats.setdefault(d, []).append(v)
    W("")
    W("== D. Lectura estadística (solo el activo PRINCIPAL de cada evento con dirección; n pequeño, no concluyente por sí solo) ==")
    for d, vs in sorted(stats.items(), reverse=True):
        n = len(vs)
        same = np.mean([np.sign(v["post24"]) == d for v in vs if v["post24"] == v["post24"]])
        cont = np.mean([np.sign(v["post168"]) == d for v in vs if v["post168"] == v["post168"]])
        rev = np.mean([np.sign(v["post168"]) == -d for v in vs if v["post168"] == v["post168"]])
        antic = np.mean([np.sign(v["pre24"]) == d for v in vs if v["pre24"] == v["pre24"]])
        m24 = np.nanmean([d * v["post24"] for v in vs]) * 100
        m7 = np.nanmean([d * v["post168"] for v in vs]) * 100
        W(f"  noticias {'positivas' if d > 0 else 'negativas'} (n={n}): en 24 h el precio fue en el sentido de la noticia el {100*same:.0f} % de las veces; "
          f"a 7 d el {100*cont:.0f} % (en contra {100*rev:.0f} %); ya se movía en ese sentido 24 h antes el {100*antic:.0f} %; "
          f"movimiento medio ORIENTADO a la noticia: 24 h {m24:+.1f} %, 7 d {m7:+.1f} %")
    W("")
    # ---------------------------------------------------------------- E
    W("== E. Ciclos de halving de BTC (cierres diarios UTC; halvings 09/07/2016, 11/05/2020, 20/04/2024) ==")
    hv = [pd.Timestamp("2016-07-09"), pd.Timestamp("2020-05-11"), pd.Timestamp("2024-04-20")]
    ends = hv[1:] + [daily_all.index[-1] + pd.Timedelta(days=1)]
    prev_peak = None
    for h0, h1 in zip(hv, ends):
        seg = daily_all[(daily_all.index >= h0) & (daily_all.index < min(h1, h0 + pd.Timedelta(days=730)))]
        p0 = float(daily_all[daily_all.index >= h0].iloc[0])
        pk = seg.idxmax()
        line = f"  halving {h0.date()}: BTC {p0:,.0f} $ -> máximo del ciclo {seg.max():,.0f} $ el {pk.date()} ({(pk-h0).days} días después, x{seg.max()/p0:.1f})"
        after = daily_all[(daily_all.index > pk) & (daily_all.index < h1)]
        if len(after):
            tr = after.idxmin()
            line += f"; mínimo posterior {after.min():,.0f} $ el {tr.date()} ({(tr-pk).days} días tras el máximo, {100*(after.min()/seg.max()-1):+.0f} %)"
        W(line)
        for d_ in (30, 90, 180, 365):
            t_ = h0 + pd.Timedelta(days=d_)
            if t_ <= daily_all.index[-1]:
                W(f"       a {d_:>3d} días del halving: {100*(float(daily_all[daily_all.index >= t_].iloc[0])/p0-1):+6.0f} %")
    W("  Con 3 ciclos NO hay significación estadística: es una hipótesis para vigilar, no una regla operable.")
    W("")
    W("Notas: (1) ventana por día, no por hora; (2) el catálogo lo elegí yo a partir de eventos conocidos: hay sesgo de selección "
      "(se eligen eventos porque el precio se movió), así que el % de aciertos de la dirección de la noticia NO demuestra nada por sí solo; "
      "(3) esto describe lo ocurrido, no una regla operable sin conocer la noticia antes.")
    with (OUTDIR / "catalogo_eventos.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    txt = "\n".join(L)
    (OUTDIR / "eventos_informe.txt").write_text(txt)
    print(txt)


if __name__ == "__main__":
    main()
