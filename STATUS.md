# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 23:26 UTC · vueltas 165 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.31 € (-1.94%) | 69 | 33 | 32% | -0.173% | -1.051% | -1.197% | -16.70 € |
| reversion_bb | 918.05 € (-0.67%) | 18 | 4 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 902.47 € (-2.36%) | 111 | 10 | 23% | -0.114% | -0.849% | -0.977% | -21.59 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.79 € (-2.00%) | 86 | 3 | 23% | -0.156% | -0.959% | -1.081% | -18.91 € |
| macd_momentum | 890.22 € (-3.68%) | 200 | 30 | 17% | -0.104% | -0.735% | -0.851% | -33.47 € |
| estocastico_rebote | 893.87 € (-3.29%) | 162 | 9 | 33% | -0.168% | -0.830% | -0.950% | -30.73 € |
| ruptura_estricta | 909.89 € (-1.55%) | 48 | 9 | 27% | -0.269% | -1.312% | -1.445% | -14.49 € |
| macd_sin_salida | 901.96 € (-2.41%) | 114 | 31 | 31% | -0.098% | -0.827% | -0.957% | -21.59 € |
| c_banda_atr_tope | 913.26 € (-1.19%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 915.15 € (-0.98%) | 36 | 5 | 17% | +0.001% | -1.099% | -1.219% | -9.11 € |
| c_banda_atr_regimen | 907.16 € (-1.85%) | 53 | 23 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 892.85 € (-3.40%) | 173 | 20 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 904.94 € (-2.09%) | 93 | 7 | 23% | -0.110% | -0.891% | -1.020% | -19.00 € |
| c_banda_atr_evento | 910.65 € (-1.47%) | 37 | 33 | 27% | -0.382% | -1.450% | -1.610% | -12.35 € |
| macd_momentum_evento | 902.73 € (-2.33%) | 80 | 30 | 10% | -0.311% | -1.141% | -1.257% | -20.94 € |
| ruptura_volumen_evento | 908.03 € (-1.75%) | 52 | 10 | 13% | -0.333% | -1.341% | -1.472% | -16.03 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 23:25 | ruptura_volumen_evento | ZRO | stop-loss | -1.33% | -1.83% | -0.42 |
| 2026-09-29 23:25 | ruptura_volumen_regimen | ZRO | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-09-29 23:25 | macd_sin_salida | POL | timeout | -0.01% | -0.51% | -0.12 |
| 2026-09-29 23:25 | macd_sin_salida | FIL | timeout | -0.73% | -1.23% | -0.28 |
| 2026-09-29 23:25 | macd_sin_salida | WLD | stop-loss | -1.58% | -2.08% | -0.47 |
| 2026-09-29 23:25 | macd_sin_salida | TRX | timeout | -0.09% | -0.59% | -0.13 |
| 2026-09-29 23:25 | macd_sin_salida | LTC | timeout | -1.00% | -1.50% | -0.34 |
| 2026-09-29 23:25 | macd_sin_salida | ADA | timeout | +0.18% | -0.32% | -0.07 |
| 2026-09-29 23:25 | ruptura_volumen | ZRO | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-09-29 23:20 | macd_sin_salida | SPX | timeout | +0.49% | -0.01% | -0.00 |
| 2026-09-29 23:15 | ruptura_estricta | AVAX | timeout | +0.42% | -0.08% | -0.02 |
| 2026-09-29 23:10 | c_banda_atr_evento | RAY | take-profit | +2.54% | +2.04% | +0.47 |
| 2026-09-29 23:10 | ruptura_volumen_tope | ZRO | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 23:10 | macd_sin_salida | AVAX | timeout | +0.85% | +0.35% | +0.08 |
| 2026-09-29 23:10 | estocastico_rebote | TRUMP | timeout | +0.56% | +0.06% | +0.01 |

## Eventos de la última vuelta

- 2026-09-29 23:25 [macd_sin_salida] CIERRE ADA timeout bruto +0.18% neto -0.32%
- 2026-09-29 23:25 [macd_sin_salida] CIERRE LTC timeout bruto -1.01% neto -1.51%
- 2026-09-29 23:25 [macd_sin_salida] CIERRE TRX timeout bruto -0.09% neto -0.59%
- 2026-09-29 23:25 [macd_sin_salida] CIERRE WLD stop-loss bruto -1.58% neto -2.08%
- 2026-09-29 23:25 [ruptura_volumen] CIERRE ZRO stop-loss bruto -1.33% neto -1.83%
- 2026-09-29 23:25 [ruptura_volumen_regimen] CIERRE ZRO stop-loss bruto -1.33% neto -1.83%
- 2026-09-29 23:25 [ruptura_volumen_evento] CIERRE ZRO stop-loss bruto -1.33% neto -1.83%
- 2026-09-29 23:25 [macd_sin_salida] CIERRE FIL timeout bruto -0.73% neto -1.23%
- 2026-09-29 23:20 [macd_momentum] ENTRADA POL @ 0.10424 (22.27 €, apertura)
- 2026-09-29 23:25 [macd_sin_salida] CIERRE POL timeout bruto -0.01% neto -0.51%
- 2026-09-29 23:20 [macd_momentum_regimen] ENTRADA POL @ 0.10424 (22.34 €, apertura)
- 2026-09-29 23:20 [macd_momentum_evento] ENTRADA POL @ 0.10424 (22.58 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
