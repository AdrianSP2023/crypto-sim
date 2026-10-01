# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 21:12 UTC · vueltas 315 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.01 € (-3.81%) | 249 | 22 | 35% | -0.024% | -0.628% | -0.752% | -35.62 € |
| reversion_bb | 917.25 € (-0.76%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 873.06 € (-5.54%) | 290 | 7 | 25% | -0.193% | -0.783% | -0.890% | -51.19 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.76 € (-3.73%) | 181 | 4 | 15% | -0.199% | -0.845% | -0.935% | -34.73 € |
| macd_momentum | 866.34 € (-6.26%) | 466 | 13 | 21% | -0.005% | -0.561% | -0.664% | -58.65 € |
| estocastico_rebote | 877.48 € (-5.06%) | 298 | 25 | 32% | -0.105% | -0.692% | -0.804% | -46.69 € |
| ruptura_estricta | 883.13 € (-4.45%) | 165 | 1 | 25% | -0.432% | -1.092% | -1.208% | -40.99 € |
| macd_sin_salida | 878.71 € (-4.93%) | 315 | 31 | 37% | -0.026% | -0.609% | -0.723% | -43.58 € |
| c_banda_atr_tope | 911.89 € (-1.34%) | 59 | 3 | 31% | +0.054% | -0.893% | -1.010% | -12.11 € |
| ruptura_volumen_tope | 907.06 € (-1.86%) | 95 | 5 | 28% | +0.008% | -0.770% | -0.884% | -16.78 € |
| c_banda_atr_regimen | 900.33 € (-2.59%) | 119 | 19 | 33% | -0.145% | -0.864% | -1.002% | -23.58 € |
| macd_momentum_regimen | 887.57 € (-3.97%) | 263 | 13 | 20% | -0.028% | -0.627% | -0.733% | -37.43 € |
| ruptura_volumen_regimen | 875.98 € (-5.22%) | 224 | 6 | 20% | -0.339% | -0.955% | -1.070% | -48.36 € |
| c_banda_atr_evento | 894.93 € (-3.17%) | 216 | 22 | 36% | +0.020% | -0.602% | -0.720% | -29.70 € |
| macd_momentum_evento | 871.14 € (-5.75%) | 419 | 13 | 19% | -0.009% | -0.572% | -0.671% | -53.86 € |
| ruptura_volumen_evento | 885.48 € (-4.19%) | 240 | 7 | 26% | -0.102% | -0.712% | -0.811% | -38.75 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 21:10 | macd_momentum_evento | WLD | momentum perdido | -0.47% | -0.97% | -0.21 |
| 2026-10-01 21:10 | macd_momentum_evento | ONDO | momentum perdido | -0.53% | -1.03% | -0.23 |
| 2026-10-01 21:10 | macd_momentum_evento | ARB | momentum perdido | -0.11% | -0.61% | -0.13 |
| 2026-10-01 21:10 | c_banda_atr_evento | PEPE | timeout | +0.18% | -0.32% | -0.07 |
| 2026-10-01 21:10 | macd_momentum_regimen | ONDO | momentum perdido | -0.53% | -1.03% | -0.23 |
| 2026-10-01 21:10 | macd_momentum_regimen | ARB | momentum perdido | -0.11% | -0.61% | -0.14 |
| 2026-10-01 21:10 | estocastico_rebote | TON | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-01 21:10 | macd_momentum | WLD | momentum perdido | -0.47% | -0.97% | -0.21 |
| 2026-10-01 21:10 | macd_momentum | ONDO | momentum perdido | -0.53% | -1.03% | -0.23 |
| 2026-10-01 21:10 | macd_momentum | ARB | momentum perdido | -0.11% | -0.61% | -0.13 |
| 2026-10-01 21:10 | c_banda_atr | PEPE | timeout | +0.18% | -0.32% | -0.07 |
| 2026-10-01 21:05 | macd_momentum_evento | APT | momentum perdido | -0.28% | -0.78% | -0.17 |
| 2026-10-01 21:05 | macd_momentum_evento | PENGU | momentum perdido | -0.14% | -0.64% | -0.14 |
| 2026-10-01 21:05 | macd_momentum_evento | ADA | momentum perdido | -0.63% | -1.13% | -0.25 |
| 2026-10-01 21:05 | c_banda_atr_evento | PUMP | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-10-01 21:10 [macd_momentum] CIERRE ARB momentum perdido bruto -0.11% neto -0.61%
- 2026-10-01 21:10 [macd_momentum_regimen] CIERRE ARB momentum perdido bruto -0.11% neto -0.61%
- 2026-10-01 21:10 [macd_momentum_evento] CIERRE ARB momentum perdido bruto -0.11% neto -0.61%
- 2026-10-01 21:10 [macd_momentum] CIERRE ONDO momentum perdido bruto -0.53% neto -1.03%
- 2026-10-01 21:10 [macd_momentum_regimen] CIERRE ONDO momentum perdido bruto -0.53% neto -1.03%
- 2026-10-01 21:10 [macd_momentum_evento] CIERRE ONDO momentum perdido bruto -0.53% neto -1.03%
- 2026-10-01 21:10 [macd_momentum] CIERRE WLD momentum perdido bruto -0.47% neto -0.97%
- 2026-10-01 21:10 [macd_momentum_evento] CIERRE WLD momentum perdido bruto -0.47% neto -0.97%
- 2026-10-01 21:10 [c_banda_atr] CIERRE PEPE timeout bruto +0.18% neto -0.32%
- 2026-10-01 21:10 [c_banda_atr_evento] CIERRE PEPE timeout bruto +0.18% neto -0.32%
- 2026-10-01 21:05 [estocastico_rebote] ENTRADA MON @ 0.03015 (21.93 €, apertura)
- 2026-10-01 21:10 [estocastico_rebote] CIERRE TON take-profit bruto +1.80% neto +1.30%
- 2026-10-01 21:05 [ruptura_volumen] ENTRADA SKY @ 0.07448 (21.83 €, apertura)
- 2026-10-01 21:05 [ruptura_volumen_regimen] ENTRADA SKY @ 0.07448 (21.90 €, apertura)
- 2026-10-01 21:05 [ruptura_volumen_evento] ENTRADA SKY @ 0.07448 (22.14 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
