# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 01:21 UTC · vueltas 87 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 904.34 € (-2.15%) | 91 | 23 | 27% | -0.251% | -1.037% | -1.165% | -21.67 € |
| reversion_bb | 921.63 € (-0.28%) | 13 | 3 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 893.83 € (-3.29%) | 119 | 12 | 16% | -0.425% | -1.145% | -1.259% | -31.12 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.97 € (-2.09%) | 76 | 6 | 17% | -0.305% | -1.152% | -1.279% | -20.07 € |
| macd_momentum | 904.36 € (-2.15%) | 139 | 31 | 24% | -0.044% | -0.732% | -0.845% | -23.29 € |
| estocastico_rebote | 903.87 € (-2.20%) | 138 | 14 | 37% | +0.021% | -0.668% | -0.791% | -21.23 € |
| ruptura_estricta | 899.74 € (-2.65%) | 56 | 13 | 16% | -1.018% | -1.989% | -2.131% | -25.63 € |
| macd_sin_salida | 905.57 € (-2.02%) | 99 | 31 | 35% | -0.176% | -0.940% | -1.064% | -21.39 € |
| c_banda_atr_tope | 918.69 € (-0.60%) | 21 | 5 | 29% | -0.083% | -1.183% | -1.319% | -5.73 € |
| ruptura_volumen_tope | 915.22 € (-0.98%) | 33 | 5 | 18% | -0.115% | -1.215% | -1.296% | -9.23 € |
| c_banda_atr_regimen | 908.07 € (-1.75%) | 47 | 9 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 909.35 € (-1.61%) | 78 | 12 | 24% | -0.062% | -0.896% | -1.021% | -16.08 € |
| ruptura_volumen_regimen | 895.05 € (-3.16%) | 96 | 5 | 14% | -0.572% | -1.344% | -1.466% | -29.50 € |
| c_banda_atr_evento | 910.70 € (-1.46%) | 58 | 23 | 26% | -0.217% | -1.147% | -1.256% | -15.31 € |
| macd_momentum_evento | 909.37 € (-1.61%) | 92 | 31 | 17% | -0.081% | -0.868% | -0.969% | -18.31 € |
| ruptura_volumen_evento | 906.55 € (-1.91%) | 69 | 12 | 13% | -0.279% | -1.162% | -1.251% | -18.41 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 01:20 | ruptura_volumen_evento | SKY | timeout | +0.47% | -0.04% | -0.01 |
| 2026-10-01 01:20 | ruptura_volumen_evento | LINK | timeout | -0.12% | -0.62% | -0.14 |
| 2026-10-01 01:20 | c_banda_atr_evento | ONDO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 01:20 | macd_sin_salida | SPX | timeout | +1.29% | +0.79% | +0.18 |
| 2026-10-01 01:20 | macd_sin_salida | NEAR | timeout | -1.15% | -1.65% | -0.37 |
| 2026-10-01 01:20 | estocastico_rebote | XLM | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 01:20 | pullback_tendencia | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 01:20 | ruptura_volumen | SKY | timeout | +0.47% | -0.04% | -0.01 |
| 2026-10-01 01:20 | ruptura_volumen | LINK | timeout | -0.12% | -0.62% | -0.14 |
| 2026-10-01 01:20 | reversion_bb | SOL | timeout | +0.20% | -0.90% | -0.21 |
| 2026-10-01 01:20 | c_banda_atr | ONDO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 01:15 | ruptura_estricta | ZRO | timeout | -1.76% | -2.26% | -0.51 |
| 2026-10-01 01:15 | estocastico_rebote | BNB | timeout | +0.51% | +0.01% | +0.00 |
| 2026-10-01 01:15 | estocastico_rebote | KSM | timeout | +1.77% | +1.27% | +0.29 |
| 2026-10-01 01:10 | macd_momentum_evento | FET | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-10-01 01:20 [reversion_bb] CIERRE SOL timeout bruto +0.20% neto -0.90%
- 2026-10-01 01:20 [macd_sin_salida] CIERRE NEAR timeout bruto -1.15% neto -1.65%
- 2026-10-01 01:20 [ruptura_volumen] CIERRE LINK timeout bruto -0.12% neto -0.62%
- 2026-10-01 01:20 [ruptura_volumen_evento] CIERRE LINK timeout bruto -0.12% neto -0.62%
- 2026-10-01 01:20 [estocastico_rebote] CIERRE XLM take-profit bruto +1.80% neto +1.30%
- 2026-10-01 01:15 [macd_momentum_regimen] ENTRADA TRX @ 0.298148 (22.70 €, apertura)
- 2026-10-01 01:20 [c_banda_atr] CIERRE ONDO take-profit bruto +2.00% neto +1.50%
- 2026-10-01 01:20 [c_banda_atr_evento] CIERRE ONDO take-profit bruto +2.00% neto +1.50%
- 2026-10-01 01:20 [pullback_tendencia] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-10-01 01:15 [macd_momentum] ENTRADA INJ @ 6.554 (22.52 €, apertura)
- 2026-10-01 01:15 [macd_momentum_regimen] ENTRADA INJ @ 6.554 (22.70 €, apertura)
- 2026-10-01 01:15 [macd_momentum_evento] ENTRADA INJ @ 6.554 (22.65 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen] CIERRE SKY timeout bruto +0.47% neto -0.03%
- 2026-10-01 01:20 [ruptura_volumen_evento] CIERRE SKY timeout bruto +0.47% neto -0.03%
- 2026-10-01 01:20 [macd_sin_salida] CIERRE SPX timeout bruto +1.29% neto +0.79%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
