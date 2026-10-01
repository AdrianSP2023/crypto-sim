# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 18:37 UTC · vueltas 284 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.81 € (-3.51%) | 235 | 15 | 36% | -0.020% | -0.631% | -0.754% | -33.78 € |
| reversion_bb | 916.85 € (-0.80%) | 45 | 3 | 49% | +0.297% | -0.763% | -0.860% | -7.91 € |
| ruptura_volumen | 879.11 € (-4.88%) | 263 | 22 | 25% | -0.169% | -0.768% | -0.878% | -45.73 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 893.11 € (-3.37%) | 161 | 7 | 16% | -0.199% | -0.863% | -0.960% | -31.62 € |
| macd_momentum | 873.90 € (-5.45%) | 422 | 9 | 22% | +0.019% | -0.543% | -0.649% | -51.62 € |
| estocastico_rebote | 877.87 € (-5.02%) | 289 | 4 | 31% | -0.125% | -0.716% | -0.827% | -46.80 € |
| ruptura_estricta | 887.49 € (-3.98%) | 144 | 19 | 25% | -0.476% | -1.159% | -1.281% | -38.07 € |
| macd_sin_salida | 885.39 € (-4.20%) | 292 | 21 | 37% | -0.020% | -0.609% | -0.724% | -40.51 € |
| c_banda_atr_tope | 912.32 € (-1.29%) | 55 | 3 | 31% | +0.014% | -0.966% | -1.084% | -12.21 € |
| ruptura_volumen_tope | 908.85 € (-1.67%) | 89 | 4 | 29% | +0.038% | -0.759% | -0.873% | -15.49 € |
| c_banda_atr_regimen | 903.04 € (-2.29%) | 112 | 10 | 35% | -0.105% | -0.838% | -0.978% | -21.56 € |
| macd_momentum_regimen | 894.20 € (-3.25%) | 225 | 6 | 22% | +0.016% | -0.600% | -0.712% | -30.79 € |
| ruptura_volumen_regimen | 882.64 € (-4.50%) | 196 | 23 | 20% | -0.315% | -0.948% | -1.066% | -42.16 € |
| c_banda_atr_evento | 897.75 € (-2.87%) | 202 | 15 | 37% | +0.028% | -0.603% | -0.720% | -27.85 € |
| macd_momentum_evento | 878.74 € (-4.92%) | 375 | 9 | 20% | +0.017% | -0.553% | -0.654% | -46.79 € |
| ruptura_volumen_evento | 891.62 € (-3.53%) | 213 | 22 | 27% | -0.061% | -0.685% | -0.785% | -33.21 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 18:35 | ruptura_volumen_evento | RENDER | timeout | +0.76% | +0.26% | +0.06 |
| 2026-10-01 18:35 | ruptura_volumen_evento | CRV | timeout | +0.33% | -0.17% | -0.04 |
| 2026-10-01 18:35 | ruptura_volumen_evento | SOL | timeout | +0.72% | +0.22% | +0.05 |
| 2026-10-01 18:35 | macd_momentum_evento | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 18:35 | macd_momentum_evento | DASH | momentum perdido | +0.30% | -0.20% | -0.04 |
| 2026-10-01 18:35 | macd_momentum_evento | ASTER | momentum perdido | +0.10% | -0.40% | -0.09 |
| 2026-10-01 18:35 | macd_momentum_evento | FIL | momentum perdido | +1.11% | +0.61% | +0.13 |
| 2026-10-01 18:35 | macd_momentum_evento | MINA | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 18:35 | c_banda_atr_evento | MINA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 18:35 | ruptura_volumen_regimen | RENDER | timeout | +0.76% | +0.26% | +0.06 |
| 2026-10-01 18:35 | ruptura_volumen_regimen | CRV | timeout | +0.33% | -0.17% | -0.04 |
| 2026-10-01 18:35 | ruptura_volumen_regimen | SOL | timeout | +0.72% | +0.22% | +0.05 |
| 2026-10-01 18:35 | macd_momentum_regimen | SKY | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 18:35 | macd_momentum_regimen | DASH | momentum perdido | +0.30% | -0.20% | -0.04 |
| 2026-10-01 18:35 | macd_momentum_regimen | ASTER | momentum perdido | +0.10% | -0.40% | -0.09 |

## Eventos de la última vuelta

- 2026-10-01 18:35 [ruptura_volumen] CIERRE SOL timeout bruto +0.72% neto +0.22%
- 2026-10-01 18:35 [ruptura_volumen_regimen] CIERRE SOL timeout bruto +0.72% neto +0.22%
- 2026-10-01 18:35 [ruptura_volumen_evento] CIERRE SOL timeout bruto +0.72% neto +0.22%
- 2026-10-01 18:30 [pullback_tendencia] ENTRADA SUI @ 1.0483 (22.32 €, apertura)
- 2026-10-01 18:35 [pullback_tendencia] CIERRE UNI rotura de tendencia bruto -0.49% neto -0.99%
- 2026-10-01 18:35 [ruptura_volumen] CIERRE CRV timeout bruto +0.33% neto -0.17%
- 2026-10-01 18:35 [ruptura_volumen_tope] CIERRE CRV timeout bruto +0.33% neto -0.17%
- 2026-10-01 18:35 [ruptura_volumen_regimen] CIERRE CRV timeout bruto +0.33% neto -0.17%
- 2026-10-01 18:35 [ruptura_volumen_evento] CIERRE CRV timeout bruto +0.33% neto -0.17%
- 2026-10-01 18:35 [ruptura_volumen] CIERRE RENDER timeout bruto +0.76% neto +0.26%
- 2026-10-01 18:35 [ruptura_volumen_regimen] CIERRE RENDER timeout bruto +0.76% neto +0.26%
- 2026-10-01 18:35 [ruptura_volumen_evento] CIERRE RENDER timeout bruto +0.76% neto +0.26%
- 2026-10-01 18:35 [c_banda_atr] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 18:35 [macd_momentum] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 18:35 [macd_sin_salida] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 18:35 [c_banda_atr_tope] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 18:35 [c_banda_atr_regimen] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 18:35 [macd_momentum_regimen] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 18:35 [c_banda_atr_evento] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 18:35 [macd_momentum_evento] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 18:35 [macd_momentum] CIERRE FIL momentum perdido bruto +1.11% neto +0.61%
- 2026-10-01 18:35 [macd_momentum_evento] CIERRE FIL momentum perdido bruto +1.11% neto +0.61%
- 2026-10-01 18:35 [macd_momentum] CIERRE ASTER momentum perdido bruto +0.10% neto -0.40%
- 2026-10-01 18:35 [macd_momentum_regimen] CIERRE ASTER momentum perdido bruto +0.10% neto -0.40%
- 2026-10-01 18:35 [macd_momentum_evento] CIERRE ASTER momentum perdido bruto +0.10% neto -0.40%
- 2026-10-01 18:35 [macd_momentum] CIERRE DASH momentum perdido bruto +0.31% neto -0.19%
- 2026-10-01 18:35 [macd_momentum_regimen] CIERRE DASH momentum perdido bruto +0.31% neto -0.19%
- 2026-10-01 18:35 [macd_momentum_evento] CIERRE DASH momentum perdido bruto +0.31% neto -0.19%
- 2026-10-01 18:35 [macd_momentum] CIERRE SKY take-profit bruto +2.00% neto +1.50%
- 2026-10-01 18:35 [macd_sin_salida] CIERRE SKY take-profit bruto +2.00% neto +1.50%
- 2026-10-01 18:35 [macd_momentum_regimen] CIERRE SKY take-profit bruto +2.00% neto +1.50%
- 2026-10-01 18:35 [macd_momentum_evento] CIERRE SKY take-profit bruto +2.00% neto +1.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
