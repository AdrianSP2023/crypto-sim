# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 01:41 UTC · vueltas 91 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 901.91 € (-2.42%) | 93 | 26 | 27% | -0.278% | -1.058% | -1.185% | -22.57 € |
| reversion_bb | 921.35 € (-0.31%) | 13 | 3 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 892.19 € (-3.47%) | 124 | 17 | 16% | -0.418% | -1.129% | -1.242% | -31.96 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.86 € (-2.20%) | 78 | 4 | 17% | -0.317% | -1.156% | -1.281% | -20.66 € |
| macd_momentum | 901.31 € (-2.48%) | 146 | 27 | 23% | -0.050% | -0.729% | -0.841% | -24.33 € |
| estocastico_rebote | 902.64 € (-2.34%) | 138 | 15 | 37% | +0.021% | -0.668% | -0.791% | -21.23 € |
| ruptura_estricta | 897.89 € (-2.85%) | 58 | 17 | 16% | -0.988% | -1.944% | -2.086% | -25.93 € |
| macd_sin_salida | 902.05 € (-2.40%) | 115 | 18 | 34% | -0.110% | -0.837% | -0.952% | -22.10 € |
| c_banda_atr_tope | 917.87 € (-0.69%) | 22 | 5 | 27% | -0.148% | -1.248% | -1.380% | -6.33 € |
| ruptura_volumen_tope | 915.28 € (-0.97%) | 33 | 5 | 18% | -0.115% | -1.215% | -1.296% | -9.23 € |
| c_banda_atr_regimen | 906.77 € (-1.89%) | 48 | 13 | 23% | -0.511% | -1.555% | -1.710% | -17.17 € |
| macd_momentum_regimen | 907.54 € (-1.81%) | 81 | 13 | 23% | -0.075% | -0.897% | -1.021% | -16.71 € |
| ruptura_volumen_regimen | 893.03 € (-3.38%) | 101 | 13 | 14% | -0.556% | -1.314% | -1.435% | -30.34 € |
| c_banda_atr_evento | 908.19 € (-1.74%) | 60 | 26 | 25% | -0.260% | -1.180% | -1.289% | -16.29 € |
| macd_momentum_evento | 906.31 € (-1.94%) | 99 | 27 | 17% | -0.087% | -0.854% | -0.954% | -19.35 € |
| ruptura_volumen_evento | 904.89 € (-2.09%) | 74 | 17 | 14% | -0.277% | -1.134% | -1.223% | -19.26 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 01:40 | ruptura_volumen_evento | OP | stop-loss | -1.30% | -1.80% | -0.41 |
| 2026-10-01 01:40 | ruptura_volumen_evento | NIGHT | stop-loss | -1.48% | -1.98% | -0.45 |
| 2026-10-01 01:40 | macd_momentum_evento | KSM | momentum perdido | -1.09% | -1.59% | -0.36 |
| 2026-10-01 01:40 | macd_momentum_evento | OP | momentum perdido | -0.87% | -1.37% | -0.31 |
| 2026-10-01 01:40 | macd_momentum_evento | LTC | momentum perdido | -0.30% | -0.80% | -0.18 |
| 2026-10-01 01:40 | c_banda_atr_evento | DASH | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 01:40 | ruptura_volumen_regimen | OP | stop-loss | -1.30% | -1.80% | -0.40 |
| 2026-10-01 01:40 | ruptura_volumen_regimen | NIGHT | stop-loss | -1.48% | -1.98% | -0.44 |
| 2026-10-01 01:40 | macd_momentum_regimen | KSM | momentum perdido | -1.09% | -1.59% | -0.36 |
| 2026-10-01 01:40 | c_banda_atr_regimen | DASH | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 01:40 | macd_sin_salida | DASH | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 01:40 | macd_sin_salida | SHIB | timeout | -0.18% | -0.68% | -0.15 |
| 2026-10-01 01:40 | macd_sin_salida | FIL | timeout | +0.65% | +0.15% | +0.04 |
| 2026-10-01 01:40 | ruptura_estricta | ALGO | timeout | -0.62% | -1.12% | -0.25 |
| 2026-10-01 01:40 | macd_momentum | KSM | momentum perdido | -1.09% | -1.59% | -0.36 |

## Eventos de la última vuelta

- 2026-10-01 01:35 [c_banda_atr] ENTRADA UNI @ 7.8355 (22.55 €, apertura)
- 2026-10-01 01:35 [macd_momentum] ENTRADA UNI @ 7.8355 (22.52 €, apertura)
- 2026-10-01 01:35 [macd_sin_salida] ENTRADA UNI @ 7.8355 (22.57 €, apertura)
- 2026-10-01 01:35 [c_banda_atr_tope] ENTRADA UNI @ 7.8355 (22.95 €, apertura)
- 2026-10-01 01:35 [c_banda_atr_regimen] ENTRADA UNI @ 7.8355 (22.69 €, apertura)
- 2026-10-01 01:35 [macd_momentum_regimen] ENTRADA UNI @ 7.8355 (22.70 €, apertura)
- 2026-10-01 01:35 [c_banda_atr_evento] ENTRADA UNI @ 7.8355 (22.71 €, apertura)
- 2026-10-01 01:35 [macd_momentum_evento] ENTRADA UNI @ 7.8355 (22.64 €, apertura)
- 2026-10-01 01:40 [macd_momentum] CIERRE LTC momentum perdido bruto -0.30% neto -0.80%
- 2026-10-01 01:40 [macd_momentum_evento] CIERRE LTC momentum perdido bruto -0.30% neto -0.80%
- 2026-10-01 01:40 [ruptura_estricta] CIERRE ALGO timeout bruto -0.62% neto -1.12%
- 2026-10-01 01:40 [ruptura_volumen] CIERRE NIGHT stop-loss bruto -1.48% neto -1.98%
- 2026-10-01 01:40 [ruptura_volumen_regimen] CIERRE NIGHT stop-loss bruto -1.48% neto -1.98%
- 2026-10-01 01:40 [ruptura_volumen_evento] CIERRE NIGHT stop-loss bruto -1.48% neto -1.98%
- 2026-10-01 01:40 [ruptura_volumen] CIERRE OP stop-loss bruto -1.30% neto -1.80%
- 2026-10-01 01:40 [macd_momentum] CIERRE OP momentum perdido bruto -0.87% neto -1.37%
- 2026-10-01 01:40 [ruptura_volumen_regimen] CIERRE OP stop-loss bruto -1.30% neto -1.80%
- 2026-10-01 01:40 [macd_momentum_evento] CIERRE OP momentum perdido bruto -0.87% neto -1.37%
- 2026-10-01 01:40 [ruptura_volumen_evento] CIERRE OP stop-loss bruto -1.30% neto -1.80%
- 2026-10-01 01:35 [c_banda_atr] ENTRADA MINA @ 0.1292 (22.55 €, apertura)
- 2026-10-01 01:35 [c_banda_atr_regimen] ENTRADA MINA @ 0.1292 (22.69 €, apertura)
- 2026-10-01 01:35 [c_banda_atr_evento] ENTRADA MINA @ 0.1292 (22.71 €, apertura)
- 2026-10-01 01:40 [macd_sin_salida] CIERRE FIL timeout bruto +0.65% neto +0.15%
- 2026-10-01 01:40 [macd_sin_salida] CIERRE SHIB timeout bruto -0.18% neto -0.68%
- 2026-10-01 01:40 [c_banda_atr] CIERRE DASH stop-loss bruto -1.51% neto -2.01%
- 2026-10-01 01:40 [macd_sin_salida] CIERRE DASH stop-loss bruto -1.51% neto -2.01%
- 2026-10-01 01:40 [c_banda_atr_regimen] CIERRE DASH stop-loss bruto -1.51% neto -2.01%
- 2026-10-01 01:40 [c_banda_atr_evento] CIERRE DASH stop-loss bruto -1.51% neto -2.01%
- 2026-10-01 01:40 [macd_momentum] CIERRE KSM momentum perdido bruto -1.09% neto -1.59%
- 2026-10-01 01:40 [macd_momentum_regimen] CIERRE KSM momentum perdido bruto -1.09% neto -1.59%
- 2026-10-01 01:40 [macd_momentum_evento] CIERRE KSM momentum perdido bruto -1.09% neto -1.59%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
