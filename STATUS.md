# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 23:01 UTC · vueltas 160 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 905.78 € (-2.00%) | 68 | 21 | 31% | -0.213% | -1.096% | -1.242% | -17.16 € |
| reversion_bb | 917.75 € (-0.70%) | 18 | 4 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 903.17 € (-2.28%) | 110 | 3 | 24% | -0.103% | -0.840% | -0.968% | -21.18 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.25 € (-2.05%) | 85 | 4 | 22% | -0.181% | -0.988% | -1.111% | -19.25 € |
| macd_momentum | 890.86 € (-3.61%) | 198 | 11 | 17% | -0.115% | -0.747% | -0.863% | -33.69 € |
| estocastico_rebote | 892.96 € (-3.38%) | 157 | 14 | 31% | -0.205% | -0.871% | -0.993% | -31.26 € |
| ruptura_estricta | 909.32 € (-1.61%) | 47 | 7 | 28% | -0.283% | -1.338% | -1.473% | -14.47 € |
| macd_sin_salida | 901.35 € (-2.48%) | 104 | 35 | 32% | -0.095% | -0.846% | -0.978% | -20.17 € |
| c_banda_atr_tope | 912.96 € (-1.22%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 915.03 € (-1.00%) | 35 | 4 | 14% | -0.070% | -1.170% | -1.287% | -9.43 € |
| c_banda_atr_regimen | 907.57 € (-1.80%) | 53 | 9 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.80 € (-3.29%) | 173 | 0 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 905.66 € (-2.01%) | 92 | 0 | 23% | -0.097% | -0.881% | -1.009% | -18.58 € |
| c_banda_atr_evento | 910.11 € (-1.53%) | 36 | 21 | 25% | -0.463% | -1.547% | -1.706% | -12.82 € |
| macd_momentum_evento | 903.38 € (-2.26%) | 78 | 11 | 9% | -0.345% | -1.183% | -1.299% | -21.17 € |
| ruptura_volumen_evento | 908.73 € (-1.68%) | 51 | 3 | 14% | -0.314% | -1.331% | -1.462% | -15.62 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 23:00 | ruptura_volumen_evento | NIGHT | timeout | -0.07% | -0.57% | -0.13 |
| 2026-09-29 23:00 | ruptura_volumen_regimen | NIGHT | timeout | -0.07% | -0.57% | -0.13 |
| 2026-09-29 23:00 | ruptura_volumen_tope | NIGHT | timeout | -0.07% | -1.17% | -0.27 |
| 2026-09-29 23:00 | ruptura_volumen | NIGHT | timeout | -0.07% | -0.57% | -0.13 |
| 2026-09-29 22:55 | ruptura_volumen_evento | ZRO | take-profit | +2.50% | +2.00% | +0.46 |
| 2026-09-29 22:55 | ruptura_volumen | ZRO | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-29 22:50 | macd_momentum_evento | PEPE | momentum perdido | -0.42% | -0.92% | -0.21 |
| 2026-09-29 22:50 | ruptura_volumen_regimen | POL | timeout | -0.81% | -1.31% | -0.30 |
| 2026-09-29 22:50 | estocastico_rebote | QNT | take-profit | +1.99% | +1.49% | +0.33 |
| 2026-09-29 22:50 | macd_momentum | PEPE | momentum perdido | -0.42% | -0.92% | -0.21 |
| 2026-09-29 22:45 | ruptura_volumen_evento | BCH | timeout | -0.15% | -0.95% | -0.22 |
| 2026-09-29 22:45 | macd_momentum_evento | XLM | momentum perdido | -0.28% | -0.78% | -0.18 |
| 2026-09-29 22:45 | ruptura_volumen_regimen | BCH | timeout | -0.15% | -0.65% | -0.15 |
| 2026-09-29 22:45 | macd_momentum | XLM | momentum perdido | -0.28% | -0.78% | -0.17 |
| 2026-09-29 22:45 | ruptura_volumen | BCH | timeout | -0.15% | -0.65% | -0.15 |

## Eventos de la última vuelta

- 2026-09-29 22:55 [macd_momentum] ENTRADA DASH @ 53.912 (22.26 €, apertura)
- 2026-09-29 22:55 [macd_momentum_evento] ENTRADA DASH @ 53.912 (22.58 €, apertura)
- 2026-09-29 22:55 [macd_momentum] ENTRADA ENA @ 0.2215 (22.26 €, apertura)
- 2026-09-29 22:55 [macd_momentum_evento] ENTRADA ENA @ 0.2215 (22.58 €, apertura)
- 2026-09-29 22:55 [ruptura_estricta] ENTRADA ZRO @ 1.46 (22.74 €, apertura)
- 2026-09-29 22:55 [ruptura_volumen_tope] ENTRADA ZRO @ 1.46 (22.88 €, apertura)
- 2026-09-29 23:00 [ruptura_volumen] CIERRE NIGHT timeout bruto -0.07% neto -0.57%
- 2026-09-29 22:55 [estocastico_rebote] ENTRADA NIGHT @ 0.02859 (22.32 €, apertura)
- 2026-09-29 23:00 [ruptura_volumen_tope] CIERRE NIGHT timeout bruto -0.07% neto -1.17%
- 2026-09-29 23:00 [ruptura_volumen_regimen] CIERRE NIGHT timeout bruto -0.07% neto -0.57%
- 2026-09-29 23:00 [ruptura_volumen_evento] CIERRE NIGHT timeout bruto -0.07% neto -0.57%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
