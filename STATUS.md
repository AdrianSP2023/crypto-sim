# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 12:41 UTC · vueltas 219 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.75 € (-2.87%) | 181 | 25 | 36% | -0.010% | -0.655% | -0.779% | -27.12 € |
| reversion_bb | 919.00 € (-0.57%) | 27 | 6 | 44% | +0.214% | -0.886% | -0.990% | -5.52 € |
| ruptura_volumen | 884.68 € (-4.28%) | 218 | 15 | 23% | -0.187% | -0.807% | -0.917% | -39.97 € |
| rebote_extremo | 922.08 € (-0.23%) | 9 | 0 | 44% | +0.060% | -1.040% | -1.178% | -2.16 € |
| pullback_tendencia | 895.67 € (-3.09%) | 129 | 6 | 15% | -0.269% | -0.974% | -1.081% | -28.63 € |
| macd_momentum | 883.28 € (-4.43%) | 316 | 11 | 21% | -0.006% | -0.588% | -0.698% | -42.09 € |
| estocastico_rebote | 880.30 € (-4.75%) | 261 | 7 | 31% | -0.158% | -0.758% | -0.869% | -44.83 € |
| ruptura_estricta | 889.06 € (-3.81%) | 126 | 9 | 25% | -0.515% | -1.224% | -1.349% | -35.24 € |
| macd_sin_salida | 889.33 € (-3.78%) | 226 | 19 | 36% | -0.089% | -0.704% | -0.819% | -36.34 € |
| c_banda_atr_tope | 913.69 € (-1.14%) | 42 | 5 | 29% | -0.003% | -1.103% | -1.222% | -10.66 € |
| ruptura_volumen_tope | 911.73 € (-1.35%) | 66 | 5 | 29% | +0.072% | -0.828% | -0.943% | -12.56 € |
| c_banda_atr_regimen | 902.41 € (-2.36%) | 109 | 1 | 34% | -0.130% | -0.870% | -1.010% | -21.77 € |
| macd_momentum_regimen | 894.41 € (-3.23%) | 203 | 3 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 885.49 € (-4.19%) | 179 | 6 | 20% | -0.303% | -0.949% | -1.063% | -38.61 € |
| c_banda_atr_evento | 903.73 € (-2.22%) | 148 | 25 | 37% | +0.056% | -0.622% | -0.739% | -21.15 € |
| macd_momentum_evento | 888.18 € (-3.90%) | 269 | 11 | 19% | -0.012% | -0.610% | -0.714% | -37.20 € |
| ruptura_volumen_evento | 897.26 € (-2.92%) | 168 | 15 | 24% | -0.057% | -0.714% | -0.812% | -27.38 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 12:40 | macd_momentum_evento | XRP | momentum perdido | +0.08% | -0.42% | -0.09 |
| 2026-10-01 12:40 | macd_momentum | XRP | momentum perdido | +0.08% | -0.42% | -0.09 |
| 2026-10-01 12:35 | macd_momentum_evento | JUP | momentum perdido | -0.45% | -0.95% | -0.21 |
| 2026-10-01 12:35 | ruptura_estricta | FET | stop-loss | -2.23% | -2.73% | -0.61 |
| 2026-10-01 12:35 | macd_momentum | JUP | momentum perdido | -0.45% | -0.95% | -0.21 |
| 2026-10-01 12:30 | macd_momentum_evento | BCH | momentum perdido | +0.40% | -0.10% | -0.02 |
| 2026-10-01 12:30 | c_banda_atr_evento | ENA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 12:30 | macd_sin_salida | PENGU | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 12:30 | estocastico_rebote | TRX | timeout | -1.21% | -1.71% | -0.38 |
| 2026-10-01 12:30 | macd_momentum | BCH | momentum perdido | +0.40% | -0.10% | -0.02 |
| 2026-10-01 12:30 | c_banda_atr | ENA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 12:25 | c_banda_atr_evento | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 12:25 | estocastico_rebote | NIGHT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 12:25 | pullback_tendencia | NIGHT | rotura de tendencia | -1.06% | -1.56% | -0.35 |
| 2026-10-01 12:25 | pullback_tendencia | FET | rotura de tendencia | -0.05% | -0.55% | -0.12 |

## Eventos de la última vuelta

- 2026-10-01 12:40 [macd_momentum] CIERRE XRP momentum perdido bruto +0.08% neto -0.42%
- 2026-10-01 12:40 [macd_momentum_evento] CIERRE XRP momentum perdido bruto +0.08% neto -0.42%
- 2026-10-01 12:35 [ruptura_volumen] ENTRADA LINK @ 12.7515 (22.11 €, apertura)
- 2026-10-01 12:35 [ruptura_volumen_evento] ENTRADA LINK @ 12.7515 (22.42 €, apertura)
- 2026-10-01 12:35 [pullback_tendencia] ENTRADA SUI @ 1.0314 (22.39 €, apertura)
- 2026-10-01 12:35 [pullback_tendencia] ENTRADA BCH @ 273.97 (22.39 €, apertura)
- 2026-10-01 12:35 [macd_momentum] ENTRADA RENDER @ 1.701 (22.05 €, apertura)
- 2026-10-01 12:35 [macd_momentum_evento] ENTRADA RENDER @ 1.701 (22.18 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
