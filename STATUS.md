# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 20:36 UTC · vueltas 131 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.07 € (-1.53%) | 59 | 15 | 34% | -0.182% | -1.124% | -1.263% | -15.29 € |
| reversion_bb | 918.95 € (-0.57%) | 15 | 4 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 906.43 € (-1.93%) | 88 | 17 | 26% | -0.091% | -0.887% | -1.025% | -17.92 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.98 € (-1.87%) | 76 | 1 | 24% | -0.160% | -1.004% | -1.122% | -17.50 € |
| macd_momentum | 898.32 € (-2.80%) | 156 | 17 | 21% | -0.057% | -0.724% | -0.843% | -25.84 € |
| estocastico_rebote | 894.80 € (-3.19%) | 150 | 9 | 31% | -0.212% | -0.886% | -1.006% | -30.39 € |
| ruptura_estricta | 911.61 € (-1.37%) | 44 | 4 | 30% | -0.193% | -1.280% | -1.414% | -12.97 € |
| macd_sin_salida | 905.00 € (-2.08%) | 101 | 18 | 33% | -0.072% | -0.831% | -0.959% | -19.25 € |
| c_banda_atr_tope | 915.52 € (-0.94%) | 24 | 5 | 25% | -0.585% | -1.685% | -1.845% | -9.32 € |
| ruptura_volumen_tope | 916.99 € (-0.78%) | 28 | 5 | 18% | -0.034% | -1.134% | -1.258% | -7.31 € |
| c_banda_atr_regimen | 908.91 € (-1.66%) | 52 | 9 | 31% | -0.275% | -1.277% | -1.415% | -15.31 € |
| macd_momentum_regimen | 898.59 € (-2.78%) | 147 | 15 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 907.85 € (-1.77%) | 76 | 11 | 26% | -0.090% | -0.933% | -1.076% | -16.29 € |
| c_banda_atr_evento | 915.53 € (-0.94%) | 27 | 15 | 30% | -0.480% | -1.580% | -1.731% | -9.84 € |
| macd_momentum_evento | 912.04 € (-1.32%) | 36 | 17 | 19% | -0.358% | -1.458% | -1.588% | -12.11 € |
| ruptura_volumen_evento | 914.10 € (-1.10%) | 29 | 17 | 21% | -0.436% | -1.536% | -1.699% | -10.26 € |
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

- 2026-09-29 20:30 [macd_momentum] ENTRADA BTC @ 73761.2 (22.46 €, apertura)
- 2026-09-29 20:30 [macd_sin_salida] ENTRADA BTC @ 73761.2 (22.62 €, apertura)
- 2026-09-29 20:30 [macd_momentum_regimen] ENTRADA BTC @ 73761.2 (22.47 €, apertura)
- 2026-09-29 20:30 [macd_momentum_evento] ENTRADA BTC @ 73761.2 (22.80 €, apertura)
- 2026-09-29 20:30 [macd_momentum] ENTRADA SUI @ 1.0203 (22.46 €, apertura)
- 2026-09-29 20:30 [macd_sin_salida] ENTRADA SUI @ 1.0203 (22.62 €, apertura)
- 2026-09-29 20:30 [macd_momentum_regimen] ENTRADA SUI @ 1.0203 (22.47 €, apertura)
- 2026-09-29 20:30 [macd_momentum_evento] ENTRADA SUI @ 1.0203 (22.80 €, apertura)
- 2026-09-29 20:30 [macd_momentum] ENTRADA ARB @ 0.1831 (22.46 €, apertura)
- 2026-09-29 20:30 [macd_sin_salida] ENTRADA ARB @ 0.1831 (22.62 €, apertura)
- 2026-09-29 20:30 [macd_momentum_regimen] ENTRADA ARB @ 0.1831 (22.47 €, apertura)
- 2026-09-29 20:30 [macd_momentum_evento] ENTRADA ARB @ 0.1831 (22.80 €, apertura)
- 2026-09-29 20:30 [macd_momentum] ENTRADA DOGE @ 0.0829728 (22.46 €, apertura)
- 2026-09-29 20:30 [macd_sin_salida] ENTRADA DOGE @ 0.0829728 (22.62 €, apertura)
- 2026-09-29 20:30 [macd_momentum_regimen] ENTRADA DOGE @ 0.0829728 (22.47 €, apertura)
- 2026-09-29 20:30 [macd_momentum_evento] ENTRADA DOGE @ 0.0829728 (22.80 €, apertura)
- 2026-09-29 20:30 [macd_momentum] ENTRADA DOT @ 1.0601 (22.46 €, apertura)
- 2026-09-29 20:30 [macd_sin_salida] ENTRADA DOT @ 1.0601 (22.62 €, apertura)
- 2026-09-29 20:30 [macd_momentum_regimen] ENTRADA DOT @ 1.0601 (22.47 €, apertura)
- 2026-09-29 20:30 [macd_momentum_evento] ENTRADA DOT @ 1.0601 (22.80 €, apertura)
- 2026-09-29 20:30 [c_banda_atr] ENTRADA ENA @ 0.2213 (22.72 €, apertura)
- 2026-09-29 20:30 [c_banda_atr_regimen] ENTRADA ENA @ 0.2213 (22.72 €, apertura)
- 2026-09-29 20:30 [c_banda_atr_evento] ENTRADA ENA @ 0.2213 (22.86 €, apertura)
- 2026-09-29 20:30 [ruptura_volumen] ENTRADA ICP @ 3.126 (22.66 €, apertura)
- 2026-09-29 20:30 [ruptura_volumen_evento] ENTRADA ICP @ 3.126 (22.85 €, apertura)
- 2026-09-29 20:30 [macd_momentum] ENTRADA ATOM @ 1.5328 (22.46 €, apertura)
- 2026-09-29 20:30 [macd_sin_salida] ENTRADA ATOM @ 1.5328 (22.62 €, apertura)
- 2026-09-29 20:30 [macd_momentum_regimen] ENTRADA ATOM @ 1.5328 (22.47 €, apertura)
- 2026-09-29 20:30 [macd_momentum_evento] ENTRADA ATOM @ 1.5328 (22.80 €, apertura)
- 2026-09-29 20:30 [macd_momentum] ENTRADA VIRTUAL @ 0.7224 (22.46 €, apertura)
- 2026-09-29 20:30 [macd_sin_salida] ENTRADA VIRTUAL @ 0.7224 (22.62 €, apertura)
- 2026-09-29 20:30 [macd_momentum_regimen] ENTRADA VIRTUAL @ 0.7224 (22.47 €, apertura)
- 2026-09-29 20:30 [macd_momentum_evento] ENTRADA VIRTUAL @ 0.7224 (22.80 €, apertura)
- 2026-09-29 20:30 [macd_momentum] ENTRADA PEPE @ 3.767e-06 (22.46 €, apertura)
- 2026-09-29 20:30 [macd_sin_salida] ENTRADA PEPE @ 3.767e-06 (22.62 €, apertura)
- 2026-09-29 20:30 [macd_momentum_regimen] ENTRADA PEPE @ 3.767e-06 (22.47 €, apertura)
- 2026-09-29 20:30 [macd_momentum_evento] ENTRADA PEPE @ 3.767e-06 (22.80 €, apertura)
- 2026-09-29 20:30 [macd_momentum] ENTRADA GRT @ 0.02608 (22.46 €, apertura)
- 2026-09-29 20:30 [macd_sin_salida] ENTRADA GRT @ 0.02608 (22.62 €, apertura)
- 2026-09-29 20:30 [macd_momentum_regimen] ENTRADA GRT @ 0.02608 (22.47 €, apertura)
- 2026-09-29 20:30 [macd_momentum_evento] ENTRADA GRT @ 0.02608 (22.80 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
