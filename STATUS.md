# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 01:46 UTC · vueltas 356 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 883.13 € (-4.45%) | 275 | 26 | 34% | -0.044% | -0.639% | -0.760% | -39.87 € |
| reversion_bb | 916.75 € (-0.81%) | 58 | 14 | 52% | +0.367% | -0.583% | -0.693% | -7.79 € |
| ruptura_volumen | 865.71 € (-6.33%) | 310 | 26 | 24% | -0.229% | -0.814% | -0.921% | -56.69 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.14 € (-3.91%) | 193 | 5 | 15% | -0.201% | -0.837% | -0.925% | -36.66 € |
| macd_momentum | 860.45 € (-6.90%) | 515 | 7 | 21% | -0.002% | -0.553% | -0.655% | -63.65 € |
| estocastico_rebote | 871.87 € (-5.67%) | 339 | 15 | 32% | -0.096% | -0.673% | -0.783% | -51.46 € |
| ruptura_estricta | 881.55 € (-4.62%) | 167 | 13 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 869.91 € (-5.88%) | 357 | 17 | 34% | -0.097% | -0.670% | -0.782% | -54.04 € |
| c_banda_atr_tope | 911.30 € (-1.40%) | 64 | 5 | 30% | +0.028% | -0.884% | -1.001% | -13.00 € |
| ruptura_volumen_tope | 903.46 € (-2.25%) | 107 | 4 | 25% | -0.075% | -0.821% | -0.935% | -20.11 € |
| c_banda_atr_regimen | 895.53 € (-3.11%) | 139 | 7 | 29% | -0.197% | -0.885% | -1.018% | -28.14 € |
| macd_momentum_regimen | 884.34 € (-4.32%) | 285 | 0 | 20% | -0.026% | -0.618% | -0.723% | -39.89 € |
| ruptura_volumen_regimen | 870.25 € (-5.84%) | 239 | 21 | 19% | -0.372% | -0.981% | -1.095% | -52.84 € |
| c_banda_atr_evento | 889.00 € (-3.81%) | 242 | 26 | 34% | -0.007% | -0.616% | -0.733% | -33.98 € |
| macd_momentum_evento | 865.22 € (-6.39%) | 468 | 7 | 19% | -0.005% | -0.562% | -0.660% | -58.88 € |
| ruptura_volumen_evento | 878.03 € (-5.00%) | 260 | 26 | 24% | -0.153% | -0.754% | -0.854% | -44.34 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-02 01:45 | ruptura_volumen | MON | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 01:45 | c_banda_atr | ZRO | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 01:40 | ruptura_volumen_evento | ONDO | timeout | -0.64% | -1.14% | -0.25 |
| 2026-10-02 01:40 | macd_momentum_evento | USELESS | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 01:40 | ruptura_volumen_tope | ONDO | timeout | -0.64% | -1.14% | -0.26 |

## Eventos de la última vuelta

- 2026-10-02 01:45 [macd_momentum] CIERRE TAO momentum perdido bruto -0.16% neto -0.66%
- 2026-10-02 01:45 [macd_momentum_evento] CIERRE TAO momentum perdido bruto -0.16% neto -0.66%
- 2026-10-02 01:45 [c_banda_atr] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 01:45 [c_banda_atr_evento] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 01:40 [macd_momentum] ENTRADA CRV @ 0.33518 (21.53 €, apertura)
- 2026-10-02 01:40 [macd_sin_salida] ENTRADA CRV @ 0.33518 (21.77 €, apertura)
- 2026-10-02 01:40 [macd_momentum_evento] ENTRADA CRV @ 0.33518 (21.65 €, apertura)
- 2026-10-02 01:45 [ruptura_volumen] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 01:45 [macd_momentum] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 01:45 [macd_sin_salida] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 01:45 [ruptura_volumen_tope] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 01:45 [macd_momentum_evento] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 01:45 [ruptura_volumen_evento] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 01:45 [macd_momentum] CIERRE INJ momentum perdido bruto -0.12% neto -0.62%
- 2026-10-02 01:45 [macd_momentum_evento] CIERRE INJ momentum perdido bruto -0.12% neto -0.62%
- 2026-10-02 01:40 [macd_momentum] ENTRADA KAS @ 0.03675 (21.51 €, apertura)
- 2026-10-02 01:40 [macd_sin_salida] ENTRADA KAS @ 0.03675 (21.76 €, apertura)
- 2026-10-02 01:40 [macd_momentum_evento] ENTRADA KAS @ 0.03675 (21.63 €, apertura)
- 2026-10-02 01:40 [c_banda_atr] ENTRADA SEI @ 0.06252 (22.11 €, apertura)
- 2026-10-02 01:40 [c_banda_atr_evento] ENTRADA SEI @ 0.06252 (22.26 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
