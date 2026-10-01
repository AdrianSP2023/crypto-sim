# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 15:11 UTC · vueltas 249 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.62 € (-3.75%) | 206 | 12 | 33% | -0.089% | -0.716% | -0.840% | -33.61 € |
| reversion_bb | 914.47 € (-1.06%) | 35 | 11 | 37% | +0.030% | -1.070% | -1.171% | -8.63 € |
| ruptura_volumen | 878.59 € (-4.94%) | 240 | 4 | 22% | -0.230% | -0.839% | -0.947% | -45.59 € |
| rebote_extremo | 921.62 € (-0.28%) | 11 | 1 | 45% | +0.049% | -1.051% | -1.228% | -2.67 € |
| pullback_tendencia | 892.94 € (-3.39%) | 143 | 1 | 13% | -0.280% | -0.965% | -1.066% | -31.39 € |
| macd_momentum | 874.33 € (-5.40%) | 354 | 9 | 20% | -0.047% | -0.621% | -0.730% | -49.54 € |
| estocastico_rebote | 876.85 € (-5.13%) | 274 | 11 | 30% | -0.161% | -0.756% | -0.869% | -46.90 € |
| ruptura_estricta | 884.97 € (-4.25%) | 137 | 2 | 23% | -0.562% | -1.254% | -1.376% | -39.15 € |
| macd_sin_salida | 879.24 € (-4.87%) | 253 | 15 | 33% | -0.152% | -0.755% | -0.872% | -43.42 € |
| c_banda_atr_tope | 911.21 € (-1.41%) | 49 | 3 | 27% | -0.057% | -1.095% | -1.209% | -12.33 € |
| ruptura_volumen_tope | 907.79 € (-1.78%) | 78 | 3 | 24% | -0.088% | -0.926% | -1.042% | -16.57 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 895.54 € (-3.11%) | 173 | 12 | 34% | -0.047% | -0.699% | -0.818% | -27.68 € |
| macd_momentum_evento | 879.18 € (-4.88%) | 307 | 9 | 17% | -0.059% | -0.645% | -0.749% | -44.69 € |
| ruptura_volumen_evento | 891.09 € (-3.59%) | 190 | 4 | 23% | -0.126% | -0.765% | -0.862% | -33.07 € |
| rebote_desplome | 925.31 € (+0.12%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 925.31 € (+0.12%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 15:10 | c_banda_atr_evento | APT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 15:10 | c_banda_atr_evento | HBAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 15:10 | c_banda_atr_tope | APT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 15:10 | macd_sin_salida | APT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 15:10 | ruptura_estricta | UNI | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-01 15:10 | pullback_tendencia | LTC | rotura de tendencia | -0.25% | -0.75% | -0.17 |
| 2026-10-01 15:10 | pullback_tendencia | ETH | rotura de tendencia | -0.38% | -0.88% | -0.20 |
| 2026-10-01 15:10 | rebote_extremo | WLD | stop-loss | -2.00% | -3.10% | -0.71 |
| 2026-10-01 15:10 | c_banda_atr | APT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 15:10 | c_banda_atr | HBAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 15:05 | estocastico_rebote | SKY | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 15:05 | estocastico_rebote | MINA | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 15:05 | reversion_bb | ENA | stop-loss | -1.55% | -2.65% | -0.61 |
| 2026-10-01 15:00 | macd_momentum_evento | MINA | momentum perdido | -1.43% | -1.93% | -0.43 |
| 2026-10-01 15:00 | macd_momentum_evento | RENDER | momentum perdido | -0.47% | -0.97% | -0.21 |

## Eventos de la última vuelta

- 2026-10-01 15:05 [macd_momentum] ENTRADA XRP @ 1.31825 (21.87 €, apertura)
- 2026-10-01 15:05 [macd_sin_salida] ENTRADA XRP @ 1.31825 (22.03 €, apertura)
- 2026-10-01 15:05 [macd_momentum_evento] ENTRADA XRP @ 1.31825 (21.99 €, apertura)
- 2026-10-01 15:05 [pullback_tendencia] ENTRADA ETH @ 2390.36 (22.33 €, apertura)
- 2026-10-01 15:10 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto -0.38% neto -0.88%
- 2026-10-01 15:05 [macd_momentum] ENTRADA LINK @ 12.7369 (21.87 €, apertura)
- 2026-10-01 15:05 [macd_momentum_evento] ENTRADA LINK @ 12.7369 (21.99 €, apertura)
- 2026-10-01 15:10 [c_banda_atr] CIERRE HBAR stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 15:10 [c_banda_atr_evento] CIERRE HBAR stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 15:10 [ruptura_estricta] CIERRE UNI stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 15:10 [pullback_tendencia] CIERRE LTC rotura de tendencia bruto -0.25% neto -0.75%
- 2026-10-01 15:10 [rebote_extremo] CIERRE WLD stop-loss bruto -2.00% neto -3.10%
- 2026-10-01 15:05 [macd_momentum] ENTRADA BCH @ 272.47 (21.87 €, apertura)
- 2026-10-01 15:05 [macd_sin_salida] ENTRADA BCH @ 272.47 (22.03 €, apertura)
- 2026-10-01 15:05 [macd_momentum_evento] ENTRADA BCH @ 272.47 (21.99 €, apertura)
- 2026-10-01 15:05 [ruptura_volumen_tope] ENTRADA SKY @ 0.07019 (22.69 €, apertura)
- 2026-10-01 15:10 [c_banda_atr] CIERRE APT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 15:10 [macd_sin_salida] CIERRE APT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 15:10 [c_banda_atr_tope] CIERRE APT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 15:10 [c_banda_atr_evento] CIERRE APT stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
