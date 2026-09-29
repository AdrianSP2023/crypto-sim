"""Paper trader del modelo de precursores (cuenta propia, aparte del motor de 5 min).

Cada hora (a los :02) : 1) baja las velas de 1 h de Kraken (USD) de los activos del modelo, 2) calcula los rasgos de la última vela CERRADA,
3) puntúa con modelo/modelo.joblib, 4) si p >= umbral y no hay posición en ese activo, compra (paper) al ASK actual,
5) gestiona las posiciones abiertas: take-profit +8 % (orden límite, sin stop-loss) o salida por tiempo a las 4 h al BID.
Receta validada en tools/analisis_modelo_1m.py (tp8_slx: +1,83 % bruto por operación en test 2023-26).
Estado en modelo/state.json; operaciones cerradas en modelo/operaciones.csv; señales (p >= 0,4) en modelo/senales.csv.
Los precios y comisiones son SIMULADOS. Comisión por lado según volumen a 30 días (mismos tramos que el motor).
"""
import csv
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from modelo.features import COLS, REQ, panel_features  # noqa: E402

MD = ROOT / "modelo"
API = "https://api.kraken.com/0/public"
ALIASES = {"XBT": "BTC", "XDG": "DOGE"}
CFG = {"size_pct": 0.025, "max_open": 8, "tp": 0.08, "hold_min": 240, "initial_cash": 924.24,
       "fee_tiers": [{"from": 0, "side": 0.0055}, {"from": 2000, "side": 0.0025}, {"from": 50000, "side": 0.0021}],
       "min_p_log": 0.4, "max_retraso_min": 30}
S = requests.Session()
OP_COLS = ["activo", "senal_utc", "entrada_utc", "salida_utc", "p", "entrada", "salida", "motivo", "min_abierta", "bruto_pct",
           "comision_pct", "neto_pct", "tamano", "pnl", "spread_entrada_pct", "retraso_min"]


def now_ts():
    return int(time.time())


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def kraken(path, params=None, tries=3):
    for k in range(tries):
        try:
            r = S.get(f"{API}/{path}", params=params, timeout=20)
            r.raise_for_status()
            j = r.json()
            if j.get("error"):
                raise RuntimeError(", ".join(j["error"]))
            return j["result"]
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(2 + 3 * k)


class Kraken:
    """Acceso real a Kraken; los tests lo sustituyen por un simulador con los mismos métodos."""

    def pairs(self, assets):
        """activo -> {'pair': altname, 'key': clave del resultado de Ticker}"""
        res = kraken("AssetPairs")
        out = {}
        for key, v in res.items():
            ws = v.get("wsname", "")
            if "/" not in ws or v.get("status", "online") != "online" or key.endswith(".d"):
                continue
            base, quote = ws.split("/")
            base = ALIASES.get(base, base)
            if quote == "USD" and base in assets:
                out[base] = {"pair": v["altname"], "key": key}
        return out

    def ohlc(self, pair):
        res = kraken("OHLC", {"pair": pair, "interval": 60})
        key = next(k for k in res if k != "last")
        df = pd.DataFrame(res[key], columns=["time", "open", "high", "low", "close", "vwap", "volume", "trades"])
        df["time"] = df["time"].astype(int)
        for c in ["open", "high", "low", "close", "volume", "trades"]:
            df[c] = df[c].astype(float)
        return df.sort_values("time").reset_index(drop=True)

    def tickers(self, pairs):
        res = kraken("Ticker", {"pair": ",".join(v["pair"] for v in pairs.values())})
        by_key = {v["key"]: a for a, v in pairs.items()}
        by_alt = {v["pair"]: a for a, v in pairs.items()}
        out = {}
        for key, t in res.items():
            a = by_key.get(key) or by_alt.get(key)
            if a:
                out[a] = {"ask": float(t["a"][0]), "bid": float(t["b"][0]), "last": float(t["c"][0])}
        return out


def side_fee(state, ts):
    v = sum(e for (t, e) in state["volume"] if ts - t <= 30 * 86400)
    fee = CFG["fee_tiers"][0]["side"]
    for tier in CFG["fee_tiers"]:
        if v >= tier["from"]:
            fee = tier["side"]
    return fee


def new_state():
    return {"initial": CFG["initial_cash"], "cash": CFG["initial_cash"], "open": [], "volume": [], "n_closed": 0,
            "last_run": None, "warnings": [], "skipped_assets": [], "runs": 0}


def load_state():
    p = MD / "state.json"
    return json.loads(p.read_text()) if p.exists() else new_state()


def to_panel(frames, ts):
    """frames: activo -> DataFrame de velas de Kraken. Solo velas cerradas; reindexa por hora (huecos = NaN), índice = inicio de vela."""
    panel = {}
    for a, df in frames.items():
        df = df[df.time + 3600 <= ts]
        if len(df) < 200:
            continue
        d = df.set_index(pd.to_datetime(df.time, unit="s"))[["open", "high", "low", "close", "volume", "trades"]]
        d = d[~d.index.duplicated()]
        panel[a] = d.reindex(pd.date_range(d.index.min(), d.index.max(), freq="h"))
    return panel


def score(panel, model, ts):
    """Puntuación de la última vela cerrada de cada activo. Devuelve DataFrame (activo, hora, p)."""
    X = panel_features(panel)
    last_start = pd.to_datetime((ts // 3600) * 3600 - 3600, unit="s")
    Z = X[X.index == last_start].dropna(subset=REQ)
    if Z.empty:
        return pd.DataFrame(columns=["activo", "hora", "p"])
    p = model.predict_proba(Z[COLS])[:, 1]
    return pd.DataFrame({"activo": Z.activo.to_numpy(), "hora": last_start, "p": p})


def manage_open(state, frames, tick, ts, log):
    """Cierra por take-profit o por tiempo. TP: máximo de las velas posteriores a la de entrada o bid >= TP (orden límite)."""
    still, closed = [], []
    for pos in state["open"]:
        a = pos["activo"]
        reason, px = None, None
        df = frames.get(a)
        tp_px = pos["tp_px"]
        if df is not None:
            hi = df[df.time > pos["entrada_ts"]].high.max()          # velas posteriores a la de entrada (incluye la vela en curso)
            if pd.notna(hi) and hi >= tp_px:
                reason, px = "take-profit", tp_px
        t = tick.get(a)
        if reason is None and t is not None and t["bid"] >= tp_px:
            reason, px = "take-profit", tp_px
        if reason is None and ts >= pos["vence_ts"] and t is not None:
            reason, px = "tiempo", t["bid"]
        if reason is None and ts >= pos["vence_ts"] + 6 * 3600 and df is not None and len(df):
            reason, px = "tiempo (sin cotización)", float(df.close.iloc[-1])
        if reason is None:
            still.append(pos)
            continue
        fee_out = side_fee(state, ts)
        units = pos["unidades"]
        proceeds = units * px
        comm = proceeds * fee_out
        pnl = proceeds - comm - pos["tamano"] - pos["fee_in"]
        state["cash"] += proceeds - comm
        state["volume"].append([ts, proceeds])
        closed.append({"activo": a, "senal_utc": pos["senal_utc"], "entrada_utc": iso(pos["entrada_ts"]), "salida_utc": iso(ts),
                       "p": round(pos["p"], 4), "entrada": pos["entrada"], "salida": px, "motivo": reason,
                       "min_abierta": round((ts - pos["entrada_ts"]) / 60), "bruto_pct": round(100 * (px / pos["entrada"] - 1), 3),
                       "comision_pct": round(100 * (pos["fee_in"] + comm) / pos["tamano"], 3),
                       "neto_pct": round(100 * pnl / pos["tamano"], 3), "tamano": round(pos["tamano"], 2), "pnl": round(pnl, 3),
                       "spread_entrada_pct": pos["spread_pct"], "retraso_min": pos["retraso_min"]})
        log(f"cierre {a} {reason} {closed[-1]['neto_pct']:+.2f}%")
    state["open"] = still
    return closed


def open_new(state, sc, tick, ts, thr, log):
    opened = []
    held = {p["activo"] for p in state["open"]}
    retraso = (ts % 3600) / 60
    for _, r in sc.sort_values("p", ascending=False).iterrows():
        if r.p < thr or r.activo in held:
            continue
        if len(state["open"]) >= CFG["max_open"]:
            log(f"señal {r.activo} p={r.p:.3f} ignorada: máximo de posiciones abiertas")
            continue
        t = tick.get(r.activo)
        if t is None or t["ask"] <= 0:
            log(f"señal {r.activo} sin cotización")
            continue
        if retraso > CFG["max_retraso_min"]:
            log(f"señal {r.activo} ignorada: retraso {retraso:.0f} min")
            continue
        equity = state["cash"] + sum(p["tamano"] for p in state["open"])
        size = min(CFG["size_pct"] * equity, state["cash"])
        if size < 5:
            continue
        fee = side_fee(state, ts)
        px = t["ask"]
        pos = {"activo": r.activo, "senal_utc": str(r.hora), "entrada_ts": ts, "entrada": px, "tamano": size,
               "unidades": size / px, "fee_in": size * fee, "tp_px": px * (1 + CFG["tp"]), "vence_ts": ts + CFG["hold_min"] * 60,
               "p": float(r.p), "spread_pct": round(100 * (t["ask"] - t["bid"]) / ((t["ask"] + t["bid"]) / 2), 3),
               "retraso_min": round(retraso, 1)}
        state["cash"] -= size + pos["fee_in"]
        state["volume"].append([ts, size])
        state["open"].append(pos)
        held.add(r.activo)
        opened.append(pos)
        log(f"compra {r.activo} p={r.p:.3f} a {px}")
    return opened


def step(state, model, thr, kr, ts, log=print):
    assets = json.loads((MD / "meta.json").read_text())["activos"]
    pairs = kr.pairs(set(assets))
    missing = sorted(set(assets) - set(pairs))
    state["skipped_assets"] = missing
    frames = {}
    for a, pair in pairs.items():
        try:
            frames[a] = kr.ohlc(pair["pair"])
        except Exception as e:  # un activo caído no debe parar al resto
            state["warnings"].append(f"{iso(ts)} ohlc {a}: {e}")
        time.sleep(float(os.environ.get("KRAKEN_PAUSA", "1.0")))
    tick = kr.tickers({a: pairs[a] for a in frames})
    closed = manage_open(state, frames, tick, ts, log)
    panel = to_panel(frames, ts)
    sc = score(panel, model, ts) if "BTC" in panel else pd.DataFrame(columns=["activo", "hora", "p"])
    if "BTC" not in panel:
        state["warnings"].append(f"{iso(ts)} sin BTC: no se puntúa")
    opened = open_new(state, sc, tick, ts, thr, log)
    state["ultimo_top"] = [[r.activo, round(float(r.p), 3)] for _, r in sc.sort_values("p", ascending=False).head(5).iterrows()]
    state["n_puntuados"] = int(len(sc))
    state["last_run"] = iso(ts)
    state["runs"] += 1
    state["warnings"] = state["warnings"][-20:]
    return closed, opened, sc


def append_csv(path, cols, rows):
    new = not path.exists()
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        if new:
            w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k) for k in cols})


def save(state, closed, sc, ts):
    (MD / "state.json").write_text(json.dumps(state, indent=1))
    if closed:
        append_csv(MD / "operaciones.csv", OP_COLS, closed)
    hi = sc[sc.p >= CFG["min_p_log"]]
    if len(hi):
        append_csv(MD / "senales.csv", ["hora", "activo", "p"], [{"hora": str(r.hora), "activo": r.activo, "p": round(r.p, 4)} for _, r in hi.iterrows()])


def sh(*a):
    return subprocess.run(a, cwd=ROOT, capture_output=True, text=True)


def main():
    meta = json.loads((MD / "meta.json").read_text())
    model = joblib.load(MD / "modelo.joblib")
    state = load_state()
    ts = now_ts()
    closed, opened, sc = step(state, model, meta["umbral"], Kraken(), ts)
    save(state, closed, sc, ts)
    sh("git", "config", "user.name", "modelo-precursores")
    sh("git", "config", "user.email", "modelo-precursores@users.noreply.github.com")
    for f in ("state.json", "operaciones.csv", "senales.csv"):
        if (MD / f).exists():
            r = sh("git", "add", f"modelo/{f}")
            if r.returncode:
                print("git add", f, r.stderr)
    if sh("git", "diff", "--cached", "--quiet").returncode == 0:
        print("sin cambios")
        return
    sh("git", "commit", "-q", "-m", f"modelo {iso(ts)[:16]}Z abiertas {len(state['open'])} cierres {len(closed)}")
    for k in range(5):
        sh("git", "pull", "-q", "--rebase", "-X", "theirs")
        if sh("git", "push", "-q").returncode == 0:
            return
        time.sleep(4 * (k + 1))
    print("no se pudo hacer push")
    sys.exit(1)


if __name__ == "__main__":
    main()
