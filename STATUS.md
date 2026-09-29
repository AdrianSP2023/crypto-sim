# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 19:17 UTC · vueltas 115 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.82 € (-1.45%) | 57 | 6 | 35% | -0.135% | -1.093% | -1.231% | -14.38 € |
| reversion_bb | 918.82 € (-0.59%) | 15 | 3 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 909.99 € (-1.54%) | 76 | 18 | 28% | -0.023% | -0.867% | -1.007% | -15.14 € |
| rebote_extremo | 922.80 € (-0.16%) | 6 | 1 | 50% | +0.064% | -1.036% | -1.189% | -1.44 € |
| pullback_tendencia | 908.05 € (-1.75%) | 72 | 1 | 25% | -0.132% | -0.994% | -1.111% | -16.44 € |
| macd_momentum | 898.14 € (-2.82%) | 154 | 1 | 20% | -0.076% | -0.746% | -0.865% | -26.27 € |
| estocastico_rebote | 894.68 € (-3.20%) | 144 | 8 | 31% | -0.244% | -0.925% | -1.045% | -30.47 € |
| ruptura_estricta | 911.38 € (-1.39%) | 43 | 2 | 30% | -0.151% | -1.251% | -1.382% | -12.40 € |
| macd_sin_salida | 905.03 € (-2.08%) | 99 | 2 | 31% | -0.102% | -0.865% | -0.993% | -19.65 € |
| c_banda_atr_tope | 916.31 € (-0.86%) | 23 | 5 | 26% | -0.546% | -1.646% | -1.804% | -8.72 € |
| ruptura_volumen_tope | 919.54 € (-0.51%) | 23 | 5 | 22% | +0.143% | -0.957% | -1.082% | -5.08 € |
| c_banda_atr_regimen | 909.89 € (-1.55%) | 50 | 1 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.14 € (-1.63%) | 71 | 11 | 27% | -0.060% | -0.928% | -1.070% | -15.14 € |
| c_banda_atr_evento | 916.56 € (-0.83%) | 25 | 6 | 32% | -0.398% | -1.498% | -1.647% | -8.65 € |
| macd_momentum_evento | 912.14 € (-1.31%) | 34 | 1 | 18% | -0.464% | -1.564% | -1.695% | -12.27 € |
| ruptura_volumen_evento | 919.34 € (-0.53%) | 17 | 18 | 24% | -0.377% | -1.477% | -1.671% | -5.79 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 19:15 | ruptura_volumen_evento | USELESS | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 19:15 | ruptura_volumen | USELESS | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 19:10 | ruptura_volumen_evento | TRX | timeout | -0.07% | -1.17% | -0.27 |
| 2026-09-29 19:10 | ruptura_volumen_tope | TRX | timeout | -0.07% | -1.17% | -0.27 |
| 2026-09-29 19:10 | pullback_tendencia | NIGHT | rotura de tendencia | -0.25% | -0.75% | -0.17 |
| 2026-09-29 19:10 | ruptura_volumen | TRX | timeout | -0.07% | -0.57% | -0.13 |
| 2026-09-29 19:05 | ruptura_volumen_evento | PUMP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 19:05 | ruptura_volumen_evento | QNT | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 19:05 | ruptura_volumen_regimen | PUMP | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 19:05 | estocastico_rebote | ICP | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-29 19:05 | ruptura_volumen | PUMP | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 19:05 | ruptura_volumen | QNT | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 18:50 | c_banda_atr_evento | VIRTUAL | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 18:50 | ruptura_volumen_regimen | QNT | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 18:50 | estocastico_rebote | AAVE | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-29 19:10 [ruptura_volumen] ENTRADA XRP @ 1.3255 (22.74 €, apertura)
- 2026-09-29 19:10 [ruptura_volumen_regimen] ENTRADA XRP @ 1.3255 (22.73 €, apertura)
- 2026-09-29 19:10 [ruptura_volumen_evento] ENTRADA XRP @ 1.3255 (22.97 €, apertura)
- 2026-09-29 19:15 [ruptura_volumen] CIERRE USELESS stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 19:15 [ruptura_volumen_evento] CIERRE USELESS stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 19:10 [ruptura_volumen_regimen] ENTRADA RAY @ 1.674 (22.73 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
