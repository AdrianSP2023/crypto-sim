# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 05:16 UTC · vueltas 219 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 854.26 € (-7.57%) | 147 | 14 | 18% | -0.778% | -1.878% | -2.004% | -69.78 € |
| reversion_bb | 919.07 € (-0.56%) | 41 | 1 | 61% | +0.486% | -0.614% | -0.785% | -5.44 € |
| ruptura_volumen | 870.35 € (-5.83%) | 119 | 18 | 13% | -0.530% | -1.630% | -1.748% | -53.62 € |
| rebote_extremo | 917.94 € (-0.68%) | 27 | 0 | 41% | +0.285% | -0.815% | -1.073% | -6.30 € |
| pullback_tendencia | 903.09 € (-2.29%) | 64 | 1 | 20% | -0.266% | -1.366% | -1.459% | -21.51 € |
| macd_momentum | 883.37 € (-4.42%) | 131 | 6 | 17% | -0.233% | -1.333% | -1.446% | -40.80 € |
| estocastico_rebote | 886.33 € (-4.10%) | 106 | 2 | 25% | -0.438% | -1.538% | -1.635% | -38.21 € |
| c_banda_atr_filtro | 887.63 € (-3.96%) | 66 | 10 | 5% | -1.317% | -2.417% | -2.532% | -36.46 € |
| ruptura_volumen_filtro | 894.07 € (-3.26%) | 69 | 14 | 7% | -0.820% | -1.920% | -2.036% | -30.26 € |
| macd_momentum_filtro | 903.93 € (-2.20%) | 57 | 4 | 9% | -0.448% | -1.548% | -1.655% | -20.23 € |
| pullback_tendencia_filtro | 914.54 € (-1.05%) | 28 | 1 | 11% | -0.461% | -1.561% | -1.621% | -10.06 € |
| estocastico_rebote_filtro | 915.40 € (-0.96%) | 21 | 0 | 14% | -0.727% | -1.827% | -1.934% | -8.84 € |
| ruptura_estricta | 912.80 € (-1.24%) | 20 | 4 | 10% | -1.388% | -2.488% | -2.633% | -11.46 € |
| macd_sin_salida | 904.08 € (-2.18%) | 52 | 6 | 23% | -0.578% | -1.678% | -1.796% | -20.03 € |
| c_banda_atr_tope | 921.21 € (-0.33%) | 10 | 4 | 40% | -0.077% | -1.177% | -1.370% | -2.72 € |
| ruptura_volumen_tope | 924.26 € (+0.00%) | 3 | 5 | 67% | +1.267% | +0.167% | +0.047% | +0.11 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 05:15 | ruptura_volumen_tope | ALGO | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 05:15 | macd_sin_salida | CC | take-profit | +2.27% | +1.17% | +0.26 |
| 2026-09-29 05:15 | macd_sin_salida | CRV | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 05:15 | pullback_tendencia_filtro | CRV | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 05:15 | macd_momentum_filtro | CRV | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 05:15 | macd_momentum_filtro | ENA | momentum perdido | -0.23% | -1.33% | -0.30 |
| 2026-09-29 05:15 | macd_momentum | CRV | stop-loss | -1.50% | -2.60% | -0.57 |
| 2026-09-29 05:15 | macd_momentum | ENA | momentum perdido | -0.23% | -1.33% | -0.29 |
| 2026-09-29 05:15 | pullback_tendencia | CRV | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 05:10 | c_banda_atr_tope | ZRO | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 05:10 | c_banda_atr_filtro | ZRO | stop-loss | -1.50% | -2.60% | -0.58 |
| 2026-09-29 05:10 | c_banda_atr | ZRO | stop-loss | -1.50% | -2.60% | -0.56 |
| 2026-09-29 05:05 | c_banda_atr_tope | RAY | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 05:05 | macd_momentum | CC | momentum perdido | +1.19% | +0.09% | +0.02 |
| 2026-09-29 05:05 | c_banda_atr | RAY | take-profit | +2.00% | +0.90% | +0.19 |

## Eventos de la última vuelta

- 2026-09-29 05:15 [macd_momentum_filtro] ENTRADA ETH @ 2348.12 (22.62 €)
- 2026-09-29 05:15 [macd_momentum] CIERRE ENA momentum perdido bruto -0.23% neto -1.33%
- 2026-09-29 05:15 [macd_momentum_filtro] CIERRE ENA momentum perdido bruto -0.23% neto -1.33%
- 2026-09-29 05:15 [ruptura_volumen_tope] CIERRE ALGO stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 05:15 [ruptura_volumen] ENTRADA ATOM @ 1.5261 (21.77 €)
- 2026-09-29 05:15 [ruptura_volumen_filtro] ENTRADA ATOM @ 1.5261 (22.35 €)
- 2026-09-29 05:15 [ruptura_volumen_tope] ENTRADA ATOM @ 1.5261 (23.11 €)
- 2026-09-29 05:15 [pullback_tendencia] CIERRE CRV stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 05:15 [macd_momentum] CIERRE CRV stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 05:15 [macd_momentum_filtro] CIERRE CRV stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 05:15 [pullback_tendencia_filtro] CIERRE CRV stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 05:15 [macd_sin_salida] CIERRE CRV stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 05:15 [ruptura_volumen] ENTRADA KAS @ 0.04044 (21.77 €)
- 2026-09-29 05:15 [ruptura_volumen_filtro] ENTRADA KAS @ 0.04044 (22.35 €)
- 2026-09-29 05:15 [ruptura_estricta] ENTRADA KAS @ 0.04044 (22.82 €)
- 2026-09-29 05:15 [macd_momentum] ENTRADA CC @ 0.1187 (22.09 €)
- 2026-09-29 05:15 [macd_momentum_filtro] ENTRADA CC @ 0.1187 (22.60 €)
- 2026-09-29 05:15 [macd_sin_salida] CIERRE CC take-profit bruto +2.26% neto +1.16%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
