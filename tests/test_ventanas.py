"""Estudio de ventanas: simulación TP/SL y flujo completo con datos sintéticos."""
import sys, tempfile
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1]) + "/tools")
import analisis_ventanas as av

def main():
    # simulate: compra a 100 al abrir vela 0
    o = np.array([100, 100, 100, 100.0]); c = o.copy()
    h = np.array([100, 103, 100, 100.0]); l = np.array([100, 100, 100, 100.0])
    g, why, k = av.simulate(o, h, l, c, 0, 0.03, 0.05, 3)
    assert why == "tp" and abs(g - 0.03) < 1e-12 and k == 1, (g, why, k)
    l2 = np.array([100, 94, 100, 100.0]); h2 = np.array([100, 104, 100, 100.0])
    g, why, k = av.simulate(o, h2, l2, c, 0, 0.03, 0.05, 3)
    assert why == "stop" and abs(g + 0.05) < 1e-12, (g, why)          # stop antes que TP en la misma vela
    o3 = np.array([100, 90, 90, 90.0]); l3 = np.array([100, 89, 89, 89.0])
    g, why, k = av.simulate(o3, o3, l3, o3, 0, None, 0.05, 3)
    assert why == "stop" and abs(g + 0.10) < 1e-12, g                   # hueco: sale a la apertura
    g, why, k = av.simulate(o, o, l, c, 0, None, None, 3)
    assert why == "timeout" and g == 0
    # flujo completo: un desplome sintético con rebote
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        t = 1_600_000_000 // 3600 * 3600
        pre, post = 4 * 3600, 9 * 3600
        idx = np.arange(t - pre, t + post, 60)
        px = np.full(len(idx), 100.0)
        k3 = (t - 3 * 3600 - (t - pre)) // 60
        px[k3:] = 100.0                                                  # referencia = 100 en t-3h
        kd = (t + 1800 - (t - pre)) // 60
        px[kd:] = np.linspace(80, 80, len(idx) - kd)                    # cae a 80 (-20 %) a t+30 min
        kr = (t + 2 * 3600 - (t - pre)) // 60
        px[kr:] = 90.0                                                   # rebota a 90 dos horas después
        df = pd.DataFrame({"time": idx, "open": px, "high": px, "low": px, "close": px, "vwap": px, "volume": 1.0, "count": 1})
        (d / "v").mkdir()
        df.to_csv(d / "v" / "EUR_TST.csv.gz", index=False)
        k_end = (t + 3600 - (t - pre)) // 60 - 1
        ev = pd.DataFrame({"quote": ["EUR"], "asset": ["TST"], "t_utc": [pd.to_datetime(t, unit="s").strftime("%Y-%m-%d %H:%M")],
                           "drop_4h_pct": [-20.0], "close_evento": [px[k_end]], "close_pre4h": [100.0]})
        ev.to_csv(d / "ev.csv", index=False)
        res, checks, skipped, nev = av.analyse(d / "v", d / "ev.csv")
        assert len(res) == 1 and skipped == 0 and np.allclose(checks, 0), (res, checks, skipped)
        r = res.iloc[0]
        assert r.disparo_min_desde_t == 30, r.disparo_min_desde_t
        assert abs(r.d0_entrada - 80) < 1e-9 and abs(r.d0_ret240 - 12.5) < 1e-6, (r.d0_entrada, r.d0_ret240)   # 80 -> 90 = +12,5 %
        assert abs(r["d0_tp8_slx"] - 12.5) < 1e-6, r["d0_tp8_slx"]      # hueco: TP se ejecuta a la apertura (90)
        assert abs(r["d0_tp3_sl2"] - 12.5) < 1e-6, r["d0_tp3_sl2"]
        assert "Eventos analizados: 1" in av.rep(res)
    print("estudio de ventanas 1 min OK")

if __name__ == "__main__":
    main()
