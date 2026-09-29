# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 11:11 UTC · vueltas 19 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 923.55 € (-0.07%) | 1 | 9 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| reversion_bb | 924.20 € (-0.00%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen | 921.79 € (-0.27%) | 3 | 15 | 0% | -1.225% | -2.325% | -2.449% | -1.61 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 921.12 € (-0.34%) | 6 | 9 | 0% | -1.000% | -2.100% | -2.225% | -2.91 € |
| macd_momentum | 911.97 € (-1.33%) | 40 | 3 | 5% | -0.258% | -1.358% | -1.475% | -12.54 € |
| estocastico_rebote | 924.10 € (-0.01%) | 2 | 36 | 50% | +0.150% | -0.950% | -1.119% | -0.44 € |
| ruptura_estricta | 922.31 € (-0.21%) | 1 | 12 | 0% | -2.000% | -3.100% | -3.312% | -0.72 € |
| macd_sin_salida | 920.00 € (-0.46%) | 7 | 34 | 43% | -0.020% | -1.120% | -1.326% | -1.81 € |
| c_banda_atr_tope | 923.71 € (-0.06%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 922.85 € (-0.15%) | 2 | 5 | 0% | -1.238% | -2.338% | -2.482% | -1.08 € |
| c_banda_atr_regimen | 923.55 € (-0.07%) | 1 | 9 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| macd_momentum_regimen | 911.97 € (-1.33%) | 40 | 3 | 5% | -0.258% | -1.358% | -1.475% | -12.54 € |
| ruptura_volumen_regimen | 921.79 € (-0.27%) | 3 | 15 | 0% | -1.225% | -2.325% | -2.449% | -1.61 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 11:10 | macd_momentum_regimen | MINA | momentum perdido | +0.59% | -0.51% | -0.12 |
| 2026-09-29 11:10 | macd_sin_salida | TON | stop-loss | -1.64% | -2.74% | -0.63 |
| 2026-09-29 11:10 | macd_momentum | MINA | momentum perdido | +0.59% | -0.51% | -0.12 |
| 2026-09-29 11:00 | macd_momentum_regimen | QNT | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 11:00 | macd_sin_salida | QNT | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 11:00 | macd_momentum | QNT | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 11:00 | pullback_tendencia | QNT | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 10:55 | macd_momentum_regimen | VIRTUAL | momentum perdido | -0.04% | -1.14% | -0.26 |
| 2026-09-29 10:55 | macd_momentum | VIRTUAL | momentum perdido | -0.04% | -1.14% | -0.26 |
| 2026-09-29 10:50 | ruptura_volumen_regimen | SPX | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 10:50 | macd_momentum_regimen | NIGHT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 10:50 | macd_sin_salida | NIGHT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 10:50 | macd_momentum | NIGHT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 10:50 | ruptura_volumen | SPX | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 10:45 | ruptura_volumen_regimen | PENGU | stop-loss | -1.28% | -2.38% | -0.55 |

## Eventos de la última vuelta

- 2026-09-29 11:05 [macd_momentum] ENTRADA PUMP @ 0.004474 (22.80 €, apertura)
- 2026-09-29 11:05 [macd_sin_salida] ENTRADA PUMP @ 0.004474 (23.08 €, apertura)
- 2026-09-29 11:05 [macd_momentum_regimen] ENTRADA PUMP @ 0.004474 (22.80 €, apertura)
- 2026-09-29 11:10 [macd_momentum] CIERRE MINA momentum perdido bruto +0.59% neto -0.51%
- 2026-09-29 11:10 [macd_momentum_regimen] CIERRE MINA momentum perdido bruto +0.59% neto -0.51%
- 2026-09-29 11:10 [macd_sin_salida] CIERRE TON stop-loss bruto -1.64% neto -2.74%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
