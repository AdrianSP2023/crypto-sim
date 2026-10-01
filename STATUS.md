# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 15:36 UTC · vueltas 254 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.93 € (-3.71%) | 208 | 25 | 34% | -0.085% | -0.710% | -0.835% | -33.68 € |
| reversion_bb | 915.38 € (-0.96%) | 37 | 10 | 38% | +0.028% | -1.072% | -1.174% | -9.13 € |
| ruptura_volumen | 879.13 € (-4.88%) | 240 | 8 | 22% | -0.230% | -0.839% | -0.947% | -45.59 € |
| rebote_extremo | 921.72 € (-0.27%) | 11 | 2 | 45% | +0.049% | -1.051% | -1.228% | -2.67 € |
| pullback_tendencia | 892.90 € (-3.39%) | 143 | 2 | 13% | -0.280% | -0.965% | -1.066% | -31.39 € |
| macd_momentum | 873.92 € (-5.44%) | 357 | 22 | 20% | -0.042% | -0.615% | -0.724% | -49.53 € |
| estocastico_rebote | 878.11 € (-4.99%) | 277 | 10 | 31% | -0.145% | -0.739% | -0.852% | -46.34 € |
| ruptura_estricta | 885.22 € (-4.22%) | 137 | 4 | 23% | -0.562% | -1.254% | -1.376% | -39.15 € |
| macd_sin_salida | 880.05 € (-4.78%) | 256 | 22 | 33% | -0.149% | -0.751% | -0.867% | -43.66 € |
| c_banda_atr_tope | 912.32 € (-1.29%) | 49 | 5 | 27% | -0.057% | -1.095% | -1.209% | -12.33 € |
| ruptura_volumen_tope | 907.56 € (-1.80%) | 79 | 5 | 24% | -0.102% | -0.936% | -1.051% | -16.96 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 895.85 € (-3.07%) | 175 | 25 | 34% | -0.043% | -0.693% | -0.811% | -27.75 € |
| macd_momentum_evento | 878.76 € (-4.92%) | 310 | 22 | 17% | -0.053% | -0.638% | -0.743% | -44.68 € |
| ruptura_volumen_evento | 891.64 € (-3.53%) | 190 | 8 | 23% | -0.126% | -0.765% | -0.862% | -33.07 € |
| rebote_desplome | 925.09 € (+0.09%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 925.09 € (+0.09%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 15:35 | ruptura_volumen_tope | TAO | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 15:30 | estocastico_rebote | BNB | timeout | +0.05% | -0.45% | -0.10 |
| 2026-10-01 15:25 | macd_momentum_evento | TON | take-profit | +2.25% | +1.75% | +0.39 |
| 2026-10-01 15:25 | c_banda_atr_evento | TON | take-profit | +2.17% | +1.67% | +0.38 |
| 2026-10-01 15:25 | macd_sin_salida | TON | take-profit | +2.25% | +1.75% | +0.39 |
| 2026-10-01 15:25 | estocastico_rebote | TON | take-profit | +2.17% | +1.67% | +0.37 |
| 2026-10-01 15:25 | estocastico_rebote | PEPE | take-profit | +1.83% | +1.33% | +0.29 |
| 2026-10-01 15:25 | macd_momentum | TON | take-profit | +2.25% | +1.75% | +0.39 |
| 2026-10-01 15:25 | c_banda_atr | TON | take-profit | +2.17% | +1.67% | +0.38 |
| 2026-10-01 15:20 | reversion_bb | APT | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-10-01 15:15 | macd_momentum_evento | BCH | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-10-01 15:15 | macd_momentum_evento | AVAX | momentum perdido | -0.44% | -0.94% | -0.21 |
| 2026-10-01 15:15 | c_banda_atr_evento | ADA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 15:15 | macd_sin_salida | MINA | timeout | -0.30% | -0.80% | -0.18 |
| 2026-10-01 15:15 | macd_sin_salida | ADA | stop-loss | -1.50% | -2.00% | -0.44 |

## Eventos de la última vuelta

- 2026-10-01 15:35 [ruptura_volumen_tope] CIERRE TAO stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 15:30 [c_banda_atr] ENTRADA USELESS @ 0.2019 (22.26 €, apertura)
- 2026-10-01 15:30 [c_banda_atr_evento] ENTRADA USELESS @ 0.2019 (22.41 €, apertura)
- 2026-10-01 15:30 [ruptura_volumen] ENTRADA XMR @ 478.95 (21.97 €, apertura)
- 2026-10-01 15:30 [ruptura_volumen_tope] ENTRADA XMR @ 478.95 (22.68 €, apertura)
- 2026-10-01 15:30 [ruptura_volumen_evento] ENTRADA XMR @ 478.95 (22.28 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
