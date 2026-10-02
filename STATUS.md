# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 01:56 UTC · vueltas 358 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.72 € (-4.17%) | 275 | 26 | 34% | -0.044% | -0.639% | -0.760% | -39.87 € |
| reversion_bb | 917.91 € (-0.69%) | 59 | 13 | 53% | +0.386% | -0.556% | -0.664% | -7.57 € |
| ruptura_volumen | 867.93 € (-6.09%) | 312 | 25 | 23% | -0.232% | -0.815% | -0.922% | -57.16 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.59 € (-3.86%) | 193 | 6 | 15% | -0.201% | -0.837% | -0.925% | -36.66 € |
| macd_momentum | 860.76 € (-6.87%) | 516 | 7 | 21% | -0.003% | -0.553% | -0.655% | -63.83 € |
| estocastico_rebote | 872.95 € (-5.55%) | 339 | 15 | 32% | -0.096% | -0.673% | -0.783% | -51.46 € |
| ruptura_estricta | 882.72 € (-4.49%) | 167 | 14 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 871.78 € (-5.68%) | 357 | 18 | 34% | -0.097% | -0.670% | -0.782% | -54.04 € |
| c_banda_atr_tope | 911.83 € (-1.34%) | 64 | 5 | 30% | +0.028% | -0.884% | -1.001% | -13.00 € |
| ruptura_volumen_tope | 903.67 € (-2.23%) | 108 | 4 | 25% | -0.083% | -0.827% | -0.940% | -20.45 € |
| c_banda_atr_regimen | 896.25 € (-3.03%) | 139 | 7 | 29% | -0.197% | -0.885% | -1.018% | -28.14 € |
| macd_momentum_regimen | 884.34 € (-4.32%) | 285 | 0 | 20% | -0.026% | -0.618% | -0.723% | -39.89 € |
| ruptura_volumen_regimen | 872.11 € (-5.64%) | 239 | 21 | 19% | -0.372% | -0.981% | -1.095% | -52.84 € |
| c_banda_atr_evento | 891.61 € (-3.53%) | 242 | 26 | 34% | -0.007% | -0.616% | -0.733% | -33.98 € |
| macd_momentum_evento | 865.53 € (-6.35%) | 469 | 7 | 19% | -0.006% | -0.562% | -0.660% | -59.06 € |
| ruptura_volumen_evento | 880.28 € (-4.76%) | 262 | 25 | 24% | -0.156% | -0.757% | -0.856% | -44.81 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 01:55 | ruptura_volumen_evento | SHIB | timeout | -0.15% | -0.66% | -0.14 |
| 2026-10-02 01:55 | ruptura_volumen | SHIB | timeout | -0.15% | -0.66% | -0.14 |
| 2026-10-02 01:55 | reversion_bb | SOL | take-profit | +1.50% | +1.00% | +0.23 |
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

## Eventos de la última vuelta

- 2026-10-02 01:55 [reversion_bb] CIERRE SOL take-profit bruto +1.50% neto +1.00%
- 2026-10-02 01:50 [pullback_tendencia] ENTRADA AAVE @ 155.8 (22.19 €, apertura)
- 2026-10-02 01:50 [ruptura_volumen] ENTRADA NIGHT @ 0.03502 (21.68 €, apertura)
- 2026-10-02 01:50 [ruptura_estricta] ENTRADA NIGHT @ 0.03502 (22.06 €, apertura)
- 2026-10-02 01:50 [ruptura_volumen_tope] ENTRADA NIGHT @ 0.03502 (22.59 €, apertura)
- 2026-10-02 01:50 [ruptura_volumen_evento] ENTRADA NIGHT @ 0.03502 (21.99 €, apertura)
- 2026-10-02 01:55 [ruptura_volumen] CIERRE SHIB timeout bruto -0.16% neto -0.66%
- 2026-10-02 01:55 [ruptura_volumen_evento] CIERRE SHIB timeout bruto -0.16% neto -0.66%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
