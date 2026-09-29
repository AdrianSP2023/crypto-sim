# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 13:36 UTC · vueltas 48 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 921.09 € (-0.34%) | 15 | 21 | 67% | +0.796% | -0.304% | -0.417% | -1.06 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 915.61 € (-0.93%) | 41 | 14 | 32% | +0.208% | -0.841% | -0.986% | -7.95 € |
| rebote_extremo | 924.34 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 916.58 € (-0.83%) | 35 | 7 | 31% | +0.179% | -0.921% | -1.026% | -7.44 € |
| macd_momentum | 908.78 € (-1.67%) | 93 | 14 | 20% | +0.074% | -0.707% | -0.820% | -15.14 € |
| estocastico_rebote | 921.71 € (-0.27%) | 33 | 33 | 73% | +1.001% | -0.035% | -0.167% | -0.26 € |
| ruptura_estricta | 919.03 € (-0.56%) | 21 | 14 | 33% | +0.190% | -0.910% | -1.043% | -4.42 € |
| macd_sin_salida | 915.82 € (-0.91%) | 47 | 20 | 38% | +0.341% | -0.657% | -0.777% | -7.10 € |
| c_banda_atr_tope | 923.41 € (-0.09%) | 3 | 5 | 67% | +0.646% | -0.454% | -0.639% | -0.32 € |
| ruptura_volumen_tope | 922.13 € (-0.23%) | 10 | 5 | 30% | +0.387% | -0.713% | -0.836% | -1.65 € |
| c_banda_atr_regimen | 921.09 € (-0.34%) | 15 | 21 | 67% | +0.796% | -0.304% | -0.417% | -1.06 € |
| macd_momentum_regimen | 908.78 € (-1.67%) | 93 | 14 | 20% | +0.074% | -0.707% | -0.820% | -15.14 € |
| ruptura_volumen_regimen | 915.61 € (-0.93%) | 41 | 14 | 32% | +0.208% | -0.841% | -0.986% | -7.95 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 13:35 | ruptura_volumen_regimen | VIRTUAL | stop-loss | -1.43% | -2.23% | -0.51 |
| 2026-09-29 13:35 | ruptura_volumen_regimen | MON | stop-loss | -1.20% | -2.00% | -0.46 |
| 2026-09-29 13:35 | ruptura_volumen_regimen | DASH | stop-loss | -1.20% | -2.00% | -0.46 |
| 2026-09-29 13:35 | ruptura_volumen_regimen | AAVE | timeout | +0.81% | +0.01% | +0.00 |
| 2026-09-29 13:35 | ruptura_volumen_regimen | NEAR | timeout | -0.17% | -0.97% | -0.23 |
| 2026-09-29 13:35 | macd_momentum_regimen | ADA | momentum perdido | -0.93% | -1.43% | -0.33 |
| 2026-09-29 13:35 | c_banda_atr_regimen | GRT | stop-loss | -2.06% | -3.16% | -0.73 |
| 2026-09-29 13:35 | c_banda_atr_regimen | ATOM | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 13:35 | c_banda_atr_regimen | TAO | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 13:35 | c_banda_atr_regimen | LINK | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 13:35 | c_banda_atr_tope | GRT | stop-loss | -2.06% | -3.16% | -0.73 |
| 2026-09-29 13:35 | macd_sin_salida | UNI | stop-loss | -1.50% | -2.30% | -0.50 |
| 2026-09-29 13:35 | macd_sin_salida | SUI | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-29 13:35 | macd_sin_salida | LINK | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-29 13:35 | ruptura_estricta | ATOM | stop-loss | -2.00% | -3.10% | -0.72 |

## Eventos de la última vuelta

- 2026-09-29 13:35 [c_banda_atr] CIERRE LINK stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 13:35 [macd_sin_salida] CIERRE LINK stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 13:35 [c_banda_atr_regimen] CIERRE LINK stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 13:35 [ruptura_volumen] CIERRE NEAR timeout bruto -0.17% neto -0.97%
- 2026-09-29 13:35 [pullback_tendencia] CIERRE NEAR rotura de tendencia bruto -0.89% neto -1.99%
- 2026-09-29 13:35 [ruptura_volumen_regimen] CIERRE NEAR timeout bruto -0.17% neto -0.97%
- 2026-09-29 13:35 [pullback_tendencia] CIERRE ADA rotura de tendencia bruto -0.93% neto -2.03%
- 2026-09-29 13:35 [macd_momentum] CIERRE ADA momentum perdido bruto -0.93% neto -1.43%
- 2026-09-29 13:35 [macd_momentum_regimen] CIERRE ADA momentum perdido bruto -0.93% neto -1.43%
- 2026-09-29 13:35 [pullback_tendencia] CIERRE SUI rotura de tendencia bruto -0.57% neto -1.67%
- 2026-09-29 13:35 [macd_sin_salida] CIERRE SUI stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 13:30 [pullback_tendencia] ENTRADA LTC @ 60.57 (22.96 €, apertura)
- 2026-09-29 13:35 [pullback_tendencia] CIERRE LTC rotura de tendencia bruto -0.53% neto -1.63%
- 2026-09-29 13:35 [ruptura_volumen] CIERRE AAVE timeout bruto +0.80% neto +0.00%
- 2026-09-29 13:35 [ruptura_volumen_regimen] CIERRE AAVE timeout bruto +0.80% neto +0.00%
- 2026-09-29 13:35 [macd_sin_salida] CIERRE UNI stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 13:35 [c_banda_atr] CIERRE TAO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 13:30 [macd_momentum] ENTRADA TAO @ 275.839 (22.73 €, apertura)
- 2026-09-29 13:35 [c_banda_atr_regimen] CIERRE TAO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 13:30 [macd_momentum_regimen] ENTRADA TAO @ 275.839 (22.73 €, apertura)
- 2026-09-29 13:30 [macd_momentum] ENTRADA XDC @ 0.03214 (22.73 €, apertura)
- 2026-09-29 13:30 [macd_sin_salida] ENTRADA XDC @ 0.03214 (22.93 €, apertura)
- 2026-09-29 13:30 [macd_momentum_regimen] ENTRADA XDC @ 0.03214 (22.73 €, apertura)
- 2026-09-29 13:35 [pullback_tendencia] CIERRE DOT rotura de tendencia bruto -0.87% neto -1.97%
- 2026-09-29 13:35 [ruptura_volumen] CIERRE DASH stop-loss bruto -1.20% neto -2.00%
- 2026-09-29 13:35 [ruptura_volumen_regimen] CIERRE DASH stop-loss bruto -1.20% neto -2.00%
- 2026-09-29 13:30 [ruptura_estricta] ENTRADA ENA @ 0.2271 (23.01 €, apertura)
- 2026-09-29 13:35 [ruptura_volumen] CIERRE MON stop-loss bruto -1.20% neto -2.00%
- 2026-09-29 13:35 [ruptura_volumen_regimen] CIERRE MON stop-loss bruto -1.20% neto -2.00%
- 2026-09-29 13:35 [estocastico_rebote] CIERRE ICP take-profit bruto +1.80% neto +1.00%
- 2026-09-29 13:30 [pullback_tendencia] ENTRADA INJ @ 6.795 (22.94 €, apertura)
- 2026-09-29 13:35 [pullback_tendencia] CIERRE INJ rotura de tendencia bruto -0.79% neto -1.89%
- 2026-09-29 13:35 [c_banda_atr] CIERRE ATOM stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 13:35 [estocastico_rebote] CIERRE ATOM stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 13:35 [ruptura_estricta] CIERRE ATOM stop-loss bruto -2.00% neto -3.10%
- 2026-09-29 13:35 [c_banda_atr_regimen] CIERRE ATOM stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 13:35 [ruptura_volumen] CIERRE VIRTUAL stop-loss bruto -1.42% neto -2.22%
- 2026-09-29 13:35 [ruptura_volumen_regimen] CIERRE VIRTUAL stop-loss bruto -1.42% neto -2.22%
- 2026-09-29 13:30 [macd_momentum] ENTRADA RAY @ 1.699 (22.73 €, apertura)
- 2026-09-29 13:30 [macd_momentum_regimen] ENTRADA RAY @ 1.699 (22.73 €, apertura)
- 2026-09-29 13:35 [pullback_tendencia] CIERRE BNB rotura de tendencia bruto -0.11% neto -1.21%
- 2026-09-29 13:35 [c_banda_atr] CIERRE GRT stop-loss bruto -2.06% neto -3.16%
- 2026-09-29 13:35 [c_banda_atr_tope] CIERRE GRT stop-loss bruto -2.06% neto -3.16%
- 2026-09-29 13:35 [c_banda_atr_regimen] CIERRE GRT stop-loss bruto -2.06% neto -3.16%
- 2026-09-29 13:30 [macd_momentum] ENTRADA ASTER @ 0.64173 (22.73 €, apertura)
- 2026-09-29 13:30 [macd_sin_salida] ENTRADA ASTER @ 0.64173 (22.93 €, apertura)
- 2026-09-29 13:30 [macd_momentum_regimen] ENTRADA ASTER @ 0.64173 (22.73 €, apertura)
- 2026-09-29 13:30 [c_banda_atr] ENTRADA FET @ 0.2076 (23.08 €, apertura)
- 2026-09-29 13:30 [c_banda_atr_tope] ENTRADA FET @ 0.2076 (23.10 €, apertura)
- 2026-09-29 13:30 [c_banda_atr_regimen] ENTRADA FET @ 0.2076 (23.08 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
