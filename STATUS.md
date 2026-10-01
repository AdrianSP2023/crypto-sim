# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 12:31 UTC · vueltas 217 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.28 € (-2.92%) | 181 | 25 | 36% | -0.010% | -0.655% | -0.779% | -27.12 € |
| reversion_bb | 919.14 € (-0.55%) | 27 | 6 | 44% | +0.214% | -0.886% | -0.990% | -5.52 € |
| ruptura_volumen | 884.72 € (-4.28%) | 218 | 13 | 23% | -0.187% | -0.807% | -0.917% | -39.97 € |
| rebote_extremo | 922.08 € (-0.23%) | 9 | 0 | 44% | +0.060% | -1.040% | -1.178% | -2.16 € |
| pullback_tendencia | 895.75 € (-3.08%) | 129 | 4 | 15% | -0.269% | -0.974% | -1.081% | -28.63 € |
| macd_momentum | 883.52 € (-4.41%) | 314 | 12 | 21% | -0.005% | -0.588% | -0.697% | -41.79 € |
| estocastico_rebote | 880.22 € (-4.76%) | 261 | 6 | 31% | -0.158% | -0.758% | -0.869% | -44.83 € |
| ruptura_estricta | 889.32 € (-3.78%) | 125 | 10 | 25% | -0.501% | -1.212% | -1.337% | -34.64 € |
| macd_sin_salida | 889.23 € (-3.79%) | 226 | 19 | 36% | -0.089% | -0.704% | -0.819% | -36.34 € |
| c_banda_atr_tope | 913.82 € (-1.13%) | 42 | 5 | 29% | -0.003% | -1.103% | -1.222% | -10.66 € |
| ruptura_volumen_tope | 911.63 € (-1.36%) | 66 | 5 | 29% | +0.072% | -0.828% | -0.943% | -12.56 € |
| c_banda_atr_regimen | 902.41 € (-2.36%) | 109 | 1 | 34% | -0.130% | -0.870% | -1.010% | -21.77 € |
| macd_momentum_regimen | 894.34 € (-3.24%) | 203 | 3 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 885.76 € (-4.16%) | 179 | 6 | 20% | -0.303% | -0.949% | -1.063% | -38.61 € |
| c_banda_atr_evento | 903.25 € (-2.27%) | 148 | 25 | 37% | +0.056% | -0.622% | -0.739% | -21.15 € |
| macd_momentum_evento | 888.41 € (-3.88%) | 267 | 12 | 19% | -0.011% | -0.609% | -0.714% | -36.90 € |
| ruptura_volumen_evento | 897.31 € (-2.91%) | 168 | 13 | 24% | -0.057% | -0.714% | -0.812% | -27.38 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-01 12:25 | c_banda_atr | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 12:20 | ruptura_volumen_evento | FET | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-10-01 12:20 | macd_momentum_evento | SKY | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-10-01 12:20 | macd_momentum_evento | TON | momentum perdido | -0.37% | -0.87% | -0.19 |
| 2026-10-01 12:20 | ruptura_volumen_regimen | FET | stop-loss | -1.33% | -1.83% | -0.41 |

## Eventos de la última vuelta

- 2026-10-01 12:30 [c_banda_atr] CIERRE ENA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 12:30 [c_banda_atr_evento] CIERRE ENA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 12:30 [estocastico_rebote] CIERRE TRX timeout bruto -1.21% neto -1.71%
- 2026-10-01 12:30 [macd_momentum] CIERRE BCH momentum perdido bruto +0.40% neto -0.10%
- 2026-10-01 12:30 [macd_momentum_evento] CIERRE BCH momentum perdido bruto +0.40% neto -0.10%
- 2026-10-01 12:30 [macd_sin_salida] CIERRE PENGU stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 12:25 [c_banda_atr] ENTRADA SKY @ 0.07036 (22.43 €, apertura)
- 2026-10-01 12:25 [ruptura_volumen] ENTRADA SKY @ 0.07036 (22.11 €, apertura)
- 2026-10-01 12:25 [c_banda_atr_evento] ENTRADA SKY @ 0.07036 (22.58 €, apertura)
- 2026-10-01 12:25 [ruptura_volumen_evento] ENTRADA SKY @ 0.07036 (22.42 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
