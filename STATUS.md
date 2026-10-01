# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 14:16 UTC · vueltas 238 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.32 € (-3.56%) | 196 | 20 | 34% | -0.066% | -0.699% | -0.826% | -31.26 € |
| reversion_bb | 917.19 € (-0.76%) | 33 | 10 | 39% | +0.133% | -0.967% | -1.063% | -7.36 € |
| ruptura_volumen | 880.15 € (-4.77%) | 235 | 3 | 23% | -0.212% | -0.823% | -0.931% | -43.82 € |
| rebote_extremo | 922.29 € (-0.21%) | 10 | 0 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 893.90 € (-3.28%) | 138 | 0 | 14% | -0.274% | -0.965% | -1.070% | -30.34 € |
| macd_momentum | 877.32 € (-5.08%) | 338 | 14 | 20% | -0.025% | -0.602% | -0.713% | -45.96 € |
| estocastico_rebote | 877.41 € (-5.07%) | 272 | 12 | 30% | -0.164% | -0.759% | -0.872% | -46.75 € |
| ruptura_estricta | 886.02 € (-4.13%) | 132 | 4 | 23% | -0.548% | -1.248% | -1.371% | -37.57 € |
| macd_sin_salida | 881.72 € (-4.60%) | 247 | 14 | 34% | -0.137% | -0.743% | -0.859% | -41.73 € |
| c_banda_atr_tope | 912.74 € (-1.24%) | 44 | 5 | 27% | -0.045% | -1.131% | -1.251% | -11.45 € |
| ruptura_volumen_tope | 909.28 € (-1.62%) | 74 | 2 | 26% | -0.019% | -0.876% | -0.991% | -14.88 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 897.25 € (-2.92%) | 163 | 20 | 35% | -0.016% | -0.678% | -0.799% | -25.31 € |
| macd_momentum_evento | 882.18 € (-4.55%) | 291 | 14 | 18% | -0.033% | -0.624% | -0.730% | -41.09 € |
| ruptura_volumen_evento | 892.67 € (-3.42%) | 185 | 3 | 24% | -0.100% | -0.743% | -0.839% | -31.29 € |
| rebote_desplome | 924.30 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.30 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 14:15 | ruptura_volumen_evento | MINA | timeout | -0.15% | -0.65% | -0.15 |
| 2026-10-01 14:15 | ruptura_volumen_evento | AAVE | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 14:15 | macd_momentum_evento | SPX | momentum perdido | -0.64% | -1.14% | -0.25 |
| 2026-10-01 14:15 | macd_momentum_evento | TRUMP | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 14:15 | macd_momentum_evento | RENDER | momentum perdido | -0.29% | -0.80% | -0.18 |
| 2026-10-01 14:15 | ruptura_volumen_regimen | MINA | timeout | -0.15% | -0.65% | -0.14 |
| 2026-10-01 14:15 | ruptura_volumen_tope | AAVE | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 14:15 | macd_sin_salida | TRUMP | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 14:15 | macd_sin_salida | ICP | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 14:15 | macd_momentum | SPX | momentum perdido | -0.64% | -1.14% | -0.25 |
| 2026-10-01 14:15 | macd_momentum | TRUMP | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 14:15 | macd_momentum | RENDER | momentum perdido | -0.29% | -0.80% | -0.17 |
| 2026-10-01 14:15 | ruptura_volumen | MINA | timeout | -0.15% | -0.65% | -0.14 |
| 2026-10-01 14:15 | ruptura_volumen | AAVE | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-01 14:15 | reversion_bb | TAO | take-profit | +1.60% | +0.50% | +0.12 |

## Eventos de la última vuelta

- 2026-10-01 14:10 [ruptura_volumen] ENTRADA AAVE @ 150.97 (22.02 €, apertura)
- 2026-10-01 14:15 [ruptura_volumen] CIERRE AAVE stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 14:10 [ruptura_estricta] ENTRADA AAVE @ 150.97 (22.17 €, apertura)
- 2026-10-01 14:10 [ruptura_volumen_tope] ENTRADA AAVE @ 150.97 (22.74 €, apertura)
- 2026-10-01 14:15 [ruptura_volumen_tope] CIERRE AAVE stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 14:10 [ruptura_volumen_evento] ENTRADA AAVE @ 150.97 (22.34 €, apertura)
- 2026-10-01 14:15 [ruptura_volumen_evento] CIERRE AAVE stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 14:15 [reversion_bb] CIERRE TAO take-profit bruto +1.60% neto +0.50%
- 2026-10-01 14:15 [macd_sin_salida] CIERRE ICP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:10 [rebote_desplome] ENTRADA NIGHT @ 0.03355 (23.11 €, apertura)
- 2026-10-01 14:10 [rebote_desplome_mercado] ENTRADA NIGHT @ 0.03355 (23.11 €, apertura)
- 2026-10-01 14:15 [macd_momentum] CIERRE RENDER momentum perdido bruto -0.30% neto -0.80%
- 2026-10-01 14:15 [macd_momentum_evento] CIERRE RENDER momentum perdido bruto -0.30% neto -0.80%
- 2026-10-01 14:15 [ruptura_volumen] CIERRE MINA timeout bruto -0.15% neto -0.65%
- 2026-10-01 14:15 [ruptura_volumen_regimen] CIERRE MINA timeout bruto -0.15% neto -0.65%
- 2026-10-01 14:15 [ruptura_volumen_evento] CIERRE MINA timeout bruto -0.15% neto -0.65%
- 2026-10-01 14:15 [macd_momentum] CIERRE TRUMP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:15 [macd_sin_salida] CIERRE TRUMP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:15 [macd_momentum_evento] CIERRE TRUMP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:15 [macd_momentum] CIERRE SPX momentum perdido bruto -0.64% neto -1.14%
- 2026-10-01 14:15 [macd_momentum_evento] CIERRE SPX momentum perdido bruto -0.64% neto -1.14%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
