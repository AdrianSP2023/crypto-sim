# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 18:31 UTC · vueltas 47 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.64 € (-1.58%) | 43 | 9 | 30% | -0.331% | -1.389% | -1.543% | -13.77 € |
| reversion_bb | 923.34 € (-0.10%) | 4 | 5 | 75% | +0.750% | -0.350% | -0.460% | -0.33 € |
| ruptura_volumen | 899.22 € (-2.71%) | 72 | 1 | 14% | -0.670% | -1.532% | -1.672% | -25.31 € |
| rebote_extremo | 923.90 € (-0.04%) | 2 | 0 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 907.41 € (-1.82%) | 52 | 3 | 15% | -0.434% | -1.436% | -1.573% | -17.14 € |
| macd_momentum | 910.68 € (-1.47%) | 70 | 2 | 30% | +0.022% | -0.851% | -0.991% | -13.73 € |
| estocastico_rebote | 911.64 € (-1.36%) | 76 | 36 | 46% | +0.244% | -0.600% | -0.739% | -10.57 € |
| ruptura_estricta | 900.34 € (-2.59%) | 43 | 3 | 9% | -1.345% | -2.438% | -2.588% | -24.15 € |
| macd_sin_salida | 906.57 € (-1.91%) | 63 | 5 | 33% | -0.294% | -1.208% | -1.348% | -17.55 € |
| c_banda_atr_tope | 922.17 € (-0.22%) | 10 | 5 | 50% | +0.251% | -0.849% | -1.019% | -1.96 € |
| ruptura_volumen_tope | 918.83 € (-0.59%) | 17 | 0 | 24% | -0.279% | -1.379% | -1.470% | -5.41 € |
| c_banda_atr_regimen | 909.58 € (-1.59%) | 40 | 5 | 28% | -0.418% | -1.518% | -1.671% | -14.00 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.60 € (-2.77%) | 71 | 1 | 13% | -0.726% | -1.594% | -1.734% | -25.94 € |
| c_banda_atr_evento | 919.93 € (-0.47%) | 10 | 9 | 30% | -0.477% | -1.577% | -1.709% | -3.64 € |
| macd_momentum_evento | 918.62 € (-0.61%) | 23 | 2 | 26% | +0.009% | -1.091% | -1.236% | -5.79 € |
| ruptura_volumen_evento | 915.05 € (-0.99%) | 22 | 1 | 9% | -0.768% | -1.868% | -1.984% | -9.49 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 18:30 | ruptura_volumen_evento | XMR | timeout | +0.35% | -0.75% | -0.17 |
| 2026-09-30 18:30 | ruptura_volumen_regimen | XMR | timeout | +0.35% | -0.15% | -0.03 |
| 2026-09-30 18:30 | ruptura_volumen | XMR | timeout | +0.35% | -0.15% | -0.03 |
| 2026-09-30 18:25 | macd_momentum_evento | TON | momentum perdido | -0.30% | -1.40% | -0.32 |
| 2026-09-30 18:25 | macd_momentum_evento | XDC | momentum perdido | -0.56% | -1.66% | -0.38 |
| 2026-09-30 18:25 | macd_momentum_regimen | XDC | momentum perdido | -0.56% | -1.06% | -0.24 |
| 2026-09-30 18:25 | macd_momentum | TON | momentum perdido | -0.30% | -0.80% | -0.18 |
| 2026-09-30 18:25 | macd_momentum | XDC | momentum perdido | -0.56% | -1.06% | -0.24 |
| 2026-09-30 18:10 | macd_sin_salida | VVV | stop-loss | -2.31% | -2.81% | -0.64 |
| 2026-09-30 18:10 | estocastico_rebote | ENA | stop-loss | -1.65% | -2.15% | -0.49 |
| 2026-09-30 18:10 | estocastico_rebote | NEAR | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 18:10 | pullback_tendencia | QNT | rotura de tendencia | -1.35% | -1.85% | -0.42 |
| 2026-09-30 18:05 | ruptura_volumen_evento | JUP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 18:05 | ruptura_volumen_evento | NIGHT | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 18:05 | ruptura_volumen_evento | ONDO | stop-loss | -1.20% | -2.30% | -0.53 |

## Eventos de la última vuelta

- 2026-09-30 18:25 [estocastico_rebote] ENTRADA QNT @ 261.76 (22.84 €, apertura)
- 2026-09-30 18:25 [macd_momentum] ENTRADA ALGO @ 0.11106 (22.76 €, apertura)
- 2026-09-30 18:25 [macd_sin_salida] ENTRADA ALGO @ 0.11106 (22.67 €, apertura)
- 2026-09-30 18:25 [macd_momentum_evento] ENTRADA ALGO @ 0.11106 (22.96 €, apertura)
- 2026-09-30 18:25 [estocastico_rebote] ENTRADA JUP @ 0.29091 (22.84 €, apertura)
- 2026-09-30 18:30 [ruptura_volumen] CIERRE XMR timeout bruto +0.35% neto -0.15%
- 2026-09-30 18:30 [ruptura_volumen_regimen] CIERRE XMR timeout bruto +0.35% neto -0.15%
- 2026-09-30 18:30 [ruptura_volumen_evento] CIERRE XMR timeout bruto +0.35% neto -0.75%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
