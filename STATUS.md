# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 17:36 UTC · vueltas 64 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 911.88 € (-1.34%) | 39 | 12 | 33% | -0.204% | -1.288% | -1.449% | -11.61 € |
| reversion_bb | 923.89 € (-0.04%) | 4 | 2 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 900.51 € (-2.57%) | 63 | 9 | 14% | -0.689% | -1.603% | -1.747% | -23.19 € |
| rebote_extremo | 923.90 € (-0.04%) | 2 | 0 | 50% | +0.370% | -0.731% | -0.816% | -0.34 € |
| pullback_tendencia | 909.03 € (-1.65%) | 43 | 8 | 16% | -0.440% | -1.519% | -1.643% | -15.01 € |
| macd_momentum | 911.55 € (-1.37%) | 63 | 3 | 32% | +0.039% | -0.875% | -1.017% | -12.72 € |
| estocastico_rebote | 915.85 € (-0.91%) | 68 | 13 | 50% | +0.288% | -0.582% | -0.739% | -9.20 € |
| ruptura_estricta | 900.55 € (-2.56%) | 42 | 3 | 10% | -1.325% | -2.425% | -2.569% | -23.48 € |
| macd_sin_salida | 907.75 € (-1.78%) | 57 | 6 | 33% | -0.259% | -1.217% | -1.359% | -16.02 € |
| c_banda_atr_tope | 922.97 € (-0.14%) | 10 | 5 | 50% | +0.251% | -0.849% | -1.020% | -1.96 € |
| ruptura_volumen_tope | 919.34 € (-0.53%) | 14 | 2 | 21% | -0.404% | -1.504% | -1.600% | -4.86 € |
| c_banda_atr_regimen | 911.57 € (-1.37%) | 36 | 9 | 31% | -0.290% | -1.390% | -1.546% | -11.56 € |
| macd_momentum_regimen | 911.91 € (-1.33%) | 55 | 2 | 31% | +0.007% | -0.967% | -1.108% | -12.28 € |
| ruptura_volumen_regimen | 900.16 € (-2.61%) | 64 | 8 | 14% | -0.697% | -1.605% | -1.748% | -23.58 € |
| c_banda_atr_evento | 922.58 € (-0.18%) | 6 | 13 | 50% | +0.250% | -0.850% | -1.016% | -1.18 € |
| macd_momentum_evento | 920.47 € (-0.41%) | 16 | 3 | 31% | +0.071% | -1.029% | -1.181% | -3.80 € |
| ruptura_volumen_evento | 917.60 € (-0.72%) | 13 | 9 | 8% | -0.927% | -2.027% | -2.148% | -6.08 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 17:35 | ruptura_volumen_evento | SPX | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:35 | ruptura_volumen_evento | SEI | stop-loss | -1.25% | -2.35% | -0.54 |
| 2026-09-30 17:35 | ruptura_volumen_evento | PENGU | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:35 | ruptura_volumen_evento | UNI | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:35 | ruptura_volumen_evento | HYPE | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:35 | ruptura_volumen_regimen | SPX | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 17:35 | ruptura_volumen_regimen | SEI | stop-loss | -1.25% | -1.75% | -0.40 |
| 2026-09-30 17:35 | ruptura_volumen_regimen | PENGU | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 17:35 | ruptura_volumen_regimen | UNI | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 17:35 | ruptura_volumen_regimen | HYPE | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 17:35 | ruptura_volumen_tope | SPX | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:35 | ruptura_volumen_tope | UNI | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:35 | estocastico_rebote | DOGE | timeout | +0.12% | -0.68% | -0.16 |
| 2026-09-30 17:35 | pullback_tendencia | SPX | rotura de tendencia | -1.32% | -2.12% | -0.48 |
| 2026-09-30 17:35 | ruptura_volumen | SPX | stop-loss | -1.20% | -1.70% | -0.39 |

## Eventos de la última vuelta

- 2026-09-30 17:35 [ruptura_volumen] CIERRE HYPE stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_regimen] CIERRE HYPE stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_evento] CIERRE HYPE stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:35 [ruptura_volumen] CIERRE UNI stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_tope] CIERRE UNI stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:35 [ruptura_volumen_regimen] CIERRE UNI stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_evento] CIERRE UNI stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:35 [estocastico_rebote] CIERRE DOGE timeout bruto +0.12% neto -0.68%
- 2026-09-30 17:30 [pullback_tendencia] ENTRADA DOT @ 1.0979 (22.74 €, apertura)
- 2026-09-30 17:30 [c_banda_atr] ENTRADA XDC @ 0.03028 (22.82 €, apertura)
- 2026-09-30 17:30 [c_banda_atr_tope] ENTRADA XDC @ 0.03028 (23.06 €, apertura)
- 2026-09-30 17:30 [c_banda_atr_regimen] ENTRADA XDC @ 0.03028 (22.82 €, apertura)
- 2026-09-30 17:30 [c_banda_atr_evento] ENTRADA XDC @ 0.03028 (23.08 €, apertura)
- 2026-09-30 17:30 [estocastico_rebote] ENTRADA RENDER @ 1.709 (22.88 €, apertura)
- 2026-09-30 17:35 [ruptura_volumen] CIERRE PENGU stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_regimen] CIERRE PENGU stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_evento] CIERRE PENGU stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:30 [reversion_bb] ENTRADA TRUMP @ 1.808 (23.10 €, apertura)
- 2026-09-30 17:35 [ruptura_volumen] CIERRE SEI stop-loss bruto -1.25% neto -1.75%
- 2026-09-30 17:35 [ruptura_volumen_regimen] CIERRE SEI stop-loss bruto -1.25% neto -1.75%
- 2026-09-30 17:35 [ruptura_volumen_evento] CIERRE SEI stop-loss bruto -1.25% neto -2.35%
- 2026-09-30 17:35 [ruptura_volumen] CIERRE SPX stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [pullback_tendencia] CIERRE SPX rotura de tendencia bruto -1.32% neto -2.12%
- 2026-09-30 17:35 [ruptura_volumen_tope] CIERRE SPX stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:35 [ruptura_volumen_regimen] CIERRE SPX stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_evento] CIERRE SPX stop-loss bruto -1.20% neto -2.30%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
