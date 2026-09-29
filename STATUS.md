# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 20:41 UTC · vueltas 132 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.69 € (-1.57%) | 59 | 16 | 34% | -0.182% | -1.124% | -1.263% | -15.29 € |
| reversion_bb | 918.97 € (-0.57%) | 15 | 4 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 905.97 € (-1.98%) | 90 | 17 | 26% | -0.084% | -0.874% | -1.012% | -18.05 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.91 € (-1.87%) | 76 | 1 | 24% | -0.160% | -1.004% | -1.122% | -17.50 € |
| macd_momentum | 897.67 € (-2.88%) | 158 | 19 | 21% | -0.059% | -0.725% | -0.842% | -26.19 € |
| estocastico_rebote | 894.72 € (-3.19%) | 150 | 9 | 31% | -0.212% | -0.886% | -1.006% | -30.39 € |
| ruptura_estricta | 911.61 € (-1.37%) | 44 | 4 | 30% | -0.193% | -1.280% | -1.414% | -12.97 € |
| macd_sin_salida | 904.57 € (-2.13%) | 101 | 22 | 33% | -0.072% | -0.831% | -0.959% | -19.25 € |
| c_banda_atr_tope | 915.46 € (-0.95%) | 24 | 5 | 25% | -0.585% | -1.685% | -1.845% | -9.32 € |
| ruptura_volumen_tope | 916.79 € (-0.81%) | 29 | 5 | 17% | -0.023% | -1.123% | -1.246% | -7.51 € |
| c_banda_atr_regimen | 908.91 € (-1.66%) | 52 | 10 | 31% | -0.275% | -1.277% | -1.415% | -15.31 € |
| macd_momentum_regimen | 897.93 € (-2.85%) | 149 | 17 | 19% | -0.081% | -0.756% | -0.871% | -25.78 € |
| ruptura_volumen_regimen | 907.93 € (-1.76%) | 76 | 13 | 26% | -0.090% | -0.933% | -1.076% | -16.29 € |
| c_banda_atr_evento | 915.15 € (-0.98%) | 27 | 16 | 30% | -0.480% | -1.580% | -1.731% | -9.84 € |
| macd_momentum_evento | 911.25 € (-1.41%) | 38 | 19 | 18% | -0.353% | -1.438% | -1.561% | -12.60 € |
| ruptura_volumen_evento | 913.35 € (-1.18%) | 31 | 17 | 19% | -0.395% | -1.495% | -1.654% | -10.67 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 20:40 | ruptura_volumen_evento | ATOM | timeout | +0.12% | -0.98% | -0.22 |
| 2026-09-29 20:40 | ruptura_volumen_evento | UNI | timeout | +0.27% | -0.83% | -0.19 |
| 2026-09-29 20:40 | macd_momentum_evento | LTC | momentum perdido | -0.52% | -1.32% | -0.30 |
| 2026-09-29 20:40 | macd_momentum_evento | BTC | momentum perdido | -0.04% | -0.84% | -0.19 |
| 2026-09-29 20:40 | macd_momentum_regimen | LTC | momentum perdido | -0.52% | -1.02% | -0.23 |
| 2026-09-29 20:40 | macd_momentum_regimen | BTC | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-09-29 20:40 | ruptura_volumen_tope | UNI | timeout | +0.27% | -0.83% | -0.19 |
| 2026-09-29 20:40 | macd_momentum | LTC | momentum perdido | -0.52% | -1.02% | -0.23 |
| 2026-09-29 20:40 | macd_momentum | BTC | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-09-29 20:40 | ruptura_volumen | ATOM | timeout | +0.12% | -0.38% | -0.09 |
| 2026-09-29 20:40 | ruptura_volumen | UNI | timeout | +0.27% | -0.23% | -0.05 |
| 2026-09-29 20:30 | macd_momentum_evento | NIGHT | take-profit | +2.21% | +1.11% | +0.25 |
| 2026-09-29 20:30 | ruptura_volumen_regimen | ICP | take-profit | +2.55% | +2.05% | +0.47 |
| 2026-09-29 20:30 | macd_sin_salida | NIGHT | take-profit | +2.21% | +1.71% | +0.39 |
| 2026-09-29 20:30 | estocastico_rebote | NIGHT | take-profit | +2.39% | +1.89% | +0.42 |

## Eventos de la última vuelta

- 2026-09-29 20:40 [macd_momentum] CIERRE BTC momentum perdido bruto -0.04% neto -0.54%
- 2026-09-29 20:40 [macd_momentum_regimen] CIERRE BTC momentum perdido bruto -0.04% neto -0.54%
- 2026-09-29 20:40 [macd_momentum_evento] CIERRE BTC momentum perdido bruto -0.04% neto -0.84%
- 2026-09-29 20:40 [macd_momentum] CIERRE LTC momentum perdido bruto -0.52% neto -1.02%
- 2026-09-29 20:40 [macd_momentum_regimen] CIERRE LTC momentum perdido bruto -0.52% neto -1.02%
- 2026-09-29 20:40 [macd_momentum_evento] CIERRE LTC momentum perdido bruto -0.52% neto -1.32%
- 2026-09-29 20:35 [ruptura_volumen] ENTRADA XLM @ 0.197325 (22.66 €, apertura)
- 2026-09-29 20:35 [ruptura_volumen_regimen] ENTRADA XLM @ 0.197325 (22.70 €, apertura)
- 2026-09-29 20:35 [ruptura_volumen_evento] ENTRADA XLM @ 0.197325 (22.85 €, apertura)
- 2026-09-29 20:40 [ruptura_volumen] CIERRE UNI timeout bruto +0.27% neto -0.23%
- 2026-09-29 20:40 [ruptura_volumen_tope] CIERRE UNI timeout bruto +0.27% neto -0.83%
- 2026-09-29 20:40 [ruptura_volumen_evento] CIERRE UNI timeout bruto +0.27% neto -0.83%
- 2026-09-29 20:35 [c_banda_atr] ENTRADA DASH @ 54.014 (22.72 €, apertura)
- 2026-09-29 20:35 [c_banda_atr_regimen] ENTRADA DASH @ 54.014 (22.72 €, apertura)
- 2026-09-29 20:35 [c_banda_atr_evento] ENTRADA DASH @ 54.014 (22.86 €, apertura)
- 2026-09-29 20:35 [macd_momentum] ENTRADA BCH @ 272.17 (22.45 €, apertura)
- 2026-09-29 20:35 [macd_sin_salida] ENTRADA BCH @ 272.17 (22.62 €, apertura)
- 2026-09-29 20:35 [macd_momentum_regimen] ENTRADA BCH @ 272.17 (22.46 €, apertura)
- 2026-09-29 20:35 [macd_momentum_evento] ENTRADA BCH @ 272.17 (22.79 €, apertura)
- 2026-09-29 20:40 [ruptura_volumen] CIERRE ATOM timeout bruto +0.12% neto -0.38%
- 2026-09-29 20:40 [ruptura_volumen_evento] CIERRE ATOM timeout bruto +0.12% neto -0.98%
- 2026-09-29 20:35 [macd_momentum] ENTRADA WLD @ 0.4371 (22.45 €, apertura)
- 2026-09-29 20:35 [macd_sin_salida] ENTRADA WLD @ 0.4371 (22.62 €, apertura)
- 2026-09-29 20:35 [macd_momentum_regimen] ENTRADA WLD @ 0.4371 (22.46 €, apertura)
- 2026-09-29 20:35 [macd_momentum_evento] ENTRADA WLD @ 0.4371 (22.79 €, apertura)
- 2026-09-29 20:35 [macd_momentum] ENTRADA SEI @ 0.06517 (22.45 €, apertura)
- 2026-09-29 20:35 [macd_sin_salida] ENTRADA SEI @ 0.06517 (22.62 €, apertura)
- 2026-09-29 20:35 [macd_momentum_regimen] ENTRADA SEI @ 0.06517 (22.46 €, apertura)
- 2026-09-29 20:35 [macd_momentum_evento] ENTRADA SEI @ 0.06517 (22.79 €, apertura)
- 2026-09-29 20:35 [macd_momentum] ENTRADA TRUMP @ 1.802 (22.45 €, apertura)
- 2026-09-29 20:35 [macd_sin_salida] ENTRADA TRUMP @ 1.802 (22.62 €, apertura)
- 2026-09-29 20:35 [macd_momentum_regimen] ENTRADA TRUMP @ 1.802 (22.46 €, apertura)
- 2026-09-29 20:35 [macd_momentum_evento] ENTRADA TRUMP @ 1.802 (22.79 €, apertura)
- 2026-09-29 20:35 [ruptura_volumen] ENTRADA SPX @ 0.3671 (22.65 €, apertura)
- 2026-09-29 20:35 [ruptura_volumen_tope] ENTRADA SPX @ 0.3671 (22.92 €, apertura)
- 2026-09-29 20:35 [ruptura_volumen_regimen] ENTRADA SPX @ 0.3671 (22.70 €, apertura)
- 2026-09-29 20:35 [ruptura_volumen_evento] ENTRADA SPX @ 0.3671 (22.84 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
