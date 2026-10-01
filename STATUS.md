# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 17:21 UTC · vueltas 275 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.57 € (-3.64%) | 223 | 22 | 33% | -0.115% | -0.732% | -0.855% | -37.11 € |
| reversion_bb | 917.41 € (-0.74%) | 40 | 8 | 42% | +0.142% | -0.950% | -1.049% | -8.76 € |
| ruptura_volumen | 878.65 € (-4.93%) | 253 | 9 | 23% | -0.223% | -0.826% | -0.935% | -47.27 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 893.27 € (-3.35%) | 155 | 5 | 14% | -0.253% | -0.924% | -1.020% | -32.56 € |
| macd_momentum | 873.74 € (-5.46%) | 390 | 18 | 20% | -0.037% | -0.604% | -0.711% | -52.98 € |
| estocastico_rebote | 877.63 € (-5.04%) | 286 | 5 | 31% | -0.137% | -0.729% | -0.840% | -47.14 € |
| ruptura_estricta | 886.29 € (-4.11%) | 139 | 11 | 23% | -0.551% | -1.241% | -1.362% | -39.30 € |
| macd_sin_salida | 883.42 € (-4.42%) | 272 | 26 | 33% | -0.121% | -0.717% | -0.831% | -44.26 € |
| c_banda_atr_tope | 911.93 € (-1.33%) | 52 | 5 | 27% | -0.078% | -1.085% | -1.200% | -12.96 € |
| ruptura_volumen_tope | 908.86 € (-1.66%) | 85 | 4 | 27% | -0.026% | -0.837% | -0.953% | -16.32 € |
| c_banda_atr_regimen | 902.32 € (-2.37%) | 110 | 4 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.50 € (-3.33%) | 208 | 0 | 22% | -0.023% | -0.648% | -0.761% | -30.74 € |
| ruptura_volumen_regimen | 882.11 € (-4.56%) | 190 | 4 | 19% | -0.347% | -0.985% | -1.101% | -42.43 € |
| c_banda_atr_evento | 896.50 € (-3.00%) | 190 | 22 | 33% | -0.081% | -0.720% | -0.837% | -31.21 € |
| macd_momentum_evento | 878.58 € (-4.94%) | 343 | 18 | 17% | -0.046% | -0.623% | -0.725% | -48.15 € |
| ruptura_volumen_evento | 891.15 € (-3.58%) | 203 | 9 | 24% | -0.124% | -0.754% | -0.852% | -34.78 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 17:20 | ruptura_volumen_evento | TRX | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-01 17:20 | ruptura_volumen_evento | XRP | timeout | +0.69% | +0.19% | +0.04 |
| 2026-10-01 17:20 | macd_momentum_evento | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 17:20 | c_banda_atr_evento | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 17:20 | ruptura_volumen_tope | XRP | timeout | +0.69% | +0.19% | +0.04 |
| 2026-10-01 17:20 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 17:20 | macd_momentum | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 17:20 | ruptura_volumen | TRX | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-01 17:20 | ruptura_volumen | XRP | timeout | +0.69% | +0.19% | +0.04 |
| 2026-10-01 17:20 | reversion_bb | SPX | take-profit | +1.50% | +0.70% | +0.16 |
| 2026-10-01 17:20 | c_banda_atr | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 17:15 | macd_momentum_evento | TRX | momentum perdido | -0.02% | -0.52% | -0.11 |
| 2026-10-01 17:15 | macd_momentum | TRX | momentum perdido | -0.02% | -0.52% | -0.11 |
| 2026-10-01 17:05 | macd_momentum_evento | TON | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 17:05 | macd_sin_salida | AAVE | stop-loss | -1.50% | -2.00% | -0.44 |

## Eventos de la última vuelta

- 2026-10-01 17:15 [macd_momentum] ENTRADA BTC @ 75205.8 (21.77 €, apertura)
- 2026-10-01 17:15 [macd_momentum_evento] ENTRADA BTC @ 75205.8 (21.89 €, apertura)
- 2026-10-01 17:20 [ruptura_volumen] CIERRE XRP timeout bruto +0.69% neto +0.19%
- 2026-10-01 17:20 [ruptura_volumen_tope] CIERRE XRP timeout bruto +0.69% neto +0.19%
- 2026-10-01 17:20 [ruptura_volumen_evento] CIERRE XRP timeout bruto +0.69% neto +0.19%
- 2026-10-01 17:15 [macd_momentum] ENTRADA DOGE @ 0.0841179 (21.77 €, apertura)
- 2026-10-01 17:15 [macd_sin_salida] ENTRADA DOGE @ 0.0841179 (21.99 €, apertura)
- 2026-10-01 17:15 [macd_momentum_evento] ENTRADA DOGE @ 0.0841179 (21.89 €, apertura)
- 2026-10-01 17:20 [ruptura_volumen] CIERRE TRX timeout bruto +0.60% neto +0.10%
- 2026-10-01 17:20 [ruptura_volumen_evento] CIERRE TRX timeout bruto +0.60% neto +0.10%
- 2026-10-01 17:20 [c_banda_atr] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:20 [macd_momentum] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:20 [macd_sin_salida] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:20 [c_banda_atr_evento] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:20 [macd_momentum_evento] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:15 [macd_momentum] ENTRADA FIL @ 0.901 (21.78 €, apertura)
- 2026-10-01 17:15 [macd_sin_salida] ENTRADA FIL @ 0.901 (22.00 €, apertura)
- 2026-10-01 17:15 [macd_momentum_evento] ENTRADA FIL @ 0.901 (21.90 €, apertura)
- 2026-10-01 17:15 [c_banda_atr] ENTRADA TON @ 1.361 (22.18 €, apertura)
- 2026-10-01 17:15 [c_banda_atr_evento] ENTRADA TON @ 1.361 (22.33 €, apertura)
- 2026-10-01 17:15 [c_banda_atr] ENTRADA SPX @ 0.388 (22.18 €, apertura)
- 2026-10-01 17:20 [reversion_bb] CIERRE SPX take-profit bruto +1.50% neto +0.70%
- 2026-10-01 17:15 [macd_momentum] ENTRADA SPX @ 0.388 (21.78 €, apertura)
- 2026-10-01 17:15 [macd_sin_salida] ENTRADA SPX @ 0.388 (22.00 €, apertura)
- 2026-10-01 17:15 [c_banda_atr_evento] ENTRADA SPX @ 0.388 (22.33 €, apertura)
- 2026-10-01 17:15 [macd_momentum_evento] ENTRADA SPX @ 0.388 (21.90 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
