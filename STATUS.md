# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 18:16 UTC · vueltas 44 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.82 € (-1.56%) | 43 | 9 | 30% | -0.331% | -1.389% | -1.543% | -13.77 € |
| reversion_bb | 923.42 € (-0.09%) | 4 | 5 | 75% | +0.750% | -0.350% | -0.460% | -0.33 € |
| ruptura_volumen | 899.40 € (-2.69%) | 71 | 2 | 14% | -0.684% | -1.552% | -1.691% | -25.28 € |
| rebote_extremo | 923.90 € (-0.04%) | 2 | 0 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 906.73 € (-1.89%) | 52 | 2 | 15% | -0.434% | -1.436% | -1.573% | -17.14 € |
| macd_momentum | 911.13 € (-1.42%) | 68 | 3 | 31% | +0.035% | -0.849% | -0.988% | -13.30 € |
| estocastico_rebote | 911.73 € (-1.35%) | 76 | 33 | 46% | +0.244% | -0.600% | -0.739% | -10.57 € |
| ruptura_estricta | 900.51 € (-2.57%) | 43 | 3 | 9% | -1.345% | -2.438% | -2.588% | -24.15 € |
| macd_sin_salida | 906.80 € (-1.89%) | 63 | 4 | 33% | -0.294% | -1.208% | -1.348% | -17.55 € |
| c_banda_atr_tope | 922.20 € (-0.22%) | 10 | 5 | 50% | +0.251% | -0.849% | -1.019% | -1.96 € |
| ruptura_volumen_tope | 918.83 € (-0.59%) | 17 | 0 | 24% | -0.279% | -1.379% | -1.470% | -5.41 € |
| c_banda_atr_regimen | 909.80 € (-1.56%) | 40 | 5 | 28% | -0.418% | -1.518% | -1.671% | -14.00 € |
| macd_momentum_regimen | 911.45 € (-1.38%) | 59 | 1 | 31% | +0.004% | -0.938% | -1.077% | -12.76 € |
| ruptura_volumen_regimen | 898.77 € (-2.76%) | 70 | 2 | 13% | -0.741% | -1.614% | -1.754% | -25.91 € |
| c_banda_atr_evento | 920.11 € (-0.45%) | 10 | 9 | 30% | -0.477% | -1.577% | -1.709% | -3.64 € |
| macd_momentum_evento | 919.35 € (-0.53%) | 21 | 3 | 29% | +0.051% | -1.049% | -1.191% | -5.08 € |
| ruptura_volumen_evento | 915.36 € (-0.96%) | 21 | 2 | 10% | -0.821% | -1.921% | -2.034% | -9.32 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 18:10 | macd_sin_salida | VVV | stop-loss | -2.31% | -2.81% | -0.64 |
| 2026-09-30 18:10 | estocastico_rebote | ENA | stop-loss | -1.65% | -2.15% | -0.49 |
| 2026-09-30 18:10 | estocastico_rebote | NEAR | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 18:10 | pullback_tendencia | QNT | rotura de tendencia | -1.35% | -1.85% | -0.42 |
| 2026-09-30 18:05 | ruptura_volumen_evento | JUP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 18:05 | ruptura_volumen_evento | NIGHT | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 18:05 | ruptura_volumen_evento | ONDO | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 18:05 | ruptura_volumen_evento | PUMP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 18:05 | macd_momentum_evento | AVAX | momentum perdido | -0.31% | -1.41% | -0.32 |
| 2026-09-30 18:05 | c_banda_atr_evento | KAS | stop-loss | -1.53% | -2.63% | -0.61 |
| 2026-09-30 18:05 | c_banda_atr_evento | OP | stop-loss | -1.63% | -2.73% | -0.63 |
| 2026-09-30 18:05 | ruptura_volumen_regimen | JUP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 18:05 | ruptura_volumen_regimen | ONDO | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 18:05 | ruptura_volumen_regimen | PUMP | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 18:05 | macd_momentum_regimen | AVAX | momentum perdido | -0.31% | -0.81% | -0.18 |

## Eventos de la última vuelta

- 2026-09-30 18:10 [estocastico_rebote] ENTRADA USELESS @ 0.21624 (22.84 €, apertura)
- 2026-09-30 18:10 [c_banda_atr] ENTRADA XMR @ 481.1 (22.76 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
