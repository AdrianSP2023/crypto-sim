# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 05:51 UTC · vueltas 359 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.51 € (-3.65%) | 323 | 13 | 39% | +0.108% | -0.473% | -0.592% | -34.84 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 865.37 € (-6.37%) | 377 | 30 | 27% | -0.112% | -0.682% | -0.792% | -57.73 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.26 € (-3.68%) | 214 | 14 | 19% | -0.078% | -0.702% | -0.788% | -34.12 € |
| macd_momentum | 856.71 € (-7.31%) | 618 | 6 | 22% | +0.047% | -0.495% | -0.596% | -68.22 € |
| estocastico_rebote | 878.15 € (-4.99%) | 376 | 8 | 36% | +0.024% | -0.546% | -0.654% | -46.48 € |
| ruptura_estricta | 884.92 € (-4.25%) | 204 | 30 | 32% | -0.209% | -0.839% | -0.953% | -39.00 € |
| macd_sin_salida | 880.99 € (-4.68%) | 412 | 20 | 40% | +0.105% | -0.459% | -0.569% | -43.08 € |
| c_banda_atr_tope | 912.98 € (-1.22%) | 71 | 5 | 34% | +0.148% | -0.724% | -0.833% | -11.81 € |
| ruptura_volumen_tope | 902.71 € (-2.33%) | 120 | 5 | 26% | -0.063% | -0.783% | -0.897% | -21.49 € |
| c_banda_atr_regimen | 903.16 € (-2.28%) | 176 | 12 | 39% | +0.108% | -0.540% | -0.667% | -21.87 € |
| macd_momentum_regimen | 879.65 € (-4.82%) | 381 | 6 | 22% | +0.042% | -0.526% | -0.629% | -45.29 € |
| ruptura_volumen_regimen | 870.07 € (-5.86%) | 300 | 30 | 24% | -0.198% | -0.785% | -0.900% | -53.02 € |
| c_banda_atr_evento | 896.43 € (-3.01%) | 290 | 13 | 40% | +0.155% | -0.436% | -0.551% | -28.92 € |
| macd_momentum_evento | 861.45 € (-6.79%) | 571 | 6 | 21% | +0.049% | -0.498% | -0.596% | -63.48 € |
| ruptura_volumen_evento | 877.68 € (-5.04%) | 327 | 30 | 28% | -0.034% | -0.615% | -0.718% | -45.39 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-02 05:40 | ruptura_volumen_regimen | SUI | stop-loss | -1.20% | -1.70% | -0.37 |

## Eventos de la última vuelta

- 2026-10-02 05:50 [ruptura_estricta] CIERRE HBAR timeout bruto +0.10% neto -0.40%
- 2026-10-02 05:45 [estocastico_rebote] ENTRADA FET @ 0.2094 (21.94 €, apertura)
- 2026-10-02 05:45 [pullback_tendencia] ENTRADA MINA @ 0.1403 (22.25 €, apertura)
- 2026-10-02 05:45 [macd_momentum] ENTRADA MINA @ 0.1403 (21.40 €, apertura)
- 2026-10-02 05:45 [macd_sin_salida] ENTRADA MINA @ 0.1403 (22.03 €, apertura)
- 2026-10-02 05:45 [macd_momentum_regimen] ENTRADA MINA @ 0.1403 (21.97 €, apertura)
- 2026-10-02 05:45 [macd_momentum_evento] ENTRADA MINA @ 0.1403 (21.52 €, apertura)
- 2026-10-02 05:45 [pullback_tendencia] ENTRADA TRUMP @ 1.865 (22.25 €, apertura)
- 2026-10-02 05:50 [c_banda_atr_regimen] CIERRE TON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:45 [ruptura_volumen] ENTRADA XMR @ 487.46 (21.66 €, apertura)
- 2026-10-02 05:45 [ruptura_volumen_tope] ENTRADA XMR @ 487.46 (22.57 €, apertura)
- 2026-10-02 05:45 [ruptura_volumen_regimen] ENTRADA XMR @ 487.46 (21.78 €, apertura)
- 2026-10-02 05:45 [ruptura_volumen_evento] ENTRADA XMR @ 487.46 (21.97 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
