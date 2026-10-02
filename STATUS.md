# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 14:41 UTC · vueltas 425 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 880.00 € (-4.79%) | 391 | 15 | 39% | +0.088% | -0.479% | -0.599% | -42.50 € |
| reversion_bb | 919.71 € (-0.49%) | 74 | 3 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 851.49 € (-7.87%) | 492 | 6 | 26% | -0.106% | -0.660% | -0.770% | -72.26 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 879.29 € (-4.86%) | 302 | 1 | 19% | -0.070% | -0.658% | -0.745% | -44.87 € |
| macd_momentum | 838.23 € (-9.31%) | 803 | 2 | 23% | +0.049% | -0.483% | -0.583% | -85.66 € |
| estocastico_rebote | 870.48 € (-5.82%) | 482 | 34 | 37% | +0.091% | -0.463% | -0.569% | -50.43 € |
| ruptura_estricta | 876.15 € (-5.20%) | 266 | 11 | 31% | -0.166% | -0.765% | -0.883% | -46.18 € |
| macd_sin_salida | 866.89 € (-6.20%) | 523 | 16 | 39% | +0.087% | -0.463% | -0.571% | -54.72 € |
| c_banda_atr_tope | 911.44 € (-1.39%) | 87 | 5 | 37% | +0.200% | -0.604% | -0.722% | -12.08 € |
| ruptura_volumen_tope | 898.30 € (-2.81%) | 148 | 1 | 23% | -0.090% | -0.769% | -0.884% | -25.95 € |
| c_banda_atr_regimen | 892.56 € (-3.43%) | 243 | 15 | 39% | +0.069% | -0.538% | -0.665% | -29.93 € |
| macd_momentum_regimen | 860.67 € (-6.88%) | 566 | 2 | 23% | +0.047% | -0.499% | -0.599% | -63.18 € |
| ruptura_volumen_regimen | 856.11 € (-7.37%) | 415 | 6 | 24% | -0.167% | -0.730% | -0.844% | -67.65 € |
| c_banda_atr_evento | 892.82 € (-3.40%) | 342 | 5 | 41% | +0.180% | -0.397% | -0.512% | -31.03 € |
| macd_momentum_evento | 851.42 € (-7.88%) | 700 | 1 | 23% | +0.070% | -0.468% | -0.564% | -72.75 € |
| ruptura_volumen_evento | 867.45 € (-6.14%) | 415 | 1 | 27% | -0.046% | -0.610% | -0.713% | -56.78 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 14:40 | ruptura_volumen_regimen | PUMP | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 14:40 | pullback_tendencia | PUMP | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 14:40 | ruptura_volumen | PUMP | stop-loss | -1.20% | -1.70% | -0.36 |
| 2026-10-02 14:35 | ruptura_volumen_regimen | DASH | timeout | -1.14% | -1.64% | -0.35 |
| 2026-10-02 14:35 | ruptura_volumen_regimen | OP | timeout | -0.51% | -1.01% | -0.22 |
| 2026-10-02 14:35 | ruptura_volumen_regimen | ARB | stop-loss | -1.20% | -1.70% | -0.36 |
| 2026-10-02 14:35 | ruptura_volumen_regimen | SUI | timeout | -1.15% | -1.65% | -0.35 |
| 2026-10-02 14:35 | c_banda_atr_regimen | UNI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 14:35 | c_banda_atr_regimen | HYPE | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 14:35 | c_banda_atr_regimen | SOL | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 14:35 | c_banda_atr_regimen | XRP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 14:35 | c_banda_atr_tope | XRP | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-02 14:35 | macd_sin_salida | BCH | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 14:35 | macd_sin_salida | DOGE | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 14:35 | macd_sin_salida | HYPE | stop-loss | -1.50% | -2.00% | -0.44 |

## Eventos de la última vuelta

- 2026-10-02 14:40 [ruptura_volumen] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 14:40 [pullback_tendencia] CIERRE PUMP stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:40 [ruptura_volumen_regimen] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
