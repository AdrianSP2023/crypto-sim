# Simulación P1 (sin dinero real)

Config `P1-v9` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-28 21:51 UTC · vueltas 158 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 872.27 € (-5.62%) | 95 | 13 | 17% | -0.841% | -1.941% | -2.062% | -49.83 € |
| reversion_bb | 922.94 € (-0.14%) | 15 | 8 | 73% | +0.795% | -0.305% | -0.488% | -0.69 € |
| ruptura_volumen | 883.70 € (-4.39%) | 84 | 1 | 13% | -0.491% | -1.591% | -1.712% | -40.29 € |
| rebote_extremo | 923.10 € (-0.12%) | 7 | 3 | 71% | +0.910% | -0.190% | -0.602% | -1.53 € |
| pullback_tendencia | 906.36 € (-1.93%) | 50 | 0 | 20% | -0.328% | -1.428% | -1.530% | -17.88 € |
| macd_momentum | 891.49 € (-3.54%) | 92 | 1 | 11% | -0.410% | -1.510% | -1.622% | -32.84 € |
| estocastico_rebote | 899.07 € (-2.72%) | 65 | 10 | 28% | -0.438% | -1.538% | -1.632% | -24.07 € |
| c_banda_atr_filtro | 896.91 € (-2.96%) | 48 | 5 | 6% | -1.275% | -2.375% | -2.499% | -26.26 € |
| ruptura_volumen_filtro | 908.82 € (-1.67%) | 37 | 0 | 8% | -0.713% | -1.813% | -1.935% | -15.42 € |
| macd_momentum_filtro | 910.17 € (-1.52%) | 42 | 0 | 12% | -0.356% | -1.456% | -1.560% | -14.07 € |
| pullback_tendencia_filtro | 917.41 € (-0.74%) | 19 | 0 | 16% | -0.459% | -1.559% | -1.628% | -6.83 € |
| estocastico_rebote_filtro | 919.26 € (-0.54%) | 14 | 1 | 21% | -0.436% | -1.536% | -1.642% | -4.96 € |
| ruptura_estricta | 920.97 € (-0.35%) | 5 | 2 | 20% | -1.045% | -2.145% | -2.276% | -2.48 € |
| macd_sin_salida | 916.56 € (-0.83%) | 12 | 8 | 8% | -1.228% | -2.328% | -2.448% | -6.45 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-28 21:50 | estocastico_rebote_filtro | ETH | timeout | -0.53% | -1.62% | -0.38 |
| 2026-09-28 21:50 | estocastico_rebote_filtro | BTC | timeout | -0.58% | -1.68% | -0.39 |
| 2026-09-28 21:50 | c_banda_atr_filtro | OP | stop-loss | -1.85% | -2.95% | -0.66 |
| 2026-09-28 21:50 | estocastico_rebote | MON | stop-loss | -1.55% | -2.65% | -0.60 |
| 2026-09-28 21:50 | estocastico_rebote | ETH | timeout | -0.53% | -1.62% | -0.37 |
| 2026-09-28 21:50 | estocastico_rebote | BTC | timeout | -0.58% | -1.68% | -0.38 |
| 2026-09-28 21:50 | pullback_tendencia | LINK | rotura de tendencia | -0.96% | -2.06% | -0.47 |
| 2026-09-28 21:50 | c_banda_atr | NIGHT | stop-loss | -2.01% | -3.11% | -0.68 |
| 2026-09-28 21:50 | c_banda_atr | OP | stop-loss | -1.60% | -2.71% | -0.59 |
| 2026-09-28 21:45 | macd_sin_salida | INJ | stop-loss | -1.88% | -2.98% | -0.69 |
| 2026-09-28 21:45 | macd_momentum | ETH | momentum perdido | -0.19% | -1.29% | -0.29 |
| 2026-09-28 21:45 | pullback_tendencia | ALGO | rotura de tendencia | -0.79% | -1.89% | -0.43 |
| 2026-09-28 21:45 | ruptura_volumen | TAO | stop-loss | -1.20% | -2.30% | -0.51 |
| 2026-09-28 21:45 | c_banda_atr | INJ | stop-loss | -2.01% | -3.11% | -0.68 |
| 2026-09-28 21:45 | c_banda_atr | FET | stop-loss | -2.06% | -3.16% | -0.69 |

## Eventos de la última vuelta

- 2026-09-28 21:50 [estocastico_rebote] CIERRE BTC timeout bruto -0.58% neto -1.68%
- 2026-09-28 21:50 [estocastico_rebote_filtro] CIERRE BTC timeout bruto -0.58% neto -1.68%
- 2026-09-28 21:50 [estocastico_rebote] CIERRE ETH timeout bruto -0.53% neto -1.63%
- 2026-09-28 21:50 [estocastico_rebote_filtro] CIERRE ETH timeout bruto -0.53% neto -1.63%
- 2026-09-28 21:50 [pullback_tendencia] CIERRE LINK rotura de tendencia bruto -0.96% neto -2.06%
- 2026-09-28 21:50 [estocastico_rebote] CIERRE MON stop-loss bruto -1.55% neto -2.65%
- 2026-09-28 21:50 [reversion_bb] ENTRADA JUP @ 0.28339 (23.09 €)
- 2026-09-28 21:50 [reversion_bb] ENTRADA INJ @ 6.32 (23.09 €)
- 2026-09-28 21:50 [c_banda_atr] CIERRE OP stop-loss bruto -1.60% neto -2.70%
- 2026-09-28 21:50 [c_banda_atr_filtro] CIERRE OP stop-loss bruto -1.85% neto -2.95%
- 2026-09-28 21:50 [c_banda_atr] CIERRE NIGHT stop-loss bruto -2.01% neto -3.11%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
