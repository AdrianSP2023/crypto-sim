# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 22:06 UTC · vueltas 149 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.63 € (-1.80%) | 65 | 14 | 32% | -0.168% | -1.070% | -1.213% | -16.02 € |
| reversion_bb | 917.96 € (-0.68%) | 18 | 3 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 903.83 € (-2.21%) | 103 | 8 | 23% | -0.137% | -0.890% | -1.021% | -21.01 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.21 € (-1.95%) | 81 | 2 | 23% | -0.174% | -0.996% | -1.119% | -18.50 € |
| macd_momentum | 892.65 € (-3.42%) | 187 | 2 | 18% | -0.102% | -0.742% | -0.858% | -31.64 € |
| estocastico_rebote | 892.97 € (-3.38%) | 155 | 14 | 30% | -0.232% | -0.900% | -1.021% | -31.88 € |
| ruptura_estricta | 910.34 € (-1.50%) | 46 | 6 | 28% | -0.245% | -1.313% | -1.447% | -13.90 € |
| macd_sin_salida | 903.06 € (-2.29%) | 104 | 26 | 32% | -0.095% | -0.846% | -0.978% | -20.17 € |
| c_banda_atr_tope | 913.51 € (-1.16%) | 28 | 3 | 21% | -0.527% | -1.627% | -1.774% | -10.49 € |
| ruptura_volumen_tope | 916.21 € (-0.87%) | 31 | 5 | 16% | -0.099% | -1.199% | -1.321% | -8.56 € |
| c_banda_atr_regimen | 908.14 € (-1.74%) | 53 | 9 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.80 € (-3.29%) | 173 | 0 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 906.93 € (-1.87%) | 86 | 6 | 24% | -0.091% | -0.894% | -1.026% | -17.65 € |
| c_banda_atr_evento | 912.24 € (-1.30%) | 33 | 14 | 27% | -0.399% | -1.499% | -1.657% | -11.39 € |
| macd_momentum_evento | 905.20 € (-2.06%) | 67 | 2 | 10% | -0.346% | -1.240% | -1.356% | -19.09 € |
| ruptura_volumen_evento | 909.74 € (-1.57%) | 44 | 8 | 14% | -0.426% | -1.492% | -1.631% | -15.10 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-29 21:50 | pullback_tendencia | FIL | rotura de tendencia | -0.42% | -0.92% | -0.21 |
| 2026-09-29 21:45 | c_banda_atr_evento | ASTER | timeout | +0.25% | -0.85% | -0.19 |
| 2026-09-29 21:45 | c_banda_atr_tope | ASTER | timeout | +0.25% | -0.85% | -0.19 |

## Eventos de la última vuelta

- 2026-09-29 22:00 [estocastico_rebote] ENTRADA SUI @ 1.0165 (22.31 €, apertura)
- 2026-09-29 22:05 [c_banda_atr] CIERRE UNI timeout bruto +0.49% neto -0.01%
- 2026-09-29 22:05 [c_banda_atr_tope] CIERRE UNI timeout bruto +0.49% neto -0.61%
- 2026-09-29 22:05 [c_banda_atr_evento] CIERRE UNI timeout bruto +0.49% neto -0.61%
- 2026-09-29 22:05 [c_banda_atr] CIERRE ARB timeout bruto +0.05% neto -0.45%
- 2026-09-29 22:05 [c_banda_atr_tope] CIERRE ARB timeout bruto +0.05% neto -1.05%
- 2026-09-29 22:05 [c_banda_atr_evento] CIERRE ARB timeout bruto +0.05% neto -1.05%
- 2026-09-29 22:00 [c_banda_atr] ENTRADA XDC @ 0.02938 (22.71 €, apertura)
- 2026-09-29 22:00 [c_banda_atr_tope] ENTRADA XDC @ 0.02938 (22.84 €, apertura)
- 2026-09-29 22:00 [c_banda_atr_evento] ENTRADA XDC @ 0.02938 (22.82 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
