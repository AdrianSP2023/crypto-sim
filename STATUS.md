# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 16:16 UTC · vueltas 262 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.26 € (-3.78%) | 216 | 21 | 33% | -0.085% | -0.706% | -0.830% | -34.72 € |
| reversion_bb | 916.12 € (-0.88%) | 38 | 9 | 39% | +0.067% | -1.033% | -1.133% | -9.04 € |
| ruptura_volumen | 879.27 € (-4.87%) | 243 | 10 | 23% | -0.212% | -0.820% | -0.928% | -45.11 € |
| rebote_extremo | 921.98 € (-0.24%) | 12 | 1 | 50% | +0.217% | -0.883% | -1.057% | -2.45 € |
| pullback_tendencia | 892.81 € (-3.40%) | 146 | 5 | 14% | -0.268% | -0.949% | -1.050% | -31.54 € |
| macd_momentum | 874.17 € (-5.42%) | 368 | 20 | 20% | -0.034% | -0.605% | -0.713% | -50.15 € |
| estocastico_rebote | 878.37 € (-4.96%) | 281 | 6 | 31% | -0.143% | -0.736% | -0.849% | -46.80 € |
| ruptura_estricta | 886.02 € (-4.14%) | 137 | 7 | 23% | -0.562% | -1.254% | -1.376% | -39.15 € |
| macd_sin_salida | 882.28 € (-4.54%) | 261 | 22 | 34% | -0.106% | -0.706% | -0.822% | -41.90 € |
| c_banda_atr_tope | 912.30 € (-1.29%) | 50 | 5 | 28% | -0.015% | -1.043% | -1.156% | -11.99 € |
| ruptura_volumen_tope | 908.18 € (-1.74%) | 80 | 5 | 25% | -0.069% | -0.899% | -1.014% | -16.50 € |
| c_banda_atr_regimen | 901.87 € (-2.42%) | 110 | 2 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.75 € (-3.30%) | 206 | 2 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.31 € (-4.43%) | 186 | 4 | 19% | -0.327% | -0.968% | -1.083% | -40.85 € |
| c_banda_atr_evento | 895.18 € (-3.14%) | 183 | 21 | 34% | -0.044% | -0.689% | -0.807% | -28.79 € |
| macd_momentum_evento | 879.02 € (-4.89%) | 321 | 20 | 18% | -0.043% | -0.625% | -0.729% | -45.31 € |
| ruptura_volumen_evento | 891.78 € (-3.51%) | 193 | 10 | 24% | -0.105% | -0.742% | -0.839% | -32.59 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 16:15 | ruptura_volumen_evento | VVV | stop-loss | -1.32% | -1.82% | -0.41 |
| 2026-10-01 16:15 | ruptura_volumen_evento | ZRO | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 16:15 | macd_momentum_evento | ZRO | take-profit | +2.07% | +1.57% | +0.34 |
| 2026-10-01 16:15 | macd_momentum_evento | AAVE | momentum perdido | -1.16% | -1.66% | -0.36 |
| 2026-10-01 16:15 | ruptura_volumen_regimen | VVV | stop-loss | -1.32% | -1.82% | -0.40 |
| 2026-10-01 16:15 | macd_sin_salida | ZRO | take-profit | +2.07% | +1.57% | +0.34 |
| 2026-10-01 16:15 | estocastico_rebote | KSM | timeout | +0.22% | -0.28% | -0.06 |
| 2026-10-01 16:15 | estocastico_rebote | BCH | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-01 16:15 | macd_momentum | ZRO | take-profit | +2.07% | +1.57% | +0.34 |
| 2026-10-01 16:15 | macd_momentum | AAVE | momentum perdido | -1.16% | -1.66% | -0.36 |
| 2026-10-01 16:15 | pullback_tendencia | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 16:15 | ruptura_volumen | VVV | stop-loss | -1.32% | -1.82% | -0.40 |
| 2026-10-01 16:15 | ruptura_volumen | ZRO | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-01 16:10 | estocastico_rebote | HYPE | timeout | -1.25% | -1.75% | -0.39 |
| 2026-10-01 16:10 | estocastico_rebote | ETH | timeout | +0.32% | -0.18% | -0.04 |

## Eventos de la última vuelta

- 2026-10-01 16:15 [macd_momentum] CIERRE AAVE momentum perdido bruto -1.15% neto -1.65%
- 2026-10-01 16:15 [macd_momentum_evento] CIERRE AAVE momentum perdido bruto -1.15% neto -1.65%
- 2026-10-01 16:10 [macd_momentum] ENTRADA UNI @ 8.093 (21.84 €, apertura)
- 2026-10-01 16:10 [macd_momentum_regimen] ENTRADA UNI @ 8.093 (22.35 €, apertura)
- 2026-10-01 16:10 [macd_momentum_evento] ENTRADA UNI @ 8.093 (21.96 €, apertura)
- 2026-10-01 16:15 [ruptura_volumen] CIERRE ZRO take-profit bruto +2.50% neto +2.00%
- 2026-10-01 16:15 [pullback_tendencia] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-10-01 16:15 [macd_momentum] CIERRE ZRO take-profit bruto +2.07% neto +1.57%
- 2026-10-01 16:15 [macd_sin_salida] CIERRE ZRO take-profit bruto +2.07% neto +1.57%
- 2026-10-01 16:15 [macd_momentum_evento] CIERRE ZRO take-profit bruto +2.07% neto +1.57%
- 2026-10-01 16:15 [ruptura_volumen_evento] CIERRE ZRO take-profit bruto +2.50% neto +2.00%
- 2026-10-01 16:10 [ruptura_volumen] ENTRADA XDC @ 0.03121 (21.99 €, apertura)
- 2026-10-01 16:10 [ruptura_volumen_regimen] ENTRADA XDC @ 0.03121 (22.09 €, apertura)
- 2026-10-01 16:10 [ruptura_volumen_evento] ENTRADA XDC @ 0.03121 (22.30 €, apertura)
- 2026-10-01 16:15 [estocastico_rebote] CIERRE BCH timeout bruto +0.60% neto +0.10%
- 2026-10-01 16:15 [ruptura_volumen] CIERRE VVV stop-loss bruto -1.32% neto -1.82%
- 2026-10-01 16:15 [ruptura_volumen_regimen] CIERRE VVV stop-loss bruto -1.32% neto -1.82%
- 2026-10-01 16:15 [ruptura_volumen_evento] CIERRE VVV stop-loss bruto -1.32% neto -1.82%
- 2026-10-01 16:15 [estocastico_rebote] CIERRE KSM timeout bruto +0.22% neto -0.28%
- 2026-10-01 16:10 [ruptura_volumen] ENTRADA SKY @ 0.0725 (21.98 €, apertura)
- 2026-10-01 16:10 [ruptura_volumen_regimen] ENTRADA SKY @ 0.0725 (22.08 €, apertura)
- 2026-10-01 16:10 [ruptura_volumen_evento] ENTRADA SKY @ 0.0725 (22.29 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
