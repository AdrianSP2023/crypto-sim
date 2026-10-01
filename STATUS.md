# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 23:41 UTC · vueltas 345 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.49 € (-4.19%) | 261 | 29 | 34% | -0.052% | -0.652% | -0.773% | -38.65 € |
| reversion_bb | 917.85 € (-0.69%) | 51 | 17 | 49% | +0.294% | -0.718% | -0.815% | -8.44 € |
| ruptura_volumen | 871.63 € (-5.69%) | 297 | 3 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.15 € (-3.80%) | 187 | 5 | 15% | -0.194% | -0.836% | -0.925% | -35.47 € |
| macd_momentum | 863.58 € (-6.56%) | 486 | 12 | 20% | -0.011% | -0.565% | -0.668% | -61.49 € |
| estocastico_rebote | 872.39 € (-5.61%) | 327 | 14 | 31% | -0.130% | -0.709% | -0.819% | -52.33 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 871.67 € (-5.69%) | 346 | 10 | 34% | -0.099% | -0.674% | -0.785% | -52.70 € |
| c_banda_atr_tope | 911.14 € (-1.42%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.70 € (-2.01%) | 101 | 3 | 27% | -0.042% | -0.803% | -0.920% | -18.58 € |
| c_banda_atr_regimen | 896.52 € (-3.00%) | 132 | 6 | 30% | -0.211% | -0.909% | -1.043% | -27.45 € |
| macd_momentum_regimen | 885.23 € (-4.22%) | 276 | 0 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 874.82 € (-5.35%) | 230 | 0 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 891.38 € (-3.55%) | 228 | 29 | 35% | -0.014% | -0.630% | -0.747% | -32.75 € |
| macd_momentum_evento | 868.36 € (-6.05%) | 439 | 12 | 19% | -0.016% | -0.576% | -0.675% | -56.72 € |
| ruptura_volumen_evento | 884.04 € (-4.35%) | 247 | 3 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 23:40 | estocastico_rebote | TRX | timeout | -0.23% | -0.73% | -0.16 |
| 2026-10-01 23:40 | pullback_tendencia | SKY | timeout | +0.65% | +0.15% | +0.03 |
| 2026-10-01 23:35 | macd_sin_salida | FET | timeout | -0.24% | -0.74% | -0.16 |
| 2026-10-01 23:25 | macd_momentum_evento | BCH | momentum perdido | -0.12% | -0.62% | -0.14 |
| 2026-10-01 23:25 | macd_momentum_evento | NIGHT | momentum perdido | -0.38% | -0.88% | -0.19 |
| 2026-10-01 23:25 | macd_sin_salida | BTC | timeout | -0.08% | -0.58% | -0.13 |
| 2026-10-01 23:25 | macd_momentum | BCH | momentum perdido | -0.12% | -0.62% | -0.13 |
| 2026-10-01 23:25 | macd_momentum | NIGHT | momentum perdido | -0.38% | -0.88% | -0.19 |
| 2026-10-01 23:20 | macd_momentum_evento | TRUMP | momentum perdido | -0.49% | -0.99% | -0.21 |
| 2026-10-01 23:20 | macd_sin_salida | XMR | timeout | +0.06% | -0.44% | -0.10 |
| 2026-10-01 23:20 | macd_sin_salida | ICP | timeout | -0.58% | -1.08% | -0.24 |
| 2026-10-01 23:20 | macd_momentum | TRUMP | momentum perdido | -0.49% | -0.99% | -0.21 |
| 2026-10-01 23:15 | macd_momentum_evento | UNI | momentum perdido | -1.01% | -1.51% | -0.33 |
| 2026-10-01 23:15 | macd_sin_salida | POL | timeout | -0.66% | -1.16% | -0.26 |
| 2026-10-01 23:15 | macd_momentum | UNI | momentum perdido | -1.01% | -1.51% | -0.33 |

## Eventos de la última vuelta

- 2026-10-01 23:35 [pullback_tendencia] ENTRADA BTC @ 75390.8 (22.22 €, apertura)
- 2026-10-01 23:35 [ruptura_volumen] ENTRADA LINK @ 12.7622 (21.79 €, apertura)
- 2026-10-01 23:35 [ruptura_volumen_tope] ENTRADA LINK @ 12.7622 (22.64 €, apertura)
- 2026-10-01 23:35 [ruptura_volumen_evento] ENTRADA LINK @ 12.7622 (22.10 €, apertura)
- 2026-10-01 23:40 [estocastico_rebote] CIERRE TRX timeout bruto -0.23% neto -0.73%
- 2026-10-01 23:40 [pullback_tendencia] CIERRE SKY timeout bruto +0.65% neto +0.15%
- 2026-10-01 23:35 [macd_momentum] ENTRADA SKY @ 0.07458 (21.57 €, apertura)
- 2026-10-01 23:35 [macd_momentum_evento] ENTRADA SKY @ 0.07458 (21.69 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
