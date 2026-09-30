# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 20:26 UTC · vueltas 70 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.78 € (-1.56%) | 49 | 23 | 27% | -0.396% | -1.423% | -1.574% | -16.06 € |
| reversion_bb | 922.84 € (-0.15%) | 7 | 5 | 57% | +0.214% | -0.886% | -1.014% | -1.44 € |
| ruptura_volumen | 898.97 € (-2.73%) | 74 | 5 | 14% | -0.665% | -1.518% | -1.656% | -25.76 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 906.12 € (-1.96%) | 58 | 3 | 16% | -0.440% | -1.395% | -1.533% | -18.56 € |
| macd_momentum | 909.60 € (-1.58%) | 79 | 6 | 27% | -0.026% | -0.856% | -0.992% | -15.57 € |
| estocastico_rebote | 907.59 € (-1.80%) | 99 | 23 | 38% | -0.027% | -0.790% | -0.925% | -18.03 € |
| ruptura_estricta | 899.46 € (-2.68%) | 46 | 3 | 11% | -1.277% | -2.350% | -2.498% | -24.89 € |
| macd_sin_salida | 906.92 € (-1.87%) | 66 | 10 | 33% | -0.296% | -1.192% | -1.330% | -18.12 € |
| c_banda_atr_tope | 921.88 € (-0.26%) | 14 | 5 | 36% | +0.100% | -1.000% | -1.153% | -3.23 € |
| ruptura_volumen_tope | 918.80 € (-0.59%) | 18 | 5 | 22% | -0.331% | -1.431% | -1.522% | -5.94 € |
| c_banda_atr_regimen | 908.91 € (-1.66%) | 43 | 2 | 26% | -0.480% | -1.573% | -1.728% | -15.58 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 919.38 € (-0.53%) | 17 | 22 | 18% | -0.577% | -1.677% | -1.812% | -6.59 € |
| macd_momentum_evento | 916.29 € (-0.86%) | 32 | 6 | 19% | -0.106% | -1.206% | -1.338% | -8.88 € |
| ruptura_volumen_evento | 914.51 € (-1.05%) | 24 | 5 | 8% | -0.746% | -1.846% | -1.960% | -10.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 20:25 | estocastico_rebote | ASTER | timeout | +0.17% | -0.33% | -0.08 |
| 2026-09-30 20:25 | estocastico_rebote | FET | take-profit | +1.99% | +1.49% | +0.34 |
| 2026-09-30 20:25 | pullback_tendencia | FET | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 20:20 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 20:20 | ruptura_estricta | MON | timeout | +1.86% | +1.06% | +0.24 |
| 2026-09-30 20:20 | estocastico_rebote | XDC | timeout | +0.53% | +0.03% | +0.01 |
| 2026-09-30 20:10 | rebote_extremo | ONDO | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 20:05 | c_banda_atr_evento | SEI | timeout | -0.82% | -1.92% | -0.44 |
| 2026-09-30 20:05 | c_banda_atr_evento | XMR | timeout | +0.17% | -0.93% | -0.21 |
| 2026-09-30 20:05 | c_banda_atr_regimen | SEI | timeout | -0.82% | -1.62% | -0.37 |
| 2026-09-30 20:05 | c_banda_atr_tope | XMR | timeout | +0.17% | -0.93% | -0.21 |
| 2026-09-30 20:05 | macd_sin_salida | ALGO | stop-loss | -1.51% | -2.01% | -0.46 |
| 2026-09-30 20:05 | c_banda_atr | SEI | timeout | -0.82% | -1.62% | -0.37 |
| 2026-09-30 20:00 | macd_momentum_evento | TON | momentum perdido | -0.22% | -1.32% | -0.30 |
| 2026-09-30 20:00 | macd_momentum_evento | XLM | momentum perdido | +0.15% | -0.95% | -0.22 |

## Eventos de la última vuelta

- 2026-09-30 20:20 [macd_momentum] ENTRADA XLM @ 0.200497 (22.72 €, apertura)
- 2026-09-30 20:20 [macd_momentum_evento] ENTRADA XLM @ 0.200497 (22.88 €, apertura)
- 2026-09-30 20:20 [macd_momentum] ENTRADA UNI @ 7.8521 (22.72 €, apertura)
- 2026-09-30 20:20 [macd_sin_salida] ENTRADA UNI @ 7.8521 (22.65 €, apertura)
- 2026-09-30 20:20 [macd_momentum_evento] ENTRADA UNI @ 7.8521 (22.88 €, apertura)
- 2026-09-30 20:25 [pullback_tendencia] CIERRE FET take-profit bruto +2.00% neto +1.50%
- 2026-09-30 20:25 [estocastico_rebote] CIERRE FET take-profit bruto +1.99% neto +1.49%
- 2026-09-30 20:20 [c_banda_atr] ENTRADA USELESS @ 0.21122 (22.70 €, apertura)
- 2026-09-30 20:20 [c_banda_atr_evento] ENTRADA USELESS @ 0.21122 (22.94 €, apertura)
- 2026-09-30 20:20 [c_banda_atr] ENTRADA JUP @ 0.28958 (22.70 €, apertura)
- 2026-09-30 20:20 [c_banda_atr_evento] ENTRADA JUP @ 0.28958 (22.94 €, apertura)
- 2026-09-30 20:20 [c_banda_atr] ENTRADA PEPE @ 3.8e-06 (22.70 €, apertura)
- 2026-09-30 20:20 [c_banda_atr_evento] ENTRADA PEPE @ 3.8e-06 (22.94 €, apertura)
- 2026-09-30 20:25 [estocastico_rebote] CIERRE ASTER timeout bruto +0.17% neto -0.33%
- 2026-09-30 20:20 [c_banda_atr] ENTRADA DASH @ 53.432 (22.70 €, apertura)
- 2026-09-30 20:20 [c_banda_atr_evento] ENTRADA DASH @ 53.432 (22.94 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
