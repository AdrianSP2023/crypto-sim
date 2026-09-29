"""Informe del paper trader del modelo: python3 modelo/report.py"""
import json
from pathlib import Path

import pandas as pd

MD = Path(__file__).resolve().parent


def main():
    st = json.loads((MD / "state.json").read_text()) if (MD / "state.json").exists() else None
    if not st:
        print("sin estado todavía (el flujo no ha corrido)")
        return
    eq = st["cash"] + sum(p["tamano"] for p in st["open"])
    print(f"Última ejecución: {st['last_run']} · ejecuciones {st['runs']} · efectivo {st['cash']:.2f} · abiertas {len(st['open'])} · "
          f"patrimonio (coste) {eq:.2f} de {st['initial']:.2f}")
    if st["skipped_assets"]:
        print("Activos sin par USD en Kraken:", ", ".join(st["skipped_assets"]))
    for w in st["warnings"][-5:]:
        print("AVISO", w)
    for p in st["open"]:
        print(f"  abierta {p['activo']} p={p['p']:.2f} desde {p['entrada_ts']} entrada {p['entrada']} TP {p['tp_px']:.6g}")
    f = MD / "operaciones.csv"
    if not f.exists():
        print("Sin operaciones cerradas todavía.")
        return
    d = pd.read_csv(f)
    n = len(d)
    print(f"\nOperaciones cerradas: {n} · take-profit {int((d.motivo == 'take-profit').sum())} ({100*(d.motivo == 'take-profit').mean():.0f} %)")
    print(f"Por operación: bruto medio {d.bruto_pct.mean():+.2f} % (mediana {d.bruto_pct.median():+.2f}) · comisión {d.comision_pct.mean():.2f} % · "
          f"neto medio {d.neto_pct.mean():+.2f} % · ganadoras {100*(d.neto_pct > 0).mean():.0f} % · pnl total {d.pnl.sum():+.2f}")
    print("Referencia del backtest 2023-26 (tp8 sin stop): bruto +1,83 %, mediana +1,77, 62 % ganadoras.")
    print(d.tail(10)[["activo", "entrada_utc", "motivo", "min_abierta", "bruto_pct", "neto_pct"]].to_string(index=False))


if __name__ == "__main__":
    main()
