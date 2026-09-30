# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 16:21 UTC · vueltas 49 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 915.60 € (-0.93%) | 32 | 11 | 38% | -0.172% | -1.272% | -1.442% | -9.41 € |
| reversion_bb | 924.04 € (-0.02%) | 3 | 1 | 67% | +0.500% | -0.600% | -0.707% | -0.42 € |
| ruptura_volumen | 905.16 € (-2.06%) | 51 | 5 | 16% | -0.638% | -1.650% | -1.798% | -19.38 € |
| rebote_extremo | 924.39 € (+0.02%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 912.43 € (-1.28%) | 33 | 1 | 18% | -0.461% | -1.561% | -1.697% | -11.86 € |
| macd_momentum | 912.86 € (-1.23%) | 56 | 7 | 32% | +0.060% | -0.906% | -1.052% | -11.71 € |
| estocastico_rebote | 918.13 € (-0.66%) | 58 | 16 | 48% | +0.189% | -0.704% | -0.868% | -9.48 € |
| ruptura_estricta | 902.49 € (-2.35%) | 38 | 3 | 11% | -1.302% | -2.402% | -2.549% | -21.08 € |
| macd_sin_salida | 909.38 € (-1.61%) | 53 | 8 | 34% | -0.231% | -1.224% | -1.370% | -14.99 € |
| c_banda_atr_tope | 923.47 € (-0.08%) | 9 | 5 | 56% | +0.446% | -0.654% | -0.837% | -1.36 € |
| ruptura_volumen_tope | 921.48 € (-0.30%) | 9 | 5 | 22% | -0.373% | -1.473% | -1.564% | -3.06 € |
| c_banda_atr_regimen | 914.60 € (-1.04%) | 30 | 7 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| macd_momentum_regimen | 912.67 € (-1.25%) | 50 | 4 | 30% | +0.002% | -1.020% | -1.162% | -11.78 € |
| ruptura_volumen_regimen | 904.89 € (-2.09%) | 52 | 4 | 15% | -0.649% | -1.651% | -1.798% | -19.76 € |
| c_banda_atr_evento | 925.77 € (+0.17%) | 2 | 9 | 100% | +2.000% | +0.900% | +0.614% | +0.42 € |
| macd_momentum_evento | 922.76 € (-0.16%) | 9 | 7 | 44% | +0.227% | -0.873% | -1.060% | -1.82 € |
| ruptura_volumen_evento | 924.02 € (-0.02%) | 1 | 5 | 0% | -1.200% | -2.300% | -2.340% | -0.53 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 16:20 | macd_sin_salida | TRX | timeout | -0.43% | -1.24% | -0.29 |
| 2026-09-30 16:15 | ruptura_volumen_evento | MON | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 16:15 | ruptura_volumen_regimen | MON | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 16:15 | estocastico_rebote | ENA | take-profit | +1.80% | +1.30% | +0.30 |
| 2026-09-30 16:15 | ruptura_volumen | MON | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 16:10 | macd_momentum_evento | SPX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:10 | macd_momentum_evento | MON | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:10 | c_banda_atr_evento | SPX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:10 | macd_momentum_regimen | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 16:10 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 16:10 | estocastico_rebote | NIGHT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 16:10 | estocastico_rebote | WLD | take-profit | +2.13% | +1.63% | +0.37 |
| 2026-09-30 16:10 | estocastico_rebote | TAO | take-profit | +1.83% | +1.03% | +0.24 |
| 2026-09-30 16:10 | estocastico_rebote | ZEC | take-profit | +1.80% | +1.30% | +0.26 |
| 2026-09-30 16:10 | estocastico_rebote | ADA | take-profit | +1.80% | +1.30% | +0.30 |

## Eventos de la última vuelta

- 2026-09-30 16:20 [macd_sin_salida] CIERRE TRX timeout bruto -0.43% neto -1.23%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
