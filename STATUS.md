# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 01:46 UTC · vueltas 177 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 857.59 € (-7.21%) | 135 | 3 | 17% | -0.828% | -1.928% | -2.050% | -66.39 € |
| reversion_bb | 919.64 € (-0.50%) | 36 | 4 | 64% | +0.540% | -0.560% | -0.733% | -4.29 € |
| ruptura_volumen | 871.90 € (-5.66%) | 113 | 2 | 12% | -0.567% | -1.667% | -1.783% | -52.38 € |
| rebote_extremo | 919.82 € (-0.48%) | 13 | 14 | 38% | +0.047% | -1.053% | -1.392% | -4.38 € |
| pullback_tendencia | 902.71 € (-2.33%) | 60 | 0 | 17% | -0.359% | -1.459% | -1.550% | -21.53 € |
| macd_momentum | 886.03 € (-4.13%) | 121 | 0 | 15% | -0.247% | -1.347% | -1.457% | -38.21 € |
| estocastico_rebote | 889.59 € (-3.75%) | 92 | 12 | 25% | -0.460% | -1.560% | -1.658% | -33.86 € |
| c_banda_atr_filtro | 889.22 € (-3.79%) | 63 | 1 | 5% | -1.325% | -2.425% | -2.543% | -34.95 € |
| ruptura_volumen_filtro | 895.61 € (-3.10%) | 64 | 2 | 6% | -0.859% | -1.959% | -2.075% | -28.67 € |
| macd_momentum_filtro | 905.52 € (-2.03%) | 54 | 0 | 9% | -0.411% | -1.511% | -1.617% | -18.72 € |
| pullback_tendencia_filtro | 914.78 € (-1.02%) | 27 | 0 | 11% | -0.422% | -1.522% | -1.579% | -9.46 € |
| estocastico_rebote_filtro | 915.40 € (-0.96%) | 21 | 0 | 14% | -0.727% | -1.827% | -1.934% | -8.84 € |
| ruptura_estricta | 913.64 € (-1.15%) | 15 | 4 | 7% | -1.780% | -2.880% | -3.033% | -9.95 € |
| macd_sin_salida | 906.54 € (-1.92%) | 42 | 1 | 19% | -0.716% | -1.816% | -1.930% | -17.54 € |
| c_banda_atr_tope | 924.24 € (+0.00%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen_tope | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 01:45 | ruptura_estricta | FIL | stop-loss | -2.05% | -3.15% | -0.72 |
| 2026-09-29 01:45 | estocastico_rebote | FIL | stop-loss | -1.52% | -2.62% | -0.58 |
| 2026-09-29 01:45 | reversion_bb | HBAR | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-09-29 01:45 | c_banda_atr | POL | stop-loss | -1.51% | -2.61% | -0.57 |
| 2026-09-29 01:40 | macd_sin_salida | AAVE | timeout | -0.19% | -1.29% | -0.30 |
| 2026-09-29 01:40 | ruptura_volumen_filtro | INJ | stop-loss | -1.20% | -2.30% | -0.52 |
| 2026-09-29 01:40 | rebote_extremo | USELESS | stop-loss | -2.00% | -3.10% | -0.71 |
| 2026-09-29 01:40 | ruptura_volumen | INJ | stop-loss | -1.20% | -2.30% | -0.51 |
| 2026-09-29 01:40 | reversion_bb | TON | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 01:40 | reversion_bb | ETH | timeout | -0.27% | -1.37% | -0.32 |
| 2026-09-29 01:35 | macd_sin_salida | TRX | timeout | -0.34% | -1.44% | -0.33 |
| 2026-09-29 01:35 | macd_sin_salida | GRT | stop-loss | -2.18% | -3.28% | -0.75 |
| 2026-09-29 01:35 | macd_sin_salida | XRP | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 01:35 | ruptura_estricta | GRT | stop-loss | -2.18% | -3.28% | -0.76 |
| 2026-09-29 01:35 | macd_momentum_filtro | GRT | stop-loss | -2.18% | -3.28% | -0.75 |

## Eventos de la última vuelta

- 2026-09-29 01:45 [c_banda_atr] ENTRADA HBAR @ 0.10639 (21.46 €)
- 2026-09-29 01:45 [reversion_bb] CIERRE HBAR take-profit bruto +1.50% neto +0.40%
- 2026-09-29 01:45 [c_banda_atr_tope] ENTRADA HBAR @ 0.10639 (23.11 €)
- 2026-09-29 01:45 [estocastico_rebote] ENTRADA AAVE @ 129.7 (22.27 €)
- 2026-09-29 01:45 [c_banda_atr] CIERRE POL stop-loss bruto -1.51% neto -2.61%
- 2026-09-29 01:45 [estocastico_rebote] CIERRE FIL stop-loss bruto -1.52% neto -2.62%
- 2026-09-29 01:45 [ruptura_estricta] CIERRE FIL stop-loss bruto -2.05% neto -3.15%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
