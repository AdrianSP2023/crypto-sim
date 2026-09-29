"""Registro CSV: una fila por operación cerrada, idempotente, con el contexto de la señal."""
import copy, csv, json, sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])); sys.path.insert(0, str(Path(__file__).resolve().parent))
import core, registro
from test_core import synth, run_batch, CFG_RAW

def main():
    for mode in ("next_open", "close"):
        cfg = copy.deepcopy(CFG_RAW)
        cfg["entry_fill"] = mode
        cfg["strategies"] = {k: cfg["strategies"][k] for k in ("c_banda_atr", "macd_momentum", "c_banda_atr_regimen")}
        frames = {a: synth(300 + k) for k, a in enumerate("ABCD")}
        st = run_batch(frames, cfg)
        closed = [c for v in st["strategies"].values() for c in v["closed"]]
        assert len(closed) > 20, len(closed)
        assert all(c.get("ctx") and "amplitud_ema50" in c["ctx"] and "amplitud_ema200" in c["ctx"] for c in closed), mode
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "sub" / "op.csv"
            n1 = registro.sync(st, cfg, path=p)
            n2 = registro.sync(st, cfg, path=p)
            assert n1 == len(closed) and n2 == 0, (n1, n2)
            rows = list(csv.DictReader(p.open(encoding="utf-8")))
            assert list(rows[0].keys()) == registro.COLUMNS
            assert {r["fase"] for r in rows} == {cfg["phase"]}
            for r in rows:
                assert abs(float(r["comision_eur"]) - float(r["cantidad_eur"]) * float(r["comision_pct"]) / 100) < 1e-3
                assert abs(float(r["neto_pct"]) - (float(r["bruto_pct"]) - float(r["comision_pct"]))) < 0.002
                json.loads(r["contexto_senal"])
            fam = {r["estrategia"]: r["familia"] for r in rows}
            assert fam.get("c_banda_atr_regimen", "c_banda_atr") == "c_banda_atr"
            # cierres nuevos se añaden sin duplicar
            st["strategies"]["c_banda_atr"]["closed"].append({**closed[0], "exit_ts": closed[0]["exit_ts"] + 99999})
            assert registro.sync(st, cfg, path=p) == 1
        print("registro CSV OK (", mode, "):", n1, "filas")

def test_velas():
    import pandas as pd
    df = synth(5)[:300]
    with tempfile.TemporaryDirectory() as d:
        st = {}
        assert registro.guardar_velas({"A/B": df.iloc[:200]}, st, 5, base=d) == 200
        assert registro.guardar_velas({"A/B": df.iloc[:200]}, st, 5, base=d) == 0          # sin duplicar
        assert registro.guardar_velas({"A/B": df}, st, 5, base=d) == 100                    # solo las nuevas
        got = pd.read_csv(Path(d) / "A_B.csv")
        assert len(got) == 300 and got.time.is_unique and got.time.is_monotonic_increasing
        assert abs(got.close.iloc[-1] - df.close.iloc[-1]) < 1e-9 * df.close.iloc[-1]
    print("guardado de velas OK")

if __name__ == "__main__":
    main()
    test_velas()
