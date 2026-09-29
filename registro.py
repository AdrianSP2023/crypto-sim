"""Registro permanente de operaciones en CSV (registro/operaciones.csv).

Una fila por operación cerrada, con todo lo necesario para analizar después:
fase, estrategia, familia, versión, activo, tipo, fechas de entrada y salida (UTC),
precios, cantidad, resultados bruto/comisión/neto/spread, motivo de salida y el
contexto de la señal (valores de los indicadores en la vela de la señal, en JSON).

`sync` es idempotente: compara con lo que ya hay en el fichero (fase, estrategia,
activo, entrada, salida) y añade solo lo que falta. El motor la llama en cada
vuelta, así que el CSV se autorrepara y no depende de cuándo se ejecute.

Uso manual (rellenar desde una fase archivada):
  python3 registro.py archive/P1
"""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
PATH = ROOT / "registro" / "operaciones.csv"
COLUMNS = ["fase", "estrategia", "familia", "version", "activo", "tipo", "entrada_utc", "salida_utc",
           "duracion_min", "precio_entrada", "precio_salida", "cantidad_eur", "bruto_pct", "comision_pct",
           "neto_pct", "coste_spread_pct", "neto_spread_pct", "comision_eur", "resultado_eur",
           "motivo_salida", "velas_5min", "hora_entrada_utc", "contexto_senal"]


def _t(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d %H:%M")


def row(c, fase, familia):
    fee = c.get("fee_pct", round(c["gross_pct"] - c["net_pct"], 3))
    return {
        "fase": fase, "estrategia": c["strategy"], "familia": familia, "version": c["version"], "activo": c["asset"],
        "tipo": "largo spot (compra->venta)", "entrada_utc": _t(c["entry_ts"]), "salida_utc": _t(c["exit_ts"]),
        "duracion_min": round((c["exit_ts"] - c["entry_ts"]) / 60), "precio_entrada": c["entry"],
        "precio_salida": c["exit"], "cantidad_eur": c["qty"], "bruto_pct": c["gross_pct"], "comision_pct": fee,
        "neto_pct": c["net_pct"], "coste_spread_pct": round(c["net_pct"] - c["net_spread_pct"], 3),
        "neto_spread_pct": c["net_spread_pct"], "comision_eur": round(c["qty"] * fee / 100, 4),
        "resultado_eur": c["pnl_eur"], "motivo_salida": c["reason"], "velas_5min": c["candles"],
        "hora_entrada_utc": datetime.fromtimestamp(c["entry_ts"], timezone.utc).hour,
        "contexto_senal": json.dumps(c["ctx"], ensure_ascii=False, separators=(",", ":")) if c.get("ctx") else "",
    }


def _key(r):
    return (r["fase"], r["estrategia"], r["activo"], r["entrada_utc"], r["salida_utc"])


def sync(state, cfg, fase=None, path=PATH):
    """Añade al CSV las operaciones cerradas de `state` que aún no estén. Devuelve cuántas añadió."""
    path = Path(path)
    fase = fase or state["phase"]
    path.parent.mkdir(exist_ok=True)
    keys, new = set(), not path.exists() or path.stat().st_size == 0
    if not new:
        with path.open(newline="", encoding="utf-8") as f:
            keys = {_key(r) for r in csv.DictReader(f)}
    rows = []
    for name, v in state["strategies"].items():
        fam = cfg.get("strategies", {}).get(name, {}).get("base", name)
        for c in v["closed"]:
            r = row(c, fase, fam)
            if _key(r) not in keys:
                rows.append(r)
    rows.sort(key=lambda r: (r["salida_utc"], r["estrategia"], r["activo"]))
    if rows:
        with path.open("a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if new:
                w.writeheader()
            w.writerows(rows)
    return len(rows)


VELAS_COLS = ["time", "open", "high", "low", "close", "vwap", "volume", "count"]


def guardar_velas(frames, state, minutes, base=None):
    """Guarda en datos/velas_<min>m/<ACTIVO>.csv todas las velas cerradas de cada activo (sin duplicar).
    Sirve para analizar después cualquier cosa: qué hizo el precio tras cada entrada o salida, patrones,
    re-simulaciones... Kraken solo devuelve las últimas 720 velas, así que lo no guardado se pierde."""
    base = Path(base) if base else ROOT / "datos" / f"velas_{minutes}m"
    base.mkdir(parents=True, exist_ok=True)
    last = state.setdefault("velas_last" if minutes == 5 else f"velas_last_{minutes}", {})
    n = 0
    for asset, df in frames.items():
        new = df[df.time > last.get(asset, 0)]
        if new.empty:
            continue
        f = base / (str(asset).replace("/", "_") + ".csv")
        cols = [c for c in VELAS_COLS if c in df.columns]
        new[cols].to_csv(f, mode="a", header=not f.exists() or f.stat().st_size == 0, index=False)
        last[asset] = int(new.time.max())
        n += len(new)
    return n


if __name__ == "__main__":
    d = ROOT / sys.argv[1]
    st = json.loads((d / "state" / "state.json").read_text())
    cf = json.loads((d / "config.json").read_text())
    print("filas añadidas:", sync(st, cf))
