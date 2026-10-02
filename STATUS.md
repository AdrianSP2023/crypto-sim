# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 00:01 UTC · vueltas 335 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.59 € (-4.29%) | 268 | 23 | 34% | -0.048% | -0.646% | -0.767% | -39.30 € |
| reversion_bb | 917.85 € (-0.69%) | 52 | 16 | 50% | +0.317% | -0.685% | -0.782% | -8.21 € |
| ruptura_volumen | 871.85 € (-5.67%) | 297 | 6 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.95 € (-3.82%) | 187 | 5 | 15% | -0.194% | -0.836% | -0.925% | -35.47 € |
| macd_momentum | 863.16 € (-6.61%) | 489 | 13 | 20% | -0.011% | -0.564% | -0.667% | -61.77 € |
| estocastico_rebote | 872.49 € (-5.60%) | 328 | 13 | 30% | -0.129% | -0.708% | -0.818% | -52.39 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 1 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 871.30 € (-5.73%) | 347 | 11 | 34% | -0.103% | -0.678% | -0.790% | -53.17 € |
| c_banda_atr_tope | 911.14 € (-1.42%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.93 € (-1.98%) | 101 | 5 | 27% | -0.042% | -0.803% | -0.919% | -18.58 € |
| c_banda_atr_regimen | 895.99 € (-3.06%) | 136 | 2 | 29% | -0.209% | -0.900% | -1.034% | -28.01 € |
| macd_momentum_regimen | 885.23 € (-4.22%) | 276 | 0 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 874.82 € (-5.35%) | 230 | 0 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 890.48 € (-3.65%) | 235 | 23 | 34% | -0.012% | -0.624% | -0.740% | -33.41 € |
| macd_momentum_evento | 867.94 € (-6.09%) | 442 | 13 | 19% | -0.015% | -0.575% | -0.674% | -57.00 € |
| ruptura_volumen_evento | 884.26 € (-4.33%) | 247 | 6 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 00:00 | c_banda_atr_evento | XMR | timeout | -0.25% | -0.75% | -0.17 |
| 2026-10-02 00:00 | c_banda_atr_regimen | XMR | timeout | -0.25% | -0.75% | -0.17 |
| 2026-10-02 00:00 | estocastico_rebote | SKY | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-02 00:00 | c_banda_atr | XMR | timeout | -0.25% | -0.75% | -0.17 |
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

## Eventos de la última vuelta

- 2026-10-01 23:55 [macd_momentum] ENTRADA POL @ 0.09587 (21.56 €, apertura)
- 2026-10-01 23:55 [macd_sin_salida] ENTRADA POL @ 0.09587 (21.78 €, apertura)
- 2026-10-01 23:55 [macd_momentum_evento] ENTRADA POL @ 0.09587 (21.68 €, apertura)
- 2026-10-01 23:55 [c_banda_atr] ENTRADA VVV @ 23.28 (22.13 €, apertura)
- 2026-10-01 23:55 [c_banda_atr_evento] ENTRADA VVV @ 23.28 (22.27 €, apertura)
- 2026-10-01 23:55 [macd_momentum] ENTRADA WLFI @ 0.0498 (21.56 €, apertura)
- 2026-10-01 23:55 [ruptura_estricta] ENTRADA WLFI @ 0.0498 (22.07 €, apertura)
- 2026-10-01 23:55 [macd_momentum_evento] ENTRADA WLFI @ 0.0498 (21.68 €, apertura)
- 2026-10-01 23:55 [ruptura_volumen] ENTRADA SHIB @ 5.149e-06 (21.79 €, apertura)
- 2026-10-01 23:55 [ruptura_volumen_evento] ENTRADA SHIB @ 5.149e-06 (22.10 €, apertura)
- 2026-10-02 00:00 [estocastico_rebote] CIERRE SKY timeout bruto +0.23% neto -0.27%
- 2026-10-02 00:00 [c_banda_atr] CIERRE XMR timeout bruto -0.25% neto -0.75%
- 2026-10-02 00:00 [c_banda_atr_regimen] CIERRE XMR timeout bruto -0.25% neto -0.75%
- 2026-10-02 00:00 [c_banda_atr_evento] CIERRE XMR timeout bruto -0.25% neto -0.75%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
