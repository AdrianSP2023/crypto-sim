# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 06:26 UTC · vueltas 224 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 894.65 € (-3.20%) | 126 | 27 | 28% | -0.230% | -0.937% | -1.072% | -27.03 € |
| reversion_bb | 916.21 € (-0.87%) | 35 | 8 | 46% | +0.183% | -0.917% | -1.027% | -7.39 € |
| ruptura_volumen | 888.69 € (-3.85%) | 160 | 16 | 19% | -0.265% | -0.928% | -1.056% | -33.80 € |
| rebote_extremo | 922.73 € (-0.16%) | 7 | 1 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.08 € (-2.18%) | 115 | 4 | 25% | -0.046% | -0.773% | -0.899% | -20.35 € |
| macd_momentum | 875.07 € (-5.32%) | 318 | 3 | 16% | -0.106% | -0.688% | -0.797% | -49.34 € |
| estocastico_rebote | 888.44 € (-3.87%) | 209 | 9 | 35% | -0.109% | -0.734% | -0.867% | -34.97 € |
| ruptura_estricta | 902.97 € (-2.30%) | 70 | 10 | 23% | -0.383% | -1.256% | -1.396% | -20.15 € |
| macd_sin_salida | 890.02 € (-3.70%) | 180 | 28 | 29% | -0.135% | -0.780% | -0.907% | -31.97 € |
| c_banda_atr_tope | 909.98 € (-1.54%) | 38 | 3 | 18% | -0.461% | -1.561% | -1.694% | -13.63 € |
| ruptura_volumen_tope | 908.88 € (-1.66%) | 60 | 2 | 17% | -0.164% | -1.104% | -1.225% | -15.20 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.45 € (-4.20%) | 201 | 1 | 14% | -0.220% | -0.850% | -0.964% | -38.77 € |
| ruptura_volumen_regimen | 896.80 € (-2.97%) | 118 | 8 | 18% | -0.255% | -0.976% | -1.105% | -26.29 € |
| c_banda_atr_evento | 897.70 € (-2.87%) | 94 | 27 | 24% | -0.332% | -1.113% | -1.250% | -23.97 € |
| macd_momentum_evento | 887.37 € (-3.99%) | 198 | 3 | 13% | -0.190% | -0.823% | -0.929% | -37.03 € |
| ruptura_volumen_evento | 894.16 € (-3.25%) | 101 | 16 | 11% | -0.466% | -1.228% | -1.357% | -28.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 06:25 | ruptura_volumen_evento | VIRTUAL | timeout | +0.46% | -0.04% | -0.01 |
| 2026-09-30 06:25 | macd_momentum_evento | CRV | momentum perdido | +0.88% | +0.38% | +0.09 |
| 2026-09-30 06:25 | estocastico_rebote | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:25 | macd_momentum | CRV | momentum perdido | +0.88% | +0.38% | +0.08 |
| 2026-09-30 06:25 | ruptura_volumen | VIRTUAL | timeout | +0.46% | -0.04% | -0.01 |
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

## Eventos de la última vuelta

- 2026-09-30 06:20 [pullback_tendencia] ENTRADA QNT @ 257.52 (22.60 €, apertura)
- 2026-09-30 06:20 [reversion_bb] ENTRADA ZEC @ 1231.37 (22.92 €, apertura)
- 2026-09-30 06:25 [macd_momentum] CIERRE CRV momentum perdido bruto +0.88% neto +0.38%
- 2026-09-30 06:25 [macd_momentum_evento] CIERRE CRV momentum perdido bruto +0.88% neto +0.38%
- 2026-09-30 06:25 [ruptura_volumen] CIERRE VIRTUAL timeout bruto +0.46% neto -0.04%
- 2026-09-30 06:25 [ruptura_volumen_evento] CIERRE VIRTUAL timeout bruto +0.46% neto -0.04%
- 2026-09-30 06:20 [rebote_extremo] ENTRADA NIGHT @ 0.02751 (23.07 €, apertura)
- 2026-09-30 06:25 [estocastico_rebote] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:20 [estocastico_rebote] ENTRADA TON @ 1.315 (22.23 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
