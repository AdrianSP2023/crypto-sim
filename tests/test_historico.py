"""Histórico de Kraken: zip troceado en partes, streaming, filtro de pares y agregación a 1 h."""
import io, sys, tempfile, zipfile
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1]) + "/tools")
import historico_kraken as hk

def trades(seed, n, t0, header=False):
    rng = np.random.default_rng(seed)
    ts = np.sort(t0 + rng.random(n) * 86400 * 5)
    ts = np.round(ts, 4)
    px = np.round(100 * np.exp(np.cumsum(rng.normal(0, 0.0007, n))), 4)
    vol = np.round(rng.lognormal(0, 1, n), 6)
    df = pd.DataFrame({"timestamp": ts, "price": px, "volume": vol, "type": "b", "order_type": "l", "misc": "", "trade_id": range(n)})
    return df

def ref(df):
    h = (df.timestamp // 3600).astype("int64") * 3600
    g = df.groupby(h)
    return pd.DataFrame({"open": g.price.first(), "high": g.price.max(), "low": g.price.min(), "close": g.price.last(),
                         "volume": g.volume.sum(), "trades": g.price.size()})

def main():
    hk.Agg.__init__  # noqa
    A = trades(1, 60000, 1_600_000_000)
    B = trades(2, 25000, 1_610_000_000)
    C = trades(3, 5000, 1_620_000_000)
    D = trades(4, 5000, 1_620_000_000)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("Kraken/XBTUSD.csv", A.to_csv(header=False, index=False))
        z.writestr("Kraken/DOGEEUR.csv", B.to_csv(header=True, index=False))      # con cabecera
        z.writestr("Kraken/ZZZZEUR.csv", C.to_csv(header=False, index=False))     # base que no queremos
        z.writestr("Kraken/XDGUSD.csv", D.to_csv(header=False, index=False))     # alias XDG -> DOGE
        z.writestr("Kraken/README.txt", "hola")
        z.writestr("MANIFEST.json", '{"ok": true}')
    data = buf.getvalue()
    third = len(data) // 3
    parts = [data[:third], data[third:2 * third], data[2 * third:]]
    stream = (p[i:i + 65536] for p in parts for i in range(0, len(p), 65536))   # trozos que cortan líneas
    with tempfile.TemporaryDirectory() as d:
        members, res, manifest = hk.process(stream, {"BTC", "DOGE"}, out_dir=d, log=lambda s: None)
        assert [m[0] for m in members][:2] == ["Kraken/XBTUSD.csv", "Kraken/DOGEEUR.csv"], members
        assert set(res) == {"BTC/USD", "DOGE/EUR", "DOGE/USD"}, res
        assert manifest == '{"ok": true}', manifest
        for key, src in (("BTC/USD", A), ("DOGE/EUR", B), ("DOGE/USD", D)):
            base, q = key.split("/")
            got = pd.read_csv(Path(d) / f"{q}_{base}.csv.gz").set_index("time")
            exp = ref(src)
            assert list(got.index) == list(exp.index), key
            for c in ("open", "high", "low", "close", "trades"):
                assert np.allclose(got[c], exp[c], rtol=1e-9), (key, c)
            assert np.allclose(got.volume, exp.volume, rtol=1e-6), key
            assert res[key]["trades"] == len(src)
        assert not (Path(d) / "EUR_ZZZZ.csv.gz").exists()
    assert hk.parse_pair(b"x/XXBTZEUR.csv") == ("BTC", "EUR") and hk.parse_pair("XDGUSD.csv") == ("DOGE", "USD")
    assert hk.parse_pair("2ZEUR.csv") == ("2Z", "EUR") and hk.parse_pair("XETHZUSD.csv") == ("ETH", "USD")
    assert hk.parse_pair("AAVEXBT.csv") is None and hk.parse_pair("ADAETH.csv") is None
    assert hk.parse_pair("USDTUSD.csv") == ("USDT", "USD") and hk.parse_pair("MANIFEST.json") is None
    # ---- modo ventanas: velas de 1 min solo dentro de las ventanas de cada evento
    with tempfile.TemporaryDirectory() as d:
        t_ev = 1_600_000_000 + 2 * 86400
        t_ev = (t_ev // 3600) * 3600
        ev = pd.DataFrame({"quote": ["USD"], "asset": ["BTC"], "t_utc": [pd.to_datetime(t_ev, unit="s", utc=True).strftime("%Y-%m-%d %H:%M")]})
        ep = Path(d) / "ev.csv"
        ev.to_csv(ep, index=False)
        stream2 = (data[i:i + 65536] for i in range(0, len(data), 65536))
        out = Path(d) / "v"
        res2 = hk.ventanas(stream2, events_path=ep, out_dir=out, log=lambda s: None)
        assert set(res2) == {"BTC/USD"}, res2
        got = pd.read_csv(out / "USD_BTC.csv.gz").set_index("time")
        m0, m1 = t_ev - hk.PRE_S, t_ev + hk.POST_S
        sub = A[(A.timestamp >= m0) & (A.timestamp < m1)]
        mm = (sub.timestamp // 60).astype("int64") * 60
        g = sub.groupby(mm)
        exp = pd.DataFrame({"open": g.price.first(), "high": g.price.max(), "low": g.price.min(), "close": g.price.last(), "trades": g.price.size()})
        assert list(got.index) == list(exp.index) and len(got) > 100, (len(got), len(exp))
        for c in ("open", "high", "low", "close", "trades"):
            assert np.allclose(got[c], exp[c], rtol=1e-9), c
        assert got.index.min() >= m0 and got.index.max() < m1
    print("histórico Kraken (streaming, partes, filtro, agregación 1 h y ventanas 1 min) OK")

if __name__ == "__main__":
    main()
