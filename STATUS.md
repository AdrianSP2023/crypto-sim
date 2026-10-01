# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 14:46 UTC · vueltas 244 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 892.25 € (-3.46%) | 200 | 17 | 34% | -0.053% | -0.683% | -0.810% | -31.20 € |
| reversion_bb | 917.41 € (-0.74%) | 33 | 10 | 39% | +0.133% | -0.967% | -1.063% | -7.36 € |
| ruptura_volumen | 879.68 € (-4.82%) | 237 | 6 | 23% | -0.216% | -0.826% | -0.933% | -44.34 € |
| rebote_extremo | 922.18 € (-0.22%) | 10 | 1 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 893.90 € (-3.28%) | 138 | 3 | 14% | -0.274% | -0.965% | -1.070% | -30.34 € |
| macd_momentum | 877.69 € (-5.04%) | 342 | 17 | 20% | -0.023% | -0.600% | -0.710% | -46.32 € |
| estocastico_rebote | 877.86 € (-5.02%) | 272 | 13 | 30% | -0.164% | -0.759% | -0.872% | -46.75 € |
| ruptura_estricta | 885.83 € (-4.16%) | 134 | 4 | 23% | -0.554% | -1.251% | -1.374% | -38.23 € |
| macd_sin_salida | 882.33 € (-4.53%) | 249 | 16 | 34% | -0.130% | -0.735% | -0.851% | -41.62 € |
| c_banda_atr_tope | 912.24 € (-1.30%) | 47 | 4 | 28% | +0.005% | -1.057% | -1.172% | -11.42 € |
| ruptura_volumen_tope | 908.78 € (-1.67%) | 75 | 4 | 25% | -0.036% | -0.888% | -1.003% | -15.29 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 898.19 € (-2.82%) | 167 | 17 | 35% | -0.002% | -0.660% | -0.780% | -25.25 € |
| macd_momentum_evento | 882.56 € (-4.51%) | 295 | 17 | 18% | -0.032% | -0.621% | -0.727% | -41.46 € |
| ruptura_volumen_evento | 892.19 € (-3.47%) | 187 | 6 | 24% | -0.106% | -0.747% | -0.843% | -31.81 € |
| rebote_desplome | 924.75 € (+0.06%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.75 € (+0.06%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 14:45 | ruptura_volumen_evento | UNI | stop-loss | -1.30% | -1.80% | -0.40 |
| 2026-10-01 14:45 | c_banda_atr_evento | ICP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 14:45 | ruptura_volumen_tope | UNI | stop-loss | -1.30% | -1.80% | -0.41 |
| 2026-10-01 14:45 | ruptura_estricta | SKY | timeout | +0.03% | -0.47% | -0.10 |
| 2026-10-01 14:45 | ruptura_estricta | AAVE | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-01 14:45 | ruptura_volumen | UNI | stop-loss | -1.30% | -1.80% | -0.40 |
| 2026-10-01 14:45 | c_banda_atr | ICP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 14:40 | c_banda_atr_evento | BCH | timeout | -0.21% | -0.71% | -0.16 |
| 2026-10-01 14:40 | c_banda_atr_evento | TAO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 14:40 | c_banda_atr_tope | SHIB | timeout | +0.41% | -0.39% | -0.09 |
| 2026-10-01 14:40 | c_banda_atr_tope | BCH | timeout | -0.21% | -1.01% | -0.23 |
| 2026-10-01 14:40 | c_banda_atr | BCH | timeout | -0.21% | -0.71% | -0.16 |
| 2026-10-01 14:40 | c_banda_atr | TAO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 14:35 | ruptura_volumen_evento | LINK | timeout | -0.05% | -0.55% | -0.12 |
| 2026-10-01 14:35 | ruptura_volumen | LINK | timeout | -0.05% | -0.55% | -0.12 |

## Eventos de la última vuelta

- 2026-10-01 14:45 [ruptura_estricta] CIERRE AAVE stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 14:45 [ruptura_volumen] CIERRE UNI stop-loss bruto -1.30% neto -1.80%
- 2026-10-01 14:45 [ruptura_volumen_tope] CIERRE UNI stop-loss bruto -1.30% neto -1.80%
- 2026-10-01 14:45 [ruptura_volumen_evento] CIERRE UNI stop-loss bruto -1.30% neto -1.80%
- 2026-10-01 14:45 [c_banda_atr] CIERRE ICP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:45 [c_banda_atr_evento] CIERRE ICP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:40 [macd_momentum] ENTRADA PEPE @ 3.876e-06 (21.95 €, apertura)
- 2026-10-01 14:40 [macd_sin_salida] ENTRADA PEPE @ 3.876e-06 (22.07 €, apertura)
- 2026-10-01 14:40 [macd_momentum_evento] ENTRADA PEPE @ 3.876e-06 (22.07 €, apertura)
- 2026-10-01 14:40 [macd_momentum] ENTRADA RENDER @ 1.691 (21.95 €, apertura)
- 2026-10-01 14:40 [macd_momentum_evento] ENTRADA RENDER @ 1.691 (22.07 €, apertura)
- 2026-10-01 14:45 [ruptura_estricta] CIERRE SKY timeout bruto +0.03% neto -0.47%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
