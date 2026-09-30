# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 07:42 UTC · vueltas 178 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 894.12 € (-3.26%) | 138 | 30 | 25% | -0.319% | -1.008% | -1.138% | -31.75 € |
| reversion_bb | 915.30 € (-0.97%) | 39 | 7 | 41% | +0.017% | -1.083% | -1.197% | -9.72 € |
| ruptura_volumen | 885.18 € (-4.23%) | 177 | 4 | 17% | -0.330% | -0.977% | -1.108% | -39.24 € |
| rebote_extremo | 923.43 € (-0.09%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.889% | -1.33 € |
| pullback_tendencia | 902.73 € (-2.33%) | 119 | 1 | 24% | -0.072% | -0.791% | -0.918% | -21.55 € |
| macd_momentum | 875.25 € (-5.30%) | 323 | 12 | 16% | -0.103% | -0.684% | -0.795% | -49.85 € |
| estocastico_rebote | 887.82 € (-3.94%) | 219 | 14 | 34% | -0.122% | -0.741% | -0.874% | -36.97 € |
| ruptura_estricta | 901.61 € (-2.45%) | 77 | 4 | 21% | -0.462% | -1.301% | -1.448% | -22.93 € |
| macd_sin_salida | 887.11 € (-4.02%) | 199 | 20 | 27% | -0.210% | -0.841% | -0.965% | -38.01 € |
| c_banda_atr_tope | 909.94 € (-1.55%) | 41 | 5 | 17% | -0.500% | -1.600% | -1.727% | -15.06 € |
| ruptura_volumen_tope | 908.14 € (-1.74%) | 63 | 4 | 16% | -0.208% | -1.127% | -1.250% | -16.28 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 895.29 € (-3.13%) | 125 | 1 | 17% | -0.307% | -1.016% | -1.148% | -28.96 € |
| c_banda_atr_evento | 897.16 € (-2.93%) | 106 | 30 | 22% | -0.436% | -1.185% | -1.315% | -28.71 € |
| macd_momentum_evento | 887.56 € (-3.97%) | 203 | 12 | 13% | -0.184% | -0.814% | -0.922% | -37.55 € |
| ruptura_volumen_evento | 890.63 € (-3.64%) | 118 | 4 | 9% | -0.534% | -1.257% | -1.391% | -33.78 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-30 07:25 | macd_momentum_evento | KAS | momentum perdido | -0.08% | -0.58% | -0.13 |
| 2026-09-30 07:25 | macd_sin_salida | VIRTUAL | timeout | -0.62% | -1.12% | -0.25 |
| 2026-09-30 07:25 | ruptura_estricta | VIRTUAL | timeout | -0.62% | -1.12% | -0.25 |
| 2026-09-30 07:25 | macd_momentum | KAS | momentum perdido | -0.08% | -0.58% | -0.13 |
| 2026-09-30 07:20 | macd_sin_salida | OP | timeout | -0.70% | -1.20% | -0.27 |

## Eventos de la última vuelta

- 2026-09-30 07:40 [ruptura_volumen_regimen] CIERRE XRP timeout bruto -0.13% neto -0.63%
- 2026-09-30 07:35 [estocastico_rebote] ENTRADA QNT @ 251.8 (22.17 €, apertura)
- 2026-09-30 07:40 [estocastico_rebote] CIERRE ICP take-profit bruto +1.84% neto +1.34%
- 2026-09-30 07:35 [ruptura_volumen] ENTRADA VVV @ 23.788 (22.13 €, apertura)
- 2026-09-30 07:35 [ruptura_volumen_tope] ENTRADA VVV @ 23.788 (22.70 €, apertura)
- 2026-09-30 07:35 [ruptura_volumen_evento] ENTRADA VVV @ 23.788 (22.26 €, apertura)
- 2026-09-30 07:40 [estocastico_rebote] CIERRE ASTER take-profit bruto +1.80% neto +1.30%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
