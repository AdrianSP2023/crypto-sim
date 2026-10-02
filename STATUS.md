# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 15:26 UTC · vueltas 434 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 875.51 € (-5.27%) | 404 | 6 | 37% | +0.037% | -0.528% | -0.648% | -48.24 € |
| reversion_bb | 919.06 € (-0.56%) | 75 | 2 | 61% | +0.566% | -0.282% | -0.386% | -4.89 € |
| ruptura_volumen | 850.18 € (-8.01%) | 496 | 2 | 26% | -0.117% | -0.669% | -0.780% | -73.85 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 879.55 € (-4.84%) | 303 | 3 | 19% | -0.075% | -0.662% | -0.749% | -45.31 € |
| macd_momentum | 836.85 € (-9.46%) | 808 | 4 | 23% | +0.042% | -0.491% | -0.591% | -87.41 € |
| estocastico_rebote | 862.27 € (-6.70%) | 503 | 32 | 35% | +0.027% | -0.525% | -0.632% | -59.42 € |
| ruptura_estricta | 874.43 € (-5.39%) | 271 | 6 | 31% | -0.198% | -0.796% | -0.912% | -48.82 € |
| macd_sin_salida | 862.93 € (-6.63%) | 537 | 8 | 38% | +0.043% | -0.505% | -0.615% | -61.09 € |
| c_banda_atr_tope | 910.50 € (-1.49%) | 90 | 4 | 36% | +0.139% | -0.655% | -0.773% | -13.53 € |
| ruptura_volumen_tope | 898.08 € (-2.83%) | 148 | 1 | 23% | -0.090% | -0.769% | -0.884% | -25.95 € |
| c_banda_atr_regimen | 888.41 € (-3.88%) | 255 | 4 | 37% | -0.004% | -0.607% | -0.733% | -35.31 € |
| macd_momentum_regimen | 859.45 € (-7.01%) | 570 | 1 | 23% | +0.036% | -0.509% | -0.611% | -64.87 € |
| ruptura_volumen_regimen | 854.79 € (-7.51%) | 419 | 2 | 23% | -0.178% | -0.741% | -0.855% | -69.24 € |
| c_banda_atr_evento | 890.78 € (-3.62%) | 347 | 4 | 40% | +0.156% | -0.420% | -0.536% | -33.25 € |
| macd_momentum_evento | 850.08 € (-8.02%) | 704 | 4 | 23% | +0.063% | -0.474% | -0.572% | -74.17 € |
| ruptura_volumen_evento | 867.24 € (-6.17%) | 415 | 1 | 27% | -0.046% | -0.610% | -0.713% | -56.78 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 15:25 | c_banda_atr_evento | ENA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 15:25 | ruptura_estricta | POL | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-02 15:25 | c_banda_atr | ENA | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 15:20 | ruptura_estricta | BTC | timeout | -1.50% | -2.00% | -0.44 |
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

## Eventos de la última vuelta

- 2026-10-02 15:20 [macd_momentum] ENTRADA LTC @ 62.7 (20.92 €, apertura)
- 2026-10-02 15:20 [macd_momentum_evento] ENTRADA LTC @ 62.7 (21.25 €, apertura)
- 2026-10-02 15:25 [c_banda_atr] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 15:25 [c_banda_atr_evento] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 15:25 [ruptura_estricta] CIERRE POL stop-loss bruto -2.00% neto -2.50%
- 2026-10-02 15:20 [c_banda_atr] ENTRADA ONDO @ 0.4518 (21.90 €, apertura)
- 2026-10-02 15:20 [macd_momentum] ENTRADA ONDO @ 0.4518 (20.92 €, apertura)
- 2026-10-02 15:20 [macd_sin_salida] ENTRADA ONDO @ 0.4518 (21.58 €, apertura)
- 2026-10-02 15:20 [c_banda_atr_tope] ENTRADA ONDO @ 0.4518 (22.77 €, apertura)
- 2026-10-02 15:20 [c_banda_atr_evento] ENTRADA ONDO @ 0.4518 (22.27 €, apertura)
- 2026-10-02 15:20 [macd_momentum_evento] ENTRADA ONDO @ 0.4518 (21.25 €, apertura)
- 2026-10-02 15:20 [pullback_tendencia] ENTRADA MON @ 0.03085 (21.97 €, apertura)
- 2026-10-02 15:20 [estocastico_rebote] ENTRADA MINA @ 0.1419 (21.62 €, apertura)
- 2026-10-02 15:20 [estocastico_rebote] ENTRADA VVV @ 26.194 (21.62 €, apertura)
- 2026-10-02 15:20 [estocastico_rebote] ENTRADA KAS @ 0.03783 (21.62 €, apertura)
- 2026-10-02 15:20 [estocastico_rebote] ENTRADA APT @ 0.7332 (21.62 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
