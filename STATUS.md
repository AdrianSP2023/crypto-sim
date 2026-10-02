# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 14:46 UTC · vueltas 426 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 880.10 € (-4.78%) | 392 | 14 | 39% | +0.087% | -0.480% | -0.600% | -42.67 € |
| reversion_bb | 919.74 € (-0.49%) | 74 | 3 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 851.51 € (-7.87%) | 492 | 6 | 26% | -0.106% | -0.660% | -0.770% | -72.26 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 879.29 € (-4.86%) | 302 | 1 | 19% | -0.070% | -0.658% | -0.745% | -44.87 € |
| macd_momentum | 838.15 € (-9.31%) | 804 | 2 | 23% | +0.048% | -0.485% | -0.584% | -86.01 € |
| estocastico_rebote | 870.96 € (-5.76%) | 482 | 36 | 37% | +0.091% | -0.463% | -0.569% | -50.43 € |
| ruptura_estricta | 876.17 € (-5.20%) | 266 | 11 | 31% | -0.166% | -0.765% | -0.883% | -46.18 € |
| macd_sin_salida | 867.04 € (-6.19%) | 523 | 17 | 39% | +0.087% | -0.463% | -0.571% | -54.72 € |
| c_banda_atr_tope | 911.61 € (-1.37%) | 87 | 5 | 37% | +0.200% | -0.604% | -0.722% | -12.08 € |
| ruptura_volumen_tope | 898.29 € (-2.81%) | 148 | 1 | 23% | -0.090% | -0.769% | -0.884% | -25.95 € |
| c_banda_atr_regimen | 892.67 € (-3.42%) | 244 | 14 | 39% | +0.068% | -0.539% | -0.666% | -30.10 € |
| macd_momentum_regimen | 860.59 € (-6.89%) | 567 | 1 | 23% | +0.045% | -0.501% | -0.602% | -63.55 € |
| ruptura_volumen_regimen | 856.13 € (-7.37%) | 415 | 6 | 24% | -0.167% | -0.730% | -0.844% | -67.65 € |
| c_banda_atr_evento | 892.89 € (-3.39%) | 343 | 4 | 41% | +0.179% | -0.398% | -0.513% | -31.20 € |
| macd_momentum_evento | 851.41 € (-7.88%) | 700 | 2 | 23% | +0.070% | -0.468% | -0.564% | -72.75 € |
| ruptura_volumen_evento | 867.44 € (-6.15%) | 415 | 1 | 27% | -0.046% | -0.610% | -0.713% | -56.78 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 14:45 | c_banda_atr_evento | OP | timeout | -0.25% | -0.75% | -0.17 |
| 2026-10-02 14:45 | macd_momentum_regimen | VVV | momentum perdido | -1.18% | -1.68% | -0.36 |
| 2026-10-02 14:45 | c_banda_atr_regimen | OP | timeout | -0.25% | -0.75% | -0.17 |
| 2026-10-02 14:45 | macd_momentum | VVV | momentum perdido | -1.18% | -1.68% | -0.35 |
| 2026-10-02 14:45 | c_banda_atr | OP | timeout | -0.25% | -0.75% | -0.17 |
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

## Eventos de la última vuelta

- 2026-10-02 14:40 [estocastico_rebote] ENTRADA MON @ 0.03069 (21.85 €, apertura)
- 2026-10-02 14:45 [c_banda_atr] CIERRE OP timeout bruto -0.25% neto -0.75%
- 2026-10-02 14:45 [c_banda_atr_regimen] CIERRE OP timeout bruto -0.25% neto -0.75%
- 2026-10-02 14:45 [c_banda_atr_evento] CIERRE OP timeout bruto -0.25% neto -0.75%
- 2026-10-02 14:45 [macd_momentum] CIERRE VVV momentum perdido bruto -1.18% neto -1.68%
- 2026-10-02 14:45 [macd_momentum_regimen] CIERRE VVV momentum perdido bruto -1.18% neto -1.68%
- 2026-10-02 14:40 [macd_momentum] ENTRADA WLFI @ 0.0503 (20.96 €, apertura)
- 2026-10-02 14:40 [macd_sin_salida] ENTRADA WLFI @ 0.0503 (21.74 €, apertura)
- 2026-10-02 14:40 [macd_momentum_evento] ENTRADA WLFI @ 0.0503 (21.29 €, apertura)
- 2026-10-02 14:40 [estocastico_rebote] ENTRADA KSM @ 4.6 (21.85 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
