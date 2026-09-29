# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 20:31 UTC · vueltas 130 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.25 € (-1.51%) | 59 | 14 | 34% | -0.182% | -1.124% | -1.263% | -15.29 € |
| reversion_bb | 919.09 € (-0.56%) | 15 | 4 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 907.38 € (-1.82%) | 88 | 16 | 26% | -0.091% | -0.887% | -1.025% | -17.92 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.95 € (-1.87%) | 76 | 1 | 24% | -0.160% | -1.004% | -1.122% | -17.50 € |
| macd_momentum | 898.51 € (-2.78%) | 156 | 8 | 21% | -0.057% | -0.724% | -0.843% | -25.84 € |
| estocastico_rebote | 895.17 € (-3.15%) | 150 | 9 | 31% | -0.212% | -0.886% | -1.006% | -30.39 € |
| ruptura_estricta | 912.17 € (-1.31%) | 44 | 4 | 30% | -0.193% | -1.280% | -1.414% | -12.97 € |
| macd_sin_salida | 905.20 € (-2.06%) | 101 | 9 | 33% | -0.072% | -0.831% | -0.959% | -19.25 € |
| c_banda_atr_tope | 915.63 € (-0.93%) | 24 | 5 | 25% | -0.585% | -1.685% | -1.845% | -9.32 € |
| ruptura_volumen_tope | 917.27 € (-0.75%) | 28 | 5 | 18% | -0.034% | -1.134% | -1.258% | -7.31 € |
| c_banda_atr_regimen | 908.98 € (-1.65%) | 52 | 8 | 31% | -0.275% | -1.277% | -1.415% | -15.31 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 6 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 908.38 € (-1.72%) | 76 | 11 | 26% | -0.090% | -0.933% | -1.076% | -16.29 € |
| c_banda_atr_evento | 915.71 € (-0.92%) | 27 | 14 | 30% | -0.480% | -1.580% | -1.731% | -9.84 € |
| macd_momentum_evento | 912.24 € (-1.30%) | 36 | 8 | 19% | -0.358% | -1.458% | -1.588% | -12.11 € |
| ruptura_volumen_evento | 915.05 € (-0.99%) | 29 | 16 | 21% | -0.436% | -1.536% | -1.699% | -10.26 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 20:30 | macd_momentum_evento | NIGHT | take-profit | +2.21% | +1.11% | +0.25 |
| 2026-09-29 20:30 | ruptura_volumen_regimen | ICP | take-profit | +2.55% | +2.05% | +0.47 |
| 2026-09-29 20:30 | macd_sin_salida | NIGHT | take-profit | +2.21% | +1.71% | +0.39 |
| 2026-09-29 20:30 | estocastico_rebote | NIGHT | take-profit | +2.39% | +1.89% | +0.42 |
| 2026-09-29 20:30 | macd_momentum | NIGHT | take-profit | +2.21% | +1.71% | +0.38 |
| 2026-09-29 20:25 | ruptura_volumen_evento | SEI | timeout | +1.41% | +0.31% | +0.07 |
| 2026-09-29 20:25 | ruptura_volumen_evento | DASH | timeout | -0.78% | -1.88% | -0.43 |
| 2026-09-29 20:25 | ruptura_volumen | SEI | timeout | +1.41% | +0.91% | +0.21 |
| 2026-09-29 20:25 | ruptura_volumen | DASH | timeout | -0.78% | -1.28% | -0.29 |
| 2026-09-29 20:20 | ruptura_volumen_evento | ASTER | timeout | -0.18% | -1.28% | -0.29 |
| 2026-09-29 20:20 | ruptura_volumen_evento | ARB | timeout | -0.16% | -1.26% | -0.29 |
| 2026-09-29 20:20 | ruptura_volumen_tope | ASTER | timeout | -0.18% | -1.28% | -0.29 |
| 2026-09-29 20:20 | ruptura_volumen_tope | ARB | timeout | -0.16% | -1.26% | -0.29 |
| 2026-09-29 20:20 | ruptura_volumen | ASTER | timeout | -0.18% | -0.68% | -0.15 |
| 2026-09-29 20:20 | ruptura_volumen | ARB | timeout | -0.16% | -0.66% | -0.15 |

## Eventos de la última vuelta

- 2026-09-29 20:25 [macd_momentum] ENTRADA ADA @ 0.216335 (22.45 €, apertura)
- 2026-09-29 20:25 [macd_sin_salida] ENTRADA ADA @ 0.216335 (22.62 €, apertura)
- 2026-09-29 20:25 [macd_momentum_regimen] ENTRADA ADA @ 0.216335 (22.47 €, apertura)
- 2026-09-29 20:25 [macd_momentum_evento] ENTRADA ADA @ 0.216335 (22.80 €, apertura)
- 2026-09-29 20:25 [c_banda_atr] ENTRADA LTC @ 59.7 (22.72 €, apertura)
- 2026-09-29 20:25 [macd_momentum] ENTRADA LTC @ 59.7 (22.45 €, apertura)
- 2026-09-29 20:25 [macd_sin_salida] ENTRADA LTC @ 59.7 (22.62 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_regimen] ENTRADA LTC @ 59.7 (22.72 €, apertura)
- 2026-09-29 20:25 [macd_momentum_regimen] ENTRADA LTC @ 59.7 (22.47 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_evento] ENTRADA LTC @ 59.7 (22.86 €, apertura)
- 2026-09-29 20:25 [macd_momentum_evento] ENTRADA LTC @ 59.7 (22.80 €, apertura)
- 2026-09-29 20:25 [c_banda_atr] ENTRADA XLM @ 0.196995 (22.72 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_regimen] ENTRADA XLM @ 0.196995 (22.72 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_evento] ENTRADA XLM @ 0.196995 (22.86 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_regimen] ENTRADA ARB @ 0.183 (22.72 €, apertura)
- 2026-09-29 20:30 [ruptura_volumen_regimen] CIERRE ICP take-profit bruto +2.55% neto +2.05%
- 2026-09-29 20:25 [macd_momentum] ENTRADA INJ @ 6.874 (22.45 €, apertura)
- 2026-09-29 20:25 [macd_sin_salida] ENTRADA INJ @ 6.874 (22.62 €, apertura)
- 2026-09-29 20:25 [macd_momentum_regimen] ENTRADA INJ @ 6.874 (22.47 €, apertura)
- 2026-09-29 20:25 [macd_momentum_evento] ENTRADA INJ @ 6.874 (22.80 €, apertura)
- 2026-09-29 20:25 [macd_momentum] ENTRADA TRX @ 0.295628 (22.45 €, apertura)
- 2026-09-29 20:25 [macd_sin_salida] ENTRADA TRX @ 0.295628 (22.62 €, apertura)
- 2026-09-29 20:25 [macd_momentum_regimen] ENTRADA TRX @ 0.295628 (22.47 €, apertura)
- 2026-09-29 20:25 [macd_momentum_evento] ENTRADA TRX @ 0.295628 (22.80 €, apertura)
- 2026-09-29 20:25 [c_banda_atr] ENTRADA ATOM @ 1.5341 (22.72 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_regimen] ENTRADA ATOM @ 1.5341 (22.72 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_evento] ENTRADA ATOM @ 1.5341 (22.86 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_regimen] ENTRADA WLD @ 0.4383 (22.72 €, apertura)
- 2026-09-29 20:25 [c_banda_atr] ENTRADA PEPE @ 3.757e-06 (22.72 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_regimen] ENTRADA PEPE @ 3.757e-06 (22.72 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_evento] ENTRADA PEPE @ 3.757e-06 (22.86 €, apertura)
- 2026-09-29 20:30 [macd_momentum] CIERRE NIGHT take-profit bruto +2.21% neto +1.71%
- 2026-09-29 20:30 [estocastico_rebote] CIERRE NIGHT take-profit bruto +2.39% neto +1.89%
- 2026-09-29 20:30 [macd_sin_salida] CIERRE NIGHT take-profit bruto +2.21% neto +1.71%
- 2026-09-29 20:30 [macd_momentum_evento] CIERRE NIGHT take-profit bruto +2.21% neto +1.11%
- 2026-09-29 20:25 [macd_momentum] ENTRADA FIL @ 0.955 (22.46 €, apertura)
- 2026-09-29 20:25 [macd_sin_salida] ENTRADA FIL @ 0.955 (22.62 €, apertura)
- 2026-09-29 20:25 [macd_momentum_regimen] ENTRADA FIL @ 0.955 (22.47 €, apertura)
- 2026-09-29 20:25 [macd_momentum_evento] ENTRADA FIL @ 0.955 (22.80 €, apertura)
- 2026-09-29 20:25 [macd_momentum] ENTRADA POL @ 0.10425 (22.46 €, apertura)
- 2026-09-29 20:25 [macd_sin_salida] ENTRADA POL @ 0.10425 (22.62 €, apertura)
- 2026-09-29 20:25 [macd_momentum_regimen] ENTRADA POL @ 0.10425 (22.47 €, apertura)
- 2026-09-29 20:25 [macd_momentum_evento] ENTRADA POL @ 0.10425 (22.80 €, apertura)
- 2026-09-29 20:25 [ruptura_volumen_regimen] ENTRADA BNB @ 667.25 (22.70 €, apertura)
- 2026-09-29 20:25 [c_banda_atr] ENTRADA TRUMP @ 1.801 (22.72 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_regimen] ENTRADA TRUMP @ 1.801 (22.72 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_evento] ENTRADA TRUMP @ 1.801 (22.86 €, apertura)
- 2026-09-29 20:25 [c_banda_atr] ENTRADA GRT @ 0.02608 (22.72 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_regimen] ENTRADA GRT @ 0.02608 (22.72 €, apertura)
- 2026-09-29 20:25 [c_banda_atr_evento] ENTRADA GRT @ 0.02608 (22.86 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
