# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 02:36 UTC · vueltas 366 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.61 € (-4.18%) | 288 | 23 | 35% | -0.009% | -0.599% | -0.720% | -39.22 € |
| reversion_bb | 919.13 € (-0.55%) | 63 | 9 | 56% | +0.466% | -0.449% | -0.556% | -6.52 € |
| ruptura_volumen | 866.20 € (-6.28%) | 332 | 21 | 25% | -0.190% | -0.768% | -0.876% | -57.31 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.77 € (-3.84%) | 194 | 7 | 15% | -0.189% | -0.825% | -0.913% | -36.33 € |
| macd_momentum | 860.97 € (-6.85%) | 523 | 34 | 21% | +0.000% | -0.550% | -0.652% | -64.28 € |
| estocastico_rebote | 872.57 € (-5.59%) | 344 | 13 | 32% | -0.092% | -0.668% | -0.776% | -51.82 € |
| ruptura_estricta | 881.75 € (-4.60%) | 168 | 27 | 25% | -0.452% | -1.109% | -1.225% | -42.37 € |
| macd_sin_salida | 873.06 € (-5.54%) | 360 | 40 | 34% | -0.080% | -0.652% | -0.764% | -53.06 € |
| c_banda_atr_tope | 911.87 € (-1.34%) | 66 | 5 | 30% | +0.050% | -0.850% | -0.964% | -12.88 € |
| ruptura_volumen_tope | 903.34 € (-2.26%) | 111 | 4 | 25% | -0.080% | -0.818% | -0.933% | -20.77 € |
| c_banda_atr_regimen | 896.38 € (-3.01%) | 139 | 26 | 29% | -0.197% | -0.885% | -1.018% | -28.14 € |
| macd_momentum_regimen | 883.86 € (-4.37%) | 290 | 29 | 20% | -0.026% | -0.616% | -0.722% | -40.51 € |
| ruptura_volumen_regimen | 870.94 € (-5.77%) | 259 | 16 | 21% | -0.303% | -0.904% | -1.017% | -52.74 € |
| c_banda_atr_evento | 891.50 € (-3.54%) | 255 | 23 | 36% | +0.030% | -0.573% | -0.689% | -33.32 € |
| macd_momentum_evento | 865.74 € (-6.33%) | 476 | 34 | 19% | -0.003% | -0.558% | -0.657% | -59.51 € |
| ruptura_volumen_evento | 878.52 € (-4.95%) | 282 | 21 | 26% | -0.112% | -0.706% | -0.806% | -44.97 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 02:35 | macd_momentum_evento | SPX | momentum perdido | -0.71% | -1.21% | -0.26 |
| 2026-10-02 02:35 | macd_momentum_evento | VVV | momentum perdido | -0.33% | -0.83% | -0.18 |
| 2026-10-02 02:35 | macd_momentum_evento | USELESS | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-02 02:35 | macd_momentum_regimen | SPX | momentum perdido | -0.71% | -1.21% | -0.27 |
| 2026-10-02 02:35 | macd_momentum_regimen | USELESS | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-02 02:35 | macd_momentum | SPX | momentum perdido | -0.71% | -1.21% | -0.26 |
| 2026-10-02 02:35 | macd_momentum | VVV | momentum perdido | -0.33% | -0.83% | -0.18 |
| 2026-10-02 02:35 | macd_momentum | USELESS | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-02 02:30 | macd_momentum_evento | INJ | momentum perdido | -0.50% | -1.00% | -0.22 |
| 2026-10-02 02:30 | macd_momentum_evento | ZRO | momentum perdido | -0.91% | -1.41% | -0.31 |
| 2026-10-02 02:30 | macd_momentum_regimen | INJ | momentum perdido | -0.50% | -1.00% | -0.22 |
| 2026-10-02 02:30 | macd_momentum_regimen | ZRO | momentum perdido | -0.91% | -1.41% | -0.31 |
| 2026-10-02 02:30 | ruptura_estricta | QNT | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-02 02:30 | estocastico_rebote | BNB | timeout | +0.21% | -0.29% | -0.06 |
| 2026-10-02 02:30 | macd_momentum | INJ | momentum perdido | -0.50% | -1.00% | -0.21 |

## Eventos de la última vuelta

- 2026-10-02 02:30 [pullback_tendencia] ENTRADA SUI @ 1.0497 (22.20 €, apertura)
- 2026-10-02 02:30 [pullback_tendencia] ENTRADA LTC @ 61.24 (22.20 €, apertura)
- 2026-10-02 02:35 [macd_momentum] CIERRE USELESS momentum perdido bruto -0.15% neto -0.65%
- 2026-10-02 02:35 [macd_momentum_regimen] CIERRE USELESS momentum perdido bruto -0.15% neto -0.65%
- 2026-10-02 02:35 [macd_momentum_evento] CIERRE USELESS momentum perdido bruto -0.15% neto -0.65%
- 2026-10-02 02:35 [macd_momentum] CIERRE VVV momentum perdido bruto -0.33% neto -0.83%
- 2026-10-02 02:35 [macd_momentum_evento] CIERRE VVV momentum perdido bruto -0.33% neto -0.83%
- 2026-10-02 02:35 [macd_momentum] CIERRE SPX momentum perdido bruto -0.71% neto -1.21%
- 2026-10-02 02:35 [macd_momentum_regimen] CIERRE SPX momentum perdido bruto -0.71% neto -1.21%
- 2026-10-02 02:35 [macd_momentum_evento] CIERRE SPX momentum perdido bruto -0.71% neto -1.21%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
