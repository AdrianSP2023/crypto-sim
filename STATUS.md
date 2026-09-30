# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 03:36 UTC · vueltas 190 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 896.26 € (-3.03%) | 112 | 14 | 27% | -0.286% | -1.020% | -1.155% | -26.16 € |
| reversion_bb | 917.92 € (-0.68%) | 29 | 9 | 48% | +0.205% | -0.895% | -0.997% | -5.98 € |
| ruptura_volumen | 893.19 € (-3.36%) | 147 | 4 | 20% | -0.245% | -0.923% | -1.049% | -30.92 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.93 € (-2.09%) | 109 | 0 | 26% | -0.034% | -0.773% | -0.900% | -19.31 € |
| macd_momentum | 880.81 € (-4.70%) | 268 | 1 | 17% | -0.118% | -0.715% | -0.827% | -43.42 € |
| estocastico_rebote | 889.09 € (-3.80%) | 188 | 17 | 34% | -0.129% | -0.768% | -0.900% | -32.97 € |
| ruptura_estricta | 904.18 € (-2.17%) | 65 | 4 | 25% | -0.348% | -1.249% | -1.393% | -18.63 € |
| macd_sin_salida | 892.53 € (-3.43%) | 160 | 12 | 29% | -0.160% | -0.823% | -0.949% | -30.04 € |
| c_banda_atr_tope | 909.96 € (-1.55%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.25 € (-1.51%) | 52 | 2 | 17% | -0.153% | -1.161% | -1.284% | -13.86 € |
| c_banda_atr_regimen | 900.61 € (-2.56%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 898.98 € (-2.73%) | 112 | 4 | 19% | -0.249% | -0.982% | -1.112% | -25.12 € |
| c_banda_atr_evento | 899.31 € (-2.70%) | 80 | 14 | 22% | -0.429% | -1.259% | -1.397% | -23.10 € |
| macd_momentum_evento | 893.20 € (-3.36%) | 148 | 1 | 13% | -0.241% | -0.919% | -1.028% | -31.03 € |
| ruptura_volumen_evento | 898.69 € (-2.76%) | 88 | 4 | 12% | -0.462% | -1.262% | -1.389% | -25.41 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 03:35 | macd_momentum_evento | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 03:35 | macd_sin_salida | SPX | timeout | +0.81% | +0.31% | +0.07 |
| 2026-09-30 03:35 | macd_sin_salida | JUP | timeout | -1.05% | -1.55% | -0.35 |
| 2026-09-30 03:35 | macd_sin_salida | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 03:35 | estocastico_rebote | JUP | timeout | -1.05% | -1.55% | -0.34 |
| 2026-09-30 03:35 | estocastico_rebote | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 03:35 | macd_momentum | QNT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-09-30 03:30 | ruptura_volumen_evento | SHIB | timeout | -1.13% | -1.63% | -0.37 |
| 2026-09-30 03:30 | ruptura_volumen_evento | CRV | stop-loss | -1.44% | -1.94% | -0.44 |
| 2026-09-30 03:30 | ruptura_volumen_evento | HBAR | timeout | +0.10% | -0.40% | -0.09 |
| 2026-09-30 03:30 | ruptura_volumen_regimen | SHIB | timeout | -1.13% | -1.63% | -0.37 |
| 2026-09-30 03:30 | ruptura_volumen_regimen | HBAR | timeout | +0.10% | -0.40% | -0.09 |
| 2026-09-30 03:30 | ruptura_volumen_tope | CRV | stop-loss | -1.44% | -1.94% | -0.44 |
| 2026-09-30 03:30 | macd_sin_salida | SEI | timeout | -0.37% | -0.87% | -0.20 |
| 2026-09-30 03:30 | estocastico_rebote | PUMP | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-30 03:30 [macd_momentum] ENTRADA QNT @ 258.9 (22.03 €, apertura)
- 2026-09-30 03:35 [macd_momentum] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 03:35 [estocastico_rebote] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 03:30 [macd_sin_salida] ENTRADA QNT @ 258.9 (22.37 €, apertura)
- 2026-09-30 03:35 [macd_sin_salida] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 03:30 [macd_momentum_evento] ENTRADA QNT @ 258.9 (22.34 €, apertura)
- 2026-09-30 03:35 [macd_momentum_evento] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 03:35 [estocastico_rebote] CIERRE JUP timeout bruto -1.05% neto -1.55%
- 2026-09-30 03:35 [macd_sin_salida] CIERRE JUP timeout bruto -1.05% neto -1.55%
- 2026-09-30 03:30 [estocastico_rebote] ENTRADA USELESS @ 0.20999 (22.28 €, apertura)
- 2026-09-30 03:30 [estocastico_rebote] ENTRADA SPX @ 0.3722 (22.28 €, apertura)
- 2026-09-30 03:35 [macd_sin_salida] CIERRE SPX timeout bruto +0.81% neto +0.31%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
