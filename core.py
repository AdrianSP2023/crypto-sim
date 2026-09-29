"""
Núcleo del simulador: estado y proceso vela a vela. Sin red ni git: función
pura sobre el estado, para poder probarlo con datos sintéticos.

Reglas genéricas de salida (en este orden, dentro de cada vela cerrada):
  1. Stop-loss:   low <= entrada*(1-sl)  -> sale a min(open, nivel SL)
  2. Take-profit: high >= entrada*(1+tp) -> sale a max(open, nivel TP)
  3. Señal propia de la estrategia        -> sale al cierre
  4. Timeout (max_hold velas)             -> sale al cierre
Se evalúa el SL antes que el TP (conservador) y se respeta el hueco de apertura.

Coste por operación: comisión de ida y vuelta (config fee_round_trip) y,
aparte, el spread medido en Kraken al entrar y al salir. Se guardan tres
cifras: bruto, neto (comisión) y neto_spread (comisión + spread).
"""

from datetime import datetime, timezone

from strategies import REGISTRY, ema


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d %H:%M")


def new_state(cfg):
    return {
        "phase": cfg["phase"],
        "started_at": datetime.now(timezone.utc).isoformat(),
        "loops": 0,
        "last_loop": None,
        "universe": [],
        "last_candle": {},
        "strategies": {},
    }


def ensure_strategies(state, cfg):
    for name in cfg["strategies"]:
        state["strategies"].setdefault(name, {
            "cash": cfg["initial_cash"],
            "positions": {},
            "closed": [],
            "skipped_no_cash": 0,
        })
        state["strategies"][name].setdefault("blocked_filter", 0)
        state["strategies"][name].setdefault("blocked_exposure", 0)


def base_of(name, p):
    return p.get("base", name)


def market_breadth(frames, cfg):
    """Fracción de activos con cierre > EMA(n) en cada vela (timestamp -> 0..1).
    Solo usa datos hasta esa vela (la EMA es causal)."""
    n = cfg.get("breadth_ema", 50)
    up, tot = {}, {}
    for df in frames.values():
        above = (df.close > ema(df.close, n)).to_numpy()
        for t, a in zip(df.time.to_numpy(), above):
            t = int(t)
            tot[t] = tot.get(t, 0) + 1
            up[t] = up.get(t, 0) + int(a)
    return {t: up[t] / tot[t] for t in tot}


def prepare(frames, cfg):
    """Calcula indicadores por activo y estrategia (una vez por vuelta)."""
    out = {}
    for asset, df in frames.items():
        out[asset] = {}
        for name, p in cfg["strategies"].items():
            prep, _, _ = REGISTRY[base_of(name, p)]
            out[asset][name] = prep(df, p).reset_index(drop=True)
    return out


def process_frames(state, frames, cfg, log, spreads=None, events=None):
    """Procesa todas las velas cerradas nuevas de todos los activos en orden
    cronológico global (el tamaño de cada operación depende de la caja)."""
    spreads = spreads or {}
    ensure_strategies(state, cfg)
    prepared = prepare(frames, cfg)
    breadth = market_breadth(frames, cfg)
    evs = []
    for asset, df in frames.items():
        last = state["last_candle"].get(asset)
        if last is None:
            idx = [len(df) - 1]  # primer contacto: solo la última vela cerrada
        else:
            idx = [i for i in range(len(df)) if int(df.time.iat[i]) > last]
        evs += [(int(df.time.iat[i]), asset, i) for i in idx]
    order = list(frames)
    for ct, asset, i in sorted(evs, key=lambda e: (e[0], order.index(e[1]))):
        step(state, cfg, asset, prepared[asset], i, log, spreads.get(asset, 0.0), events, breadth.get(ct))
        state["last_candle"][asset] = ct


def step(state, cfg, asset, prepared_asset, i, log, spread, events, breadth=None):
    fee = cfg["fee_round_trip"]
    csec = cfg["candle_minutes"] * 60
    for name, p in cfg["strategies"].items():
        st = state["strategies"][name]
        d = prepared_asset[name]
        ct = int(d.time.iat[i])
        close_t = ct + csec
        prep, entry, exit_signal = REGISTRY[base_of(name, p)]
        pos = st["positions"].get(asset)

        if pos is not None:
            if ct <= pos["entry_candle"]:
                continue
            e = pos["entry_price"]
            o, h, l, c = d.open.iat[i], d.high.iat[i], d.low.iat[i], d.close.iat[i]
            px, why = None, None
            if l <= e * (1 - pos["sl"]):
                px, why = min(o, e * (1 - pos["sl"])), "stop-loss"
            elif h >= e * (1 + pos["tp"]):
                px, why = max(o, e * (1 + pos["tp"])), "take-profit"
            else:
                why = exit_signal(d, i, p)
                if why:
                    px = c
                elif (ct - pos["entry_candle"]) // csec >= pos["max_hold"]:
                    px, why = c, "timeout"
            if px is None:
                continue
            gross = px / e - 1
            net = gross - fee
            net_sp = net - (pos["spread_in"] + spread) / 2
            pnl = pos["qty"] * net
            st["cash"] += pos["qty"] + pnl
            rec = {
                "asset": asset, "strategy": name, "version": pos["version"],
                "entry_t": iso(pos["entry_candle"] + csec), "exit_t": iso(close_t),
                "entry_ts": pos["entry_candle"] + csec, "exit_ts": close_t,
                "entry": round(e, 10), "exit": round(px, 10), "qty": round(pos["qty"], 2),
                "gross_pct": round(gross * 100, 3), "net_pct": round(net * 100, 3),
                "net_spread_pct": round(net_sp * 100, 3), "pnl_eur": round(pnl, 3),
                "reason": why, "candles": int((ct - pos["entry_candle"]) // csec),
            }
            st["closed"].append(rec)
            del st["positions"][asset]
            log.append(f"{iso(close_t)} [{name}] CIERRE {asset} {why} bruto {gross*100:+.2f}% neto {net*100:+.2f}%")
            if events is not None:
                events.append({"type": "exit", **rec})
            continue

        if not p.get("enabled", True) or i < cfg["warmup"]:
            continue
        if not entry(d, i, p):
            continue
        mf = p.get("market_filter")
        if mf and (breadth is None or breadth < mf):
            st["blocked_filter"] += 1
            continue
        mo = p.get("max_open")
        if mo and len(st["positions"]) >= mo:
            st["blocked_exposure"] = st.get("blocked_exposure", 0) + 1
            continue
        equity_cost = st["cash"] + sum(x["qty"] for x in st["positions"].values())
        qty = min(st["cash"], cfg["position_pct"] * equity_cost)
        if qty < 5:
            st["skipped_no_cash"] += 1
            continue
        st["cash"] -= qty
        st["positions"][asset] = {
            "entry_price": float(d.close.iat[i]), "entry_candle": ct, "qty": qty,
            "tp": p["tp"], "sl": p["sl"], "max_hold": p["max_hold"],
            "spread_in": spread, "version": cfg["version"],
        }
        log.append(f"{iso(close_t)} [{name}] ENTRADA {asset} @ {d.close.iat[i]:.6g} ({qty:.2f} €)")
        if events is not None:
            events.append({"type": "entry", "asset": asset, "strategy": name, "version": cfg["version"],
                           "t": iso(close_t), "ts": close_t, "price": float(d.close.iat[i]), "qty": round(qty, 2),
                           "spread": round(spread, 5)})
