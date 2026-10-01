# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 12:26 UTC · vueltas 216 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.05 € (-2.94%) | 180 | 25 | 36% | -0.022% | -0.667% | -0.791% | -27.46 € |
| reversion_bb | 919.11 € (-0.56%) | 27 | 6 | 44% | +0.214% | -0.886% | -0.990% | -5.52 € |
| ruptura_volumen | 884.71 € (-4.28%) | 218 | 12 | 23% | -0.187% | -0.807% | -0.917% | -39.97 € |
| rebote_extremo | 922.08 € (-0.23%) | 9 | 0 | 44% | +0.060% | -1.040% | -1.178% | -2.16 € |
| pullback_tendencia | 895.67 € (-3.09%) | 129 | 4 | 15% | -0.269% | -0.974% | -1.081% | -28.63 € |
| macd_momentum | 883.56 € (-4.40%) | 313 | 13 | 21% | -0.006% | -0.589% | -0.699% | -41.77 € |
| estocastico_rebote | 880.27 € (-4.76%) | 260 | 7 | 31% | -0.154% | -0.754% | -0.866% | -44.45 € |
| ruptura_estricta | 889.34 € (-3.78%) | 125 | 10 | 25% | -0.501% | -1.212% | -1.337% | -34.64 € |
| macd_sin_salida | 889.50 € (-3.76%) | 225 | 20 | 36% | -0.083% | -0.699% | -0.814% | -35.90 € |
| c_banda_atr_tope | 913.72 € (-1.14%) | 42 | 5 | 29% | -0.003% | -1.103% | -1.222% | -10.66 € |
| ruptura_volumen_tope | 911.64 € (-1.36%) | 66 | 5 | 29% | +0.072% | -0.828% | -0.943% | -12.56 € |
| c_banda_atr_regimen | 902.47 € (-2.36%) | 109 | 1 | 34% | -0.130% | -0.870% | -1.010% | -21.77 € |
| macd_momentum_regimen | 894.23 € (-3.25%) | 203 | 3 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 885.66 € (-4.17%) | 179 | 6 | 20% | -0.303% | -0.949% | -1.063% | -38.61 € |
| c_banda_atr_evento | 903.02 € (-2.30%) | 147 | 25 | 37% | +0.043% | -0.637% | -0.753% | -21.49 € |
| macd_momentum_evento | 888.46 € (-3.87%) | 266 | 13 | 19% | -0.012% | -0.611% | -0.716% | -36.88 € |
| ruptura_volumen_evento | 897.30 € (-2.92%) | 168 | 12 | 24% | -0.057% | -0.714% | -0.812% | -27.38 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 12:25 | c_banda_atr_evento | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 12:25 | estocastico_rebote | NIGHT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 12:25 | pullback_tendencia | NIGHT | rotura de tendencia | -1.06% | -1.56% | -0.35 |
| 2026-10-01 12:25 | pullback_tendencia | FET | rotura de tendencia | -0.05% | -0.55% | -0.12 |
| 2026-10-01 12:25 | c_banda_atr | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 12:20 | ruptura_volumen_evento | FET | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-10-01 12:20 | macd_momentum_evento | SKY | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-10-01 12:20 | macd_momentum_evento | TON | momentum perdido | -0.37% | -0.87% | -0.19 |
| 2026-10-01 12:20 | ruptura_volumen_regimen | FET | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-10-01 12:20 | macd_momentum | SKY | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-10-01 12:20 | macd_momentum | TON | momentum perdido | -0.37% | -0.87% | -0.19 |
| 2026-10-01 12:20 | ruptura_volumen | FET | stop-loss | -1.33% | -1.83% | -0.40 |
| 2026-10-01 12:15 | macd_momentum_evento | RENDER | momentum perdido | +0.18% | -0.32% | -0.07 |
| 2026-10-01 12:15 | c_banda_atr_evento | SUI | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 12:15 | ruptura_volumen_regimen | KSM | stop-loss | -1.92% | -2.42% | -0.54 |

## Eventos de la última vuelta

- 2026-10-01 12:20 [pullback_tendencia] ENTRADA UNI @ 7.9956 (22.40 €, apertura)
- 2026-10-01 12:20 [pullback_tendencia] ENTRADA FET @ 0.2077 (22.40 €, apertura)
- 2026-10-01 12:25 [pullback_tendencia] CIERRE FET rotura de tendencia bruto -0.05% neto -0.55%
- 2026-10-01 12:25 [c_banda_atr] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 12:20 [pullback_tendencia] ENTRADA NIGHT @ 0.0387 (22.40 €, apertura)
- 2026-10-01 12:25 [pullback_tendencia] CIERRE NIGHT rotura de tendencia bruto -1.06% neto -1.56%
- 2026-10-01 12:25 [estocastico_rebote] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 12:25 [c_banda_atr_evento] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 12:20 [pullback_tendencia] ENTRADA RENDER @ 1.702 (22.39 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
