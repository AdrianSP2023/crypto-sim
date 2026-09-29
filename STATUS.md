# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 15:12 UTC · vueltas 66 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 913.96 € (-1.11%) | 39 | 11 | 41% | +0.118% | -0.967% | -1.110% | -8.70 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 911.56 € (-1.37%) | 65 | 4 | 29% | +0.050% | -0.851% | -0.987% | -12.73 € |
| rebote_extremo | 924.06 € (-0.02%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 911.90 € (-1.33%) | 57 | 7 | 28% | +0.031% | -0.922% | -1.033% | -12.10 € |
| macd_momentum | 901.26 € (-2.49%) | 137 | 10 | 21% | -0.008% | -0.698% | -0.815% | -21.93 € |
| estocastico_rebote | 912.08 € (-1.32%) | 70 | 23 | 46% | +0.282% | -0.578% | -0.715% | -9.34 € |
| ruptura_estricta | 917.08 € (-0.77%) | 32 | 9 | 34% | +0.108% | -0.992% | -1.115% | -7.33 € |
| macd_sin_salida | 910.85 € (-1.45%) | 77 | 16 | 38% | +0.215% | -0.624% | -0.752% | -11.04 € |
| c_banda_atr_tope | 918.03 € (-0.67%) | 14 | 3 | 21% | -0.635% | -1.735% | -1.906% | -5.60 € |
| ruptura_volumen_tope | 920.88 € (-0.36%) | 18 | 2 | 22% | +0.248% | -0.852% | -0.988% | -3.54 € |
| c_banda_atr_regimen | 913.96 € (-1.11%) | 39 | 11 | 41% | +0.118% | -0.967% | -1.110% | -8.70 € |
| macd_momentum_regimen | 901.26 € (-2.49%) | 137 | 10 | 21% | -0.008% | -0.698% | -0.815% | -21.93 € |
| ruptura_volumen_regimen | 911.56 € (-1.37%) | 65 | 4 | 29% | +0.050% | -0.851% | -0.987% | -12.73 € |
| c_banda_atr_evento | 920.54 € (-0.40%) | 9 | 9 | 44% | +0.012% | -1.088% | -1.298% | -2.26 € |
| macd_momentum_evento | 917.67 € (-0.71%) | 17 | 10 | 24% | -0.312% | -1.412% | -1.531% | -5.55 € |
| ruptura_volumen_evento | 921.55 € (-0.29%) | 7 | 3 | 29% | -0.366% | -1.466% | -1.659% | -2.37 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 15:10 | ruptura_volumen_evento | ASTER | stop-loss | -1.28% | -2.38% | -0.55 |
| 2026-09-29 15:10 | ruptura_volumen_evento | OP | stop-loss | -1.34% | -2.44% | -0.56 |
| 2026-09-29 15:10 | ruptura_volumen_evento | RAY | stop-loss | -2.22% | -3.32% | -0.77 |
| 2026-09-29 15:10 | ruptura_volumen_evento | CRV | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 15:10 | macd_momentum_evento | ASTER | momentum perdido | -1.08% | -2.18% | -0.50 |
| 2026-09-29 15:10 | macd_momentum_evento | BNB | momentum perdido | -0.51% | -1.61% | -0.37 |
| 2026-09-29 15:10 | macd_momentum_evento | SHIB | momentum perdido | -0.35% | -1.45% | -0.34 |
| 2026-09-29 15:10 | macd_momentum_evento | RAY | stop-loss | -2.22% | -3.32% | -0.77 |
| 2026-09-29 15:10 | macd_momentum_evento | RENDER | momentum perdido | -0.87% | -1.97% | -0.46 |
| 2026-09-29 15:10 | macd_momentum_evento | MON | stop-loss | -1.65% | -2.75% | -0.64 |
| 2026-09-29 15:10 | macd_momentum_evento | JUP | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 15:10 | macd_momentum_evento | DASH | momentum perdido | -0.86% | -1.96% | -0.45 |
| 2026-09-29 15:10 | macd_momentum_evento | DOGE | momentum perdido | -1.06% | -2.16% | -0.50 |
| 2026-09-29 15:10 | c_banda_atr_evento | RAY | stop-loss | -2.22% | -3.32% | -0.77 |
| 2026-09-29 15:10 | c_banda_atr_evento | JUP | stop-loss | -1.50% | -2.60% | -0.60 |

## Eventos de la última vuelta

- 2026-09-29 15:10 [macd_sin_salida] CIERRE SOL stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:05 [pullback_tendencia] ENTRADA NEAR @ 4.3818 (22.82 €, apertura)
- 2026-09-29 15:10 [c_banda_atr] CIERRE ADA stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:10 [c_banda_atr_regimen] CIERRE ADA stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:10 [c_banda_atr] CIERRE LTC stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:10 [c_banda_atr_regimen] CIERRE LTC stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:10 [estocastico_rebote] CIERRE UNI stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 15:10 [c_banda_atr] CIERRE ALGO stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 15:10 [c_banda_atr_tope] CIERRE ALGO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:10 [c_banda_atr_regimen] CIERRE ALGO stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 15:10 [c_banda_atr_evento] CIERRE ALGO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:10 [estocastico_rebote] CIERRE ARB stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:10 [macd_momentum] CIERRE DOGE momentum perdido bruto -1.06% neto -1.56%
- 2026-09-29 15:10 [macd_momentum_regimen] CIERRE DOGE momentum perdido bruto -1.06% neto -1.56%
- 2026-09-29 15:10 [macd_momentum_evento] CIERRE DOGE momentum perdido bruto -1.06% neto -2.16%
- 2026-09-29 15:05 [pullback_tendencia] ENTRADA DOT @ 1.0666 (22.82 €, apertura)
- 2026-09-29 15:10 [pullback_tendencia] CIERRE DOT rotura de tendencia bruto -0.08% neto -0.58%
- 2026-09-29 15:10 [ruptura_volumen] CIERRE CRV take-profit bruto +2.50% neto +2.00%
- 2026-09-29 15:10 [ruptura_volumen_tope] CIERRE CRV take-profit bruto +2.50% neto +1.40%
- 2026-09-29 15:10 [ruptura_volumen_regimen] CIERRE CRV take-profit bruto +2.50% neto +2.00%
- 2026-09-29 15:10 [ruptura_volumen_evento] CIERRE CRV take-profit bruto +2.50% neto +1.40%
- 2026-09-29 15:10 [macd_momentum] CIERRE DASH momentum perdido bruto -0.86% neto -1.36%
- 2026-09-29 15:10 [macd_momentum_regimen] CIERRE DASH momentum perdido bruto -0.86% neto -1.36%
- 2026-09-29 15:10 [macd_momentum_evento] CIERRE DASH momentum perdido bruto -0.86% neto -1.96%
- 2026-09-29 15:10 [c_banda_atr] CIERRE JUP stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 15:10 [macd_momentum] CIERRE JUP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:10 [estocastico_rebote] CIERRE JUP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:10 [macd_sin_salida] CIERRE JUP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:10 [c_banda_atr_tope] CIERRE JUP stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:10 [c_banda_atr_regimen] CIERRE JUP stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 15:10 [macd_momentum_regimen] CIERRE JUP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:10 [c_banda_atr_evento] CIERRE JUP stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:10 [macd_momentum_evento] CIERRE JUP stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:10 [macd_momentum] CIERRE MON stop-loss bruto -1.65% neto -2.15%
- 2026-09-29 15:10 [macd_sin_salida] CIERRE MON stop-loss bruto -1.65% neto -2.15%
- 2026-09-29 15:10 [macd_momentum_regimen] CIERRE MON stop-loss bruto -1.65% neto -2.15%
- 2026-09-29 15:10 [macd_momentum_evento] CIERRE MON stop-loss bruto -1.65% neto -2.75%
- 2026-09-29 15:10 [ruptura_volumen] CIERRE INJ stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 15:10 [ruptura_volumen_tope] CIERRE INJ stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 15:10 [ruptura_volumen_regimen] CIERRE INJ stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 15:10 [macd_momentum] CIERRE RENDER momentum perdido bruto -0.87% neto -1.37%
- 2026-09-29 15:10 [macd_momentum_regimen] CIERRE RENDER momentum perdido bruto -0.87% neto -1.37%
- 2026-09-29 15:10 [macd_momentum_evento] CIERRE RENDER momentum perdido bruto -0.87% neto -1.97%
- 2026-09-29 15:10 [estocastico_rebote] CIERRE VIRTUAL stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:10 [macd_sin_salida] CIERRE VIRTUAL stop-loss bruto -1.55% neto -2.05%
- 2026-09-29 15:10 [ruptura_volumen] CIERRE RAY stop-loss bruto -2.22% neto -2.72%
- 2026-09-29 15:10 [pullback_tendencia] CIERRE RAY rotura de tendencia bruto -1.36% neto -2.16%
- 2026-09-29 15:10 [macd_momentum] CIERRE RAY stop-loss bruto -2.22% neto -2.72%
- 2026-09-29 15:10 [macd_momentum_regimen] CIERRE RAY stop-loss bruto -2.22% neto -2.72%
- 2026-09-29 15:10 [ruptura_volumen_regimen] CIERRE RAY stop-loss bruto -2.22% neto -2.72%
- 2026-09-29 15:10 [c_banda_atr_evento] CIERRE RAY stop-loss bruto -2.22% neto -3.32%
- 2026-09-29 15:10 [macd_momentum_evento] CIERRE RAY stop-loss bruto -2.22% neto -3.32%
- 2026-09-29 15:10 [ruptura_volumen_evento] CIERRE RAY stop-loss bruto -2.22% neto -3.32%
- 2026-09-29 15:10 [ruptura_volumen] CIERRE OP stop-loss bruto -1.34% neto -1.84%
- 2026-09-29 15:10 [ruptura_volumen_tope] CIERRE OP stop-loss bruto -1.34% neto -2.44%
- 2026-09-29 15:10 [ruptura_volumen_regimen] CIERRE OP stop-loss bruto -1.34% neto -1.84%
- 2026-09-29 15:10 [ruptura_volumen_evento] CIERRE OP stop-loss bruto -1.34% neto -2.44%
- 2026-09-29 15:10 [macd_momentum] CIERRE SHIB momentum perdido bruto -0.35% neto -0.85%
- 2026-09-29 15:10 [macd_momentum_regimen] CIERRE SHIB momentum perdido bruto -0.35% neto -0.85%
- 2026-09-29 15:10 [macd_momentum_evento] CIERRE SHIB momentum perdido bruto -0.35% neto -1.45%
- 2026-09-29 15:10 [macd_momentum] CIERRE BNB momentum perdido bruto -0.51% neto -1.01%
- 2026-09-29 15:10 [macd_momentum_regimen] CIERRE BNB momentum perdido bruto -0.51% neto -1.01%
- 2026-09-29 15:10 [macd_momentum_evento] CIERRE BNB momentum perdido bruto -0.51% neto -1.61%
- 2026-09-29 15:10 [ruptura_volumen] CIERRE ASTER stop-loss bruto -1.28% neto -1.78%
- 2026-09-29 15:10 [macd_momentum] CIERRE ASTER momentum perdido bruto -1.08% neto -1.58%
- 2026-09-29 15:10 [macd_momentum_regimen] CIERRE ASTER momentum perdido bruto -1.08% neto -1.58%
- 2026-09-29 15:10 [ruptura_volumen_regimen] CIERRE ASTER stop-loss bruto -1.28% neto -1.78%
- 2026-09-29 15:10 [macd_momentum_evento] CIERRE ASTER momentum perdido bruto -1.08% neto -2.18%
- 2026-09-29 15:10 [ruptura_volumen_evento] CIERRE ASTER stop-loss bruto -1.28% neto -2.38%
- 2026-09-29 15:10 [macd_sin_salida] CIERRE SPX stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
