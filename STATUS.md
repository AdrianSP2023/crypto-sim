# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 17:52 UTC · vueltas 98 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.33 € (-1.61%) | 54 | 2 | 33% | -0.188% | -1.172% | -1.312% | -14.59 € |
| reversion_bb | 917.97 € (-0.68%) | 12 | 4 | 17% | -1.026% | -2.126% | -2.232% | -5.89 € |
| ruptura_volumen | 909.49 € (-1.60%) | 70 | 1 | 27% | -0.044% | -0.917% | -1.054% | -14.76 € |
| rebote_extremo | 922.94 € (-0.14%) | 4 | 2 | 25% | -0.905% | -2.005% | -2.191% | -1.85 € |
| pullback_tendencia | 907.99 € (-1.76%) | 69 | 0 | 25% | -0.147% | -1.026% | -1.140% | -16.25 € |
| macd_momentum | 897.30 € (-2.91%) | 152 | 1 | 19% | -0.104% | -0.775% | -0.894% | -26.94 € |
| estocastico_rebote | 891.27 € (-3.57%) | 118 | 28 | 28% | -0.398% | -1.120% | -1.241% | -30.21 € |
| ruptura_estricta | 911.41 € (-1.39%) | 42 | 0 | 29% | -0.226% | -1.326% | -1.452% | -12.83 € |
| macd_sin_salida | 903.78 € (-2.21%) | 97 | 2 | 30% | -0.145% | -0.914% | -1.041% | -20.33 € |
| c_banda_atr_tope | 915.60 € (-0.93%) | 21 | 2 | 24% | -0.619% | -1.719% | -1.887% | -8.32 € |
| ruptura_volumen_tope | 919.11 € (-0.55%) | 21 | 1 | 19% | +0.041% | -1.059% | -1.189% | -5.13 € |
| c_banda_atr_regimen | 909.84 € (-1.56%) | 50 | 0 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| c_banda_atr_evento | 915.76 € (-0.92%) | 21 | 3 | 29% | -0.519% | -1.619% | -1.781% | -7.85 € |
| macd_momentum_evento | 911.56 € (-1.37%) | 32 | 1 | 12% | -0.618% | -1.718% | -1.847% | -12.68 € |
| ruptura_volumen_evento | 919.66 € (-0.50%) | 11 | 1 | 18% | -0.704% | -1.804% | -2.004% | -4.58 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 17:50 | macd_momentum_evento | NIGHT | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 17:50 | c_banda_atr_evento | MINA | stop-loss | -1.59% | -2.69% | -0.62 |
| 2026-09-29 17:50 | c_banda_atr_tope | MINA | stop-loss | -1.59% | -2.69% | -0.62 |
| 2026-09-29 17:50 | macd_sin_salida | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:50 | estocastico_rebote | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:50 | macd_momentum | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:50 | c_banda_atr | MINA | stop-loss | -1.59% | -2.09% | -0.47 |
| 2026-09-29 17:45 | reversion_bb | BCH | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 17:40 | macd_sin_salida | MINA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:40 | estocastico_rebote | CRV | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-09-29 17:40 | reversion_bb | ZRO | stop-loss | -1.70% | -2.80% | -0.64 |
| 2026-09-29 17:35 | c_banda_atr_evento | VVV | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 17:35 | c_banda_atr_tope | VVV | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 17:35 | ruptura_estricta | JUP | stop-loss | -2.00% | -3.10% | -0.71 |
| 2026-09-29 17:35 | estocastico_rebote | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-29 17:50 [estocastico_rebote] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 17:45 [estocastico_rebote] ENTRADA PUMP @ 0.005004 (22.35 €, apertura)
- 2026-09-29 17:45 [estocastico_rebote] ENTRADA ZRO @ 1.373 (22.35 €, apertura)
- 2026-09-29 17:50 [c_banda_atr] CIERRE MINA stop-loss bruto -1.59% neto -2.09%
- 2026-09-29 17:50 [c_banda_atr_tope] CIERRE MINA stop-loss bruto -1.59% neto -2.69%
- 2026-09-29 17:50 [c_banda_atr_evento] CIERRE MINA stop-loss bruto -1.59% neto -2.69%
- 2026-09-29 17:50 [macd_momentum] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 17:50 [macd_sin_salida] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 17:50 [macd_momentum_evento] CIERRE NIGHT stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 17:45 [c_banda_atr] ENTRADA ASTER @ 0.63712 (22.74 €, apertura)
- 2026-09-29 17:45 [macd_momentum] ENTRADA ASTER @ 0.63712 (22.43 €, apertura)
- 2026-09-29 17:45 [macd_sin_salida] ENTRADA ASTER @ 0.63712 (22.60 €, apertura)
- 2026-09-29 17:45 [c_banda_atr_tope] ENTRADA ASTER @ 0.63712 (22.90 €, apertura)
- 2026-09-29 17:45 [c_banda_atr_evento] ENTRADA ASTER @ 0.63712 (22.91 €, apertura)
- 2026-09-29 17:45 [macd_momentum_evento] ENTRADA ASTER @ 0.63712 (22.79 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
