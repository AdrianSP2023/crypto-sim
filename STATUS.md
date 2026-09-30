# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 05:51 UTC · vueltas 217 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.73 € (-2.65%) | 124 | 29 | 27% | -0.250% | -0.961% | -1.095% | -27.28 € |
| reversion_bb | 918.32 € (-0.64%) | 33 | 7 | 48% | +0.215% | -0.885% | -0.994% | -6.74 € |
| ruptura_volumen | 893.01 € (-3.38%) | 155 | 20 | 19% | -0.261% | -0.929% | -1.055% | -32.79 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.05 € (-2.08%) | 112 | 4 | 26% | -0.024% | -0.757% | -0.883% | -19.44 € |
| macd_momentum | 879.95 € (-4.79%) | 295 | 25 | 17% | -0.099% | -0.687% | -0.799% | -45.85 € |
| estocastico_rebote | 891.67 € (-3.52%) | 202 | 12 | 35% | -0.096% | -0.725% | -0.857% | -33.44 € |
| ruptura_estricta | 904.89 € (-2.09%) | 70 | 8 | 23% | -0.383% | -1.256% | -1.396% | -20.15 € |
| macd_sin_salida | 895.20 € (-3.14%) | 176 | 31 | 29% | -0.139% | -0.787% | -0.912% | -31.56 € |
| c_banda_atr_tope | 911.45 € (-1.38%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.05 € (-1.54%) | 57 | 5 | 18% | -0.161% | -1.124% | -1.243% | -14.70 € |
| c_banda_atr_regimen | 900.82 € (-2.53%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.66 € (-4.07%) | 197 | 4 | 15% | -0.206% | -0.839% | -0.952% | -37.55 € |
| ruptura_volumen_regimen | 899.04 € (-2.73%) | 116 | 8 | 18% | -0.234% | -0.959% | -1.087% | -25.40 € |
| c_banda_atr_evento | 902.80 € (-2.32%) | 92 | 29 | 24% | -0.362% | -1.149% | -1.285% | -24.22 € |
| macd_momentum_evento | 892.32 € (-3.45%) | 175 | 25 | 13% | -0.190% | -0.841% | -0.949% | -33.50 € |
| ruptura_volumen_evento | 898.51 € (-2.78%) | 96 | 20 | 11% | -0.470% | -1.245% | -1.370% | -27.29 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 05:50 | macd_momentum_evento | POL | momentum perdido | +0.24% | -0.26% | -0.06 |
| 2026-09-30 05:50 | macd_momentum_evento | DOT | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-09-30 05:50 | macd_momentum_evento | AVAX | momentum perdido | -0.06% | -0.56% | -0.12 |
| 2026-09-30 05:50 | macd_momentum_regimen | POL | momentum perdido | +0.24% | -0.26% | -0.06 |
| 2026-09-30 05:50 | macd_sin_salida | HBAR | timeout | +0.69% | +0.19% | +0.04 |
| 2026-09-30 05:50 | macd_momentum | POL | momentum perdido | +0.24% | -0.26% | -0.06 |
| 2026-09-30 05:50 | macd_momentum | DOT | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-09-30 05:50 | macd_momentum | AVAX | momentum perdido | -0.06% | -0.56% | -0.12 |
| 2026-09-30 05:45 | c_banda_atr_evento | BCH | timeout | +0.03% | -0.47% | -0.11 |
| 2026-09-30 05:45 | ruptura_volumen_tope | TON | timeout | +1.29% | +0.79% | +0.18 |
| 2026-09-30 05:45 | estocastico_rebote | SHIB | timeout | -0.16% | -0.66% | -0.15 |
| 2026-09-30 05:45 | estocastico_rebote | DASH | timeout | -0.40% | -0.90% | -0.20 |
| 2026-09-30 05:45 | reversion_bb | ENA | timeout | -0.46% | -1.56% | -0.36 |
| 2026-09-30 05:45 | c_banda_atr | BCH | timeout | +0.03% | -0.47% | -0.11 |
| 2026-09-30 05:40 | macd_momentum_evento | ASTER | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-09-30 05:50 [macd_sin_salida] CIERRE HBAR timeout bruto +0.69% neto +0.19%
- 2026-09-30 05:50 [macd_momentum] CIERRE AVAX momentum perdido bruto -0.06% neto -0.56%
- 2026-09-30 05:50 [macd_momentum_evento] CIERRE AVAX momentum perdido bruto -0.06% neto -0.56%
- 2026-09-30 05:45 [macd_momentum] ENTRADA TAO @ 269.497 (21.96 €, apertura)
- 2026-09-30 05:45 [macd_momentum_regimen] ENTRADA TAO @ 269.497 (22.17 €, apertura)
- 2026-09-30 05:45 [macd_momentum_evento] ENTRADA TAO @ 269.497 (22.27 €, apertura)
- 2026-09-30 05:50 [macd_momentum] CIERRE DOT momentum perdido bruto -0.13% neto -0.63%
- 2026-09-30 05:50 [macd_momentum_evento] CIERRE DOT momentum perdido bruto -0.13% neto -0.63%
- 2026-09-30 05:45 [ruptura_volumen] ENTRADA CRV @ 0.3475 (22.29 €, apertura)
- 2026-09-30 05:45 [ruptura_volumen_regimen] ENTRADA CRV @ 0.3475 (22.47 €, apertura)
- 2026-09-30 05:45 [ruptura_volumen_evento] ENTRADA CRV @ 0.3475 (22.42 €, apertura)
- 2026-09-30 05:45 [ruptura_volumen_regimen] ENTRADA TRX @ 0.297718 (22.47 €, apertura)
- 2026-09-30 05:45 [reversion_bb] ENTRADA NIGHT @ 0.02833 (22.94 €, apertura)
- 2026-09-30 05:50 [macd_momentum] CIERRE POL momentum perdido bruto +0.24% neto -0.26%
- 2026-09-30 05:50 [macd_momentum_regimen] CIERRE POL momentum perdido bruto +0.24% neto -0.26%
- 2026-09-30 05:50 [macd_momentum_evento] CIERRE POL momentum perdido bruto +0.24% neto -0.26%
- 2026-09-30 05:45 [macd_momentum] ENTRADA TRUMP @ 1.821 (21.96 €, apertura)
- 2026-09-30 05:45 [macd_momentum_regimen] ENTRADA TRUMP @ 1.821 (22.17 €, apertura)
- 2026-09-30 05:45 [macd_momentum_evento] ENTRADA TRUMP @ 1.821 (22.27 €, apertura)
- 2026-09-30 05:45 [ruptura_estricta] ENTRADA XPL @ 0.086 (22.60 €, apertura)
- 2026-09-30 05:45 [ruptura_volumen_regimen] ENTRADA XPL @ 0.086 (22.47 €, apertura)
- 2026-09-30 05:45 [estocastico_rebote] ENTRADA KAS @ 0.03884 (22.27 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
