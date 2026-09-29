# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 05:11 UTC · vueltas 218 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 853.96 € (-7.60%) | 147 | 14 | 18% | -0.778% | -1.878% | -2.004% | -69.78 € |
| reversion_bb | 918.96 € (-0.57%) | 41 | 1 | 61% | +0.486% | -0.614% | -0.785% | -5.44 € |
| ruptura_volumen | 870.46 € (-5.82%) | 119 | 16 | 13% | -0.530% | -1.630% | -1.748% | -53.62 € |
| rebote_extremo | 917.94 € (-0.68%) | 27 | 0 | 41% | +0.285% | -0.815% | -1.073% | -6.30 € |
| pullback_tendencia | 903.44 € (-2.25%) | 63 | 2 | 21% | -0.247% | -1.347% | -1.438% | -20.92 € |
| macd_momentum | 883.75 € (-4.38%) | 129 | 7 | 17% | -0.224% | -1.324% | -1.436% | -39.93 € |
| estocastico_rebote | 886.13 € (-4.12%) | 106 | 2 | 25% | -0.438% | -1.538% | -1.635% | -38.21 € |
| c_banda_atr_filtro | 887.54 € (-3.97%) | 66 | 10 | 5% | -1.317% | -2.417% | -2.532% | -36.46 € |
| ruptura_volumen_filtro | 894.19 € (-3.25%) | 69 | 12 | 7% | -0.820% | -1.920% | -2.036% | -30.26 € |
| macd_momentum_filtro | 904.35 € (-2.15%) | 55 | 4 | 9% | -0.433% | -1.533% | -1.639% | -19.34 € |
| pullback_tendencia_filtro | 914.90 € (-1.01%) | 27 | 2 | 11% | -0.422% | -1.522% | -1.579% | -9.46 € |
| estocastico_rebote_filtro | 915.40 € (-0.96%) | 21 | 0 | 14% | -0.727% | -1.827% | -1.934% | -8.84 € |
| ruptura_estricta | 912.85 € (-1.23%) | 20 | 3 | 10% | -1.388% | -2.488% | -2.633% | -11.46 € |
| macd_sin_salida | 904.23 € (-2.17%) | 50 | 8 | 22% | -0.616% | -1.716% | -1.832% | -19.71 € |
| c_banda_atr_tope | 921.13 € (-0.34%) | 10 | 4 | 40% | -0.077% | -1.177% | -1.370% | -2.72 € |
| ruptura_volumen_tope | 924.76 € (+0.06%) | 2 | 5 | 100% | +2.500% | +1.400% | +1.262% | +0.65 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 05:10 | c_banda_atr_tope | ZRO | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 05:10 | c_banda_atr_filtro | ZRO | stop-loss | -1.50% | -2.60% | -0.58 |
| 2026-09-29 05:10 | c_banda_atr | ZRO | stop-loss | -1.50% | -2.60% | -0.56 |
| 2026-09-29 05:05 | c_banda_atr_tope | RAY | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 05:05 | macd_momentum | CC | momentum perdido | +1.19% | +0.09% | +0.02 |
| 2026-09-29 05:05 | c_banda_atr | RAY | take-profit | +2.00% | +0.90% | +0.19 |
| 2026-09-29 04:55 | ruptura_volumen_filtro | ARB | stop-loss | -1.20% | -2.30% | -0.52 |
| 2026-09-29 04:55 | ruptura_volumen | ARB | stop-loss | -1.20% | -2.30% | -0.50 |
| 2026-09-29 04:50 | c_banda_atr_tope | JUP | stop-loss | -1.64% | -2.74% | -0.63 |
| 2026-09-29 04:50 | macd_sin_salida | JUP | stop-loss | -1.64% | -2.74% | -0.62 |
| 2026-09-29 04:50 | macd_momentum_filtro | JUP | stop-loss | -1.64% | -2.74% | -0.62 |
| 2026-09-29 04:50 | c_banda_atr_filtro | JUP | stop-loss | -1.64% | -2.74% | -0.61 |
| 2026-09-29 04:50 | macd_momentum | JUP | stop-loss | -1.64% | -2.74% | -0.61 |
| 2026-09-29 04:50 | c_banda_atr | JUP | stop-loss | -1.64% | -2.74% | -0.59 |
| 2026-09-29 04:45 | estocastico_rebote | AAVE | timeout | +0.89% | -0.21% | -0.05 |

## Eventos de la última vuelta

- 2026-09-29 05:10 [c_banda_atr] CIERRE ZRO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 05:10 [c_banda_atr_filtro] CIERRE ZRO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 05:10 [c_banda_atr_tope] CIERRE ZRO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 05:10 [macd_momentum] ENTRADA RAY @ 1.649 (22.11 €)
- 2026-09-29 05:10 [macd_sin_salida] ENTRADA RAY @ 1.649 (22.61 €)
- 2026-09-29 05:10 [c_banda_atr] ENTRADA TRUMP @ 1.731 (21.36 €)
- 2026-09-29 05:10 [macd_momentum] ENTRADA TRUMP @ 1.731 (22.11 €)
- 2026-09-29 05:10 [macd_sin_salida] ENTRADA TRUMP @ 1.731 (22.61 €)
- 2026-09-29 05:10 [c_banda_atr_tope] ENTRADA TRUMP @ 1.731 (23.04 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
