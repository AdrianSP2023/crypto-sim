# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 18:01 UTC · vueltas 69 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.44 € (-1.49%) | 41 | 10 | 32% | -0.270% | -1.340% | -1.501% | -12.68 € |
| reversion_bb | 923.48 € (-0.08%) | 4 | 3 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 899.96 € (-2.63%) | 67 | 6 | 13% | -0.709% | -1.598% | -1.738% | -24.57 € |
| rebote_extremo | 923.90 € (-0.04%) | 2 | 0 | 50% | +0.370% | -0.731% | -0.816% | -0.34 € |
| pullback_tendencia | 907.61 € (-1.80%) | 50 | 4 | 16% | -0.411% | -1.433% | -1.561% | -16.46 € |
| macd_momentum | 911.33 € (-1.40%) | 67 | 4 | 31% | +0.040% | -0.849% | -0.996% | -13.12 € |
| estocastico_rebote | 913.75 € (-1.14%) | 74 | 31 | 47% | +0.293% | -0.560% | -0.707% | -9.62 € |
| ruptura_estricta | 900.82 € (-2.53%) | 43 | 3 | 9% | -1.345% | -2.438% | -2.586% | -24.15 € |
| macd_sin_salida | 907.25 € (-1.84%) | 61 | 6 | 33% | -0.285% | -1.212% | -1.357% | -17.06 € |
| c_banda_atr_tope | 922.18 € (-0.22%) | 10 | 5 | 50% | +0.251% | -0.849% | -1.020% | -1.96 € |
| ruptura_volumen_tope | 918.93 € (-0.57%) | 16 | 1 | 19% | -0.453% | -1.553% | -1.655% | -5.74 € |
| c_banda_atr_regimen | 910.46 € (-1.49%) | 38 | 7 | 29% | -0.357% | -1.457% | -1.613% | -12.78 € |
| macd_momentum_regimen | 911.61 € (-1.37%) | 58 | 2 | 31% | +0.010% | -0.940% | -1.086% | -12.58 € |
| ruptura_volumen_regimen | 899.37 € (-2.69%) | 67 | 5 | 13% | -0.721% | -1.610% | -1.751% | -24.75 € |
| c_banda_atr_evento | 920.72 € (-0.38%) | 8 | 11 | 38% | -0.201% | -1.301% | -1.463% | -2.41 € |
| macd_momentum_evento | 919.70 € (-0.49%) | 20 | 4 | 30% | +0.069% | -1.031% | -1.198% | -4.76 € |
| ruptura_volumen_evento | 916.49 € (-0.84%) | 17 | 6 | 6% | -0.950% | -2.050% | -2.160% | -8.05 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 18:00 | macd_momentum_evento | XLM | momentum perdido | -0.24% | -1.34% | -0.31 |
| 2026-09-30 18:00 | macd_momentum_regimen | XLM | momentum perdido | -0.24% | -0.74% | -0.17 |
| 2026-09-30 18:00 | macd_momentum | XLM | momentum perdido | -0.24% | -0.74% | -0.17 |
| 2026-09-30 18:00 | pullback_tendencia | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 17:55 | macd_sin_salida | ENA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 17:55 | ruptura_estricta | KSM | stop-loss | -2.17% | -2.96% | -0.67 |
| 2026-09-30 17:50 | pullback_tendencia | USELESS | rotura de tendencia | -1.07% | -1.87% | -0.43 |
| 2026-09-30 17:45 | ruptura_volumen_evento | AAVE | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:45 | macd_momentum_evento | TON | momentum perdido | +0.07% | -1.02% | -0.24 |
| 2026-09-30 17:45 | macd_momentum_evento | NIGHT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 17:45 | c_banda_atr_evento | INJ | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 17:45 | ruptura_volumen_regimen | AAVE | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 17:45 | macd_momentum_regimen | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 17:45 | c_banda_atr_regimen | INJ | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-30 17:45 | ruptura_volumen_tope | XMR | stop-loss | -1.20% | -2.30% | -0.53 |

## Eventos de la última vuelta

- 2026-09-30 17:55 [estocastico_rebote] ENTRADA ZEC @ 1272 (22.87 €, apertura)
- 2026-09-30 17:55 [estocastico_rebote] ENTRADA HYPE @ 78.56 (22.87 €, apertura)
- 2026-09-30 18:00 [macd_momentum] CIERRE XLM momentum perdido bruto -0.25% neto -0.75%
- 2026-09-30 18:00 [macd_momentum_regimen] CIERRE XLM momentum perdido bruto -0.25% neto -0.75%
- 2026-09-30 18:00 [macd_momentum_evento] CIERRE XLM momentum perdido bruto -0.25% neto -1.35%
- 2026-09-30 17:55 [estocastico_rebote] ENTRADA DOGE @ 0.0831768 (22.87 €, apertura)
- 2026-09-30 17:55 [estocastico_rebote] ENTRADA ONDO @ 0.44495 (22.87 €, apertura)
- 2026-09-30 17:55 [estocastico_rebote] ENTRADA WLD @ 0.4701 (22.87 €, apertura)
- 2026-09-30 18:00 [pullback_tendencia] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 17:55 [macd_momentum] ENTRADA MON @ 0.02548 (22.78 €, apertura)
- 2026-09-30 17:55 [macd_sin_salida] ENTRADA MON @ 0.02548 (22.68 €, apertura)
- 2026-09-30 17:55 [macd_momentum_evento] ENTRADA MON @ 0.02548 (22.99 €, apertura)
- 2026-09-30 17:55 [macd_momentum] ENTRADA TON @ 1.339 (22.78 €, apertura)
- 2026-09-30 17:55 [macd_momentum_evento] ENTRADA TON @ 1.339 (22.99 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
