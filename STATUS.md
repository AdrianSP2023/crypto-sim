# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 15:16 UTC · vueltas 250 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.07 € (-3.70%) | 207 | 11 | 33% | -0.096% | -0.722% | -0.846% | -34.06 € |
| reversion_bb | 915.51 € (-0.94%) | 36 | 11 | 36% | -0.013% | -1.113% | -1.213% | -9.23 € |
| ruptura_volumen | 878.49 € (-4.95%) | 240 | 4 | 22% | -0.230% | -0.839% | -0.947% | -45.59 € |
| rebote_extremo | 922.14 € (-0.23%) | 11 | 2 | 45% | +0.049% | -1.051% | -1.228% | -2.67 € |
| pullback_tendencia | 892.98 € (-3.38%) | 143 | 1 | 13% | -0.280% | -0.965% | -1.066% | -31.39 € |
| macd_momentum | 874.45 € (-5.39%) | 356 | 7 | 20% | -0.049% | -0.622% | -0.731% | -49.91 € |
| estocastico_rebote | 877.34 € (-5.07%) | 274 | 11 | 30% | -0.161% | -0.756% | -0.869% | -46.90 € |
| ruptura_estricta | 884.99 € (-4.25%) | 137 | 2 | 23% | -0.562% | -1.254% | -1.376% | -39.15 € |
| macd_sin_salida | 880.02 € (-4.78%) | 255 | 13 | 33% | -0.158% | -0.761% | -0.876% | -44.04 € |
| c_banda_atr_tope | 911.62 € (-1.36%) | 49 | 3 | 27% | -0.057% | -1.095% | -1.209% | -12.33 € |
| ruptura_volumen_tope | 907.62 € (-1.80%) | 78 | 3 | 24% | -0.088% | -0.926% | -1.042% | -16.57 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 895.99 € (-3.06%) | 174 | 11 | 34% | -0.055% | -0.707% | -0.825% | -28.13 € |
| macd_momentum_evento | 879.30 € (-4.86%) | 309 | 7 | 17% | -0.061% | -0.646% | -0.750% | -45.07 € |
| ruptura_volumen_evento | 890.99 € (-3.60%) | 190 | 4 | 23% | -0.126% | -0.765% | -0.862% | -33.07 € |
| rebote_desplome | 925.20 € (+0.10%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 925.20 € (+0.10%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-01 15:10 | pullback_tendencia | LTC | rotura de tendencia | -0.25% | -0.75% | -0.17 |

## Eventos de la última vuelta

- 2026-10-01 15:15 [c_banda_atr] CIERRE ADA stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 15:15 [macd_sin_salida] CIERRE ADA stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 15:15 [c_banda_atr_evento] CIERRE ADA stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 15:15 [macd_momentum] CIERRE AVAX momentum perdido bruto -0.44% neto -0.94%
- 2026-10-01 15:15 [macd_momentum_evento] CIERRE AVAX momentum perdido bruto -0.44% neto -0.94%
- 2026-10-01 15:10 [rebote_extremo] ENTRADA ENA @ 0.22 (23.04 €, apertura)
- 2026-10-01 15:15 [macd_momentum] CIERRE BCH momentum perdido bruto -0.27% neto -0.77%
- 2026-10-01 15:15 [macd_momentum_evento] CIERRE BCH momentum perdido bruto -0.27% neto -0.77%
- 2026-10-01 15:15 [macd_sin_salida] CIERRE MINA timeout bruto -0.30% neto -0.80%
- 2026-10-01 15:15 [reversion_bb] CIERRE VVV stop-loss bruto -1.50% neto -2.60%
- 2026-10-01 15:10 [reversion_bb] ENTRADA APT @ 0.6707 (22.88 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
