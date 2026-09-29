# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 05:21 UTC · vueltas 220 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 855.04 € (-7.49%) | 147 | 17 | 18% | -0.778% | -1.878% | -2.004% | -69.78 € |
| reversion_bb | 919.08 € (-0.56%) | 41 | 1 | 61% | +0.486% | -0.614% | -0.785% | -5.44 € |
| ruptura_volumen | 870.78 € (-5.78%) | 120 | 19 | 13% | -0.536% | -1.636% | -1.754% | -54.12 € |
| rebote_extremo | 917.94 € (-0.68%) | 27 | 0 | 41% | +0.285% | -0.815% | -1.073% | -6.30 € |
| pullback_tendencia | 902.96 € (-2.30%) | 65 | 0 | 22% | -0.230% | -1.330% | -1.423% | -21.28 € |
| macd_momentum | 883.43 € (-4.42%) | 131 | 10 | 17% | -0.233% | -1.333% | -1.446% | -40.80 € |
| estocastico_rebote | 886.47 € (-4.09%) | 106 | 2 | 25% | -0.438% | -1.538% | -1.635% | -38.21 € |
| c_banda_atr_filtro | 888.11 € (-3.91%) | 66 | 14 | 5% | -1.317% | -2.417% | -2.532% | -36.46 € |
| ruptura_volumen_filtro | 894.43 € (-3.23%) | 70 | 15 | 7% | -0.825% | -1.925% | -2.041% | -30.77 € |
| macd_momentum_filtro | 903.99 € (-2.19%) | 57 | 8 | 9% | -0.448% | -1.548% | -1.655% | -20.23 € |
| pullback_tendencia_filtro | 914.41 € (-1.06%) | 29 | 0 | 14% | -0.372% | -1.472% | -1.535% | -9.83 € |
| estocastico_rebote_filtro | 915.40 € (-0.96%) | 21 | 0 | 14% | -0.727% | -1.827% | -1.934% | -8.84 € |
| ruptura_estricta | 912.26 € (-1.30%) | 21 | 5 | 10% | -1.417% | -2.517% | -2.661% | -12.17 € |
| macd_sin_salida | 904.26 € (-2.16%) | 52 | 9 | 23% | -0.578% | -1.678% | -1.796% | -20.03 € |
| c_banda_atr_tope | 921.44 € (-0.30%) | 10 | 5 | 40% | -0.077% | -1.177% | -1.370% | -2.72 € |
| ruptura_volumen_tope | 924.27 € (+0.00%) | 3 | 5 | 67% | +1.267% | +0.167% | +0.047% | +0.11 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 05:20 | ruptura_estricta | ALGO | stop-loss | -2.00% | -3.10% | -0.71 |
| 2026-09-29 05:20 | pullback_tendencia_filtro | NIGHT | take-profit | +2.10% | +1.00% | +0.23 |
| 2026-09-29 05:20 | ruptura_volumen_filtro | ALGO | stop-loss | -1.20% | -2.30% | -0.51 |
| 2026-09-29 05:20 | pullback_tendencia | NIGHT | take-profit | +2.10% | +1.00% | +0.23 |
| 2026-09-29 05:20 | ruptura_volumen | ALGO | stop-loss | -1.20% | -2.30% | -0.50 |
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

## Eventos de la última vuelta

- 2026-09-29 05:20 [macd_momentum] ENTRADA SOL @ 103.85 (22.09 €)
- 2026-09-29 05:20 [macd_momentum_filtro] ENTRADA SOL @ 103.85 (22.60 €)
- 2026-09-29 05:20 [macd_sin_salida] ENTRADA SOL @ 103.85 (22.61 €)
- 2026-09-29 05:20 [ruptura_volumen] ENTRADA ETH @ 2352.05 (21.77 €)
- 2026-09-29 05:20 [ruptura_volumen_filtro] ENTRADA ETH @ 2352.05 (22.35 €)
- 2026-09-29 05:20 [c_banda_atr] ENTRADA ZEC @ 1213.81 (21.36 €)
- 2026-09-29 05:20 [c_banda_atr_filtro] ENTRADA ZEC @ 1213.81 (22.19 €)
- 2026-09-29 05:20 [c_banda_atr_tope] ENTRADA ZEC @ 1213.81 (23.04 €)
- 2026-09-29 05:20 [ruptura_estricta] ENTRADA PUMP @ 0.004368 (22.82 €)
- 2026-09-29 05:20 [c_banda_atr] ENTRADA ARB @ 0.1744 (21.36 €)
- 2026-09-29 05:20 [macd_momentum] ENTRADA ARB @ 0.1744 (22.09 €)
- 2026-09-29 05:20 [c_banda_atr_filtro] ENTRADA ARB @ 0.1744 (22.19 €)
- 2026-09-29 05:20 [macd_momentum_filtro] ENTRADA ARB @ 0.1744 (22.60 €)
- 2026-09-29 05:20 [macd_sin_salida] ENTRADA ARB @ 0.1744 (22.61 €)
- 2026-09-29 05:20 [ruptura_volumen] ENTRADA AVAX @ 9.29 (21.77 €)
- 2026-09-29 05:20 [ruptura_volumen_filtro] ENTRADA AVAX @ 9.29 (22.35 €)
- 2026-09-29 05:20 [c_banda_atr] ENTRADA ENA @ 0.2216 (21.36 €)
- 2026-09-29 05:20 [macd_momentum] ENTRADA ENA @ 0.2216 (22.09 €)
- 2026-09-29 05:20 [c_banda_atr_filtro] ENTRADA ENA @ 0.2216 (22.19 €)
- 2026-09-29 05:20 [macd_momentum_filtro] ENTRADA ENA @ 0.2216 (22.60 €)
- 2026-09-29 05:20 [ruptura_volumen] CIERRE ALGO stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 05:20 [ruptura_volumen_filtro] CIERRE ALGO stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 05:20 [ruptura_estricta] CIERRE ALGO stop-loss bruto -2.00% neto -3.10%
- 2026-09-29 05:20 [macd_momentum] ENTRADA INJ @ 6.467 (22.09 €)
- 2026-09-29 05:20 [macd_momentum_filtro] ENTRADA INJ @ 6.467 (22.60 €)
- 2026-09-29 05:20 [macd_sin_salida] ENTRADA INJ @ 6.467 (22.61 €)
- 2026-09-29 05:20 [pullback_tendencia] CIERRE NIGHT take-profit bruto +2.10% neto +1.00%
- 2026-09-29 05:20 [pullback_tendencia_filtro] CIERRE NIGHT take-profit bruto +2.10% neto +1.00%
- 2026-09-29 05:20 [ruptura_estricta] ENTRADA NIGHT @ 0.02535 (22.80 €)
- 2026-09-29 05:20 [c_banda_atr_filtro] ENTRADA EIGEN @ 0.2204 (22.19 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
