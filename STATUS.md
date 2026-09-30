# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 06:11 UTC · vueltas 221 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.53 € (-2.89%) | 126 | 27 | 28% | -0.230% | -0.937% | -1.072% | -27.03 € |
| reversion_bb | 917.19 € (-0.76%) | 34 | 6 | 47% | +0.236% | -0.865% | -0.970% | -6.78 € |
| ruptura_volumen | 890.98 € (-3.60%) | 157 | 19 | 19% | -0.267% | -0.933% | -1.060% | -33.34 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.60 € (-2.13%) | 114 | 4 | 25% | -0.038% | -0.767% | -0.894% | -20.04 € |
| macd_momentum | 876.76 € (-5.14%) | 308 | 13 | 17% | -0.095% | -0.679% | -0.791% | -47.27 € |
| estocastico_rebote | 889.47 € (-3.76%) | 207 | 8 | 35% | -0.097% | -0.723% | -0.856% | -34.16 € |
| ruptura_estricta | 904.11 € (-2.18%) | 70 | 10 | 23% | -0.383% | -1.256% | -1.396% | -20.15 € |
| macd_sin_salida | 892.37 € (-3.45%) | 180 | 28 | 29% | -0.135% | -0.780% | -0.907% | -31.97 € |
| c_banda_atr_tope | 910.56 € (-1.48%) | 38 | 3 | 18% | -0.461% | -1.561% | -1.694% | -13.63 € |
| ruptura_volumen_tope | 909.59 € (-1.59%) | 58 | 4 | 17% | -0.153% | -1.108% | -1.228% | -14.75 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.65 € (-4.18%) | 200 | 2 | 14% | -0.215% | -0.846% | -0.960% | -38.41 € |
| ruptura_volumen_regimen | 897.87 € (-2.85%) | 117 | 9 | 18% | -0.246% | -0.970% | -1.099% | -25.91 € |
| c_banda_atr_evento | 900.59 € (-2.56%) | 94 | 27 | 24% | -0.332% | -1.113% | -1.250% | -23.97 € |
| macd_momentum_evento | 889.09 € (-3.80%) | 188 | 13 | 13% | -0.177% | -0.817% | -0.926% | -34.93 € |
| ruptura_volumen_evento | 896.46 € (-3.01%) | 98 | 19 | 11% | -0.475% | -1.244% | -1.371% | -27.85 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 06:10 | ruptura_volumen_evento | USELESS | stop-loss | -1.77% | -2.27% | -0.51 |
| 2026-09-30 06:10 | ruptura_volumen_evento | XDC | timeout | +0.30% | -0.20% | -0.04 |
| 2026-09-30 06:10 | macd_momentum_evento | TAO | momentum perdido | -0.49% | -0.99% | -0.22 |
| 2026-09-30 06:10 | macd_momentum_evento | UNI | momentum perdido | -0.12% | -0.62% | -0.14 |
| 2026-09-30 06:10 | macd_momentum_evento | LTC | momentum perdido | -0.29% | -0.79% | -0.17 |
| 2026-09-30 06:10 | macd_momentum_evento | ETH | momentum perdido | -0.19% | -0.69% | -0.15 |
| 2026-09-30 06:10 | macd_momentum_evento | BTC | momentum perdido | -0.23% | -0.73% | -0.16 |
| 2026-09-30 06:10 | c_banda_atr_evento | XLM | timeout | +0.09% | -0.41% | -0.09 |
| 2026-09-30 06:10 | ruptura_volumen_regimen | USELESS | stop-loss | -1.74% | -2.23% | -0.50 |
| 2026-09-30 06:10 | macd_momentum_regimen | TAO | momentum perdido | -0.49% | -0.99% | -0.22 |
| 2026-09-30 06:10 | c_banda_atr_regimen | XLM | timeout | +0.09% | -0.41% | -0.09 |
| 2026-09-30 06:10 | ruptura_volumen_tope | XDC | timeout | +0.30% | -0.20% | -0.04 |
| 2026-09-30 06:10 | c_banda_atr_tope | XLM | timeout | +0.09% | -1.01% | -0.23 |
| 2026-09-30 06:10 | estocastico_rebote | PENGU | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:10 | estocastico_rebote | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-30 06:10 [macd_momentum] CIERRE BTC momentum perdido bruto -0.23% neto -0.73%
- 2026-09-30 06:10 [macd_momentum_evento] CIERRE BTC momentum perdido bruto -0.23% neto -0.73%
- 2026-09-30 06:10 [macd_momentum] CIERRE ETH momentum perdido bruto -0.19% neto -0.69%
- 2026-09-30 06:10 [macd_momentum_evento] CIERRE ETH momentum perdido bruto -0.19% neto -0.69%
- 2026-09-30 06:10 [estocastico_rebote] CIERRE QNT take-profit bruto +1.80% neto +1.30%
- 2026-09-30 06:10 [macd_momentum] CIERRE LTC momentum perdido bruto -0.29% neto -0.79%
- 2026-09-30 06:10 [macd_momentum_evento] CIERRE LTC momentum perdido bruto -0.29% neto -0.79%
- 2026-09-30 06:10 [c_banda_atr] CIERRE XLM timeout bruto +0.09% neto -0.41%
- 2026-09-30 06:10 [c_banda_atr_tope] CIERRE XLM timeout bruto +0.09% neto -1.01%
- 2026-09-30 06:10 [c_banda_atr_regimen] CIERRE XLM timeout bruto +0.09% neto -0.41%
- 2026-09-30 06:10 [c_banda_atr_evento] CIERRE XLM timeout bruto +0.09% neto -0.41%
- 2026-09-30 06:10 [macd_momentum] CIERRE UNI momentum perdido bruto -0.12% neto -0.62%
- 2026-09-30 06:10 [macd_momentum_evento] CIERRE UNI momentum perdido bruto -0.12% neto -0.62%
- 2026-09-30 06:10 [macd_momentum] CIERRE TAO momentum perdido bruto -0.49% neto -0.99%
- 2026-09-30 06:10 [macd_momentum_regimen] CIERRE TAO momentum perdido bruto -0.49% neto -0.99%
- 2026-09-30 06:10 [macd_momentum_evento] CIERRE TAO momentum perdido bruto -0.49% neto -0.99%
- 2026-09-30 06:10 [ruptura_volumen] CIERRE XDC timeout bruto +0.30% neto -0.20%
- 2026-09-30 06:10 [ruptura_volumen_tope] CIERRE XDC timeout bruto +0.30% neto -0.20%
- 2026-09-30 06:10 [ruptura_volumen_evento] CIERRE XDC timeout bruto +0.30% neto -0.20%
- 2026-09-30 06:10 [estocastico_rebote] CIERRE JUP stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:10 [estocastico_rebote] CIERRE PEPE take-profit bruto +1.94% neto +1.44%
- 2026-09-30 06:10 [ruptura_volumen] CIERRE USELESS stop-loss bruto -1.77% neto -2.27%
- 2026-09-30 06:10 [ruptura_volumen_regimen] CIERRE USELESS stop-loss bruto -1.74% neto -2.24%
- 2026-09-30 06:10 [ruptura_volumen_evento] CIERRE USELESS stop-loss bruto -1.77% neto -2.27%
- 2026-09-30 06:10 [estocastico_rebote] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:10 [estocastico_rebote] CIERRE PENGU stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
