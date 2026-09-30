# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 06:56 UTC · vueltas 230 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.30 € (-3.56%) | 134 | 19 | 26% | -0.291% | -0.986% | -1.117% | -30.19 € |
| reversion_bb | 915.21 € (-0.98%) | 36 | 10 | 44% | +0.156% | -0.944% | -1.055% | -7.83 € |
| ruptura_volumen | 885.77 € (-4.16%) | 172 | 6 | 17% | -0.313% | -0.965% | -1.092% | -37.67 € |
| rebote_extremo | 922.89 € (-0.15%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.879% | -1.33 € |
| pullback_tendencia | 902.69 € (-2.33%) | 119 | 0 | 24% | -0.072% | -0.791% | -0.916% | -21.55 € |
| macd_momentum | 874.81 € (-5.35%) | 321 | 2 | 16% | -0.105% | -0.686% | -0.796% | -49.69 € |
| estocastico_rebote | 886.44 € (-4.09%) | 214 | 15 | 34% | -0.129% | -0.751% | -0.883% | -36.59 € |
| ruptura_estricta | 902.16 € (-2.39%) | 73 | 7 | 22% | -0.453% | -1.311% | -1.451% | -21.92 € |
| macd_sin_salida | 887.27 € (-4.00%) | 187 | 22 | 28% | -0.178% | -0.818% | -0.943% | -34.77 € |
| c_banda_atr_tope | 909.33 € (-1.61%) | 40 | 1 | 18% | -0.507% | -1.607% | -1.736% | -14.76 € |
| ruptura_volumen_tope | 908.23 € (-1.73%) | 63 | 1 | 16% | -0.208% | -1.127% | -1.246% | -16.28 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.963% | -38.90 € |
| ruptura_volumen_regimen | 895.77 € (-3.08%) | 121 | 5 | 17% | -0.284% | -0.999% | -1.129% | -27.59 € |
| c_banda_atr_evento | 894.34 € (-3.24%) | 102 | 19 | 23% | -0.404% | -1.163% | -1.294% | -27.14 € |
| macd_momentum_evento | 887.11 € (-4.02%) | 201 | 2 | 13% | -0.188% | -0.819% | -0.924% | -37.39 € |
| ruptura_volumen_evento | 891.23 € (-3.57%) | 113 | 6 | 10% | -0.517% | -1.251% | -1.380% | -32.20 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 06:55 | ruptura_volumen_evento | XPL | stop-loss | -2.00% | -2.50% | -0.56 |
| 2026-09-30 06:55 | macd_momentum_evento | SUI | momentum perdido | +0.05% | -0.45% | -0.10 |
| 2026-09-30 06:55 | ruptura_estricta | XPL | stop-loss | -2.91% | -3.41% | -0.77 |
| 2026-09-30 06:55 | ruptura_estricta | ASTER | stop-loss | -2.04% | -2.54% | -0.57 |
| 2026-09-30 06:55 | macd_momentum | SUI | momentum perdido | +0.05% | -0.45% | -0.10 |
| 2026-09-30 06:55 | ruptura_volumen | XPL | stop-loss | -2.00% | -2.50% | -0.56 |
| 2026-09-30 06:55 | reversion_bb | ATOM | timeout | -0.81% | -1.91% | -0.44 |
| 2026-09-30 06:50 | ruptura_volumen_evento | WLD | timeout | -0.43% | -0.93% | -0.21 |
| 2026-09-30 06:50 | ruptura_volumen_evento | CRV | stop-loss | -1.36% | -1.86% | -0.42 |
| 2026-09-30 06:50 | ruptura_volumen_evento | AAVE | timeout | -0.85% | -1.35% | -0.30 |
| 2026-09-30 06:50 | ruptura_volumen_evento | QNT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 06:50 | c_banda_atr_evento | FIL | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:50 | c_banda_atr_evento | TRX | timeout | +0.47% | -0.04% | -0.01 |
| 2026-09-30 06:50 | c_banda_atr_evento | ADA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:50 | ruptura_volumen_regimen | CRV | stop-loss | -1.36% | -1.86% | -0.42 |

## Eventos de la última vuelta

- 2026-09-30 06:55 [macd_momentum] CIERRE SUI momentum perdido bruto +0.05% neto -0.45%
- 2026-09-30 06:55 [macd_momentum_evento] CIERRE SUI momentum perdido bruto +0.05% neto -0.45%
- 2026-09-30 06:55 [reversion_bb] CIERRE ATOM timeout bruto -0.81% neto -1.91%
- 2026-09-30 06:50 [reversion_bb] ENTRADA OP @ 0.1135 (22.91 €, apertura)
- 2026-09-30 06:50 [estocastico_rebote] ENTRADA BNB @ 666.91 (22.19 €, apertura)
- 2026-09-30 06:50 [rebote_extremo] ENTRADA TRUMP @ 1.777 (23.07 €, apertura)
- 2026-09-30 06:55 [ruptura_estricta] CIERRE ASTER stop-loss bruto -2.04% neto -2.54%
- 2026-09-30 06:55 [ruptura_volumen] CIERRE XPL stop-loss bruto -2.00% neto -2.50%
- 2026-09-30 06:55 [ruptura_estricta] CIERRE XPL stop-loss bruto -2.91% neto -3.41%
- 2026-09-30 06:55 [ruptura_volumen_evento] CIERRE XPL stop-loss bruto -2.00% neto -2.50%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
