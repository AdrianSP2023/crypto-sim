# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 21:56 UTC · vueltas 147 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.50 € (-1.81%) | 63 | 15 | 33% | -0.182% | -1.096% | -1.242% | -15.91 € |
| reversion_bb | 917.82 € (-0.70%) | 18 | 3 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 903.35 € (-2.26%) | 103 | 8 | 23% | -0.137% | -0.890% | -1.021% | -21.01 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.12 € (-1.96%) | 80 | 3 | 24% | -0.155% | -0.981% | -1.101% | -18.01 € |
| macd_momentum | 892.63 € (-3.42%) | 187 | 1 | 18% | -0.102% | -0.742% | -0.858% | -31.64 € |
| estocastico_rebote | 892.57 € (-3.43%) | 154 | 13 | 31% | -0.236% | -0.905% | -1.026% | -31.86 € |
| ruptura_estricta | 910.10 € (-1.53%) | 46 | 6 | 28% | -0.245% | -1.313% | -1.447% | -13.90 € |
| macd_sin_salida | 902.29 € (-2.37%) | 104 | 26 | 32% | -0.095% | -0.846% | -0.978% | -20.17 € |
| c_banda_atr_tope | 914.23 € (-1.08%) | 26 | 4 | 23% | -0.588% | -1.688% | -1.841% | -10.11 € |
| ruptura_volumen_tope | 915.82 € (-0.91%) | 31 | 5 | 16% | -0.099% | -1.199% | -1.321% | -8.56 € |
| c_banda_atr_regimen | 907.84 € (-1.77%) | 53 | 9 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.80 € (-3.29%) | 173 | 0 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 906.68 € (-1.90%) | 86 | 6 | 24% | -0.091% | -0.894% | -1.026% | -17.65 € |
| c_banda_atr_evento | 912.40 € (-1.28%) | 31 | 15 | 29% | -0.442% | -1.542% | -1.705% | -11.02 € |
| macd_momentum_evento | 905.18 € (-2.06%) | 67 | 1 | 10% | -0.346% | -1.240% | -1.356% | -19.09 € |
| ruptura_volumen_evento | 909.25 € (-1.62%) | 44 | 8 | 14% | -0.426% | -1.492% | -1.631% | -15.10 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-29 21:35 | macd_momentum_evento | SPX | momentum perdido | +0.19% | -0.61% | -0.14 |
| 2026-09-29 21:35 | macd_momentum_evento | SHIB | momentum perdido | -0.43% | -0.93% | -0.21 |

## Eventos de la última vuelta

- 2026-09-29 21:50 [c_banda_atr] ENTRADA ZEC @ 1245.81 (22.72 €, apertura)
- 2026-09-29 21:50 [ruptura_volumen] ENTRADA ZEC @ 1245.81 (22.58 €, apertura)
- 2026-09-29 21:50 [ruptura_volumen_tope] ENTRADA ZEC @ 1245.81 (22.89 €, apertura)
- 2026-09-29 21:50 [c_banda_atr_evento] ENTRADA ZEC @ 1245.81 (22.85 €, apertura)
- 2026-09-29 21:50 [ruptura_volumen_evento] ENTRADA ZEC @ 1245.81 (22.73 €, apertura)
- 2026-09-29 21:55 [c_banda_atr] CIERRE ALGO stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 21:55 [c_banda_atr_tope] CIERRE ALGO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 21:55 [c_banda_atr_evento] CIERRE ALGO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 21:50 [macd_momentum] ENTRADA BCH @ 273.01 (22.32 €, apertura)
- 2026-09-29 21:50 [ruptura_estricta] ENTRADA BCH @ 273.01 (22.76 €, apertura)
- 2026-09-29 21:50 [macd_momentum_evento] ENTRADA BCH @ 273.01 (22.63 €, apertura)
- 2026-09-29 21:50 [estocastico_rebote] ENTRADA INJ @ 6.79 (22.31 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
