# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 10:22 UTC · vueltas 413 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.20 € (-3.79%) | 343 | 26 | 40% | +0.140% | -0.436% | -0.555% | -34.09 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 858.10 € (-7.16%) | 443 | 9 | 26% | -0.106% | -0.665% | -0.772% | -65.81 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 890.01 € (-3.70%) | 249 | 8 | 21% | -0.012% | -0.618% | -0.705% | -34.96 € |
| macd_momentum | 851.17 € (-7.91%) | 697 | 21 | 24% | +0.062% | -0.476% | -0.577% | -73.72 € |
| estocastico_rebote | 879.97 € (-4.79%) | 425 | 35 | 38% | +0.106% | -0.455% | -0.562% | -43.91 € |
| ruptura_estricta | 881.88 € (-4.58%) | 238 | 14 | 32% | -0.140% | -0.751% | -0.868% | -40.72 € |
| macd_sin_salida | 879.12 € (-4.88%) | 453 | 36 | 40% | +0.107% | -0.451% | -0.561% | -46.41 € |
| c_banda_atr_tope | 913.19 € (-1.20%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 900.17 € (-2.60%) | 133 | 4 | 23% | -0.101% | -0.800% | -0.912% | -24.29 € |
| c_banda_atr_regimen | 901.82 € (-2.43%) | 196 | 25 | 41% | +0.156% | -0.477% | -0.604% | -21.52 € |
| macd_momentum_regimen | 873.96 € (-5.44%) | 460 | 21 | 24% | +0.065% | -0.492% | -0.594% | -50.93 € |
| ruptura_volumen_regimen | 862.76 € (-6.65%) | 366 | 9 | 24% | -0.174% | -0.745% | -0.858% | -61.16 € |
| c_banda_atr_evento | 895.12 € (-3.15%) | 310 | 26 | 41% | +0.188% | -0.397% | -0.512% | -28.17 € |
| macd_momentum_evento | 855.88 € (-7.40%) | 650 | 21 | 23% | +0.064% | -0.477% | -0.575% | -69.01 € |
| ruptura_volumen_evento | 870.31 € (-5.84%) | 393 | 9 | 27% | -0.039% | -0.607% | -0.709% | -53.59 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 10:20 | ruptura_volumen_evento | TRUMP | timeout | +0.96% | +0.46% | +0.10 |
| 2026-10-02 10:20 | ruptura_volumen_evento | FIL | timeout | -0.97% | -1.47% | -0.32 |
| 2026-10-02 10:20 | ruptura_volumen_evento | RENDER | timeout | -0.51% | -1.01% | -0.22 |
| 2026-10-02 10:20 | ruptura_volumen_evento | NIGHT | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 10:20 | ruptura_volumen_evento | TAO | timeout | -0.22% | -0.72% | -0.16 |
| 2026-10-02 10:20 | ruptura_volumen_evento | LINK | timeout | -0.76% | -1.26% | -0.28 |
| 2026-10-02 10:20 | ruptura_volumen_evento | SOL | timeout | -0.62% | -1.12% | -0.25 |
| 2026-10-02 10:20 | macd_momentum_evento | NIGHT | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 10:20 | macd_momentum_evento | ARB | momentum perdido | -0.65% | -1.15% | -0.25 |
| 2026-10-02 10:20 | c_banda_atr_evento | KAS | timeout | +0.71% | +0.21% | +0.05 |
| 2026-10-02 10:20 | ruptura_volumen_regimen | TRUMP | timeout | +0.96% | +0.46% | +0.10 |
| 2026-10-02 10:20 | ruptura_volumen_regimen | FIL | timeout | -0.97% | -1.47% | -0.32 |
| 2026-10-02 10:20 | ruptura_volumen_regimen | RENDER | timeout | -0.51% | -1.01% | -0.22 |
| 2026-10-02 10:20 | ruptura_volumen_regimen | NIGHT | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 10:20 | ruptura_volumen_regimen | TAO | timeout | -0.22% | -0.72% | -0.16 |

## Eventos de la última vuelta

- 2026-10-02 10:20 [ruptura_volumen] CIERRE SOL timeout bruto -0.62% neto -1.12%
- 2026-10-02 10:20 [ruptura_volumen_regimen] CIERRE SOL timeout bruto -0.62% neto -1.12%
- 2026-10-02 10:20 [ruptura_volumen_evento] CIERRE SOL timeout bruto -0.62% neto -1.12%
- 2026-10-02 10:20 [ruptura_volumen] CIERRE LINK timeout bruto -0.76% neto -1.26%
- 2026-10-02 10:20 [ruptura_volumen_regimen] CIERRE LINK timeout bruto -0.76% neto -1.26%
- 2026-10-02 10:20 [ruptura_volumen_evento] CIERRE LINK timeout bruto -0.76% neto -1.26%
- 2026-10-02 10:20 [estocastico_rebote] CIERRE ZEC take-profit bruto +1.80% neto +1.30%
- 2026-10-02 10:20 [ruptura_volumen] CIERRE TAO timeout bruto -0.22% neto -0.72%
- 2026-10-02 10:20 [ruptura_volumen_regimen] CIERRE TAO timeout bruto -0.22% neto -0.72%
- 2026-10-02 10:20 [ruptura_volumen_evento] CIERRE TAO timeout bruto -0.22% neto -0.72%
- 2026-10-02 10:20 [macd_momentum] CIERRE ARB momentum perdido bruto -0.65% neto -1.15%
- 2026-10-02 10:20 [macd_momentum_regimen] CIERRE ARB momentum perdido bruto -0.65% neto -1.15%
- 2026-10-02 10:20 [macd_momentum_evento] CIERRE ARB momentum perdido bruto -0.65% neto -1.15%
- 2026-10-02 10:20 [ruptura_volumen] CIERRE NIGHT stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 10:20 [macd_momentum] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 10:20 [macd_sin_salida] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 10:20 [macd_momentum_regimen] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 10:20 [ruptura_volumen_regimen] CIERRE NIGHT stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 10:20 [macd_momentum_evento] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 10:20 [ruptura_volumen_evento] CIERRE NIGHT stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 10:20 [ruptura_volumen] CIERRE RENDER timeout bruto -0.51% neto -1.01%
- 2026-10-02 10:20 [ruptura_volumen_regimen] CIERRE RENDER timeout bruto -0.51% neto -1.01%
- 2026-10-02 10:20 [ruptura_volumen_evento] CIERRE RENDER timeout bruto -0.51% neto -1.01%
- 2026-10-02 10:20 [ruptura_volumen] CIERRE FIL timeout bruto -0.97% neto -1.47%
- 2026-10-02 10:20 [ruptura_volumen_regimen] CIERRE FIL timeout bruto -0.97% neto -1.47%
- 2026-10-02 10:20 [ruptura_volumen_evento] CIERRE FIL timeout bruto -0.97% neto -1.47%
- 2026-10-02 10:15 [macd_momentum] ENTRADA DASH @ 53.4 (21.26 €, apertura)
- 2026-10-02 10:15 [macd_momentum_regimen] ENTRADA DASH @ 53.4 (21.83 €, apertura)
- 2026-10-02 10:15 [macd_momentum_evento] ENTRADA DASH @ 53.4 (21.38 €, apertura)
- 2026-10-02 10:20 [ruptura_volumen] CIERRE TRUMP timeout bruto +0.96% neto +0.46%
- 2026-10-02 10:20 [ruptura_volumen_regimen] CIERRE TRUMP timeout bruto +0.96% neto +0.46%
- 2026-10-02 10:20 [ruptura_volumen_evento] CIERRE TRUMP timeout bruto +0.96% neto +0.46%
- 2026-10-02 10:15 [macd_momentum] ENTRADA BNB @ 691.02 (21.26 €, apertura)
- 2026-10-02 10:15 [macd_momentum_regimen] ENTRADA BNB @ 691.02 (21.83 €, apertura)
- 2026-10-02 10:15 [macd_momentum_evento] ENTRADA BNB @ 691.02 (21.38 €, apertura)
- 2026-10-02 10:20 [c_banda_atr] CIERRE KAS timeout bruto +0.71% neto +0.21%
- 2026-10-02 10:20 [c_banda_atr_regimen] CIERRE KAS timeout bruto +0.71% neto +0.21%
- 2026-10-02 10:20 [c_banda_atr_evento] CIERRE KAS timeout bruto +0.71% neto +0.21%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
