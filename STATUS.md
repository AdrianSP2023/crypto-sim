# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 04:31 UTC · vueltas 210 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 855.99 € (-7.38%) | 144 | 12 | 18% | -0.786% | -1.886% | -2.012% | -68.83 € |
| reversion_bb | 918.93 € (-0.57%) | 41 | 1 | 61% | +0.486% | -0.614% | -0.785% | -5.44 € |
| ruptura_volumen | 871.75 € (-5.68%) | 116 | 15 | 13% | -0.544% | -1.644% | -1.762% | -52.91 € |
| rebote_extremo | 919.01 € (-0.57%) | 23 | 4 | 30% | +0.097% | -1.003% | -1.274% | -6.54 € |
| pullback_tendencia | 903.69 € (-2.22%) | 62 | 2 | 19% | -0.283% | -1.383% | -1.475% | -21.13 € |
| macd_momentum | 885.23 € (-4.22%) | 127 | 2 | 17% | -0.224% | -1.324% | -1.436% | -39.35 € |
| estocastico_rebote | 886.65 € (-4.07%) | 105 | 3 | 25% | -0.451% | -1.551% | -1.648% | -38.17 € |
| c_banda_atr_filtro | 888.89 € (-3.82%) | 64 | 8 | 5% | -1.309% | -2.409% | -2.525% | -35.27 € |
| ruptura_volumen_filtro | 895.23 € (-3.14%) | 67 | 11 | 7% | -0.808% | -1.908% | -2.024% | -29.22 € |
| macd_momentum_filtro | 905.52 € (-2.03%) | 54 | 1 | 9% | -0.411% | -1.511% | -1.617% | -18.72 € |
| pullback_tendencia_filtro | 914.97 € (-1.00%) | 27 | 1 | 11% | -0.422% | -1.522% | -1.579% | -9.46 € |
| estocastico_rebote_filtro | 915.40 € (-0.96%) | 21 | 0 | 14% | -0.727% | -1.827% | -1.934% | -8.84 € |
| ruptura_estricta | 912.79 € (-1.24%) | 20 | 1 | 10% | -1.388% | -2.488% | -2.633% | -11.46 € |
| macd_sin_salida | 905.49 € (-2.03%) | 49 | 2 | 22% | -0.595% | -1.695% | -1.810% | -19.08 € |
| c_banda_atr_tope | 923.12 € (-0.12%) | 7 | 5 | 43% | +0.054% | -1.046% | -1.263% | -1.69 € |
| ruptura_volumen_tope | 925.12 € (+0.10%) | 1 | 5 | 100% | +2.500% | +1.400% | +1.330% | +0.32 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 04:30 | rebote_extremo | TRUMP | timeout | +0.94% | -0.17% | -0.04 |
| 2026-09-29 04:30 | rebote_extremo | PENGU | timeout | +0.52% | -0.58% | -0.13 |
| 2026-09-29 04:30 | rebote_extremo | XPL | timeout | +1.90% | +0.80% | +0.18 |
| 2026-09-29 04:25 | c_banda_atr_tope | XPL | take-profit | +2.02% | +0.92% | +0.21 |
| 2026-09-29 04:25 | c_banda_atr_filtro | TRX | timeout | -0.32% | -1.42% | -0.32 |
| 2026-09-29 04:25 | estocastico_rebote | NIGHT | timeout | +0.65% | -0.45% | -0.10 |
| 2026-09-29 04:25 | estocastico_rebote | ETH | timeout | +0.18% | -0.92% | -0.20 |
| 2026-09-29 04:25 | c_banda_atr | TRX | timeout | -0.32% | -1.42% | -0.31 |
| 2026-09-29 04:25 | c_banda_atr | XPL | take-profit | +2.02% | +0.92% | +0.20 |
| 2026-09-29 04:20 | c_banda_atr_tope | W | take-profit | +2.35% | +1.25% | +0.29 |
| 2026-09-29 04:20 | rebote_extremo | SEI | timeout | +0.75% | -0.35% | -0.08 |
| 2026-09-29 04:20 | rebote_extremo | FET | timeout | +1.08% | -0.02% | -0.01 |
| 2026-09-29 04:20 | rebote_extremo | SUI | timeout | +0.44% | -0.66% | -0.15 |
| 2026-09-29 04:20 | c_banda_atr | W | take-profit | +2.35% | +1.25% | +0.27 |
| 2026-09-29 04:10 | c_banda_atr_tope | XDC | stop-loss | -1.50% | -2.60% | -0.60 |

## Eventos de la última vuelta

- 2026-09-29 04:30 [rebote_extremo] CIERRE XPL timeout bruto +1.90% neto +0.80%
- 2026-09-29 04:30 [c_banda_atr_filtro] ENTRADA FIL @ 0.909 (22.22 €)
- 2026-09-29 04:30 [c_banda_atr] ENTRADA PENGU @ 0.00809 (21.39 €)
- 2026-09-29 04:30 [rebote_extremo] CIERRE PENGU timeout bruto +0.52% neto -0.58%
- 2026-09-29 04:30 [c_banda_atr_filtro] ENTRADA PENGU @ 0.00809 (22.22 €)
- 2026-09-29 04:30 [ruptura_volumen] ENTRADA TON @ 1.384 (21.78 €)
- 2026-09-29 04:30 [ruptura_volumen_filtro] ENTRADA TON @ 1.384 (22.38 €)
- 2026-09-29 04:30 [rebote_extremo] CIERRE TRUMP timeout bruto +0.94% neto -0.16%
- 2026-09-29 04:30 [c_banda_atr] ENTRADA NIGHT @ 0.02493 (21.39 €)
- 2026-09-29 04:30 [ruptura_volumen] ENTRADA NIGHT @ 0.02493 (21.78 €)
- 2026-09-29 04:30 [c_banda_atr_filtro] ENTRADA NIGHT @ 0.02493 (22.22 €)
- 2026-09-29 04:30 [ruptura_volumen_filtro] ENTRADA NIGHT @ 0.02493 (22.38 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
