# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 07:01 UTC · vueltas 231 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.37 € (-3.56%) | 135 | 18 | 26% | -0.300% | -0.993% | -1.124% | -30.64 € |
| reversion_bb | 915.06 € (-0.99%) | 36 | 10 | 44% | +0.156% | -0.944% | -1.055% | -7.83 € |
| ruptura_volumen | 885.82 € (-4.16%) | 172 | 6 | 17% | -0.313% | -0.965% | -1.092% | -37.67 € |
| rebote_extremo | 922.91 € (-0.14%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.879% | -1.33 € |
| pullback_tendencia | 902.69 € (-2.33%) | 119 | 0 | 24% | -0.072% | -0.791% | -0.916% | -21.55 € |
| macd_momentum | 874.70 € (-5.36%) | 321 | 2 | 16% | -0.105% | -0.686% | -0.796% | -49.69 € |
| estocastico_rebote | 886.21 € (-4.12%) | 215 | 14 | 34% | -0.136% | -0.757% | -0.890% | -37.08 € |
| ruptura_estricta | 901.84 € (-2.42%) | 73 | 7 | 22% | -0.453% | -1.311% | -1.451% | -21.92 € |
| macd_sin_salida | 886.63 € (-4.07%) | 189 | 20 | 28% | -0.183% | -0.821% | -0.947% | -35.28 € |
| c_banda_atr_tope | 909.41 € (-1.60%) | 40 | 1 | 18% | -0.507% | -1.607% | -1.736% | -14.76 € |
| ruptura_volumen_tope | 908.19 € (-1.74%) | 63 | 1 | 16% | -0.208% | -1.127% | -1.246% | -16.28 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.963% | -38.90 € |
| ruptura_volumen_regimen | 895.82 € (-3.08%) | 121 | 5 | 17% | -0.284% | -0.999% | -1.129% | -27.59 € |
| c_banda_atr_evento | 894.41 € (-3.23%) | 103 | 18 | 22% | -0.415% | -1.171% | -1.302% | -27.59 € |
| macd_momentum_evento | 887.00 € (-4.03%) | 201 | 2 | 13% | -0.188% | -0.819% | -0.924% | -37.39 € |
| ruptura_volumen_evento | 891.28 € (-3.57%) | 113 | 6 | 10% | -0.517% | -1.251% | -1.380% | -32.20 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 07:00 | c_banda_atr_evento | RENDER | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 07:00 | macd_sin_salida | KAS | timeout | +0.36% | -0.14% | -0.03 |
| 2026-09-30 07:00 | macd_sin_salida | POL | stop-loss | -1.66% | -2.16% | -0.48 |
| 2026-09-30 07:00 | estocastico_rebote | ZRO | stop-loss | -1.67% | -2.17% | -0.48 |
| 2026-09-30 07:00 | c_banda_atr | RENDER | stop-loss | -1.50% | -2.00% | -0.45 |
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

## Eventos de la última vuelta

- 2026-09-30 07:00 [c_banda_atr] CIERRE RENDER stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 07:00 [c_banda_atr_evento] CIERRE RENDER stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 07:00 [estocastico_rebote] CIERRE ZRO stop-loss bruto -1.67% neto -2.17%
- 2026-09-30 07:00 [macd_sin_salida] CIERRE POL stop-loss bruto -1.66% neto -2.16%
- 2026-09-30 07:00 [macd_sin_salida] CIERRE KAS timeout bruto +0.37% neto -0.13%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
