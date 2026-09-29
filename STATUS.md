# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 06:21 UTC · vueltas 232 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 857.30 € (-7.24%) | 154 | 26 | 21% | -0.674% | -1.774% | -1.900% | -69.17 € |
| reversion_bb | 918.89 € (-0.58%) | 42 | 0 | 62% | +0.511% | -0.589% | -0.762% | -5.35 € |
| ruptura_volumen | 867.79 € (-6.11%) | 133 | 29 | 14% | -0.473% | -1.573% | -1.695% | -56.92 € |
| rebote_extremo | 917.94 € (-0.68%) | 27 | 0 | 41% | +0.285% | -0.815% | -1.073% | -6.30 € |
| pullback_tendencia | 903.16 € (-2.28%) | 66 | 0 | 23% | -0.196% | -1.296% | -1.390% | -21.08 € |
| macd_momentum | 880.40 € (-4.74%) | 149 | 32 | 17% | -0.234% | -1.334% | -1.445% | -46.12 € |
| estocastico_rebote | 884.75 € (-4.27%) | 110 | 1 | 25% | -0.435% | -1.535% | -1.632% | -39.51 € |
| c_banda_atr_filtro | 890.53 € (-3.65%) | 72 | 25 | 11% | -1.088% | -2.188% | -2.308% | -36.03 € |
| ruptura_volumen_filtro | 892.60 € (-3.42%) | 79 | 28 | 10% | -0.686% | -1.786% | -1.907% | -32.18 € |
| macd_momentum_filtro | 900.98 € (-2.52%) | 73 | 32 | 10% | -0.434% | -1.534% | -1.636% | -25.59 € |
| pullback_tendencia_filtro | 914.62 € (-1.04%) | 30 | 0 | 17% | -0.293% | -1.393% | -1.459% | -9.62 € |
| estocastico_rebote_filtro | 914.23 € (-1.08%) | 23 | 1 | 13% | -0.795% | -1.895% | -2.002% | -10.03 € |
| ruptura_estricta | 911.63 € (-1.36%) | 24 | 17 | 12% | -1.290% | -2.390% | -2.535% | -13.20 € |
| macd_sin_salida | 907.42 € (-1.82%) | 55 | 35 | 27% | -0.437% | -1.537% | -1.660% | -19.42 € |
| c_banda_atr_tope | 921.81 € (-0.26%) | 13 | 4 | 46% | +0.130% | -0.970% | -1.146% | -2.91 € |
| ruptura_volumen_tope | 923.56 € (-0.07%) | 8 | 5 | 38% | +0.641% | -0.459% | -0.604% | -0.85 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 06:20 | ruptura_estricta | CRV | take-profit | +3.00% | +1.90% | +0.43 |
| 2026-09-29 06:20 | pullback_tendencia_filtro | CRV | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 06:20 | ruptura_volumen_filtro | VVV | timeout | +0.25% | -0.85% | -0.19 |
| 2026-09-29 06:20 | ruptura_volumen_filtro | HYPE | timeout | +0.47% | -0.63% | -0.14 |
| 2026-09-29 06:20 | pullback_tendencia | CRV | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 06:20 | ruptura_volumen | VVV | timeout | +0.25% | -0.85% | -0.18 |
| 2026-09-29 06:20 | ruptura_volumen | HYPE | timeout | +0.47% | -0.63% | -0.14 |
| 2026-09-29 06:15 | ruptura_volumen_tope | XPL | timeout | -0.58% | -1.69% | -0.39 |
| 2026-09-29 06:15 | c_banda_atr_tope | EIGEN | take-profit | +2.02% | +0.92% | +0.21 |
| 2026-09-29 06:15 | c_banda_atr_tope | ICP | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 06:15 | macd_sin_salida | RAY | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 06:15 | estocastico_rebote_filtro | ALGO | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 06:15 | macd_momentum_filtro | ZRO | momentum perdido | -0.52% | -1.62% | -0.36 |
| 2026-09-29 06:15 | ruptura_volumen_filtro | CC | stop-loss | -1.40% | -2.50% | -0.56 |
| 2026-09-29 06:15 | c_banda_atr_filtro | RAY | take-profit | +2.00% | +0.90% | +0.20 |

## Eventos de la última vuelta

- 2026-09-29 06:20 [ruptura_volumen] CIERRE HYPE timeout bruto +0.47% neto -0.63%
- 2026-09-29 06:20 [ruptura_volumen_filtro] CIERRE HYPE timeout bruto +0.47% neto -0.63%
- 2026-09-29 06:20 [ruptura_volumen] ENTRADA TRX @ 0.29454 (21.69 €)
- 2026-09-29 06:20 [ruptura_volumen_filtro] ENTRADA TRX @ 0.29454 (22.31 €)
- 2026-09-29 06:20 [ruptura_estricta] ENTRADA TRX @ 0.29454 (22.77 €)
- 2026-09-29 06:20 [macd_momentum] ENTRADA RENDER @ 1.688 (21.95 €)
- 2026-09-29 06:20 [macd_momentum_filtro] ENTRADA RENDER @ 1.688 (22.47 €)
- 2026-09-29 06:20 [macd_sin_salida] ENTRADA RENDER @ 1.688 (22.62 €)
- 2026-09-29 06:20 [ruptura_volumen] CIERRE VVV timeout bruto +0.25% neto -0.85%
- 2026-09-29 06:20 [ruptura_volumen_filtro] CIERRE VVV timeout bruto +0.25% neto -0.85%
- 2026-09-29 06:20 [pullback_tendencia] CIERRE CRV take-profit bruto +2.00% neto +0.90%
- 2026-09-29 06:20 [pullback_tendencia_filtro] CIERRE CRV take-profit bruto +2.00% neto +0.90%
- 2026-09-29 06:20 [ruptura_estricta] CIERRE CRV take-profit bruto +3.00% neto +1.90%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
