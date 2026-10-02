# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 02:41 UTC · vueltas 367 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.51 € (-4.19%) | 288 | 23 | 35% | -0.009% | -0.599% | -0.720% | -39.22 € |
| reversion_bb | 919.00 € (-0.57%) | 63 | 9 | 56% | +0.466% | -0.449% | -0.556% | -6.52 € |
| ruptura_volumen | 866.11 € (-6.29%) | 332 | 21 | 25% | -0.190% | -0.768% | -0.876% | -57.31 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.75 € (-3.84%) | 195 | 9 | 15% | -0.178% | -0.813% | -0.902% | -35.98 € |
| macd_momentum | 860.60 € (-6.89%) | 525 | 33 | 21% | -0.002% | -0.551% | -0.654% | -64.69 € |
| estocastico_rebote | 872.58 € (-5.59%) | 344 | 13 | 32% | -0.092% | -0.668% | -0.776% | -51.82 € |
| ruptura_estricta | 881.61 € (-4.61%) | 168 | 27 | 25% | -0.452% | -1.109% | -1.225% | -42.37 € |
| macd_sin_salida | 872.79 € (-5.57%) | 362 | 38 | 34% | -0.072% | -0.644% | -0.757% | -52.72 € |
| c_banda_atr_tope | 911.83 € (-1.34%) | 66 | 5 | 30% | +0.050% | -0.850% | -0.964% | -12.88 € |
| ruptura_volumen_tope | 903.29 € (-2.27%) | 111 | 4 | 25% | -0.080% | -0.818% | -0.933% | -20.77 € |
| c_banda_atr_regimen | 896.33 € (-3.02%) | 139 | 26 | 29% | -0.197% | -0.885% | -1.018% | -28.14 € |
| macd_momentum_regimen | 883.55 € (-4.40%) | 292 | 28 | 20% | -0.029% | -0.619% | -0.725% | -40.94 € |
| ruptura_volumen_regimen | 871.00 € (-5.76%) | 259 | 16 | 21% | -0.303% | -0.904% | -1.017% | -52.74 € |
| c_banda_atr_evento | 891.40 € (-3.55%) | 255 | 23 | 36% | +0.030% | -0.573% | -0.689% | -33.32 € |
| macd_momentum_evento | 865.37 € (-6.37%) | 478 | 33 | 19% | -0.005% | -0.560% | -0.659% | -59.93 € |
| ruptura_volumen_evento | 878.43 € (-4.96%) | 282 | 21 | 26% | -0.112% | -0.706% | -0.806% | -44.97 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 02:40 | macd_momentum_evento | JUP | momentum perdido | -0.85% | -1.35% | -0.29 |
| 2026-10-02 02:40 | macd_momentum_evento | HYPE | momentum perdido | -0.09% | -0.59% | -0.13 |
| 2026-10-02 02:40 | macd_momentum_regimen | JUP | momentum perdido | -0.85% | -1.35% | -0.30 |
| 2026-10-02 02:40 | macd_momentum_regimen | HYPE | momentum perdido | -0.09% | -0.59% | -0.13 |
| 2026-10-02 02:40 | macd_sin_salida | MINA | take-profit | +2.06% | +1.56% | +0.34 |
| 2026-10-02 02:40 | macd_sin_salida | SUI | timeout | +0.48% | -0.02% | -0.01 |
| 2026-10-02 02:40 | macd_momentum | JUP | momentum perdido | -0.85% | -1.35% | -0.29 |
| 2026-10-02 02:40 | macd_momentum | HYPE | momentum perdido | -0.09% | -0.59% | -0.13 |
| 2026-10-02 02:40 | pullback_tendencia | MINA | take-profit | +2.06% | +1.56% | +0.35 |
| 2026-10-02 02:35 | macd_momentum_evento | SPX | momentum perdido | -0.71% | -1.21% | -0.26 |
| 2026-10-02 02:35 | macd_momentum_evento | VVV | momentum perdido | -0.33% | -0.83% | -0.18 |
| 2026-10-02 02:35 | macd_momentum_evento | USELESS | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-02 02:35 | macd_momentum_regimen | SPX | momentum perdido | -0.71% | -1.21% | -0.27 |
| 2026-10-02 02:35 | macd_momentum_regimen | USELESS | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-02 02:35 | macd_momentum | SPX | momentum perdido | -0.71% | -1.21% | -0.26 |

## Eventos de la última vuelta

- 2026-10-02 02:35 [pullback_tendencia] ENTRADA BTC @ 75492.1 (22.20 €, apertura)
- 2026-10-02 02:35 [pullback_tendencia] ENTRADA XRP @ 1.32988 (22.20 €, apertura)
- 2026-10-02 02:40 [macd_sin_salida] CIERRE SUI timeout bruto +0.48% neto -0.02%
- 2026-10-02 02:40 [macd_momentum] CIERRE HYPE momentum perdido bruto -0.09% neto -0.59%
- 2026-10-02 02:40 [macd_momentum_regimen] CIERRE HYPE momentum perdido bruto -0.09% neto -0.59%
- 2026-10-02 02:40 [macd_momentum_evento] CIERRE HYPE momentum perdido bruto -0.09% neto -0.59%
- 2026-10-02 02:35 [pullback_tendencia] ENTRADA ONDO @ 0.44041 (22.20 €, apertura)
- 2026-10-02 02:40 [macd_momentum] CIERRE JUP momentum perdido bruto -0.85% neto -1.35%
- 2026-10-02 02:40 [macd_momentum_regimen] CIERRE JUP momentum perdido bruto -0.85% neto -1.35%
- 2026-10-02 02:40 [macd_momentum_evento] CIERRE JUP momentum perdido bruto -0.85% neto -1.35%
- 2026-10-02 02:40 [pullback_tendencia] CIERRE MINA take-profit bruto +2.06% neto +1.56%
- 2026-10-02 02:35 [macd_momentum] ENTRADA MINA @ 0.1384 (21.49 €, apertura)
- 2026-10-02 02:40 [macd_sin_salida] CIERRE MINA take-profit bruto +2.06% neto +1.56%
- 2026-10-02 02:35 [macd_momentum_regimen] ENTRADA MINA @ 0.1384 (22.08 €, apertura)
- 2026-10-02 02:35 [macd_momentum_evento] ENTRADA MINA @ 0.1384 (21.61 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
