# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 14:42 UTC · vueltas 60 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 918.16 € (-0.66%) | 29 | 20 | 45% | +0.141% | -0.959% | -1.108% | -6.42 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 913.85 € (-1.12%) | 56 | 7 | 29% | +0.102% | -0.864% | -0.992% | -11.15 € |
| rebote_extremo | 924.29 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 915.37 € (-0.96%) | 46 | 8 | 30% | +0.105% | -0.936% | -1.045% | -9.92 € |
| macd_momentum | 906.74 € (-1.89%) | 121 | 19 | 21% | +0.051% | -0.664% | -0.782% | -18.47 € |
| estocastico_rebote | 920.65 € (-0.39%) | 57 | 34 | 54% | +0.618% | -0.308% | -0.437% | -4.05 € |
| ruptura_estricta | 919.54 € (-0.51%) | 27 | 12 | 37% | +0.208% | -0.892% | -1.023% | -5.56 € |
| macd_sin_salida | 916.70 € (-0.82%) | 65 | 25 | 40% | +0.328% | -0.560% | -0.686% | -8.36 € |
| c_banda_atr_tope | 920.28 € (-0.43%) | 11 | 5 | 27% | -0.397% | -1.497% | -1.686% | -3.80 € |
| ruptura_volumen_tope | 922.14 € (-0.23%) | 14 | 5 | 21% | +0.267% | -0.833% | -0.958% | -2.69 € |
| c_banda_atr_regimen | 918.16 € (-0.66%) | 29 | 20 | 45% | +0.141% | -0.959% | -1.108% | -6.42 € |
| macd_momentum_regimen | 906.74 € (-1.89%) | 121 | 19 | 21% | +0.051% | -0.664% | -0.782% | -18.47 € |
| ruptura_volumen_regimen | 913.85 € (-1.12%) | 56 | 7 | 29% | +0.102% | -0.864% | -0.992% | -11.15 € |
| c_banda_atr_evento | 923.95 € (-0.03%) | 2 | 14 | 50% | +0.201% | -0.899% | -1.210% | -0.42 € |
| macd_momentum_evento | 925.48 € (+0.13%) | 1 | 19 | 100% | +2.000% | +0.900% | +0.589% | +0.21 € |
| ruptura_volumen_evento | 924.25 € (+0.00%) | 0 | 3 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 14:40 | macd_momentum_evento | WLD | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 14:40 | c_banda_atr_evento | USELESS | stop-loss | -1.60% | -2.70% | -0.62 |
| 2026-09-29 14:40 | c_banda_atr_evento | WLD | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 14:40 | ruptura_volumen_regimen | DOGE | timeout | -0.44% | -1.24% | -0.28 |
| 2026-09-29 14:40 | macd_momentum_regimen | WLD | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:40 | c_banda_atr_regimen | USELESS | stop-loss | -1.60% | -2.70% | -0.62 |
| 2026-09-29 14:40 | c_banda_atr_regimen | WLD | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 14:40 | macd_sin_salida | WLD | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:40 | estocastico_rebote | OP | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-29 14:40 | estocastico_rebote | WLD | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-29 14:40 | macd_momentum | WLD | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:40 | pullback_tendencia | USELESS | stop-loss | -1.60% | -2.10% | -0.48 |
| 2026-09-29 14:40 | pullback_tendencia | NEAR | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 14:40 | ruptura_volumen | DOGE | timeout | -0.44% | -1.24% | -0.28 |
| 2026-09-29 14:40 | c_banda_atr | USELESS | stop-loss | -1.60% | -2.70% | -0.62 |

## Eventos de la última vuelta

- 2026-09-29 14:40 [pullback_tendencia] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 14:35 [macd_momentum] ENTRADA ADA @ 0.222524 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_momentum_regimen] ENTRADA ADA @ 0.222524 (22.64 €, apertura)
- 2026-09-29 14:35 [c_banda_atr_evento] ENTRADA ADA @ 0.222524 (23.11 €, apertura)
- 2026-09-29 14:35 [macd_momentum_evento] ENTRADA ADA @ 0.222524 (23.11 €, apertura)
- 2026-09-29 14:35 [macd_momentum] ENTRADA SUI @ 1.0277 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_sin_salida] ENTRADA SUI @ 1.0277 (22.89 €, apertura)
- 2026-09-29 14:35 [macd_momentum_regimen] ENTRADA SUI @ 1.0277 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_momentum_evento] ENTRADA SUI @ 1.0277 (23.11 €, apertura)
- 2026-09-29 14:35 [estocastico_rebote] ENTRADA XDC @ 0.03107 (22.99 €, apertura)
- 2026-09-29 14:40 [ruptura_volumen] CIERRE DOGE timeout bruto -0.44% neto -1.24%
- 2026-09-29 14:40 [ruptura_volumen_regimen] CIERRE DOGE timeout bruto -0.44% neto -1.24%
- 2026-09-29 14:35 [macd_momentum] ENTRADA DASH @ 54.436 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_momentum_regimen] ENTRADA DASH @ 54.436 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_momentum_evento] ENTRADA DASH @ 54.436 (23.11 €, apertura)
- 2026-09-29 14:35 [macd_momentum] ENTRADA MON @ 0.0254 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_sin_salida] ENTRADA MON @ 0.0254 (22.89 €, apertura)
- 2026-09-29 14:35 [macd_momentum_regimen] ENTRADA MON @ 0.0254 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_momentum_evento] ENTRADA MON @ 0.0254 (23.11 €, apertura)
- 2026-09-29 14:35 [macd_momentum] ENTRADA BCH @ 275.12 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_momentum_regimen] ENTRADA BCH @ 275.12 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_momentum_evento] ENTRADA BCH @ 275.12 (23.11 €, apertura)
- 2026-09-29 14:35 [macd_momentum] ENTRADA RENDER @ 1.729 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_sin_salida] ENTRADA RENDER @ 1.729 (22.89 €, apertura)
- 2026-09-29 14:35 [macd_momentum_regimen] ENTRADA RENDER @ 1.729 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_momentum_evento] ENTRADA RENDER @ 1.729 (23.11 €, apertura)
- 2026-09-29 14:40 [c_banda_atr] CIERRE WLD take-profit bruto +2.00% neto +0.90%
- 2026-09-29 14:40 [macd_momentum] CIERRE WLD take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:40 [estocastico_rebote] CIERRE WLD take-profit bruto +1.80% neto +1.00%
- 2026-09-29 14:40 [macd_sin_salida] CIERRE WLD take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:40 [c_banda_atr_regimen] CIERRE WLD take-profit bruto +2.00% neto +0.90%
- 2026-09-29 14:40 [macd_momentum_regimen] CIERRE WLD take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:40 [c_banda_atr_evento] CIERRE WLD take-profit bruto +2.00% neto +0.90%
- 2026-09-29 14:40 [macd_momentum_evento] CIERRE WLD take-profit bruto +2.00% neto +0.90%
- 2026-09-29 14:35 [macd_momentum] ENTRADA ZRO @ 1.489 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_sin_salida] ENTRADA ZRO @ 1.489 (22.90 €, apertura)
- 2026-09-29 14:35 [macd_momentum_regimen] ENTRADA ZRO @ 1.489 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_momentum_evento] ENTRADA ZRO @ 1.489 (23.11 €, apertura)
- 2026-09-29 14:40 [c_banda_atr] CIERRE USELESS stop-loss bruto -1.60% neto -2.70%
- 2026-09-29 14:40 [pullback_tendencia] CIERRE USELESS stop-loss bruto -1.60% neto -2.10%
- 2026-09-29 14:40 [c_banda_atr_regimen] CIERRE USELESS stop-loss bruto -1.60% neto -2.70%
- 2026-09-29 14:40 [c_banda_atr_evento] CIERRE USELESS stop-loss bruto -1.60% neto -2.70%
- 2026-09-29 14:40 [estocastico_rebote] CIERRE OP take-profit bruto +1.80% neto +1.00%
- 2026-09-29 14:35 [ruptura_volumen] ENTRADA FIL @ 0.958 (22.83 €, apertura)
- 2026-09-29 14:35 [ruptura_estricta] ENTRADA FIL @ 0.958 (22.97 €, apertura)
- 2026-09-29 14:35 [ruptura_volumen_regimen] ENTRADA FIL @ 0.958 (22.83 €, apertura)
- 2026-09-29 14:35 [ruptura_volumen_evento] ENTRADA FIL @ 0.958 (23.11 €, apertura)
- 2026-09-29 14:35 [macd_momentum] ENTRADA SHIB @ 5.182e-06 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_momentum_regimen] ENTRADA SHIB @ 5.182e-06 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_momentum_evento] ENTRADA SHIB @ 5.182e-06 (23.11 €, apertura)
- 2026-09-29 14:35 [c_banda_atr_evento] ENTRADA BNB @ 673.63 (23.10 €, apertura)
- 2026-09-29 14:35 [macd_momentum] ENTRADA XPL @ 0.0883 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_sin_salida] ENTRADA XPL @ 0.0883 (22.90 €, apertura)
- 2026-09-29 14:35 [macd_momentum_regimen] ENTRADA XPL @ 0.0883 (22.64 €, apertura)
- 2026-09-29 14:35 [macd_momentum_evento] ENTRADA XPL @ 0.0883 (23.11 €, apertura)
- 2026-09-29 14:35 [c_banda_atr_evento] ENTRADA SPX @ 0.3696 (23.10 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
