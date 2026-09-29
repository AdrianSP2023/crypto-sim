#!/usr/bin/env python3
"""
Motor continuo de P1 (paper trading, sin dinero real).

Corre en GitHub Actions en bucle durante ~5 h 45 min. Al cerrarse cada vela
de 5 min descarga los datos de Kraken, procesa las estrategias y hace commit
del estado en el repo. Luego termina y la siguiente ejecución encolada
continúa donde se quedó; el estado persiste en el repo y no se pierde
ninguna vela.

Ajustes in situ: en cada vuelta hace `git pull` y relee config.json. Si
cambia el código del motor o de las estrategias, sale para que la siguiente
ejecución arranque con el código nuevo.
"""

import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

import core

ROOT = Path(__file__).parent
CONFIG = ROOT / "config.json"
STATE = ROOT / "state" / "state.json"
EVENTS = ROOT / "state" / "events.jsonl"
STATUS = ROOT / "STATUS.md"
CODE_FILES = ["engine.py", "core.py", "strategies.py", "registro.py"]
API = "https://api.kraken.com/0/public"
ALIASES = {"XBT": "BTC", "XDG": "DOGE"}

S = requests.Session()


def now():
    return datetime.now(timezone.utc)


def code_hash():
    h = hashlib.sha256()
    for f in CODE_FILES:
        h.update((ROOT / f).read_bytes())
    return h.hexdigest()


def sh(*args, check=True):
    return subprocess.run(args, cwd=ROOT, check=check, capture_output=True, text=True)


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


# ------------------------------------------------------------------ universo

def resolve_universe(cfg):
    u = cfg["universe"]
    pairs = kraken("AssetPairs")
    cands = {}
    for key, v in pairs.items():
        ws = v.get("wsname", "")
        if "/" not in ws or v.get("status", "online") != "online":
            continue
        base, quote = ws.split("/")
        base = ALIASES.get(base, base)
        if quote != u["quote"] or base in u["exclude_bases"] or key.endswith(".d"):
            continue
        cands[key] = {"asset": base, "pair": v["altname"], "key": key}
    tick = kraken("Ticker", {"pair": ",".join(c["pair"] for c in cands.values())})
    rows = []
    for key, t in tick.items():
        if key not in cands:
            continue
        ask, bid = float(t["a"][0]), float(t["b"][0])
        mid = (ask + bid) / 2
        if mid <= 0:
            continue
        spread = (ask - bid) / mid
        vol_eur = float(t["v"][1]) * float(t["p"][1])
        if spread <= u["max_spread"]:
            rows.append({**cands[key], "vol_eur_24h": round(vol_eur), "spread": round(spread, 5)})
    rows.sort(key=lambda r: -r["vol_eur_24h"])
    return rows[: u["top_n"]]


def fetch_spreads(universe):
    tick = kraken("Ticker", {"pair": ",".join(x["pair"] for x in universe)})
    by_key = {x["key"]: x["asset"] for x in universe}
    by_alt = {x["pair"]: x["asset"] for x in universe}
    out = {}
    for key, t in tick.items():
        a = by_key.get(key) or by_alt.get(key)
        if not a:
            continue
        ask, bid = float(t["a"][0]), float(t["b"][0])
        mid = (ask + bid) / 2
        if mid > 0:
            out[a] = (ask - bid) / mid
    return out


def fetch_ohlc(pair, minutes, now_ts):
    res = kraken("OHLC", {"pair": pair, "interval": minutes})
    key = next(k for k in res if k != "last")
    df = pd.DataFrame(res[key], columns=["time", "open", "high", "low", "close", "vwap", "volume", "count"])
    df["time"] = df["time"].astype(int)
    for c in ["open", "high", "low", "close", "volume"]:
        df[c] = df[c].astype(float)
    # Solo velas cerradas: Kraken incluye la vela en curso como última fila
    return df[df.time + minutes * 60 <= now_ts].sort_values("time").reset_index(drop=True)


# ------------------------------------------------------------------- estado

def load_json(p, default):
    return json.loads(p.read_text()) if p.exists() else default


def save_all(state, events, cfg, warnings, log):
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(state, ensure_ascii=False, separators=(",", ":")))
    if events:
        with EVENTS.open("a") as f:
            for e in events:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")
    import report
    STATUS.write_text(report.status_md(state, cfg, warnings, log))
    try:
        import registro
        registro.sync(state, cfg)
    except Exception as ex:  # el registro nunca debe parar el motor
        warnings.append(f"registro CSV: {ex}")


def git_sync(msg):
    sh("git", "add", "state", "STATUS.md", "registro", "datos")
    if sh("git", "diff", "--cached", "--quiet", check=False).returncode == 0:
        return
    sh("git", "commit", "-q", "-m", msg)
    for k in range(4):
        sh("git", "pull", "-q", "--rebase", "-X", "theirs", check=False)
        if sh("git", "push", "-q", check=False).returncode == 0:
            return
        time.sleep(3 + 5 * k)
    print("AVISO: no se pudo hacer push; se reintentará en la siguiente vuelta")


# ---------------------------------------------------------------------- bucle

def one_loop(state, cfg):
    warnings, log, events = [], [], []
    ts = int(now().timestamp())
    if not state["universe"] or state.get("universe_cfg") != cfg["universe"]:
        state["universe"] = resolve_universe(cfg)
        state["universe_cfg"] = cfg["universe"]
        events.append({"type": "universe", "t": now().isoformat(), "assets": [x["asset"] for x in state["universe"]]})
    try:
        spreads = fetch_spreads(state["universe"])
    except Exception as e:
        spreads = {}
        warnings.append(f"sin spreads de Kraken ({e})")
    frames = {}
    for x in state["universe"]:
        try:
            df = fetch_ohlc(x["pair"], cfg["candle_minutes"], ts)
            if len(df) > cfg["warmup"] + 2:
                frames[x["asset"]] = df
            else:
                warnings.append(f"{x['asset']}: solo {len(df)} velas")
        except Exception as e:
            warnings.append(f"{x['asset']}: sin datos ({e})")
        time.sleep(0.6)  # ~1 petición/s: límite de la API pública de Kraken
    core.process_frames(state, frames, cfg, log, spreads, events)
    try:
        import registro
        registro.guardar_velas(frames, state, cfg["candle_minutes"])
    except Exception as ex:  # guardar precios nunca debe parar el motor
        warnings.append(f"guardar velas: {ex}")
    if cfg.get("record_1m", True):
        # Velas de 1 min solo para registro y análisis (no las usa ninguna estrategia). Kraken devuelve 12 h por
        # petición, así que cada vuelta recupera lo que falte. Con límite de tiempo para no retrasar el ciclo de 5 min.
        t_1m, f1, fails = time.time(), {}, 0
        for x in state["universe"]:
            if time.time() - t_1m > 150:
                warnings.append("velas 1m: cortado por tiempo")
                break
            try:
                f1[x["asset"]] = fetch_ohlc(x["pair"], 1, ts)
            except Exception:
                fails += 1
            time.sleep(0.6)
        if fails:
            warnings.append(f"velas 1m: {fails} activos sin datos")
        try:
            registro.guardar_velas(f1, state, 1)
        except Exception as ex:
            warnings.append(f"guardar velas 1m: {ex}")
    prev = state.get("last_loop")
    if prev:
        gap = (now() - datetime.fromisoformat(prev)).total_seconds() / 60
        if gap > 15:
            state.setdefault("loop_gaps", []).append([ts, round(gap, 1)])
            warnings.append(f"hueco de {gap:.0f} min entre vueltas")
    state["loops"] += 1
    state["last_loop"] = now().isoformat()
    state["last_prices"] = {a: float(df.close.iat[-1]) for a, df in frames.items()}
    snaps = state.setdefault("snapshots", [])
    if not snaps or ts - snaps[-1]["ts"] >= 3600 - 120:
        snaps.append({"ts": ts, "prices": {a: round(x, 10) for a, x in state["last_prices"].items()},
                      "equity": core.equity_marked(state, cfg, state["last_prices"])})
        del snaps[:-24 * 8]
    state["last_warnings"] = warnings
    return warnings, log, events


def main():
    run_minutes = float(os.environ.get("RUN_MINUTES", "345"))
    deadline = time.time() + run_minutes * 60
    start_hash = code_hash()
    first = True
    while time.time() < deadline:
        if not first:
            cm = json.loads(CONFIG.read_text())["candle_minutes"] * 60
            wake = (int(time.time()) // cm + 1) * cm + 20  # 20 s tras el cierre de la vela
            if wake > deadline:
                break
            time.sleep(max(0, wake - time.time()))
            sh("git", "pull", "-q", "--rebase", "-X", "theirs", check=False)
            if code_hash() != start_hash:
                print("Código cambiado: salgo para relanzar con la versión nueva")
                break
        first = False
        cfg = json.loads(CONFIG.read_text())
        end = cfg.get("phase_end_utc")
        if not cfg.get("enabled", True) or (end and now().isoformat() >= end):
            print("Motor desactivado o fase terminada: no se opera")
            break
        state = load_json(STATE, None) or core.new_state(cfg)
        if state.get("phase") != cfg["phase"]:
            print(f"Fase de config ({cfg['phase']}) distinta de la del estado ({state.get('phase')}): archivar antes")
            break
        try:
            warnings, log, events = one_loop(state, cfg)
        except Exception as e:
            print("ERROR en la vuelta:", e)
            continue
        save_all(state, events, cfg, warnings, log)
        git_sync(f"{cfg['phase']} {cfg['version']} {now().strftime('%Y-%m-%d %H:%M')}Z")
        for x in warnings + log:
            print(x)
        print(f"{now().isoformat()} vuelta {state['loops']}: {len(log)} eventos, {len(warnings)} avisos")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
