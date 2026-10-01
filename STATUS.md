# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 16:06 UTC · vueltas 260 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.04 € (-3.70%) | 216 | 19 | 33% | -0.085% | -0.706% | -0.830% | -34.72 € |
| reversion_bb | 916.63 € (-0.82%) | 38 | 9 | 39% | +0.067% | -1.033% | -1.133% | -9.04 € |
| ruptura_volumen | 879.56 € (-4.83%) | 241 | 7 | 23% | -0.219% | -0.827% | -0.935% | -45.15 € |
| rebote_extremo | 922.06 € (-0.24%) | 12 | 1 | 50% | +0.217% | -0.883% | -1.057% | -2.45 € |
| pullback_tendencia | 892.86 € (-3.40%) | 145 | 6 | 13% | -0.284% | -0.966% | -1.067% | -31.87 € |
| macd_momentum | 875.35 € (-5.29%) | 366 | 20 | 20% | -0.037% | -0.608% | -0.716% | -50.13 € |
| estocastico_rebote | 879.15 € (-4.88%) | 277 | 10 | 31% | -0.145% | -0.739% | -0.852% | -46.34 € |
| ruptura_estricta | 885.60 € (-4.18%) | 137 | 6 | 23% | -0.562% | -1.254% | -1.376% | -39.15 € |
| macd_sin_salida | 883.24 € (-4.44%) | 260 | 23 | 34% | -0.114% | -0.715% | -0.831% | -42.25 € |
| c_banda_atr_tope | 912.54 € (-1.27%) | 50 | 5 | 28% | -0.015% | -1.043% | -1.156% | -11.99 € |
| ruptura_volumen_tope | 907.80 € (-1.78%) | 80 | 5 | 25% | -0.069% | -0.899% | -1.014% | -16.50 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 895.96 € (-3.06%) | 183 | 19 | 34% | -0.044% | -0.689% | -0.807% | -28.79 € |
| macd_momentum_evento | 880.20 € (-4.76%) | 319 | 20 | 18% | -0.046% | -0.629% | -0.733% | -45.29 € |
| ruptura_volumen_evento | 892.08 € (-3.48%) | 191 | 7 | 24% | -0.112% | -0.751% | -0.847% | -32.63 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 16:05 | rebote_desplome_mercado | NIGHT | take-profit | +8.00% | +6.90% | +1.59 |
| 2026-10-01 16:05 | rebote_desplome | NIGHT | take-profit | +8.00% | +6.90% | +1.59 |
| 2026-10-01 16:05 | macd_momentum_evento | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 16:05 | macd_momentum_evento | UNI | momentum perdido | -0.00% | -0.50% | -0.11 |
| 2026-10-01 16:05 | c_banda_atr_evento | XMR | timeout | +0.09% | -0.41% | -0.09 |
| 2026-10-01 16:05 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 16:05 | macd_sin_salida | USELESS | take-profit | +2.16% | +1.66% | +0.37 |
| 2026-10-01 16:05 | macd_momentum | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 16:05 | macd_momentum | UNI | momentum perdido | -0.00% | -0.50% | -0.11 |
| 2026-10-01 16:05 | c_banda_atr | XMR | timeout | +0.09% | -0.41% | -0.09 |
| 2026-10-01 16:00 | macd_sin_salida | PEPE | take-profit | +2.06% | +1.56% | +0.34 |
| 2026-10-01 16:00 | rebote_extremo | PUMP | take-profit | +2.07% | +0.97% | +0.22 |
| 2026-10-01 15:55 | ruptura_volumen_evento | SKY | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 15:55 | ruptura_volumen | SKY | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-01 15:50 | macd_momentum_evento | SKY | take-profit | +2.17% | +1.67% | +0.37 |

## Eventos de la última vuelta

- 2026-10-01 16:00 [pullback_tendencia] ENTRADA ETH @ 2387.42 (22.31 €, apertura)
- 2026-10-01 16:05 [macd_momentum] CIERRE UNI momentum perdido bruto -0.00% neto -0.50%
- 2026-10-01 16:05 [macd_momentum_evento] CIERRE UNI momentum perdido bruto -0.00% neto -0.50%
- 2026-10-01 16:05 [rebote_desplome] CIERRE NIGHT take-profit bruto +8.00% neto +6.90%
- 2026-10-01 16:05 [rebote_desplome_mercado] CIERRE NIGHT take-profit bruto +8.00% neto +6.90%
- 2026-10-01 16:05 [macd_sin_salida] CIERRE USELESS take-profit bruto +2.16% neto +1.66%
- 2026-10-01 16:05 [macd_momentum] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-10-01 16:05 [macd_sin_salida] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-10-01 16:05 [macd_momentum_evento] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-10-01 16:00 [macd_momentum] ENTRADA MINA @ 0.1322 (21.85 €, apertura)
- 2026-10-01 16:00 [macd_sin_salida] ENTRADA MINA @ 0.1322 (22.05 €, apertura)
- 2026-10-01 16:00 [macd_momentum_evento] ENTRADA MINA @ 0.1322 (21.97 €, apertura)
- 2026-10-01 16:05 [c_banda_atr] CIERRE XMR timeout bruto +0.09% neto -0.41%
- 2026-10-01 16:05 [c_banda_atr_evento] CIERRE XMR timeout bruto +0.09% neto -0.41%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
