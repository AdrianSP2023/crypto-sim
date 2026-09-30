# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 20:11 UTC · vueltas 67 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.06 € (-1.86%) | 49 | 17 | 27% | -0.396% | -1.423% | -1.574% | -16.06 € |
| reversion_bb | 922.42 € (-0.20%) | 7 | 5 | 57% | +0.214% | -0.886% | -1.014% | -1.44 € |
| ruptura_volumen | 898.30 € (-2.81%) | 74 | 5 | 14% | -0.665% | -1.518% | -1.656% | -25.76 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 905.46 € (-2.03%) | 57 | 3 | 14% | -0.483% | -1.446% | -1.583% | -18.90 € |
| macd_momentum | 908.63 € (-1.69%) | 79 | 3 | 27% | -0.026% | -0.856% | -0.992% | -15.57 € |
| estocastico_rebote | 904.20 € (-2.17%) | 96 | 24 | 38% | -0.056% | -0.828% | -0.961% | -18.31 € |
| ruptura_estricta | 899.27 € (-2.70%) | 45 | 4 | 9% | -1.346% | -2.426% | -2.575% | -25.13 € |
| macd_sin_salida | 905.27 € (-2.05%) | 65 | 10 | 32% | -0.332% | -1.233% | -1.372% | -18.46 € |
| c_banda_atr_tope | 920.90 € (-0.36%) | 14 | 4 | 36% | +0.100% | -1.000% | -1.153% | -3.23 € |
| ruptura_volumen_tope | 918.11 € (-0.66%) | 18 | 5 | 22% | -0.331% | -1.431% | -1.522% | -5.94 € |
| c_banda_atr_regimen | 908.79 € (-1.67%) | 43 | 2 | 26% | -0.480% | -1.573% | -1.728% | -15.58 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 916.65 € (-0.82%) | 17 | 16 | 18% | -0.577% | -1.677% | -1.812% | -6.59 € |
| macd_momentum_evento | 915.32 € (-0.97%) | 32 | 3 | 19% | -0.106% | -1.206% | -1.338% | -8.88 € |
| ruptura_volumen_evento | 913.82 € (-1.13%) | 24 | 5 | 8% | -0.746% | -1.846% | -1.960% | -10.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 20:10 | rebote_extremo | ONDO | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 20:05 | c_banda_atr_evento | SEI | timeout | -0.82% | -1.92% | -0.44 |
| 2026-09-30 20:05 | c_banda_atr_evento | XMR | timeout | +0.17% | -0.93% | -0.21 |
| 2026-09-30 20:05 | c_banda_atr_regimen | SEI | timeout | -0.82% | -1.62% | -0.37 |
| 2026-09-30 20:05 | c_banda_atr_tope | XMR | timeout | +0.17% | -0.93% | -0.21 |
| 2026-09-30 20:05 | macd_sin_salida | ALGO | stop-loss | -1.51% | -2.01% | -0.46 |
| 2026-09-30 20:05 | c_banda_atr | SEI | timeout | -0.82% | -1.62% | -0.37 |
| 2026-09-30 20:00 | macd_momentum_evento | TON | momentum perdido | -0.22% | -1.32% | -0.30 |
| 2026-09-30 20:00 | macd_momentum_evento | XLM | momentum perdido | +0.15% | -0.95% | -0.22 |
| 2026-09-30 20:00 | estocastico_rebote | JUP | stop-loss | -1.60% | -2.10% | -0.48 |
| 2026-09-30 20:00 | estocastico_rebote | TRX | timeout | +0.11% | -0.39% | -0.09 |
| 2026-09-30 20:00 | macd_momentum | TON | momentum perdido | -0.22% | -0.72% | -0.16 |
| 2026-09-30 20:00 | macd_momentum | XLM | momentum perdido | +0.15% | -0.35% | -0.08 |
| 2026-09-30 19:55 | estocastico_rebote | SPX | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 19:55 | estocastico_rebote | DASH | stop-loss | -1.56% | -2.06% | -0.47 |

## Eventos de la última vuelta

- 2026-09-30 20:05 [pullback_tendencia] ENTRADA XLM @ 0.200074 (22.63 €, apertura)
- 2026-09-30 20:10 [rebote_extremo] CIERRE ONDO take-profit bruto +2.00% neto +0.90%
- 2026-09-30 20:05 [pullback_tendencia] ENTRADA MON @ 0.02558 (22.63 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
