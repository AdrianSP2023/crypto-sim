# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 23:31 UTC · vueltas 343 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.60 € (-4.29%) | 261 | 28 | 34% | -0.052% | -0.652% | -0.773% | -38.65 € |
| reversion_bb | 917.44 € (-0.74%) | 51 | 17 | 49% | +0.294% | -0.718% | -0.815% | -8.44 € |
| ruptura_volumen | 871.61 € (-5.69%) | 297 | 2 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.27 € (-3.78%) | 186 | 5 | 15% | -0.199% | -0.841% | -0.930% | -35.51 € |
| macd_momentum | 863.30 € (-6.59%) | 486 | 11 | 20% | -0.011% | -0.565% | -0.668% | -61.49 € |
| estocastico_rebote | 872.23 € (-5.63%) | 326 | 14 | 31% | -0.129% | -0.709% | -0.820% | -52.17 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 871.82 € (-5.67%) | 345 | 11 | 34% | -0.098% | -0.674% | -0.785% | -52.54 € |
| c_banda_atr_tope | 911.00 € (-1.43%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.67 € (-2.01%) | 101 | 2 | 27% | -0.042% | -0.803% | -0.920% | -18.58 € |
| c_banda_atr_regimen | 896.25 € (-3.03%) | 132 | 6 | 30% | -0.211% | -0.909% | -1.043% | -27.45 € |
| macd_momentum_regimen | 885.23 € (-4.22%) | 276 | 0 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 874.82 € (-5.35%) | 230 | 0 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 890.48 € (-3.65%) | 228 | 28 | 35% | -0.014% | -0.630% | -0.747% | -32.75 € |
| macd_momentum_evento | 868.08 € (-6.08%) | 439 | 11 | 19% | -0.016% | -0.576% | -0.675% | -56.72 € |
| ruptura_volumen_evento | 884.01 € (-4.35%) | 247 | 2 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-01 23:15 | pullback_tendencia | BTC | rotura de tendencia | -0.06% | -0.56% | -0.12 |
| 2026-10-01 23:10 | macd_momentum_evento | POL | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-10-01 23:10 | c_banda_atr_evento | LTC | timeout | +0.15% | -0.35% | -0.08 |

## Eventos de la última vuelta

- 2026-10-01 23:25 [estocastico_rebote] ENTRADA SUI @ 1.0417 (21.80 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
