# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 07:36 UTC · vueltas 380 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.91 € (-3.93%) | 333 | 15 | 39% | +0.124% | -0.454% | -0.575% | -34.48 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 862.32 € (-6.70%) | 408 | 8 | 26% | -0.116% | -0.680% | -0.787% | -62.18 € |
| rebote_extremo | 922.53 € (-0.18%) | 14 | 1 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.18 € (-3.79%) | 236 | 7 | 20% | -0.033% | -0.645% | -0.731% | -34.58 € |
| macd_momentum | 853.44 € (-7.66%) | 645 | 3 | 22% | +0.046% | -0.494% | -0.596% | -70.98 € |
| estocastico_rebote | 875.33 € (-5.29%) | 386 | 34 | 36% | +0.038% | -0.529% | -0.637% | -46.27 € |
| ruptura_estricta | 882.01 € (-4.57%) | 229 | 7 | 32% | -0.182% | -0.797% | -0.911% | -41.54 € |
| macd_sin_salida | 878.69 € (-4.93%) | 432 | 16 | 40% | +0.113% | -0.447% | -0.558% | -44.02 € |
| c_banda_atr_tope | 912.76 € (-1.24%) | 76 | 3 | 37% | +0.213% | -0.634% | -0.750% | -11.08 € |
| ruptura_volumen_tope | 901.91 € (-2.42%) | 124 | 4 | 25% | -0.070% | -0.782% | -0.894% | -22.18 € |
| c_banda_atr_regimen | 900.32 € (-2.59%) | 185 | 16 | 40% | +0.131% | -0.510% | -0.640% | -21.73 € |
| macd_momentum_regimen | 876.29 € (-5.19%) | 408 | 3 | 22% | +0.041% | -0.523% | -0.626% | -48.11 € |
| ruptura_volumen_regimen | 867.00 € (-6.19%) | 331 | 8 | 24% | -0.194% | -0.773% | -0.885% | -57.50 € |
| c_banda_atr_evento | 893.82 € (-3.29%) | 300 | 15 | 40% | +0.172% | -0.416% | -0.533% | -28.56 € |
| macd_momentum_evento | 858.16 € (-7.15%) | 598 | 3 | 21% | +0.048% | -0.497% | -0.595% | -66.25 € |
| ruptura_volumen_evento | 874.58 € (-5.37%) | 358 | 8 | 27% | -0.045% | -0.619% | -0.720% | -49.91 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 07:35 | ruptura_volumen_evento | ASTER | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-02 07:35 | c_banda_atr_evento | UNI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 07:35 | ruptura_volumen_regimen | ASTER | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-02 07:35 | c_banda_atr_regimen | UNI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 07:35 | ruptura_volumen_tope | ASTER | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-02 07:35 | c_banda_atr_tope | UNI | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-02 07:35 | estocastico_rebote | PEPE | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 07:35 | pullback_tendencia | TRUMP | rotura de tendencia | -0.59% | -1.09% | -0.24 |
| 2026-10-02 07:35 | ruptura_volumen | ASTER | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-02 07:35 | c_banda_atr | UNI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 07:30 | macd_momentum_evento | ASTER | momentum perdido | -0.76% | -1.26% | -0.27 |
| 2026-10-02 07:30 | macd_momentum_evento | PUMP | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 07:30 | macd_momentum_regimen | ASTER | momentum perdido | -0.76% | -1.26% | -0.28 |
| 2026-10-02 07:30 | macd_momentum_regimen | PUMP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 07:30 | macd_sin_salida | KAS | timeout | -0.93% | -1.43% | -0.31 |

## Eventos de la última vuelta

- 2026-10-02 07:30 [estocastico_rebote] ENTRADA LINK @ 12.6758 (21.96 €, apertura)
- 2026-10-02 07:30 [ruptura_volumen] ENTRADA PUMP @ 0.00538 (21.56 €, apertura)
- 2026-10-02 07:30 [ruptura_volumen_tope] ENTRADA PUMP @ 0.00538 (22.56 €, apertura)
- 2026-10-02 07:30 [ruptura_volumen_regimen] ENTRADA PUMP @ 0.00538 (21.67 €, apertura)
- 2026-10-02 07:30 [ruptura_volumen_evento] ENTRADA PUMP @ 0.00538 (21.86 €, apertura)
- 2026-10-02 07:35 [c_banda_atr] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 07:35 [c_banda_atr_tope] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 07:35 [c_banda_atr_regimen] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 07:35 [c_banda_atr_evento] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 07:30 [estocastico_rebote] ENTRADA CRV @ 0.33662 (21.96 €, apertura)
- 2026-10-02 07:35 [estocastico_rebote] CIERRE PEPE stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 07:35 [ruptura_volumen] CIERRE ASTER timeout bruto -0.36% neto -0.86%
- 2026-10-02 07:35 [ruptura_volumen_tope] CIERRE ASTER timeout bruto -0.36% neto -0.86%
- 2026-10-02 07:35 [ruptura_volumen_regimen] CIERRE ASTER timeout bruto -0.36% neto -0.86%
- 2026-10-02 07:35 [ruptura_volumen_evento] CIERRE ASTER timeout bruto -0.36% neto -0.86%
- 2026-10-02 07:30 [estocastico_rebote] ENTRADA PENGU @ 0.008751 (21.95 €, apertura)
- 2026-10-02 07:35 [pullback_tendencia] CIERRE TRUMP rotura de tendencia bruto -0.59% neto -1.09%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
