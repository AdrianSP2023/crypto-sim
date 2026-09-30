# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 07:47 UTC · vueltas 179 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 895.02 € (-3.16%) | 139 | 30 | 26% | -0.307% | -0.995% | -1.125% | -31.59 € |
| reversion_bb | 915.29 € (-0.97%) | 39 | 7 | 41% | +0.017% | -1.083% | -1.197% | -9.72 € |
| ruptura_volumen | 885.49 € (-4.19%) | 177 | 7 | 17% | -0.330% | -0.977% | -1.108% | -39.24 € |
| rebote_extremo | 923.54 € (-0.08%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.889% | -1.33 € |
| pullback_tendencia | 902.73 € (-2.33%) | 119 | 1 | 24% | -0.072% | -0.791% | -0.918% | -21.55 € |
| macd_momentum | 875.83 € (-5.24%) | 323 | 16 | 16% | -0.103% | -0.684% | -0.795% | -49.85 € |
| estocastico_rebote | 888.24 € (-3.90%) | 220 | 13 | 34% | -0.128% | -0.747% | -0.880% | -37.42 € |
| ruptura_estricta | 901.71 € (-2.44%) | 78 | 5 | 22% | -0.442% | -1.277% | -1.425% | -22.80 € |
| macd_sin_salida | 887.84 € (-3.94%) | 199 | 23 | 27% | -0.210% | -0.841% | -0.965% | -38.01 € |
| c_banda_atr_tope | 910.16 € (-1.52%) | 41 | 5 | 17% | -0.500% | -1.600% | -1.727% | -15.06 € |
| ruptura_volumen_tope | 908.44 € (-1.71%) | 63 | 5 | 16% | -0.208% | -1.127% | -1.250% | -16.28 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 895.18 € (-3.14%) | 126 | 0 | 17% | -0.305% | -1.012% | -1.143% | -29.06 € |
| c_banda_atr_evento | 898.07 € (-2.83%) | 107 | 30 | 22% | -0.420% | -1.167% | -1.297% | -28.54 € |
| macd_momentum_evento | 888.14 € (-3.91%) | 203 | 16 | 13% | -0.184% | -0.814% | -0.922% | -37.55 € |
| ruptura_volumen_evento | 890.94 € (-3.60%) | 118 | 7 | 9% | -0.534% | -1.257% | -1.391% | -33.78 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 07:45 | c_banda_atr_evento | KAS | timeout | +1.23% | +0.73% | +0.16 |
| 2026-09-30 07:45 | ruptura_volumen_regimen | TRX | timeout | +0.04% | -0.46% | -0.10 |
| 2026-09-30 07:45 | ruptura_estricta | XDC | timeout | +1.08% | +0.58% | +0.13 |
| 2026-09-30 07:45 | estocastico_rebote | QNT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-09-30 07:45 | c_banda_atr | KAS | timeout | +1.23% | +0.73% | +0.16 |
| 2026-09-30 07:40 | ruptura_volumen_regimen | XRP | timeout | -0.13% | -0.63% | -0.14 |
| 2026-09-30 07:40 | estocastico_rebote | ASTER | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 07:40 | estocastico_rebote | ICP | take-profit | +1.84% | +1.34% | +0.30 |
| 2026-09-30 07:35 | ruptura_volumen_evento | XRP | timeout | -0.36% | -0.86% | -0.19 |
| 2026-09-30 07:35 | ruptura_estricta | TRX | timeout | +0.27% | -0.23% | -0.05 |
| 2026-09-30 07:35 | ruptura_volumen | XRP | timeout | -0.36% | -0.86% | -0.19 |
| 2026-09-30 07:30 | ruptura_volumen_evento | BCH | timeout | -0.24% | -0.74% | -0.17 |
| 2026-09-30 07:30 | macd_momentum_evento | XDC | momentum perdido | +0.37% | -0.13% | -0.03 |
| 2026-09-30 07:30 | macd_momentum | XDC | momentum perdido | +0.37% | -0.13% | -0.03 |
| 2026-09-30 07:30 | ruptura_volumen | BCH | timeout | -0.24% | -0.74% | -0.16 |

## Eventos de la última vuelta

- 2026-09-30 07:45 [estocastico_rebote] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 07:40 [ruptura_volumen] ENTRADA NEAR @ 4.4324 (22.13 €, apertura)
- 2026-09-30 07:40 [ruptura_estricta] ENTRADA NEAR @ 4.4324 (22.53 €, apertura)
- 2026-09-30 07:40 [ruptura_volumen_tope] ENTRADA NEAR @ 4.4324 (22.70 €, apertura)
- 2026-09-30 07:40 [ruptura_volumen_evento] ENTRADA NEAR @ 4.4324 (22.26 €, apertura)
- 2026-09-30 07:40 [ruptura_volumen] ENTRADA XLM @ 0.197936 (22.13 €, apertura)
- 2026-09-30 07:40 [ruptura_estricta] ENTRADA XLM @ 0.197936 (22.53 €, apertura)
- 2026-09-30 07:40 [ruptura_volumen_evento] ENTRADA XLM @ 0.197936 (22.26 €, apertura)
- 2026-09-30 07:45 [ruptura_estricta] CIERRE XDC timeout bruto +1.08% neto +0.58%
- 2026-09-30 07:45 [ruptura_volumen_regimen] CIERRE TRX timeout bruto +0.04% neto -0.46%
- 2026-09-30 07:40 [ruptura_volumen] ENTRADA WLD @ 0.4414 (22.13 €, apertura)
- 2026-09-30 07:40 [macd_momentum] ENTRADA WLD @ 0.4414 (21.86 €, apertura)
- 2026-09-30 07:40 [macd_sin_salida] ENTRADA WLD @ 0.4414 (22.16 €, apertura)
- 2026-09-30 07:40 [macd_momentum_evento] ENTRADA WLD @ 0.4414 (22.17 €, apertura)
- 2026-09-30 07:40 [ruptura_volumen_evento] ENTRADA WLD @ 0.4414 (22.26 €, apertura)
- 2026-09-30 07:40 [macd_momentum] ENTRADA PEPE @ 3.795e-06 (21.86 €, apertura)
- 2026-09-30 07:40 [macd_sin_salida] ENTRADA PEPE @ 3.795e-06 (22.16 €, apertura)
- 2026-09-30 07:40 [macd_momentum_evento] ENTRADA PEPE @ 3.795e-06 (22.17 €, apertura)
- 2026-09-30 07:40 [c_banda_atr] ENTRADA XPL @ 0.0848 (22.31 €, apertura)
- 2026-09-30 07:40 [macd_momentum] ENTRADA XPL @ 0.0848 (21.86 €, apertura)
- 2026-09-30 07:40 [macd_sin_salida] ENTRADA XPL @ 0.0848 (22.16 €, apertura)
- 2026-09-30 07:40 [c_banda_atr_evento] ENTRADA XPL @ 0.0848 (22.39 €, apertura)
- 2026-09-30 07:40 [macd_momentum_evento] ENTRADA XPL @ 0.0848 (22.17 €, apertura)
- 2026-09-30 07:45 [c_banda_atr] CIERRE KAS timeout bruto +1.23% neto +0.73%
- 2026-09-30 07:40 [macd_momentum] ENTRADA KAS @ 0.03877 (21.86 €, apertura)
- 2026-09-30 07:45 [c_banda_atr_evento] CIERRE KAS timeout bruto +1.23% neto +0.73%
- 2026-09-30 07:40 [macd_momentum_evento] ENTRADA KAS @ 0.03877 (22.17 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
