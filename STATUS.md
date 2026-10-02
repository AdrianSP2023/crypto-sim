# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 05:56 UTC · vueltas 360 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.28 € (-3.67%) | 323 | 13 | 39% | +0.108% | -0.473% | -0.592% | -34.84 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 865.12 € (-6.40%) | 377 | 30 | 27% | -0.112% | -0.682% | -0.792% | -57.73 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.94 € (-3.71%) | 215 | 14 | 20% | -0.069% | -0.691% | -0.778% | -33.79 € |
| macd_momentum | 856.41 € (-7.34%) | 618 | 6 | 22% | +0.047% | -0.495% | -0.596% | -68.22 € |
| estocastico_rebote | 878.06 € (-5.00%) | 376 | 11 | 36% | +0.024% | -0.546% | -0.654% | -46.48 € |
| ruptura_estricta | 884.83 € (-4.26%) | 204 | 30 | 32% | -0.209% | -0.839% | -0.953% | -39.00 € |
| macd_sin_salida | 880.80 € (-4.70%) | 412 | 20 | 40% | +0.105% | -0.459% | -0.569% | -43.08 € |
| c_banda_atr_tope | 912.79 € (-1.24%) | 71 | 5 | 34% | +0.148% | -0.724% | -0.833% | -11.81 € |
| ruptura_volumen_tope | 902.64 € (-2.34%) | 120 | 5 | 26% | -0.063% | -0.783% | -0.897% | -21.49 € |
| c_banda_atr_regimen | 902.95 € (-2.30%) | 176 | 12 | 39% | +0.108% | -0.540% | -0.667% | -21.87 € |
| macd_momentum_regimen | 879.34 € (-4.86%) | 381 | 6 | 22% | +0.042% | -0.526% | -0.629% | -45.29 € |
| ruptura_volumen_regimen | 869.81 € (-5.89%) | 300 | 30 | 24% | -0.198% | -0.785% | -0.900% | -53.02 € |
| c_banda_atr_evento | 896.20 € (-3.03%) | 290 | 13 | 40% | +0.155% | -0.436% | -0.551% | -28.92 € |
| macd_momentum_evento | 861.15 € (-6.83%) | 571 | 6 | 21% | +0.049% | -0.498% | -0.596% | -63.48 € |
| ruptura_volumen_evento | 877.43 € (-5.07%) | 327 | 30 | 28% | -0.034% | -0.615% | -0.718% | -45.39 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 05:55 | pullback_tendencia | HYPE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 05:50 | c_banda_atr_regimen | TON | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 05:50 | ruptura_estricta | HBAR | timeout | +0.10% | -0.40% | -0.09 |
| 2026-10-02 05:45 | macd_momentum_evento | TRUMP | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 05:45 | macd_momentum_evento | FIL | momentum perdido | +0.11% | -0.39% | -0.08 |
| 2026-10-02 05:45 | c_banda_atr_evento | FET | stop-loss | -1.51% | -2.01% | -0.45 |
| 2026-10-02 05:45 | macd_momentum_regimen | TRUMP | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 05:45 | macd_momentum_regimen | FIL | momentum perdido | +0.11% | -0.39% | -0.09 |
| 2026-10-02 05:45 | ruptura_estricta | INJ | stop-loss | -2.09% | -2.59% | -0.57 |
| 2026-10-02 05:45 | macd_momentum | TRUMP | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 05:45 | macd_momentum | FIL | momentum perdido | +0.11% | -0.39% | -0.08 |
| 2026-10-02 05:45 | c_banda_atr | FET | stop-loss | -1.51% | -2.01% | -0.45 |
| 2026-10-02 05:40 | ruptura_volumen_evento | SUI | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 05:40 | macd_momentum_evento | SEI | momentum perdido | +0.03% | -0.47% | -0.10 |
| 2026-10-02 05:40 | macd_momentum_evento | WLD | momentum perdido | -1.05% | -1.55% | -0.33 |

## Eventos de la última vuelta

- 2026-10-02 05:50 [estocastico_rebote] ENTRADA BTC @ 76474 (21.94 €, apertura)
- 2026-10-02 05:55 [pullback_tendencia] CIERRE HYPE take-profit bruto +2.00% neto +1.50%
- 2026-10-02 05:50 [pullback_tendencia] ENTRADA ONDO @ 0.4489 (22.26 €, apertura)
- 2026-10-02 05:50 [estocastico_rebote] ENTRADA BNB @ 690.63 (21.94 €, apertura)
- 2026-10-02 05:50 [estocastico_rebote] ENTRADA SPX @ 0.3984 (21.94 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
