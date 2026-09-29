# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 04:41 UTC · vueltas 212 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 855.30 € (-7.46%) | 144 | 12 | 18% | -0.786% | -1.886% | -2.012% | -68.83 € |
| reversion_bb | 918.91 € (-0.58%) | 41 | 1 | 61% | +0.486% | -0.614% | -0.785% | -5.44 € |
| ruptura_volumen | 870.88 € (-5.77%) | 118 | 15 | 14% | -0.525% | -1.625% | -1.742% | -53.12 € |
| rebote_extremo | 917.94 € (-0.68%) | 27 | 0 | 41% | +0.285% | -0.815% | -1.073% | -6.30 € |
| pullback_tendencia | 903.47 € (-2.25%) | 63 | 2 | 21% | -0.247% | -1.347% | -1.438% | -20.92 € |
| macd_momentum | 885.11 € (-4.23%) | 127 | 3 | 17% | -0.224% | -1.324% | -1.436% | -39.35 € |
| estocastico_rebote | 886.39 € (-4.10%) | 105 | 3 | 25% | -0.451% | -1.551% | -1.648% | -38.17 € |
| c_banda_atr_filtro | 888.45 € (-3.87%) | 64 | 8 | 5% | -1.309% | -2.409% | -2.525% | -35.27 € |
| ruptura_volumen_filtro | 894.37 € (-3.23%) | 68 | 12 | 7% | -0.814% | -1.914% | -2.030% | -29.75 € |
| macd_momentum_filtro | 905.39 € (-2.04%) | 54 | 2 | 9% | -0.411% | -1.511% | -1.617% | -18.72 € |
| pullback_tendencia_filtro | 914.92 € (-1.01%) | 27 | 2 | 11% | -0.422% | -1.522% | -1.579% | -9.46 € |
| estocastico_rebote_filtro | 915.40 € (-0.96%) | 21 | 0 | 14% | -0.727% | -1.827% | -1.934% | -8.84 € |
| ruptura_estricta | 913.15 € (-1.20%) | 20 | 2 | 10% | -1.388% | -2.488% | -2.633% | -11.46 € |
| macd_sin_salida | 905.37 € (-2.04%) | 49 | 3 | 22% | -0.595% | -1.695% | -1.810% | -19.08 € |
| c_banda_atr_tope | 922.69 € (-0.17%) | 7 | 5 | 43% | +0.054% | -1.046% | -1.263% | -1.69 € |
| ruptura_volumen_tope | 925.02 € (+0.08%) | 2 | 4 | 100% | +2.500% | +1.400% | +1.262% | +0.65 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 04:40 | ruptura_volumen_tope | CRV | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 04:40 | ruptura_volumen_filtro | XLM | stop-loss | -1.26% | -2.36% | -0.53 |
| 2026-09-29 04:40 | pullback_tendencia | ALGO | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 04:40 | rebote_extremo | KAS | timeout | +1.23% | +0.13% | +0.03 |
| 2026-09-29 04:40 | rebote_extremo | RENDER | timeout | +1.45% | +0.35% | +0.08 |
| 2026-09-29 04:40 | ruptura_volumen | CRV | take-profit | +2.50% | +1.40% | +0.30 |
| 2026-09-29 04:40 | ruptura_volumen | XLM | stop-loss | -1.26% | -2.36% | -0.51 |
| 2026-09-29 04:35 | rebote_extremo | SHIB | timeout | +1.54% | +0.45% | +0.10 |
| 2026-09-29 04:35 | rebote_extremo | RAY | timeout | +1.24% | +0.14% | +0.03 |
| 2026-09-29 04:30 | rebote_extremo | TRUMP | timeout | +0.94% | -0.17% | -0.04 |
| 2026-09-29 04:30 | rebote_extremo | PENGU | timeout | +0.52% | -0.58% | -0.13 |
| 2026-09-29 04:30 | rebote_extremo | XPL | timeout | +1.90% | +0.80% | +0.18 |
| 2026-09-29 04:25 | c_banda_atr_tope | XPL | take-profit | +2.02% | +0.92% | +0.21 |
| 2026-09-29 04:25 | c_banda_atr_filtro | TRX | timeout | -0.32% | -1.42% | -0.32 |
| 2026-09-29 04:25 | estocastico_rebote | NIGHT | timeout | +0.65% | -0.45% | -0.10 |

## Eventos de la última vuelta

- 2026-09-29 04:40 [ruptura_volumen] CIERRE XLM stop-loss bruto -1.26% neto -2.36%
- 2026-09-29 04:40 [ruptura_volumen_filtro] CIERRE XLM stop-loss bruto -1.26% neto -2.36%
- 2026-09-29 04:40 [ruptura_volumen] ENTRADA ALGO @ 0.12176 (21.77 €)
- 2026-09-29 04:40 [pullback_tendencia] CIERRE ALGO take-profit bruto +2.00% neto +0.90%
- 2026-09-29 04:40 [ruptura_volumen_filtro] ENTRADA ALGO @ 0.12176 (22.36 €)
- 2026-09-29 04:40 [ruptura_estricta] ENTRADA ALGO @ 0.12176 (22.82 €)
- 2026-09-29 04:40 [rebote_extremo] CIERRE RENDER timeout bruto +1.45% neto +0.35%
- 2026-09-29 04:40 [ruptura_volumen] CIERRE CRV take-profit bruto +2.50% neto +1.40%
- 2026-09-29 04:40 [pullback_tendencia] ENTRADA CRV @ 0.3444 (22.58 €)
- 2026-09-29 04:40 [macd_momentum] ENTRADA CRV @ 0.3444 (22.12 €)
- 2026-09-29 04:40 [macd_momentum_filtro] ENTRADA CRV @ 0.3444 (22.64 €)
- 2026-09-29 04:40 [pullback_tendencia_filtro] ENTRADA CRV @ 0.3444 (22.87 €)
- 2026-09-29 04:40 [macd_sin_salida] ENTRADA CRV @ 0.3444 (22.63 €)
- 2026-09-29 04:40 [ruptura_volumen_tope] CIERRE CRV take-profit bruto +2.50% neto +1.40%
- 2026-09-29 04:40 [rebote_extremo] CIERRE KAS timeout bruto +1.23% neto +0.13%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
