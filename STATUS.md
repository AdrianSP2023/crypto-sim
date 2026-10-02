# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 07:46 UTC · vueltas 382 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.09 € (-3.80%) | 333 | 16 | 39% | +0.124% | -0.454% | -0.575% | -34.48 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 862.29 € (-6.70%) | 410 | 6 | 26% | -0.119% | -0.682% | -0.790% | -62.65 € |
| rebote_extremo | 922.56 € (-0.18%) | 14 | 1 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.47 € (-3.76%) | 237 | 6 | 20% | -0.036% | -0.647% | -0.733% | -34.84 € |
| macd_momentum | 853.61 € (-7.64%) | 645 | 4 | 22% | +0.046% | -0.494% | -0.596% | -70.98 € |
| estocastico_rebote | 877.62 € (-5.04%) | 386 | 40 | 36% | +0.038% | -0.529% | -0.637% | -46.27 € |
| ruptura_estricta | 882.58 € (-4.51%) | 229 | 7 | 32% | -0.182% | -0.797% | -0.911% | -41.54 € |
| macd_sin_salida | 879.54 € (-4.84%) | 432 | 17 | 40% | +0.113% | -0.447% | -0.558% | -44.02 € |
| c_banda_atr_tope | 912.99 € (-1.22%) | 76 | 5 | 37% | +0.213% | -0.634% | -0.750% | -11.08 € |
| ruptura_volumen_tope | 901.33 € (-2.48%) | 126 | 2 | 25% | -0.078% | -0.787% | -0.901% | -22.68 € |
| c_banda_atr_regimen | 901.59 € (-2.45%) | 185 | 17 | 40% | +0.131% | -0.510% | -0.640% | -21.73 € |
| macd_momentum_regimen | 876.47 € (-5.17%) | 408 | 4 | 22% | +0.041% | -0.523% | -0.626% | -48.11 € |
| ruptura_volumen_regimen | 866.97 € (-6.20%) | 333 | 6 | 24% | -0.197% | -0.775% | -0.888% | -57.98 € |
| c_banda_atr_evento | 895.01 € (-3.16%) | 300 | 16 | 40% | +0.172% | -0.416% | -0.533% | -28.56 € |
| macd_momentum_evento | 858.34 € (-7.13%) | 598 | 4 | 21% | +0.048% | -0.497% | -0.595% | -66.25 € |
| ruptura_volumen_evento | 874.56 € (-5.38%) | 360 | 6 | 27% | -0.048% | -0.621% | -0.723% | -50.39 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 07:45 | ruptura_volumen_evento | XMR | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 07:45 | ruptura_volumen_regimen | XMR | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 07:45 | ruptura_volumen_tope | XMR | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 07:45 | ruptura_volumen | XMR | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 07:40 | ruptura_volumen_evento | MON | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:40 | ruptura_volumen_regimen | MON | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:40 | ruptura_volumen_tope | MON | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 07:40 | pullback_tendencia | ADA | rotura de tendencia | -0.65% | -1.15% | -0.26 |
| 2026-10-02 07:40 | ruptura_volumen | MON | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:35 | ruptura_volumen_evento | ASTER | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-02 07:35 | c_banda_atr_evento | UNI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 07:35 | ruptura_volumen_regimen | ASTER | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-02 07:35 | c_banda_atr_regimen | UNI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 07:35 | ruptura_volumen_tope | ASTER | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-02 07:35 | c_banda_atr_tope | UNI | stop-loss | -1.50% | -2.00% | -0.46 |

## Eventos de la última vuelta

- 2026-10-02 07:40 [estocastico_rebote] ENTRADA LTC @ 62.02 (21.95 €, apertura)
- 2026-10-02 07:40 [c_banda_atr_tope] ENTRADA POL @ 0.098 (22.83 €, apertura)
- 2026-10-02 07:40 [estocastico_rebote] ENTRADA ONDO @ 0.44516 (21.95 €, apertura)
- 2026-10-02 07:40 [estocastico_rebote] ENTRADA VVV @ 25.142 (21.95 €, apertura)
- 2026-10-02 07:40 [macd_momentum] ENTRADA SKY @ 0.075 (21.33 €, apertura)
- 2026-10-02 07:40 [macd_sin_salida] ENTRADA SKY @ 0.075 (22.01 €, apertura)
- 2026-10-02 07:40 [macd_momentum_regimen] ENTRADA SKY @ 0.075 (21.90 €, apertura)
- 2026-10-02 07:40 [macd_momentum_evento] ENTRADA SKY @ 0.075 (21.45 €, apertura)
- 2026-10-02 07:45 [ruptura_volumen] CIERRE XMR timeout bruto +0.00% neto -0.50%
- 2026-10-02 07:45 [ruptura_volumen_tope] CIERRE XMR timeout bruto +0.00% neto -0.50%
- 2026-10-02 07:45 [ruptura_volumen_regimen] CIERRE XMR timeout bruto +0.00% neto -0.50%
- 2026-10-02 07:45 [ruptura_volumen_evento] CIERRE XMR timeout bruto +0.00% neto -0.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
