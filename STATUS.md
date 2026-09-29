# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 05:31 UTC · vueltas 222 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 856.12 € (-7.37%) | 148 | 17 | 19% | -0.759% | -1.859% | -1.986% | -69.59 € |
| reversion_bb | 918.89 € (-0.58%) | 42 | 0 | 62% | +0.511% | -0.589% | -0.762% | -5.35 € |
| ruptura_volumen | 870.87 € (-5.77%) | 124 | 18 | 15% | -0.472% | -1.572% | -1.691% | -53.82 € |
| rebote_extremo | 917.94 € (-0.68%) | 27 | 0 | 41% | +0.285% | -0.815% | -1.073% | -6.30 € |
| pullback_tendencia | 902.96 € (-2.30%) | 65 | 0 | 22% | -0.230% | -1.330% | -1.423% | -21.28 € |
| macd_momentum | 883.97 € (-4.36%) | 131 | 21 | 17% | -0.233% | -1.333% | -1.446% | -40.80 € |
| estocastico_rebote | 886.31 € (-4.10%) | 106 | 2 | 25% | -0.438% | -1.538% | -1.635% | -38.21 € |
| c_banda_atr_filtro | 888.79 € (-3.84%) | 67 | 15 | 6% | -1.267% | -2.367% | -2.485% | -36.26 € |
| ruptura_volumen_filtro | 894.78 € (-3.19%) | 72 | 16 | 10% | -0.717% | -1.817% | -1.937% | -29.90 € |
| macd_momentum_filtro | 904.54 € (-2.13%) | 57 | 19 | 9% | -0.448% | -1.548% | -1.655% | -20.23 € |
| pullback_tendencia_filtro | 914.41 € (-1.06%) | 29 | 0 | 14% | -0.372% | -1.472% | -1.535% | -9.83 € |
| estocastico_rebote_filtro | 915.40 € (-0.96%) | 21 | 0 | 14% | -0.727% | -1.827% | -1.934% | -8.84 € |
| ruptura_estricta | 912.53 € (-1.27%) | 21 | 6 | 10% | -1.417% | -2.517% | -2.661% | -12.17 € |
| macd_sin_salida | 904.80 € (-2.10%) | 52 | 20 | 23% | -0.578% | -1.678% | -1.796% | -20.03 € |
| c_banda_atr_tope | 922.01 € (-0.24%) | 10 | 5 | 40% | -0.077% | -1.177% | -1.370% | -2.72 € |
| ruptura_volumen_tope | 924.20 € (-0.00%) | 6 | 4 | 50% | +1.179% | +0.079% | -0.041% | +0.11 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 05:30 | ruptura_volumen_tope | W | take-profit | +3.63% | +2.53% | +0.58 |
| 2026-09-29 05:30 | ruptura_volumen_tope | TAO | timeout | +0.13% | -0.97% | -0.22 |
| 2026-09-29 05:30 | ruptura_volumen_filtro | W | take-profit | +3.63% | +2.53% | +0.57 |
| 2026-09-29 05:30 | ruptura_volumen_filtro | PUMP | take-profit | +2.50% | +1.40% | +0.31 |
| 2026-09-29 05:30 | c_banda_atr_filtro | NIGHT | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 05:30 | ruptura_volumen | W | take-profit | +3.63% | +2.53% | +0.55 |
| 2026-09-29 05:30 | ruptura_volumen | TAO | timeout | +0.13% | -0.97% | -0.21 |
| 2026-09-29 05:30 | ruptura_volumen | PUMP | take-profit | +2.50% | +1.40% | +0.30 |
| 2026-09-29 05:30 | c_banda_atr | NIGHT | take-profit | +2.00% | +0.90% | +0.19 |
| 2026-09-29 05:25 | ruptura_volumen_tope | PEPE | timeout | -0.49% | -1.59% | -0.37 |
| 2026-09-29 05:25 | ruptura_volumen | PEPE | timeout | -0.49% | -1.59% | -0.35 |
| 2026-09-29 05:25 | reversion_bb | XDC | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-09-29 05:20 | ruptura_estricta | ALGO | stop-loss | -2.00% | -3.10% | -0.71 |
| 2026-09-29 05:20 | pullback_tendencia_filtro | NIGHT | take-profit | +2.10% | +1.00% | +0.23 |
| 2026-09-29 05:20 | ruptura_volumen_filtro | ALGO | stop-loss | -1.20% | -2.30% | -0.51 |

## Eventos de la última vuelta

- 2026-09-29 05:30 [macd_momentum] ENTRADA LTC @ 59.89 (22.09 €)
- 2026-09-29 05:30 [macd_momentum_filtro] ENTRADA LTC @ 59.89 (22.60 €)
- 2026-09-29 05:30 [macd_sin_salida] ENTRADA LTC @ 59.89 (22.61 €)
- 2026-09-29 05:30 [ruptura_volumen] CIERRE PUMP take-profit bruto +2.50% neto +1.40%
- 2026-09-29 05:30 [ruptura_volumen_filtro] CIERRE PUMP take-profit bruto +2.50% neto +1.40%
- 2026-09-29 05:30 [ruptura_volumen] CIERRE TAO timeout bruto +0.13% neto -0.97%
- 2026-09-29 05:30 [ruptura_volumen_tope] CIERRE TAO timeout bruto +0.13% neto -0.97%
- 2026-09-29 05:30 [macd_momentum] ENTRADA DOT @ 1.0215 (22.09 €)
- 2026-09-29 05:30 [macd_momentum_filtro] ENTRADA DOT @ 1.0215 (22.60 €)
- 2026-09-29 05:30 [macd_sin_salida] ENTRADA DOT @ 1.0215 (22.61 €)
- 2026-09-29 05:30 [ruptura_volumen] CIERRE W take-profit bruto +3.63% neto +2.53%
- 2026-09-29 05:30 [ruptura_volumen_filtro] CIERRE W take-profit bruto +3.63% neto +2.53%
- 2026-09-29 05:30 [ruptura_volumen_tope] CIERRE W take-profit bruto +3.63% neto +2.53%
- 2026-09-29 05:30 [ruptura_volumen] ENTRADA FET @ 0.1982 (21.76 €)
- 2026-09-29 05:30 [macd_momentum] ENTRADA FET @ 0.1982 (22.09 €)
- 2026-09-29 05:30 [ruptura_volumen_filtro] ENTRADA FET @ 0.1982 (22.36 €)
- 2026-09-29 05:30 [macd_momentum_filtro] ENTRADA FET @ 0.1982 (22.60 €)
- 2026-09-29 05:30 [macd_sin_salida] ENTRADA FET @ 0.1982 (22.61 €)
- 2026-09-29 05:30 [ruptura_volumen_tope] ENTRADA FET @ 0.1982 (23.11 €)
- 2026-09-29 05:30 [macd_momentum] ENTRADA SEI @ 0.06558 (22.09 €)
- 2026-09-29 05:30 [macd_momentum_filtro] ENTRADA SEI @ 0.06558 (22.60 €)
- 2026-09-29 05:30 [macd_sin_salida] ENTRADA SEI @ 0.06558 (22.61 €)
- 2026-09-29 05:30 [macd_momentum] ENTRADA SHIB @ 4.927e-06 (22.09 €)
- 2026-09-29 05:30 [macd_momentum_filtro] ENTRADA SHIB @ 4.927e-06 (22.60 €)
- 2026-09-29 05:30 [macd_sin_salida] ENTRADA SHIB @ 4.927e-06 (22.61 €)
- 2026-09-29 05:30 [c_banda_atr] CIERRE NIGHT take-profit bruto +2.00% neto +0.90%
- 2026-09-29 05:30 [c_banda_atr_filtro] CIERRE NIGHT take-profit bruto +2.00% neto +0.90%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
