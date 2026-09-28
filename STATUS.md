# Simulación P1 (sin dinero real)

Config `P1-v9` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-28 20:31 UTC · vueltas 142 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 879.67 € (-4.82%) | 84 | 17 | 18% | -0.803% | -1.903% | -2.022% | -44.41 € |
| reversion_bb | 925.29 € (+0.11%) | 12 | 7 | 75% | +0.836% | -0.264% | -0.473% | -0.36 € |
| ruptura_volumen | 886.79 € (-4.05%) | 78 | 2 | 14% | -0.447% | -1.547% | -1.671% | -37.41 € |
| rebote_extremo | 923.19 € (-0.11%) | 7 | 3 | 71% | +0.910% | -0.190% | -0.602% | -1.53 € |
| pullback_tendencia | 908.59 € (-1.69%) | 44 | 3 | 20% | -0.340% | -1.440% | -1.542% | -16.06 € |
| macd_momentum | 899.36 € (-2.69%) | 72 | 16 | 12% | -0.336% | -1.436% | -1.549% | -24.86 € |
| estocastico_rebote | 903.02 € (-2.30%) | 59 | 12 | 29% | -0.417% | -1.517% | -1.615% | -21.71 € |
| c_banda_atr_filtro | 900.03 € (-2.62%) | 43 | 3 | 7% | -1.335% | -2.435% | -2.564% | -24.15 € |
| ruptura_volumen_filtro | 910.69 € (-1.47%) | 33 | 1 | 9% | -0.679% | -1.779% | -1.904% | -13.51 € |
| macd_momentum_filtro | 911.02 € (-1.43%) | 40 | 0 | 12% | -0.335% | -1.435% | -1.538% | -13.22 € |
| pullback_tendencia_filtro | 917.83 € (-0.69%) | 18 | 0 | 17% | -0.443% | -1.543% | -1.609% | -6.41 € |
| estocastico_rebote_filtro | 920.43 € (-0.41%) | 11 | 2 | 27% | -0.318% | -1.418% | -1.547% | -3.60 € |
| ruptura_estricta | 921.76 € (-0.27%) | 5 | 0 | 20% | -1.045% | -2.145% | -2.276% | -2.48 € |
| macd_sin_salida | 923.35 € (-0.10%) | 1 | 17 | 0% | -1.500% | -2.600% | -2.740% | -0.60 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-28 20:30 | ruptura_estricta | CRV | take-profit | +3.00% | +1.90% | +0.44 |
| 2026-09-28 20:30 | macd_momentum | NIGHT | momentum perdido | -1.17% | -2.27% | -0.51 |
| 2026-09-28 20:30 | reversion_bb | OP | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-28 20:25 | estocastico_rebote | ALGO | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-28 20:20 | estocastico_rebote_filtro | MON | timeout | -0.12% | -1.22% | -0.28 |
| 2026-09-28 20:20 | estocastico_rebote | MON | timeout | -0.12% | -1.22% | -0.28 |
| 2026-09-28 20:15 | estocastico_rebote | PUMP | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-28 20:10 | estocastico_rebote | CRV | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-28 20:10 | estocastico_rebote | LINK | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-28 20:10 | reversion_bb | RENDER | take-profit | +1.86% | +0.77% | +0.18 |
| 2026-09-28 20:10 | reversion_bb | USELESS | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-09-28 20:05 | c_banda_atr_filtro | DASH | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-28 20:05 | estocastico_rebote | XRP | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-28 20:05 | reversion_bb | WLD | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-28 20:05 | c_banda_atr | DASH | stop-loss | -1.50% | -2.60% | -0.59 |

## Eventos de la última vuelta

- 2026-09-28 20:30 [ruptura_volumen] ENTRADA LINK @ 13.4692 (22.17 €)
- 2026-09-28 20:30 [c_banda_atr] ENTRADA MON @ 0.02576 (22.00 €)
- 2026-09-28 20:30 [macd_momentum] ENTRADA ZRO @ 1.375 (22.50 €)
- 2026-09-28 20:30 [macd_sin_salida] ENTRADA ZRO @ 1.375 (23.09 €)
- 2026-09-28 20:30 [macd_momentum] ENTRADA ICP @ 2.67 (22.50 €)
- 2026-09-28 20:30 [macd_sin_salida] ENTRADA ICP @ 2.67 (23.09 €)
- 2026-09-28 20:30 [ruptura_estricta] CIERRE CRV take-profit bruto +3.00% neto +1.90%
- 2026-09-28 20:30 [reversion_bb] CIERRE OP take-profit bruto +1.80% neto +0.70%
- 2026-09-28 20:30 [macd_momentum] CIERRE NIGHT momentum perdido bruto -1.17% neto -2.27%
- 2026-09-28 20:30 [c_banda_atr] ENTRADA CC @ 0.11353 (22.00 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
