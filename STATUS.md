# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 06:51 UTC · vueltas 229 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.92 € (-3.60%) | 134 | 19 | 26% | -0.291% | -0.986% | -1.117% | -30.19 € |
| reversion_bb | 915.24 € (-0.97%) | 35 | 10 | 46% | +0.183% | -0.917% | -1.027% | -7.39 € |
| ruptura_volumen | 885.99 € (-4.14%) | 171 | 7 | 18% | -0.303% | -0.956% | -1.083% | -37.11 € |
| rebote_extremo | 922.91 € (-0.14%) | 8 | 1 | 50% | +0.378% | -0.722% | -0.879% | -1.33 € |
| pullback_tendencia | 902.69 € (-2.33%) | 119 | 0 | 24% | -0.072% | -0.791% | -0.916% | -21.55 € |
| macd_momentum | 874.63 € (-5.37%) | 320 | 3 | 16% | -0.105% | -0.687% | -0.797% | -49.59 € |
| estocastico_rebote | 886.54 € (-4.08%) | 214 | 14 | 34% | -0.129% | -0.751% | -0.883% | -36.59 € |
| ruptura_estricta | 902.46 € (-2.36%) | 71 | 9 | 23% | -0.397% | -1.264% | -1.406% | -20.58 € |
| macd_sin_salida | 886.75 € (-4.06%) | 187 | 22 | 28% | -0.178% | -0.818% | -0.943% | -34.77 € |
| c_banda_atr_tope | 909.37 € (-1.61%) | 40 | 1 | 18% | -0.507% | -1.607% | -1.736% | -14.76 € |
| ruptura_volumen_tope | 908.10 € (-1.75%) | 63 | 1 | 16% | -0.208% | -1.127% | -1.246% | -16.28 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.963% | -38.90 € |
| ruptura_volumen_regimen | 895.81 € (-3.08%) | 121 | 5 | 17% | -0.284% | -0.999% | -1.129% | -27.59 € |
| c_banda_atr_evento | 893.96 € (-3.28%) | 102 | 19 | 23% | -0.404% | -1.163% | -1.294% | -27.14 € |
| macd_momentum_evento | 886.92 € (-4.04%) | 200 | 3 | 13% | -0.189% | -0.821% | -0.927% | -37.29 € |
| ruptura_volumen_evento | 891.44 € (-3.55%) | 112 | 7 | 10% | -0.504% | -1.240% | -1.368% | -31.64 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 06:50 | ruptura_volumen_evento | WLD | timeout | -0.43% | -0.93% | -0.21 |
| 2026-09-30 06:50 | ruptura_volumen_evento | CRV | stop-loss | -1.36% | -1.86% | -0.42 |
| 2026-09-30 06:50 | ruptura_volumen_evento | AAVE | timeout | -0.85% | -1.35% | -0.30 |
| 2026-09-30 06:50 | ruptura_volumen_evento | QNT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 06:50 | c_banda_atr_evento | FIL | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:50 | c_banda_atr_evento | TRX | timeout | +0.47% | -0.04% | -0.01 |
| 2026-09-30 06:50 | c_banda_atr_evento | ADA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:50 | ruptura_volumen_regimen | CRV | stop-loss | -1.36% | -1.86% | -0.42 |
| 2026-09-30 06:50 | ruptura_volumen_tope | AAVE | timeout | -0.85% | -1.35% | -0.31 |
| 2026-09-30 06:50 | ruptura_volumen_tope | QNT | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 06:50 | macd_sin_salida | UNI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:50 | macd_sin_salida | AVAX | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:50 | macd_sin_salida | ADA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:50 | macd_sin_salida | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:50 | pullback_tendencia | SUI | rotura de tendencia | -0.20% | -0.70% | -0.16 |

## Eventos de la última vuelta

- 2026-09-30 06:50 [ruptura_volumen] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 06:50 [pullback_tendencia] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:50 [ruptura_volumen_tope] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 06:50 [ruptura_volumen_evento] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 06:45 [macd_momentum] ENTRADA HBAR @ 0.09248 (21.87 €, apertura)
- 2026-09-30 06:45 [macd_sin_salida] ENTRADA HBAR @ 0.09248 (22.28 €, apertura)
- 2026-09-30 06:45 [macd_momentum_evento] ENTRADA HBAR @ 0.09248 (22.17 €, apertura)
- 2026-09-30 06:50 [macd_sin_salida] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:50 [c_banda_atr] CIERRE ADA stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:50 [macd_sin_salida] CIERRE ADA stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:50 [c_banda_atr_evento] CIERRE ADA stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:50 [pullback_tendencia] CIERRE SUI rotura de tendencia bruto -0.20% neto -0.70%
- 2026-09-30 06:50 [macd_sin_salida] CIERRE AVAX stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:50 [ruptura_volumen] CIERRE AAVE timeout bruto -0.85% neto -1.35%
- 2026-09-30 06:50 [ruptura_volumen_tope] CIERRE AAVE timeout bruto -0.85% neto -1.35%
- 2026-09-30 06:50 [ruptura_volumen_evento] CIERRE AAVE timeout bruto -0.85% neto -1.35%
- 2026-09-30 06:50 [macd_sin_salida] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:45 [ruptura_volumen] ENTRADA XDC @ 0.0297 (22.19 €, apertura)
- 2026-09-30 06:45 [macd_momentum] ENTRADA XDC @ 0.0297 (21.87 €, apertura)
- 2026-09-30 06:45 [ruptura_volumen_tope] ENTRADA XDC @ 0.0297 (22.70 €, apertura)
- 2026-09-30 06:45 [macd_momentum_evento] ENTRADA XDC @ 0.0297 (22.17 €, apertura)
- 2026-09-30 06:45 [ruptura_volumen_evento] ENTRADA XDC @ 0.0297 (22.33 €, apertura)
- 2026-09-30 06:45 [estocastico_rebote] ENTRADA DOT @ 1.0518 (22.19 €, apertura)
- 2026-09-30 06:50 [ruptura_volumen] CIERRE CRV stop-loss bruto -1.36% neto -1.86%
- 2026-09-30 06:50 [ruptura_volumen_regimen] CIERRE CRV stop-loss bruto -1.36% neto -1.86%
- 2026-09-30 06:50 [ruptura_volumen_evento] CIERRE CRV stop-loss bruto -1.36% neto -1.86%
- 2026-09-30 06:45 [estocastico_rebote] ENTRADA ICP @ 2.983 (22.19 €, apertura)
- 2026-09-30 06:50 [c_banda_atr] CIERRE TRX timeout bruto +0.46% neto -0.04%
- 2026-09-30 06:50 [c_banda_atr_evento] CIERRE TRX timeout bruto +0.46% neto -0.04%
- 2026-09-30 06:50 [ruptura_volumen] CIERRE WLD timeout bruto -0.43% neto -0.93%
- 2026-09-30 06:45 [estocastico_rebote] ENTRADA WLD @ 0.4371 (22.19 €, apertura)
- 2026-09-30 06:50 [ruptura_volumen_evento] CIERRE WLD timeout bruto -0.43% neto -0.93%
- 2026-09-30 06:45 [estocastico_rebote] ENTRADA PEPE @ 3.777e-06 (22.19 €, apertura)
- 2026-09-30 06:50 [c_banda_atr] CIERRE FIL stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:50 [c_banda_atr_evento] CIERRE FIL stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:45 [estocastico_rebote] ENTRADA SHIB @ 5.071e-06 (22.19 €, apertura)
- 2026-09-30 06:45 [estocastico_rebote] ENTRADA ASTER @ 0.65847 (22.19 €, apertura)
- 2026-09-30 06:45 [estocastico_rebote] ENTRADA SPX @ 0.3694 (22.19 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
