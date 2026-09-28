# Simulación P1 (sin dinero real)

Config `P1-v9` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-28 22:01 UTC · vueltas 160 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 870.21 € (-5.85%) | 100 | 8 | 16% | -0.880% | -1.980% | -2.103% | -52.81 € |
| reversion_bb | 922.08 € (-0.23%) | 17 | 10 | 65% | +0.520% | -0.580% | -0.794% | -1.91 € |
| ruptura_volumen | 883.44 € (-4.41%) | 85 | 0 | 13% | -0.499% | -1.599% | -1.720% | -40.80 € |
| rebote_extremo | 922.89 € (-0.15%) | 7 | 3 | 71% | +0.910% | -0.190% | -0.602% | -1.53 € |
| pullback_tendencia | 906.36 € (-1.93%) | 50 | 0 | 20% | -0.328% | -1.428% | -1.530% | -17.88 € |
| macd_momentum | 891.33 € (-3.56%) | 92 | 1 | 11% | -0.410% | -1.510% | -1.622% | -32.84 € |
| estocastico_rebote | 898.84 € (-2.75%) | 65 | 12 | 28% | -0.438% | -1.538% | -1.632% | -24.07 € |
| c_banda_atr_filtro | 896.23 € (-3.03%) | 50 | 3 | 6% | -1.288% | -2.388% | -2.511% | -27.47 € |
| ruptura_volumen_filtro | 908.82 € (-1.67%) | 37 | 0 | 8% | -0.713% | -1.813% | -1.935% | -15.42 € |
| macd_momentum_filtro | 910.17 € (-1.52%) | 42 | 0 | 12% | -0.356% | -1.456% | -1.560% | -14.07 € |
| pullback_tendencia_filtro | 917.41 € (-0.74%) | 19 | 0 | 16% | -0.459% | -1.559% | -1.628% | -6.83 € |
| estocastico_rebote_filtro | 919.25 € (-0.54%) | 14 | 1 | 21% | -0.436% | -1.536% | -1.642% | -4.96 € |
| ruptura_estricta | 920.61 € (-0.39%) | 6 | 1 | 17% | -1.214% | -2.314% | -2.454% | -3.21 € |
| macd_sin_salida | 915.70 € (-0.92%) | 13 | 7 | 8% | -1.249% | -2.349% | -2.463% | -7.05 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-28 22:00 | c_banda_atr_filtro | AAVE | stop-loss | -1.50% | -2.60% | -0.58 |
| 2026-09-28 22:00 | reversion_bb | PUMP | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-28 22:00 | c_banda_atr | AAVE | stop-loss | -1.50% | -2.60% | -0.57 |
| 2026-09-28 21:55 | macd_sin_salida | TAO | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-28 21:55 | ruptura_estricta | ATOM | stop-loss | -2.06% | -3.16% | -0.73 |
| 2026-09-28 21:55 | c_banda_atr_filtro | PEPE | stop-loss | -1.70% | -2.80% | -0.63 |
| 2026-09-28 21:55 | ruptura_volumen | LINK | stop-loss | -1.20% | -2.30% | -0.51 |
| 2026-09-28 21:55 | reversion_bb | FET | stop-loss | -1.59% | -2.69% | -0.62 |
| 2026-09-28 21:55 | c_banda_atr | RAY | stop-loss | -1.50% | -2.60% | -0.57 |
| 2026-09-28 21:55 | c_banda_atr | SEI | stop-loss | -1.63% | -2.73% | -0.60 |
| 2026-09-28 21:55 | c_banda_atr | XPL | stop-loss | -1.73% | -2.83% | -0.62 |
| 2026-09-28 21:55 | c_banda_atr | PEPE | stop-loss | -1.70% | -2.80% | -0.61 |
| 2026-09-28 21:50 | estocastico_rebote_filtro | ETH | timeout | -0.53% | -1.62% | -0.38 |
| 2026-09-28 21:50 | estocastico_rebote_filtro | BTC | timeout | -0.58% | -1.68% | -0.39 |
| 2026-09-28 21:50 | c_banda_atr_filtro | OP | stop-loss | -1.85% | -2.95% | -0.66 |

## Eventos de la última vuelta

- 2026-09-28 22:00 [estocastico_rebote] ENTRADA LINK @ 13.3202 (22.50 €)
- 2026-09-28 22:00 [reversion_bb] CIERRE PUMP stop-loss bruto -1.50% neto -2.60%
- 2026-09-28 22:00 [c_banda_atr] CIERRE AAVE stop-loss bruto -1.50% neto -2.60%
- 2026-09-28 22:00 [reversion_bb] ENTRADA AAVE @ 128.31 (23.06 €)
- 2026-09-28 22:00 [c_banda_atr_filtro] CIERRE AAVE stop-loss bruto -1.50% neto -2.60%
- 2026-09-28 22:00 [estocastico_rebote] ENTRADA ALGO @ 0.11959 (22.50 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
