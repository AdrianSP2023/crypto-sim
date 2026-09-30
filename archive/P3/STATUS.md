# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 10:11 UTC · vueltas 208 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 895.43 € (-3.12%) | 161 | 24 | 29% | -0.161% | -0.823% | -0.951% | -30.28 € |
| reversion_bb | 915.20 € (-0.98%) | 43 | 3 | 42% | +0.124% | -0.962% | -1.072% | -9.52 € |
| ruptura_volumen | 886.01 € (-4.14%) | 197 | 24 | 20% | -0.241% | -0.873% | -1.004% | -39.04 € |
| rebote_extremo | 923.34 € (-0.10%) | 10 | 0 | 60% | +0.710% | -0.389% | -0.540% | -0.90 € |
| pullback_tendencia | 901.82 € (-2.43%) | 124 | 6 | 23% | -0.093% | -0.804% | -0.930% | -22.80 € |
| macd_momentum | 874.40 € (-5.39%) | 362 | 11 | 17% | -0.064% | -0.636% | -0.747% | -51.88 € |
| estocastico_rebote | 888.10 € (-3.91%) | 235 | 7 | 37% | -0.069% | -0.680% | -0.813% | -36.41 € |
| ruptura_estricta | 902.45 € (-2.36%) | 81 | 18 | 22% | -0.396% | -1.218% | -1.368% | -22.60 € |
| macd_sin_salida | 889.61 € (-3.75%) | 218 | 29 | 29% | -0.117% | -0.736% | -0.857% | -36.49 € |
| c_banda_atr_tope | 909.96 € (-1.54%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.25 € (-1.73%) | 70 | 5 | 20% | -0.118% | -0.995% | -1.117% | -15.97 € |
| c_banda_atr_regimen | 900.76 € (-2.54%) | 78 | 6 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 884.14 € (-4.34%) | 213 | 3 | 14% | -0.216% | -0.838% | -0.950% | -40.49 € |
| ruptura_volumen_regimen | 893.99 € (-3.27%) | 136 | 21 | 18% | -0.285% | -0.977% | -1.107% | -30.28 € |
| c_banda_atr_evento | 898.48 € (-2.79%) | 129 | 24 | 26% | -0.218% | -0.922% | -1.051% | -27.23 € |
| macd_momentum_evento | 886.69 € (-4.06%) | 242 | 11 | 15% | -0.113% | -0.722% | -0.830% | -39.60 € |
| ruptura_volumen_evento | 891.47 € (-3.55%) | 138 | 24 | 15% | -0.378% | -1.069% | -1.201% | -33.59 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 10:10 | ruptura_volumen_evento | NIGHT | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 10:10 | ruptura_volumen_evento | CRV | stop-loss | -1.45% | -1.95% | -0.43 |
| 2026-09-30 10:10 | macd_momentum_evento | SHIB | momentum perdido | +0.77% | +0.27% | +0.06 |
| 2026-09-30 10:10 | macd_momentum_evento | FIL | momentum perdido | +0.96% | +0.46% | +0.10 |
| 2026-09-30 10:10 | macd_momentum_evento | TRX | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-09-30 10:10 | macd_momentum_evento | HYPE | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-09-30 10:10 | macd_momentum_evento | UNI | momentum perdido | +0.13% | -0.37% | -0.08 |
| 2026-09-30 10:10 | macd_momentum_evento | ZEC | momentum perdido | +0.02% | -0.48% | -0.11 |
| 2026-09-30 10:10 | ruptura_volumen_regimen | NIGHT | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 10:10 | ruptura_volumen_regimen | CRV | stop-loss | -1.45% | -1.95% | -0.43 |
| 2026-09-30 10:10 | macd_momentum_regimen | TRX | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-09-30 10:10 | macd_momentum_regimen | UNI | momentum perdido | +0.13% | -0.37% | -0.08 |
| 2026-09-30 10:10 | macd_momentum_regimen | ZEC | momentum perdido | +0.02% | -0.48% | -0.11 |
| 2026-09-30 10:10 | macd_sin_salida | SPX | timeout | +0.81% | +0.30% | +0.07 |
| 2026-09-30 10:10 | estocastico_rebote | QNT | take-profit | +1.80% | +1.30% | +0.29 |

## Eventos de la última vuelta

- 2026-09-30 10:10 [estocastico_rebote] CIERRE QNT take-profit bruto +1.80% neto +1.30%
- 2026-09-30 10:10 [macd_momentum] CIERRE ZEC momentum perdido bruto +0.02% neto -0.48%
- 2026-09-30 10:10 [macd_momentum_regimen] CIERRE ZEC momentum perdido bruto +0.02% neto -0.48%
- 2026-09-30 10:10 [macd_momentum_evento] CIERRE ZEC momentum perdido bruto +0.02% neto -0.48%
- 2026-09-30 10:10 [macd_momentum] CIERRE UNI momentum perdido bruto +0.13% neto -0.37%
- 2026-09-30 10:10 [macd_momentum_regimen] CIERRE UNI momentum perdido bruto +0.13% neto -0.37%
- 2026-09-30 10:10 [macd_momentum_evento] CIERRE UNI momentum perdido bruto +0.13% neto -0.37%
- 2026-09-30 10:10 [macd_momentum] CIERRE HYPE momentum perdido bruto -0.13% neto -0.63%
- 2026-09-30 10:10 [macd_momentum_evento] CIERRE HYPE momentum perdido bruto -0.13% neto -0.63%
- 2026-09-30 10:10 [ruptura_volumen] CIERRE CRV stop-loss bruto -1.44% neto -1.94%
- 2026-09-30 10:10 [ruptura_volumen_regimen] CIERRE CRV stop-loss bruto -1.44% neto -1.94%
- 2026-09-30 10:10 [ruptura_volumen_evento] CIERRE CRV stop-loss bruto -1.44% neto -1.94%
- 2026-09-30 10:10 [macd_momentum] CIERRE TRX momentum perdido bruto +0.04% neto -0.46%
- 2026-09-30 10:10 [macd_momentum_regimen] CIERRE TRX momentum perdido bruto +0.04% neto -0.46%
- 2026-09-30 10:10 [macd_momentum_evento] CIERRE TRX momentum perdido bruto +0.04% neto -0.46%
- 2026-09-30 10:05 [estocastico_rebote] ENTRADA ZRO @ 1.551 (22.20 €, apertura)
- 2026-09-30 10:10 [ruptura_volumen] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%
- 2026-09-30 10:10 [ruptura_volumen_regimen] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%
- 2026-09-30 10:10 [ruptura_volumen_evento] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%
- 2026-09-30 10:10 [macd_momentum] CIERRE FIL momentum perdido bruto +0.96% neto +0.46%
- 2026-09-30 10:10 [macd_momentum_evento] CIERRE FIL momentum perdido bruto +0.96% neto +0.46%
- 2026-09-30 10:05 [pullback_tendencia] ENTRADA SHIB @ 5.117e-06 (22.54 €, apertura)
- 2026-09-30 10:10 [macd_momentum] CIERRE SHIB momentum perdido bruto +0.77% neto +0.27%
- 2026-09-30 10:10 [macd_momentum_evento] CIERRE SHIB momentum perdido bruto +0.77% neto +0.27%
- 2026-09-30 10:10 [macd_sin_salida] CIERRE SPX timeout bruto +0.81% neto +0.31%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
