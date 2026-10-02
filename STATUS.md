# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 07:41 UTC · vueltas 381 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.27 € (-3.89%) | 333 | 16 | 39% | +0.124% | -0.454% | -0.575% | -34.48 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 861.76 € (-6.76%) | 409 | 7 | 26% | -0.119% | -0.683% | -0.790% | -62.55 € |
| rebote_extremo | 922.48 € (-0.19%) | 14 | 1 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.03 € (-3.81%) | 237 | 6 | 20% | -0.036% | -0.647% | -0.733% | -34.84 € |
| macd_momentum | 853.43 € (-7.66%) | 645 | 3 | 22% | +0.046% | -0.494% | -0.596% | -70.98 € |
| estocastico_rebote | 875.71 € (-5.25%) | 386 | 37 | 36% | +0.038% | -0.529% | -0.637% | -46.27 € |
| ruptura_estricta | 882.00 € (-4.57%) | 229 | 7 | 32% | -0.182% | -0.797% | -0.911% | -41.54 € |
| macd_sin_salida | 878.76 € (-4.92%) | 432 | 16 | 40% | +0.113% | -0.447% | -0.558% | -44.02 € |
| c_banda_atr_tope | 912.82 € (-1.24%) | 76 | 4 | 37% | +0.213% | -0.634% | -0.750% | -11.08 € |
| ruptura_volumen_tope | 901.36 € (-2.48%) | 125 | 3 | 25% | -0.079% | -0.790% | -0.903% | -22.56 € |
| c_banda_atr_regimen | 900.75 € (-2.54%) | 185 | 17 | 40% | +0.131% | -0.510% | -0.640% | -21.73 € |
| macd_momentum_regimen | 876.29 € (-5.19%) | 408 | 3 | 22% | +0.041% | -0.523% | -0.626% | -48.11 € |
| ruptura_volumen_regimen | 866.44 € (-6.25%) | 332 | 7 | 24% | -0.197% | -0.776% | -0.888% | -57.87 € |
| c_banda_atr_evento | 894.18 € (-3.25%) | 300 | 16 | 40% | +0.172% | -0.416% | -0.533% | -28.56 € |
| macd_momentum_evento | 858.16 € (-7.15%) | 598 | 3 | 21% | +0.048% | -0.497% | -0.595% | -66.25 € |
| ruptura_volumen_evento | 874.02 € (-5.43%) | 359 | 7 | 27% | -0.048% | -0.622% | -0.723% | -50.28 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-02 07:35 | estocastico_rebote | PEPE | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 07:35 | pullback_tendencia | TRUMP | rotura de tendencia | -0.59% | -1.09% | -0.24 |
| 2026-10-02 07:35 | ruptura_volumen | ASTER | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-02 07:35 | c_banda_atr | UNI | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-10-02 07:40 [pullback_tendencia] CIERRE ADA rotura de tendencia bruto -0.65% neto -1.15%
- 2026-10-02 07:35 [estocastico_rebote] ENTRADA HBAR @ 0.09211 (21.95 €, apertura)
- 2026-10-02 07:35 [estocastico_rebote] ENTRADA HYPE @ 79.83 (21.95 €, apertura)
- 2026-10-02 07:40 [ruptura_volumen] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:40 [ruptura_volumen_tope] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:40 [ruptura_volumen_regimen] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:40 [ruptura_volumen_evento] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:35 [c_banda_atr] ENTRADA WLFI @ 0.0499 (22.24 €, apertura)
- 2026-10-02 07:35 [estocastico_rebote] ENTRADA WLFI @ 0.0499 (21.95 €, apertura)
- 2026-10-02 07:35 [c_banda_atr_tope] ENTRADA WLFI @ 0.0499 (22.83 €, apertura)
- 2026-10-02 07:35 [c_banda_atr_regimen] ENTRADA WLFI @ 0.0499 (22.56 €, apertura)
- 2026-10-02 07:35 [c_banda_atr_evento] ENTRADA WLFI @ 0.0499 (22.39 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
