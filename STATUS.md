# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 06:21 UTC · vueltas 223 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 895.74 € (-3.08%) | 126 | 27 | 28% | -0.230% | -0.937% | -1.072% | -27.03 € |
| reversion_bb | 916.53 € (-0.83%) | 35 | 7 | 46% | +0.183% | -0.917% | -1.027% | -7.39 € |
| ruptura_volumen | 889.55 € (-3.75%) | 159 | 17 | 19% | -0.270% | -0.934% | -1.061% | -33.79 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 903.97 € (-2.19%) | 115 | 3 | 25% | -0.046% | -0.773% | -0.899% | -20.35 € |
| macd_momentum | 875.27 € (-5.30%) | 317 | 4 | 16% | -0.109% | -0.691% | -0.801% | -49.42 € |
| estocastico_rebote | 888.62 € (-3.85%) | 208 | 9 | 35% | -0.102% | -0.728% | -0.860% | -34.52 € |
| ruptura_estricta | 903.38 € (-2.26%) | 70 | 10 | 23% | -0.383% | -1.256% | -1.396% | -20.15 € |
| macd_sin_salida | 890.85 € (-3.61%) | 180 | 28 | 29% | -0.135% | -0.780% | -0.907% | -31.97 € |
| c_banda_atr_tope | 910.21 € (-1.52%) | 38 | 3 | 18% | -0.461% | -1.561% | -1.694% | -13.63 € |
| ruptura_volumen_tope | 909.06 € (-1.64%) | 60 | 2 | 17% | -0.164% | -1.104% | -1.225% | -15.20 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.46 € (-4.20%) | 201 | 1 | 14% | -0.220% | -0.850% | -0.964% | -38.77 € |
| ruptura_volumen_regimen | 897.11 € (-2.94%) | 118 | 8 | 18% | -0.255% | -0.976% | -1.105% | -26.29 € |
| c_banda_atr_evento | 898.79 € (-2.75%) | 94 | 27 | 24% | -0.332% | -1.113% | -1.250% | -23.97 € |
| macd_momentum_evento | 887.57 € (-3.97%) | 197 | 4 | 13% | -0.195% | -0.829% | -0.935% | -37.11 € |
| ruptura_volumen_evento | 895.03 € (-3.16%) | 100 | 17 | 11% | -0.475% | -1.239% | -1.367% | -28.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 06:20 | macd_momentum_evento | TRUMP | momentum perdido | -1.15% | -1.65% | -0.37 |
| 2026-09-30 06:20 | macd_momentum_evento | ENA | momentum perdido | -0.78% | -1.28% | -0.28 |
| 2026-09-30 06:20 | macd_momentum_evento | DOGE | momentum perdido | -0.14% | -0.64% | -0.14 |
| 2026-09-30 06:20 | macd_momentum_evento | XLM | momentum perdido | -0.52% | -1.02% | -0.23 |
| 2026-09-30 06:20 | macd_momentum_evento | ADA | momentum perdido | -0.52% | -1.02% | -0.23 |
| 2026-09-30 06:20 | macd_momentum_evento | XRP | momentum perdido | +0.23% | -0.27% | -0.06 |
| 2026-09-30 06:20 | macd_momentum_regimen | TRUMP | momentum perdido | -1.15% | -1.65% | -0.37 |
| 2026-09-30 06:20 | estocastico_rebote | ZEC | timeout | -1.12% | -1.62% | -0.36 |
| 2026-09-30 06:20 | macd_momentum | TRUMP | momentum perdido | -1.15% | -1.65% | -0.36 |
| 2026-09-30 06:20 | macd_momentum | ENA | momentum perdido | -0.78% | -1.28% | -0.28 |
| 2026-09-30 06:20 | macd_momentum | DOGE | momentum perdido | -0.14% | -0.64% | -0.14 |
| 2026-09-30 06:20 | macd_momentum | XLM | momentum perdido | -0.52% | -1.02% | -0.22 |
| 2026-09-30 06:20 | macd_momentum | ADA | momentum perdido | -0.52% | -1.02% | -0.23 |
| 2026-09-30 06:20 | macd_momentum | XRP | momentum perdido | +0.23% | -0.27% | -0.06 |
| 2026-09-30 06:15 | ruptura_volumen_evento | KAS | timeout | +0.21% | -0.29% | -0.07 |

## Eventos de la última vuelta

- 2026-09-30 06:15 [reversion_bb] ENTRADA BTC @ 73221.6 (22.92 €, apertura)
- 2026-09-30 06:20 [macd_momentum] CIERRE XRP momentum perdido bruto +0.23% neto -0.27%
- 2026-09-30 06:20 [macd_momentum_evento] CIERRE XRP momentum perdido bruto +0.23% neto -0.27%
- 2026-09-30 06:20 [estocastico_rebote] CIERRE ZEC timeout bruto -1.12% neto -1.62%
- 2026-09-30 06:20 [macd_momentum] CIERRE ADA momentum perdido bruto -0.52% neto -1.02%
- 2026-09-30 06:20 [macd_momentum_evento] CIERRE ADA momentum perdido bruto -0.52% neto -1.02%
- 2026-09-30 06:20 [macd_momentum] CIERRE XLM momentum perdido bruto -0.52% neto -1.02%
- 2026-09-30 06:20 [macd_momentum_evento] CIERRE XLM momentum perdido bruto -0.52% neto -1.02%
- 2026-09-30 06:20 [macd_momentum] CIERRE DOGE momentum perdido bruto -0.14% neto -0.64%
- 2026-09-30 06:20 [macd_momentum_evento] CIERRE DOGE momentum perdido bruto -0.14% neto -0.64%
- 2026-09-30 06:20 [macd_momentum] CIERRE ENA momentum perdido bruto -0.78% neto -1.28%
- 2026-09-30 06:20 [macd_momentum_evento] CIERRE ENA momentum perdido bruto -0.78% neto -1.28%
- 2026-09-30 06:15 [estocastico_rebote] ENTRADA RENDER @ 1.702 (22.24 €, apertura)
- 2026-09-30 06:15 [estocastico_rebote] ENTRADA NIGHT @ 0.02793 (22.24 €, apertura)
- 2026-09-30 06:20 [macd_momentum] CIERRE TRUMP momentum perdido bruto -1.15% neto -1.65%
- 2026-09-30 06:20 [macd_momentum_regimen] CIERRE TRUMP momentum perdido bruto -1.15% neto -1.65%
- 2026-09-30 06:20 [macd_momentum_evento] CIERRE TRUMP momentum perdido bruto -1.15% neto -1.65%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
