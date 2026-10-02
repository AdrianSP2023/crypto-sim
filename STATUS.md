# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 01:51 UTC · vueltas 357 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 883.44 € (-4.41%) | 275 | 26 | 34% | -0.044% | -0.639% | -0.760% | -39.87 € |
| reversion_bb | 916.84 € (-0.80%) | 58 | 14 | 52% | +0.367% | -0.583% | -0.693% | -7.79 € |
| ruptura_volumen | 865.84 € (-6.32%) | 311 | 25 | 23% | -0.232% | -0.816% | -0.923% | -57.01 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.15 € (-3.90%) | 193 | 5 | 15% | -0.201% | -0.837% | -0.925% | -36.66 € |
| macd_momentum | 860.35 € (-6.91%) | 516 | 7 | 21% | -0.003% | -0.553% | -0.655% | -63.83 € |
| estocastico_rebote | 871.82 € (-5.67%) | 339 | 15 | 32% | -0.096% | -0.673% | -0.783% | -51.46 € |
| ruptura_estricta | 881.61 € (-4.61%) | 167 | 13 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 869.98 € (-5.87%) | 357 | 18 | 34% | -0.097% | -0.670% | -0.782% | -54.04 € |
| c_banda_atr_tope | 911.35 € (-1.39%) | 64 | 5 | 30% | +0.028% | -0.884% | -1.001% | -13.00 € |
| ruptura_volumen_tope | 903.45 € (-2.25%) | 108 | 3 | 25% | -0.083% | -0.827% | -0.940% | -20.45 € |
| c_banda_atr_regimen | 895.63 € (-3.10%) | 139 | 7 | 29% | -0.197% | -0.885% | -1.018% | -28.14 € |
| macd_momentum_regimen | 884.34 € (-4.32%) | 285 | 0 | 20% | -0.026% | -0.618% | -0.723% | -39.89 € |
| ruptura_volumen_regimen | 870.30 € (-5.84%) | 239 | 21 | 19% | -0.372% | -0.981% | -1.095% | -52.84 € |
| c_banda_atr_evento | 889.32 € (-3.78%) | 242 | 26 | 34% | -0.007% | -0.616% | -0.733% | -33.98 € |
| macd_momentum_evento | 865.12 € (-6.40%) | 469 | 7 | 19% | -0.006% | -0.562% | -0.660% | -59.06 € |
| ruptura_volumen_evento | 878.16 € (-4.99%) | 261 | 25 | 24% | -0.156% | -0.757% | -0.856% | -44.67 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 01:50 | ruptura_volumen_evento | AVAX | timeout | -0.98% | -1.48% | -0.33 |
| 2026-10-02 01:50 | macd_momentum_evento | ICP | momentum perdido | -0.31% | -0.81% | -0.17 |
| 2026-10-02 01:50 | ruptura_volumen_tope | AVAX | timeout | -0.98% | -1.48% | -0.34 |
| 2026-10-02 01:50 | macd_momentum | ICP | momentum perdido | -0.31% | -0.81% | -0.17 |
| 2026-10-02 01:50 | ruptura_volumen | AVAX | timeout | -0.98% | -1.48% | -0.32 |
| 2026-10-02 01:45 | ruptura_volumen_evento | MON | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 01:45 | macd_momentum_evento | INJ | momentum perdido | -0.12% | -0.62% | -0.13 |
| 2026-10-02 01:45 | macd_momentum_evento | MON | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 01:45 | macd_momentum_evento | TAO | momentum perdido | -0.16% | -0.66% | -0.14 |
| 2026-10-02 01:45 | c_banda_atr_evento | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 01:45 | ruptura_volumen_tope | MON | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-02 01:45 | macd_sin_salida | MON | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 01:45 | macd_momentum | INJ | momentum perdido | -0.12% | -0.62% | -0.13 |
| 2026-10-02 01:45 | macd_momentum | MON | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 01:45 | macd_momentum | TAO | momentum perdido | -0.16% | -0.66% | -0.14 |

## Eventos de la última vuelta

- 2026-10-02 01:50 [ruptura_volumen] CIERRE AVAX timeout bruto -0.98% neto -1.48%
- 2026-10-02 01:50 [ruptura_volumen_tope] CIERRE AVAX timeout bruto -0.98% neto -1.48%
- 2026-10-02 01:50 [ruptura_volumen_evento] CIERRE AVAX timeout bruto -0.98% neto -1.48%
- 2026-10-02 01:50 [macd_momentum] CIERRE ICP momentum perdido bruto -0.31% neto -0.81%
- 2026-10-02 01:50 [macd_momentum_evento] CIERRE ICP momentum perdido bruto -0.31% neto -0.81%
- 2026-10-02 01:45 [macd_momentum] ENTRADA RENDER @ 1.703 (21.51 €, apertura)
- 2026-10-02 01:45 [macd_sin_salida] ENTRADA RENDER @ 1.703 (21.76 €, apertura)
- 2026-10-02 01:45 [macd_momentum_evento] ENTRADA RENDER @ 1.703 (21.63 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
