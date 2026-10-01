# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 16:56 UTC · vueltas 270 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 886.73 € (-4.06%) | 219 | 20 | 33% | -0.104% | -0.724% | -0.848% | -36.07 € |
| reversion_bb | 915.17 € (-0.98%) | 39 | 9 | 41% | +0.107% | -0.993% | -1.091% | -8.92 € |
| ruptura_volumen | 876.79 € (-5.13%) | 250 | 11 | 23% | -0.225% | -0.829% | -0.938% | -46.89 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 892.10 € (-3.48%) | 151 | 5 | 13% | -0.265% | -0.940% | -1.039% | -32.29 € |
| macd_momentum | 871.37 € (-5.72%) | 386 | 4 | 20% | -0.042% | -0.610% | -0.717% | -52.94 € |
| estocastico_rebote | 876.83 € (-5.13%) | 286 | 2 | 31% | -0.137% | -0.729% | -0.840% | -47.14 € |
| ruptura_estricta | 884.17 € (-4.34%) | 139 | 11 | 23% | -0.551% | -1.241% | -1.362% | -39.30 € |
| macd_sin_salida | 879.55 € (-4.84%) | 268 | 16 | 34% | -0.111% | -0.709% | -0.824% | -43.17 € |
| c_banda_atr_tope | 911.30 € (-1.40%) | 51 | 5 | 27% | -0.046% | -1.063% | -1.178% | -12.46 € |
| ruptura_volumen_tope | 907.73 € (-1.79%) | 84 | 4 | 26% | -0.035% | -0.849% | -0.966% | -16.36 € |
| c_banda_atr_regimen | 901.28 € (-2.48%) | 110 | 4 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.50 € (-3.33%) | 208 | 0 | 22% | -0.023% | -0.648% | -0.761% | -30.74 € |
| ruptura_volumen_regimen | 881.52 € (-4.62%) | 189 | 5 | 19% | -0.341% | -0.979% | -1.095% | -41.98 € |
| c_banda_atr_evento | 892.63 € (-3.42%) | 186 | 20 | 33% | -0.068% | -0.710% | -0.828% | -30.15 € |
| macd_momentum_evento | 876.19 € (-5.20%) | 339 | 4 | 17% | -0.052% | -0.630% | -0.733% | -48.11 € |
| ruptura_volumen_evento | 889.26 € (-3.78%) | 200 | 11 | 24% | -0.124% | -0.756% | -0.855% | -34.39 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 16:55 | ruptura_volumen_evento | XDC | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 16:55 | ruptura_volumen_evento | ZRO | stop-loss | -1.54% | -2.04% | -0.45 |
| 2026-10-01 16:55 | macd_momentum_evento | ICP | momentum perdido | -0.38% | -0.88% | -0.19 |
| 2026-10-01 16:55 | macd_momentum_evento | ADA | momentum perdido | -0.53% | -1.03% | -0.23 |
| 2026-10-01 16:55 | ruptura_volumen_regimen | XDC | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 16:55 | macd_sin_salida | ETH | timeout | +0.05% | -0.45% | -0.10 |
| 2026-10-01 16:55 | ruptura_estricta | ZRO | stop-loss | -2.66% | -3.16% | -0.70 |
| 2026-10-01 16:55 | macd_momentum | ICP | momentum perdido | -0.38% | -0.88% | -0.19 |
| 2026-10-01 16:55 | macd_momentum | ADA | momentum perdido | -0.53% | -1.03% | -0.23 |
| 2026-10-01 16:55 | pullback_tendencia | XRP | rotura de tendencia | -0.31% | -0.81% | -0.18 |
| 2026-10-01 16:55 | ruptura_volumen | XDC | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-01 16:55 | ruptura_volumen | ZRO | stop-loss | -1.54% | -2.04% | -0.45 |
| 2026-10-01 16:50 | ruptura_volumen_evento | WLFI | timeout | +0.20% | -0.30% | -0.07 |
| 2026-10-01 16:50 | macd_momentum_evento | WLFI | momentum perdido | +0.20% | -0.30% | -0.07 |
| 2026-10-01 16:50 | macd_momentum_evento | RENDER | momentum perdido | -0.65% | -1.15% | -0.25 |

## Eventos de la última vuelta

- 2026-10-01 16:55 [pullback_tendencia] CIERRE XRP rotura de tendencia bruto -0.31% neto -0.81%
- 2026-10-01 16:55 [macd_sin_salida] CIERRE ETH timeout bruto +0.05% neto -0.45%
- 2026-10-01 16:55 [macd_momentum] CIERRE ADA momentum perdido bruto -0.53% neto -1.03%
- 2026-10-01 16:55 [macd_momentum_evento] CIERRE ADA momentum perdido bruto -0.53% neto -1.03%
- 2026-10-01 16:55 [ruptura_volumen] CIERRE ZRO stop-loss bruto -1.54% neto -2.04%
- 2026-10-01 16:55 [ruptura_estricta] CIERRE ZRO stop-loss bruto -2.66% neto -3.16%
- 2026-10-01 16:55 [ruptura_volumen_evento] CIERRE ZRO stop-loss bruto -1.54% neto -2.04%
- 2026-10-01 16:55 [macd_momentum] CIERRE ICP momentum perdido bruto -0.38% neto -0.88%
- 2026-10-01 16:55 [macd_momentum_evento] CIERRE ICP momentum perdido bruto -0.38% neto -0.88%
- 2026-10-01 16:55 [ruptura_volumen] CIERRE XDC stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 16:55 [ruptura_volumen_regimen] CIERRE XDC stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 16:55 [ruptura_volumen_evento] CIERRE XDC stop-loss bruto -1.20% neto -1.70%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
