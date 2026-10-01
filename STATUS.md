# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 17:06 UTC · vueltas 272 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 886.79 € (-4.05%) | 222 | 17 | 32% | -0.124% | -0.742% | -0.866% | -37.45 € |
| reversion_bb | 916.00 € (-0.89%) | 39 | 9 | 41% | +0.107% | -0.993% | -1.091% | -8.92 € |
| ruptura_volumen | 877.02 € (-5.11%) | 251 | 10 | 23% | -0.230% | -0.834% | -0.944% | -47.33 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 892.16 € (-3.47%) | 155 | 4 | 14% | -0.253% | -0.924% | -1.020% | -32.56 € |
| macd_momentum | 871.22 € (-5.74%) | 388 | 3 | 20% | -0.042% | -0.610% | -0.717% | -53.20 € |
| estocastico_rebote | 876.89 € (-5.12%) | 286 | 2 | 31% | -0.137% | -0.729% | -0.840% | -47.14 € |
| ruptura_estricta | 884.95 € (-4.25%) | 139 | 11 | 23% | -0.551% | -1.241% | -1.362% | -39.30 € |
| macd_sin_salida | 879.83 € (-4.80%) | 271 | 14 | 33% | -0.129% | -0.725% | -0.840% | -44.59 € |
| c_banda_atr_tope | 911.25 € (-1.41%) | 52 | 4 | 27% | -0.078% | -1.085% | -1.200% | -12.96 € |
| ruptura_volumen_tope | 907.86 € (-1.77%) | 84 | 4 | 26% | -0.035% | -0.849% | -0.966% | -16.36 € |
| c_banda_atr_regimen | 901.50 € (-2.46%) | 110 | 4 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.50 € (-3.33%) | 208 | 0 | 22% | -0.023% | -0.648% | -0.761% | -30.74 € |
| ruptura_volumen_regimen | 881.37 € (-4.64%) | 190 | 4 | 19% | -0.347% | -0.985% | -1.101% | -42.43 € |
| c_banda_atr_evento | 892.69 € (-3.41%) | 189 | 17 | 33% | -0.092% | -0.732% | -0.850% | -31.54 € |
| macd_momentum_evento | 876.05 € (-5.21%) | 341 | 3 | 17% | -0.052% | -0.629% | -0.732% | -48.37 € |
| ruptura_volumen_evento | 889.49 € (-3.76%) | 201 | 10 | 23% | -0.131% | -0.763% | -0.862% | -34.84 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 17:05 | macd_momentum_evento | TON | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 17:05 | macd_sin_salida | AAVE | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 17:05 | macd_momentum | TON | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 17:05 | pullback_tendencia | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 17:00 | ruptura_volumen_evento | KSM | stop-loss | -1.52% | -2.02% | -0.45 |
| 2026-10-01 17:00 | macd_momentum_evento | SHIB | momentum perdido | -0.16% | -0.66% | -0.14 |
| 2026-10-01 17:00 | c_banda_atr_evento | INJ | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 17:00 | c_banda_atr_evento | BCH | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 17:00 | c_banda_atr_evento | XDC | stop-loss | -1.70% | -2.20% | -0.49 |
| 2026-10-01 17:00 | ruptura_volumen_regimen | KSM | stop-loss | -1.52% | -2.02% | -0.45 |
| 2026-10-01 17:00 | c_banda_atr_tope | XDC | stop-loss | -1.70% | -2.20% | -0.50 |
| 2026-10-01 17:00 | macd_sin_salida | MINA | stop-loss | -1.97% | -2.47% | -0.54 |
| 2026-10-01 17:00 | macd_sin_salida | INJ | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 17:00 | macd_momentum | SHIB | momentum perdido | -0.16% | -0.66% | -0.14 |
| 2026-10-01 17:00 | pullback_tendencia | SHIB | rotura de tendencia | -0.08% | -0.58% | -0.13 |

## Eventos de la última vuelta

- 2026-10-01 17:05 [macd_sin_salida] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 17:00 [macd_momentum] ENTRADA TRX @ 0.298236 (21.78 €, apertura)
- 2026-10-01 17:00 [macd_sin_salida] ENTRADA TRX @ 0.298236 (21.99 €, apertura)
- 2026-10-01 17:00 [macd_momentum_evento] ENTRADA TRX @ 0.298236 (21.90 €, apertura)
- 2026-10-01 17:05 [pullback_tendencia] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:05 [macd_momentum] CIERRE TON momentum perdido bruto +0.00% neto -0.50%
- 2026-10-01 17:05 [macd_momentum_evento] CIERRE TON momentum perdido bruto +0.00% neto -0.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
