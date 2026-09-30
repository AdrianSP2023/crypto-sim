# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 06:01 UTC · vueltas 219 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.28 € (-2.81%) | 125 | 28 | 28% | -0.232% | -0.941% | -1.077% | -26.94 € |
| reversion_bb | 917.70 € (-0.71%) | 34 | 6 | 47% | +0.236% | -0.865% | -0.970% | -6.78 € |
| ruptura_volumen | 892.09 € (-3.48%) | 155 | 21 | 19% | -0.261% | -0.929% | -1.055% | -32.79 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.38 € (-2.15%) | 114 | 4 | 25% | -0.038% | -0.767% | -0.894% | -20.04 € |
| macd_momentum | 878.37 € (-4.96%) | 299 | 22 | 17% | -0.094% | -0.681% | -0.795% | -46.06 € |
| estocastico_rebote | 890.43 € (-3.66%) | 202 | 13 | 35% | -0.096% | -0.725% | -0.857% | -33.44 € |
| ruptura_estricta | 904.36 € (-2.15%) | 70 | 10 | 23% | -0.383% | -1.256% | -1.396% | -20.15 € |
| macd_sin_salida | 893.23 € (-3.35%) | 180 | 28 | 29% | -0.135% | -0.780% | -0.907% | -31.97 € |
| c_banda_atr_tope | 910.78 € (-1.46%) | 37 | 4 | 19% | -0.476% | -1.576% | -1.712% | -13.40 € |
| ruptura_volumen_tope | 909.91 € (-1.55%) | 57 | 5 | 18% | -0.161% | -1.124% | -1.243% | -14.70 € |
| c_banda_atr_regimen | 900.80 € (-2.54%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.13 € (-4.12%) | 198 | 4 | 15% | -0.213% | -0.845% | -0.959% | -37.99 € |
| ruptura_volumen_regimen | 898.39 € (-2.80%) | 116 | 10 | 18% | -0.234% | -0.959% | -1.087% | -25.40 € |
| c_banda_atr_evento | 901.34 € (-2.48%) | 93 | 28 | 25% | -0.336% | -1.120% | -1.259% | -23.88 € |
| macd_momentum_evento | 890.72 € (-3.63%) | 179 | 22 | 13% | -0.180% | -0.827% | -0.939% | -33.71 € |
| ruptura_volumen_evento | 897.59 € (-2.88%) | 96 | 21 | 11% | -0.470% | -1.245% | -1.370% | -27.29 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 06:00 | macd_momentum_evento | BNB | momentum perdido | +0.07% | -0.43% | -0.10 |
| 2026-09-30 06:00 | macd_momentum_evento | VIRTUAL | momentum perdido | +0.46% | -0.04% | -0.01 |
| 2026-09-30 06:00 | macd_momentum_evento | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:00 | macd_momentum_regimen | QNT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-09-30 06:00 | macd_sin_salida | DOT | timeout | -0.33% | -0.83% | -0.19 |
| 2026-09-30 06:00 | macd_sin_salida | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:00 | macd_momentum | BNB | momentum perdido | +0.07% | -0.43% | -0.09 |
| 2026-09-30 06:00 | macd_momentum | VIRTUAL | momentum perdido | +0.46% | -0.04% | -0.01 |
| 2026-09-30 06:00 | macd_momentum | QNT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-09-30 06:00 | pullback_tendencia | DOT | rotura de tendencia | -0.48% | -0.98% | -0.22 |
| 2026-09-30 06:00 | reversion_bb | TRX | timeout | +0.92% | -0.18% | -0.04 |
| 2026-09-30 05:55 | macd_momentum_evento | WLD | take-profit | +2.01% | +1.51% | +0.34 |
| 2026-09-30 05:55 | c_banda_atr_evento | MINA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 05:55 | c_banda_atr_tope | SEI | timeout | +0.17% | -0.93% | -0.21 |
| 2026-09-30 05:55 | macd_sin_salida | FIL | timeout | +0.00% | -0.50% | -0.11 |

## Eventos de la última vuelta

- 2026-09-30 06:00 [macd_momentum] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:00 [macd_sin_salida] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:00 [macd_momentum_regimen] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:00 [macd_momentum_evento] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:00 [pullback_tendencia] CIERRE DOT rotura de tendencia bruto -0.48% neto -0.98%
- 2026-09-30 06:00 [macd_sin_salida] CIERRE DOT timeout bruto -0.33% neto -0.83%
- 2026-09-30 06:00 [reversion_bb] CIERRE TRX timeout bruto +0.92% neto -0.18%
- 2026-09-30 05:55 [ruptura_estricta] ENTRADA WLD @ 0.4405 (22.60 €, apertura)
- 2026-09-30 05:55 [ruptura_volumen_regimen] ENTRADA WLD @ 0.4405 (22.47 €, apertura)
- 2026-09-30 05:55 [pullback_tendencia] ENTRADA ZRO @ 1.632 (22.61 €, apertura)
- 2026-09-30 06:00 [macd_momentum] CIERRE VIRTUAL momentum perdido bruto +0.46% neto -0.04%
- 2026-09-30 06:00 [macd_momentum_evento] CIERRE VIRTUAL momentum perdido bruto +0.46% neto -0.04%
- 2026-09-30 05:55 [ruptura_volumen] ENTRADA MINA @ 0.1273 (22.29 €, apertura)
- 2026-09-30 05:55 [ruptura_estricta] ENTRADA MINA @ 0.1273 (22.60 €, apertura)
- 2026-09-30 05:55 [ruptura_volumen_regimen] ENTRADA MINA @ 0.1273 (22.47 €, apertura)
- 2026-09-30 05:55 [ruptura_volumen_evento] ENTRADA MINA @ 0.1273 (22.42 €, apertura)
- 2026-09-30 06:00 [macd_momentum] CIERRE BNB momentum perdido bruto +0.07% neto -0.43%
- 2026-09-30 06:00 [macd_momentum_evento] CIERRE BNB momentum perdido bruto +0.07% neto -0.43%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
