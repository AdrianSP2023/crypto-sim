# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 19:27 UTC · vueltas 294 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.48 € (-3.87%) | 241 | 17 | 36% | -0.021% | -0.629% | -0.752% | -34.55 € |
| reversion_bb | 916.50 € (-0.84%) | 48 | 0 | 50% | +0.344% | -0.700% | -0.796% | -7.74 € |
| ruptura_volumen | 875.08 € (-5.32%) | 277 | 12 | 25% | -0.187% | -0.782% | -0.890% | -48.91 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 891.06 € (-3.59%) | 169 | 7 | 15% | -0.219% | -0.875% | -0.971% | -33.63 € |
| macd_momentum | 870.80 € (-5.78%) | 437 | 2 | 22% | +0.016% | -0.544% | -0.649% | -53.48 € |
| estocastico_rebote | 875.66 € (-5.26%) | 289 | 24 | 31% | -0.125% | -0.716% | -0.827% | -46.80 € |
| ruptura_estricta | 884.33 € (-4.32%) | 148 | 17 | 26% | -0.451% | -1.130% | -1.249% | -38.13 € |
| macd_sin_salida | 881.58 € (-4.62%) | 297 | 20 | 37% | -0.035% | -0.622% | -0.739% | -42.05 € |
| c_banda_atr_tope | 911.57 € (-1.37%) | 55 | 5 | 31% | +0.014% | -0.966% | -1.084% | -12.21 € |
| ruptura_volumen_tope | 907.95 € (-1.76%) | 92 | 2 | 29% | +0.032% | -0.755% | -0.869% | -15.93 € |
| c_banda_atr_regimen | 900.29 € (-2.59%) | 113 | 18 | 35% | -0.117% | -0.848% | -0.988% | -22.01 € |
| macd_momentum_regimen | 891.61 € (-3.53%) | 237 | 2 | 22% | +0.005% | -0.605% | -0.716% | -32.66 € |
| ruptura_volumen_regimen | 878.36 € (-4.96%) | 209 | 14 | 20% | -0.334% | -0.959% | -1.076% | -45.38 € |
| c_banda_atr_evento | 894.40 € (-3.23%) | 208 | 17 | 37% | +0.025% | -0.602% | -0.719% | -28.62 € |
| macd_momentum_evento | 875.63 € (-5.26%) | 390 | 2 | 20% | +0.014% | -0.554% | -0.654% | -48.66 € |
| ruptura_volumen_evento | 887.53 € (-3.97%) | 227 | 12 | 26% | -0.091% | -0.707% | -0.806% | -36.44 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 19:25 | ruptura_volumen_evento | SPX | timeout | -0.97% | -1.47% | -0.33 |
| 2026-10-01 19:25 | ruptura_volumen_evento | TRUMP | timeout | -0.65% | -1.15% | -0.26 |
| 2026-10-01 19:25 | ruptura_volumen_evento | DASH | stop-loss | -1.27% | -1.77% | -0.39 |
| 2026-10-01 19:25 | ruptura_volumen_evento | WLFI | timeout | +0.61% | +0.11% | +0.02 |
| 2026-10-01 19:25 | c_banda_atr_evento | DASH | timeout | -0.42% | -0.93% | -0.21 |
| 2026-10-01 19:25 | c_banda_atr_evento | OP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 19:25 | ruptura_volumen_regimen | SPX | timeout | -0.97% | -1.47% | -0.33 |
| 2026-10-01 19:25 | ruptura_volumen_regimen | TRUMP | timeout | -0.65% | -1.15% | -0.25 |
| 2026-10-01 19:25 | ruptura_volumen_regimen | DASH | stop-loss | -1.27% | -1.77% | -0.39 |
| 2026-10-01 19:25 | ruptura_volumen_regimen | WLFI | timeout | +0.61% | +0.11% | +0.02 |
| 2026-10-01 19:25 | c_banda_atr_regimen | OP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 19:25 | ruptura_volumen_tope | SPX | timeout | -0.97% | -1.47% | -0.34 |
| 2026-10-01 19:25 | ruptura_volumen_tope | WLFI | timeout | +0.61% | +0.11% | +0.03 |
| 2026-10-01 19:25 | macd_sin_salida | OP | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 19:25 | macd_sin_salida | INJ | stop-loss | -1.50% | -2.00% | -0.44 |

## Eventos de la última vuelta

- 2026-10-01 19:25 [pullback_tendencia] CIERRE SUI rotura de tendencia bruto -0.97% neto -1.47%
- 2026-10-01 19:25 [pullback_tendencia] CIERRE DOGE rotura de tendencia bruto -0.56% neto -1.06%
- 2026-10-01 19:25 [macd_sin_salida] CIERRE INJ stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 19:25 [c_banda_atr] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 19:25 [macd_sin_salida] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 19:25 [c_banda_atr_regimen] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 19:25 [c_banda_atr_evento] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 19:25 [pullback_tendencia] CIERRE FIL rotura de tendencia bruto -0.55% neto -1.05%
- 2026-10-01 19:20 [estocastico_rebote] ENTRADA VVV @ 23.4 (21.94 €, apertura)
- 2026-10-01 19:25 [ruptura_volumen] CIERRE WLFI timeout bruto +0.61% neto +0.11%
- 2026-10-01 19:25 [ruptura_volumen_tope] CIERRE WLFI timeout bruto +0.61% neto +0.11%
- 2026-10-01 19:25 [ruptura_volumen_regimen] CIERRE WLFI timeout bruto +0.61% neto +0.11%
- 2026-10-01 19:25 [ruptura_volumen_evento] CIERRE WLFI timeout bruto +0.61% neto +0.11%
- 2026-10-01 19:25 [c_banda_atr] CIERRE DASH timeout bruto -0.43% neto -0.93%
- 2026-10-01 19:25 [ruptura_volumen] CIERRE DASH stop-loss bruto -1.27% neto -1.77%
- 2026-10-01 19:25 [ruptura_volumen_regimen] CIERRE DASH stop-loss bruto -1.27% neto -1.77%
- 2026-10-01 19:25 [c_banda_atr_evento] CIERRE DASH timeout bruto -0.43% neto -0.93%
- 2026-10-01 19:25 [ruptura_volumen_evento] CIERRE DASH stop-loss bruto -1.27% neto -1.77%
- 2026-10-01 19:25 [ruptura_volumen] CIERRE TRUMP timeout bruto -0.65% neto -1.15%
- 2026-10-01 19:25 [ruptura_volumen_regimen] CIERRE TRUMP timeout bruto -0.65% neto -1.15%
- 2026-10-01 19:25 [ruptura_volumen_evento] CIERRE TRUMP timeout bruto -0.65% neto -1.15%
- 2026-10-01 19:25 [pullback_tendencia] CIERRE XMR rotura de tendencia bruto -0.83% neto -1.33%
- 2026-10-01 19:25 [ruptura_estricta] CIERRE XMR timeout bruto +0.25% neto -0.25%
- 2026-10-01 19:25 [ruptura_volumen] CIERRE SPX timeout bruto -0.97% neto -1.47%
- 2026-10-01 19:25 [ruptura_volumen_tope] CIERRE SPX timeout bruto -0.97% neto -1.47%
- 2026-10-01 19:25 [ruptura_volumen_regimen] CIERRE SPX timeout bruto -0.97% neto -1.47%
- 2026-10-01 19:25 [ruptura_volumen_evento] CIERRE SPX timeout bruto -0.97% neto -1.47%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
