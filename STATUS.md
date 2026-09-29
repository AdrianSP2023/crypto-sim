# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 22:11 UTC · vueltas 150 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.13 € (-1.85%) | 66 | 18 | 32% | -0.188% | -1.084% | -1.228% | -16.47 € |
| reversion_bb | 917.86 € (-0.69%) | 18 | 3 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 903.53 € (-2.24%) | 103 | 9 | 23% | -0.137% | -0.890% | -1.021% | -21.01 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.99 € (-1.97%) | 81 | 2 | 23% | -0.174% | -0.996% | -1.119% | -18.50 € |
| macd_momentum | 892.59 € (-3.42%) | 187 | 11 | 18% | -0.102% | -0.742% | -0.858% | -31.64 € |
| estocastico_rebote | 892.99 € (-3.38%) | 155 | 14 | 30% | -0.232% | -0.900% | -1.021% | -31.88 € |
| ruptura_estricta | 910.06 € (-1.53%) | 46 | 6 | 28% | -0.245% | -1.313% | -1.447% | -13.90 € |
| macd_sin_salida | 902.77 € (-2.32%) | 104 | 30 | 32% | -0.095% | -0.846% | -0.978% | -20.17 € |
| c_banda_atr_tope | 913.15 € (-1.20%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 915.92 € (-0.90%) | 31 | 5 | 16% | -0.099% | -1.199% | -1.321% | -8.56 € |
| c_banda_atr_regimen | 908.10 € (-1.75%) | 53 | 9 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.80 € (-3.29%) | 173 | 0 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 906.75 € (-1.89%) | 86 | 6 | 24% | -0.091% | -0.894% | -1.026% | -17.65 € |
| c_banda_atr_evento | 911.61 € (-1.37%) | 34 | 18 | 26% | -0.431% | -1.531% | -1.689% | -11.99 € |
| macd_momentum_evento | 905.13 € (-2.07%) | 67 | 11 | 10% | -0.346% | -1.240% | -1.356% | -19.09 € |
| ruptura_volumen_evento | 909.44 € (-1.60%) | 44 | 9 | 14% | -0.426% | -1.492% | -1.631% | -15.10 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-29 21:55 | c_banda_atr_tope | ALGO | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 21:55 | c_banda_atr | ALGO | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 21:50 | estocastico_rebote | PUMP | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-29 22:05 [c_banda_atr] ENTRADA BTC @ 73679.1 (22.71 €, apertura)
- 2026-09-29 22:05 [c_banda_atr_tope] ENTRADA BTC @ 73679.1 (22.84 €, apertura)
- 2026-09-29 22:05 [c_banda_atr_evento] ENTRADA BTC @ 73679.1 (22.82 €, apertura)
- 2026-09-29 22:05 [macd_momentum] ENTRADA SOL @ 105.09 (22.32 €, apertura)
- 2026-09-29 22:05 [macd_sin_salida] ENTRADA SOL @ 105.09 (22.60 €, apertura)
- 2026-09-29 22:05 [macd_momentum_evento] ENTRADA SOL @ 105.09 (22.63 €, apertura)
- 2026-09-29 22:05 [macd_momentum] ENTRADA ADA @ 0.215783 (22.32 €, apertura)
- 2026-09-29 22:05 [macd_momentum_evento] ENTRADA ADA @ 0.215783 (22.63 €, apertura)
- 2026-09-29 22:05 [macd_momentum] ENTRADA XLM @ 0.197553 (22.32 €, apertura)
- 2026-09-29 22:05 [macd_sin_salida] ENTRADA XLM @ 0.197553 (22.60 €, apertura)
- 2026-09-29 22:05 [c_banda_atr_tope] ENTRADA XLM @ 0.197553 (22.84 €, apertura)
- 2026-09-29 22:05 [macd_momentum_evento] ENTRADA XLM @ 0.197553 (22.63 €, apertura)
- 2026-09-29 22:05 [c_banda_atr] ENTRADA AVAX @ 10.138 (22.71 €, apertura)
- 2026-09-29 22:05 [c_banda_atr_evento] ENTRADA AVAX @ 10.138 (22.82 €, apertura)
- 2026-09-29 22:05 [macd_momentum] ENTRADA HYPE @ 75.95 (22.32 €, apertura)
- 2026-09-29 22:05 [macd_sin_salida] ENTRADA HYPE @ 75.95 (22.60 €, apertura)
- 2026-09-29 22:05 [macd_momentum_evento] ENTRADA HYPE @ 75.95 (22.63 €, apertura)
- 2026-09-29 22:05 [macd_momentum] ENTRADA DOT @ 1.0589 (22.32 €, apertura)
- 2026-09-29 22:05 [macd_momentum_evento] ENTRADA DOT @ 1.0589 (22.63 €, apertura)
- 2026-09-29 22:10 [c_banda_atr] CIERRE CRV stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 22:10 [c_banda_atr_tope] CIERRE CRV stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 22:10 [c_banda_atr_evento] CIERRE CRV stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 22:05 [macd_momentum] ENTRADA DASH @ 53.876 (22.32 €, apertura)
- 2026-09-29 22:05 [c_banda_atr_tope] ENTRADA DASH @ 53.876 (22.83 €, apertura)
- 2026-09-29 22:05 [macd_momentum_evento] ENTRADA DASH @ 53.876 (22.63 €, apertura)
- 2026-09-29 22:05 [ruptura_volumen] ENTRADA PEPE @ 3.774e-06 (22.58 €, apertura)
- 2026-09-29 22:05 [macd_momentum] ENTRADA PEPE @ 3.774e-06 (22.32 €, apertura)
- 2026-09-29 22:05 [macd_momentum_evento] ENTRADA PEPE @ 3.774e-06 (22.63 €, apertura)
- 2026-09-29 22:05 [ruptura_volumen_evento] ENTRADA PEPE @ 3.774e-06 (22.73 €, apertura)
- 2026-09-29 22:05 [macd_momentum] ENTRADA NIGHT @ 0.02877 (22.32 €, apertura)
- 2026-09-29 22:05 [macd_sin_salida] ENTRADA NIGHT @ 0.02877 (22.60 €, apertura)
- 2026-09-29 22:05 [macd_momentum_evento] ENTRADA NIGHT @ 0.02877 (22.63 €, apertura)
- 2026-09-29 22:05 [c_banda_atr] ENTRADA FIL @ 0.954 (22.69 €, apertura)
- 2026-09-29 22:05 [c_banda_atr_evento] ENTRADA FIL @ 0.954 (22.81 €, apertura)
- 2026-09-29 22:05 [c_banda_atr] ENTRADA PENGU @ 0.008825 (22.69 €, apertura)
- 2026-09-29 22:05 [c_banda_atr_evento] ENTRADA PENGU @ 0.008825 (22.81 €, apertura)
- 2026-09-29 22:05 [macd_momentum] ENTRADA POL @ 0.10439 (22.32 €, apertura)
- 2026-09-29 22:05 [macd_momentum_evento] ENTRADA POL @ 0.10439 (22.63 €, apertura)
- 2026-09-29 22:05 [c_banda_atr] ENTRADA BNB @ 668.95 (22.69 €, apertura)
- 2026-09-29 22:05 [c_banda_atr_evento] ENTRADA BNB @ 668.95 (22.81 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
