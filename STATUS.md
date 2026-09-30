# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 04:16 UTC · vueltas 198 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.77 € (-2.86%) | 114 | 20 | 27% | -0.265% | -0.994% | -1.128% | -25.96 € |
| reversion_bb | 918.48 € (-0.62%) | 30 | 9 | 47% | +0.137% | -0.963% | -1.068% | -6.66 € |
| ruptura_volumen | 893.00 € (-3.38%) | 151 | 2 | 20% | -0.234% | -0.907% | -1.032% | -31.19 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.06 € (-2.08%) | 109 | 1 | 26% | -0.034% | -0.773% | -0.900% | -19.31 € |
| macd_momentum | 880.68 € (-4.71%) | 271 | 12 | 17% | -0.123% | -0.720% | -0.834% | -44.14 € |
| estocastico_rebote | 890.90 € (-3.61%) | 191 | 18 | 34% | -0.133% | -0.770% | -0.902% | -33.57 € |
| ruptura_estricta | 904.97 € (-2.09%) | 66 | 4 | 24% | -0.359% | -1.255% | -1.397% | -19.00 € |
| macd_sin_salida | 893.34 € (-3.34%) | 166 | 16 | 28% | -0.173% | -0.831% | -0.956% | -31.42 € |
| c_banda_atr_tope | 910.53 € (-1.48%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.17 € (-1.52%) | 54 | 3 | 17% | -0.149% | -1.138% | -1.257% | -14.11 € |
| c_banda_atr_regimen | 900.73 € (-2.54%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 898.84 € (-2.75%) | 116 | 0 | 18% | -0.234% | -0.959% | -1.087% | -25.40 € |
| c_banda_atr_evento | 900.83 € (-2.53%) | 82 | 20 | 23% | -0.396% | -1.217% | -1.354% | -22.90 € |
| macd_momentum_evento | 893.06 € (-3.37%) | 151 | 12 | 13% | -0.248% | -0.923% | -1.035% | -31.77 € |
| ruptura_volumen_evento | 898.50 € (-2.78%) | 92 | 2 | 12% | -0.434% | -1.221% | -1.346% | -25.69 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 04:15 | ruptura_volumen_evento | BNB | timeout | +0.27% | -0.23% | -0.05 |
| 2026-09-30 04:15 | macd_momentum_evento | QNT | stop-loss | -1.58% | -2.08% | -0.47 |
| 2026-09-30 04:15 | c_banda_atr_evento | SPX | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 04:15 | ruptura_volumen_regimen | BNB | timeout | +0.27% | -0.23% | -0.05 |
| 2026-09-30 04:15 | ruptura_volumen_tope | BNB | timeout | +0.27% | -0.23% | -0.05 |
| 2026-09-30 04:15 | macd_sin_salida | QNT | stop-loss | -1.58% | -2.08% | -0.47 |
| 2026-09-30 04:15 | ruptura_estricta | SUI | timeout | -1.12% | -1.62% | -0.37 |
| 2026-09-30 04:15 | macd_momentum | QNT | stop-loss | -1.58% | -2.08% | -0.46 |
| 2026-09-30 04:15 | ruptura_volumen | BNB | timeout | +0.27% | -0.23% | -0.05 |
| 2026-09-30 04:15 | c_banda_atr | SPX | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 04:10 | ruptura_volumen_evento | TON | timeout | +0.46% | -0.04% | -0.01 |
| 2026-09-30 04:10 | ruptura_volumen_evento | SOL | timeout | -0.36% | -0.86% | -0.19 |
| 2026-09-30 04:10 | ruptura_volumen_regimen | TON | timeout | +0.46% | -0.04% | -0.01 |
| 2026-09-30 04:10 | ruptura_volumen_regimen | SOL | timeout | -0.36% | -0.86% | -0.19 |
| 2026-09-30 04:10 | ruptura_volumen_tope | SOL | timeout | -0.36% | -0.86% | -0.20 |

## Eventos de la última vuelta

- 2026-09-30 04:15 [macd_momentum] CIERRE QNT stop-loss bruto -1.58% neto -2.08%
- 2026-09-30 04:15 [macd_sin_salida] CIERRE QNT stop-loss bruto -1.58% neto -2.08%
- 2026-09-30 04:15 [macd_momentum_evento] CIERRE QNT stop-loss bruto -1.58% neto -2.08%
- 2026-09-30 04:15 [ruptura_estricta] CIERRE SUI timeout bruto -1.12% neto -1.62%
- 2026-09-30 04:10 [ruptura_volumen] ENTRADA XDC @ 0.02954 (22.33 €, apertura)
- 2026-09-30 04:10 [ruptura_volumen_tope] ENTRADA XDC @ 0.02954 (22.75 €, apertura)
- 2026-09-30 04:10 [ruptura_volumen_evento] ENTRADA XDC @ 0.02954 (22.47 €, apertura)
- 2026-09-30 04:10 [macd_momentum] ENTRADA DOT @ 1.0656 (22.00 €, apertura)
- 2026-09-30 04:10 [macd_momentum_evento] ENTRADA DOT @ 1.0656 (22.31 €, apertura)
- 2026-09-30 04:10 [c_banda_atr] ENTRADA CRV @ 0.34283 (22.45 €, apertura)
- 2026-09-30 04:10 [macd_momentum] ENTRADA CRV @ 0.34283 (22.00 €, apertura)
- 2026-09-30 04:10 [macd_sin_salida] ENTRADA CRV @ 0.34283 (22.32 €, apertura)
- 2026-09-30 04:10 [c_banda_atr_evento] ENTRADA CRV @ 0.34283 (22.52 €, apertura)
- 2026-09-30 04:10 [macd_momentum_evento] ENTRADA CRV @ 0.34283 (22.31 €, apertura)
- 2026-09-30 04:10 [c_banda_atr] ENTRADA DASH @ 53.734 (22.45 €, apertura)
- 2026-09-30 04:10 [c_banda_atr_evento] ENTRADA DASH @ 53.734 (22.52 €, apertura)
- 2026-09-30 04:10 [macd_momentum] ENTRADA RENDER @ 1.707 (22.00 €, apertura)
- 2026-09-30 04:10 [macd_sin_salida] ENTRADA RENDER @ 1.707 (22.32 €, apertura)
- 2026-09-30 04:10 [macd_momentum_evento] ENTRADA RENDER @ 1.707 (22.31 €, apertura)
- 2026-09-30 04:10 [macd_momentum] ENTRADA SHIB @ 5.08e-06 (22.00 €, apertura)
- 2026-09-30 04:10 [macd_sin_salida] ENTRADA SHIB @ 5.08e-06 (22.32 €, apertura)
- 2026-09-30 04:10 [macd_momentum_evento] ENTRADA SHIB @ 5.08e-06 (22.31 €, apertura)
- 2026-09-30 04:15 [ruptura_volumen] CIERRE BNB timeout bruto +0.27% neto -0.23%
- 2026-09-30 04:15 [ruptura_volumen_tope] CIERRE BNB timeout bruto +0.27% neto -0.23%
- 2026-09-30 04:15 [ruptura_volumen_regimen] CIERRE BNB timeout bruto +0.27% neto -0.23%
- 2026-09-30 04:15 [ruptura_volumen_evento] CIERRE BNB timeout bruto +0.27% neto -0.23%
- 2026-09-30 04:10 [macd_momentum] ENTRADA ASTER @ 0.65888 (22.00 €, apertura)
- 2026-09-30 04:10 [macd_sin_salida] ENTRADA ASTER @ 0.65888 (22.32 €, apertura)
- 2026-09-30 04:10 [macd_momentum_evento] ENTRADA ASTER @ 0.65888 (22.31 €, apertura)
- 2026-09-30 04:15 [c_banda_atr] CIERRE SPX take-profit bruto +2.00% neto +1.50%
- 2026-09-30 04:15 [c_banda_atr_evento] CIERRE SPX take-profit bruto +2.00% neto +1.50%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
