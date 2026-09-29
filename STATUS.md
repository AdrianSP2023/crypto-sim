# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 21:51 UTC · vueltas 146 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.43 € (-1.82%) | 62 | 15 | 34% | -0.161% | -1.082% | -1.228% | -15.46 € |
| reversion_bb | 917.71 € (-0.71%) | 18 | 3 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 902.97 € (-2.30%) | 103 | 7 | 23% | -0.137% | -0.890% | -1.021% | -21.01 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.29 € (-1.94%) | 80 | 3 | 24% | -0.155% | -0.981% | -1.101% | -18.01 € |
| macd_momentum | 892.61 € (-3.42%) | 187 | 0 | 18% | -0.102% | -0.742% | -0.858% | -31.64 € |
| estocastico_rebote | 892.23 € (-3.46%) | 154 | 12 | 31% | -0.236% | -0.905% | -1.026% | -31.86 € |
| ruptura_estricta | 909.68 € (-1.58%) | 46 | 5 | 28% | -0.245% | -1.313% | -1.447% | -13.90 € |
| macd_sin_salida | 901.48 € (-2.46%) | 104 | 26 | 32% | -0.095% | -0.846% | -0.978% | -20.17 € |
| c_banda_atr_tope | 914.32 € (-1.07%) | 25 | 5 | 24% | -0.552% | -1.652% | -1.807% | -9.51 € |
| ruptura_volumen_tope | 915.47 € (-0.95%) | 31 | 4 | 16% | -0.099% | -1.199% | -1.321% | -8.56 € |
| c_banda_atr_regimen | 907.53 € (-1.81%) | 53 | 9 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.80 € (-3.29%) | 173 | 0 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 906.27 € (-1.94%) | 86 | 6 | 24% | -0.091% | -0.894% | -1.026% | -17.65 € |
| c_banda_atr_evento | 912.46 € (-1.27%) | 30 | 15 | 30% | -0.407% | -1.507% | -1.672% | -10.42 € |
| macd_momentum_evento | 905.15 € (-2.07%) | 67 | 0 | 10% | -0.346% | -1.240% | -1.356% | -19.09 € |
| ruptura_volumen_evento | 908.87 € (-1.66%) | 44 | 7 | 14% | -0.426% | -1.492% | -1.631% | -15.10 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 21:50 | estocastico_rebote | PUMP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 21:50 | pullback_tendencia | FIL | rotura de tendencia | -0.42% | -0.92% | -0.21 |
| 2026-09-29 21:45 | c_banda_atr_evento | ASTER | timeout | +0.25% | -0.85% | -0.19 |
| 2026-09-29 21:45 | c_banda_atr_tope | ASTER | timeout | +0.25% | -0.85% | -0.19 |
| 2026-09-29 21:45 | ruptura_estricta | PUMP | timeout | -0.78% | -1.58% | -0.36 |
| 2026-09-29 21:45 | c_banda_atr | ASTER | timeout | +0.25% | -0.25% | -0.06 |
| 2026-09-29 21:40 | ruptura_volumen_evento | RENDER | timeout | +0.18% | -0.62% | -0.14 |
| 2026-09-29 21:40 | ruptura_volumen_regimen | RENDER | timeout | +0.18% | -0.32% | -0.07 |
| 2026-09-29 21:40 | ruptura_volumen | RENDER | timeout | +0.18% | -0.32% | -0.07 |
| 2026-09-29 21:35 | ruptura_volumen_evento | DOT | timeout | -0.27% | -1.07% | -0.24 |
| 2026-09-29 21:35 | macd_momentum_evento | SPX | momentum perdido | +0.19% | -0.61% | -0.14 |
| 2026-09-29 21:35 | macd_momentum_evento | SHIB | momentum perdido | -0.43% | -0.93% | -0.21 |
| 2026-09-29 21:35 | macd_momentum_evento | ATOM | momentum perdido | -0.49% | -1.29% | -0.29 |
| 2026-09-29 21:35 | ruptura_volumen_regimen | DOT | timeout | -0.27% | -0.77% | -0.17 |
| 2026-09-29 21:35 | macd_momentum_regimen | ATOM | momentum perdido | -0.49% | -0.99% | -0.22 |

## Eventos de la última vuelta

- 2026-09-29 21:50 [estocastico_rebote] CIERRE PUMP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 21:45 [estocastico_rebote] ENTRADA JUP @ 0.28863 (22.31 €, apertura)
- 2026-09-29 21:45 [c_banda_atr_tope] ENTRADA BCH @ 272.59 (22.87 €, apertura)
- 2026-09-29 21:50 [pullback_tendencia] CIERRE FIL rotura de tendencia bruto -0.42% neto -0.92%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
