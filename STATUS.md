# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 07:37 UTC · vueltas 177 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.91 € (-3.50%) | 138 | 30 | 25% | -0.319% | -1.008% | -1.138% | -31.75 € |
| reversion_bb | 914.74 € (-1.03%) | 39 | 7 | 41% | +0.017% | -1.083% | -1.197% | -9.72 € |
| ruptura_volumen | 884.74 € (-4.27%) | 177 | 3 | 17% | -0.330% | -0.977% | -1.108% | -39.24 € |
| rebote_extremo | 923.26 € (-0.11%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.889% | -1.33 € |
| pullback_tendencia | 902.71 € (-2.33%) | 119 | 1 | 24% | -0.072% | -0.791% | -0.918% | -21.55 € |
| macd_momentum | 874.66 € (-5.36%) | 323 | 12 | 16% | -0.103% | -0.684% | -0.795% | -49.85 € |
| estocastico_rebote | 887.44 € (-3.98%) | 217 | 15 | 34% | -0.140% | -0.760% | -0.894% | -37.56 € |
| ruptura_estricta | 901.14 € (-2.50%) | 77 | 4 | 21% | -0.462% | -1.301% | -1.448% | -22.93 € |
| macd_sin_salida | 886.20 € (-4.12%) | 199 | 20 | 27% | -0.210% | -0.841% | -0.965% | -38.01 € |
| c_banda_atr_tope | 909.60 € (-1.58%) | 41 | 5 | 17% | -0.500% | -1.600% | -1.727% | -15.06 € |
| ruptura_volumen_tope | 907.68 € (-1.79%) | 63 | 3 | 16% | -0.208% | -1.127% | -1.250% | -16.28 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 895.35 € (-3.13%) | 124 | 2 | 17% | -0.309% | -1.019% | -1.152% | -28.81 € |
| c_banda_atr_evento | 894.95 € (-3.17%) | 106 | 30 | 22% | -0.436% | -1.185% | -1.315% | -28.71 € |
| macd_momentum_evento | 886.96 € (-4.03%) | 203 | 12 | 13% | -0.184% | -0.814% | -0.922% | -37.55 € |
| ruptura_volumen_evento | 890.19 € (-3.68%) | 118 | 3 | 9% | -0.534% | -1.257% | -1.391% | -33.78 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-30 07:20 | macd_sin_salida | SOL | timeout | -1.00% | -1.50% | -0.33 |
| 2026-09-30 07:15 | ruptura_volumen_evento | XLM | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 07:15 | ruptura_volumen_regimen | WLD | stop-loss | -1.20% | -1.70% | -0.38 |

## Eventos de la última vuelta

- 2026-09-30 07:35 [ruptura_volumen] CIERRE XRP timeout bruto -0.36% neto -0.86%
- 2026-09-30 07:30 [macd_momentum] ENTRADA XRP @ 1.32161 (21.86 €, apertura)
- 2026-09-30 07:30 [macd_sin_salida] ENTRADA XRP @ 1.32161 (22.16 €, apertura)
- 2026-09-30 07:30 [macd_momentum_evento] ENTRADA XRP @ 1.32161 (22.17 €, apertura)
- 2026-09-30 07:35 [ruptura_volumen_evento] CIERRE XRP timeout bruto -0.36% neto -0.86%
- 2026-09-30 07:30 [c_banda_atr] ENTRADA JUP @ 0.28552 (22.31 €, apertura)
- 2026-09-30 07:30 [c_banda_atr_evento] ENTRADA JUP @ 0.28552 (22.39 €, apertura)
- 2026-09-30 07:30 [c_banda_atr] ENTRADA ICP @ 3.029 (22.31 €, apertura)
- 2026-09-30 07:30 [macd_momentum] ENTRADA ICP @ 3.029 (21.86 €, apertura)
- 2026-09-30 07:30 [macd_sin_salida] ENTRADA ICP @ 3.029 (22.16 €, apertura)
- 2026-09-30 07:30 [c_banda_atr_evento] ENTRADA ICP @ 3.029 (22.39 €, apertura)
- 2026-09-30 07:30 [macd_momentum_evento] ENTRADA ICP @ 3.029 (22.17 €, apertura)
- 2026-09-30 07:30 [macd_momentum] ENTRADA TRX @ 0.2975 (21.86 €, apertura)
- 2026-09-30 07:35 [ruptura_estricta] CIERRE TRX timeout bruto +0.27% neto -0.23%
- 2026-09-30 07:30 [macd_momentum_evento] ENTRADA TRX @ 0.2975 (22.17 €, apertura)
- 2026-09-30 07:30 [macd_momentum] ENTRADA RAY @ 1.656 (21.86 €, apertura)
- 2026-09-30 07:30 [macd_sin_salida] ENTRADA RAY @ 1.656 (22.16 €, apertura)
- 2026-09-30 07:30 [macd_momentum_evento] ENTRADA RAY @ 1.656 (22.17 €, apertura)
- 2026-09-30 07:30 [macd_momentum] ENTRADA SHIB @ 5.078e-06 (21.86 €, apertura)
- 2026-09-30 07:30 [macd_sin_salida] ENTRADA SHIB @ 5.078e-06 (22.16 €, apertura)
- 2026-09-30 07:30 [macd_momentum_evento] ENTRADA SHIB @ 5.078e-06 (22.17 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
