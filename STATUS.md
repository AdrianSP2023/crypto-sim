# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 03:11 UTC · vueltas 109 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.13 € (-2.28%) | 104 | 27 | 29% | -0.202% | -0.953% | -1.076% | -22.73 € |
| reversion_bb | 921.28 € (-0.32%) | 13 | 5 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 890.70 € (-3.63%) | 140 | 14 | 19% | -0.366% | -1.052% | -1.168% | -33.60 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.18 € (-2.28%) | 83 | 5 | 16% | -0.312% | -1.130% | -1.250% | -21.48 € |
| macd_momentum | 897.09 € (-2.94%) | 182 | 27 | 21% | -0.037% | -0.680% | -0.788% | -28.24 € |
| estocastico_rebote | 902.60 € (-2.34%) | 150 | 18 | 37% | +0.043% | -0.631% | -0.753% | -21.77 € |
| ruptura_estricta | 899.62 € (-2.66%) | 63 | 20 | 17% | -0.812% | -1.731% | -1.871% | -25.10 € |
| macd_sin_salida | 903.50 € (-2.24%) | 122 | 38 | 35% | -0.051% | -0.765% | -0.881% | -21.44 € |
| c_banda_atr_tope | 917.67 € (-0.71%) | 25 | 5 | 24% | -0.111% | -1.211% | -1.337% | -6.98 € |
| ruptura_volumen_tope | 914.09 € (-1.10%) | 41 | 5 | 22% | +0.040% | -1.060% | -1.161% | -10.00 € |
| c_banda_atr_regimen | 907.97 € (-1.76%) | 53 | 21 | 26% | -0.396% | -1.389% | -1.541% | -16.93 € |
| macd_momentum_regimen | 905.64 € (-2.01%) | 97 | 26 | 21% | -0.087% | -0.856% | -0.974% | -19.07 € |
| ruptura_volumen_regimen | 891.84 € (-3.51%) | 110 | 17 | 14% | -0.551% | -1.288% | -1.409% | -32.34 € |
| c_banda_atr_evento | 909.14 € (-1.63%) | 71 | 27 | 28% | -0.152% | -1.024% | -1.131% | -16.72 € |
| macd_momentum_evento | 902.07 € (-2.40%) | 135 | 27 | 16% | -0.059% | -0.755% | -0.853% | -23.28 € |
| ruptura_volumen_evento | 903.38 € (-2.26%) | 90 | 14 | 19% | -0.221% | -1.014% | -1.111% | -20.92 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 03:10 | ruptura_volumen_evento | RENDER | timeout | +0.53% | +0.03% | +0.01 |
| 2026-10-01 03:10 | ruptura_volumen_evento | BCH | timeout | -0.41% | -0.91% | -0.20 |
| 2026-10-01 03:10 | ruptura_volumen_evento | ICP | timeout | +1.52% | +1.02% | +0.23 |
| 2026-10-01 03:10 | macd_momentum_evento | TRX | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-10-01 03:10 | macd_momentum | TRX | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-10-01 03:10 | pullback_tendencia | TRX | rotura de tendencia | -0.12% | -0.62% | -0.14 |
| 2026-10-01 03:10 | ruptura_volumen | RENDER | timeout | +0.53% | +0.03% | +0.01 |
| 2026-10-01 03:10 | ruptura_volumen | BCH | timeout | -0.41% | -0.91% | -0.20 |
| 2026-10-01 03:10 | ruptura_volumen | ICP | timeout | +1.52% | +1.02% | +0.23 |
| 2026-10-01 03:05 | ruptura_volumen_evento | TRUMP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 03:05 | macd_momentum_evento | AAVE | take-profit | +2.02% | +1.52% | +0.34 |
| 2026-10-01 03:05 | ruptura_volumen_regimen | TRUMP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 03:05 | ruptura_volumen_tope | TRUMP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-10-01 03:05 | macd_sin_salida | ALGO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 03:05 | estocastico_rebote | ENA | take-profit | +1.80% | +1.30% | +0.29 |

## Eventos de la última vuelta

- 2026-10-01 03:05 [pullback_tendencia] ENTRADA ETH @ 2370.46 (22.57 €, apertura)
- 2026-10-01 03:05 [ruptura_volumen] ENTRADA AAVE @ 144.19 (22.27 €, apertura)
- 2026-10-01 03:05 [ruptura_volumen_regimen] ENTRADA AAVE @ 144.19 (22.30 €, apertura)
- 2026-10-01 03:05 [ruptura_volumen_evento] ENTRADA AAVE @ 144.19 (22.58 €, apertura)
- 2026-10-01 03:10 [ruptura_volumen] CIERRE ICP timeout bruto +1.52% neto +1.02%
- 2026-10-01 03:10 [ruptura_volumen_evento] CIERRE ICP timeout bruto +1.52% neto +1.02%
- 2026-10-01 03:10 [pullback_tendencia] CIERRE TRX rotura de tendencia bruto -0.12% neto -0.62%
- 2026-10-01 03:10 [macd_momentum] CIERRE TRX momentum perdido bruto -0.13% neto -0.63%
- 2026-10-01 03:10 [macd_momentum_evento] CIERRE TRX momentum perdido bruto -0.13% neto -0.63%
- 2026-10-01 03:05 [macd_momentum] ENTRADA ONDO @ 0.44676 (22.40 €, apertura)
- 2026-10-01 03:05 [macd_sin_salida] ENTRADA ONDO @ 0.44676 (22.57 €, apertura)
- 2026-10-01 03:05 [macd_momentum_regimen] ENTRADA ONDO @ 0.44676 (22.63 €, apertura)
- 2026-10-01 03:05 [macd_momentum_evento] ENTRADA ONDO @ 0.44676 (22.52 €, apertura)
- 2026-10-01 03:05 [estocastico_rebote] ENTRADA XDC @ 0.03088 (22.56 €, apertura)
- 2026-10-01 03:10 [ruptura_volumen] CIERRE BCH timeout bruto -0.41% neto -0.91%
- 2026-10-01 03:10 [ruptura_volumen_evento] CIERRE BCH timeout bruto -0.41% neto -0.91%
- 2026-10-01 03:10 [ruptura_volumen] CIERRE RENDER timeout bruto +0.53% neto +0.03%
- 2026-10-01 03:10 [ruptura_volumen_evento] CIERRE RENDER timeout bruto +0.53% neto +0.03%
- 2026-10-01 03:05 [ruptura_volumen] ENTRADA MINA @ 0.1306 (22.27 €, apertura)
- 2026-10-01 03:05 [ruptura_volumen_regimen] ENTRADA MINA @ 0.1306 (22.30 €, apertura)
- 2026-10-01 03:05 [ruptura_volumen_evento] ENTRADA MINA @ 0.1306 (22.58 €, apertura)
- 2026-10-01 03:05 [ruptura_volumen] ENTRADA SHIB @ 5.096e-06 (22.27 €, apertura)
- 2026-10-01 03:05 [macd_momentum] ENTRADA SHIB @ 5.096e-06 (22.40 €, apertura)
- 2026-10-01 03:05 [macd_sin_salida] ENTRADA SHIB @ 5.096e-06 (22.57 €, apertura)
- 2026-10-01 03:05 [macd_momentum_regimen] ENTRADA SHIB @ 5.096e-06 (22.63 €, apertura)
- 2026-10-01 03:05 [ruptura_volumen_regimen] ENTRADA SHIB @ 5.096e-06 (22.30 €, apertura)
- 2026-10-01 03:05 [macd_momentum_evento] ENTRADA SHIB @ 5.096e-06 (22.52 €, apertura)
- 2026-10-01 03:05 [ruptura_volumen_evento] ENTRADA SHIB @ 5.096e-06 (22.58 €, apertura)
- 2026-10-01 03:05 [ruptura_volumen] ENTRADA PENGU @ 0.008606 (22.27 €, apertura)
- 2026-10-01 03:05 [ruptura_estricta] ENTRADA PENGU @ 0.008606 (22.48 €, apertura)
- 2026-10-01 03:05 [ruptura_volumen_regimen] ENTRADA PENGU @ 0.008606 (22.30 €, apertura)
- 2026-10-01 03:05 [ruptura_volumen_evento] ENTRADA PENGU @ 0.008606 (22.58 €, apertura)
- 2026-10-01 03:05 [macd_momentum] ENTRADA BNB @ 677.7 (22.40 €, apertura)
- 2026-10-01 03:05 [macd_sin_salida] ENTRADA BNB @ 677.7 (22.57 €, apertura)
- 2026-10-01 03:05 [macd_momentum_regimen] ENTRADA BNB @ 677.7 (22.63 €, apertura)
- 2026-10-01 03:05 [macd_momentum_evento] ENTRADA BNB @ 677.7 (22.52 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
