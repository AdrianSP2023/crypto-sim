# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 02:31 UTC · vueltas 365 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.70 € (-4.17%) | 288 | 23 | 35% | -0.009% | -0.599% | -0.720% | -39.22 € |
| reversion_bb | 919.14 € (-0.55%) | 63 | 9 | 56% | +0.466% | -0.449% | -0.556% | -6.52 € |
| ruptura_volumen | 866.32 € (-6.27%) | 332 | 21 | 25% | -0.190% | -0.768% | -0.876% | -57.31 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.66 € (-3.85%) | 194 | 5 | 15% | -0.189% | -0.825% | -0.913% | -36.33 € |
| macd_momentum | 861.86 € (-6.75%) | 520 | 37 | 21% | +0.002% | -0.548% | -0.650% | -63.70 € |
| estocastico_rebote | 872.70 € (-5.58%) | 344 | 13 | 32% | -0.092% | -0.668% | -0.776% | -51.82 € |
| ruptura_estricta | 881.73 € (-4.60%) | 168 | 27 | 25% | -0.452% | -1.109% | -1.225% | -42.37 € |
| macd_sin_salida | 873.51 € (-5.49%) | 360 | 40 | 34% | -0.080% | -0.652% | -0.764% | -53.06 € |
| c_banda_atr_tope | 911.95 € (-1.33%) | 66 | 5 | 30% | +0.050% | -0.850% | -0.964% | -12.88 € |
| ruptura_volumen_tope | 903.53 € (-2.24%) | 111 | 4 | 25% | -0.080% | -0.818% | -0.933% | -20.77 € |
| c_banda_atr_regimen | 896.54 € (-3.00%) | 139 | 26 | 29% | -0.197% | -0.885% | -1.018% | -28.14 € |
| macd_momentum_regimen | 884.62 € (-4.29%) | 288 | 31 | 20% | -0.024% | -0.614% | -0.719% | -40.10 € |
| ruptura_volumen_regimen | 870.90 € (-5.77%) | 259 | 16 | 21% | -0.303% | -0.904% | -1.017% | -52.74 € |
| c_banda_atr_evento | 891.60 € (-3.53%) | 255 | 23 | 36% | +0.030% | -0.573% | -0.689% | -33.32 € |
| macd_momentum_evento | 866.63 € (-6.23%) | 473 | 37 | 19% | -0.000% | -0.556% | -0.655% | -58.93 € |
| ruptura_volumen_evento | 878.65 € (-4.93%) | 282 | 21 | 26% | -0.112% | -0.706% | -0.806% | -44.97 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 02:30 | macd_momentum_evento | INJ | momentum perdido | -0.50% | -1.00% | -0.22 |
| 2026-10-02 02:30 | macd_momentum_evento | ZRO | momentum perdido | -0.91% | -1.41% | -0.31 |
| 2026-10-02 02:30 | macd_momentum_regimen | INJ | momentum perdido | -0.50% | -1.00% | -0.22 |
| 2026-10-02 02:30 | macd_momentum_regimen | ZRO | momentum perdido | -0.91% | -1.41% | -0.31 |
| 2026-10-02 02:30 | ruptura_estricta | QNT | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-02 02:30 | estocastico_rebote | BNB | timeout | +0.21% | -0.29% | -0.06 |
| 2026-10-02 02:30 | macd_momentum | INJ | momentum perdido | -0.50% | -1.00% | -0.21 |
| 2026-10-02 02:30 | macd_momentum | ZRO | momentum perdido | -0.91% | -1.41% | -0.30 |
| 2026-10-02 02:25 | ruptura_volumen_evento | BNB | timeout | +0.07% | -0.43% | -0.09 |
| 2026-10-02 02:25 | ruptura_volumen_evento | KSM | timeout | -0.88% | -1.38% | -0.30 |
| 2026-10-02 02:25 | ruptura_volumen_evento | CRV | timeout | +0.55% | +0.05% | +0.01 |
| 2026-10-02 02:25 | ruptura_volumen_evento | DOT | timeout | +1.22% | +0.72% | +0.16 |
| 2026-10-02 02:25 | ruptura_volumen_evento | ADA | timeout | +0.43% | -0.07% | -0.02 |
| 2026-10-02 02:25 | ruptura_volumen_regimen | BNB | timeout | +0.07% | -0.43% | -0.09 |
| 2026-10-02 02:25 | ruptura_volumen_regimen | KSM | timeout | -0.88% | -1.38% | -0.30 |

## Eventos de la última vuelta

- 2026-10-02 02:30 [ruptura_estricta] CIERRE QNT stop-loss bruto -2.00% neto -2.50%
- 2026-10-02 02:30 [macd_momentum] CIERRE ZRO momentum perdido bruto -0.91% neto -1.41%
- 2026-10-02 02:30 [macd_momentum_regimen] CIERRE ZRO momentum perdido bruto -0.91% neto -1.41%
- 2026-10-02 02:30 [macd_momentum_evento] CIERRE ZRO momentum perdido bruto -0.91% neto -1.41%
- 2026-10-02 02:30 [macd_momentum] CIERRE INJ momentum perdido bruto -0.50% neto -1.00%
- 2026-10-02 02:30 [macd_momentum_regimen] CIERRE INJ momentum perdido bruto -0.50% neto -1.00%
- 2026-10-02 02:30 [macd_momentum_evento] CIERRE INJ momentum perdido bruto -0.50% neto -1.00%
- 2026-10-02 02:30 [estocastico_rebote] CIERRE BNB timeout bruto +0.21% neto -0.29%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
