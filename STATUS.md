# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 14:21 UTC · vueltas 239 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 892.22 € (-3.46%) | 196 | 20 | 34% | -0.066% | -0.699% | -0.826% | -31.26 € |
| reversion_bb | 917.61 € (-0.72%) | 33 | 10 | 39% | +0.133% | -0.967% | -1.063% | -7.36 € |
| ruptura_volumen | 880.18 € (-4.77%) | 235 | 3 | 23% | -0.212% | -0.823% | -0.931% | -43.82 € |
| rebote_extremo | 922.34 € (-0.21%) | 10 | 1 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 893.95 € (-3.28%) | 138 | 1 | 14% | -0.274% | -0.965% | -1.070% | -30.34 € |
| macd_momentum | 877.76 € (-5.03%) | 339 | 13 | 20% | -0.027% | -0.604% | -0.714% | -46.23 € |
| estocastico_rebote | 877.68 € (-5.04%) | 272 | 12 | 30% | -0.164% | -0.759% | -0.872% | -46.75 € |
| ruptura_estricta | 886.31 € (-4.10%) | 132 | 4 | 23% | -0.548% | -1.248% | -1.371% | -37.57 € |
| macd_sin_salida | 882.04 € (-4.57%) | 248 | 13 | 33% | -0.139% | -0.744% | -0.860% | -41.95 € |
| c_banda_atr_tope | 912.90 € (-1.23%) | 44 | 5 | 27% | -0.045% | -1.131% | -1.251% | -11.45 € |
| ruptura_volumen_tope | 909.21 € (-1.63%) | 74 | 2 | 26% | -0.019% | -0.876% | -0.991% | -14.88 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 898.16 € (-2.82%) | 163 | 20 | 35% | -0.016% | -0.678% | -0.799% | -25.31 € |
| macd_momentum_evento | 882.63 € (-4.50%) | 292 | 13 | 18% | -0.036% | -0.626% | -0.732% | -41.37 € |
| ruptura_volumen_evento | 892.70 € (-3.41%) | 185 | 3 | 24% | -0.100% | -0.743% | -0.839% | -31.29 € |
| rebote_desplome | 924.56 € (+0.03%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.56 € (+0.03%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 14:20 | macd_momentum_evento | ZEC | momentum perdido | -0.75% | -1.25% | -0.28 |
| 2026-10-01 14:20 | macd_sin_salida | SKY | timeout | -0.47% | -0.97% | -0.21 |
| 2026-10-01 14:20 | macd_momentum | ZEC | momentum perdido | -0.75% | -1.25% | -0.28 |
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

## Eventos de la última vuelta

- 2026-10-01 14:15 [pullback_tendencia] ENTRADA BTC @ 74220.3 (22.35 €, apertura)
- 2026-10-01 14:20 [macd_momentum] CIERRE ZEC momentum perdido bruto -0.75% neto -1.25%
- 2026-10-01 14:20 [macd_momentum_evento] CIERRE ZEC momentum perdido bruto -0.75% neto -1.25%
- 2026-10-01 14:15 [rebote_extremo] ENTRADA WLD @ 0.4443 (23.06 €, apertura)
- 2026-10-01 14:20 [macd_sin_salida] CIERRE SKY timeout bruto -0.47% neto -0.97%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
