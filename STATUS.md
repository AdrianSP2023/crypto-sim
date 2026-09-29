# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 04:11 UTC · vueltas 206 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 855.65 € (-7.42%) | 141 | 9 | 17% | -0.832% | -1.932% | -2.057% | -68.99 € |
| reversion_bb | 918.80 € (-0.59%) | 41 | 1 | 61% | +0.486% | -0.614% | -0.785% | -5.44 € |
| ruptura_volumen | 871.00 € (-5.76%) | 116 | 4 | 13% | -0.544% | -1.644% | -1.762% | -52.91 € |
| rebote_extremo | 919.31 € (-0.53%) | 17 | 10 | 35% | -0.199% | -1.299% | -1.597% | -6.32 € |
| pullback_tendencia | 902.98 € (-2.30%) | 62 | 1 | 19% | -0.283% | -1.383% | -1.475% | -21.13 € |
| macd_momentum | 884.99 € (-4.25%) | 127 | 1 | 17% | -0.224% | -1.324% | -1.436% | -39.35 € |
| estocastico_rebote | 886.45 € (-4.09%) | 103 | 5 | 25% | -0.468% | -1.568% | -1.666% | -37.86 € |
| c_banda_atr_filtro | 889.19 € (-3.79%) | 63 | 2 | 5% | -1.325% | -2.425% | -2.543% | -34.95 € |
| ruptura_volumen_filtro | 894.97 € (-3.17%) | 67 | 1 | 7% | -0.808% | -1.908% | -2.024% | -29.22 € |
| macd_momentum_filtro | 905.52 € (-2.03%) | 54 | 0 | 9% | -0.411% | -1.511% | -1.617% | -18.72 € |
| pullback_tendencia_filtro | 914.78 € (-1.02%) | 27 | 0 | 11% | -0.422% | -1.522% | -1.579% | -9.46 € |
| estocastico_rebote_filtro | 915.40 € (-0.96%) | 21 | 0 | 14% | -0.727% | -1.827% | -1.934% | -8.84 € |
| ruptura_estricta | 912.65 € (-1.25%) | 20 | 1 | 10% | -1.388% | -2.488% | -2.633% | -11.46 € |
| macd_sin_salida | 905.24 € (-2.06%) | 49 | 1 | 22% | -0.595% | -1.695% | -1.810% | -19.08 € |
| c_banda_atr_tope | 922.93 € (-0.14%) | 5 | 4 | 20% | -0.800% | -1.900% | -2.115% | -2.19 € |
| ruptura_volumen_tope | 924.22 € (-0.00%) | 1 | 4 | 100% | +2.500% | +1.400% | +1.330% | +0.32 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 04:10 | c_banda_atr_tope | XDC | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 04:10 | c_banda_atr | XDC | stop-loss | -1.50% | -2.60% | -0.56 |
| 2026-09-29 04:05 | ruptura_volumen_tope | ICP | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 04:05 | ruptura_estricta | ICP | take-profit | +3.00% | +1.90% | +0.43 |
| 2026-09-29 04:05 | ruptura_volumen_filtro | ICP | take-profit | +2.50% | +1.40% | +0.31 |
| 2026-09-29 04:05 | ruptura_volumen | ICP | take-profit | +2.50% | +1.40% | +0.30 |
| 2026-09-29 03:55 | ruptura_estricta | WLFI | timeout | -1.20% | -2.30% | -0.53 |
| 2026-09-29 03:55 | reversion_bb | SOL | timeout | +0.12% | -0.98% | -0.23 |
| 2026-09-29 03:45 | macd_sin_salida | ALGO | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 03:45 | macd_sin_salida | BTC | timeout | -0.45% | -1.55% | -0.35 |
| 2026-09-29 03:45 | macd_momentum | ALGO | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 03:35 | macd_sin_salida | ICP | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 03:35 | macd_momentum | ICP | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 03:35 | pullback_tendencia | ICP | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 03:35 | reversion_bb | NIGHT | take-profit | +1.88% | +0.78% | +0.18 |

## Eventos de la última vuelta

- 2026-09-29 04:10 [c_banda_atr] CIERRE XDC stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 04:10 [reversion_bb] ENTRADA XDC @ 0.02957 (22.97 €)
- 2026-09-29 04:10 [c_banda_atr_tope] CIERRE XDC stop-loss bruto -1.50% neto -2.60%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
