# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 15:16 UTC · vueltas 432 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 875.74 € (-5.25%) | 403 | 6 | 37% | +0.041% | -0.524% | -0.645% | -47.80 € |
| reversion_bb | 919.05 € (-0.56%) | 75 | 2 | 61% | +0.566% | -0.282% | -0.386% | -4.89 € |
| ruptura_volumen | 850.18 € (-8.01%) | 496 | 2 | 26% | -0.117% | -0.669% | -0.780% | -73.85 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 879.31 € (-4.86%) | 303 | 2 | 19% | -0.075% | -0.662% | -0.749% | -45.31 € |
| macd_momentum | 836.82 € (-9.46%) | 808 | 1 | 23% | +0.042% | -0.491% | -0.591% | -87.41 € |
| estocastico_rebote | 862.72 € (-6.66%) | 503 | 26 | 35% | +0.027% | -0.525% | -0.632% | -59.42 € |
| ruptura_estricta | 874.40 € (-5.39%) | 269 | 8 | 31% | -0.187% | -0.785% | -0.902% | -47.83 € |
| macd_sin_salida | 862.78 € (-6.65%) | 537 | 6 | 38% | +0.043% | -0.505% | -0.615% | -61.09 € |
| c_banda_atr_tope | 910.45 € (-1.49%) | 90 | 3 | 36% | +0.139% | -0.655% | -0.773% | -13.53 € |
| ruptura_volumen_tope | 898.08 € (-2.83%) | 148 | 1 | 23% | -0.090% | -0.769% | -0.884% | -25.95 € |
| c_banda_atr_regimen | 888.41 € (-3.88%) | 255 | 4 | 37% | -0.004% | -0.607% | -0.733% | -35.31 € |
| macd_momentum_regimen | 859.34 € (-7.02%) | 570 | 1 | 23% | +0.036% | -0.509% | -0.611% | -64.87 € |
| ruptura_volumen_regimen | 854.79 € (-7.51%) | 419 | 2 | 23% | -0.178% | -0.741% | -0.855% | -69.24 € |
| c_banda_atr_evento | 891.01 € (-3.60%) | 346 | 4 | 40% | +0.161% | -0.416% | -0.532% | -32.80 € |
| macd_momentum_evento | 850.06 € (-8.03%) | 704 | 1 | 23% | +0.063% | -0.474% | -0.572% | -74.17 € |
| ruptura_volumen_evento | 867.24 € (-6.17%) | 415 | 1 | 27% | -0.046% | -0.610% | -0.713% | -56.78 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 15:15 | macd_sin_salida | DASH | timeout | -1.26% | -1.76% | -0.39 |
| 2026-10-02 15:10 | c_banda_atr_evento | USELESS | stop-loss | -2.40% | -2.90% | -0.65 |
| 2026-10-02 15:10 | c_banda_atr_evento | POL | stop-loss | -1.57% | -2.07% | -0.46 |
| 2026-10-02 15:10 | c_banda_atr_regimen | USELESS | stop-loss | -2.40% | -2.90% | -0.65 |
| 2026-10-02 15:10 | c_banda_atr_regimen | POL | stop-loss | -1.57% | -2.07% | -0.46 |
| 2026-10-02 15:10 | c_banda_atr_regimen | AAVE | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 15:10 | c_banda_atr_tope | POL | stop-loss | -1.57% | -2.07% | -0.47 |
| 2026-10-02 15:10 | macd_sin_salida | USELESS | stop-loss | -2.40% | -2.90% | -0.63 |
| 2026-10-02 15:10 | macd_sin_salida | AAVE | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 15:10 | ruptura_estricta | APT | stop-loss | -2.01% | -2.51% | -0.55 |
| 2026-10-02 15:10 | ruptura_estricta | UNI | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-02 15:10 | estocastico_rebote | AAVE | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 15:10 | reversion_bb | INJ | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-02 15:10 | c_banda_atr | USELESS | stop-loss | -2.40% | -2.90% | -0.64 |
| 2026-10-02 15:10 | c_banda_atr | POL | stop-loss | -1.57% | -2.07% | -0.46 |

## Eventos de la última vuelta

- 2026-10-02 15:10 [pullback_tendencia] ENTRADA QNT @ 220.19 (21.97 €, apertura)
- 2026-10-02 15:10 [pullback_tendencia] ENTRADA ZRO @ 1.742 (21.97 €, apertura)
- 2026-10-02 15:10 [estocastico_rebote] ENTRADA FIL @ 0.917 (21.62 €, apertura)
- 2026-10-02 15:15 [macd_sin_salida] CIERRE DASH timeout bruto -1.26% neto -1.76%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
