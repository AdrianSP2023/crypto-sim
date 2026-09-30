# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 17:56 UTC · vueltas 68 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.74 € (-1.46%) | 41 | 10 | 32% | -0.270% | -1.340% | -1.501% | -12.68 € |
| reversion_bb | 923.51 € (-0.08%) | 4 | 3 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 899.75 € (-2.65%) | 67 | 6 | 13% | -0.709% | -1.598% | -1.738% | -24.57 € |
| rebote_extremo | 923.90 € (-0.04%) | 2 | 0 | 50% | +0.370% | -0.731% | -0.816% | -0.34 € |
| pullback_tendencia | 907.76 € (-1.78%) | 49 | 5 | 14% | -0.460% | -1.493% | -1.620% | -16.80 € |
| macd_momentum | 911.21 € (-1.41%) | 66 | 3 | 32% | +0.045% | -0.851% | -0.999% | -12.95 € |
| estocastico_rebote | 913.43 € (-1.17%) | 74 | 26 | 47% | +0.293% | -0.560% | -0.707% | -9.62 € |
| ruptura_estricta | 900.47 € (-2.57%) | 43 | 3 | 9% | -1.345% | -2.438% | -2.586% | -24.15 € |
| macd_sin_salida | 907.04 € (-1.86%) | 61 | 5 | 33% | -0.285% | -1.212% | -1.357% | -17.06 € |
| c_banda_atr_tope | 922.26 € (-0.21%) | 10 | 5 | 50% | +0.251% | -0.849% | -1.020% | -1.96 € |
| ruptura_volumen_tope | 918.87 € (-0.58%) | 16 | 1 | 19% | -0.453% | -1.553% | -1.655% | -5.74 € |
| c_banda_atr_regimen | 910.66 € (-1.47%) | 38 | 7 | 29% | -0.357% | -1.457% | -1.613% | -12.78 € |
| macd_momentum_regimen | 911.75 € (-1.35%) | 57 | 3 | 32% | +0.014% | -0.944% | -1.091% | -12.41 € |
| ruptura_volumen_regimen | 899.22 € (-2.71%) | 67 | 5 | 13% | -0.721% | -1.610% | -1.751% | -24.75 € |
| c_banda_atr_evento | 921.02 € (-0.35%) | 8 | 11 | 38% | -0.201% | -1.301% | -1.463% | -2.41 € |
| macd_momentum_evento | 919.71 € (-0.49%) | 19 | 3 | 32% | +0.085% | -1.015% | -1.188% | -4.45 € |
| ruptura_volumen_evento | 916.28 € (-0.86%) | 17 | 6 | 6% | -0.950% | -2.050% | -2.160% | -8.05 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-30 17:45 | macd_sin_salida | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 17:45 | estocastico_rebote | AAVE | timeout | +0.57% | +0.07% | +0.02 |
| 2026-09-30 17:45 | estocastico_rebote | ETH | timeout | +0.38% | -0.12% | -0.03 |
| 2026-09-30 17:45 | macd_momentum | TON | momentum perdido | +0.07% | -0.42% | -0.10 |

## Eventos de la última vuelta

- 2026-09-30 17:50 [estocastico_rebote] ENTRADA BTC @ 74153 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA ETH @ 2366.22 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA SOL @ 105.22 (22.87 €, apertura)
- 2026-09-30 17:50 [pullback_tendencia] ENTRADA QNT @ 265.72 (22.69 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA NEAR @ 4.7664 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA ADA @ 0.217836 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA SUI @ 1.0404 (22.87 €, apertura)
- 2026-09-30 17:50 [macd_momentum] ENTRADA AVAX @ 9.723 (22.78 €, apertura)
- 2026-09-30 17:50 [macd_sin_salida] ENTRADA AVAX @ 9.723 (22.69 €, apertura)
- 2026-09-30 17:50 [macd_momentum_regimen] ENTRADA AVAX @ 9.723 (22.80 €, apertura)
- 2026-09-30 17:50 [macd_momentum_evento] ENTRADA AVAX @ 9.723 (22.99 €, apertura)
- 2026-09-30 17:50 [macd_momentum] ENTRADA XLM @ 0.199008 (22.78 €, apertura)
- 2026-09-30 17:50 [macd_sin_salida] ENTRADA XLM @ 0.199008 (22.69 €, apertura)
- 2026-09-30 17:50 [macd_momentum_regimen] ENTRADA XLM @ 0.199008 (22.80 €, apertura)
- 2026-09-30 17:50 [macd_momentum_evento] ENTRADA XLM @ 0.199008 (22.99 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA TAO @ 269.329 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA UNI @ 7.8339 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA DOT @ 1.0968 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA ARB @ 0.1807 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA ENA @ 0.2367 (22.87 €, apertura)
- 2026-09-30 17:55 [macd_sin_salida] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:55 [ruptura_estricta] CIERRE KSM stop-loss bruto -2.16% neto -2.96%
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA BNB @ 677.87 (22.87 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
