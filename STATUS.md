# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 23:06 UTC · vueltas 161 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.05 € (-1.97%) | 68 | 21 | 31% | -0.213% | -1.096% | -1.242% | -17.16 € |
| reversion_bb | 917.85 € (-0.69%) | 18 | 4 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 903.32 € (-2.26%) | 110 | 3 | 24% | -0.103% | -0.840% | -0.968% | -21.18 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.81 € (-1.99%) | 85 | 4 | 22% | -0.181% | -0.988% | -1.111% | -19.25 € |
| macd_momentum | 891.18 € (-3.58%) | 200 | 9 | 17% | -0.104% | -0.735% | -0.851% | -33.47 € |
| estocastico_rebote | 893.17 € (-3.36%) | 157 | 14 | 31% | -0.205% | -0.871% | -0.993% | -31.26 € |
| ruptura_estricta | 909.74 € (-1.57%) | 47 | 7 | 28% | -0.283% | -1.338% | -1.473% | -14.47 € |
| macd_sin_salida | 901.80 € (-2.43%) | 106 | 33 | 32% | -0.087% | -0.833% | -0.965% | -20.25 € |
| c_banda_atr_tope | 913.13 € (-1.20%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 915.28 € (-0.97%) | 35 | 4 | 14% | -0.070% | -1.170% | -1.287% | -9.43 € |
| c_banda_atr_regimen | 907.45 € (-1.82%) | 53 | 9 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.80 € (-3.29%) | 173 | 0 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 905.66 € (-2.01%) | 92 | 0 | 23% | -0.097% | -0.881% | -1.009% | -18.58 € |
| c_banda_atr_evento | 910.38 € (-1.50%) | 36 | 21 | 25% | -0.463% | -1.547% | -1.706% | -12.82 € |
| macd_momentum_evento | 903.71 € (-2.22%) | 80 | 9 | 10% | -0.311% | -1.141% | -1.257% | -20.94 € |
| ruptura_volumen_evento | 908.89 € (-1.66%) | 51 | 3 | 14% | -0.314% | -1.331% | -1.462% | -15.62 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 23:05 | macd_momentum_evento | ZRO | take-profit | +2.43% | +1.93% | +0.44 |
| 2026-09-29 23:05 | macd_momentum_evento | AAVE | momentum perdido | -0.44% | -0.94% | -0.21 |
| 2026-09-29 23:05 | macd_sin_salida | ZRO | take-profit | +2.43% | +1.93% | +0.44 |
| 2026-09-29 23:05 | macd_sin_salida | INJ | stop-loss | -1.80% | -2.30% | -0.52 |
| 2026-09-29 23:05 | macd_momentum | ZRO | take-profit | +2.43% | +1.93% | +0.43 |
| 2026-09-29 23:05 | macd_momentum | AAVE | momentum perdido | -0.44% | -0.94% | -0.21 |
| 2026-09-29 23:00 | ruptura_volumen_evento | NIGHT | timeout | -0.07% | -0.57% | -0.13 |
| 2026-09-29 23:00 | ruptura_volumen_regimen | NIGHT | timeout | -0.07% | -0.57% | -0.13 |
| 2026-09-29 23:00 | ruptura_volumen_tope | NIGHT | timeout | -0.07% | -1.17% | -0.27 |
| 2026-09-29 23:00 | ruptura_volumen | NIGHT | timeout | -0.07% | -0.57% | -0.13 |
| 2026-09-29 22:55 | ruptura_volumen_evento | ZRO | take-profit | +2.50% | +2.00% | +0.46 |
| 2026-09-29 22:55 | ruptura_volumen | ZRO | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-29 22:50 | macd_momentum_evento | PEPE | momentum perdido | -0.42% | -0.92% | -0.21 |
| 2026-09-29 22:50 | ruptura_volumen_regimen | POL | timeout | -0.81% | -1.31% | -0.30 |
| 2026-09-29 22:50 | estocastico_rebote | QNT | take-profit | +1.99% | +1.49% | +0.33 |

## Eventos de la última vuelta

- 2026-09-29 23:05 [macd_momentum] CIERRE AAVE momentum perdido bruto -0.44% neto -0.94%
- 2026-09-29 23:05 [macd_momentum_evento] CIERRE AAVE momentum perdido bruto -0.44% neto -0.94%
- 2026-09-29 23:05 [macd_sin_salida] CIERRE INJ stop-loss bruto -1.80% neto -2.30%
- 2026-09-29 23:05 [macd_momentum] CIERRE ZRO take-profit bruto +2.43% neto +1.93%
- 2026-09-29 23:05 [macd_sin_salida] CIERRE ZRO take-profit bruto +2.43% neto +1.93%
- 2026-09-29 23:05 [macd_momentum_evento] CIERRE ZRO take-profit bruto +2.43% neto +1.93%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
