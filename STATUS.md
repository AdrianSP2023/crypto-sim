# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 14:51 UTC · vueltas 427 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 880.62 € (-4.72%) | 392 | 15 | 39% | +0.087% | -0.480% | -0.600% | -42.67 € |
| reversion_bb | 919.78 € (-0.48%) | 74 | 3 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 851.54 € (-7.87%) | 492 | 6 | 26% | -0.106% | -0.660% | -0.770% | -72.26 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 878.94 € (-4.90%) | 303 | 0 | 19% | -0.075% | -0.662% | -0.749% | -45.31 € |
| macd_momentum | 837.82 € (-9.35%) | 805 | 1 | 23% | +0.046% | -0.487% | -0.586% | -86.43 € |
| estocastico_rebote | 872.22 € (-5.63%) | 484 | 38 | 37% | +0.089% | -0.465% | -0.571% | -50.82 € |
| ruptura_estricta | 876.36 € (-5.18%) | 266 | 11 | 31% | -0.166% | -0.765% | -0.883% | -46.18 € |
| macd_sin_salida | 867.14 € (-6.18%) | 525 | 15 | 38% | +0.081% | -0.469% | -0.577% | -55.60 € |
| c_banda_atr_tope | 911.79 € (-1.35%) | 87 | 5 | 37% | +0.200% | -0.604% | -0.722% | -12.08 € |
| ruptura_volumen_tope | 898.29 € (-2.81%) | 148 | 1 | 23% | -0.090% | -0.769% | -0.884% | -25.95 € |
| c_banda_atr_regimen | 893.21 € (-3.36%) | 244 | 14 | 39% | +0.068% | -0.539% | -0.666% | -30.10 € |
| macd_momentum_regimen | 860.25 € (-6.92%) | 568 | 0 | 23% | +0.042% | -0.504% | -0.604% | -63.98 € |
| ruptura_volumen_regimen | 856.16 € (-7.37%) | 415 | 6 | 24% | -0.167% | -0.730% | -0.844% | -67.65 € |
| c_banda_atr_evento | 892.92 € (-3.39%) | 343 | 5 | 41% | +0.179% | -0.398% | -0.513% | -31.20 € |
| macd_momentum_evento | 851.07 € (-7.92%) | 701 | 1 | 23% | +0.068% | -0.470% | -0.566% | -73.18 € |
| ruptura_volumen_evento | 867.44 € (-6.15%) | 415 | 1 | 27% | -0.046% | -0.610% | -0.713% | -56.78 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 14:50 | macd_momentum_evento | SKY | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 14:50 | macd_momentum_regimen | SKY | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 14:50 | macd_sin_salida | SKY | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 14:50 | macd_sin_salida | XDC | stop-loss | -1.55% | -2.05% | -0.45 |
| 2026-10-02 14:50 | estocastico_rebote | MINA | timeout | +0.35% | -0.15% | -0.03 |
| 2026-10-02 14:50 | estocastico_rebote | PEPE | timeout | -1.08% | -1.58% | -0.35 |
| 2026-10-02 14:50 | macd_momentum | SKY | stop-loss | -1.50% | -2.00% | -0.42 |
| 2026-10-02 14:50 | pullback_tendencia | SKY | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 14:45 | c_banda_atr_evento | OP | timeout | -0.25% | -0.75% | -0.17 |
| 2026-10-02 14:45 | macd_momentum_regimen | VVV | momentum perdido | -1.18% | -1.68% | -0.36 |
| 2026-10-02 14:45 | c_banda_atr_regimen | OP | timeout | -0.25% | -0.75% | -0.17 |
| 2026-10-02 14:45 | macd_momentum | VVV | momentum perdido | -1.18% | -1.68% | -0.35 |
| 2026-10-02 14:45 | c_banda_atr | OP | timeout | -0.25% | -0.75% | -0.17 |
| 2026-10-02 14:40 | ruptura_volumen_regimen | PUMP | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 14:40 | pullback_tendencia | PUMP | stop-loss | -1.50% | -2.00% | -0.44 |

## Eventos de la última vuelta

- 2026-10-02 14:45 [estocastico_rebote] ENTRADA PUMP @ 0.005364 (21.85 €, apertura)
- 2026-10-02 14:45 [estocastico_rebote] ENTRADA XLM @ 0.19822 (21.85 €, apertura)
- 2026-10-02 14:45 [estocastico_rebote] ENTRADA LTC @ 62.17 (21.85 €, apertura)
- 2026-10-02 14:45 [c_banda_atr] ENTRADA ENA @ 0.2189 (22.04 €, apertura)
- 2026-10-02 14:45 [c_banda_atr_evento] ENTRADA ENA @ 0.2189 (22.33 €, apertura)
- 2026-10-02 14:50 [macd_sin_salida] CIERRE XDC stop-loss bruto -1.55% neto -2.05%
- 2026-10-02 14:50 [estocastico_rebote] CIERRE PEPE timeout bruto -1.09% neto -1.59%
- 2026-10-02 14:50 [estocastico_rebote] CIERRE MINA timeout bruto +0.35% neto -0.15%
- 2026-10-02 14:45 [estocastico_rebote] ENTRADA TRUMP @ 1.92 (21.84 €, apertura)
- 2026-10-02 14:50 [pullback_tendencia] CIERRE SKY stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:50 [macd_momentum] CIERRE SKY stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:50 [macd_sin_salida] CIERRE SKY stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:50 [macd_momentum_regimen] CIERRE SKY stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:50 [macd_momentum_evento] CIERRE SKY stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
