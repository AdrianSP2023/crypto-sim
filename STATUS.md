# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 15:21 UTC · vueltas 251 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.52 € (-3.54%) | 207 | 13 | 33% | -0.096% | -0.722% | -0.846% | -34.06 € |
| reversion_bb | 916.56 € (-0.83%) | 37 | 10 | 38% | +0.028% | -1.072% | -1.174% | -9.13 € |
| ruptura_volumen | 879.08 € (-4.89%) | 240 | 4 | 22% | -0.230% | -0.839% | -0.947% | -45.59 € |
| rebote_extremo | 922.41 € (-0.20%) | 11 | 2 | 45% | +0.049% | -1.051% | -1.228% | -2.67 € |
| pullback_tendencia | 893.22 € (-3.36%) | 143 | 2 | 13% | -0.280% | -0.965% | -1.066% | -31.39 € |
| macd_momentum | 875.35 € (-5.29%) | 356 | 8 | 20% | -0.049% | -0.622% | -0.731% | -49.91 € |
| estocastico_rebote | 878.64 € (-4.93%) | 274 | 13 | 30% | -0.161% | -0.756% | -0.869% | -46.90 € |
| ruptura_estricta | 885.37 € (-4.21%) | 137 | 2 | 23% | -0.562% | -1.254% | -1.376% | -39.15 € |
| macd_sin_salida | 881.51 € (-4.62%) | 255 | 13 | 33% | -0.158% | -0.761% | -0.876% | -44.04 € |
| c_banda_atr_tope | 912.29 € (-1.29%) | 49 | 5 | 27% | -0.057% | -1.095% | -1.209% | -12.33 € |
| ruptura_volumen_tope | 907.94 € (-1.76%) | 78 | 3 | 24% | -0.088% | -0.926% | -1.042% | -16.57 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 897.45 € (-2.90%) | 174 | 13 | 34% | -0.055% | -0.707% | -0.825% | -28.13 € |
| macd_momentum_evento | 880.20 € (-4.77%) | 309 | 8 | 17% | -0.061% | -0.646% | -0.750% | -45.07 € |
| ruptura_volumen_evento | 891.59 € (-3.53%) | 190 | 4 | 23% | -0.126% | -0.765% | -0.862% | -33.07 € |
| rebote_desplome | 925.38 € (+0.12%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 925.38 € (+0.12%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 15:20 | reversion_bb | APT | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-10-01 15:15 | macd_momentum_evento | BCH | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-10-01 15:15 | macd_momentum_evento | AVAX | momentum perdido | -0.44% | -0.94% | -0.21 |
| 2026-10-01 15:15 | c_banda_atr_evento | ADA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 15:15 | macd_sin_salida | MINA | timeout | -0.30% | -0.80% | -0.18 |
| 2026-10-01 15:15 | macd_sin_salida | ADA | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 15:15 | macd_momentum | BCH | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-10-01 15:15 | macd_momentum | AVAX | momentum perdido | -0.44% | -0.94% | -0.21 |
| 2026-10-01 15:15 | reversion_bb | VVV | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-10-01 15:15 | c_banda_atr | ADA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 15:10 | c_banda_atr_evento | APT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 15:10 | c_banda_atr_evento | HBAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 15:10 | c_banda_atr_tope | APT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 15:10 | macd_sin_salida | APT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 15:10 | ruptura_estricta | UNI | stop-loss | -2.00% | -2.50% | -0.55 |

## Eventos de la última vuelta

- 2026-10-01 15:15 [pullback_tendencia] ENTRADA TAO @ 272.875 (22.32 €, apertura)
- 2026-10-01 15:15 [estocastico_rebote] ENTRADA UNI @ 8.0687 (21.93 €, apertura)
- 2026-10-01 15:15 [c_banda_atr] ENTRADA ZRO @ 1.496 (22.25 €, apertura)
- 2026-10-01 15:15 [c_banda_atr_tope] ENTRADA ZRO @ 1.496 (22.80 €, apertura)
- 2026-10-01 15:15 [c_banda_atr_evento] ENTRADA ZRO @ 1.496 (22.40 €, apertura)
- 2026-10-01 15:15 [macd_momentum] ENTRADA PEPE @ 3.892e-06 (21.86 €, apertura)
- 2026-10-01 15:15 [macd_momentum_evento] ENTRADA PEPE @ 3.892e-06 (21.98 €, apertura)
- 2026-10-01 15:15 [estocastico_rebote] ENTRADA MINA @ 0.1315 (21.93 €, apertura)
- 2026-10-01 15:15 [c_banda_atr] ENTRADA KAS @ 0.0378 (22.25 €, apertura)
- 2026-10-01 15:15 [c_banda_atr_tope] ENTRADA KAS @ 0.0378 (22.80 €, apertura)
- 2026-10-01 15:15 [c_banda_atr_evento] ENTRADA KAS @ 0.0378 (22.40 €, apertura)
- 2026-10-01 15:20 [reversion_bb] CIERRE APT take-profit bruto +1.50% neto +0.40%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
