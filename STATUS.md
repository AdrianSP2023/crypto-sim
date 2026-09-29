# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 02:01 UTC · vueltas 180 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 857.61 € (-7.21%) | 135 | 4 | 17% | -0.828% | -1.928% | -2.050% | -66.39 € |
| reversion_bb | 920.14 € (-0.44%) | 36 | 5 | 64% | +0.540% | -0.560% | -0.733% | -4.29 € |
| ruptura_volumen | 871.02 € (-5.76%) | 115 | 0 | 12% | -0.571% | -1.671% | -1.789% | -53.22 € |
| rebote_extremo | 921.03 € (-0.35%) | 13 | 14 | 38% | +0.047% | -1.053% | -1.392% | -4.38 € |
| pullback_tendencia | 902.71 € (-2.33%) | 60 | 0 | 17% | -0.359% | -1.459% | -1.550% | -21.53 € |
| macd_momentum | 885.91 € (-4.15%) | 121 | 1 | 15% | -0.247% | -1.347% | -1.457% | -38.21 € |
| estocastico_rebote | 890.51 € (-3.65%) | 92 | 12 | 25% | -0.460% | -1.560% | -1.658% | -33.86 € |
| c_banda_atr_filtro | 889.24 € (-3.79%) | 63 | 1 | 5% | -1.325% | -2.425% | -2.543% | -34.95 € |
| ruptura_volumen_filtro | 894.71 € (-3.20%) | 66 | 0 | 6% | -0.858% | -1.958% | -2.075% | -29.53 € |
| macd_momentum_filtro | 905.52 € (-2.03%) | 54 | 0 | 9% | -0.411% | -1.511% | -1.617% | -18.72 € |
| pullback_tendencia_filtro | 914.78 € (-1.02%) | 27 | 0 | 11% | -0.422% | -1.522% | -1.579% | -9.46 € |
| estocastico_rebote_filtro | 915.40 € (-0.96%) | 21 | 0 | 14% | -0.727% | -1.827% | -1.934% | -8.84 € |
| ruptura_estricta | 913.20 € (-1.19%) | 17 | 2 | 6% | -1.645% | -2.745% | -2.897% | -10.75 € |
| macd_sin_salida | 906.45 € (-1.93%) | 42 | 2 | 19% | -0.716% | -1.816% | -1.930% | -17.54 € |
| c_banda_atr_tope | 924.16 € (-0.01%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen_tope | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 02:00 | ruptura_volumen_filtro | XDC | stop-loss | -1.47% | -2.57% | -0.58 |
| 2026-09-29 02:00 | ruptura_volumen | XDC | stop-loss | -1.47% | -2.57% | -0.57 |
| 2026-09-29 01:55 | ruptura_estricta | ICP | timeout | +0.74% | -0.36% | -0.08 |
| 2026-09-29 01:50 | ruptura_estricta | CC | stop-loss | -2.00% | -3.10% | -0.71 |
| 2026-09-29 01:50 | ruptura_volumen_filtro | CC | timeout | -0.13% | -1.23% | -0.28 |
| 2026-09-29 01:50 | ruptura_volumen | CC | timeout | -0.13% | -1.23% | -0.27 |
| 2026-09-29 01:45 | ruptura_estricta | FIL | stop-loss | -2.05% | -3.15% | -0.72 |
| 2026-09-29 01:45 | estocastico_rebote | FIL | stop-loss | -1.52% | -2.62% | -0.58 |
| 2026-09-29 01:45 | reversion_bb | HBAR | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-09-29 01:45 | c_banda_atr | POL | stop-loss | -1.51% | -2.61% | -0.57 |
| 2026-09-29 01:40 | macd_sin_salida | AAVE | timeout | -0.19% | -1.29% | -0.30 |
| 2026-09-29 01:40 | ruptura_volumen_filtro | INJ | stop-loss | -1.20% | -2.30% | -0.52 |
| 2026-09-29 01:40 | rebote_extremo | USELESS | stop-loss | -2.00% | -3.10% | -0.71 |
| 2026-09-29 01:40 | ruptura_volumen | INJ | stop-loss | -1.20% | -2.30% | -0.51 |
| 2026-09-29 01:40 | reversion_bb | TON | stop-loss | -1.50% | -2.60% | -0.60 |

## Eventos de la última vuelta

- 2026-09-29 02:00 [reversion_bb] ENTRADA XDC @ 0.02984 (23.00 €)
- 2026-09-29 02:00 [ruptura_volumen] CIERRE XDC stop-loss bruto -1.47% neto -2.57%
- 2026-09-29 02:00 [ruptura_volumen_filtro] CIERRE XDC stop-loss bruto -1.47% neto -2.57%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
