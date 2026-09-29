# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 02:31 UTC · vueltas 186 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 855.67 € (-7.42%) | 138 | 4 | 17% | -0.843% | -1.943% | -2.067% | -68.06 € |
| reversion_bb | 919.43 € (-0.52%) | 37 | 4 | 65% | +0.566% | -0.534% | -0.708% | -4.20 € |
| ruptura_volumen | 871.02 € (-5.76%) | 115 | 0 | 12% | -0.571% | -1.671% | -1.789% | -53.22 € |
| rebote_extremo | 917.36 € (-0.74%) | 13 | 14 | 38% | +0.047% | -1.053% | -1.392% | -4.38 € |
| pullback_tendencia | 902.71 € (-2.33%) | 60 | 0 | 17% | -0.359% | -1.459% | -1.550% | -21.53 € |
| macd_momentum | 884.25 € (-4.33%) | 124 | 0 | 15% | -0.279% | -1.379% | -1.490% | -40.00 € |
| estocastico_rebote | 887.93 € (-3.93%) | 95 | 10 | 24% | -0.497% | -1.597% | -1.697% | -35.69 € |
| c_banda_atr_filtro | 889.21 € (-3.79%) | 63 | 1 | 5% | -1.325% | -2.425% | -2.543% | -34.95 € |
| ruptura_volumen_filtro | 894.71 € (-3.20%) | 66 | 0 | 6% | -0.858% | -1.958% | -2.075% | -29.53 € |
| macd_momentum_filtro | 905.52 € (-2.03%) | 54 | 0 | 9% | -0.411% | -1.511% | -1.617% | -18.72 € |
| pullback_tendencia_filtro | 914.78 € (-1.02%) | 27 | 0 | 11% | -0.422% | -1.522% | -1.579% | -9.46 € |
| estocastico_rebote_filtro | 915.40 € (-0.96%) | 21 | 0 | 14% | -0.727% | -1.827% | -1.934% | -8.84 € |
| ruptura_estricta | 912.60 € (-1.26%) | 18 | 1 | 6% | -1.642% | -2.742% | -2.888% | -11.37 € |
| macd_sin_salida | 904.96 € (-2.09%) | 44 | 2 | 18% | -0.759% | -1.859% | -1.974% | -18.80 € |
| c_banda_atr_tope | 922.25 € (-0.22%) | 3 | 2 | 0% | -1.500% | -2.600% | -2.815% | -1.80 € |
| ruptura_volumen_tope | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 02:30 | c_banda_atr_tope | W | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 02:30 | macd_sin_salida | ALGO | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 02:30 | ruptura_estricta | AVAX | timeout | -1.59% | -2.69% | -0.62 |
| 2026-09-29 02:30 | macd_momentum | ICP | momentum perdido | -1.43% | -2.53% | -0.56 |
| 2026-09-29 02:30 | macd_momentum | ALGO | stop-loss | -1.50% | -2.60% | -0.58 |
| 2026-09-29 02:30 | reversion_bb | XDC | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-09-29 02:30 | c_banda_atr | W | stop-loss | -1.50% | -2.60% | -0.56 |
| 2026-09-29 02:25 | estocastico_rebote | VIRTUAL | stop-loss | -1.91% | -3.01% | -0.67 |
| 2026-09-29 02:15 | c_banda_atr_tope | FET | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 02:15 | macd_sin_salida | CRV | stop-loss | -1.84% | -2.94% | -0.67 |
| 2026-09-29 02:15 | estocastico_rebote | ADA | stop-loss | -1.50% | -2.60% | -0.58 |
| 2026-09-29 02:15 | estocastico_rebote | LINK | stop-loss | -1.50% | -2.60% | -0.58 |
| 2026-09-29 02:15 | macd_momentum | CRV | stop-loss | -1.84% | -2.94% | -0.65 |
| 2026-09-29 02:15 | c_banda_atr | FET | stop-loss | -1.50% | -2.60% | -0.56 |
| 2026-09-29 02:10 | c_banda_atr_tope | HBAR | stop-loss | -1.50% | -2.60% | -0.60 |

## Eventos de la última vuelta

- 2026-09-29 02:30 [ruptura_estricta] CIERRE AVAX timeout bruto -1.59% neto -2.69%
- 2026-09-29 02:30 [c_banda_atr] ENTRADA XDC @ 0.03032 (21.42 €)
- 2026-09-29 02:30 [reversion_bb] CIERRE XDC take-profit bruto +1.50% neto +0.40%
- 2026-09-29 02:30 [c_banda_atr_tope] ENTRADA XDC @ 0.03032 (23.08 €)
- 2026-09-29 02:30 [macd_momentum] CIERRE ALGO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 02:30 [macd_sin_salida] CIERRE ALGO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 02:30 [c_banda_atr] CIERRE W stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 02:30 [c_banda_atr_tope] CIERRE W stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 02:30 [macd_momentum] CIERRE ICP momentum perdido bruto -1.43% neto -2.53%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
