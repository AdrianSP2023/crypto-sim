# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 11:56 UTC · vueltas 392 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.28 € (-3.89%) | 361 | 15 | 41% | +0.152% | -0.420% | -0.539% | -34.58 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 1 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 855.14 € (-7.48%) | 454 | 10 | 26% | -0.120% | -0.677% | -0.784% | -68.63 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 888.84 € (-3.83%) | 259 | 12 | 21% | -0.003% | -0.605% | -0.691% | -35.56 € |
| macd_momentum | 846.94 € (-8.36%) | 737 | 9 | 23% | +0.060% | -0.476% | -0.574% | -77.76 € |
| estocastico_rebote | 878.02 € (-5.00%) | 438 | 34 | 38% | +0.116% | -0.444% | -0.551% | -44.12 € |
| ruptura_estricta | 880.37 € (-4.75%) | 247 | 10 | 32% | -0.164% | -0.771% | -0.886% | -43.27 € |
| macd_sin_salida | 875.84 € (-5.24%) | 479 | 26 | 39% | +0.112% | -0.443% | -0.550% | -48.15 € |
| c_banda_atr_tope | 912.89 € (-1.23%) | 82 | 5 | 38% | +0.248% | -0.574% | -0.689% | -10.83 € |
| ruptura_volumen_tope | 898.51 € (-2.78%) | 138 | 2 | 22% | -0.121% | -0.812% | -0.925% | -25.58 € |
| c_banda_atr_regimen | 900.88 € (-2.53%) | 213 | 16 | 42% | +0.176% | -0.447% | -0.572% | -21.90 € |
| macd_momentum_regimen | 869.62 € (-5.91%) | 500 | 9 | 24% | +0.062% | -0.490% | -0.589% | -55.07 € |
| ruptura_volumen_regimen | 859.78 € (-6.97%) | 377 | 10 | 23% | -0.189% | -0.758% | -0.869% | -63.99 € |
| c_banda_atr_evento | 894.19 € (-3.25%) | 328 | 15 | 42% | +0.199% | -0.382% | -0.497% | -28.66 € |
| macd_momentum_evento | 851.63 € (-7.86%) | 690 | 9 | 23% | +0.062% | -0.477% | -0.572% | -73.07 € |
| ruptura_volumen_evento | 867.31 € (-6.16%) | 404 | 10 | 26% | -0.057% | -0.622% | -0.724% | -56.45 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 11:55 | ruptura_volumen_evento | TON | timeout | -0.07% | -0.57% | -0.12 |
| 2026-10-02 11:55 | ruptura_volumen_evento | VVV | timeout | -0.33% | -0.83% | -0.18 |
| 2026-10-02 11:55 | ruptura_volumen_evento | USELESS | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 11:55 | ruptura_volumen_evento | ADA | timeout | -0.44% | -0.94% | -0.21 |
| 2026-10-02 11:55 | macd_momentum_evento | SPX | momentum perdido | -0.03% | -0.53% | -0.11 |
| 2026-10-02 11:55 | c_banda_atr_evento | ASTER | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 11:55 | c_banda_atr_evento | JUP | timeout | -0.95% | -1.45% | -0.32 |
| 2026-10-02 11:55 | c_banda_atr_evento | ICP | timeout | -0.95% | -1.45% | -0.33 |
| 2026-10-02 11:55 | ruptura_volumen_regimen | TON | timeout | -0.07% | -0.57% | -0.12 |
| 2026-10-02 11:55 | ruptura_volumen_regimen | VVV | timeout | -0.33% | -0.83% | -0.18 |
| 2026-10-02 11:55 | ruptura_volumen_regimen | USELESS | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 11:55 | ruptura_volumen_regimen | ADA | timeout | -0.44% | -0.94% | -0.20 |
| 2026-10-02 11:55 | macd_momentum_regimen | SPX | momentum perdido | -0.03% | -0.53% | -0.11 |
| 2026-10-02 11:55 | c_banda_atr_regimen | ASTER | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 11:55 | c_banda_atr_regimen | JUP | timeout | -0.95% | -1.45% | -0.33 |

## Eventos de la última vuelta

- 2026-10-02 11:50 [ruptura_volumen] ENTRADA QNT @ 221 (21.41 €, apertura)
- 2026-10-02 11:50 [ruptura_estricta] ENTRADA QNT @ 221 (22.02 €, apertura)
- 2026-10-02 11:50 [ruptura_volumen_tope] ENTRADA QNT @ 221 (22.48 €, apertura)
- 2026-10-02 11:50 [ruptura_volumen_regimen] ENTRADA QNT @ 221 (21.53 €, apertura)
- 2026-10-02 11:50 [ruptura_volumen_evento] ENTRADA QNT @ 221 (21.72 €, apertura)
- 2026-10-02 11:55 [ruptura_volumen] CIERRE ADA timeout bruto -0.44% neto -0.94%
- 2026-10-02 11:55 [ruptura_volumen_tope] CIERRE ADA timeout bruto -0.44% neto -0.94%
- 2026-10-02 11:55 [ruptura_volumen_regimen] CIERRE ADA timeout bruto -0.44% neto -0.94%
- 2026-10-02 11:55 [ruptura_volumen_evento] CIERRE ADA timeout bruto -0.44% neto -0.94%
- 2026-10-02 11:55 [c_banda_atr] CIERRE ICP timeout bruto -0.95% neto -1.45%
- 2026-10-02 11:55 [c_banda_atr_regimen] CIERRE ICP timeout bruto -0.95% neto -1.45%
- 2026-10-02 11:55 [c_banda_atr_evento] CIERRE ICP timeout bruto -0.95% neto -1.45%
- 2026-10-02 11:55 [ruptura_volumen] CIERRE USELESS stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 11:55 [ruptura_volumen_regimen] CIERRE USELESS stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 11:55 [ruptura_volumen_evento] CIERRE USELESS stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 11:55 [c_banda_atr] CIERRE JUP timeout bruto -0.95% neto -1.45%
- 2026-10-02 11:55 [c_banda_atr_regimen] CIERRE JUP timeout bruto -0.95% neto -1.45%
- 2026-10-02 11:55 [c_banda_atr_evento] CIERRE JUP timeout bruto -0.95% neto -1.45%
- 2026-10-02 11:50 [estocastico_rebote] ENTRADA PEPE @ 3.962e-06 (22.00 €, apertura)
- 2026-10-02 11:50 [estocastico_rebote] ENTRADA MINA @ 0.1426 (22.00 €, apertura)
- 2026-10-02 11:55 [ruptura_volumen] CIERRE VVV timeout bruto -0.33% neto -0.83%
- 2026-10-02 11:50 [pullback_tendencia] ENTRADA VVV @ 26.693 (22.22 €, apertura)
- 2026-10-02 11:55 [ruptura_volumen_tope] CIERRE VVV timeout bruto -0.33% neto -0.83%
- 2026-10-02 11:55 [ruptura_volumen_regimen] CIERRE VVV timeout bruto -0.33% neto -0.83%
- 2026-10-02 11:55 [ruptura_volumen_evento] CIERRE VVV timeout bruto -0.33% neto -0.83%
- 2026-10-02 11:55 [c_banda_atr] CIERRE ASTER stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 11:55 [c_banda_atr_regimen] CIERRE ASTER stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 11:55 [c_banda_atr_evento] CIERRE ASTER stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 11:55 [ruptura_volumen] CIERRE TON timeout bruto -0.07% neto -0.57%
- 2026-10-02 11:55 [ruptura_volumen_tope] CIERRE TON timeout bruto -0.07% neto -0.57%
- 2026-10-02 11:55 [ruptura_volumen_regimen] CIERRE TON timeout bruto -0.07% neto -0.57%
- 2026-10-02 11:55 [ruptura_volumen_evento] CIERRE TON timeout bruto -0.07% neto -0.57%
- 2026-10-02 11:55 [macd_momentum] CIERRE SPX momentum perdido bruto -0.02% neto -0.52%
- 2026-10-02 11:55 [macd_momentum_regimen] CIERRE SPX momentum perdido bruto -0.02% neto -0.52%
- 2026-10-02 11:55 [macd_momentum_evento] CIERRE SPX momentum perdido bruto -0.02% neto -0.52%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
