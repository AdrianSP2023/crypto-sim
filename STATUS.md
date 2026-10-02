# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 15:11 UTC · vueltas 431 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 875.67 € (-5.25%) | 403 | 6 | 37% | +0.041% | -0.524% | -0.645% | -47.80 € |
| reversion_bb | 918.96 € (-0.57%) | 75 | 2 | 61% | +0.566% | -0.282% | -0.386% | -4.89 € |
| ruptura_volumen | 850.18 € (-8.01%) | 496 | 2 | 26% | -0.117% | -0.669% | -0.780% | -73.85 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 878.94 € (-4.90%) | 303 | 0 | 19% | -0.075% | -0.662% | -0.749% | -45.31 € |
| macd_momentum | 836.75 € (-9.47%) | 808 | 1 | 23% | +0.042% | -0.491% | -0.591% | -87.41 € |
| estocastico_rebote | 861.43 € (-6.80%) | 503 | 25 | 35% | +0.027% | -0.525% | -0.632% | -59.42 € |
| ruptura_estricta | 874.14 € (-5.42%) | 269 | 8 | 31% | -0.187% | -0.785% | -0.902% | -47.83 € |
| macd_sin_salida | 862.66 € (-6.66%) | 536 | 7 | 38% | +0.046% | -0.503% | -0.612% | -60.70 € |
| c_banda_atr_tope | 910.44 € (-1.49%) | 90 | 3 | 36% | +0.139% | -0.655% | -0.773% | -13.53 € |
| ruptura_volumen_tope | 898.08 € (-2.83%) | 148 | 1 | 23% | -0.090% | -0.769% | -0.884% | -25.95 € |
| c_banda_atr_regimen | 888.41 € (-3.88%) | 255 | 4 | 37% | -0.004% | -0.607% | -0.733% | -35.31 € |
| macd_momentum_regimen | 859.26 € (-7.03%) | 570 | 1 | 23% | +0.036% | -0.509% | -0.611% | -64.87 € |
| ruptura_volumen_regimen | 854.79 € (-7.51%) | 419 | 2 | 23% | -0.178% | -0.741% | -0.855% | -69.24 € |
| c_banda_atr_evento | 890.94 € (-3.60%) | 346 | 4 | 40% | +0.161% | -0.416% | -0.532% | -32.80 € |
| macd_momentum_evento | 849.99 € (-8.03%) | 704 | 1 | 23% | +0.063% | -0.474% | -0.572% | -74.17 € |
| ruptura_volumen_evento | 867.24 € (-6.17%) | 415 | 1 | 27% | -0.046% | -0.610% | -0.713% | -56.78 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-02 15:10 | c_banda_atr | AAVE | stop-loss | -1.50% | -2.00% | -0.44 |

## Eventos de la última vuelta

- 2026-10-02 15:10 [c_banda_atr] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 15:10 [estocastico_rebote] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 15:10 [macd_sin_salida] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 15:10 [c_banda_atr_regimen] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 15:10 [ruptura_estricta] CIERRE UNI stop-loss bruto -2.00% neto -2.50%
- 2026-10-02 15:05 [c_banda_atr] ENTRADA TRX @ 0.297316 (21.94 €, apertura)
- 2026-10-02 15:05 [c_banda_atr_tope] ENTRADA TRX @ 0.297316 (22.78 €, apertura)
- 2026-10-02 15:05 [c_banda_atr_evento] ENTRADA TRX @ 0.297316 (22.31 €, apertura)
- 2026-10-02 15:10 [c_banda_atr] CIERRE POL stop-loss bruto -1.57% neto -2.07%
- 2026-10-02 15:10 [c_banda_atr_tope] CIERRE POL stop-loss bruto -1.57% neto -2.07%
- 2026-10-02 15:10 [c_banda_atr_regimen] CIERRE POL stop-loss bruto -1.57% neto -2.07%
- 2026-10-02 15:10 [c_banda_atr_evento] CIERRE POL stop-loss bruto -1.57% neto -2.07%
- 2026-10-02 15:10 [c_banda_atr] CIERRE USELESS stop-loss bruto -2.40% neto -2.90%
- 2026-10-02 15:10 [macd_sin_salida] CIERRE USELESS stop-loss bruto -2.40% neto -2.90%
- 2026-10-02 15:10 [c_banda_atr_regimen] CIERRE USELESS stop-loss bruto -2.40% neto -2.90%
- 2026-10-02 15:10 [c_banda_atr_evento] CIERRE USELESS stop-loss bruto -2.40% neto -2.90%
- 2026-10-02 15:10 [reversion_bb] CIERRE INJ stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 15:10 [ruptura_estricta] CIERRE APT stop-loss bruto -2.01% neto -2.51%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
