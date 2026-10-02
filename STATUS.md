# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 00:11 UTC · vueltas 337 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.10 € (-4.34%) | 271 | 20 | 34% | -0.055% | -0.651% | -0.773% | -40.07 € |
| reversion_bb | 917.66 € (-0.71%) | 52 | 17 | 50% | +0.317% | -0.685% | -0.782% | -8.21 € |
| ruptura_volumen | 871.66 € (-5.69%) | 297 | 9 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.21 € (-3.90%) | 189 | 4 | 15% | -0.199% | -0.839% | -0.928% | -35.99 € |
| macd_momentum | 863.36 € (-6.59%) | 490 | 14 | 20% | -0.011% | -0.564% | -0.667% | -61.90 € |
| estocastico_rebote | 872.18 € (-5.63%) | 328 | 14 | 30% | -0.129% | -0.708% | -0.818% | -52.39 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 1 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 871.32 € (-5.73%) | 347 | 14 | 34% | -0.103% | -0.678% | -0.790% | -53.17 € |
| c_banda_atr_tope | 911.17 € (-1.41%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.69 € (-2.01%) | 101 | 5 | 27% | -0.042% | -0.803% | -0.919% | -18.58 € |
| c_banda_atr_regimen | 895.77 € (-3.08%) | 138 | 0 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 885.23 € (-4.22%) | 276 | 0 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 874.82 € (-5.35%) | 230 | 0 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 889.98 € (-3.71%) | 238 | 20 | 34% | -0.020% | -0.631% | -0.747% | -34.18 € |
| macd_momentum_evento | 868.14 € (-6.07%) | 443 | 14 | 19% | -0.015% | -0.575% | -0.674% | -57.13 € |
| ruptura_volumen_evento | 884.06 € (-4.35%) | 247 | 9 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 00:10 | c_banda_atr_evento | DASH | timeout | -0.87% | -1.37% | -0.31 |
| 2026-10-02 00:10 | pullback_tendencia | AAVE | rotura de tendencia | +0.18% | -0.32% | -0.07 |
| 2026-10-02 00:10 | c_banda_atr | DASH | timeout | -0.87% | -1.37% | -0.30 |
| 2026-10-02 00:05 | macd_momentum_evento | PUMP | momentum perdido | -0.10% | -0.60% | -0.13 |
| 2026-10-02 00:05 | c_banda_atr_evento | APT | timeout | -0.86% | -1.36% | -0.30 |
| 2026-10-02 00:05 | c_banda_atr_evento | FIL | timeout | -0.22% | -0.72% | -0.16 |
| 2026-10-02 00:05 | c_banda_atr_regimen | APT | timeout | -0.86% | -1.36% | -0.30 |
| 2026-10-02 00:05 | c_banda_atr_regimen | FIL | timeout | -0.22% | -0.72% | -0.16 |
| 2026-10-02 00:05 | macd_momentum | PUMP | momentum perdido | -0.10% | -0.60% | -0.13 |
| 2026-10-02 00:05 | pullback_tendencia | BCH | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 00:05 | c_banda_atr | APT | timeout | -0.86% | -1.36% | -0.30 |
| 2026-10-02 00:05 | c_banda_atr | FIL | timeout | -0.22% | -0.72% | -0.16 |
| 2026-10-02 00:00 | c_banda_atr_evento | XMR | timeout | -0.25% | -0.75% | -0.17 |
| 2026-10-02 00:00 | c_banda_atr_regimen | XMR | timeout | -0.25% | -0.75% | -0.17 |
| 2026-10-02 00:00 | estocastico_rebote | SKY | timeout | +0.23% | -0.27% | -0.06 |

## Eventos de la última vuelta

- 2026-10-02 00:05 [pullback_tendencia] ENTRADA SOL @ 105.2 (22.21 €, apertura)
- 2026-10-02 00:10 [pullback_tendencia] CIERRE AAVE rotura de tendencia bruto +0.18% neto -0.32%
- 2026-10-02 00:05 [macd_momentum] ENTRADA LTC @ 60.69 (21.56 €, apertura)
- 2026-10-02 00:05 [macd_sin_salida] ENTRADA LTC @ 60.69 (21.78 €, apertura)
- 2026-10-02 00:05 [macd_momentum_evento] ENTRADA LTC @ 60.69 (21.68 €, apertura)
- 2026-10-02 00:05 [ruptura_volumen] ENTRADA ICP @ 2.93 (21.79 €, apertura)
- 2026-10-02 00:05 [macd_sin_salida] ENTRADA ICP @ 2.93 (21.78 €, apertura)
- 2026-10-02 00:05 [ruptura_volumen_evento] ENTRADA ICP @ 2.93 (22.10 €, apertura)
- 2026-10-02 00:05 [reversion_bb] ENTRADA BCH @ 271.65 (22.90 €, apertura)
- 2026-10-02 00:10 [c_banda_atr] CIERRE DASH timeout bruto -0.87% neto -1.37%
- 2026-10-02 00:10 [c_banda_atr_evento] CIERRE DASH timeout bruto -0.87% neto -1.37%
- 2026-10-02 00:05 [ruptura_volumen] ENTRADA TRUMP @ 1.834 (21.79 €, apertura)
- 2026-10-02 00:05 [ruptura_volumen_evento] ENTRADA TRUMP @ 1.834 (22.10 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
