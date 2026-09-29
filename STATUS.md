# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 23:16 UTC · vueltas 163 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.96 € (-1.76%) | 69 | 32 | 32% | -0.173% | -1.051% | -1.197% | -16.70 € |
| reversion_bb | 918.32 € (-0.64%) | 18 | 4 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 903.41 € (-2.25%) | 110 | 10 | 24% | -0.103% | -0.840% | -0.968% | -21.18 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.97 € (-1.98%) | 86 | 3 | 23% | -0.156% | -0.959% | -1.081% | -18.91 € |
| macd_momentum | 891.91 € (-3.50%) | 200 | 21 | 17% | -0.104% | -0.735% | -0.851% | -33.47 € |
| estocastico_rebote | 894.09 € (-3.26%) | 162 | 9 | 33% | -0.168% | -0.830% | -0.950% | -30.73 € |
| ruptura_estricta | 910.33 € (-1.50%) | 48 | 8 | 27% | -0.269% | -1.312% | -1.445% | -14.49 € |
| macd_sin_salida | 904.89 € (-2.09%) | 107 | 37 | 33% | -0.078% | -0.822% | -0.953% | -20.17 € |
| c_banda_atr_tope | 913.45 € (-1.17%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 915.52 € (-0.94%) | 36 | 5 | 17% | +0.001% | -1.099% | -1.219% | -9.11 € |
| c_banda_atr_regimen | 908.64 € (-1.69%) | 53 | 22 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.72 € (-3.30%) | 173 | 11 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 905.56 € (-2.02%) | 92 | 6 | 23% | -0.097% | -0.881% | -1.009% | -18.58 € |
| c_banda_atr_evento | 912.31 € (-1.29%) | 37 | 32 | 27% | -0.382% | -1.450% | -1.610% | -12.35 € |
| macd_momentum_evento | 904.45 € (-2.14%) | 80 | 21 | 10% | -0.311% | -1.141% | -1.257% | -20.94 € |
| ruptura_volumen_evento | 908.97 € (-1.65%) | 51 | 10 | 14% | -0.314% | -1.331% | -1.462% | -15.62 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 23:15 | ruptura_estricta | AVAX | timeout | +0.42% | -0.08% | -0.02 |
| 2026-09-29 23:10 | c_banda_atr_evento | RAY | take-profit | +2.54% | +2.04% | +0.47 |
| 2026-09-29 23:10 | ruptura_volumen_tope | ZRO | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 23:10 | macd_sin_salida | AVAX | timeout | +0.85% | +0.35% | +0.08 |
| 2026-09-29 23:10 | estocastico_rebote | TRUMP | timeout | +0.56% | +0.06% | +0.01 |
| 2026-09-29 23:10 | estocastico_rebote | PENGU | timeout | +1.12% | +0.62% | +0.14 |
| 2026-09-29 23:10 | estocastico_rebote | FIL | timeout | +0.42% | -0.08% | -0.02 |
| 2026-09-29 23:10 | estocastico_rebote | JUP | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-29 23:10 | estocastico_rebote | NEAR | timeout | +0.97% | +0.47% | +0.10 |
| 2026-09-29 23:10 | pullback_tendencia | PUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 23:10 | c_banda_atr | RAY | take-profit | +2.54% | +2.04% | +0.46 |
| 2026-09-29 23:05 | macd_momentum_evento | ZRO | take-profit | +2.43% | +1.93% | +0.44 |
| 2026-09-29 23:05 | macd_momentum_evento | AAVE | momentum perdido | -0.44% | -0.94% | -0.21 |
| 2026-09-29 23:05 | macd_sin_salida | ZRO | take-profit | +2.43% | +1.93% | +0.44 |
| 2026-09-29 23:05 | macd_sin_salida | INJ | stop-loss | -1.80% | -2.30% | -0.52 |

## Eventos de la última vuelta

- 2026-09-29 23:10 [ruptura_volumen] ENTRADA BTC @ 73876.4 (22.58 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen_tope] ENTRADA BTC @ 73876.4 (22.88 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen_regimen] ENTRADA BTC @ 73876.4 (22.64 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen_evento] ENTRADA BTC @ 73876.4 (22.72 €, apertura)
- 2026-09-29 23:10 [macd_momentum_regimen] ENTRADA ADA @ 0.217158 (22.34 €, apertura)
- 2026-09-29 23:10 [c_banda_atr] ENTRADA SUI @ 1.0206 (22.69 €, apertura)
- 2026-09-29 23:10 [macd_momentum] ENTRADA SUI @ 1.0206 (22.27 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_regimen] ENTRADA SUI @ 1.0206 (22.71 €, apertura)
- 2026-09-29 23:10 [macd_momentum_regimen] ENTRADA SUI @ 1.0206 (22.34 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_evento] ENTRADA SUI @ 1.0206 (22.80 €, apertura)
- 2026-09-29 23:10 [macd_momentum_evento] ENTRADA SUI @ 1.0206 (22.58 €, apertura)
- 2026-09-29 23:10 [macd_momentum] ENTRADA XLM @ 0.198071 (22.27 €, apertura)
- 2026-09-29 23:10 [macd_momentum_regimen] ENTRADA XLM @ 0.198071 (22.34 €, apertura)
- 2026-09-29 23:10 [macd_momentum_evento] ENTRADA XLM @ 0.198071 (22.58 €, apertura)
- 2026-09-29 23:15 [ruptura_estricta] CIERRE AVAX timeout bruto +0.42% neto -0.08%
- 2026-09-29 23:10 [c_banda_atr] ENTRADA TAO @ 267.004 (22.69 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_regimen] ENTRADA TAO @ 267.004 (22.71 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_evento] ENTRADA TAO @ 267.004 (22.80 €, apertura)
- 2026-09-29 23:10 [c_banda_atr] ENTRADA DOGE @ 0.0832168 (22.69 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_regimen] ENTRADA DOGE @ 0.0832168 (22.71 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_evento] ENTRADA DOGE @ 0.0832168 (22.80 €, apertura)
- 2026-09-29 23:10 [c_banda_atr] ENTRADA DOT @ 1.0614 (22.69 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen] ENTRADA DOT @ 1.0614 (22.58 €, apertura)
- 2026-09-29 23:10 [macd_momentum] ENTRADA DOT @ 1.0614 (22.27 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_regimen] ENTRADA DOT @ 1.0614 (22.71 €, apertura)
- 2026-09-29 23:10 [macd_momentum_regimen] ENTRADA DOT @ 1.0614 (22.34 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen_regimen] ENTRADA DOT @ 1.0614 (22.64 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_evento] ENTRADA DOT @ 1.0614 (22.80 €, apertura)
- 2026-09-29 23:10 [macd_momentum_evento] ENTRADA DOT @ 1.0614 (22.58 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen_evento] ENTRADA DOT @ 1.0614 (22.72 €, apertura)
- 2026-09-29 23:10 [c_banda_atr] ENTRADA CRV @ 0.33793 (22.69 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_regimen] ENTRADA CRV @ 0.33793 (22.71 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_evento] ENTRADA CRV @ 0.33793 (22.80 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen] ENTRADA DASH @ 54.166 (22.58 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen_regimen] ENTRADA DASH @ 54.166 (22.64 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen_evento] ENTRADA DASH @ 54.166 (22.72 €, apertura)
- 2026-09-29 23:10 [macd_momentum] ENTRADA ICP @ 3.055 (22.27 €, apertura)
- 2026-09-29 23:10 [macd_sin_salida] ENTRADA ICP @ 3.055 (22.60 €, apertura)
- 2026-09-29 23:10 [macd_momentum_regimen] ENTRADA ICP @ 3.055 (22.34 €, apertura)
- 2026-09-29 23:10 [macd_momentum_evento] ENTRADA ICP @ 3.055 (22.58 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_regimen] ENTRADA BCH @ 273.09 (22.71 €, apertura)
- 2026-09-29 23:10 [macd_momentum] ENTRADA ATOM @ 1.5299 (22.27 €, apertura)
- 2026-09-29 23:10 [macd_momentum_regimen] ENTRADA ATOM @ 1.5299 (22.34 €, apertura)
- 2026-09-29 23:10 [macd_momentum_evento] ENTRADA ATOM @ 1.5299 (22.58 €, apertura)
- 2026-09-29 23:10 [c_banda_atr] ENTRADA RENDER @ 1.695 (22.69 €, apertura)
- 2026-09-29 23:10 [macd_momentum] ENTRADA RENDER @ 1.695 (22.27 €, apertura)
- 2026-09-29 23:10 [macd_sin_salida] ENTRADA RENDER @ 1.695 (22.60 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_regimen] ENTRADA RENDER @ 1.695 (22.71 €, apertura)
- 2026-09-29 23:10 [macd_momentum_regimen] ENTRADA RENDER @ 1.695 (22.34 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_evento] ENTRADA RENDER @ 1.695 (22.80 €, apertura)
- 2026-09-29 23:10 [macd_momentum_evento] ENTRADA RENDER @ 1.695 (22.58 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen] ENTRADA ZRO @ 1.501 (22.58 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen_regimen] ENTRADA ZRO @ 1.501 (22.64 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen_evento] ENTRADA ZRO @ 1.501 (22.72 €, apertura)
- 2026-09-29 23:10 [c_banda_atr] ENTRADA USELESS @ 0.21491 (22.69 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_regimen] ENTRADA USELESS @ 0.21491 (22.71 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_evento] ENTRADA USELESS @ 0.21491 (22.80 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen] ENTRADA RAY @ 1.697 (22.58 €, apertura)
- 2026-09-29 23:10 [ruptura_estricta] ENTRADA RAY @ 1.697 (22.74 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen_regimen] ENTRADA RAY @ 1.697 (22.64 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen_evento] ENTRADA RAY @ 1.697 (22.72 €, apertura)
- 2026-09-29 23:10 [c_banda_atr] ENTRADA SEI @ 0.06507 (22.69 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_regimen] ENTRADA SEI @ 0.06507 (22.71 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_evento] ENTRADA SEI @ 0.06507 (22.80 €, apertura)
- 2026-09-29 23:10 [c_banda_atr] ENTRADA MINA @ 0.1273 (22.69 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_regimen] ENTRADA MINA @ 0.1273 (22.71 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_evento] ENTRADA MINA @ 0.1273 (22.80 €, apertura)
- 2026-09-29 23:10 [c_banda_atr] ENTRADA OP @ 0.1148 (22.69 €, apertura)
- 2026-09-29 23:10 [macd_momentum] ENTRADA OP @ 0.1148 (22.27 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_regimen] ENTRADA OP @ 0.1148 (22.71 €, apertura)
- 2026-09-29 23:10 [macd_momentum_regimen] ENTRADA OP @ 0.1148 (22.34 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_evento] ENTRADA OP @ 0.1148 (22.80 €, apertura)
- 2026-09-29 23:10 [macd_momentum_evento] ENTRADA OP @ 0.1148 (22.58 €, apertura)
- 2026-09-29 23:10 [macd_momentum] ENTRADA NIGHT @ 0.02891 (22.27 €, apertura)
- 2026-09-29 23:10 [macd_momentum_regimen] ENTRADA NIGHT @ 0.02891 (22.34 €, apertura)
- 2026-09-29 23:10 [macd_momentum_evento] ENTRADA NIGHT @ 0.02891 (22.58 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen] ENTRADA SHIB @ 5.099e-06 (22.58 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen_regimen] ENTRADA SHIB @ 5.099e-06 (22.64 €, apertura)
- 2026-09-29 23:10 [ruptura_volumen_evento] ENTRADA SHIB @ 5.099e-06 (22.72 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_regimen] ENTRADA PENGU @ 0.008841 (22.71 €, apertura)
- 2026-09-29 23:10 [macd_momentum] ENTRADA TRUMP @ 1.804 (22.27 €, apertura)
- 2026-09-29 23:10 [macd_momentum_regimen] ENTRADA TRUMP @ 1.804 (22.34 €, apertura)
- 2026-09-29 23:10 [macd_momentum_evento] ENTRADA TRUMP @ 1.804 (22.58 €, apertura)
- 2026-09-29 23:10 [c_banda_atr] ENTRADA XPL @ 0.0859 (22.69 €, apertura)
- 2026-09-29 23:10 [macd_momentum] ENTRADA XPL @ 0.0859 (22.27 €, apertura)
- 2026-09-29 23:10 [macd_sin_salida] ENTRADA XPL @ 0.0859 (22.60 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_regimen] ENTRADA XPL @ 0.0859 (22.71 €, apertura)
- 2026-09-29 23:10 [macd_momentum_regimen] ENTRADA XPL @ 0.0859 (22.34 €, apertura)
- 2026-09-29 23:10 [c_banda_atr_evento] ENTRADA XPL @ 0.0859 (22.80 €, apertura)
- 2026-09-29 23:10 [macd_momentum_evento] ENTRADA XPL @ 0.0859 (22.58 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
