# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 12:56 UTC · vueltas 40 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 924.65 € (+0.04%) | 8 | 25 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 918.29 € (-0.64%) | 34 | 19 | 35% | +0.392% | -0.708% | -0.839% | -5.56 € |
| rebote_extremo | 924.28 € (+0.00%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 920.80 € (-0.37%) | 24 | 11 | 42% | +0.446% | -0.654% | -0.769% | -3.63 € |
| macd_momentum | 910.44 € (-1.49%) | 84 | 11 | 18% | +0.038% | -0.773% | -0.892% | -14.96 € |
| estocastico_rebote | 925.12 € (+0.10%) | 25 | 27 | 80% | +1.204% | +0.104% | -0.035% | +0.60 € |
| ruptura_estricta | 921.74 € (-0.27%) | 16 | 16 | 38% | +0.456% | -0.645% | -0.779% | -2.38 € |
| macd_sin_salida | 918.75 € (-0.59%) | 42 | 15 | 43% | +0.523% | -0.499% | -0.613% | -4.84 € |
| c_banda_atr_tope | 924.44 € (+0.02%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 922.94 € (-0.14%) | 10 | 5 | 30% | +0.387% | -0.713% | -0.836% | -1.65 € |
| c_banda_atr_regimen | 924.65 € (+0.04%) | 8 | 25 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| macd_momentum_regimen | 910.44 € (-1.49%) | 84 | 11 | 18% | +0.038% | -0.773% | -0.892% | -14.96 € |
| ruptura_volumen_regimen | 918.29 € (-0.64%) | 34 | 19 | 35% | +0.392% | -0.708% | -0.839% | -5.56 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 12:55 | macd_momentum_regimen | AAVE | momentum perdido | +0.57% | +0.07% | +0.01 |
| 2026-09-29 12:55 | macd_sin_salida | SPX | timeout | +0.22% | -0.58% | -0.13 |
| 2026-09-29 12:55 | macd_sin_salida | BNB | timeout | -0.10% | -0.90% | -0.21 |
| 2026-09-29 12:55 | macd_sin_salida | HYPE | timeout | -0.43% | -1.24% | -0.28 |
| 2026-09-29 12:55 | ruptura_estricta | DOGE | timeout | +0.21% | -0.89% | -0.20 |
| 2026-09-29 12:55 | ruptura_estricta | SUI | timeout | +0.54% | -0.56% | -0.13 |
| 2026-09-29 12:55 | ruptura_estricta | XRP | timeout | +2.55% | +1.45% | +0.34 |
| 2026-09-29 12:55 | estocastico_rebote | TRUMP | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-29 12:55 | macd_momentum | AAVE | momentum perdido | +0.57% | +0.07% | +0.01 |
| 2026-09-29 12:55 | pullback_tendencia | NIGHT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 12:50 | ruptura_volumen_regimen | AVAX | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 12:50 | macd_momentum_regimen | INJ | momentum perdido | +0.37% | -0.13% | -0.03 |
| 2026-09-29 12:50 | macd_momentum_regimen | LINK | momentum perdido | -0.72% | -1.22% | -0.28 |
| 2026-09-29 12:50 | ruptura_volumen_tope | ATOM | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 12:50 | macd_sin_salida | ASTER | timeout | -0.01% | -0.81% | -0.19 |

## Eventos de la última vuelta

- 2026-09-29 12:55 [ruptura_estricta] CIERRE XRP timeout bruto +2.55% neto +1.45%
- 2026-09-29 12:55 [ruptura_estricta] CIERRE SUI timeout bruto +0.54% neto -0.56%
- 2026-09-29 12:55 [macd_momentum] CIERRE AAVE momentum perdido bruto +0.57% neto +0.07%
- 2026-09-29 12:55 [macd_momentum_regimen] CIERRE AAVE momentum perdido bruto +0.57% neto +0.07%
- 2026-09-29 12:55 [macd_sin_salida] CIERRE HYPE timeout bruto -0.44% neto -1.24%
- 2026-09-29 12:50 [estocastico_rebote] ENTRADA XDC @ 0.03148 (23.12 €, apertura)
- 2026-09-29 12:55 [ruptura_estricta] CIERRE DOGE timeout bruto +0.21% neto -0.89%
- 2026-09-29 12:50 [macd_momentum] ENTRADA BCH @ 275.9 (22.73 €, apertura)
- 2026-09-29 12:50 [macd_sin_salida] ENTRADA BCH @ 275.9 (22.99 €, apertura)
- 2026-09-29 12:50 [macd_momentum_regimen] ENTRADA BCH @ 275.9 (22.73 €, apertura)
- 2026-09-29 12:50 [rebote_extremo] ENTRADA VVV @ 23.964 (23.11 €, apertura)
- 2026-09-29 12:55 [pullback_tendencia] CIERRE NIGHT take-profit bruto +2.00% neto +0.90%
- 2026-09-29 12:50 [pullback_tendencia] ENTRADA BNB @ 674.41 (23.02 €, apertura)
- 2026-09-29 12:55 [macd_sin_salida] CIERRE BNB timeout bruto -0.10% neto -0.90%
- 2026-09-29 12:55 [estocastico_rebote] CIERRE TRUMP take-profit bruto +1.80% neto +0.70%
- 2026-09-29 12:55 [macd_sin_salida] CIERRE SPX timeout bruto +0.22% neto -0.58%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
