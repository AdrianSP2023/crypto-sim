# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 05:36 UTC · vueltas 223 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 853.96 € (-7.60%) | 149 | 17 | 19% | -0.765% | -1.865% | -1.991% | -70.16 € |
| reversion_bb | 918.89 € (-0.58%) | 42 | 0 | 62% | +0.511% | -0.589% | -0.762% | -5.35 € |
| ruptura_volumen | 868.37 € (-6.04%) | 126 | 17 | 14% | -0.490% | -1.590% | -1.710% | -54.99 € |
| rebote_extremo | 917.94 € (-0.68%) | 27 | 0 | 41% | +0.285% | -0.815% | -1.073% | -6.30 € |
| pullback_tendencia | 902.96 € (-2.30%) | 65 | 0 | 22% | -0.230% | -1.330% | -1.423% | -21.28 € |
| macd_momentum | 881.79 € (-4.59%) | 131 | 21 | 17% | -0.233% | -1.333% | -1.446% | -40.80 € |
| estocastico_rebote | 885.89 € (-4.15%) | 106 | 2 | 25% | -0.438% | -1.538% | -1.635% | -38.21 € |
| c_banda_atr_filtro | 886.95 € (-4.03%) | 68 | 14 | 6% | -1.272% | -2.372% | -2.490% | -36.85 € |
| ruptura_volumen_filtro | 892.59 € (-3.42%) | 74 | 14 | 9% | -0.740% | -1.840% | -1.962% | -31.09 € |
| macd_momentum_filtro | 902.32 € (-2.37%) | 57 | 19 | 9% | -0.448% | -1.548% | -1.655% | -20.23 € |
| pullback_tendencia_filtro | 914.41 € (-1.06%) | 29 | 0 | 14% | -0.372% | -1.472% | -1.535% | -9.83 € |
| estocastico_rebote_filtro | 915.40 € (-0.96%) | 21 | 0 | 14% | -0.727% | -1.827% | -1.934% | -8.84 € |
| ruptura_estricta | 910.92 € (-1.44%) | 22 | 5 | 9% | -1.443% | -2.543% | -2.686% | -12.88 € |
| macd_sin_salida | 902.57 € (-2.34%) | 52 | 20 | 23% | -0.578% | -1.678% | -1.796% | -20.03 € |
| c_banda_atr_tope | 921.08 € (-0.34%) | 11 | 5 | 36% | -0.212% | -1.312% | -1.500% | -3.33 € |
| ruptura_volumen_tope | 923.86 € (-0.04%) | 6 | 5 | 50% | +1.179% | +0.079% | -0.041% | +0.11 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 05:35 | c_banda_atr_tope | SEI | stop-loss | -1.56% | -2.67% | -0.61 |
| 2026-09-29 05:35 | ruptura_estricta | PUMP | stop-loss | -2.00% | -3.10% | -0.71 |
| 2026-09-29 05:35 | ruptura_volumen_filtro | TON | stop-loss | -1.81% | -2.91% | -0.65 |
| 2026-09-29 05:35 | ruptura_volumen_filtro | POL | stop-loss | -1.34% | -2.44% | -0.55 |
| 2026-09-29 05:35 | c_banda_atr_filtro | SEI | stop-loss | -1.56% | -2.67% | -0.59 |
| 2026-09-29 05:35 | ruptura_volumen | TON | stop-loss | -1.81% | -2.91% | -0.63 |
| 2026-09-29 05:35 | ruptura_volumen | POL | stop-loss | -1.34% | -2.44% | -0.53 |
| 2026-09-29 05:35 | c_banda_atr | SEI | stop-loss | -1.56% | -2.67% | -0.57 |
| 2026-09-29 05:30 | ruptura_volumen_tope | W | take-profit | +3.63% | +2.53% | +0.58 |
| 2026-09-29 05:30 | ruptura_volumen_tope | TAO | timeout | +0.13% | -0.97% | -0.22 |
| 2026-09-29 05:30 | ruptura_volumen_filtro | W | take-profit | +3.63% | +2.53% | +0.57 |
| 2026-09-29 05:30 | ruptura_volumen_filtro | PUMP | take-profit | +2.50% | +1.40% | +0.31 |
| 2026-09-29 05:30 | c_banda_atr_filtro | NIGHT | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 05:30 | ruptura_volumen | W | take-profit | +3.63% | +2.53% | +0.55 |
| 2026-09-29 05:30 | ruptura_volumen | TAO | timeout | +0.13% | -0.97% | -0.21 |

## Eventos de la última vuelta

- 2026-09-29 05:35 [ruptura_estricta] CIERRE PUMP stop-loss bruto -2.00% neto -3.10%
- 2026-09-29 05:35 [ruptura_volumen] ENTRADA XDC @ 0.03043 (21.76 €)
- 2026-09-29 05:35 [ruptura_volumen_tope] ENTRADA XDC @ 0.03043 (23.11 €)
- 2026-09-29 05:35 [ruptura_volumen] CIERRE POL stop-loss bruto -1.34% neto -2.44%
- 2026-09-29 05:35 [ruptura_volumen_filtro] CIERRE POL stop-loss bruto -1.34% neto -2.44%
- 2026-09-29 05:35 [c_banda_atr] CIERRE SEI stop-loss bruto -1.56% neto -2.66%
- 2026-09-29 05:35 [c_banda_atr_filtro] CIERRE SEI stop-loss bruto -1.56% neto -2.66%
- 2026-09-29 05:35 [c_banda_atr_tope] CIERRE SEI stop-loss bruto -1.56% neto -2.66%
- 2026-09-29 05:35 [ruptura_volumen] CIERRE TON stop-loss bruto -1.81% neto -2.91%
- 2026-09-29 05:35 [ruptura_volumen_filtro] CIERRE TON stop-loss bruto -1.81% neto -2.91%
- 2026-09-29 05:35 [c_banda_atr] ENTRADA SKY @ 0.06836 (21.35 €)
- 2026-09-29 05:35 [c_banda_atr_tope] ENTRADA SKY @ 0.06836 (23.02 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
