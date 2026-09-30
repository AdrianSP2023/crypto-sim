# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 04:21 UTC · vueltas 199 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.30 € (-2.81%) | 114 | 22 | 27% | -0.265% | -0.994% | -1.128% | -25.96 € |
| reversion_bb | 918.39 € (-0.63%) | 31 | 8 | 48% | +0.189% | -0.911% | -1.015% | -6.51 € |
| ruptura_volumen | 893.04 € (-3.38%) | 151 | 4 | 20% | -0.234% | -0.907% | -1.032% | -31.19 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.27 € (-2.05%) | 109 | 1 | 26% | -0.034% | -0.773% | -0.900% | -19.31 € |
| macd_momentum | 880.93 € (-4.69%) | 271 | 19 | 17% | -0.123% | -0.720% | -0.834% | -44.14 € |
| estocastico_rebote | 891.71 € (-3.52%) | 191 | 18 | 34% | -0.133% | -0.770% | -0.902% | -33.57 € |
| ruptura_estricta | 904.99 € (-2.08%) | 66 | 6 | 24% | -0.359% | -1.255% | -1.397% | -19.00 € |
| macd_sin_salida | 893.85 € (-3.29%) | 167 | 21 | 28% | -0.160% | -0.817% | -0.942% | -31.09 € |
| c_banda_atr_tope | 910.66 € (-1.47%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.23 € (-1.52%) | 54 | 5 | 17% | -0.149% | -1.138% | -1.257% | -14.11 € |
| c_banda_atr_regimen | 900.77 € (-2.54%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 898.84 € (-2.75%) | 116 | 0 | 18% | -0.234% | -0.959% | -1.087% | -25.40 € |
| c_banda_atr_evento | 901.36 € (-2.48%) | 82 | 22 | 23% | -0.396% | -1.217% | -1.354% | -22.90 € |
| macd_momentum_evento | 893.31 € (-3.35%) | 151 | 19 | 13% | -0.248% | -0.923% | -1.035% | -31.77 € |
| ruptura_volumen_evento | 898.54 € (-2.78%) | 92 | 4 | 12% | -0.434% | -1.221% | -1.346% | -25.69 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 04:20 | macd_sin_salida | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 04:20 | reversion_bb | ICP | take-profit | +1.76% | +0.66% | +0.15 |
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

## Eventos de la última vuelta

- 2026-09-30 04:15 [macd_momentum] ENTRADA XRP @ 1.32003 (22.00 €, apertura)
- 2026-09-30 04:15 [macd_sin_salida] ENTRADA XRP @ 1.32003 (22.32 €, apertura)
- 2026-09-30 04:15 [macd_momentum_evento] ENTRADA XRP @ 1.32003 (22.31 €, apertura)
- 2026-09-30 04:15 [c_banda_atr] ENTRADA NEAR @ 4.3806 (22.46 €, apertura)
- 2026-09-30 04:15 [macd_momentum] ENTRADA NEAR @ 4.3806 (22.00 €, apertura)
- 2026-09-30 04:15 [macd_sin_salida] ENTRADA NEAR @ 4.3806 (22.32 €, apertura)
- 2026-09-30 04:15 [c_banda_atr_evento] ENTRADA NEAR @ 4.3806 (22.53 €, apertura)
- 2026-09-30 04:15 [macd_momentum_evento] ENTRADA NEAR @ 4.3806 (22.31 €, apertura)
- 2026-09-30 04:15 [macd_momentum] ENTRADA ADA @ 0.216576 (22.00 €, apertura)
- 2026-09-30 04:15 [macd_sin_salida] ENTRADA ADA @ 0.216576 (22.32 €, apertura)
- 2026-09-30 04:15 [macd_momentum_evento] ENTRADA ADA @ 0.216576 (22.31 €, apertura)
- 2026-09-30 04:15 [macd_momentum] ENTRADA SUI @ 1.02 (22.00 €, apertura)
- 2026-09-30 04:15 [macd_sin_salida] ENTRADA SUI @ 1.02 (22.32 €, apertura)
- 2026-09-30 04:15 [macd_momentum_evento] ENTRADA SUI @ 1.02 (22.31 €, apertura)
- 2026-09-30 04:15 [macd_momentum] ENTRADA DASH @ 53.734 (22.00 €, apertura)
- 2026-09-30 04:15 [macd_momentum_evento] ENTRADA DASH @ 53.734 (22.31 €, apertura)
- 2026-09-30 04:20 [reversion_bb] CIERRE ICP take-profit bruto +1.76% neto +0.66%
- 2026-09-30 04:20 [macd_sin_salida] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-30 04:15 [macd_momentum] ENTRADA PEPE @ 3.776e-06 (22.00 €, apertura)
- 2026-09-30 04:15 [macd_sin_salida] ENTRADA PEPE @ 3.776e-06 (22.33 €, apertura)
- 2026-09-30 04:15 [macd_momentum_evento] ENTRADA PEPE @ 3.776e-06 (22.31 €, apertura)
- 2026-09-30 04:15 [c_banda_atr] ENTRADA POL @ 0.1035 (22.46 €, apertura)
- 2026-09-30 04:15 [c_banda_atr_evento] ENTRADA POL @ 0.1035 (22.53 €, apertura)
- 2026-09-30 04:15 [ruptura_volumen] ENTRADA KAS @ 0.03867 (22.33 €, apertura)
- 2026-09-30 04:15 [ruptura_estricta] ENTRADA KAS @ 0.03867 (22.63 €, apertura)
- 2026-09-30 04:15 [ruptura_volumen_tope] ENTRADA KAS @ 0.03867 (22.75 €, apertura)
- 2026-09-30 04:15 [ruptura_volumen_evento] ENTRADA KAS @ 0.03867 (22.46 €, apertura)
- 2026-09-30 04:15 [ruptura_volumen] ENTRADA SPX @ 0.3779 (22.33 €, apertura)
- 2026-09-30 04:15 [macd_momentum] ENTRADA SPX @ 0.3779 (22.00 €, apertura)
- 2026-09-30 04:15 [ruptura_estricta] ENTRADA SPX @ 0.3779 (22.63 €, apertura)
- 2026-09-30 04:15 [macd_sin_salida] ENTRADA SPX @ 0.3779 (22.33 €, apertura)
- 2026-09-30 04:15 [ruptura_volumen_tope] ENTRADA SPX @ 0.3779 (22.75 €, apertura)
- 2026-09-30 04:15 [macd_momentum_evento] ENTRADA SPX @ 0.3779 (22.31 €, apertura)
- 2026-09-30 04:15 [ruptura_volumen_evento] ENTRADA SPX @ 0.3779 (22.46 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
