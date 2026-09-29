# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 14:01 UTC · vueltas 53 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 920.92 € (-0.36%) | 21 | 18 | 52% | +0.442% | -0.658% | -0.794% | -3.19 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 915.49 € (-0.95%) | 50 | 8 | 30% | +0.166% | -0.838% | -0.971% | -9.66 € |
| rebote_extremo | 924.34 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 916.25 € (-0.86%) | 39 | 7 | 33% | +0.234% | -0.866% | -0.975% | -7.79 € |
| macd_momentum | 908.22 € (-1.73%) | 107 | 6 | 21% | +0.077% | -0.667% | -0.780% | -16.42 € |
| estocastico_rebote | 922.62 € (-0.17%) | 47 | 24 | 60% | +0.821% | -0.139% | -0.254% | -1.50 € |
| ruptura_estricta | 921.44 € (-0.30%) | 23 | 13 | 39% | +0.434% | -0.666% | -0.800% | -3.54 € |
| macd_sin_salida | 917.14 € (-0.77%) | 54 | 18 | 41% | +0.373% | -0.571% | -0.695% | -7.09 € |
| c_banda_atr_tope | 922.33 € (-0.21%) | 8 | 5 | 38% | +0.019% | -1.081% | -1.255% | -2.00 € |
| ruptura_volumen_tope | 922.36 € (-0.20%) | 13 | 5 | 23% | +0.215% | -0.885% | -1.016% | -2.66 € |
| c_banda_atr_regimen | 920.92 € (-0.36%) | 21 | 18 | 52% | +0.442% | -0.658% | -0.794% | -3.19 € |
| macd_momentum_regimen | 908.22 € (-1.73%) | 107 | 6 | 21% | +0.077% | -0.667% | -0.780% | -16.42 € |
| ruptura_volumen_regimen | 915.49 € (-0.95%) | 50 | 8 | 30% | +0.166% | -0.838% | -0.971% | -9.66 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 14:00 | macd_momentum_regimen | ENA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:00 | macd_sin_salida | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:00 | macd_sin_salida | ENA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:00 | macd_sin_salida | ALGO | timeout | -0.85% | -1.65% | -0.38 |
| 2026-09-29 14:00 | estocastico_rebote | SPX | timeout | +1.37% | +0.57% | +0.13 |
| 2026-09-29 14:00 | estocastico_rebote | BNB | timeout | +0.07% | -0.73% | -0.17 |
| 2026-09-29 14:00 | estocastico_rebote | ONDO | timeout | -0.57% | -1.37% | -0.32 |
| 2026-09-29 14:00 | estocastico_rebote | ETH | timeout | +0.52% | -0.28% | -0.06 |
| 2026-09-29 14:00 | estocastico_rebote | LINK | timeout | -1.17% | -1.97% | -0.46 |
| 2026-09-29 14:00 | macd_momentum | ENA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:00 | pullback_tendencia | QNT | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 13:55 | ruptura_volumen_regimen | SPX | timeout | +0.08% | -0.72% | -0.17 |
| 2026-09-29 13:55 | ruptura_volumen_regimen | SOL | timeout | +1.20% | +0.40% | +0.09 |
| 2026-09-29 13:55 | ruptura_volumen_regimen | ETH | timeout | +0.07% | -0.73% | -0.17 |
| 2026-09-29 13:55 | macd_momentum_regimen | USELESS | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-09-29 14:00 [estocastico_rebote] CIERRE LINK timeout bruto -1.17% neto -1.97%
- 2026-09-29 14:00 [estocastico_rebote] CIERRE ETH timeout bruto +0.52% neto -0.28%
- 2026-09-29 13:55 [macd_sin_salida] ENTRADA SOL @ 107.11 (22.92 €, apertura)
- 2026-09-29 14:00 [pullback_tendencia] CIERRE QNT stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 14:00 [macd_sin_salida] CIERRE ALGO timeout bruto -0.85% neto -1.65%
- 2026-09-29 13:55 [c_banda_atr] ENTRADA TAO @ 278.447 (23.03 €, apertura)
- 2026-09-29 13:55 [macd_momentum] ENTRADA TAO @ 278.447 (22.69 €, apertura)
- 2026-09-29 13:55 [c_banda_atr_tope] ENTRADA TAO @ 278.447 (23.06 €, apertura)
- 2026-09-29 13:55 [c_banda_atr_regimen] ENTRADA TAO @ 278.447 (23.03 €, apertura)
- 2026-09-29 13:55 [macd_momentum_regimen] ENTRADA TAO @ 278.447 (22.69 €, apertura)
- 2026-09-29 14:00 [estocastico_rebote] CIERRE ONDO timeout bruto -0.57% neto -1.37%
- 2026-09-29 14:00 [macd_momentum] CIERRE ENA take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:00 [macd_sin_salida] CIERRE ENA take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:00 [macd_momentum_regimen] CIERRE ENA take-profit bruto +2.00% neto +1.50%
- 2026-09-29 13:55 [ruptura_volumen] ENTRADA INJ @ 6.848 (22.86 €, apertura)
- 2026-09-29 13:55 [ruptura_volumen_tope] ENTRADA INJ @ 6.848 (23.04 €, apertura)
- 2026-09-29 13:55 [ruptura_volumen_regimen] ENTRADA INJ @ 6.848 (22.86 €, apertura)
- 2026-09-29 13:55 [estocastico_rebote] ENTRADA TRX @ 0.295358 (23.07 €, apertura)
- 2026-09-29 13:55 [macd_momentum] ENTRADA ZRO @ 1.472 (22.70 €, apertura)
- 2026-09-29 14:00 [macd_sin_salida] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-29 13:55 [macd_momentum_regimen] ENTRADA ZRO @ 1.472 (22.70 €, apertura)
- 2026-09-29 13:55 [c_banda_atr_tope] ENTRADA VIRTUAL @ 0.7273 (23.06 €, apertura)
- 2026-09-29 13:55 [c_banda_atr_tope] ENTRADA RAY @ 1.697 (23.06 €, apertura)
- 2026-09-29 13:55 [macd_momentum] ENTRADA OP @ 0.1184 (22.70 €, apertura)
- 2026-09-29 13:55 [macd_sin_salida] ENTRADA OP @ 0.1184 (22.93 €, apertura)
- 2026-09-29 13:55 [macd_momentum_regimen] ENTRADA OP @ 0.1184 (22.70 €, apertura)
- 2026-09-29 14:00 [estocastico_rebote] CIERRE BNB timeout bruto +0.07% neto -0.73%
- 2026-09-29 14:00 [estocastico_rebote] CIERRE SPX timeout bruto +1.37% neto +0.57%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
