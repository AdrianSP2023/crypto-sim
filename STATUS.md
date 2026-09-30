# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 08:02 UTC · vueltas 182 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 894.16 € (-3.25%) | 140 | 29 | 26% | -0.291% | -0.977% | -1.108% | -31.25 € |
| reversion_bb | 915.31 € (-0.97%) | 39 | 7 | 41% | +0.017% | -1.083% | -1.197% | -9.72 € |
| ruptura_volumen | 885.44 € (-4.20%) | 177 | 13 | 17% | -0.330% | -0.977% | -1.108% | -39.24 € |
| rebote_extremo | 923.43 € (-0.09%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.889% | -1.33 € |
| pullback_tendencia | 902.67 € (-2.33%) | 119 | 2 | 24% | -0.072% | -0.791% | -0.918% | -21.55 € |
| macd_momentum | 875.34 € (-5.29%) | 324 | 17 | 16% | -0.097% | -0.677% | -0.788% | -49.52 € |
| estocastico_rebote | 888.18 € (-3.90%) | 220 | 14 | 34% | -0.128% | -0.747% | -0.880% | -37.42 € |
| ruptura_estricta | 901.48 € (-2.46%) | 78 | 7 | 22% | -0.442% | -1.277% | -1.425% | -22.80 € |
| macd_sin_salida | 887.47 € (-3.98%) | 200 | 24 | 27% | -0.199% | -0.829% | -0.954% | -37.68 € |
| c_banda_atr_tope | 910.08 € (-1.53%) | 42 | 4 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.49 € (-1.70%) | 63 | 5 | 16% | -0.208% | -1.127% | -1.250% | -16.28 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 895.09 € (-3.15%) | 126 | 6 | 17% | -0.305% | -1.012% | -1.143% | -29.06 € |
| c_banda_atr_evento | 897.21 € (-2.92%) | 108 | 29 | 23% | -0.398% | -1.142% | -1.273% | -28.20 € |
| macd_momentum_evento | 887.65 € (-3.96%) | 204 | 17 | 13% | -0.174% | -0.803% | -0.911% | -37.21 € |
| ruptura_volumen_evento | 890.90 € (-3.61%) | 118 | 13 | 9% | -0.534% | -1.257% | -1.391% | -33.78 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 07:55 | macd_momentum_evento | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 07:55 | c_banda_atr_evento | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 07:55 | c_banda_atr_tope | MON | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-30 07:55 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 07:55 | macd_momentum | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 07:55 | c_banda_atr | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 07:45 | c_banda_atr_evento | KAS | timeout | +1.23% | +0.73% | +0.16 |
| 2026-09-30 07:45 | ruptura_volumen_regimen | TRX | timeout | +0.04% | -0.46% | -0.10 |
| 2026-09-30 07:45 | ruptura_estricta | XDC | timeout | +1.08% | +0.58% | +0.13 |
| 2026-09-30 07:45 | estocastico_rebote | QNT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-09-30 07:45 | c_banda_atr | KAS | timeout | +1.23% | +0.73% | +0.16 |
| 2026-09-30 07:40 | ruptura_volumen_regimen | XRP | timeout | -0.13% | -0.63% | -0.14 |
| 2026-09-30 07:40 | estocastico_rebote | ASTER | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 07:40 | estocastico_rebote | ICP | take-profit | +1.84% | +1.34% | +0.30 |
| 2026-09-30 07:35 | ruptura_volumen_evento | XRP | timeout | -0.36% | -0.86% | -0.19 |

## Eventos de la última vuelta

- 2026-09-30 07:55 [ruptura_volumen] ENTRADA ZEC @ 1245 (22.13 €, apertura)
- 2026-09-30 07:55 [ruptura_volumen_regimen] ENTRADA ZEC @ 1245 (22.38 €, apertura)
- 2026-09-30 07:55 [ruptura_volumen_evento] ENTRADA ZEC @ 1245 (22.26 €, apertura)
- 2026-09-30 07:55 [ruptura_volumen] ENTRADA MON @ 0.02404 (22.13 €, apertura)
- 2026-09-30 07:55 [ruptura_estricta] ENTRADA MON @ 0.02404 (22.54 €, apertura)
- 2026-09-30 07:55 [ruptura_volumen_regimen] ENTRADA MON @ 0.02404 (22.38 €, apertura)
- 2026-09-30 07:55 [ruptura_volumen_evento] ENTRADA MON @ 0.02404 (22.26 €, apertura)
- 2026-09-30 07:55 [ruptura_volumen] ENTRADA PENGU @ 0.008691 (22.13 €, apertura)
- 2026-09-30 07:55 [ruptura_volumen_regimen] ENTRADA PENGU @ 0.008691 (22.38 €, apertura)
- 2026-09-30 07:55 [ruptura_volumen_evento] ENTRADA PENGU @ 0.008691 (22.26 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
