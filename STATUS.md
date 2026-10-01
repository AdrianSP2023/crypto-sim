# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 16:21 UTC · vueltas 263 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.38 € (-3.77%) | 216 | 21 | 33% | -0.085% | -0.706% | -0.830% | -34.72 € |
| reversion_bb | 916.15 € (-0.88%) | 38 | 9 | 39% | +0.067% | -1.033% | -1.133% | -9.04 € |
| ruptura_volumen | 879.28 € (-4.86%) | 243 | 10 | 23% | -0.212% | -0.820% | -0.928% | -45.11 € |
| rebote_extremo | 921.95 € (-0.25%) | 12 | 1 | 50% | +0.217% | -0.883% | -1.057% | -2.45 € |
| pullback_tendencia | 893.09 € (-3.37%) | 146 | 6 | 14% | -0.268% | -0.949% | -1.050% | -31.54 € |
| macd_momentum | 873.88 € (-5.45%) | 369 | 19 | 20% | -0.034% | -0.605% | -0.713% | -50.27 € |
| estocastico_rebote | 877.96 € (-5.01%) | 283 | 4 | 31% | -0.135% | -0.727% | -0.839% | -46.57 € |
| ruptura_estricta | 885.96 € (-4.14%) | 138 | 6 | 23% | -0.536% | -1.227% | -1.349% | -38.60 € |
| macd_sin_salida | 882.20 € (-4.55%) | 261 | 22 | 34% | -0.106% | -0.706% | -0.822% | -41.90 € |
| c_banda_atr_tope | 912.17 € (-1.31%) | 50 | 5 | 28% | -0.015% | -1.043% | -1.156% | -11.99 € |
| ruptura_volumen_tope | 908.54 € (-1.70%) | 81 | 4 | 26% | -0.038% | -0.864% | -0.978% | -16.05 € |
| c_banda_atr_regimen | 901.88 € (-2.42%) | 110 | 2 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.67 € (-3.31%) | 207 | 1 | 22% | -0.021% | -0.647% | -0.760% | -30.54 € |
| ruptura_volumen_regimen | 883.24 € (-4.44%) | 186 | 4 | 19% | -0.327% | -0.968% | -1.083% | -40.85 € |
| c_banda_atr_evento | 895.30 € (-3.13%) | 183 | 21 | 34% | -0.044% | -0.689% | -0.807% | -28.79 € |
| macd_momentum_evento | 878.73 € (-4.92%) | 322 | 19 | 18% | -0.043% | -0.625% | -0.729% | -45.43 € |
| ruptura_volumen_evento | 891.79 € (-3.51%) | 193 | 10 | 24% | -0.105% | -0.742% | -0.839% | -32.59 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 16:20 | macd_momentum_evento | UNI | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-10-01 16:20 | macd_momentum_regimen | UNI | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-10-01 16:20 | ruptura_volumen_tope | ZRO | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 16:20 | ruptura_estricta | ZRO | take-profit | +3.00% | +2.50% | +0.55 |
| 2026-10-01 16:20 | estocastico_rebote | LINK | timeout | +0.69% | +0.19% | +0.04 |
| 2026-10-01 16:20 | estocastico_rebote | BTC | timeout | +1.36% | +0.86% | +0.19 |
| 2026-10-01 16:20 | macd_momentum | UNI | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-10-01 16:15 | ruptura_volumen_evento | VVV | stop-loss | -1.32% | -1.82% | -0.41 |
| 2026-10-01 16:15 | ruptura_volumen_evento | ZRO | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 16:15 | macd_momentum_evento | ZRO | take-profit | +2.07% | +1.57% | +0.34 |
| 2026-10-01 16:15 | macd_momentum_evento | AAVE | momentum perdido | -1.16% | -1.66% | -0.36 |
| 2026-10-01 16:15 | ruptura_volumen_regimen | VVV | stop-loss | -1.32% | -1.82% | -0.40 |
| 2026-10-01 16:15 | macd_sin_salida | ZRO | take-profit | +2.07% | +1.57% | +0.34 |
| 2026-10-01 16:15 | estocastico_rebote | KSM | timeout | +0.22% | -0.28% | -0.06 |
| 2026-10-01 16:15 | estocastico_rebote | BCH | timeout | +0.60% | +0.10% | +0.02 |

## Eventos de la última vuelta

- 2026-10-01 16:20 [estocastico_rebote] CIERRE BTC timeout bruto +1.36% neto +0.86%
- 2026-10-01 16:20 [estocastico_rebote] CIERRE LINK timeout bruto +0.69% neto +0.19%
- 2026-10-01 16:20 [macd_momentum] CIERRE UNI momentum perdido bruto -0.04% neto -0.54%
- 2026-10-01 16:20 [macd_momentum_regimen] CIERRE UNI momentum perdido bruto -0.04% neto -0.54%
- 2026-10-01 16:20 [macd_momentum_evento] CIERRE UNI momentum perdido bruto -0.04% neto -0.54%
- 2026-10-01 16:20 [ruptura_estricta] CIERRE ZRO take-profit bruto +3.00% neto +2.50%
- 2026-10-01 16:20 [ruptura_volumen_tope] CIERRE ZRO take-profit bruto +2.50% neto +2.00%
- 2026-10-01 16:15 [pullback_tendencia] ENTRADA TON @ 1.347 (22.32 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
