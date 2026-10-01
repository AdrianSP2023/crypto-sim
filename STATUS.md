# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 23:16 UTC · vueltas 340 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 883.98 € (-4.36%) | 261 | 27 | 34% | -0.052% | -0.652% | -0.773% | -38.65 € |
| reversion_bb | 916.86 € (-0.80%) | 51 | 17 | 49% | +0.294% | -0.718% | -0.815% | -8.44 € |
| ruptura_volumen | 871.58 € (-5.70%) | 297 | 2 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.89 € (-3.82%) | 186 | 5 | 15% | -0.199% | -0.841% | -0.930% | -35.51 € |
| macd_momentum | 863.32 € (-6.59%) | 483 | 14 | 20% | -0.010% | -0.564% | -0.666% | -60.96 € |
| estocastico_rebote | 871.72 € (-5.68%) | 326 | 13 | 31% | -0.129% | -0.709% | -0.820% | -52.17 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 871.67 € (-5.69%) | 342 | 14 | 34% | -0.097% | -0.674% | -0.785% | -52.07 € |
| c_banda_atr_tope | 910.95 € (-1.44%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.64 € (-2.01%) | 101 | 2 | 27% | -0.042% | -0.803% | -0.920% | -18.58 € |
| c_banda_atr_regimen | 896.16 € (-3.04%) | 132 | 6 | 30% | -0.211% | -0.909% | -1.043% | -27.45 € |
| macd_momentum_regimen | 885.23 € (-4.22%) | 276 | 0 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 874.82 € (-5.35%) | 230 | 0 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 889.86 € (-3.72%) | 228 | 27 | 35% | -0.014% | -0.630% | -0.747% | -32.75 € |
| macd_momentum_evento | 868.10 € (-6.07%) | 436 | 14 | 19% | -0.014% | -0.574% | -0.673% | -56.18 € |
| ruptura_volumen_evento | 883.98 € (-4.36%) | 247 | 2 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 23:15 | macd_momentum_evento | UNI | momentum perdido | -1.01% | -1.51% | -0.33 |
| 2026-10-01 23:15 | macd_sin_salida | POL | timeout | -0.66% | -1.16% | -0.26 |
| 2026-10-01 23:15 | macd_momentum | UNI | momentum perdido | -1.01% | -1.51% | -0.33 |
| 2026-10-01 23:15 | pullback_tendencia | BTC | rotura de tendencia | -0.06% | -0.56% | -0.12 |
| 2026-10-01 23:10 | macd_momentum_evento | POL | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-10-01 23:10 | c_banda_atr_evento | LTC | timeout | +0.15% | -0.35% | -0.08 |
| 2026-10-01 23:10 | c_banda_atr_regimen | LTC | timeout | +0.15% | -0.35% | -0.08 |
| 2026-10-01 23:10 | ruptura_volumen_tope | TON | timeout | +0.07% | -0.43% | -0.10 |
| 2026-10-01 23:10 | macd_sin_salida | APT | timeout | -1.06% | -1.56% | -0.34 |
| 2026-10-01 23:10 | macd_sin_salida | BNB | timeout | +0.15% | -0.35% | -0.08 |
| 2026-10-01 23:10 | macd_sin_salida | XLM | timeout | -0.52% | -1.02% | -0.23 |
| 2026-10-01 23:10 | macd_sin_salida | SOL | timeout | -0.19% | -0.69% | -0.15 |
| 2026-10-01 23:10 | macd_sin_salida | ETH | timeout | -0.08% | -0.58% | -0.13 |
| 2026-10-01 23:10 | estocastico_rebote | ZRO | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-01 23:10 | macd_momentum | POL | momentum perdido | -0.27% | -0.77% | -0.17 |

## Eventos de la última vuelta

- 2026-10-01 23:15 [pullback_tendencia] CIERRE BTC rotura de tendencia bruto -0.06% neto -0.56%
- 2026-10-01 23:15 [macd_momentum] CIERRE UNI momentum perdido bruto -1.01% neto -1.51%
- 2026-10-01 23:15 [macd_momentum_evento] CIERRE UNI momentum perdido bruto -1.01% neto -1.51%
- 2026-10-01 23:15 [macd_sin_salida] CIERRE POL timeout bruto -0.66% neto -1.16%
- 2026-10-01 23:10 [macd_momentum] ENTRADA NIGHT @ 0.03467 (21.58 €, apertura)
- 2026-10-01 23:10 [macd_sin_salida] ENTRADA NIGHT @ 0.03467 (21.80 €, apertura)
- 2026-10-01 23:10 [macd_momentum_evento] ENTRADA NIGHT @ 0.03467 (21.70 €, apertura)
- 2026-10-01 23:10 [estocastico_rebote] ENTRADA SHIB @ 5.127e-06 (21.80 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
