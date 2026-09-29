# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 11:16 UTC · vueltas 20 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 923.25 € (-0.11%) | 1 | 10 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| reversion_bb | 924.19 € (-0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen | 921.25 € (-0.32%) | 6 | 12 | 17% | -0.602% | -1.702% | -1.846% | -2.36 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 921.29 € (-0.32%) | 6 | 10 | 0% | -1.000% | -2.100% | -2.225% | -2.91 € |
| macd_momentum | 912.17 € (-1.31%) | 40 | 3 | 5% | -0.258% | -1.358% | -1.475% | -12.54 € |
| estocastico_rebote | 923.73 € (-0.05%) | 3 | 36 | 67% | +0.701% | -0.399% | -0.587% | -0.28 € |
| ruptura_estricta | 922.47 € (-0.19%) | 1 | 12 | 0% | -2.000% | -3.100% | -3.312% | -0.72 € |
| macd_sin_salida | 919.48 € (-0.52%) | 7 | 34 | 43% | -0.020% | -1.120% | -1.326% | -1.81 € |
| c_banda_atr_tope | 923.57 € (-0.07%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 923.03 € (-0.13%) | 2 | 5 | 0% | -1.238% | -2.338% | -2.482% | -1.08 € |
| c_banda_atr_regimen | 923.25 € (-0.11%) | 1 | 10 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| macd_momentum_regimen | 912.17 € (-1.31%) | 40 | 3 | 5% | -0.258% | -1.358% | -1.475% | -12.54 € |
| ruptura_volumen_regimen | 921.25 € (-0.32%) | 6 | 12 | 17% | -0.602% | -1.702% | -1.846% | -2.36 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 11:15 | ruptura_volumen_regimen | NIGHT | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 11:15 | ruptura_volumen_regimen | JUP | stop-loss | -1.24% | -2.34% | -0.54 |
| 2026-09-29 11:15 | ruptura_volumen_regimen | ONDO | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 11:15 | estocastico_rebote | PUMP | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-29 11:15 | ruptura_volumen | NIGHT | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 11:15 | ruptura_volumen | JUP | stop-loss | -1.24% | -2.34% | -0.54 |
| 2026-09-29 11:15 | ruptura_volumen | ONDO | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 11:10 | macd_momentum_regimen | MINA | momentum perdido | +0.59% | -0.51% | -0.12 |
| 2026-09-29 11:10 | macd_sin_salida | TON | stop-loss | -1.64% | -2.74% | -0.63 |
| 2026-09-29 11:10 | macd_momentum | MINA | momentum perdido | +0.59% | -0.51% | -0.12 |
| 2026-09-29 11:00 | macd_momentum_regimen | QNT | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 11:00 | macd_sin_salida | QNT | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 11:00 | macd_momentum | QNT | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 11:00 | pullback_tendencia | QNT | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 10:55 | macd_momentum_regimen | VIRTUAL | momentum perdido | -0.04% | -1.14% | -0.26 |

## Eventos de la última vuelta

- 2026-09-29 11:10 [estocastico_rebote] ENTRADA BTC @ 74061.2 (23.10 €, apertura)
- 2026-09-29 11:10 [pullback_tendencia] ENTRADA NEAR @ 4.2054 (23.03 €, apertura)
- 2026-09-29 11:10 [c_banda_atr] ENTRADA XLM @ 0.202859 (23.11 €, apertura)
- 2026-09-29 11:10 [c_banda_atr_regimen] ENTRADA XLM @ 0.202859 (23.11 €, apertura)
- 2026-09-29 11:15 [estocastico_rebote] CIERRE PUMP take-profit bruto +1.80% neto +0.70%
- 2026-09-29 11:15 [ruptura_volumen] CIERRE ONDO stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 11:15 [ruptura_volumen_regimen] CIERRE ONDO stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 11:15 [ruptura_volumen] CIERRE JUP stop-loss bruto -1.24% neto -2.34%
- 2026-09-29 11:15 [ruptura_volumen_regimen] CIERRE JUP stop-loss bruto -1.24% neto -2.34%
- 2026-09-29 11:15 [ruptura_volumen] CIERRE NIGHT take-profit bruto +2.50% neto +1.40%
- 2026-09-29 11:15 [ruptura_volumen_regimen] CIERRE NIGHT take-profit bruto +2.50% neto +1.40%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
