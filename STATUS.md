# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 03:56 UTC · vueltas 203 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 856.69 € (-7.31%) | 140 | 10 | 17% | -0.827% | -1.927% | -2.051% | -68.43 € |
| reversion_bb | 918.80 € (-0.59%) | 41 | 0 | 61% | +0.486% | -0.614% | -0.785% | -5.44 € |
| ruptura_volumen | 871.51 € (-5.71%) | 115 | 5 | 12% | -0.571% | -1.671% | -1.789% | -53.22 € |
| rebote_extremo | 920.21 € (-0.44%) | 17 | 10 | 35% | -0.199% | -1.299% | -1.597% | -6.32 € |
| pullback_tendencia | 903.12 € (-2.29%) | 62 | 0 | 19% | -0.283% | -1.383% | -1.475% | -21.13 € |
| macd_momentum | 885.11 € (-4.23%) | 127 | 1 | 17% | -0.224% | -1.324% | -1.436% | -39.35 € |
| estocastico_rebote | 887.05 € (-4.02%) | 103 | 5 | 25% | -0.468% | -1.568% | -1.666% | -37.86 € |
| c_banda_atr_filtro | 889.27 € (-3.78%) | 63 | 2 | 5% | -1.325% | -2.425% | -2.543% | -34.95 € |
| ruptura_volumen_filtro | 894.92 € (-3.17%) | 66 | 2 | 6% | -0.858% | -1.958% | -2.075% | -29.53 € |
| macd_momentum_filtro | 905.52 € (-2.03%) | 54 | 0 | 9% | -0.411% | -1.511% | -1.617% | -18.72 € |
| pullback_tendencia_filtro | 914.78 € (-1.02%) | 27 | 0 | 11% | -0.422% | -1.522% | -1.579% | -9.46 € |
| estocastico_rebote_filtro | 915.40 € (-0.96%) | 21 | 0 | 14% | -0.727% | -1.827% | -1.934% | -8.84 € |
| ruptura_estricta | 912.71 € (-1.25%) | 19 | 2 | 5% | -1.619% | -2.719% | -2.868% | -11.90 € |
| macd_sin_salida | 905.37 € (-2.04%) | 49 | 1 | 22% | -0.595% | -1.695% | -1.810% | -19.08 € |
| c_banda_atr_tope | 923.54 € (-0.08%) | 4 | 5 | 25% | -0.625% | -1.725% | -1.948% | -1.59 € |
| ruptura_volumen_tope | 924.76 € (+0.06%) | 0 | 5 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 03:55 | ruptura_estricta | WLFI | timeout | -1.20% | -2.30% | -0.53 |
| 2026-09-29 03:55 | reversion_bb | SOL | timeout | +0.12% | -0.98% | -0.23 |
| 2026-09-29 03:45 | macd_sin_salida | ALGO | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 03:45 | macd_sin_salida | BTC | timeout | -0.45% | -1.55% | -0.35 |
| 2026-09-29 03:45 | macd_momentum | ALGO | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 03:35 | macd_sin_salida | ICP | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 03:35 | macd_momentum | ICP | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 03:35 | pullback_tendencia | ICP | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 03:35 | reversion_bb | NIGHT | take-profit | +1.88% | +0.78% | +0.18 |
| 2026-09-29 03:30 | estocastico_rebote | ICP | take-profit | +1.88% | +0.78% | +0.17 |
| 2026-09-29 03:25 | macd_sin_salida | CRV | take-profit | +2.26% | +1.16% | +0.26 |
| 2026-09-29 03:25 | estocastico_rebote | XDC | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-29 03:25 | macd_momentum | CRV | take-profit | +2.26% | +1.16% | +0.26 |
| 2026-09-29 03:25 | rebote_extremo | ARB | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 03:20 | c_banda_atr_tope | CRV | take-profit | +2.00% | +0.90% | +0.21 |

## Eventos de la última vuelta

- 2026-09-29 03:55 [reversion_bb] CIERRE SOL timeout bruto +0.12% neto -0.98%
- 2026-09-29 03:55 [ruptura_volumen] ENTRADA W @ 0.01212 (21.78 €)
- 2026-09-29 03:55 [ruptura_volumen_filtro] ENTRADA W @ 0.01212 (22.37 €)
- 2026-09-29 03:55 [ruptura_volumen_tope] ENTRADA W @ 0.01212 (23.11 €)
- 2026-09-29 03:55 [ruptura_estricta] CIERRE WLFI timeout bruto -1.20% neto -2.30%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
