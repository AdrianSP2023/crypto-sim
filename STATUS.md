# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 15:02 UTC · vueltas 64 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 917.77 € (-0.70%) | 35 | 14 | 46% | +0.303% | -0.797% | -0.949% | -6.44 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 914.47 € (-1.06%) | 58 | 11 | 31% | +0.165% | -0.785% | -0.913% | -10.50 € |
| rebote_extremo | 924.18 € (-0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 914.32 € (-1.07%) | 50 | 11 | 32% | +0.139% | -0.871% | -0.982% | -10.03 € |
| macd_momentum | 906.76 € (-1.89%) | 125 | 22 | 23% | +0.095% | -0.614% | -0.732% | -17.65 € |
| estocastico_rebote | 918.30 € (-0.64%) | 62 | 31 | 52% | +0.513% | -0.379% | -0.516% | -5.41 € |
| ruptura_estricta | 918.41 € (-0.63%) | 32 | 9 | 34% | +0.108% | -0.992% | -1.115% | -7.33 € |
| macd_sin_salida | 916.10 € (-0.88%) | 70 | 23 | 41% | +0.389% | -0.484% | -0.613% | -7.79 € |
| c_banda_atr_tope | 919.92 € (-0.47%) | 12 | 4 | 25% | -0.491% | -1.591% | -1.772% | -4.41 € |
| ruptura_volumen_tope | 922.02 € (-0.24%) | 15 | 5 | 20% | +0.300% | -0.800% | -0.920% | -2.77 € |
| c_banda_atr_regimen | 917.77 € (-0.70%) | 35 | 14 | 46% | +0.303% | -0.797% | -0.949% | -6.44 € |
| macd_momentum_regimen | 906.76 € (-1.89%) | 125 | 22 | 23% | +0.095% | -0.614% | -0.732% | -17.65 € |
| ruptura_volumen_regimen | 914.47 € (-1.06%) | 58 | 11 | 31% | +0.165% | -0.785% | -0.913% | -10.50 € |
| c_banda_atr_evento | 923.83 € (-0.04%) | 6 | 11 | 67% | +0.888% | -0.212% | -0.426% | -0.29 € |
| macd_momentum_evento | 924.94 € (+0.08%) | 5 | 22 | 80% | +1.529% | +0.429% | +0.260% | +0.50 € |
| ruptura_volumen_evento | 925.00 € (+0.08%) | 1 | 9 | 100% | +2.500% | +1.400% | +1.245% | +0.32 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 15:00 | ruptura_volumen_evento | FIL | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 15:00 | macd_momentum_evento | FIL | take-profit | +2.41% | +1.31% | +0.30 |
| 2026-09-29 15:00 | c_banda_atr_evento | FIL | take-profit | +2.41% | +1.31% | +0.30 |
| 2026-09-29 15:00 | ruptura_volumen_regimen | FIL | take-profit | +2.50% | +2.00% | +0.46 |
| 2026-09-29 15:00 | macd_momentum_regimen | FIL | take-profit | +2.41% | +1.91% | +0.43 |
| 2026-09-29 15:00 | estocastico_rebote | FET | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 15:00 | estocastico_rebote | QNT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 15:00 | macd_momentum | FIL | take-profit | +2.41% | +1.91% | +0.43 |
| 2026-09-29 15:00 | pullback_tendencia | XLM | rotura de tendencia | -0.38% | -0.88% | -0.20 |
| 2026-09-29 15:00 | ruptura_volumen | FIL | take-profit | +2.50% | +2.00% | +0.46 |
| 2026-09-29 14:55 | macd_momentum_evento | AVAX | momentum perdido | -0.76% | -1.86% | -0.43 |
| 2026-09-29 14:55 | c_banda_atr_evento | ENA | stop-loss | -1.53% | -2.63% | -0.61 |
| 2026-09-29 14:55 | ruptura_volumen_regimen | TRUMP | timeout | +1.32% | +0.82% | +0.19 |
| 2026-09-29 14:55 | macd_momentum_regimen | AVAX | momentum perdido | -0.76% | -1.26% | -0.29 |
| 2026-09-29 14:55 | c_banda_atr_regimen | ASTER | timeout | +0.71% | -0.39% | -0.09 |

## Eventos de la última vuelta

- 2026-09-29 14:55 [estocastico_rebote] ENTRADA QNT @ 213.4 (22.99 €, apertura)
- 2026-09-29 15:00 [estocastico_rebote] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 14:55 [pullback_tendencia] ENTRADA XLM @ 0.204192 (22.86 €, apertura)
- 2026-09-29 15:00 [pullback_tendencia] CIERRE XLM rotura de tendencia bruto -0.37% neto -0.87%
- 2026-09-29 14:55 [pullback_tendencia] ENTRADA ICP @ 3.019 (22.86 €, apertura)
- 2026-09-29 14:55 [pullback_tendencia] ENTRADA RENDER @ 1.73 (22.86 €, apertura)
- 2026-09-29 15:00 [ruptura_volumen] CIERRE FIL take-profit bruto +2.50% neto +2.00%
- 2026-09-29 15:00 [macd_momentum] CIERRE FIL take-profit bruto +2.41% neto +1.91%
- 2026-09-29 15:00 [macd_momentum_regimen] CIERRE FIL take-profit bruto +2.41% neto +1.91%
- 2026-09-29 15:00 [ruptura_volumen_regimen] CIERRE FIL take-profit bruto +2.50% neto +2.00%
- 2026-09-29 15:00 [c_banda_atr_evento] CIERRE FIL take-profit bruto +2.41% neto +1.31%
- 2026-09-29 15:00 [macd_momentum_evento] CIERRE FIL take-profit bruto +2.41% neto +1.31%
- 2026-09-29 15:00 [ruptura_volumen_evento] CIERRE FIL take-profit bruto +2.50% neto +1.40%
- 2026-09-29 15:00 [estocastico_rebote] CIERRE FET stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
