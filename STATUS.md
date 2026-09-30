# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 20:21 UTC · vueltas 69 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.62 € (-1.80%) | 49 | 19 | 27% | -0.396% | -1.423% | -1.574% | -16.06 € |
| reversion_bb | 922.48 € (-0.19%) | 7 | 5 | 57% | +0.214% | -0.886% | -1.014% | -1.44 € |
| ruptura_volumen | 898.51 € (-2.78%) | 74 | 5 | 14% | -0.665% | -1.518% | -1.656% | -25.76 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 905.63 € (-2.01%) | 57 | 4 | 14% | -0.483% | -1.446% | -1.583% | -18.90 € |
| macd_momentum | 908.81 € (-1.67%) | 79 | 4 | 27% | -0.026% | -0.856% | -0.992% | -15.57 € |
| estocastico_rebote | 904.95 € (-2.09%) | 97 | 25 | 38% | -0.050% | -0.819% | -0.953% | -18.30 € |
| ruptura_estricta | 899.22 € (-2.71%) | 46 | 3 | 11% | -1.277% | -2.350% | -2.498% | -24.89 € |
| macd_sin_salida | 905.81 € (-1.99%) | 66 | 9 | 33% | -0.296% | -1.192% | -1.330% | -18.12 € |
| c_banda_atr_tope | 921.09 € (-0.34%) | 14 | 5 | 36% | +0.100% | -1.000% | -1.153% | -3.23 € |
| ruptura_volumen_tope | 918.33 € (-0.64%) | 18 | 5 | 22% | -0.331% | -1.431% | -1.522% | -5.94 € |
| c_banda_atr_regimen | 908.80 € (-1.67%) | 43 | 2 | 26% | -0.480% | -1.573% | -1.728% | -15.58 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 917.21 € (-0.76%) | 17 | 18 | 18% | -0.577% | -1.677% | -1.812% | -6.59 € |
| macd_momentum_evento | 915.50 € (-0.95%) | 32 | 4 | 19% | -0.106% | -1.206% | -1.338% | -8.88 € |
| ruptura_volumen_evento | 914.04 € (-1.10%) | 24 | 5 | 8% | -0.746% | -1.846% | -1.960% | -10.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-30 20:00 | estocastico_rebote | JUP | stop-loss | -1.60% | -2.10% | -0.48 |
| 2026-09-30 20:00 | estocastico_rebote | TRX | timeout | +0.11% | -0.39% | -0.09 |
| 2026-09-30 20:00 | macd_momentum | TON | momentum perdido | -0.22% | -0.72% | -0.16 |

## Eventos de la última vuelta

- 2026-09-30 20:15 [estocastico_rebote] ENTRADA NEAR @ 4.7104 (22.65 €, apertura)
- 2026-09-30 20:15 [c_banda_atr] ENTRADA SUI @ 1.024 (22.70 €, apertura)
- 2026-09-30 20:15 [c_banda_atr_evento] ENTRADA SUI @ 1.024 (22.94 €, apertura)
- 2026-09-30 20:20 [estocastico_rebote] CIERRE XDC timeout bruto +0.53% neto +0.03%
- 2026-09-30 20:15 [macd_momentum] ENTRADA MON @ 0.02593 (22.72 €, apertura)
- 2026-09-30 20:20 [ruptura_estricta] CIERRE MON timeout bruto +1.86% neto +1.06%
- 2026-09-30 20:20 [macd_sin_salida] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 20:15 [macd_momentum_evento] ENTRADA MON @ 0.02593 (22.88 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
