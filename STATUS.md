# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 21:21 UTC · vueltas 317 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.36 € (-3.99%) | 252 | 19 | 35% | -0.021% | -0.625% | -0.747% | -35.83 € |
| reversion_bb | 917.00 € (-0.78%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 872.63 € (-5.58%) | 291 | 6 | 25% | -0.196% | -0.786% | -0.894% | -51.56 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.50 € (-3.76%) | 183 | 2 | 15% | -0.201% | -0.845% | -0.935% | -35.11 € |
| macd_momentum | 864.99 € (-6.41%) | 472 | 7 | 21% | -0.005% | -0.561% | -0.663% | -59.33 € |
| estocastico_rebote | 876.58 € (-5.16%) | 298 | 25 | 32% | -0.105% | -0.692% | -0.804% | -46.69 € |
| ruptura_estricta | 883.09 € (-4.45%) | 165 | 1 | 25% | -0.432% | -1.092% | -1.208% | -40.99 € |
| macd_sin_salida | 875.95 € (-5.22%) | 319 | 27 | 36% | -0.046% | -0.628% | -0.742% | -45.42 € |
| c_banda_atr_tope | 911.60 € (-1.37%) | 59 | 4 | 31% | +0.054% | -0.893% | -1.010% | -12.11 € |
| ruptura_volumen_tope | 906.21 € (-1.95%) | 97 | 4 | 28% | -0.020% | -0.792% | -0.907% | -17.61 € |
| c_banda_atr_regimen | 898.93 € (-2.74%) | 123 | 15 | 32% | -0.162% | -0.874% | -1.012% | -24.64 € |
| macd_momentum_regimen | 886.19 € (-4.12%) | 269 | 7 | 20% | -0.028% | -0.625% | -0.730% | -38.12 € |
| ruptura_volumen_regimen | 875.55 € (-5.27%) | 225 | 5 | 20% | -0.343% | -0.959% | -1.074% | -48.73 € |
| c_banda_atr_evento | 893.26 € (-3.35%) | 219 | 19 | 36% | +0.022% | -0.598% | -0.715% | -29.91 € |
| macd_momentum_evento | 869.79 € (-5.89%) | 425 | 7 | 19% | -0.009% | -0.571% | -0.670% | -54.53 € |
| ruptura_volumen_evento | 885.04 € (-4.24%) | 241 | 6 | 26% | -0.107% | -0.716% | -0.815% | -39.13 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 21:20 | macd_momentum_evento | SPX | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 21:20 | macd_momentum_evento | POL | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-10-01 21:20 | macd_momentum_evento | ICP | momentum perdido | -0.58% | -1.08% | -0.24 |
| 2026-10-01 21:20 | macd_momentum_evento | LTC | momentum perdido | +0.45% | -0.06% | -0.01 |
| 2026-10-01 21:20 | macd_momentum_evento | AAVE | momentum perdido | +0.53% | +0.03% | +0.01 |
| 2026-10-01 21:20 | c_banda_atr_evento | UNI | timeout | -0.65% | -1.15% | -0.26 |
| 2026-10-01 21:20 | c_banda_atr_evento | AVAX | timeout | +0.36% | -0.14% | -0.03 |
| 2026-10-01 21:20 | macd_momentum_regimen | SPX | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 21:20 | macd_momentum_regimen | POL | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-10-01 21:20 | macd_momentum_regimen | ICP | momentum perdido | -0.58% | -1.08% | -0.24 |
| 2026-10-01 21:20 | macd_momentum_regimen | LTC | momentum perdido | +0.45% | -0.06% | -0.01 |
| 2026-10-01 21:20 | macd_momentum_regimen | AAVE | momentum perdido | +0.53% | +0.03% | +0.01 |
| 2026-10-01 21:20 | c_banda_atr_regimen | KSM | stop-loss | -1.52% | -2.02% | -0.46 |
| 2026-10-01 21:20 | c_banda_atr_regimen | DASH | timeout | -0.85% | -1.35% | -0.31 |
| 2026-10-01 21:20 | c_banda_atr_regimen | UNI | timeout | -0.65% | -1.15% | -0.26 |

## Eventos de la última vuelta

- 2026-10-01 21:20 [macd_sin_salida] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 21:20 [c_banda_atr] CIERRE AVAX timeout bruto +0.36% neto -0.14%
- 2026-10-01 21:20 [c_banda_atr_regimen] CIERRE AVAX timeout bruto +0.36% neto -0.14%
- 2026-10-01 21:20 [c_banda_atr_evento] CIERRE AVAX timeout bruto +0.36% neto -0.14%
- 2026-10-01 21:20 [macd_momentum] CIERRE AAVE momentum perdido bruto +0.53% neto +0.03%
- 2026-10-01 21:20 [macd_momentum_regimen] CIERRE AAVE momentum perdido bruto +0.53% neto +0.03%
- 2026-10-01 21:20 [macd_momentum_evento] CIERRE AAVE momentum perdido bruto +0.53% neto +0.03%
- 2026-10-01 21:20 [c_banda_atr] CIERRE UNI timeout bruto -0.65% neto -1.15%
- 2026-10-01 21:20 [c_banda_atr_regimen] CIERRE UNI timeout bruto -0.65% neto -1.15%
- 2026-10-01 21:20 [c_banda_atr_evento] CIERRE UNI timeout bruto -0.65% neto -1.15%
- 2026-10-01 21:20 [macd_momentum] CIERRE LTC momentum perdido bruto +0.45% neto -0.05%
- 2026-10-01 21:20 [macd_momentum_regimen] CIERRE LTC momentum perdido bruto +0.45% neto -0.05%
- 2026-10-01 21:20 [macd_momentum_evento] CIERRE LTC momentum perdido bruto +0.45% neto -0.05%
- 2026-10-01 21:20 [macd_momentum] CIERRE ICP momentum perdido bruto -0.58% neto -1.08%
- 2026-10-01 21:20 [macd_momentum_regimen] CIERRE ICP momentum perdido bruto -0.58% neto -1.08%
- 2026-10-01 21:20 [macd_momentum_evento] CIERRE ICP momentum perdido bruto -0.58% neto -1.08%
- 2026-10-01 21:20 [macd_momentum] CIERRE POL momentum perdido bruto -0.17% neto -0.67%
- 2026-10-01 21:20 [macd_momentum_regimen] CIERRE POL momentum perdido bruto -0.17% neto -0.67%
- 2026-10-01 21:20 [macd_momentum_evento] CIERRE POL momentum perdido bruto -0.17% neto -0.67%
- 2026-10-01 21:20 [macd_sin_salida] CIERRE MINA stop-loss bruto -1.84% neto -2.34%
- 2026-10-01 21:20 [c_banda_atr_regimen] CIERRE DASH timeout bruto -0.86% neto -1.36%
- 2026-10-01 21:20 [c_banda_atr_regimen] CIERRE KSM stop-loss bruto -1.53% neto -2.03%
- 2026-10-01 21:20 [macd_momentum] CIERRE SPX momentum perdido bruto +0.00% neto -0.50%
- 2026-10-01 21:20 [macd_momentum_regimen] CIERRE SPX momentum perdido bruto +0.00% neto -0.50%
- 2026-10-01 21:20 [macd_momentum_evento] CIERRE SPX momentum perdido bruto +0.00% neto -0.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
