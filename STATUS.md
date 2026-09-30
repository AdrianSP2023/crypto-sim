# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 05:16 UTC · vueltas 210 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.78 € (-2.86%) | 121 | 22 | 28% | -0.232% | -0.947% | -1.082% | -26.26 € |
| reversion_bb | 917.71 € (-0.71%) | 32 | 7 | 50% | +0.236% | -0.864% | -0.973% | -6.38 € |
| ruptura_volumen | 892.05 € (-3.48%) | 154 | 13 | 19% | -0.252% | -0.922% | -1.047% | -32.33 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.11 € (-2.07%) | 111 | 2 | 26% | -0.016% | -0.751% | -0.878% | -19.12 € |
| macd_momentum | 880.25 € (-4.76%) | 283 | 16 | 17% | -0.111% | -0.703% | -0.816% | -45.02 € |
| estocastico_rebote | 890.41 € (-3.66%) | 195 | 16 | 34% | -0.111% | -0.744% | -0.877% | -33.14 € |
| ruptura_estricta | 904.96 € (-2.09%) | 69 | 6 | 23% | -0.359% | -1.237% | -1.378% | -19.58 € |
| macd_sin_salida | 893.16 € (-3.36%) | 172 | 23 | 28% | -0.151% | -0.803% | -0.930% | -31.47 € |
| c_banda_atr_tope | 910.82 € (-1.45%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 909.92 € (-1.55%) | 56 | 4 | 16% | -0.186% | -1.158% | -1.275% | -14.88 € |
| c_banda_atr_regimen | 900.71 € (-2.55%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 898.84 € (-2.75%) | 116 | 0 | 18% | -0.234% | -0.959% | -1.087% | -25.40 € |
| c_banda_atr_evento | 900.84 € (-2.53%) | 89 | 22 | 25% | -0.340% | -1.137% | -1.273% | -23.20 € |
| macd_momentum_evento | 892.62 € (-3.42%) | 163 | 16 | 13% | -0.217% | -0.879% | -0.990% | -32.65 € |
| ruptura_volumen_evento | 897.54 € (-2.89%) | 95 | 13 | 12% | -0.458% | -1.236% | -1.360% | -26.83 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 05:15 | macd_momentum_evento | CRV | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-09-30 05:15 | macd_momentum_evento | NEAR | momentum perdido | -1.30% | -1.80% | -0.40 |
| 2026-09-30 05:15 | macd_sin_salida | SPX | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 05:15 | estocastico_rebote | ICP | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 05:15 | macd_momentum | CRV | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-09-30 05:15 | macd_momentum | NEAR | momentum perdido | -1.30% | -1.80% | -0.40 |
| 2026-09-30 05:15 | pullback_tendencia | SUI | rotura de tendencia | -0.14% | -0.64% | -0.14 |
| 2026-09-30 05:10 | ruptura_volumen_evento | SPX | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 05:10 | ruptura_volumen_tope | SPX | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 05:10 | estocastico_rebote | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 05:10 | ruptura_volumen | SPX | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 05:05 | macd_momentum_evento | SPX | momentum perdido | -0.69% | -1.19% | -0.27 |
| 2026-09-30 05:05 | macd_momentum_evento | TRUMP | momentum perdido | -0.55% | -1.05% | -0.23 |
| 2026-09-30 05:05 | macd_momentum_evento | TON | take-profit | +2.28% | +1.78% | +0.40 |
| 2026-09-30 05:05 | macd_momentum_evento | DOT | momentum perdido | +0.19% | -0.31% | -0.07 |

## Eventos de la última vuelta

- 2026-09-30 05:10 [macd_momentum] ENTRADA XRP @ 1.31942 (21.99 €, apertura)
- 2026-09-30 05:10 [macd_momentum_evento] ENTRADA XRP @ 1.31942 (22.30 €, apertura)
- 2026-09-30 05:15 [macd_momentum] CIERRE NEAR momentum perdido bruto -1.30% neto -1.80%
- 2026-09-30 05:15 [macd_momentum_evento] CIERRE NEAR momentum perdido bruto -1.30% neto -1.80%
- 2026-09-30 05:15 [pullback_tendencia] CIERRE SUI rotura de tendencia bruto -0.14% neto -0.64%
- 2026-09-30 05:15 [macd_momentum] CIERRE CRV momentum perdido bruto -0.04% neto -0.54%
- 2026-09-30 05:15 [macd_momentum_evento] CIERRE CRV momentum perdido bruto -0.04% neto -0.54%
- 2026-09-30 05:15 [estocastico_rebote] CIERRE ICP take-profit bruto +1.80% neto +1.30%
- 2026-09-30 05:15 [macd_sin_salida] CIERRE SPX stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
