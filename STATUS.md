# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 13:21 UTC · vueltas 227 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 893.17 € (-3.36%) | 191 | 15 | 35% | -0.027% | -0.664% | -0.790% | -28.99 € |
| reversion_bb | 917.84 € (-0.69%) | 28 | 12 | 43% | +0.152% | -0.948% | -1.050% | -6.12 € |
| ruptura_volumen | 882.03 € (-4.57%) | 228 | 5 | 23% | -0.199% | -0.813% | -0.922% | -42.05 € |
| rebote_extremo | 922.29 € (-0.21%) | 10 | 0 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 894.53 € (-3.21%) | 135 | 0 | 14% | -0.271% | -0.966% | -1.072% | -29.72 € |
| macd_momentum | 880.61 € (-4.72%) | 328 | 2 | 21% | -0.009% | -0.589% | -0.698% | -43.68 € |
| estocastico_rebote | 878.21 € (-4.98%) | 266 | 10 | 30% | -0.157% | -0.755% | -0.866% | -45.48 € |
| ruptura_estricta | 886.59 € (-4.07%) | 128 | 7 | 24% | -0.538% | -1.244% | -1.368% | -36.36 € |
| macd_sin_salida | 884.02 € (-4.35%) | 231 | 17 | 35% | -0.115% | -0.728% | -0.844% | -38.36 € |
| c_banda_atr_tope | 912.52 € (-1.27%) | 44 | 3 | 27% | -0.045% | -1.131% | -1.251% | -11.45 € |
| ruptura_volumen_tope | 910.87 € (-1.45%) | 69 | 2 | 28% | +0.056% | -0.827% | -0.941% | -13.11 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 894.06 € (-3.26%) | 205 | 1 | 22% | -0.022% | -0.649% | -0.762% | -30.34 € |
| ruptura_volumen_regimen | 884.17 € (-4.34%) | 183 | 2 | 20% | -0.324% | -0.966% | -1.081% | -40.16 € |
| c_banda_atr_evento | 899.11 € (-2.72%) | 158 | 15 | 36% | +0.032% | -0.635% | -0.755% | -23.03 € |
| macd_momentum_evento | 885.49 € (-4.19%) | 281 | 2 | 19% | -0.016% | -0.609% | -0.714% | -38.80 € |
| ruptura_volumen_evento | 894.58 € (-3.21%) | 178 | 5 | 24% | -0.078% | -0.727% | -0.824% | -29.49 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 13:20 | ruptura_volumen_evento | KSM | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 13:20 | ruptura_volumen_regimen | KAS | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-10-01 13:20 | ruptura_volumen_tope | KSM | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 13:20 | estocastico_rebote | MINA | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 13:20 | estocastico_rebote | ALGO | timeout | -0.26% | -0.76% | -0.17 |
| 2026-10-01 13:20 | estocastico_rebote | UNI | timeout | -0.28% | -0.78% | -0.17 |
| 2026-10-01 13:20 | ruptura_volumen | KSM | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 13:15 | ruptura_volumen_evento | SKY | stop-loss | -1.32% | -1.82% | -0.41 |
| 2026-10-01 13:15 | ruptura_volumen_evento | XDC | timeout | +1.08% | +0.58% | +0.13 |
| 2026-10-01 13:15 | macd_momentum_evento | ALGO | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-10-01 13:15 | c_banda_atr_evento | SKY | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 13:15 | c_banda_atr_evento | DASH | stop-loss | -1.58% | -2.08% | -0.47 |
| 2026-10-01 13:15 | macd_momentum_regimen | ALGO | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-10-01 13:15 | c_banda_atr_regimen | VVV | stop-loss | -1.53% | -2.03% | -0.46 |
| 2026-10-01 13:15 | macd_sin_salida | WLD | stop-loss | -1.65% | -2.15% | -0.48 |

## Eventos de la última vuelta

- 2026-10-01 13:20 [estocastico_rebote] CIERRE UNI timeout bruto -0.28% neto -0.78%
- 2026-10-01 13:15 [reversion_bb] ENTRADA DOGE @ 0.0831947 (22.95 €, apertura)
- 2026-10-01 13:20 [estocastico_rebote] CIERRE ALGO timeout bruto -0.26% neto -0.76%
- 2026-10-01 13:15 [reversion_bb] ENTRADA ONDO @ 0.43853 (22.95 €, apertura)
- 2026-10-01 13:15 [estocastico_rebote] ENTRADA BCH @ 271.83 (21.96 €, apertura)
- 2026-10-01 13:20 [estocastico_rebote] CIERRE MINA take-profit bruto +1.80% neto +1.30%
- 2026-10-01 13:15 [reversion_bb] ENTRADA SHIB @ 5.055e-06 (22.95 €, apertura)
- 2026-10-01 13:20 [ruptura_volumen] CIERRE KSM stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 13:15 [estocastico_rebote] ENTRADA KSM @ 4.6 (21.97 €, apertura)
- 2026-10-01 13:20 [ruptura_volumen_tope] CIERRE KSM stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 13:20 [ruptura_volumen_evento] CIERRE KSM stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 13:20 [ruptura_volumen_regimen] CIERRE KAS stop-loss bruto -1.34% neto -1.84%
- 2026-10-01 13:15 [estocastico_rebote] ENTRADA SKY @ 0.06924 (21.97 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
