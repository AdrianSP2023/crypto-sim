# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 13:16 UTC · vueltas 226 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 893.07 € (-3.37%) | 191 | 15 | 35% | -0.027% | -0.664% | -0.790% | -28.99 € |
| reversion_bb | 917.44 € (-0.74%) | 28 | 9 | 43% | +0.152% | -0.948% | -1.050% | -6.12 € |
| ruptura_volumen | 882.01 € (-4.57%) | 227 | 6 | 23% | -0.194% | -0.809% | -0.918% | -41.68 € |
| rebote_extremo | 922.29 € (-0.21%) | 10 | 0 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 894.53 € (-3.21%) | 135 | 0 | 14% | -0.271% | -0.966% | -1.072% | -29.72 € |
| macd_momentum | 880.69 € (-4.71%) | 328 | 2 | 21% | -0.009% | -0.589% | -0.698% | -43.68 € |
| estocastico_rebote | 878.38 € (-4.96%) | 263 | 10 | 30% | -0.163% | -0.763% | -0.873% | -45.42 € |
| ruptura_estricta | 886.68 € (-4.06%) | 128 | 7 | 24% | -0.538% | -1.244% | -1.368% | -36.36 € |
| macd_sin_salida | 884.15 € (-4.34%) | 231 | 17 | 35% | -0.115% | -0.728% | -0.844% | -38.36 € |
| c_banda_atr_tope | 912.45 € (-1.28%) | 44 | 3 | 27% | -0.045% | -1.131% | -1.251% | -11.45 € |
| ruptura_volumen_tope | 911.17 € (-1.41%) | 68 | 3 | 28% | +0.074% | -0.814% | -0.926% | -12.72 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 894.00 € (-3.27%) | 205 | 1 | 22% | -0.022% | -0.649% | -0.762% | -30.34 € |
| ruptura_volumen_regimen | 884.25 € (-4.33%) | 182 | 3 | 20% | -0.318% | -0.961% | -1.076% | -39.75 € |
| c_banda_atr_evento | 899.02 € (-2.73%) | 158 | 15 | 36% | +0.032% | -0.635% | -0.755% | -23.03 € |
| macd_momentum_evento | 885.57 € (-4.18%) | 281 | 2 | 19% | -0.016% | -0.609% | -0.714% | -38.80 € |
| ruptura_volumen_evento | 894.56 € (-3.21%) | 177 | 6 | 24% | -0.072% | -0.721% | -0.818% | -29.11 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 13:15 | ruptura_volumen_evento | SKY | stop-loss | -1.32% | -1.82% | -0.41 |
| 2026-10-01 13:15 | ruptura_volumen_evento | XDC | timeout | +1.08% | +0.58% | +0.13 |
| 2026-10-01 13:15 | macd_momentum_evento | ALGO | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-10-01 13:15 | c_banda_atr_evento | SKY | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 13:15 | c_banda_atr_evento | DASH | stop-loss | -1.58% | -2.08% | -0.47 |
| 2026-10-01 13:15 | macd_momentum_regimen | ALGO | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-10-01 13:15 | c_banda_atr_regimen | VVV | stop-loss | -1.53% | -2.03% | -0.46 |
| 2026-10-01 13:15 | macd_sin_salida | WLD | stop-loss | -1.65% | -2.15% | -0.48 |
| 2026-10-01 13:15 | macd_momentum | ALGO | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-10-01 13:15 | rebote_extremo | NEAR | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-10-01 13:15 | ruptura_volumen | SKY | stop-loss | -1.32% | -1.82% | -0.40 |
| 2026-10-01 13:15 | ruptura_volumen | XDC | timeout | +1.08% | +0.58% | +0.13 |
| 2026-10-01 13:15 | reversion_bb | XLM | stop-loss | -1.52% | -2.62% | -0.60 |
| 2026-10-01 13:15 | c_banda_atr | SKY | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 13:15 | c_banda_atr | DASH | stop-loss | -1.58% | -2.08% | -0.47 |

## Eventos de la última vuelta

- 2026-10-01 13:10 [estocastico_rebote] ENTRADA ETH @ 2380.75 (21.97 €, apertura)
- 2026-10-01 13:10 [rebote_extremo] ENTRADA NEAR @ 4.2812 (23.05 €, apertura)
- 2026-10-01 13:15 [rebote_extremo] CIERRE NEAR take-profit bruto +2.00% neto +0.90%
- 2026-10-01 13:10 [estocastico_rebote] ENTRADA HYPE @ 78.89 (21.97 €, apertura)
- 2026-10-01 13:15 [reversion_bb] CIERRE XLM stop-loss bruto -1.52% neto -2.62%
- 2026-10-01 13:10 [reversion_bb] ENTRADA TAO @ 266.692 (22.95 €, apertura)
- 2026-10-01 13:15 [macd_momentum] CIERRE ALGO momentum perdido bruto +0.04% neto -0.46%
- 2026-10-01 13:15 [macd_momentum_regimen] CIERRE ALGO momentum perdido bruto +0.04% neto -0.46%
- 2026-10-01 13:15 [macd_momentum_evento] CIERRE ALGO momentum perdido bruto +0.04% neto -0.46%
- 2026-10-01 13:15 [macd_sin_salida] CIERRE WLD stop-loss bruto -1.65% neto -2.15%
- 2026-10-01 13:15 [ruptura_volumen] CIERRE XDC timeout bruto +1.09% neto +0.59%
- 2026-10-01 13:15 [ruptura_volumen_evento] CIERRE XDC timeout bruto +1.09% neto +0.59%
- 2026-10-01 13:10 [reversion_bb] ENTRADA VVV @ 24.15 (22.95 €, apertura)
- 2026-10-01 13:15 [c_banda_atr_regimen] CIERRE VVV stop-loss bruto -1.53% neto -2.03%
- 2026-10-01 13:15 [c_banda_atr] CIERRE DASH stop-loss bruto -1.58% neto -2.08%
- 2026-10-01 13:15 [c_banda_atr_evento] CIERRE DASH stop-loss bruto -1.58% neto -2.08%
- 2026-10-01 13:15 [c_banda_atr] CIERRE SKY stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 13:15 [ruptura_volumen] CIERRE SKY stop-loss bruto -1.32% neto -1.82%
- 2026-10-01 13:15 [c_banda_atr_evento] CIERRE SKY stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 13:15 [ruptura_volumen_evento] CIERRE SKY stop-loss bruto -1.32% neto -1.82%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
