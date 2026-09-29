# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 13:06 UTC · vueltas 42 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 924.61 € (+0.04%) | 8 | 25 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 918.16 € (-0.66%) | 34 | 20 | 35% | +0.392% | -0.708% | -0.839% | -5.56 € |
| rebote_extremo | 924.36 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 919.97 € (-0.46%) | 26 | 9 | 38% | +0.382% | -0.718% | -0.833% | -4.31 € |
| macd_momentum | 910.14 € (-1.53%) | 87 | 9 | 18% | +0.043% | -0.757% | -0.873% | -15.18 € |
| estocastico_rebote | 924.93 € (+0.08%) | 25 | 31 | 80% | +1.204% | +0.104% | -0.035% | +0.60 € |
| ruptura_estricta | 920.84 € (-0.37%) | 19 | 14 | 37% | +0.352% | -0.748% | -0.875% | -3.28 € |
| macd_sin_salida | 918.21 € (-0.65%) | 44 | 14 | 41% | +0.466% | -0.545% | -0.668% | -5.54 € |
| c_banda_atr_tope | 924.41 € (+0.02%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 922.56 € (-0.18%) | 10 | 5 | 30% | +0.387% | -0.713% | -0.836% | -1.65 € |
| c_banda_atr_regimen | 924.61 € (+0.04%) | 8 | 25 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| macd_momentum_regimen | 910.14 € (-1.53%) | 87 | 9 | 18% | +0.043% | -0.757% | -0.873% | -15.18 € |
| ruptura_volumen_regimen | 918.16 € (-0.66%) | 34 | 20 | 35% | +0.392% | -0.708% | -0.839% | -5.56 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 13:05 | macd_momentum_regimen | ETH | momentum perdido | +0.70% | +0.20% | +0.05 |
| 2026-09-29 13:05 | macd_sin_salida | GRT | timeout | -1.14% | -1.94% | -0.45 |
| 2026-09-29 13:05 | macd_sin_salida | VIRTUAL | timeout | -0.30% | -1.10% | -0.26 |
| 2026-09-29 13:05 | ruptura_estricta | ZRO | take-profit | +3.00% | +1.90% | +0.44 |
| 2026-09-29 13:05 | ruptura_estricta | XLM | stop-loss | -2.00% | -3.10% | -0.72 |
| 2026-09-29 13:05 | macd_momentum | ETH | momentum perdido | +0.70% | +0.20% | +0.05 |
| 2026-09-29 13:05 | pullback_tendencia | FIL | rotura de tendencia | +0.32% | -0.78% | -0.18 |
| 2026-09-29 13:05 | pullback_tendencia | XLM | rotura de tendencia | -1.10% | -2.20% | -0.51 |
| 2026-09-29 13:00 | macd_momentum_regimen | BNB | momentum perdido | -0.05% | -0.55% | -0.12 |
| 2026-09-29 13:00 | macd_momentum_regimen | TRX | momentum perdido | -0.11% | -0.61% | -0.14 |
| 2026-09-29 13:00 | ruptura_estricta | ONDO | timeout | -1.60% | -2.70% | -0.62 |
| 2026-09-29 13:00 | macd_momentum | BNB | momentum perdido | -0.05% | -0.55% | -0.12 |
| 2026-09-29 13:00 | macd_momentum | TRX | momentum perdido | -0.11% | -0.61% | -0.14 |
| 2026-09-29 12:55 | macd_momentum_regimen | AAVE | momentum perdido | +0.57% | +0.07% | +0.01 |
| 2026-09-29 12:55 | macd_sin_salida | SPX | timeout | +0.22% | -0.58% | -0.13 |

## Eventos de la última vuelta

- 2026-09-29 13:05 [macd_momentum] CIERRE ETH momentum perdido bruto +0.70% neto +0.20%
- 2026-09-29 13:05 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto +0.70% neto +0.20%
- 2026-09-29 13:00 [estocastico_rebote] ENTRADA LTC @ 60.57 (23.12 €, apertura)
- 2026-09-29 13:05 [pullback_tendencia] CIERRE XLM rotura de tendencia bruto -1.10% neto -2.20%
- 2026-09-29 13:05 [ruptura_estricta] CIERRE XLM stop-loss bruto -2.00% neto -3.10%
- 2026-09-29 13:00 [estocastico_rebote] ENTRADA UNI @ 7.9925 (23.12 €, apertura)
- 2026-09-29 13:00 [estocastico_rebote] ENTRADA ARB @ 0.1876 (23.12 €, apertura)
- 2026-09-29 13:00 [macd_momentum] ENTRADA ENA @ 0.225 (22.73 €, apertura)
- 2026-09-29 13:00 [macd_sin_salida] ENTRADA ENA @ 0.225 (22.99 €, apertura)
- 2026-09-29 13:00 [macd_momentum_regimen] ENTRADA ENA @ 0.225 (22.73 €, apertura)
- 2026-09-29 13:00 [estocastico_rebote] ENTRADA WLD @ 0.4421 (23.12 €, apertura)
- 2026-09-29 13:05 [ruptura_estricta] CIERRE ZRO take-profit bruto +3.00% neto +1.90%
- 2026-09-29 13:05 [macd_sin_salida] CIERRE VIRTUAL timeout bruto -0.30% neto -1.10%
- 2026-09-29 13:05 [pullback_tendencia] CIERRE FIL rotura de tendencia bruto +0.32% neto -0.78%
- 2026-09-29 13:05 [macd_sin_salida] CIERRE GRT timeout bruto -1.14% neto -1.94%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
