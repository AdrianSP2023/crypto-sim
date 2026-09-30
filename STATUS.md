# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 23:26 UTC · vueltas 106 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.50 € (-1.92%) | 71 | 30 | 27% | -0.390% | -1.258% | -1.400% | -20.51 € |
| reversion_bb | 922.00 € (-0.24%) | 10 | 4 | 40% | -0.070% | -1.170% | -1.296% | -2.71 € |
| ruptura_volumen | 896.26 € (-3.03%) | 95 | 22 | 17% | -0.481% | -1.256% | -1.391% | -27.32 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.54 € (-2.13%) | 66 | 3 | 15% | -0.407% | -1.307% | -1.444% | -19.77 € |
| macd_momentum | 905.63 € (-2.01%) | 109 | 26 | 24% | -0.085% | -0.825% | -0.953% | -20.61 € |
| estocastico_rebote | 903.40 € (-2.25%) | 127 | 8 | 35% | -0.037% | -0.743% | -0.875% | -21.70 € |
| ruptura_estricta | 898.65 € (-2.77%) | 51 | 9 | 12% | -1.194% | -2.211% | -2.360% | -25.94 € |
| macd_sin_salida | 905.36 € (-2.04%) | 87 | 29 | 33% | -0.214% | -1.014% | -1.143% | -20.29 € |
| c_banda_atr_tope | 919.65 € (-0.50%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.258% | -5.10 € |
| ruptura_volumen_tope | 916.14 € (-0.88%) | 27 | 5 | 19% | -0.185% | -1.285% | -1.398% | -8.00 € |
| c_banda_atr_regimen | 908.37 € (-1.72%) | 45 | 6 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.08 € (-1.42%) | 63 | 12 | 30% | -0.004% | -0.918% | -1.055% | -13.33 € |
| ruptura_volumen_regimen | 897.66 € (-2.88%) | 74 | 20 | 14% | -0.676% | -1.529% | -1.667% | -25.94 € |
| c_banda_atr_evento | 913.92 € (-1.12%) | 38 | 30 | 24% | -0.461% | -1.498% | -1.623% | -13.11 € |
| macd_momentum_evento | 910.72 € (-1.46%) | 62 | 26 | 16% | -0.171% | -1.092% | -1.213% | -15.53 € |
| ruptura_volumen_evento | 909.15 € (-1.63%) | 45 | 22 | 13% | -0.319% | -1.392% | -1.511% | -14.42 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 23:25 | ruptura_volumen_evento | MON | take-profit | +2.50% | +2.00% | +0.46 |
| 2026-09-30 23:25 | macd_momentum_evento | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 23:25 | c_banda_atr_evento | ASTER | timeout | +1.62% | +0.82% | +0.19 |
| 2026-09-30 23:25 | ruptura_volumen_regimen | MON | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 23:25 | macd_momentum_regimen | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 23:25 | macd_sin_salida | TON | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 23:25 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 23:25 | macd_sin_salida | POL | timeout | +1.75% | +1.25% | +0.28 |
| 2026-09-30 23:25 | macd_sin_salida | LINK | timeout | +0.40% | -0.10% | -0.02 |
| 2026-09-30 23:25 | ruptura_estricta | XDC | timeout | +0.46% | -0.04% | -0.01 |
| 2026-09-30 23:25 | macd_momentum | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 23:25 | ruptura_volumen | MON | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 23:25 | c_banda_atr | ASTER | timeout | +1.62% | +1.12% | +0.25 |
| 2026-09-30 23:20 | macd_momentum_evento | INJ | momentum perdido | -0.52% | -1.02% | -0.23 |
| 2026-09-30 23:20 | macd_momentum_evento | PUMP | momentum perdido | -0.89% | -1.39% | -0.32 |

## Eventos de la última vuelta

- 2026-09-30 23:20 [ruptura_volumen] ENTRADA LINK @ 12.7083 (22.41 €, apertura)
- 2026-09-30 23:25 [macd_sin_salida] CIERRE LINK timeout bruto +0.40% neto -0.10%
- 2026-09-30 23:20 [ruptura_volumen_evento] ENTRADA LINK @ 12.7083 (22.73 €, apertura)
- 2026-09-30 23:20 [pullback_tendencia] ENTRADA FET @ 0.2004 (22.61 €, apertura)
- 2026-09-30 23:25 [macd_sin_salida] CIERRE POL timeout bruto +1.75% neto +1.25%
- 2026-09-30 23:25 [ruptura_estricta] CIERRE XDC timeout bruto +0.46% neto -0.04%
- 2026-09-30 23:25 [ruptura_volumen] CIERRE MON take-profit bruto +2.50% neto +2.00%
- 2026-09-30 23:25 [macd_momentum] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 23:25 [macd_sin_salida] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 23:25 [macd_momentum_regimen] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 23:25 [ruptura_volumen_regimen] CIERRE MON take-profit bruto +2.50% neto +2.00%
- 2026-09-30 23:25 [macd_momentum_evento] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 23:25 [ruptura_volumen_evento] CIERRE MON take-profit bruto +2.50% neto +2.00%
- 2026-09-30 23:25 [c_banda_atr] CIERRE ASTER timeout bruto +1.62% neto +1.12%
- 2026-09-30 23:25 [c_banda_atr_evento] CIERRE ASTER timeout bruto +1.62% neto +0.82%
- 2026-09-30 23:25 [macd_sin_salida] CIERRE TON stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 23:20 [macd_momentum] ENTRADA KAS @ 0.03834 (22.59 €, apertura)
- 2026-09-30 23:20 [macd_sin_salida] ENTRADA KAS @ 0.03834 (22.60 €, apertura)
- 2026-09-30 23:20 [macd_momentum_evento] ENTRADA KAS @ 0.03834 (22.72 €, apertura)
- 2026-09-30 23:20 [ruptura_volumen] ENTRADA SKY @ 0.06876 (22.42 €, apertura)
- 2026-09-30 23:20 [ruptura_volumen_evento] ENTRADA SKY @ 0.06876 (22.75 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
