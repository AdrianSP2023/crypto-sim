# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 22:01 UTC · vueltas 148 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.97 € (-1.87%) | 63 | 15 | 33% | -0.182% | -1.096% | -1.242% | -15.91 € |
| reversion_bb | 917.76 € (-0.70%) | 18 | 3 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 903.20 € (-2.28%) | 103 | 8 | 23% | -0.137% | -0.890% | -1.021% | -21.01 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.98 € (-1.98%) | 81 | 2 | 23% | -0.174% | -0.996% | -1.119% | -18.50 € |
| macd_momentum | 892.51 € (-3.43%) | 187 | 2 | 18% | -0.102% | -0.742% | -0.858% | -31.64 € |
| estocastico_rebote | 892.48 € (-3.44%) | 155 | 13 | 30% | -0.232% | -0.900% | -1.021% | -31.88 € |
| ruptura_estricta | 909.98 € (-1.54%) | 46 | 6 | 28% | -0.245% | -1.313% | -1.447% | -13.90 € |
| macd_sin_salida | 901.87 € (-2.42%) | 104 | 26 | 32% | -0.095% | -0.846% | -0.978% | -20.17 € |
| c_banda_atr_tope | 913.88 € (-1.12%) | 26 | 4 | 23% | -0.588% | -1.688% | -1.841% | -10.11 € |
| ruptura_volumen_tope | 915.84 € (-0.91%) | 31 | 5 | 16% | -0.099% | -1.199% | -1.321% | -8.56 € |
| c_banda_atr_regimen | 907.54 € (-1.81%) | 53 | 9 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.80 € (-3.29%) | 173 | 0 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 906.60 € (-1.91%) | 86 | 6 | 24% | -0.091% | -0.894% | -1.026% | -17.65 € |
| c_banda_atr_evento | 911.86 € (-1.34%) | 31 | 15 | 29% | -0.442% | -1.542% | -1.705% | -11.02 € |
| macd_momentum_evento | 905.06 € (-2.08%) | 67 | 2 | 10% | -0.346% | -1.240% | -1.356% | -19.09 € |
| ruptura_volumen_evento | 909.10 € (-1.64%) | 44 | 8 | 14% | -0.426% | -1.492% | -1.631% | -15.10 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 22:00 | estocastico_rebote | AAVE | timeout | +0.38% | -0.12% | -0.03 |
| 2026-09-29 22:00 | pullback_tendencia | QNT | stop-loss | -1.68% | -2.18% | -0.49 |
| 2026-09-29 21:55 | c_banda_atr_evento | ALGO | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 21:55 | c_banda_atr_tope | ALGO | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 21:55 | c_banda_atr | ALGO | stop-loss | -1.50% | -2.00% | -0.46 |
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

## Eventos de la última vuelta

- 2026-09-29 22:00 [pullback_tendencia] CIERRE QNT stop-loss bruto -1.68% neto -2.18%
- 2026-09-29 22:00 [estocastico_rebote] CIERRE AAVE timeout bruto +0.38% neto -0.12%
- 2026-09-29 21:55 [macd_momentum] ENTRADA DOGE @ 0.0829733 (22.32 €, apertura)
- 2026-09-29 21:55 [macd_momentum_evento] ENTRADA DOGE @ 0.0829733 (22.63 €, apertura)
- 2026-09-29 21:55 [estocastico_rebote] ENTRADA SPX @ 0.3692 (22.31 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
