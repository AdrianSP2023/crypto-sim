# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 19:42 UTC · vueltas 120 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.54 € (-1.48%) | 57 | 7 | 35% | -0.135% | -1.093% | -1.231% | -14.38 € |
| reversion_bb | 918.87 € (-0.58%) | 15 | 3 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 909.38 € (-1.61%) | 76 | 23 | 28% | -0.023% | -0.867% | -1.007% | -15.14 € |
| rebote_extremo | 922.95 € (-0.14%) | 6 | 1 | 50% | +0.064% | -1.036% | -1.189% | -1.44 € |
| pullback_tendencia | 907.98 € (-1.76%) | 72 | 1 | 25% | -0.132% | -0.994% | -1.111% | -16.44 € |
| macd_momentum | 898.02 € (-2.84%) | 155 | 0 | 21% | -0.071% | -0.740% | -0.858% | -26.22 € |
| estocastico_rebote | 895.27 € (-3.13%) | 144 | 8 | 31% | -0.244% | -0.925% | -1.045% | -30.47 € |
| ruptura_estricta | 911.53 € (-1.37%) | 44 | 1 | 30% | -0.193% | -1.280% | -1.414% | -12.97 € |
| macd_sin_salida | 904.75 € (-2.11%) | 100 | 1 | 32% | -0.095% | -0.856% | -0.984% | -19.64 € |
| c_banda_atr_tope | 915.86 € (-0.91%) | 23 | 5 | 26% | -0.546% | -1.646% | -1.804% | -8.72 € |
| ruptura_volumen_tope | 919.26 € (-0.54%) | 23 | 5 | 22% | +0.143% | -0.957% | -1.082% | -5.08 € |
| c_banda_atr_regimen | 909.67 € (-1.58%) | 50 | 2 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 908.79 € (-1.67%) | 71 | 13 | 27% | -0.060% | -0.928% | -1.070% | -15.14 € |
| c_banda_atr_evento | 916.27 € (-0.86%) | 25 | 7 | 32% | -0.398% | -1.498% | -1.647% | -8.65 € |
| macd_momentum_evento | 911.88 € (-1.34%) | 35 | 0 | 17% | -0.431% | -1.531% | -1.660% | -12.36 € |
| ruptura_volumen_evento | 918.73 € (-0.60%) | 17 | 23 | 24% | -0.377% | -1.477% | -1.671% | -5.79 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 19:40 | ruptura_estricta | USELESS | stop-loss | -2.00% | -2.50% | -0.57 |
| 2026-09-29 19:35 | macd_momentum_evento | ASTER | momentum perdido | +0.69% | -0.41% | -0.09 |
| 2026-09-29 19:35 | macd_momentum | ASTER | momentum perdido | +0.69% | +0.19% | +0.04 |
| 2026-09-29 19:25 | macd_sin_salida | INJ | timeout | +0.56% | +0.06% | +0.01 |
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

## Eventos de la última vuelta

- 2026-09-29 19:35 [ruptura_volumen] ENTRADA DOT @ 1.0536 (22.73 €, apertura)
- 2026-09-29 19:35 [ruptura_volumen_regimen] ENTRADA DOT @ 1.0536 (22.73 €, apertura)
- 2026-09-29 19:35 [ruptura_volumen_evento] ENTRADA DOT @ 1.0536 (22.96 €, apertura)
- 2026-09-29 19:35 [ruptura_volumen_regimen] ENTRADA ICP @ 3.021 (22.73 €, apertura)
- 2026-09-29 19:40 [ruptura_estricta] CIERRE USELESS stop-loss bruto -2.00% neto -2.50%
- 2026-09-29 19:35 [c_banda_atr] ENTRADA XPL @ 0.0873 (22.75 €, apertura)
- 2026-09-29 19:35 [c_banda_atr_regimen] ENTRADA XPL @ 0.0873 (22.75 €, apertura)
- 2026-09-29 19:35 [c_banda_atr_evento] ENTRADA XPL @ 0.0873 (22.89 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
