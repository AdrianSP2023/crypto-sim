# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 14:56 UTC · vueltas 246 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.28 € (-3.67%) | 204 | 14 | 34% | -0.075% | -0.703% | -0.829% | -32.71 € |
| reversion_bb | 915.12 € (-0.99%) | 34 | 11 | 38% | +0.076% | -1.024% | -1.122% | -8.02 € |
| ruptura_volumen | 878.48 € (-4.95%) | 240 | 4 | 22% | -0.230% | -0.839% | -0.947% | -45.59 € |
| rebote_extremo | 921.87 € (-0.26%) | 10 | 1 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 893.26 € (-3.35%) | 141 | 2 | 13% | -0.279% | -0.967% | -1.069% | -31.03 € |
| macd_momentum | 875.12 € (-5.31%) | 348 | 12 | 20% | -0.038% | -0.613% | -0.723% | -48.15 € |
| estocastico_rebote | 877.13 € (-5.10%) | 272 | 13 | 30% | -0.164% | -0.759% | -0.872% | -46.75 € |
| ruptura_estricta | 885.22 € (-4.22%) | 136 | 3 | 23% | -0.551% | -1.245% | -1.367% | -38.60 € |
| macd_sin_salida | 880.03 € (-4.78%) | 252 | 14 | 33% | -0.147% | -0.751% | -0.867% | -42.98 € |
| c_banda_atr_tope | 911.71 € (-1.36%) | 48 | 4 | 27% | -0.027% | -1.077% | -1.191% | -11.88 € |
| ruptura_volumen_tope | 907.67 € (-1.79%) | 78 | 2 | 24% | -0.088% | -0.926% | -1.042% | -16.57 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 896.20 € (-3.03%) | 171 | 14 | 35% | -0.030% | -0.684% | -0.803% | -26.77 € |
| macd_momentum_evento | 879.97 € (-4.79%) | 301 | 12 | 18% | -0.049% | -0.637% | -0.741% | -43.30 € |
| ruptura_volumen_evento | 890.98 € (-3.60%) | 190 | 4 | 23% | -0.126% | -0.765% | -0.862% | -33.07 € |
| rebote_desplome | 925.07 € (+0.09%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 925.07 € (+0.09%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 14:55 | ruptura_volumen_evento | SEI | stop-loss | -1.31% | -1.81% | -0.41 |
| 2026-10-01 14:55 | ruptura_volumen_evento | ARB | stop-loss | -1.62% | -2.12% | -0.47 |
| 2026-10-01 14:55 | macd_momentum_evento | APT | momentum perdido | -0.86% | -1.36% | -0.30 |
| 2026-10-01 14:55 | macd_momentum_evento | BNB | momentum perdido | -0.26% | -0.76% | -0.17 |
| 2026-10-01 14:55 | macd_momentum_evento | OP | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 14:55 | macd_momentum_evento | PEPE | momentum perdido | -0.93% | -1.43% | -0.32 |
| 2026-10-01 14:55 | macd_momentum_evento | ARB | stop-loss | -1.62% | -2.12% | -0.47 |
| 2026-10-01 14:55 | macd_momentum_evento | SOL | momentum perdido | -0.16% | -0.66% | -0.15 |
| 2026-10-01 14:55 | c_banda_atr_evento | SEI | timeout | -1.31% | -1.81% | -0.41 |
| 2026-10-01 14:55 | c_banda_atr_evento | OP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 14:55 | ruptura_volumen_tope | SEI | stop-loss | -1.31% | -1.81% | -0.41 |
| 2026-10-01 14:55 | ruptura_volumen_tope | ARB | stop-loss | -1.62% | -2.12% | -0.48 |
| 2026-10-01 14:55 | macd_sin_salida | SPX | stop-loss | -1.54% | -2.04% | -0.45 |
| 2026-10-01 14:55 | macd_sin_salida | ARB | stop-loss | -1.62% | -2.12% | -0.47 |
| 2026-10-01 14:55 | macd_momentum | APT | momentum perdido | -0.86% | -1.36% | -0.30 |

## Eventos de la última vuelta

- 2026-10-01 14:55 [macd_momentum] CIERRE SOL momentum perdido bruto -0.16% neto -0.66%
- 2026-10-01 14:55 [macd_momentum_evento] CIERRE SOL momentum perdido bruto -0.16% neto -0.66%
- 2026-10-01 14:50 [pullback_tendencia] ENTRADA LTC @ 59.53 (22.33 €, apertura)
- 2026-10-01 14:50 [reversion_bb] ENTRADA DOT @ 1.0419 (22.92 €, apertura)
- 2026-10-01 14:55 [ruptura_volumen] CIERRE ARB stop-loss bruto -1.62% neto -2.12%
- 2026-10-01 14:55 [macd_momentum] CIERRE ARB stop-loss bruto -1.62% neto -2.12%
- 2026-10-01 14:55 [macd_sin_salida] CIERRE ARB stop-loss bruto -1.62% neto -2.12%
- 2026-10-01 14:55 [ruptura_volumen_tope] CIERRE ARB stop-loss bruto -1.62% neto -2.12%
- 2026-10-01 14:55 [macd_momentum_evento] CIERRE ARB stop-loss bruto -1.62% neto -2.12%
- 2026-10-01 14:55 [ruptura_volumen_evento] CIERRE ARB stop-loss bruto -1.62% neto -2.12%
- 2026-10-01 14:50 [reversion_bb] ENTRADA ENA @ 0.226 (22.92 €, apertura)
- 2026-10-01 14:55 [macd_momentum] CIERRE PEPE momentum perdido bruto -0.93% neto -1.43%
- 2026-10-01 14:55 [macd_momentum_evento] CIERRE PEPE momentum perdido bruto -0.93% neto -1.43%
- 2026-10-01 14:55 [c_banda_atr] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:55 [macd_momentum] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:55 [c_banda_atr_evento] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:55 [macd_momentum_evento] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:55 [reversion_bb] CIERRE FIL stop-loss bruto -1.79% neto -2.89%
- 2026-10-01 14:50 [ruptura_volumen] ENTRADA WLFI @ 0.0489 (21.98 €, apertura)
- 2026-10-01 14:50 [macd_momentum] ENTRADA WLFI @ 0.0489 (21.91 €, apertura)
- 2026-10-01 14:50 [ruptura_estricta] ENTRADA WLFI @ 0.0489 (22.14 €, apertura)
- 2026-10-01 14:50 [macd_sin_salida] ENTRADA WLFI @ 0.0489 (22.04 €, apertura)
- 2026-10-01 14:50 [ruptura_volumen_tope] ENTRADA WLFI @ 0.0489 (22.70 €, apertura)
- 2026-10-01 14:50 [macd_momentum_evento] ENTRADA WLFI @ 0.0489 (22.04 €, apertura)
- 2026-10-01 14:50 [ruptura_volumen_evento] ENTRADA WLFI @ 0.0489 (22.29 €, apertura)
- 2026-10-01 14:55 [macd_momentum] CIERRE BNB momentum perdido bruto -0.26% neto -0.76%
- 2026-10-01 14:55 [macd_momentum_evento] CIERRE BNB momentum perdido bruto -0.26% neto -0.76%
- 2026-10-01 14:55 [c_banda_atr] CIERRE SEI timeout bruto -1.31% neto -1.81%
- 2026-10-01 14:55 [ruptura_volumen] CIERRE SEI stop-loss bruto -1.31% neto -1.81%
- 2026-10-01 14:55 [ruptura_volumen_tope] CIERRE SEI stop-loss bruto -1.31% neto -1.81%
- 2026-10-01 14:55 [c_banda_atr_evento] CIERRE SEI timeout bruto -1.31% neto -1.81%
- 2026-10-01 14:55 [ruptura_volumen_evento] CIERRE SEI stop-loss bruto -1.31% neto -1.81%
- 2026-10-01 14:55 [macd_momentum] CIERRE APT momentum perdido bruto -0.86% neto -1.36%
- 2026-10-01 14:55 [macd_momentum_evento] CIERRE APT momentum perdido bruto -0.86% neto -1.36%
- 2026-10-01 14:55 [macd_sin_salida] CIERRE SPX stop-loss bruto -1.54% neto -2.04%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
