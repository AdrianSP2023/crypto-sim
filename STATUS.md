# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 21:17 UTC · vueltas 316 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.00 € (-3.92%) | 250 | 21 | 36% | -0.020% | -0.625% | -0.747% | -35.54 € |
| reversion_bb | 917.05 € (-0.78%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 872.62 € (-5.58%) | 291 | 6 | 25% | -0.196% | -0.786% | -0.894% | -51.56 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.36 € (-3.77%) | 183 | 2 | 15% | -0.201% | -0.845% | -0.935% | -35.11 € |
| macd_momentum | 865.87 € (-6.32%) | 467 | 12 | 21% | -0.006% | -0.562% | -0.665% | -58.83 € |
| estocastico_rebote | 876.80 € (-5.13%) | 298 | 25 | 32% | -0.105% | -0.692% | -0.804% | -46.69 € |
| ruptura_estricta | 883.07 € (-4.45%) | 165 | 1 | 25% | -0.432% | -1.092% | -1.208% | -40.99 € |
| macd_sin_salida | 877.25 € (-5.08%) | 317 | 29 | 37% | -0.035% | -0.618% | -0.732% | -44.46 € |
| c_banda_atr_tope | 911.74 € (-1.35%) | 59 | 4 | 31% | +0.054% | -0.893% | -1.010% | -12.11 € |
| ruptura_volumen_tope | 906.35 € (-1.94%) | 97 | 4 | 28% | -0.020% | -0.792% | -0.907% | -17.61 € |
| c_banda_atr_regimen | 899.76 € (-2.65%) | 119 | 19 | 33% | -0.145% | -0.864% | -1.002% | -23.58 € |
| macd_momentum_regimen | 887.09 € (-4.02%) | 264 | 12 | 20% | -0.029% | -0.628% | -0.734% | -37.61 € |
| ruptura_volumen_regimen | 875.55 € (-5.27%) | 225 | 5 | 20% | -0.343% | -0.959% | -1.074% | -48.73 € |
| c_banda_atr_evento | 893.91 € (-3.28%) | 217 | 21 | 36% | +0.024% | -0.598% | -0.715% | -29.63 € |
| macd_momentum_evento | 870.67 € (-5.80%) | 420 | 12 | 19% | -0.010% | -0.573% | -0.672% | -54.04 € |
| ruptura_volumen_evento | 885.04 € (-4.24%) | 241 | 6 | 26% | -0.107% | -0.716% | -0.815% | -39.13 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 21:15 | ruptura_volumen_evento | PUMP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 21:15 | macd_momentum_evento | TRUMP | momentum perdido | -0.33% | -0.83% | -0.18 |
| 2026-10-01 21:15 | c_banda_atr_evento | SPX | timeout | +0.85% | +0.35% | +0.08 |
| 2026-10-01 21:15 | ruptura_volumen_regimen | PUMP | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-01 21:15 | macd_momentum_regimen | TRUMP | momentum perdido | -0.33% | -0.83% | -0.18 |
| 2026-10-01 21:15 | ruptura_volumen_tope | MINA | stop-loss | -1.47% | -1.97% | -0.45 |
| 2026-10-01 21:15 | ruptura_volumen_tope | PUMP | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 21:15 | macd_sin_salida | ZRO | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 21:15 | macd_sin_salida | PUMP | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 21:15 | macd_momentum | TRUMP | momentum perdido | -0.33% | -0.83% | -0.18 |
| 2026-10-01 21:15 | pullback_tendencia | TRUMP | rotura de tendencia | -0.33% | -0.83% | -0.18 |
| 2026-10-01 21:15 | pullback_tendencia | AVAX | rotura de tendencia | -0.38% | -0.88% | -0.20 |
| 2026-10-01 21:15 | ruptura_volumen | PUMP | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-01 21:15 | c_banda_atr | SPX | timeout | +0.85% | +0.35% | +0.08 |
| 2026-10-01 21:10 | macd_momentum_evento | WLD | momentum perdido | -0.47% | -0.97% | -0.21 |

## Eventos de la última vuelta

- 2026-10-01 21:15 [pullback_tendencia] CIERRE AVAX rotura de tendencia bruto -0.38% neto -0.88%
- 2026-10-01 21:15 [ruptura_volumen] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 21:15 [macd_sin_salida] CIERRE PUMP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 21:15 [ruptura_volumen_tope] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 21:15 [ruptura_volumen_regimen] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 21:15 [ruptura_volumen_evento] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 21:15 [macd_sin_salida] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 21:15 [ruptura_volumen_tope] CIERRE MINA stop-loss bruto -1.47% neto -1.97%
- 2026-10-01 21:10 [c_banda_atr_tope] ENTRADA DASH @ 52.098 (22.80 €, apertura)
- 2026-10-01 21:15 [pullback_tendencia] CIERRE TRUMP rotura de tendencia bruto -0.33% neto -0.83%
- 2026-10-01 21:15 [macd_momentum] CIERRE TRUMP momentum perdido bruto -0.33% neto -0.83%
- 2026-10-01 21:15 [macd_momentum_regimen] CIERRE TRUMP momentum perdido bruto -0.33% neto -0.83%
- 2026-10-01 21:15 [macd_momentum_evento] CIERRE TRUMP momentum perdido bruto -0.33% neto -0.83%
- 2026-10-01 21:10 [ruptura_volumen_tope] ENTRADA TON @ 1.403 (22.67 €, apertura)
- 2026-10-01 21:15 [c_banda_atr] CIERRE SPX timeout bruto +0.85% neto +0.35%
- 2026-10-01 21:15 [c_banda_atr_evento] CIERRE SPX timeout bruto +0.85% neto +0.35%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
