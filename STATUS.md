# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 06:36 UTC · vueltas 226 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 893.07 € (-3.37%) | 129 | 24 | 27% | -0.260% | -0.962% | -1.096% | -28.40 € |
| reversion_bb | 915.80 € (-0.91%) | 35 | 10 | 46% | +0.183% | -0.917% | -1.027% | -7.39 € |
| ruptura_volumen | 887.61 € (-3.96%) | 165 | 12 | 18% | -0.276% | -0.934% | -1.061% | -35.03 € |
| rebote_extremo | 923.03 € (-0.13%) | 7 | 1 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 903.81 € (-2.21%) | 116 | 3 | 25% | -0.046% | -0.771% | -0.898% | -20.49 € |
| macd_momentum | 874.69 € (-5.36%) | 320 | 1 | 16% | -0.105% | -0.687% | -0.797% | -49.59 € |
| estocastico_rebote | 887.63 € (-3.96%) | 212 | 8 | 34% | -0.124% | -0.747% | -0.880% | -36.09 € |
| ruptura_estricta | 902.77 € (-2.32%) | 70 | 10 | 23% | -0.383% | -1.256% | -1.396% | -20.15 € |
| macd_sin_salida | 888.70 € (-3.85%) | 182 | 26 | 29% | -0.150% | -0.794% | -0.921% | -32.90 € |
| c_banda_atr_tope | 909.65 € (-1.58%) | 39 | 2 | 18% | -0.490% | -1.590% | -1.722% | -14.24 € |
| ruptura_volumen_tope | 908.81 € (-1.67%) | 61 | 2 | 16% | -0.181% | -1.114% | -1.234% | -15.59 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.963% | -38.90 € |
| ruptura_volumen_regimen | 896.27 € (-3.03%) | 119 | 7 | 18% | -0.267% | -0.986% | -1.116% | -26.79 € |
| c_banda_atr_evento | 896.11 € (-3.04%) | 97 | 24 | 24% | -0.369% | -1.141% | -1.277% | -25.35 € |
| macd_momentum_evento | 886.99 € (-4.03%) | 200 | 1 | 13% | -0.189% | -0.821% | -0.927% | -37.29 € |
| ruptura_volumen_evento | 893.07 € (-3.37%) | 106 | 12 | 10% | -0.473% | -1.222% | -1.351% | -29.55 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 06:35 | ruptura_volumen_evento | TRX | timeout | +0.15% | -0.35% | -0.08 |
| 2026-09-30 06:35 | c_banda_atr_evento | POL | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:35 | ruptura_volumen_tope | ICP | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 06:35 | estocastico_rebote | SOL | timeout | -0.93% | -1.43% | -0.32 |
| 2026-09-30 06:35 | ruptura_volumen | TRX | timeout | +0.15% | -0.35% | -0.08 |
| 2026-09-30 06:35 | c_banda_atr | POL | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:30 | ruptura_volumen_evento | SEI | timeout | +0.09% | -0.41% | -0.09 |
| 2026-09-30 06:30 | ruptura_volumen_evento | INJ | stop-loss | -1.31% | -1.81% | -0.41 |
| 2026-09-30 06:30 | ruptura_volumen_evento | MON | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 06:30 | ruptura_volumen_evento | TAO | timeout | -0.78% | -1.28% | -0.29 |
| 2026-09-30 06:30 | macd_momentum_evento | PEPE | momentum perdido | -0.11% | -0.61% | -0.14 |
| 2026-09-30 06:30 | macd_momentum_evento | XDC | momentum perdido | -0.07% | -0.57% | -0.13 |
| 2026-09-30 06:30 | c_banda_atr_evento | ALGO | stop-loss | -1.55% | -2.05% | -0.46 |
| 2026-09-30 06:30 | c_banda_atr_evento | AVAX | stop-loss | -1.53% | -2.03% | -0.46 |
| 2026-09-30 06:30 | ruptura_volumen_regimen | XPL | stop-loss | -1.74% | -2.24% | -0.50 |

## Eventos de la última vuelta

- 2026-09-30 06:35 [estocastico_rebote] CIERRE SOL timeout bruto -0.93% neto -1.43%
- 2026-09-30 06:35 [ruptura_volumen_tope] CIERRE ICP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 06:35 [ruptura_volumen] CIERRE TRX timeout bruto +0.15% neto -0.35%
- 2026-09-30 06:35 [ruptura_volumen_evento] CIERRE TRX timeout bruto +0.15% neto -0.35%
- 2026-09-30 06:30 [estocastico_rebote] ENTRADA SEI @ 0.06528 (22.20 €, apertura)
- 2026-09-30 06:35 [c_banda_atr] CIERRE POL stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:35 [c_banda_atr_evento] CIERRE POL stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:30 [reversion_bb] ENTRADA TRUMP @ 1.795 (22.92 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
