# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 15:06 UTC · vueltas 430 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 876.43 € (-5.17%) | 400 | 8 | 38% | +0.055% | -0.511% | -0.631% | -46.26 € |
| reversion_bb | 919.26 € (-0.54%) | 74 | 3 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 850.23 € (-8.01%) | 496 | 2 | 26% | -0.117% | -0.669% | -0.780% | -73.85 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 878.94 € (-4.90%) | 303 | 0 | 19% | -0.075% | -0.662% | -0.749% | -45.31 € |
| macd_momentum | 836.89 € (-9.45%) | 808 | 1 | 23% | +0.042% | -0.491% | -0.591% | -87.41 € |
| estocastico_rebote | 861.93 € (-6.74%) | 502 | 26 | 35% | +0.030% | -0.522% | -0.629% | -58.98 € |
| ruptura_estricta | 874.66 € (-5.36%) | 267 | 10 | 31% | -0.173% | -0.772% | -0.889% | -46.73 € |
| macd_sin_salida | 863.26 € (-6.60%) | 534 | 9 | 38% | +0.053% | -0.496% | -0.604% | -59.64 € |
| c_banda_atr_tope | 910.57 € (-1.48%) | 89 | 3 | 36% | +0.158% | -0.639% | -0.757% | -13.06 € |
| ruptura_volumen_tope | 898.13 € (-2.82%) | 148 | 1 | 23% | -0.090% | -0.769% | -0.884% | -25.95 € |
| c_banda_atr_regimen | 889.18 € (-3.79%) | 252 | 7 | 37% | +0.017% | -0.586% | -0.712% | -33.75 € |
| macd_momentum_regimen | 859.40 € (-7.02%) | 570 | 1 | 23% | +0.036% | -0.509% | -0.611% | -64.87 € |
| ruptura_volumen_regimen | 854.84 € (-7.51%) | 419 | 2 | 23% | -0.178% | -0.741% | -0.855% | -69.24 € |
| c_banda_atr_evento | 891.52 € (-3.54%) | 344 | 5 | 40% | +0.173% | -0.403% | -0.519% | -31.69 € |
| macd_momentum_evento | 850.13 € (-8.02%) | 704 | 1 | 23% | +0.063% | -0.474% | -0.572% | -74.17 € |
| ruptura_volumen_evento | 867.29 € (-6.16%) | 415 | 1 | 27% | -0.046% | -0.610% | -0.713% | -56.78 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 15:05 | c_banda_atr_regimen | VVV | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 15:05 | estocastico_rebote | VVV | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 15:05 | c_banda_atr | VVV | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 15:00 | macd_momentum_evento | USELESS | momentum perdido | -1.22% | -1.72% | -0.37 |
| 2026-10-02 15:00 | macd_momentum_evento | NIGHT | stop-loss | -1.95% | -2.45% | -0.52 |
| 2026-10-02 15:00 | c_banda_atr_evento | KAS | stop-loss | -1.72% | -2.22% | -0.50 |
| 2026-10-02 15:00 | ruptura_volumen_regimen | KSM | stop-loss | -1.51% | -2.02% | -0.43 |
| 2026-10-02 15:00 | ruptura_volumen_regimen | FIL | stop-loss | -1.51% | -2.01% | -0.43 |
| 2026-10-02 15:00 | macd_momentum_regimen | USELESS | momentum perdido | -1.22% | -1.72% | -0.37 |
| 2026-10-02 15:00 | macd_momentum_regimen | NIGHT | stop-loss | -1.95% | -2.45% | -0.53 |
| 2026-10-02 15:00 | c_banda_atr_regimen | KAS | stop-loss | -1.72% | -2.22% | -0.50 |
| 2026-10-02 15:00 | c_banda_atr_regimen | JUP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 15:00 | c_banda_atr_tope | KAS | stop-loss | -1.72% | -2.22% | -0.51 |
| 2026-10-02 15:00 | macd_sin_salida | JUP | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 15:00 | macd_sin_salida | NIGHT | stop-loss | -1.95% | -2.45% | -0.53 |

## Eventos de la última vuelta

- 2026-10-02 15:00 [estocastico_rebote] ENTRADA SUI @ 1.0419 (21.64 €, apertura)
- 2026-10-02 15:00 [estocastico_rebote] ENTRADA ZEC @ 1218.91 (21.64 €, apertura)
- 2026-10-02 15:00 [estocastico_rebote] ENTRADA ICP @ 2.909 (21.64 €, apertura)
- 2026-10-02 15:05 [c_banda_atr] CIERRE VVV stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 15:05 [estocastico_rebote] CIERRE VVV stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 15:05 [c_banda_atr_regimen] CIERRE VVV stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
