# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 06:16 UTC · vueltas 222 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 895.66 € (-3.09%) | 126 | 27 | 28% | -0.230% | -0.937% | -1.072% | -27.03 € |
| reversion_bb | 916.35 € (-0.85%) | 35 | 6 | 46% | +0.183% | -0.917% | -1.027% | -7.39 € |
| ruptura_volumen | 889.56 € (-3.75%) | 159 | 17 | 19% | -0.270% | -0.934% | -1.061% | -33.79 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 903.92 € (-2.20%) | 115 | 3 | 25% | -0.046% | -0.773% | -0.899% | -20.35 € |
| macd_momentum | 875.80 € (-5.24%) | 311 | 10 | 16% | -0.101% | -0.685% | -0.796% | -48.13 € |
| estocastico_rebote | 889.22 € (-3.79%) | 207 | 8 | 35% | -0.097% | -0.723% | -0.856% | -34.16 € |
| ruptura_estricta | 903.53 € (-2.24%) | 70 | 10 | 23% | -0.383% | -1.256% | -1.396% | -20.15 € |
| macd_sin_salida | 890.68 € (-3.63%) | 180 | 28 | 29% | -0.135% | -0.780% | -0.907% | -31.97 € |
| c_banda_atr_tope | 910.12 € (-1.53%) | 38 | 3 | 18% | -0.461% | -1.561% | -1.694% | -13.63 € |
| ruptura_volumen_tope | 909.10 € (-1.64%) | 60 | 2 | 17% | -0.164% | -1.104% | -1.225% | -15.20 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.57 € (-4.18%) | 200 | 2 | 14% | -0.215% | -0.846% | -0.960% | -38.41 € |
| ruptura_volumen_regimen | 897.11 € (-2.94%) | 118 | 8 | 18% | -0.255% | -0.976% | -1.105% | -26.29 € |
| c_banda_atr_evento | 898.72 € (-2.76%) | 94 | 27 | 24% | -0.332% | -1.113% | -1.250% | -23.97 € |
| macd_momentum_evento | 888.12 € (-3.91%) | 191 | 10 | 13% | -0.186% | -0.825% | -0.933% | -35.80 € |
| ruptura_volumen_evento | 895.04 € (-3.16%) | 100 | 17 | 11% | -0.475% | -1.239% | -1.367% | -28.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 06:15 | ruptura_volumen_evento | KAS | timeout | +0.21% | -0.29% | -0.07 |
| 2026-09-30 06:15 | ruptura_volumen_evento | ASTER | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 06:15 | macd_momentum_evento | SHIB | momentum perdido | -0.41% | -0.91% | -0.20 |
| 2026-09-30 06:15 | macd_momentum_evento | NEAR | momentum perdido | -1.24% | -1.74% | -0.39 |
| 2026-09-30 06:15 | macd_momentum_evento | SOL | momentum perdido | -0.76% | -1.26% | -0.28 |
| 2026-09-30 06:15 | ruptura_volumen_regimen | ASTER | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 06:15 | ruptura_volumen_tope | KAS | timeout | +0.21% | -0.29% | -0.07 |
| 2026-09-30 06:15 | ruptura_volumen_tope | ASTER | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 06:15 | macd_momentum | SHIB | momentum perdido | -0.41% | -0.91% | -0.20 |
| 2026-09-30 06:15 | macd_momentum | NEAR | momentum perdido | -1.24% | -1.74% | -0.38 |
| 2026-09-30 06:15 | macd_momentum | SOL | momentum perdido | -0.76% | -1.26% | -0.28 |
| 2026-09-30 06:15 | pullback_tendencia | INJ | rotura de tendencia | -0.88% | -1.38% | -0.31 |
| 2026-09-30 06:15 | ruptura_volumen | KAS | timeout | +0.21% | -0.29% | -0.07 |
| 2026-09-30 06:15 | ruptura_volumen | ASTER | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 06:15 | reversion_bb | NIGHT | stop-loss | -1.59% | -2.69% | -0.62 |

## Eventos de la última vuelta

- 2026-09-30 06:15 [macd_momentum] CIERRE SOL momentum perdido bruto -0.76% neto -1.26%
- 2026-09-30 06:15 [macd_momentum_evento] CIERRE SOL momentum perdido bruto -0.76% neto -1.26%
- 2026-09-30 06:15 [macd_momentum] CIERRE NEAR momentum perdido bruto -1.24% neto -1.74%
- 2026-09-30 06:15 [macd_momentum_evento] CIERRE NEAR momentum perdido bruto -1.24% neto -1.74%
- 2026-09-30 06:10 [reversion_bb] ENTRADA JUP @ 0.28645 (22.94 €, apertura)
- 2026-09-30 06:15 [pullback_tendencia] CIERRE INJ rotura de tendencia bruto -0.88% neto -1.38%
- 2026-09-30 06:15 [reversion_bb] CIERRE NIGHT stop-loss bruto -1.59% neto -2.69%
- 2026-09-30 06:15 [macd_momentum] CIERRE SHIB momentum perdido bruto -0.41% neto -0.91%
- 2026-09-30 06:15 [macd_momentum_evento] CIERRE SHIB momentum perdido bruto -0.41% neto -0.91%
- 2026-09-30 06:15 [ruptura_volumen] CIERRE ASTER stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 06:15 [ruptura_volumen_tope] CIERRE ASTER stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 06:15 [ruptura_volumen_regimen] CIERRE ASTER stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 06:15 [ruptura_volumen_evento] CIERRE ASTER stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 06:15 [ruptura_volumen] CIERRE KAS timeout bruto +0.21% neto -0.29%
- 2026-09-30 06:15 [ruptura_volumen_tope] CIERRE KAS timeout bruto +0.21% neto -0.29%
- 2026-09-30 06:15 [ruptura_volumen_evento] CIERRE KAS timeout bruto +0.21% neto -0.29%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
