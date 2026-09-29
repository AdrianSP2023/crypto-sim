# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 12:41 UTC · vueltas 37 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 926.04 € (+0.19%) | 8 | 24 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| reversion_bb | 923.64 € (-0.07%) | 1 | 0 | 0% | -1.500% | -2.600% | -2.784% | -0.60 € |
| ruptura_volumen | 919.21 € (-0.54%) | 33 | 19 | 36% | +0.440% | -0.660% | -0.793% | -5.03 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 922.74 € (-0.16%) | 19 | 9 | 47% | +0.531% | -0.569% | -0.680% | -2.50 € |
| macd_momentum | 911.50 € (-1.38%) | 79 | 12 | 18% | +0.052% | -0.778% | -0.895% | -14.17 € |
| estocastico_rebote | 927.12 € (+0.31%) | 22 | 29 | 77% | +1.122% | +0.022% | -0.122% | +0.12 € |
| ruptura_estricta | 924.49 € (+0.03%) | 8 | 23 | 50% | +0.552% | -0.548% | -0.733% | -1.01 € |
| macd_sin_salida | 922.38 € (-0.20%) | 30 | 25 | 57% | +0.741% | -0.359% | -0.483% | -2.48 € |
| c_banda_atr_tope | 924.61 € (+0.04%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 923.01 € (-0.13%) | 9 | 5 | 33% | +0.563% | -0.537% | -0.664% | -1.12 € |
| c_banda_atr_regimen | 926.04 € (+0.19%) | 8 | 24 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| macd_momentum_regimen | 911.50 € (-1.38%) | 79 | 12 | 18% | +0.052% | -0.778% | -0.895% | -14.17 € |
| ruptura_volumen_regimen | 919.21 € (-0.54%) | 33 | 19 | 36% | +0.440% | -0.660% | -0.793% | -5.03 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 12:40 | ruptura_volumen_regimen | JUP | stop-loss | -1.21% | -2.31% | -0.53 |
| 2026-09-29 12:40 | macd_momentum_regimen | FET | momentum perdido | -0.67% | -1.17% | -0.27 |
| 2026-09-29 12:40 | macd_momentum_regimen | XPL | momentum perdido | +0.11% | -0.39% | -0.09 |
| 2026-09-29 12:40 | macd_momentum_regimen | SEI | momentum perdido | -0.99% | -1.49% | -0.34 |
| 2026-09-29 12:40 | macd_momentum_regimen | XRP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 12:40 | macd_sin_salida | TRUMP | timeout | +1.12% | +0.02% | +0.00 |
| 2026-09-29 12:40 | macd_sin_salida | TON | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 12:40 | macd_sin_salida | BCH | timeout | +0.30% | -0.80% | -0.18 |
| 2026-09-29 12:40 | macd_sin_salida | ENA | timeout | +0.81% | -0.29% | -0.07 |
| 2026-09-29 12:40 | macd_sin_salida | DOGE | timeout | +0.79% | -0.31% | -0.07 |
| 2026-09-29 12:40 | macd_sin_salida | HBAR | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 12:40 | macd_sin_salida | XRP | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 12:40 | macd_sin_salida | BTC | timeout | +0.38% | -0.72% | -0.17 |
| 2026-09-29 12:40 | estocastico_rebote | GRT | timeout | -0.18% | -1.28% | -0.30 |
| 2026-09-29 12:40 | macd_momentum | FET | momentum perdido | -0.67% | -1.17% | -0.27 |

## Eventos de la última vuelta

- 2026-09-29 12:40 [macd_sin_salida] CIERRE BTC timeout bruto +0.38% neto -0.72%
- 2026-09-29 12:35 [ruptura_volumen] ENTRADA XRP @ 1.3536 (22.99 €, apertura)
- 2026-09-29 12:40 [pullback_tendencia] CIERRE XRP take-profit bruto +2.00% neto +0.90%
- 2026-09-29 12:40 [macd_momentum] CIERRE XRP take-profit bruto +2.00% neto +1.50%
- 2026-09-29 12:40 [macd_sin_salida] CIERRE XRP take-profit bruto +2.00% neto +0.90%
- 2026-09-29 12:35 [ruptura_volumen_tope] ENTRADA XRP @ 1.3536 (23.08 €, apertura)
- 2026-09-29 12:40 [macd_momentum_regimen] CIERRE XRP take-profit bruto +2.00% neto +1.50%
- 2026-09-29 12:35 [ruptura_volumen_regimen] ENTRADA XRP @ 1.3536 (22.99 €, apertura)
- 2026-09-29 12:40 [macd_sin_salida] CIERRE HBAR stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 12:40 [macd_sin_salida] CIERRE DOGE timeout bruto +0.79% neto -0.31%
- 2026-09-29 12:40 [macd_sin_salida] CIERRE ENA timeout bruto +0.81% neto -0.29%
- 2026-09-29 12:40 [ruptura_volumen] CIERRE JUP stop-loss bruto -1.21% neto -2.31%
- 2026-09-29 12:40 [pullback_tendencia] CIERRE JUP rotura de tendencia bruto -0.92% neto -2.02%
- 2026-09-29 12:40 [ruptura_volumen_regimen] CIERRE JUP stop-loss bruto -1.21% neto -2.31%
- 2026-09-29 12:35 [estocastico_rebote] ENTRADA ICP @ 2.93 (23.12 €, apertura)
- 2026-09-29 12:40 [macd_sin_salida] CIERRE BCH timeout bruto +0.30% neto -0.80%
- 2026-09-29 12:35 [macd_momentum] ENTRADA TRX @ 0.29568 (22.77 €, apertura)
- 2026-09-29 12:35 [macd_momentum_regimen] ENTRADA TRX @ 0.29568 (22.77 €, apertura)
- 2026-09-29 12:40 [macd_momentum] CIERRE SEI momentum perdido bruto -0.99% neto -1.49%
- 2026-09-29 12:40 [macd_momentum_regimen] CIERRE SEI momentum perdido bruto -0.99% neto -1.49%
- 2026-09-29 12:40 [macd_sin_salida] CIERRE TON stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 12:35 [ruptura_volumen_tope] ENTRADA POL @ 0.10952 (23.08 €, apertura)
- 2026-09-29 12:40 [macd_sin_salida] CIERRE TRUMP timeout bruto +1.12% neto +0.02%
- 2026-09-29 12:40 [estocastico_rebote] CIERRE GRT timeout bruto -0.18% neto -1.28%
- 2026-09-29 12:40 [macd_momentum] CIERRE XPL momentum perdido bruto +0.11% neto -0.39%
- 2026-09-29 12:40 [macd_momentum_regimen] CIERRE XPL momentum perdido bruto +0.11% neto -0.39%
- 2026-09-29 12:40 [macd_momentum] CIERRE FET momentum perdido bruto -0.67% neto -1.17%
- 2026-09-29 12:40 [macd_momentum_regimen] CIERRE FET momentum perdido bruto -0.67% neto -1.17%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
