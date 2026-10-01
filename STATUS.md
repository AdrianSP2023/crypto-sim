# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 21:31 UTC · vueltas 319 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 886.47 € (-4.09%) | 254 | 17 | 35% | -0.023% | -0.626% | -0.748% | -36.16 € |
| reversion_bb | 916.65 € (-0.82%) | 49 | 4 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 872.58 € (-5.59%) | 291 | 6 | 25% | -0.196% | -0.786% | -0.894% | -51.56 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.58 € (-3.75%) | 183 | 3 | 15% | -0.201% | -0.845% | -0.935% | -35.11 € |
| macd_momentum | 864.75 € (-6.44%) | 474 | 6 | 21% | -0.008% | -0.563% | -0.665% | -59.79 € |
| estocastico_rebote | 875.95 € (-5.22%) | 298 | 28 | 32% | -0.105% | -0.692% | -0.804% | -46.69 € |
| ruptura_estricta | 883.08 € (-4.45%) | 165 | 1 | 25% | -0.432% | -1.092% | -1.208% | -40.99 € |
| macd_sin_salida | 875.16 € (-5.31%) | 319 | 28 | 36% | -0.046% | -0.628% | -0.742% | -45.42 € |
| c_banda_atr_tope | 911.32 € (-1.40%) | 60 | 3 | 30% | +0.028% | -0.912% | -1.029% | -12.57 € |
| ruptura_volumen_tope | 906.09 € (-1.96%) | 97 | 4 | 28% | -0.020% | -0.792% | -0.907% | -17.61 € |
| c_banda_atr_regimen | 898.07 € (-2.83%) | 125 | 13 | 32% | -0.163% | -0.872% | -1.009% | -24.97 € |
| macd_momentum_regimen | 885.86 € (-4.15%) | 271 | 5 | 20% | -0.031% | -0.628% | -0.733% | -38.59 € |
| ruptura_volumen_regimen | 875.50 € (-5.27%) | 225 | 5 | 20% | -0.343% | -0.959% | -1.074% | -48.73 € |
| c_banda_atr_evento | 892.37 € (-3.45%) | 221 | 17 | 36% | +0.020% | -0.600% | -0.716% | -30.25 € |
| macd_momentum_evento | 869.54 € (-5.92%) | 427 | 6 | 19% | -0.012% | -0.574% | -0.672% | -55.00 € |
| ruptura_volumen_evento | 884.99 € (-4.25%) | 241 | 6 | 26% | -0.107% | -0.716% | -0.815% | -39.13 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 21:30 | c_banda_atr_evento | ONDO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 21:30 | c_banda_atr_regimen | ONDO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 21:30 | c_banda_atr_tope | ONDO | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 21:30 | c_banda_atr | ONDO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 21:25 | macd_momentum_evento | DASH | momentum perdido | -0.32% | -0.82% | -0.18 |
| 2026-10-01 21:25 | macd_momentum_evento | TAO | momentum perdido | -0.81% | -1.31% | -0.29 |
| 2026-10-01 21:25 | c_banda_atr_evento | AAVE | timeout | +1.01% | +0.51% | +0.11 |
| 2026-10-01 21:25 | macd_momentum_regimen | DASH | momentum perdido | -0.32% | -0.82% | -0.18 |
| 2026-10-01 21:25 | macd_momentum_regimen | TAO | momentum perdido | -0.81% | -1.31% | -0.29 |
| 2026-10-01 21:25 | c_banda_atr_regimen | AAVE | timeout | +1.01% | +0.51% | +0.12 |
| 2026-10-01 21:25 | macd_momentum | DASH | momentum perdido | -0.32% | -0.82% | -0.18 |
| 2026-10-01 21:25 | macd_momentum | TAO | momentum perdido | -0.81% | -1.31% | -0.28 |
| 2026-10-01 21:25 | c_banda_atr | AAVE | timeout | +1.01% | +0.51% | +0.11 |
| 2026-10-01 21:20 | macd_momentum_evento | SPX | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 21:20 | macd_momentum_evento | POL | momentum perdido | -0.17% | -0.67% | -0.15 |

## Eventos de la última vuelta

- 2026-10-01 21:25 [estocastico_rebote] ENTRADA ZRO @ 1.595 (21.94 €, apertura)
- 2026-10-01 21:25 [estocastico_rebote] ENTRADA ARB @ 0.1778 (21.94 €, apertura)
- 2026-10-01 21:30 [c_banda_atr] CIERRE ONDO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 21:30 [c_banda_atr_tope] CIERRE ONDO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 21:30 [c_banda_atr_regimen] CIERRE ONDO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 21:30 [c_banda_atr_evento] CIERRE ONDO stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
