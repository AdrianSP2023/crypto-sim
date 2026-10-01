# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 23:56 UTC · vueltas 348 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.73 € (-4.27%) | 267 | 23 | 34% | -0.048% | -0.645% | -0.767% | -39.14 € |
| reversion_bb | 917.76 € (-0.70%) | 52 | 16 | 50% | +0.317% | -0.685% | -0.782% | -8.21 € |
| ruptura_volumen | 871.82 € (-5.67%) | 297 | 5 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.05 € (-3.81%) | 187 | 5 | 15% | -0.194% | -0.836% | -0.925% | -35.47 € |
| macd_momentum | 863.11 € (-6.61%) | 489 | 11 | 20% | -0.011% | -0.564% | -0.668% | -61.77 € |
| estocastico_rebote | 872.52 € (-5.60%) | 327 | 14 | 31% | -0.130% | -0.709% | -0.819% | -52.33 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 871.33 € (-5.72%) | 347 | 10 | 34% | -0.103% | -0.678% | -0.790% | -53.17 € |
| c_banda_atr_tope | 911.13 € (-1.42%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.89 € (-1.99%) | 101 | 5 | 27% | -0.042% | -0.803% | -0.920% | -18.58 € |
| c_banda_atr_regimen | 896.11 € (-3.04%) | 135 | 3 | 30% | -0.208% | -0.902% | -1.035% | -27.84 € |
| macd_momentum_regimen | 885.23 € (-4.22%) | 276 | 0 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 874.82 € (-5.35%) | 230 | 0 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 890.62 € (-3.64%) | 234 | 23 | 35% | -0.011% | -0.623% | -0.740% | -33.24 € |
| macd_momentum_evento | 867.90 € (-6.10%) | 442 | 11 | 19% | -0.015% | -0.575% | -0.675% | -57.00 € |
| ruptura_volumen_evento | 884.22 € (-4.33%) | 247 | 5 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 23:55 | macd_momentum_evento | AAVE | momentum perdido | +0.45% | -0.05% | -0.01 |
| 2026-10-01 23:55 | c_banda_atr_evento | TRUMP | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 23:55 | c_banda_atr_evento | FET | timeout | +0.24% | -0.26% | -0.06 |
| 2026-10-01 23:55 | c_banda_atr_evento | TAO | timeout | -0.32% | -0.82% | -0.18 |
| 2026-10-01 23:55 | c_banda_atr_evento | XLM | timeout | -0.22% | -0.72% | -0.16 |
| 2026-10-01 23:55 | c_banda_atr_regimen | TRUMP | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 23:55 | c_banda_atr_regimen | FET | timeout | +0.24% | -0.26% | -0.06 |
| 2026-10-01 23:55 | c_banda_atr_regimen | TAO | timeout | -0.32% | -0.82% | -0.19 |
| 2026-10-01 23:55 | macd_sin_salida | NIGHT | stop-loss | -1.64% | -2.14% | -0.47 |
| 2026-10-01 23:55 | macd_momentum | AAVE | momentum perdido | +0.45% | -0.05% | -0.01 |
| 2026-10-01 23:55 | c_banda_atr | TRUMP | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 23:55 | c_banda_atr | FET | timeout | +0.24% | -0.26% | -0.06 |
| 2026-10-01 23:55 | c_banda_atr | TAO | timeout | -0.32% | -0.82% | -0.18 |
| 2026-10-01 23:55 | c_banda_atr | XLM | timeout | -0.22% | -0.72% | -0.16 |
| 2026-10-01 23:50 | macd_momentum_evento | DASH | momentum perdido | -0.65% | -1.15% | -0.25 |

## Eventos de la última vuelta

- 2026-10-01 23:50 [ruptura_volumen] ENTRADA AVAX @ 9.769 (21.79 €, apertura)
- 2026-10-01 23:50 [ruptura_volumen_tope] ENTRADA AVAX @ 9.769 (22.64 €, apertura)
- 2026-10-01 23:50 [ruptura_volumen_evento] ENTRADA AVAX @ 9.769 (22.10 €, apertura)
- 2026-10-01 23:55 [macd_momentum] CIERRE AAVE momentum perdido bruto +0.45% neto -0.05%
- 2026-10-01 23:55 [macd_momentum_evento] CIERRE AAVE momentum perdido bruto +0.45% neto -0.05%
- 2026-10-01 23:55 [c_banda_atr] CIERRE XLM timeout bruto -0.22% neto -0.72%
- 2026-10-01 23:55 [c_banda_atr_evento] CIERRE XLM timeout bruto -0.22% neto -0.72%
- 2026-10-01 23:55 [c_banda_atr] CIERRE TAO timeout bruto -0.32% neto -0.82%
- 2026-10-01 23:55 [c_banda_atr_regimen] CIERRE TAO timeout bruto -0.32% neto -0.82%
- 2026-10-01 23:55 [c_banda_atr_evento] CIERRE TAO timeout bruto -0.32% neto -0.82%
- 2026-10-01 23:55 [c_banda_atr] CIERRE FET timeout bruto +0.24% neto -0.26%
- 2026-10-01 23:55 [c_banda_atr_regimen] CIERRE FET timeout bruto +0.24% neto -0.26%
- 2026-10-01 23:55 [c_banda_atr_evento] CIERRE FET timeout bruto +0.24% neto -0.26%
- 2026-10-01 23:55 [macd_sin_salida] CIERRE NIGHT stop-loss bruto -1.64% neto -2.14%
- 2026-10-01 23:55 [c_banda_atr] CIERRE TRUMP timeout bruto -0.16% neto -0.66%
- 2026-10-01 23:55 [c_banda_atr_regimen] CIERRE TRUMP timeout bruto -0.16% neto -0.66%
- 2026-10-01 23:55 [c_banda_atr_evento] CIERRE TRUMP timeout bruto -0.16% neto -0.66%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
