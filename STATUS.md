# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 15:52 UTC · vueltas 74 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.59 € (-1.48%) | 49 | 2 | 33% | -0.200% | -1.227% | -1.362% | -13.87 € |
| reversion_bb | 922.31 € (-0.21%) | 5 | 10 | 20% | -0.900% | -2.000% | -2.120% | -2.31 € |
| ruptura_volumen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| rebote_extremo | 923.83 € (-0.04%) | 1 | 2 | 0% | -1.619% | -2.719% | -2.843% | -0.63 € |
| pullback_tendencia | 909.47 € (-1.60%) | 65 | 2 | 26% | -0.086% | -0.988% | -1.102% | -14.75 € |
| macd_momentum | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| estocastico_rebote | 907.15 € (-1.85%) | 92 | 40 | 36% | -0.109% | -0.892% | -1.020% | -18.92 € |
| ruptura_estricta | 914.13 € (-1.09%) | 37 | 4 | 32% | -0.049% | -1.149% | -1.275% | -9.80 € |
| macd_sin_salida | 905.74 € (-2.00%) | 93 | 0 | 31% | -0.086% | -0.867% | -0.991% | -18.50 € |
| c_banda_atr_tope | 916.96 € (-0.79%) | 17 | 1 | 18% | -0.831% | -1.931% | -2.096% | -7.57 € |
| ruptura_volumen_tope | 919.64 € (-0.50%) | 20 | 0 | 20% | +0.103% | -0.997% | -1.127% | -4.60 € |
| c_banda_atr_regimen | 910.30 € (-1.51%) | 49 | 1 | 33% | -0.200% | -1.227% | -1.362% | -13.87 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| c_banda_atr_evento | 917.76 € (-0.70%) | 16 | 3 | 25% | -0.658% | -1.758% | -1.914% | -6.50 € |
| macd_momentum_evento | 913.78 € (-1.13%) | 27 | 0 | 15% | -0.576% | -1.676% | -1.793% | -10.46 € |
| ruptura_volumen_evento | 920.19 € (-0.44%) | 10 | 0 | 20% | -0.654% | -1.754% | -1.962% | -4.05 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 15:50 | estocastico_rebote | POL | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-29 15:50 | rebote_extremo | VVV | timeout | -1.62% | -2.72% | -0.63 |
| 2026-09-29 15:50 | reversion_bb | JUP | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-09-29 15:40 | estocastico_rebote | HYPE | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 15:35 | c_banda_atr_regimen | BNB | timeout | -1.20% | -2.00% | -0.46 |
| 2026-09-29 15:35 | c_banda_atr_regimen | SOL | timeout | -1.07% | -1.87% | -0.43 |
| 2026-09-29 15:35 | c_banda_atr | BNB | timeout | -1.20% | -2.00% | -0.46 |
| 2026-09-29 15:35 | c_banda_atr | SOL | timeout | -1.07% | -1.87% | -0.43 |
| 2026-09-29 15:30 | ruptura_volumen_evento | XPL | stop-loss | -1.58% | -2.68% | -0.62 |
| 2026-09-29 15:30 | macd_momentum_evento | XPL | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 15:30 | c_banda_atr_evento | ATOM | stop-loss | -1.59% | -2.69% | -0.62 |
| 2026-09-29 15:30 | c_banda_atr_evento | LTC | stop-loss | -1.51% | -2.61% | -0.60 |
| 2026-09-29 15:30 | ruptura_volumen_regimen | XPL | stop-loss | -1.58% | -2.08% | -0.47 |
| 2026-09-29 15:30 | ruptura_volumen_regimen | NEAR | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 15:30 | macd_momentum_regimen | XPL | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-29 15:45 [pullback_tendencia] ENTRADA NEAR @ 4.3801 (22.74 €, apertura)
- 2026-09-29 15:50 [reversion_bb] CIERRE JUP take-profit bruto +1.50% neto +0.40%
- 2026-09-29 15:50 [rebote_extremo] CIERRE VVV timeout bruto -1.62% neto -2.72%
- 2026-09-29 15:45 [estocastico_rebote] ENTRADA ZRO @ 1.471 (20.75 €, apertura)
- 2026-09-29 15:50 [estocastico_rebote] CIERRE POL take-profit bruto +1.80% neto +1.30%
- 2026-09-29 15:45 [estocastico_rebote] ENTRADA XPL @ 0.0869 (22.63 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
