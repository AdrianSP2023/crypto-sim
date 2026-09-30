# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 20:01 UTC · vueltas 65 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.12 € (-1.85%) | 48 | 18 | 27% | -0.388% | -1.419% | -1.570% | -15.69 € |
| reversion_bb | 922.47 € (-0.19%) | 7 | 5 | 57% | +0.214% | -0.886% | -1.014% | -1.44 € |
| ruptura_volumen | 898.30 € (-2.81%) | 74 | 4 | 14% | -0.665% | -1.518% | -1.656% | -25.76 € |
| rebote_extremo | 924.27 € (+0.00%) | 2 | 1 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 905.32 € (-2.05%) | 57 | 1 | 14% | -0.483% | -1.446% | -1.583% | -18.90 € |
| macd_momentum | 908.51 € (-1.70%) | 79 | 3 | 27% | -0.026% | -0.856% | -0.992% | -15.57 € |
| estocastico_rebote | 904.21 € (-2.17%) | 96 | 24 | 38% | -0.056% | -0.828% | -0.961% | -18.31 € |
| ruptura_estricta | 898.90 € (-2.74%) | 45 | 3 | 9% | -1.346% | -2.426% | -2.575% | -25.13 € |
| macd_sin_salida | 904.91 € (-2.09%) | 64 | 11 | 33% | -0.313% | -1.221% | -1.360% | -18.01 € |
| c_banda_atr_tope | 921.40 € (-0.31%) | 13 | 5 | 38% | +0.095% | -1.005% | -1.154% | -3.02 € |
| ruptura_volumen_tope | 918.12 € (-0.66%) | 18 | 4 | 22% | -0.331% | -1.431% | -1.522% | -5.94 € |
| c_banda_atr_regimen | 909.03 € (-1.65%) | 42 | 3 | 26% | -0.472% | -1.572% | -1.727% | -15.21 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 917.03 € (-0.78%) | 15 | 18 | 20% | -0.611% | -1.711% | -1.842% | -5.93 € |
| macd_momentum_evento | 915.19 € (-0.98%) | 32 | 3 | 19% | -0.106% | -1.206% | -1.338% | -8.88 € |
| ruptura_volumen_evento | 913.83 € (-1.13%) | 24 | 4 | 8% | -0.746% | -1.846% | -1.960% | -10.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 20:00 | macd_momentum_evento | TON | momentum perdido | -0.22% | -1.32% | -0.30 |
| 2026-09-30 20:00 | macd_momentum_evento | XLM | momentum perdido | +0.15% | -0.95% | -0.22 |
| 2026-09-30 20:00 | estocastico_rebote | JUP | stop-loss | -1.60% | -2.10% | -0.48 |
| 2026-09-30 20:00 | estocastico_rebote | TRX | timeout | +0.11% | -0.39% | -0.09 |
| 2026-09-30 20:00 | macd_momentum | TON | momentum perdido | -0.22% | -0.72% | -0.16 |
| 2026-09-30 20:00 | macd_momentum | XLM | momentum perdido | +0.15% | -0.35% | -0.08 |
| 2026-09-30 19:55 | estocastico_rebote | SPX | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 19:55 | estocastico_rebote | DASH | stop-loss | -1.56% | -2.06% | -0.47 |
| 2026-09-30 19:55 | estocastico_rebote | USELESS | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 19:55 | pullback_tendencia | HYPE | rotura de tendencia | -0.47% | -0.97% | -0.22 |
| 2026-09-30 19:55 | pullback_tendencia | NEAR | rotura de tendencia | -1.00% | -1.50% | -0.34 |
| 2026-09-30 19:50 | estocastico_rebote | HBAR | take-profit | +1.80% | +1.30% | +0.30 |
| 2026-09-30 19:45 | reversion_bb | CRV | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-09-30 19:35 | c_banda_atr_evento | ICP | timeout | -0.89% | -1.99% | -0.46 |
| 2026-09-30 19:35 | c_banda_atr_evento | UNI | timeout | +0.54% | -0.56% | -0.13 |

## Eventos de la última vuelta

- 2026-09-30 20:00 [macd_momentum] CIERRE XLM momentum perdido bruto +0.15% neto -0.35%
- 2026-09-30 20:00 [macd_momentum_evento] CIERRE XLM momentum perdido bruto +0.15% neto -0.95%
- 2026-09-30 20:00 [estocastico_rebote] CIERRE TRX timeout bruto +0.11% neto -0.39%
- 2026-09-30 20:00 [estocastico_rebote] CIERRE JUP stop-loss bruto -1.61% neto -2.11%
- 2026-09-30 20:00 [macd_momentum] CIERRE TON momentum perdido bruto -0.22% neto -0.72%
- 2026-09-30 20:00 [macd_momentum_evento] CIERRE TON momentum perdido bruto -0.22% neto -1.32%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
