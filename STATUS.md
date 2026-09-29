# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 04:21 UTC · vueltas 208 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 856.25 € (-7.36%) | 142 | 9 | 18% | -0.810% | -1.910% | -2.035% | -68.72 € |
| reversion_bb | 918.91 € (-0.58%) | 41 | 1 | 61% | +0.486% | -0.614% | -0.785% | -5.44 € |
| ruptura_volumen | 871.80 € (-5.67%) | 116 | 9 | 13% | -0.544% | -1.644% | -1.762% | -52.91 € |
| rebote_extremo | 919.07 € (-0.56%) | 20 | 7 | 30% | -0.056% | -1.156% | -1.440% | -6.55 € |
| pullback_tendencia | 903.30 € (-2.27%) | 62 | 1 | 19% | -0.283% | -1.383% | -1.475% | -21.13 € |
| macd_momentum | 884.99 € (-4.25%) | 127 | 1 | 17% | -0.224% | -1.324% | -1.436% | -39.35 € |
| estocastico_rebote | 887.21 € (-4.01%) | 103 | 5 | 25% | -0.468% | -1.568% | -1.666% | -37.86 € |
| c_banda_atr_filtro | 889.18 € (-3.79%) | 63 | 3 | 5% | -1.325% | -2.425% | -2.543% | -34.95 € |
| ruptura_volumen_filtro | 895.26 € (-3.14%) | 67 | 5 | 7% | -0.808% | -1.908% | -2.024% | -29.22 € |
| macd_momentum_filtro | 905.52 € (-2.03%) | 54 | 0 | 9% | -0.411% | -1.511% | -1.617% | -18.72 € |
| pullback_tendencia_filtro | 914.78 € (-1.02%) | 27 | 0 | 11% | -0.422% | -1.522% | -1.579% | -9.46 € |
| estocastico_rebote_filtro | 915.40 € (-0.96%) | 21 | 0 | 14% | -0.727% | -1.827% | -1.934% | -8.84 € |
| ruptura_estricta | 912.84 € (-1.23%) | 20 | 1 | 10% | -1.388% | -2.488% | -2.633% | -11.46 € |
| macd_sin_salida | 905.24 € (-2.06%) | 49 | 1 | 22% | -0.595% | -1.695% | -1.810% | -19.08 € |
| c_banda_atr_tope | 923.08 € (-0.13%) | 6 | 4 | 33% | -0.275% | -1.375% | -1.589% | -1.91 € |
| ruptura_volumen_tope | 925.07 € (+0.09%) | 1 | 5 | 100% | +2.500% | +1.400% | +1.330% | +0.32 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 04:20 | c_banda_atr_tope | W | take-profit | +2.35% | +1.25% | +0.29 |
| 2026-09-29 04:20 | rebote_extremo | SEI | timeout | +0.75% | -0.35% | -0.08 |
| 2026-09-29 04:20 | rebote_extremo | FET | timeout | +1.08% | -0.02% | -0.01 |
| 2026-09-29 04:20 | rebote_extremo | SUI | timeout | +0.44% | -0.66% | -0.15 |
| 2026-09-29 04:20 | c_banda_atr | W | take-profit | +2.35% | +1.25% | +0.27 |
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

## Eventos de la última vuelta

- 2026-09-29 04:20 [rebote_extremo] CIERRE SUI timeout bruto +0.44% neto -0.66%
- 2026-09-29 04:20 [ruptura_volumen] ENTRADA PUMP @ 0.004278 (21.78 €)
- 2026-09-29 04:20 [ruptura_volumen_filtro] ENTRADA PUMP @ 0.004278 (22.38 €)
- 2026-09-29 04:20 [ruptura_volumen] ENTRADA XLM @ 0.200317 (21.78 €)
- 2026-09-29 04:20 [ruptura_volumen_filtro] ENTRADA XLM @ 0.200317 (22.38 €)
- 2026-09-29 04:20 [ruptura_volumen] ENTRADA HYPE @ 76.85 (21.78 €)
- 2026-09-29 04:20 [ruptura_volumen_filtro] ENTRADA HYPE @ 76.85 (22.38 €)
- 2026-09-29 04:20 [c_banda_atr] CIERRE W take-profit bruto +2.35% neto +1.25%
- 2026-09-29 04:20 [c_banda_atr_tope] CIERRE W take-profit bruto +2.35% neto +1.25%
- 2026-09-29 04:20 [rebote_extremo] CIERRE FET timeout bruto +1.08% neto -0.02%
- 2026-09-29 04:20 [c_banda_atr] ENTRADA ZRO @ 1.355 (21.39 €)
- 2026-09-29 04:20 [c_banda_atr_filtro] ENTRADA ZRO @ 1.355 (22.23 €)
- 2026-09-29 04:20 [c_banda_atr_tope] ENTRADA ZRO @ 1.355 (23.06 €)
- 2026-09-29 04:20 [rebote_extremo] CIERRE SEI timeout bruto +0.75% neto -0.35%
- 2026-09-29 04:20 [ruptura_volumen] ENTRADA VVV @ 24.113 (21.78 €)
- 2026-09-29 04:20 [ruptura_volumen_filtro] ENTRADA VVV @ 24.113 (22.38 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
