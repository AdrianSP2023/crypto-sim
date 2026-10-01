# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 19:32 UTC · vueltas 295 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.32 € (-3.99%) | 242 | 17 | 36% | -0.027% | -0.635% | -0.757% | -34.99 € |
| reversion_bb | 916.50 € (-0.84%) | 48 | 0 | 50% | +0.344% | -0.700% | -0.796% | -7.74 € |
| ruptura_volumen | 873.99 € (-5.44%) | 279 | 10 | 25% | -0.191% | -0.784% | -0.892% | -49.39 € |
| rebote_extremo | 922.08 € (-0.23%) | 13 | 1 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 890.20 € (-3.68%) | 173 | 3 | 15% | -0.215% | -0.867% | -0.961% | -34.10 € |
| macd_momentum | 870.68 € (-5.79%) | 437 | 2 | 22% | +0.016% | -0.544% | -0.649% | -53.48 € |
| estocastico_rebote | 874.14 € (-5.42%) | 289 | 24 | 31% | -0.125% | -0.716% | -0.827% | -46.80 € |
| ruptura_estricta | 882.93 € (-4.47%) | 149 | 16 | 26% | -0.462% | -1.139% | -1.258% | -38.68 € |
| macd_sin_salida | 880.21 € (-4.76%) | 299 | 18 | 36% | -0.044% | -0.632% | -0.748% | -42.93 € |
| c_banda_atr_tope | 911.38 € (-1.39%) | 55 | 5 | 31% | +0.014% | -0.966% | -1.084% | -12.21 € |
| ruptura_volumen_tope | 907.83 € (-1.78%) | 92 | 2 | 29% | +0.032% | -0.755% | -0.869% | -15.93 € |
| c_banda_atr_regimen | 898.87 € (-2.74%) | 115 | 16 | 34% | -0.141% | -0.868% | -1.008% | -22.91 € |
| macd_momentum_regimen | 891.49 € (-3.54%) | 237 | 2 | 22% | +0.005% | -0.605% | -0.716% | -32.66 € |
| ruptura_volumen_regimen | 877.07 € (-5.10%) | 212 | 11 | 19% | -0.338% | -0.961% | -1.076% | -46.09 € |
| c_banda_atr_evento | 893.23 € (-3.36%) | 209 | 17 | 37% | +0.018% | -0.609% | -0.726% | -29.07 € |
| macd_momentum_evento | 875.51 € (-5.27%) | 390 | 2 | 20% | +0.014% | -0.554% | -0.654% | -48.66 € |
| ruptura_volumen_evento | 886.43 € (-4.09%) | 229 | 10 | 26% | -0.095% | -0.711% | -0.809% | -36.93 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 19:30 | ruptura_volumen_evento | FET | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 19:30 | ruptura_volumen_evento | AVAX | timeout | -0.03% | -0.53% | -0.12 |
| 2026-10-01 19:30 | c_banda_atr_evento | WLD | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 19:30 | ruptura_volumen_regimen | FET | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 19:30 | ruptura_volumen_regimen | AVAX | timeout | -0.03% | -0.53% | -0.12 |
| 2026-10-01 19:30 | ruptura_volumen_regimen | BTC | timeout | -0.47% | -0.97% | -0.21 |
| 2026-10-01 19:30 | c_banda_atr_regimen | WLD | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 19:30 | c_banda_atr_regimen | ARB | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 19:30 | macd_sin_salida | PEPE | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 19:30 | macd_sin_salida | TAO | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 19:30 | ruptura_estricta | ALGO | stop-loss | -2.00% | -2.50% | -0.56 |
| 2026-10-01 19:30 | pullback_tendencia | PEPE | rotura de tendencia | +0.10% | -0.40% | -0.09 |
| 2026-10-01 19:30 | pullback_tendencia | LTC | rotura de tendencia | +0.67% | +0.17% | +0.04 |
| 2026-10-01 19:30 | pullback_tendencia | ETH | rotura de tendencia | -0.33% | -0.83% | -0.18 |
| 2026-10-01 19:30 | pullback_tendencia | XRP | rotura de tendencia | -0.56% | -1.06% | -0.24 |

## Eventos de la última vuelta

- 2026-10-01 19:30 [ruptura_volumen_regimen] CIERRE BTC timeout bruto -0.47% neto -0.97%
- 2026-10-01 19:30 [pullback_tendencia] CIERRE XRP rotura de tendencia bruto -0.57% neto -1.07%
- 2026-10-01 19:30 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto -0.33% neto -0.83%
- 2026-10-01 19:30 [ruptura_volumen] CIERRE AVAX timeout bruto -0.03% neto -0.53%
- 2026-10-01 19:30 [ruptura_volumen_regimen] CIERRE AVAX timeout bruto -0.03% neto -0.53%
- 2026-10-01 19:30 [ruptura_volumen_evento] CIERRE AVAX timeout bruto -0.03% neto -0.53%
- 2026-10-01 19:30 [macd_sin_salida] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 19:30 [pullback_tendencia] CIERRE LTC rotura de tendencia bruto +0.67% neto +0.17%
- 2026-10-01 19:30 [c_banda_atr_regimen] CIERRE ARB stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 19:30 [ruptura_volumen] CIERRE FET stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 19:30 [ruptura_volumen_regimen] CIERRE FET stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 19:30 [ruptura_volumen_evento] CIERRE FET stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 19:30 [ruptura_estricta] CIERRE ALGO stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 19:30 [c_banda_atr] CIERRE WLD stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 19:30 [c_banda_atr_regimen] CIERRE WLD stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 19:30 [c_banda_atr_evento] CIERRE WLD stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 19:30 [pullback_tendencia] CIERRE PEPE rotura de tendencia bruto +0.10% neto -0.40%
- 2026-10-01 19:30 [macd_sin_salida] CIERRE PEPE stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 19:25 [c_banda_atr] ENTRADA MINA @ 0.1346 (22.23 €, apertura)
- 2026-10-01 19:25 [c_banda_atr_evento] ENTRADA MINA @ 0.1346 (22.38 €, apertura)
- 2026-10-01 19:25 [rebote_extremo] ENTRADA VVV @ 23.162 (23.05 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
