# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 18:14 UTC · vueltas 279 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

**Avisos:** hueco de 38 min entre vueltas

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.82 € (-3.51%) | 233 | 17 | 36% | -0.037% | -0.649% | -0.772% | -34.45 € |
| reversion_bb | 916.81 € (-0.80%) | 45 | 3 | 49% | +0.297% | -0.763% | -0.860% | -7.91 € |
| ruptura_volumen | 878.97 € (-4.90%) | 258 | 26 | 24% | -0.191% | -0.793% | -0.901% | -46.26 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 893.54 € (-3.32%) | 158 | 4 | 15% | -0.210% | -0.878% | -0.974% | -31.55 € |
| macd_momentum | 875.83 € (-5.24%) | 396 | 35 | 20% | -0.018% | -0.584% | -0.691% | -52.07 € |
| estocastico_rebote | 878.15 € (-4.99%) | 287 | 6 | 31% | -0.129% | -0.720% | -0.831% | -46.73 € |
| ruptura_estricta | 887.54 € (-3.97%) | 142 | 21 | 24% | -0.509% | -1.195% | -1.317% | -38.69 € |
| macd_sin_salida | 885.47 € (-4.19%) | 285 | 28 | 36% | -0.053% | -0.644% | -0.759% | -41.78 € |
| c_banda_atr_tope | 912.11 € (-1.31%) | 54 | 4 | 30% | -0.023% | -1.012% | -1.128% | -12.56 € |
| ruptura_volumen_tope | 909.11 € (-1.64%) | 87 | 5 | 29% | +0.028% | -0.775% | -0.891% | -15.48 € |
| c_banda_atr_regimen | 903.12 € (-2.28%) | 111 | 11 | 34% | -0.124% | -0.859% | -0.998% | -21.89 € |
| macd_momentum_regimen | 894.98 € (-3.17%) | 210 | 21 | 22% | -0.019% | -0.644% | -0.756% | -30.80 € |
| ruptura_volumen_regimen | 882.39 € (-4.53%) | 192 | 26 | 19% | -0.344% | -0.980% | -1.097% | -42.67 € |
| c_banda_atr_evento | 897.76 € (-2.87%) | 200 | 17 | 36% | +0.008% | -0.624% | -0.741% | -28.52 € |
| macd_momentum_evento | 880.68 € (-4.71%) | 349 | 35 | 18% | -0.025% | -0.600% | -0.703% | -47.24 € |
| ruptura_volumen_evento | 891.48 € (-3.54%) | 208 | 26 | 25% | -0.087% | -0.714% | -0.813% | -33.76 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 18:10 | macd_momentum_evento | BTC | momentum perdido | +0.47% | -0.03% | -0.01 |
| 2026-10-01 18:10 | macd_sin_salida | TON | take-profit | +2.07% | +1.57% | +0.35 |
| 2026-10-01 18:10 | macd_momentum | BTC | momentum perdido | +0.47% | -0.03% | -0.01 |
| 2026-10-01 18:05 | ruptura_volumen_evento | SHIB | timeout | +1.11% | +0.61% | +0.14 |
| 2026-10-01 18:05 | ruptura_volumen_regimen | SHIB | timeout | +1.11% | +0.61% | +0.14 |
| 2026-10-01 18:05 | macd_sin_salida | BCH | timeout | +0.62% | +0.12% | +0.03 |
| 2026-10-01 18:05 | macd_sin_salida | XRP | timeout | +1.23% | +0.73% | +0.16 |
| 2026-10-01 18:05 | ruptura_volumen | SHIB | timeout | +1.11% | +0.61% | +0.14 |
| 2026-10-01 18:00 | ruptura_estricta | SKY | take-profit | +3.13% | +2.63% | +0.58 |
| 2026-10-01 18:00 | estocastico_rebote | SKY | take-profit | +2.36% | +1.86% | +0.41 |
| 2026-10-01 17:55 | macd_momentum_evento | JUP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 17:55 | c_banda_atr_evento | JUP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 17:55 | c_banda_atr_regimen | JUP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 17:55 | macd_sin_salida | JUP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 17:55 | macd_momentum | JUP | take-profit | +2.00% | +1.50% | +0.33 |

## Eventos de la última vuelta

- 2026-10-01 17:40 [c_banda_atr] CIERRE BTC timeout bruto +1.87% neto +1.37%
- 2026-10-01 17:40 [c_banda_atr_evento] CIERRE BTC timeout bruto +1.87% neto +1.37%
- 2026-10-01 17:40 [c_banda_atr] CIERRE XRP timeout bruto +1.36% neto +0.86%
- 2026-10-01 17:40 [c_banda_atr_evento] CIERRE XRP timeout bruto +1.36% neto +0.86%
- 2026-10-01 17:40 [macd_sin_salida] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 17:35 [ruptura_volumen] ENTRADA DOT @ 1.0503 (21.94 €, apertura)
- 2026-10-01 17:35 [ruptura_volumen_regimen] ENTRADA DOT @ 1.0503 (22.05 €, apertura)
- 2026-10-01 17:35 [ruptura_volumen_evento] ENTRADA DOT @ 1.0503 (22.26 €, apertura)
- 2026-10-01 17:35 [ruptura_volumen] ENTRADA DASH @ 52.661 (21.94 €, apertura)
- 2026-10-01 17:35 [ruptura_volumen_regimen] ENTRADA DASH @ 52.661 (22.05 €, apertura)
- 2026-10-01 17:35 [ruptura_volumen_evento] ENTRADA DASH @ 52.661 (22.26 €, apertura)
- 2026-10-01 17:40 [ruptura_volumen] CIERRE PENGU take-profit bruto +2.50% neto +2.00%
- 2026-10-01 17:40 [ruptura_volumen_evento] CIERRE PENGU take-profit bruto +2.50% neto +2.00%
- 2026-10-01 17:40 [c_banda_atr] CIERRE BNB timeout bruto +0.94% neto +0.44%
- 2026-10-01 17:40 [c_banda_atr_evento] CIERRE BNB timeout bruto +0.94% neto +0.44%
- 2026-10-01 17:45 [macd_sin_salida] CIERRE ADA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:45 [macd_momentum] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:45 [macd_sin_salida] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:45 [macd_momentum_regimen] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:45 [macd_momentum_evento] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:45 [reversion_bb] CIERRE JUP take-profit bruto +1.68% neto +0.88%
- 2026-10-01 17:40 [ruptura_volumen] ENTRADA FIL @ 0.914 (21.96 €, apertura)
- 2026-10-01 17:40 [ruptura_estricta] ENTRADA FIL @ 0.914 (22.12 €, apertura)
- 2026-10-01 17:40 [ruptura_volumen_regimen] ENTRADA FIL @ 0.914 (22.05 €, apertura)
- 2026-10-01 17:40 [ruptura_volumen_evento] ENTRADA FIL @ 0.914 (22.27 €, apertura)
- 2026-10-01 17:40 [ruptura_estricta] ENTRADA PENGU @ 0.00847 (22.12 €, apertura)
- 2026-10-01 17:40 [ruptura_volumen_regimen] ENTRADA PENGU @ 0.00847 (22.05 €, apertura)
- 2026-10-01 17:45 [macd_sin_salida] CIERRE APT take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:50 [pullback_tendencia] CIERRE BTC take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:45 [ruptura_volumen] ENTRADA XRP @ 1.33862 (21.96 €, apertura)
- 2026-10-01 17:45 [ruptura_volumen_regimen] ENTRADA XRP @ 1.33862 (22.05 €, apertura)
- 2026-10-01 17:45 [ruptura_volumen_evento] ENTRADA XRP @ 1.33862 (22.27 €, apertura)
- 2026-10-01 17:45 [ruptura_volumen] ENTRADA AAVE @ 151.26 (21.96 €, apertura)
- 2026-10-01 17:45 [ruptura_volumen_regimen] ENTRADA AAVE @ 151.26 (22.05 €, apertura)
- 2026-10-01 17:45 [ruptura_volumen_evento] ENTRADA AAVE @ 151.26 (22.27 €, apertura)
- 2026-10-01 17:45 [ruptura_volumen] ENTRADA PUMP @ 0.005186 (21.96 €, apertura)
- 2026-10-01 17:50 [ruptura_volumen] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 17:45 [ruptura_volumen_regimen] ENTRADA PUMP @ 0.005186 (22.05 €, apertura)
- 2026-10-01 17:50 [ruptura_volumen_regimen] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 17:45 [ruptura_volumen_evento] ENTRADA PUMP @ 0.005186 (22.27 €, apertura)
- 2026-10-01 17:50 [ruptura_volumen_evento] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 17:45 [ruptura_volumen] ENTRADA FET @ 0.206 (21.95 €, apertura)
- 2026-10-01 17:45 [ruptura_estricta] ENTRADA FET @ 0.206 (22.12 €, apertura)
- 2026-10-01 17:45 [ruptura_volumen_regimen] ENTRADA FET @ 0.206 (22.04 €, apertura)
- 2026-10-01 17:45 [ruptura_volumen_evento] ENTRADA FET @ 0.206 (22.26 €, apertura)
- 2026-10-01 17:45 [ruptura_volumen] ENTRADA BCH @ 275.12 (21.95 €, apertura)
- 2026-10-01 17:45 [ruptura_estricta] ENTRADA BCH @ 275.12 (22.12 €, apertura)
- 2026-10-01 17:45 [ruptura_volumen_regimen] ENTRADA BCH @ 275.12 (22.04 €, apertura)
- 2026-10-01 17:45 [ruptura_volumen_evento] ENTRADA BCH @ 275.12 (22.26 €, apertura)
- 2026-10-01 17:50 [c_banda_atr] CIERRE FIL take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:50 [c_banda_atr_evento] CIERRE FIL take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:50 [ruptura_estricta] CIERRE WLFI timeout bruto +1.02% neto +0.52%
- 2026-10-01 17:50 [macd_sin_salida] CIERRE WLFI timeout bruto +1.02% neto +0.52%
- 2026-10-01 17:50 [c_banda_atr] CIERRE SHIB take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:50 [macd_sin_salida] CIERRE SHIB take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:50 [c_banda_atr_evento] CIERRE SHIB take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:45 [ruptura_estricta] ENTRADA DASH @ 52.788 (22.12 €, apertura)
- 2026-10-01 17:45 [macd_momentum] ENTRADA SKY @ 0.07238 (21.80 €, apertura)
- 2026-10-01 17:45 [macd_sin_salida] ENTRADA SKY @ 0.07238 (22.04 €, apertura)
- 2026-10-01 17:45 [macd_momentum_regimen] ENTRADA SKY @ 0.07238 (22.34 €, apertura)
- 2026-10-01 17:45 [macd_momentum_evento] ENTRADA SKY @ 0.07238 (21.92 €, apertura)
- 2026-10-01 17:55 [c_banda_atr] CIERRE JUP take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:55 [macd_momentum] CIERRE JUP take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:55 [macd_sin_salida] CIERRE JUP take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:55 [c_banda_atr_regimen] CIERRE JUP take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:55 [c_banda_atr_evento] CIERRE JUP take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:55 [macd_momentum_evento] CIERRE JUP take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:55 [ruptura_volumen] ENTRADA JUP @ 0.29002 (21.95 €, apertura)
- 2026-10-01 17:55 [ruptura_estricta] ENTRADA JUP @ 0.29002 (22.12 €, apertura)
- 2026-10-01 17:55 [ruptura_volumen_regimen] ENTRADA JUP @ 0.29002 (22.04 €, apertura)
- 2026-10-01 17:55 [ruptura_volumen_evento] ENTRADA JUP @ 0.29002 (22.26 €, apertura)
- 2026-10-01 18:00 [estocastico_rebote] CIERRE SKY take-profit bruto +2.36% neto +1.86%
- 2026-10-01 18:00 [ruptura_estricta] CIERRE SKY take-profit bruto +3.13% neto +2.63%
- 2026-10-01 18:05 [macd_sin_salida] CIERRE XRP timeout bruto +1.23% neto +0.73%
- 2026-10-01 18:00 [pullback_tendencia] ENTRADA ZRO @ 1.591 (22.32 €, apertura)
- 2026-10-01 18:05 [macd_sin_salida] CIERRE BCH timeout bruto +0.62% neto +0.12%
- 2026-10-01 18:05 [ruptura_volumen] CIERRE SHIB timeout bruto +1.11% neto +0.61%
- 2026-10-01 18:05 [ruptura_volumen_regimen] CIERRE SHIB timeout bruto +1.11% neto +0.61%
- 2026-10-01 18:05 [ruptura_volumen_evento] CIERRE SHIB timeout bruto +1.11% neto +0.61%
- 2026-10-01 18:00 [ruptura_volumen] ENTRADA TON @ 1.372 (21.95 €, apertura)
- 2026-10-01 18:00 [ruptura_estricta] ENTRADA TON @ 1.372 (22.14 €, apertura)
- 2026-10-01 18:00 [ruptura_volumen_regimen] ENTRADA TON @ 1.372 (22.04 €, apertura)
- 2026-10-01 18:00 [ruptura_volumen_evento] ENTRADA TON @ 1.372 (22.26 €, apertura)
- 2026-10-01 18:00 [ruptura_volumen] ENTRADA SKY @ 0.07323 (21.95 €, apertura)
- 2026-10-01 18:00 [ruptura_volumen_regimen] ENTRADA SKY @ 0.07323 (22.04 €, apertura)
- 2026-10-01 18:00 [ruptura_volumen_evento] ENTRADA SKY @ 0.07323 (22.26 €, apertura)
- 2026-10-01 18:10 [macd_momentum] CIERRE BTC momentum perdido bruto +0.47% neto -0.03%
- 2026-10-01 18:10 [macd_momentum_evento] CIERRE BTC momentum perdido bruto +0.47% neto -0.03%
- 2026-10-01 18:05 [macd_momentum] ENTRADA ZRO @ 1.591 (21.80 €, apertura)
- 2026-10-01 18:05 [macd_sin_salida] ENTRADA ZRO @ 1.591 (22.05 €, apertura)
- 2026-10-01 18:05 [macd_momentum_regimen] ENTRADA ZRO @ 1.591 (22.34 €, apertura)
- 2026-10-01 18:05 [macd_momentum_evento] ENTRADA ZRO @ 1.591 (21.93 €, apertura)
- 2026-10-01 18:10 [macd_sin_salida] CIERRE TON take-profit bruto +2.07% neto +1.57%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
