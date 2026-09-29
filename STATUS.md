# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 20:02 UTC · vueltas 124 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.32 € (-1.61%) | 58 | 6 | 34% | -0.159% | -1.109% | -1.248% | -14.83 € |
| reversion_bb | 918.53 € (-0.62%) | 15 | 3 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 905.30 € (-2.05%) | 81 | 20 | 26% | -0.100% | -0.922% | -1.063% | -17.15 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 907.22 € (-1.84%) | 75 | 1 | 24% | -0.142% | -0.990% | -1.106% | -17.05 € |
| macd_momentum | 898.02 € (-2.84%) | 155 | 1 | 21% | -0.071% | -0.740% | -0.858% | -26.22 € |
| estocastico_rebote | 893.76 € (-3.30%) | 147 | 5 | 31% | -0.231% | -0.909% | -1.027% | -30.55 € |
| ruptura_estricta | 911.17 € (-1.41%) | 44 | 2 | 30% | -0.193% | -1.280% | -1.414% | -12.97 € |
| macd_sin_salida | 904.70 € (-2.11%) | 100 | 2 | 32% | -0.095% | -0.856% | -0.984% | -19.64 € |
| c_banda_atr_tope | 915.35 € (-0.96%) | 23 | 5 | 26% | -0.546% | -1.646% | -1.804% | -8.72 € |
| ruptura_volumen_tope | 917.73 € (-0.70%) | 25 | 4 | 20% | +0.024% | -1.076% | -1.207% | -6.20 € |
| c_banda_atr_regimen | 909.12 € (-1.64%) | 51 | 1 | 31% | -0.251% | -1.263% | -1.400% | -14.85 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 906.63 € (-1.91%) | 73 | 13 | 26% | -0.096% | -0.953% | -1.096% | -15.98 € |
| c_banda_atr_evento | 914.91 € (-1.01%) | 26 | 6 | 31% | -0.440% | -1.540% | -1.691% | -9.24 € |
| macd_momentum_evento | 911.88 € (-1.34%) | 35 | 1 | 17% | -0.431% | -1.531% | -1.660% | -12.36 € |
| ruptura_volumen_evento | 913.91 € (-1.12%) | 22 | 20 | 18% | -0.579% | -1.679% | -1.862% | -8.51 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 20:00 | ruptura_volumen_evento | PENGU | stop-loss | -1.22% | -2.32% | -0.53 |
| 2026-09-29 20:00 | estocastico_rebote | TRUMP | timeout | +0.11% | -0.39% | -0.09 |
| 2026-09-29 20:00 | estocastico_rebote | FIL | timeout | +0.75% | +0.25% | +0.06 |
| 2026-09-29 20:00 | estocastico_rebote | XRP | timeout | +0.31% | -0.19% | -0.04 |
| 2026-09-29 20:00 | pullback_tendencia | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 20:00 | ruptura_volumen | PENGU | stop-loss | -1.22% | -1.72% | -0.39 |
| 2026-09-29 19:55 | ruptura_volumen_evento | RAY | stop-loss | -1.49% | -2.59% | -0.60 |
| 2026-09-29 19:55 | ruptura_volumen_regimen | RAY | stop-loss | -1.49% | -1.99% | -0.45 |
| 2026-09-29 19:55 | ruptura_volumen_tope | RAY | stop-loss | -1.49% | -2.59% | -0.60 |
| 2026-09-29 19:55 | pullback_tendencia | NIGHT | rotura de tendencia | +0.18% | -0.32% | -0.07 |
| 2026-09-29 19:55 | pullback_tendencia | INJ | rotura de tendencia | +0.13% | -0.37% | -0.08 |
| 2026-09-29 19:55 | ruptura_volumen | RAY | stop-loss | -1.49% | -1.99% | -0.45 |
| 2026-09-29 19:50 | ruptura_volumen_evento | ENA | stop-loss | -1.21% | -2.31% | -0.53 |
| 2026-09-29 19:50 | ruptura_volumen_evento | ZEC | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 19:50 | c_banda_atr_evento | XPL | stop-loss | -1.50% | -2.60% | -0.59 |

## Eventos de la última vuelta

- 2026-09-29 20:00 [estocastico_rebote] CIERRE XRP timeout bruto +0.31% neto -0.19%
- 2026-09-29 20:00 [pullback_tendencia] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 20:00 [estocastico_rebote] CIERRE FIL timeout bruto +0.75% neto +0.25%
- 2026-09-29 20:00 [ruptura_volumen] CIERRE PENGU stop-loss bruto -1.22% neto -1.72%
- 2026-09-29 20:00 [ruptura_volumen_evento] CIERRE PENGU stop-loss bruto -1.22% neto -2.32%
- 2026-09-29 20:00 [estocastico_rebote] CIERRE TRUMP timeout bruto +0.11% neto -0.39%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
