# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 22:16 UTC · vueltas 151 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.47 € (-1.81%) | 66 | 18 | 32% | -0.188% | -1.084% | -1.228% | -16.47 € |
| reversion_bb | 917.88 € (-0.69%) | 18 | 3 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 903.67 € (-2.23%) | 104 | 8 | 24% | -0.130% | -0.881% | -1.011% | -21.00 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.14 € (-1.96%) | 81 | 2 | 23% | -0.174% | -0.996% | -1.119% | -18.50 € |
| macd_momentum | 892.93 € (-3.39%) | 187 | 15 | 18% | -0.102% | -0.742% | -0.858% | -31.64 € |
| estocastico_rebote | 893.38 € (-3.34%) | 155 | 14 | 30% | -0.232% | -0.900% | -1.021% | -31.88 € |
| ruptura_estricta | 910.21 € (-1.52%) | 46 | 6 | 28% | -0.245% | -1.313% | -1.447% | -13.90 € |
| macd_sin_salida | 903.50 € (-2.24%) | 104 | 32 | 32% | -0.095% | -0.846% | -0.978% | -20.17 € |
| c_banda_atr_tope | 913.24 € (-1.19%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 915.88 € (-0.90%) | 32 | 4 | 16% | -0.079% | -1.179% | -1.298% | -8.69 € |
| c_banda_atr_regimen | 908.26 € (-1.73%) | 53 | 9 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.80 € (-3.29%) | 173 | 0 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 906.90 € (-1.88%) | 86 | 6 | 24% | -0.091% | -0.894% | -1.026% | -17.65 € |
| c_banda_atr_evento | 911.95 € (-1.33%) | 34 | 18 | 26% | -0.431% | -1.531% | -1.689% | -11.99 € |
| macd_momentum_evento | 905.48 € (-2.03%) | 67 | 15 | 10% | -0.346% | -1.240% | -1.356% | -19.09 € |
| ruptura_volumen_evento | 909.51 € (-1.59%) | 45 | 8 | 13% | -0.404% | -1.464% | -1.601% | -15.16 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 22:15 | ruptura_volumen_evento | AVAX | timeout | +0.56% | -0.24% | -0.06 |
| 2026-09-29 22:15 | ruptura_volumen_tope | AVAX | timeout | +0.56% | -0.55% | -0.12 |
| 2026-09-29 22:15 | ruptura_volumen | AVAX | timeout | +0.56% | +0.06% | +0.01 |
| 2026-09-29 22:10 | c_banda_atr_evento | CRV | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 22:10 | c_banda_atr_tope | CRV | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 22:10 | c_banda_atr | CRV | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 22:05 | c_banda_atr_evento | ARB | timeout | +0.06% | -1.04% | -0.24 |
| 2026-09-29 22:05 | c_banda_atr_evento | UNI | timeout | +0.49% | -0.61% | -0.14 |
| 2026-09-29 22:05 | c_banda_atr_tope | ARB | timeout | +0.06% | -1.04% | -0.24 |
| 2026-09-29 22:05 | c_banda_atr_tope | UNI | timeout | +0.49% | -0.61% | -0.14 |
| 2026-09-29 22:05 | c_banda_atr | ARB | timeout | +0.06% | -0.45% | -0.10 |
| 2026-09-29 22:05 | c_banda_atr | UNI | timeout | +0.49% | -0.01% | -0.00 |
| 2026-09-29 22:00 | estocastico_rebote | AAVE | timeout | +0.38% | -0.12% | -0.03 |
| 2026-09-29 22:00 | pullback_tendencia | QNT | stop-loss | -1.68% | -2.18% | -0.49 |
| 2026-09-29 21:55 | c_banda_atr_evento | ALGO | stop-loss | -1.50% | -2.60% | -0.59 |

## Eventos de la última vuelta

- 2026-09-29 22:10 [macd_momentum] ENTRADA BTC @ 73689 (22.32 €, apertura)
- 2026-09-29 22:10 [macd_momentum_evento] ENTRADA BTC @ 73689 (22.63 €, apertura)
- 2026-09-29 22:15 [ruptura_volumen] CIERRE AVAX timeout bruto +0.56% neto +0.06%
- 2026-09-29 22:15 [ruptura_volumen_tope] CIERRE AVAX timeout bruto +0.56% neto -0.54%
- 2026-09-29 22:15 [ruptura_volumen_evento] CIERRE AVAX timeout bruto +0.56% neto -0.24%
- 2026-09-29 22:10 [macd_momentum] ENTRADA ENA @ 0.2212 (22.32 €, apertura)
- 2026-09-29 22:10 [macd_momentum_evento] ENTRADA ENA @ 0.2212 (22.63 €, apertura)
- 2026-09-29 22:10 [macd_momentum] ENTRADA PENGU @ 0.008814 (22.32 €, apertura)
- 2026-09-29 22:10 [macd_sin_salida] ENTRADA PENGU @ 0.008814 (22.60 €, apertura)
- 2026-09-29 22:10 [macd_momentum_evento] ENTRADA PENGU @ 0.008814 (22.63 €, apertura)
- 2026-09-29 22:10 [macd_momentum] ENTRADA BNB @ 668.95 (22.32 €, apertura)
- 2026-09-29 22:10 [macd_sin_salida] ENTRADA BNB @ 668.95 (22.60 €, apertura)
- 2026-09-29 22:10 [macd_momentum_evento] ENTRADA BNB @ 668.95 (22.63 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
