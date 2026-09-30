# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 06:46 UTC · vueltas 228 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 892.54 € (-3.43%) | 131 | 22 | 27% | -0.278% | -0.978% | -1.110% | -29.28 € |
| reversion_bb | 915.71 € (-0.92%) | 35 | 10 | 46% | +0.183% | -0.917% | -1.027% | -7.39 € |
| ruptura_volumen | 887.23 € (-4.00%) | 167 | 10 | 18% | -0.287% | -0.943% | -1.070% | -35.81 € |
| rebote_extremo | 922.91 € (-0.14%) | 8 | 1 | 50% | +0.378% | -0.722% | -0.879% | -1.33 € |
| pullback_tendencia | 903.76 € (-2.22%) | 117 | 2 | 25% | -0.059% | -0.782% | -0.908% | -20.94 € |
| macd_momentum | 874.77 € (-5.35%) | 320 | 1 | 16% | -0.105% | -0.687% | -0.797% | -49.59 € |
| estocastico_rebote | 887.15 € (-4.01%) | 214 | 7 | 34% | -0.129% | -0.751% | -0.883% | -36.59 € |
| ruptura_estricta | 902.52 € (-2.35%) | 71 | 9 | 23% | -0.397% | -1.264% | -1.406% | -20.58 € |
| macd_sin_salida | 888.69 € (-3.85%) | 183 | 25 | 28% | -0.149% | -0.792% | -0.919% | -32.99 € |
| c_banda_atr_tope | 909.41 € (-1.60%) | 40 | 1 | 18% | -0.507% | -1.607% | -1.736% | -14.76 € |
| ruptura_volumen_tope | 908.82 € (-1.67%) | 61 | 2 | 16% | -0.181% | -1.114% | -1.234% | -15.59 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.963% | -38.90 € |
| ruptura_volumen_regimen | 896.10 € (-3.05%) | 120 | 6 | 18% | -0.275% | -0.992% | -1.121% | -27.17 € |
| c_banda_atr_evento | 895.59 € (-3.10%) | 99 | 22 | 23% | -0.391% | -1.158% | -1.291% | -26.23 € |
| macd_momentum_evento | 887.06 € (-4.02%) | 200 | 1 | 13% | -0.189% | -0.821% | -0.927% | -37.29 € |
| ruptura_volumen_evento | 892.69 € (-3.41%) | 108 | 10 | 10% | -0.487% | -1.232% | -1.359% | -30.33 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 06:45 | ruptura_volumen_evento | ICP | stop-loss | -1.71% | -2.21% | -0.50 |
| 2026-09-30 06:45 | ruptura_volumen_evento | ONDO | timeout | -0.75% | -1.25% | -0.28 |
| 2026-09-30 06:45 | c_banda_atr_evento | LINK | timeout | -1.18% | -1.68% | -0.38 |
| 2026-09-30 06:45 | c_banda_atr_tope | LINK | timeout | -1.18% | -2.28% | -0.52 |
| 2026-09-30 06:45 | ruptura_estricta | TON | timeout | -1.37% | -1.87% | -0.42 |
| 2026-09-30 06:45 | rebote_extremo | NIGHT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 06:45 | ruptura_volumen | ICP | stop-loss | -1.71% | -2.21% | -0.49 |
| 2026-09-30 06:45 | ruptura_volumen | ONDO | timeout | -0.75% | -1.25% | -0.28 |
| 2026-09-30 06:45 | c_banda_atr | LINK | timeout | -1.18% | -1.68% | -0.38 |
| 2026-09-30 06:40 | c_banda_atr_evento | TRUMP | stop-loss | -1.76% | -2.26% | -0.51 |
| 2026-09-30 06:40 | ruptura_volumen_regimen | MON | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 06:40 | macd_sin_salida | SEI | timeout | +0.09% | -0.41% | -0.09 |
| 2026-09-30 06:40 | estocastico_rebote | BNB | timeout | -0.40% | -0.90% | -0.20 |
| 2026-09-30 06:40 | estocastico_rebote | PUMP | timeout | -0.87% | -1.37% | -0.30 |
| 2026-09-30 06:40 | pullback_tendencia | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-30 06:40 [estocastico_rebote] ENTRADA XRP @ 1.31816 (22.19 €, apertura)
- 2026-09-30 06:45 [c_banda_atr] CIERRE LINK timeout bruto -1.18% neto -1.68%
- 2026-09-30 06:45 [c_banda_atr_tope] CIERRE LINK timeout bruto -1.18% neto -2.28%
- 2026-09-30 06:45 [c_banda_atr_evento] CIERRE LINK timeout bruto -1.18% neto -1.68%
- 2026-09-30 06:45 [ruptura_volumen] CIERRE ONDO timeout bruto -0.75% neto -1.25%
- 2026-09-30 06:45 [ruptura_volumen_evento] CIERRE ONDO timeout bruto -0.75% neto -1.25%
- 2026-09-30 06:40 [rebote_extremo] ENTRADA JUP @ 0.28341 (23.07 €, apertura)
- 2026-09-30 06:45 [ruptura_volumen] CIERRE ICP stop-loss bruto -1.71% neto -2.21%
- 2026-09-30 06:45 [ruptura_volumen_evento] CIERRE ICP stop-loss bruto -1.71% neto -2.21%
- 2026-09-30 06:45 [rebote_extremo] CIERRE NIGHT take-profit bruto +2.00% neto +0.90%
- 2026-09-30 06:45 [ruptura_estricta] CIERRE TON timeout bruto -1.37% neto -1.87%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
