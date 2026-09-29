"""Histórico de Kraken (trades / time and sales) -> velas de 1 h de los activos que usamos.

Fuente: https://support.kraken.com/es/articles/360047543791-downloadable-historical-market-data-time-and-sales-
13 partes de ~2 GB (.zip.part00 ... part12) que, concatenadas byte a byte, forman UN zip con un CSV por par
(timestamp, price, volume, type, order_type, misc, trade_id). No cabe en disco (26 GB), así que se procesa en
streaming: se encadenan las partes, se descomprime al vuelo con stream-unzip y solo se parsean los pares
que interesan (base en WANTED, cotizados en EUR o USD). El resto se descomprime y se descarta.

Uso (en GitHub Actions, workflow "Histórico Kraken"):
  python3 tools/historico_kraken.py probe   # comprueba acceso, tamaños, nombres de los primeros ficheros y formato
  python3 tools/historico_kraken.py full    # procesa todo y escribe datos/historico_1h/*.csv.gz + informe
"""
import gzip
import io
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "datos" / "historico_1h"
URL = "https://assets.kraken.com/marketing/institutions/Kraken_Trades_Full_2026Q2.zip.part%02d"
SUMS = "https://assets.kraken.com/marketing/institutions/Trades_Full_PARTS_SHA256SUMS.txt"
NPARTS = 13
QUOTES = ("EUR", "USD")
EXTRA = {"BTC", "ETH", "XRP", "DOGE", "SHIB", "LTC", "ADA", "SOL", "BCH", "DOT", "LINK", "XLM", "TRX", "AVAX",
         "POL", "MATIC", "ETC", "XMR", "ZEC", "ATOM", "UNI", "AAVE", "FIL", "ALGO", "EOS", "DASH", "PEPE"}
ALIAS = {"XBT": "BTC", "XXBT": "BTC", "XDG": "DOGE", "XXDG": "DOGE", "XETH": "ETH", "XXRP": "XRP", "XLTC": "LTC",
         "XXLM": "XLM", "XETC": "ETC", "XXMR": "XMR", "XZEC": "ZEC", "XREP": "REP", "XMLN": "MLN"}
NAMES = ["timestamp", "price", "volume", "type", "order_type", "misc", "trade_id"]


def wanted_bases():
    b = set(EXTRA)
    sp = ROOT / "state" / "state.json"
    if sp.exists():
        b |= {str(x["asset"]).upper() for x in json.loads(sp.read_text()).get("universe", [])}
    return b


def parse_pair(member):
    """'Kraken/XBTEUR.csv' -> ('BTC', 'EUR'); None si no es un CSV de par."""
    n = member.decode() if isinstance(member, bytes) else member
    n = n.rsplit("/", 1)[-1]
    if not n.lower().endswith(".csv"):
        return None
    p = n[:-4].upper()
    for q in QUOTES:
        if p.endswith(q) and len(p) > len(q):
            base = p[: -len(q)]
            if base.endswith("Z") and base[:-1] in ALIAS:      # nombres antiguos: XXBTZEUR, XETHZUSD...
                base = base[:-1]
            return ALIAS.get(base, base), q
    return None


# ----------------------------------------------------------------- lectura en streaming

def http_parts(nparts=NPARTS, url=URL, limit_bytes=None):
    """Concatena las partes descargándolas una a una, con reintento y reanudación por Range."""
    import requests
    sess = requests.Session()
    sent = 0
    for k in range(nparts):
        pos, tries = 0, 0
        while True:
            try:
                hdr = {"Range": f"bytes={pos}-"} if pos else {}
                with sess.get(url % k, headers=hdr, stream=True, timeout=90) as r:
                    if r.status_code == 404 and k > 0:
                        return
                    if r.status_code not in (200, 206):
                        raise RuntimeError(f"HTTP {r.status_code} en parte {k}")
                    if pos and r.status_code != 206:
                        raise RuntimeError("el servidor no admite Range")
                    for chunk in r.iter_content(1 << 20):
                        pos += len(chunk)
                        sent += len(chunk)
                        yield chunk
                        if limit_bytes and sent >= limit_bytes:
                            return
                break
            except Exception as e:  # noqa: BLE001
                tries += 1
                print(f"[aviso] parte {k} en byte {pos}: {e} (intento {tries})", flush=True)
                if tries > 10:
                    raise
                time.sleep(5 * tries)


class Agg:
    """Agrega trades a velas de 1 h de forma incremental (los datos vienen ordenados por tiempo)."""

    def __init__(self):
        self.parts, self.buf, self.rows, self.first = [], b"", 0, True

    def _flush_lines(self, data):
        if self.first:
            self.first = False
            if data[:64].lstrip().lower().startswith(b"timestamp") or data[:1].isalpha():
                data = data.split(b"\n", 1)[1] if b"\n" in data else b""
        if not data:
            return
        df = pd.read_csv(io.BytesIO(data), header=None, names=NAMES, usecols=[0, 1, 2],
                         dtype={"timestamp": "float64", "price": "float64", "volume": "float64"})
        if df.empty:
            return
        ts = df.timestamp.to_numpy()
        ts = np.where(ts > 1e12, ts / 1000.0, ts)
        df["h"] = (ts // 3600).astype("int64") * 3600
        g = df.groupby("h", sort=True)
        a = pd.DataFrame({"open": g.price.first(), "high": g.price.max(), "low": g.price.min(),
                          "close": g.price.last(), "volume": g.volume.sum(), "trades": g.price.size()})
        self.parts.append(a)
        self.rows += len(df)

    def feed(self, chunk):
        self.buf += chunk
        if len(self.buf) >= (48 << 20):
            i = self.buf.rfind(b"\n")
            if i >= 0:
                data, self.buf = self.buf[: i + 1], self.buf[i + 1:]
                self._flush_lines(data)

    def finish(self):
        if self.buf.strip():
            self._flush_lines(self.buf if self.buf.endswith(b"\n") else self.buf + b"\n")
        self.buf = b""
        if not self.parts:
            return pd.DataFrame(columns=["open", "high", "low", "close", "volume", "trades"])
        a = pd.concat(self.parts)
        g = a.groupby(level=0, sort=True)
        out = pd.DataFrame({"open": g.open.first(), "high": g.high.max(), "low": g.low.min(),
                            "close": g.close.last(), "volume": g.volume.sum(), "trades": g.trades.sum()})
        out.index.name = "time"
        self.parts = []
        return out


def process(stream, wanted, out_dir=None, log=print, max_members=None):
    """Recorre el zip en streaming. Devuelve (miembros, resultados por par)."""
    from stream_unzip import stream_unzip
    out_dir = Path(out_dir) if out_dir else OUT
    out_dir.mkdir(parents=True, exist_ok=True)
    members, results, manifest = [], {}, None
    for name, size, chunks in stream_unzip(stream):
        nm = name.decode(errors="replace")
        pair = parse_pair(nm)
        take = pair is not None and pair[0] in wanted
        base = nm.rsplit("/", 1)[-1]
        agg = Agg() if take else None
        keep_manifest = base.upper() == "MANIFEST.JSON"
        mbuf = b""
        nbytes = 0
        for c in chunks:
            nbytes += len(c)
            if take:
                agg.feed(c)
            elif keep_manifest and len(mbuf) < 200_000:
                mbuf += c
        members.append((nm, size, nbytes))
        if keep_manifest:
            manifest = mbuf.decode(errors="replace")
        if take:
            df = agg.finish()
            if len(df):
                f = out_dir / f"{pair[1]}_{pair[0]}.csv.gz"
                df.reset_index().to_csv(f, index=False, compression="gzip", float_format="%.10g")
                results[f"{pair[0]}/{pair[1]}"] = {"filas_1h": len(df), "trades": int(agg.rows),
                                                   "desde": pd.to_datetime(df.index.min(), unit="s").strftime("%Y-%m-%d %H:%M"),
                                                   "hasta": pd.to_datetime(df.index.max(), unit="s").strftime("%Y-%m-%d %H:%M")}
                log(f"[ok] {nm}: {agg.rows:,} trades -> {len(df):,} velas 1h ({results[f'{pair[0]}/{pair[1]}']['desde']} -> {results[f'{pair[0]}/{pair[1]}']['hasta']})")
        if max_members and len(members) >= max_members:
            break
    return members, results, manifest


# ------------------------------------------------------------------------- modos

def probe():
    import traceback
    lines = []
    OUT.mkdir(parents=True, exist_ok=True)

    def L(s):
        print(s, flush=True)
        lines.append(s)
        (OUT / "_probe.txt").write_text("\n".join(lines))
    try:
        _probe(L)
    except Exception:  # noqa: BLE001
        L("== ERROR ==")
        L(traceback.format_exc())


def _probe(L):
    import requests
    L("== HEAD de las 13 partes ==")
    for k in range(NPARTS):
        try:
            r = requests.head(URL % k, timeout=30, allow_redirects=True)
            L(f"parte {k:02d}: HTTP {r.status_code} · {r.headers.get('Content-Length')} bytes · Range: {r.headers.get('Accept-Ranges')}")
        except Exception as e:  # noqa: BLE001
            L(f"parte {k:02d}: ERROR {e}")
    try:
        L("== SHA256SUMS (primeras líneas) ==")
        L(requests.get(SUMS, timeout=30).text[:900])
    except Exception as e:  # noqa: BLE001
        L(f"sums: ERROR {e}")
    L("== Primeros miembros del zip (streaming de la parte 00, máx. 300 MB) ==")
    from stream_unzip import stream_unzip
    n = 0
    for name, size, chunks in stream_unzip(http_parts(limit_bytes=300 << 20)):
        L(f"miembro {n}: {name.decode(errors='replace')} · tamaño declarado {size} · par {parse_pair(name)}")
        head = b""
        nbytes = 0
        for c in chunks:
            nbytes += len(c)
            if len(head) < 400:
                head += c
            if len(head) >= 400 and n < 3 and nbytes < 500:
                L("   primeras líneas: " + repr(head[:300]))
        L(f"   leídos {nbytes:,} bytes sin comprimir")
        if n < 3 or name.upper().endswith(b"MANIFEST.JSON"):
            L("   cabecera: " + repr(head[:300]))
        n += 1
        if n >= 40:
            break


def full():
    t0 = time.time()
    wanted = wanted_bases()
    print("bases buscadas:", len(wanted), sorted(wanted), flush=True)
    members, results, manifest = process(http_parts(), wanted)
    rep = [f"Histórico Kraken -> velas 1 h · {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())} · {time.time()-t0:.0f} s",
           f"miembros en el zip: {len(members)} · pares guardados: {len(results)}", "", "== MANIFEST ==", (manifest or "(no encontrado)")[:3000],
           "", "== Pares guardados ==", json.dumps(results, indent=1, ensure_ascii=False),
           "", "== Todos los miembros (nombre · tamaño sin comprimir leído) ==",
           *[f"{n} · {b:,}" for n, _, b in members]]
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "_informe.txt").write_text("\n".join(rep))
    print("\n".join(rep[:6]))


if __name__ == "__main__":
    {"probe": probe, "full": full}[sys.argv[1] if len(sys.argv) > 1 else "probe"]()
