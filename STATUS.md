# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 01:31 UTC · vueltas 353 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 883.92 € (-4.36%) | 273 | 25 | 34% | -0.040% | -0.636% | -0.757% | -39.41 € |
| reversion_bb | 916.84 € (-0.80%) | 57 | 15 | 53% | +0.375% | -0.583% | -0.692% | -7.66 € |
| ruptura_volumen | 866.51 € (-6.25%) | 307 | 26 | 24% | -0.223% | -0.808% | -0.916% | -55.81 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.07 € (-3.91%) | 193 | 4 | 15% | -0.201% | -0.837% | -0.925% | -36.66 € |
| macd_momentum | 861.43 € (-6.80%) | 509 | 5 | 20% | -0.004% | -0.556% | -0.658% | -63.24 € |
| estocastico_rebote | 872.14 € (-5.64%) | 339 | 12 | 32% | -0.096% | -0.673% | -0.783% | -51.46 € |
| ruptura_estricta | 881.91 € (-4.58%) | 167 | 11 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 870.56 € (-5.81%) | 356 | 12 | 34% | -0.093% | -0.667% | -0.778% | -53.60 € |
| c_banda_atr_tope | 911.56 € (-1.37%) | 63 | 5 | 30% | +0.022% | -0.897% | -1.012% | -12.97 € |
| ruptura_volumen_tope | 904.22 € (-2.17%) | 104 | 5 | 26% | -0.052% | -0.806% | -0.922% | -19.20 € |
| c_banda_atr_regimen | 895.72 € (-3.09%) | 138 | 8 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 884.31 € (-4.32%) | 284 | 1 | 19% | -0.033% | -0.625% | -0.730% | -40.23 € |
| ruptura_volumen_regimen | 870.17 € (-5.85%) | 239 | 21 | 19% | -0.372% | -0.981% | -1.095% | -52.84 € |
| c_banda_atr_evento | 889.81 € (-3.73%) | 240 | 25 | 35% | -0.003% | -0.613% | -0.729% | -33.51 € |
| macd_momentum_evento | 866.21 € (-6.28%) | 462 | 5 | 19% | -0.008% | -0.565% | -0.663% | -58.47 € |
| ruptura_volumen_evento | 878.84 € (-4.91%) | 257 | 26 | 25% | -0.145% | -0.748% | -0.847% | -43.45 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 01:30 | macd_momentum_evento | MINA | momentum perdido | +0.52% | +0.02% | +0.00 |
| 2026-10-02 01:30 | macd_momentum_regimen | MINA | momentum perdido | +0.52% | +0.02% | +0.00 |
| 2026-10-02 01:30 | macd_sin_salida | PUMP | timeout | -0.47% | -0.96% | -0.21 |
| 2026-10-02 01:30 | estocastico_rebote | AAVE | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 01:30 | macd_momentum | MINA | momentum perdido | +0.52% | +0.02% | +0.00 |
| 2026-10-02 01:25 | ruptura_volumen_evento | PEPE | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 01:25 | ruptura_volumen_evento | WLD | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 01:25 | ruptura_volumen_evento | TAO | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 01:25 | ruptura_volumen_evento | XLM | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 01:25 | ruptura_volumen_regimen | TRUMP | stop-loss | -1.57% | -2.07% | -0.45 |
| 2026-10-02 01:25 | ruptura_volumen_regimen | PEPE | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 01:25 | ruptura_volumen_regimen | WLD | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 01:25 | ruptura_volumen_regimen | TAO | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 01:25 | ruptura_volumen_regimen | XLM | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 01:25 | macd_momentum_regimen | SOL | momentum perdido | +0.41% | -0.09% | -0.02 |

## Eventos de la última vuelta

- 2026-10-02 01:25 [estocastico_rebote] ENTRADA BTC @ 75288 (21.81 €, apertura)
- 2026-10-02 01:25 [estocastico_rebote] ENTRADA XRP @ 1.32802 (21.81 €, apertura)
- 2026-10-02 01:25 [macd_momentum] ENTRADA NEAR @ 4.307 (21.53 €, apertura)
- 2026-10-02 01:25 [macd_sin_salida] ENTRADA NEAR @ 4.307 (21.77 €, apertura)
- 2026-10-02 01:25 [macd_momentum_evento] ENTRADA NEAR @ 4.307 (21.64 €, apertura)
- 2026-10-02 01:30 [estocastico_rebote] CIERRE AAVE take-profit bruto +1.80% neto +1.30%
- 2026-10-02 01:30 [macd_sin_salida] CIERRE PUMP timeout bruto -0.47% neto -0.97%
- 2026-10-02 01:25 [ruptura_volumen] ENTRADA MON @ 0.03019 (21.71 €, apertura)
- 2026-10-02 01:25 [macd_momentum] ENTRADA MON @ 0.03019 (21.53 €, apertura)
- 2026-10-02 01:25 [macd_sin_salida] ENTRADA MON @ 0.03019 (21.77 €, apertura)
- 2026-10-02 01:25 [ruptura_volumen_tope] ENTRADA MON @ 0.03019 (22.63 €, apertura)
- 2026-10-02 01:25 [macd_momentum_evento] ENTRADA MON @ 0.03019 (21.64 €, apertura)
- 2026-10-02 01:25 [ruptura_volumen_evento] ENTRADA MON @ 0.03019 (22.02 €, apertura)
- 2026-10-02 01:25 [pullback_tendencia] ENTRADA OP @ 0.1145 (22.19 €, apertura)
- 2026-10-02 01:30 [macd_momentum] CIERRE MINA momentum perdido bruto +0.52% neto +0.02%
- 2026-10-02 01:30 [macd_momentum_regimen] CIERRE MINA momentum perdido bruto +0.52% neto +0.02%
- 2026-10-02 01:30 [macd_momentum_evento] CIERRE MINA momentum perdido bruto +0.52% neto +0.02%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
