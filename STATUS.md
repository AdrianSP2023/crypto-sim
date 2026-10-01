# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 20:17 UTC · vueltas 304 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.30 € (-3.67%) | 244 | 27 | 36% | -0.032% | -0.639% | -0.762% | -35.51 € |
| reversion_bb | 917.10 € (-0.77%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 873.55 € (-5.48%) | 287 | 5 | 25% | -0.193% | -0.784% | -0.891% | -50.76 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.45 € (-3.66%) | 175 | 4 | 15% | -0.201% | -0.852% | -0.945% | -33.89 € |
| macd_momentum | 870.63 € (-5.80%) | 439 | 30 | 22% | +0.015% | -0.545% | -0.649% | -53.76 € |
| estocastico_rebote | 878.80 € (-4.92%) | 295 | 24 | 32% | -0.109% | -0.697% | -0.808% | -46.55 € |
| ruptura_estricta | 884.60 € (-4.29%) | 152 | 14 | 25% | -0.452% | -1.126% | -1.243% | -39.01 € |
| macd_sin_salida | 881.40 € (-4.63%) | 309 | 29 | 37% | -0.023% | -0.607% | -0.721% | -42.67 € |
| c_banda_atr_tope | 912.02 € (-1.32%) | 56 | 5 | 30% | +0.019% | -0.953% | -1.068% | -12.26 € |
| ruptura_volumen_tope | 907.77 € (-1.78%) | 93 | 5 | 29% | +0.019% | -0.765% | -0.878% | -16.32 € |
| c_banda_atr_regimen | 901.18 € (-2.49%) | 117 | 21 | 33% | -0.150% | -0.873% | -1.012% | -23.43 € |
| macd_momentum_regimen | 891.36 € (-3.56%) | 239 | 27 | 22% | +0.003% | -0.606% | -0.715% | -32.95 € |
| ruptura_volumen_regimen | 876.40 € (-5.18%) | 221 | 4 | 19% | -0.340% | -0.958% | -1.073% | -47.86 € |
| c_banda_atr_evento | 896.22 € (-3.03%) | 211 | 27 | 36% | +0.011% | -0.614% | -0.731% | -29.59 € |
| macd_momentum_evento | 875.46 € (-5.28%) | 392 | 30 | 20% | +0.013% | -0.554% | -0.654% | -48.94 € |
| ruptura_volumen_evento | 885.98 € (-4.14%) | 237 | 5 | 26% | -0.101% | -0.713% | -0.811% | -38.33 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 20:15 | macd_sin_salida | SPX | timeout | +0.90% | +0.40% | +0.09 |
| 2026-10-01 20:15 | macd_sin_salida | FIL | timeout | +0.78% | +0.28% | +0.06 |
| 2026-10-01 20:15 | macd_sin_salida | DOGE | timeout | +0.27% | -0.23% | -0.05 |
| 2026-10-01 20:15 | estocastico_rebote | AAVE | take-profit | +1.90% | +1.40% | +0.31 |
| 2026-10-01 20:10 | macd_sin_salida | TRUMP | timeout | +0.77% | +0.27% | +0.06 |
| 2026-10-01 20:10 | macd_sin_salida | CRV | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-01 20:10 | macd_sin_salida | LTC | timeout | +1.46% | +0.95% | +0.21 |
| 2026-10-01 20:10 | estocastico_rebote | PEPE | timeout | +0.74% | +0.24% | +0.05 |
| 2026-10-01 20:05 | c_banda_atr_evento | RENDER | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 20:05 | c_banda_atr_regimen | RENDER | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 20:05 | macd_sin_salida | XLM | timeout | +0.27% | -0.23% | -0.05 |
| 2026-10-01 20:05 | macd_sin_salida | SOL | timeout | +0.48% | -0.02% | -0.01 |
| 2026-10-01 20:05 | macd_sin_salida | ETH | timeout | +0.42% | -0.08% | -0.02 |
| 2026-10-01 20:05 | estocastico_rebote | BCH | timeout | +0.41% | -0.09% | -0.02 |
| 2026-10-01 20:05 | estocastico_rebote | TAO | timeout | +0.77% | +0.27% | +0.06 |

## Eventos de la última vuelta

- 2026-10-01 20:10 [macd_momentum] ENTRADA XRP @ 1.33598 (21.76 €, apertura)
- 2026-10-01 20:10 [macd_momentum_regimen] ENTRADA XRP @ 1.33598 (22.28 €, apertura)
- 2026-10-01 20:10 [macd_momentum_evento] ENTRADA XRP @ 1.33598 (21.88 €, apertura)
- 2026-10-01 20:10 [macd_momentum] ENTRADA ETH @ 2402.57 (21.76 €, apertura)
- 2026-10-01 20:10 [macd_sin_salida] ENTRADA ETH @ 2402.57 (22.04 €, apertura)
- 2026-10-01 20:10 [macd_momentum_regimen] ENTRADA ETH @ 2402.57 (22.28 €, apertura)
- 2026-10-01 20:10 [macd_momentum_evento] ENTRADA ETH @ 2402.57 (21.88 €, apertura)
- 2026-10-01 20:10 [macd_momentum] ENTRADA SOL @ 105.25 (21.76 €, apertura)
- 2026-10-01 20:10 [macd_sin_salida] ENTRADA SOL @ 105.25 (22.04 €, apertura)
- 2026-10-01 20:10 [macd_momentum_regimen] ENTRADA SOL @ 105.25 (22.28 €, apertura)
- 2026-10-01 20:10 [macd_momentum_evento] ENTRADA SOL @ 105.25 (21.88 €, apertura)
- 2026-10-01 20:15 [estocastico_rebote] CIERRE AAVE take-profit bruto +1.90% neto +1.40%
- 2026-10-01 20:10 [macd_momentum] ENTRADA XLM @ 0.19563 (21.76 €, apertura)
- 2026-10-01 20:10 [macd_sin_salida] ENTRADA XLM @ 0.19563 (22.04 €, apertura)
- 2026-10-01 20:10 [macd_momentum_regimen] ENTRADA XLM @ 0.19563 (22.28 €, apertura)
- 2026-10-01 20:10 [macd_momentum_evento] ENTRADA XLM @ 0.19563 (21.88 €, apertura)
- 2026-10-01 20:15 [macd_sin_salida] CIERRE DOGE timeout bruto +0.27% neto -0.23%
- 2026-10-01 20:10 [macd_momentum] ENTRADA CRV @ 0.34016 (21.76 €, apertura)
- 2026-10-01 20:10 [macd_momentum_regimen] ENTRADA CRV @ 0.34016 (22.28 €, apertura)
- 2026-10-01 20:10 [macd_momentum_evento] ENTRADA CRV @ 0.34016 (21.88 €, apertura)
- 2026-10-01 20:15 [macd_sin_salida] CIERRE FIL timeout bruto +0.78% neto +0.28%
- 2026-10-01 20:10 [c_banda_atr] ENTRADA DASH @ 52.264 (22.22 €, apertura)
- 2026-10-01 20:10 [macd_momentum] ENTRADA DASH @ 52.264 (21.76 €, apertura)
- 2026-10-01 20:10 [macd_momentum_regimen] ENTRADA DASH @ 52.264 (22.28 €, apertura)
- 2026-10-01 20:10 [c_banda_atr_evento] ENTRADA DASH @ 52.264 (22.37 €, apertura)
- 2026-10-01 20:10 [macd_momentum_evento] ENTRADA DASH @ 52.264 (21.88 €, apertura)
- 2026-10-01 20:10 [macd_momentum] ENTRADA BNB @ 684.3 (21.76 €, apertura)
- 2026-10-01 20:10 [macd_sin_salida] ENTRADA BNB @ 684.3 (22.04 €, apertura)
- 2026-10-01 20:10 [macd_momentum_regimen] ENTRADA BNB @ 684.3 (22.28 €, apertura)
- 2026-10-01 20:10 [macd_momentum_evento] ENTRADA BNB @ 684.3 (21.88 €, apertura)
- 2026-10-01 20:10 [macd_momentum] ENTRADA APT @ 0.6909 (21.76 €, apertura)
- 2026-10-01 20:10 [macd_sin_salida] ENTRADA APT @ 0.6909 (22.04 €, apertura)
- 2026-10-01 20:10 [macd_momentum_regimen] ENTRADA APT @ 0.6909 (22.28 €, apertura)
- 2026-10-01 20:10 [macd_momentum_evento] ENTRADA APT @ 0.6909 (21.88 €, apertura)
- 2026-10-01 20:15 [macd_sin_salida] CIERRE SPX timeout bruto +0.90% neto +0.40%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
