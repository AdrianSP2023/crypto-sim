# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 14:47 UTC · vueltas 61 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 918.94 € (-0.57%) | 29 | 20 | 45% | +0.141% | -0.959% | -1.108% | -6.42 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 913.71 € (-1.14%) | 56 | 9 | 29% | +0.102% | -0.864% | -0.992% | -11.15 € |
| rebote_extremo | 924.32 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 915.84 € (-0.91%) | 47 | 11 | 32% | +0.146% | -0.891% | -0.999% | -9.65 € |
| macd_momentum | 907.33 € (-1.83%) | 121 | 21 | 21% | +0.051% | -0.664% | -0.782% | -18.47 € |
| estocastico_rebote | 920.98 € (-0.35%) | 59 | 33 | 54% | +0.616% | -0.296% | -0.429% | -4.03 € |
| ruptura_estricta | 919.66 € (-0.50%) | 27 | 13 | 37% | +0.208% | -0.892% | -1.023% | -5.56 € |
| macd_sin_salida | 917.19 € (-0.76%) | 67 | 24 | 40% | +0.348% | -0.537% | -0.668% | -8.28 € |
| c_banda_atr_tope | 920.50 € (-0.40%) | 11 | 5 | 27% | -0.397% | -1.497% | -1.686% | -3.80 € |
| ruptura_volumen_tope | 921.82 € (-0.26%) | 15 | 5 | 20% | +0.300% | -0.800% | -0.920% | -2.77 € |
| c_banda_atr_regimen | 918.94 € (-0.57%) | 29 | 20 | 45% | +0.141% | -0.959% | -1.108% | -6.42 € |
| macd_momentum_regimen | 907.33 € (-1.83%) | 121 | 21 | 21% | +0.051% | -0.664% | -0.782% | -18.47 € |
| ruptura_volumen_regimen | 913.71 € (-1.14%) | 56 | 9 | 29% | +0.102% | -0.864% | -0.992% | -11.15 € |
| c_banda_atr_evento | 924.36 € (+0.01%) | 2 | 14 | 50% | +0.201% | -0.899% | -1.210% | -0.42 € |
| macd_momentum_evento | 926.08 € (+0.20%) | 1 | 21 | 100% | +2.000% | +0.900% | +0.589% | +0.21 € |
| ruptura_volumen_evento | 924.29 € (+0.01%) | 0 | 5 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 14:45 | ruptura_volumen_tope | PEPE | timeout | +0.76% | -0.34% | -0.08 |
| 2026-09-29 14:45 | macd_sin_salida | SHIB | timeout | +1.27% | +0.47% | +0.11 |
| 2026-09-29 14:45 | macd_sin_salida | RAY | timeout | +0.71% | -0.09% | -0.02 |
| 2026-09-29 14:45 | estocastico_rebote | MINA | take-profit | +2.61% | +2.11% | +0.49 |
| 2026-09-29 14:45 | estocastico_rebote | QNT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 14:45 | pullback_tendencia | AAVE | take-profit | +2.00% | +1.20% | +0.28 |
| 2026-09-29 14:40 | macd_momentum_evento | WLD | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 14:40 | c_banda_atr_evento | USELESS | stop-loss | -1.60% | -2.70% | -0.62 |
| 2026-09-29 14:40 | c_banda_atr_evento | WLD | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 14:40 | ruptura_volumen_regimen | DOGE | timeout | -0.44% | -1.24% | -0.28 |
| 2026-09-29 14:40 | macd_momentum_regimen | WLD | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:40 | c_banda_atr_regimen | USELESS | stop-loss | -1.60% | -2.70% | -0.62 |
| 2026-09-29 14:40 | c_banda_atr_regimen | WLD | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 14:40 | macd_sin_salida | WLD | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:40 | estocastico_rebote | OP | take-profit | +1.80% | +1.00% | +0.23 |

## Eventos de la última vuelta

- 2026-09-29 14:45 [estocastico_rebote] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 14:40 [pullback_tendencia] ENTRADA ADA @ 0.223022 (22.86 €, apertura)
- 2026-09-29 14:45 [pullback_tendencia] CIERRE AAVE take-profit bruto +2.00% neto +1.20%
- 2026-09-29 14:40 [macd_momentum] ENTRADA AAVE @ 154.8 (22.64 €, apertura)
- 2026-09-29 14:40 [macd_sin_salida] ENTRADA AAVE @ 154.8 (22.90 €, apertura)
- 2026-09-29 14:40 [macd_momentum_regimen] ENTRADA AAVE @ 154.8 (22.64 €, apertura)
- 2026-09-29 14:40 [macd_momentum_evento] ENTRADA AAVE @ 154.8 (23.11 €, apertura)
- 2026-09-29 14:40 [pullback_tendencia] ENTRADA TAO @ 277.99 (22.86 €, apertura)
- 2026-09-29 14:40 [pullback_tendencia] ENTRADA DOGE @ 0.0844675 (22.86 €, apertura)
- 2026-09-29 14:40 [pullback_tendencia] ENTRADA ENA @ 0.2265 (22.86 €, apertura)
- 2026-09-29 14:40 [ruptura_volumen] ENTRADA WLD @ 0.4583 (22.83 €, apertura)
- 2026-09-29 14:40 [ruptura_estricta] ENTRADA WLD @ 0.4583 (22.97 €, apertura)
- 2026-09-29 14:40 [ruptura_volumen_regimen] ENTRADA WLD @ 0.4583 (22.83 €, apertura)
- 2026-09-29 14:40 [ruptura_volumen_evento] ENTRADA WLD @ 0.4583 (23.11 €, apertura)
- 2026-09-29 14:45 [ruptura_volumen_tope] CIERRE PEPE timeout bruto +0.76% neto -0.34%
- 2026-09-29 14:45 [macd_sin_salida] CIERRE RAY timeout bruto +0.71% neto -0.09%
- 2026-09-29 14:45 [estocastico_rebote] CIERRE MINA take-profit bruto +2.61% neto +2.11%
- 2026-09-29 14:40 [ruptura_volumen] ENTRADA OP @ 0.1198 (22.83 €, apertura)
- 2026-09-29 14:40 [ruptura_volumen_tope] ENTRADA OP @ 0.1198 (23.04 €, apertura)
- 2026-09-29 14:40 [ruptura_volumen_regimen] ENTRADA OP @ 0.1198 (22.83 €, apertura)
- 2026-09-29 14:40 [ruptura_volumen_evento] ENTRADA OP @ 0.1198 (23.11 €, apertura)
- 2026-09-29 14:45 [macd_sin_salida] CIERRE SHIB timeout bruto +1.27% neto +0.47%
- 2026-09-29 14:40 [macd_momentum] ENTRADA SPX @ 0.3702 (22.64 €, apertura)
- 2026-09-29 14:40 [macd_momentum_regimen] ENTRADA SPX @ 0.3702 (22.64 €, apertura)
- 2026-09-29 14:40 [macd_momentum_evento] ENTRADA SPX @ 0.3702 (23.11 €, apertura)
- 2026-09-29 14:40 [estocastico_rebote] ENTRADA FET @ 0.2059 (23.01 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
