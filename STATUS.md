# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 17:16 UTC · vueltas 274 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.87 € (-3.94%) | 222 | 21 | 32% | -0.124% | -0.742% | -0.866% | -37.45 € |
| reversion_bb | 916.43 € (-0.84%) | 39 | 9 | 41% | +0.107% | -0.993% | -1.091% | -8.92 € |
| ruptura_volumen | 877.88 € (-5.02%) | 251 | 11 | 23% | -0.230% | -0.834% | -0.944% | -47.33 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 892.51 € (-3.43%) | 155 | 5 | 14% | -0.253% | -0.924% | -1.020% | -32.56 € |
| macd_momentum | 871.67 € (-5.69%) | 389 | 15 | 20% | -0.042% | -0.609% | -0.716% | -53.31 € |
| estocastico_rebote | 876.94 € (-5.12%) | 286 | 5 | 31% | -0.137% | -0.729% | -0.840% | -47.14 € |
| ruptura_estricta | 885.29 € (-4.21%) | 139 | 11 | 23% | -0.551% | -1.241% | -1.362% | -39.30 € |
| macd_sin_salida | 880.61 € (-4.72%) | 271 | 24 | 33% | -0.129% | -0.725% | -0.840% | -44.59 € |
| c_banda_atr_tope | 911.35 € (-1.39%) | 52 | 5 | 27% | -0.078% | -1.085% | -1.200% | -12.96 € |
| ruptura_volumen_tope | 908.69 € (-1.68%) | 84 | 5 | 26% | -0.035% | -0.849% | -0.966% | -16.36 € |
| c_banda_atr_regimen | 901.70 € (-2.44%) | 110 | 4 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.50 € (-3.33%) | 208 | 0 | 22% | -0.023% | -0.648% | -0.761% | -30.74 € |
| ruptura_volumen_regimen | 881.58 € (-4.62%) | 190 | 4 | 19% | -0.347% | -0.985% | -1.101% | -42.43 € |
| c_banda_atr_evento | 893.77 € (-3.30%) | 189 | 21 | 33% | -0.092% | -0.732% | -0.850% | -31.54 € |
| macd_momentum_evento | 876.50 € (-5.16%) | 342 | 15 | 17% | -0.052% | -0.629% | -0.732% | -48.48 € |
| ruptura_volumen_evento | 890.37 € (-3.67%) | 201 | 11 | 23% | -0.131% | -0.763% | -0.862% | -34.84 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 17:15 | macd_momentum_evento | TRX | momentum perdido | -0.02% | -0.52% | -0.11 |
| 2026-10-01 17:15 | macd_momentum | TRX | momentum perdido | -0.02% | -0.52% | -0.11 |
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

## Eventos de la última vuelta

- 2026-10-01 17:10 [macd_momentum] ENTRADA XRP @ 1.32632 (21.78 €, apertura)
- 2026-10-01 17:10 [macd_momentum_evento] ENTRADA XRP @ 1.32632 (21.90 €, apertura)
- 2026-10-01 17:10 [macd_momentum] ENTRADA ADA @ 0.220175 (21.78 €, apertura)
- 2026-10-01 17:10 [macd_momentum_evento] ENTRADA ADA @ 0.220175 (21.90 €, apertura)
- 2026-10-01 17:10 [macd_momentum] ENTRADA LTC @ 59.81 (21.78 €, apertura)
- 2026-10-01 17:10 [macd_sin_salida] ENTRADA LTC @ 59.81 (21.99 €, apertura)
- 2026-10-01 17:10 [macd_momentum_evento] ENTRADA LTC @ 59.81 (21.90 €, apertura)
- 2026-10-01 17:10 [macd_momentum] ENTRADA ICP @ 2.906 (21.78 €, apertura)
- 2026-10-01 17:10 [macd_momentum_evento] ENTRADA ICP @ 2.906 (21.90 €, apertura)
- 2026-10-01 17:15 [macd_momentum] CIERRE TRX momentum perdido bruto -0.02% neto -0.52%
- 2026-10-01 17:15 [macd_momentum_evento] CIERRE TRX momentum perdido bruto -0.02% neto -0.52%
- 2026-10-01 17:10 [macd_momentum] ENTRADA CRV @ 0.33814 (21.77 €, apertura)
- 2026-10-01 17:10 [macd_sin_salida] ENTRADA CRV @ 0.33814 (21.99 €, apertura)
- 2026-10-01 17:10 [macd_momentum_evento] ENTRADA CRV @ 0.33814 (21.89 €, apertura)
- 2026-10-01 17:10 [c_banda_atr] ENTRADA PEPE @ 3.933e-06 (22.17 €, apertura)
- 2026-10-01 17:10 [estocastico_rebote] ENTRADA PEPE @ 3.933e-06 (21.93 €, apertura)
- 2026-10-01 17:10 [c_banda_atr_evento] ENTRADA PEPE @ 3.933e-06 (22.32 €, apertura)
- 2026-10-01 17:10 [macd_momentum] ENTRADA TRUMP @ 1.823 (21.77 €, apertura)
- 2026-10-01 17:10 [macd_sin_salida] ENTRADA TRUMP @ 1.823 (21.99 €, apertura)
- 2026-10-01 17:10 [macd_momentum_evento] ENTRADA TRUMP @ 1.823 (21.89 €, apertura)
- 2026-10-01 17:10 [macd_momentum] ENTRADA APT @ 0.6845 (21.77 €, apertura)
- 2026-10-01 17:10 [macd_momentum_evento] ENTRADA APT @ 0.6845 (21.89 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
