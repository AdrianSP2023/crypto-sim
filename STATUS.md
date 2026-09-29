# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 18:52 UTC · vueltas 110 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.84 € (-1.45%) | 57 | 6 | 35% | -0.135% | -1.093% | -1.231% | -14.38 € |
| reversion_bb | 918.85 € (-0.58%) | 15 | 3 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 910.53 € (-1.48%) | 72 | 16 | 29% | +0.026% | -0.836% | -0.974% | -13.85 € |
| rebote_extremo | 922.73 € (-0.16%) | 6 | 1 | 50% | +0.064% | -1.036% | -1.189% | -1.44 € |
| pullback_tendencia | 908.13 € (-1.74%) | 71 | 1 | 25% | -0.130% | -0.998% | -1.114% | -16.27 € |
| macd_momentum | 898.13 € (-2.83%) | 154 | 1 | 20% | -0.076% | -0.746% | -0.865% | -26.27 € |
| estocastico_rebote | 894.61 € (-3.21%) | 143 | 7 | 31% | -0.258% | -0.941% | -1.060% | -30.76 € |
| ruptura_estricta | 911.64 € (-1.36%) | 43 | 1 | 30% | -0.151% | -1.251% | -1.382% | -12.40 € |
| macd_sin_salida | 904.93 € (-2.09%) | 99 | 2 | 31% | -0.102% | -0.865% | -0.993% | -19.65 € |
| c_banda_atr_tope | 916.33 € (-0.86%) | 23 | 5 | 26% | -0.546% | -1.646% | -1.804% | -8.72 € |
| ruptura_volumen_tope | 919.70 € (-0.49%) | 22 | 5 | 23% | +0.153% | -0.947% | -1.078% | -4.81 € |
| c_banda_atr_regimen | 909.84 € (-1.56%) | 50 | 1 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.01 € (-1.65%) | 70 | 10 | 27% | -0.044% | -0.917% | -1.058% | -14.76 € |
| c_banda_atr_evento | 916.58 € (-0.83%) | 25 | 6 | 32% | -0.398% | -1.498% | -1.647% | -8.65 € |
| macd_momentum_evento | 912.13 € (-1.31%) | 34 | 1 | 18% | -0.464% | -1.564% | -1.695% | -12.27 € |
| ruptura_volumen_evento | 920.44 € (-0.41%) | 13 | 16 | 31% | -0.211% | -1.311% | -1.508% | -3.94 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 18:50 | c_banda_atr_evento | VIRTUAL | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 18:50 | ruptura_volumen_regimen | QNT | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 18:50 | estocastico_rebote | AAVE | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 18:50 | c_banda_atr | VIRTUAL | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 18:45 | ruptura_volumen_evento | NEAR | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 18:45 | macd_momentum_evento | NEAR | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 18:45 | c_banda_atr_evento | PENGU | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 18:45 | ruptura_volumen_tope | NEAR | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 18:45 | c_banda_atr_tope | PENGU | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 18:45 | macd_sin_salida | NEAR | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 18:45 | ruptura_estricta | QNT | take-profit | +3.00% | +1.90% | +0.43 |
| 2026-09-29 18:45 | estocastico_rebote | XPL | timeout | +0.57% | +0.07% | +0.02 |
| 2026-09-29 18:45 | estocastico_rebote | CRV | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-29 18:45 | macd_momentum | NEAR | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 18:45 | pullback_tendencia | PUMP | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-09-29 18:45 [ruptura_volumen] ENTRADA SOL @ 105.05 (22.76 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_regimen] ENTRADA SOL @ 105.05 (22.75 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_evento] ENTRADA SOL @ 105.05 (23.01 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_regimen] ENTRADA QNT @ 241.95 (22.75 €, apertura)
- 2026-09-29 18:50 [ruptura_volumen_regimen] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 18:45 [ruptura_volumen_regimen] ENTRADA NEAR @ 4.4989 (22.74 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen] ENTRADA ADA @ 0.216049 (22.76 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_regimen] ENTRADA ADA @ 0.216049 (22.74 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_evento] ENTRADA ADA @ 0.216049 (23.01 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen] ENTRADA SUI @ 1.0158 (22.76 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_regimen] ENTRADA SUI @ 1.0158 (22.74 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_evento] ENTRADA SUI @ 1.0158 (23.01 €, apertura)
- 2026-09-29 18:50 [estocastico_rebote] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 18:45 [ruptura_volumen_regimen] ENTRADA UNI @ 7.9349 (22.74 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen] ENTRADA PUMP @ 0.005155 (22.76 €, apertura)
- 2026-09-29 18:45 [ruptura_estricta] ENTRADA PUMP @ 0.005155 (22.80 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_regimen] ENTRADA PUMP @ 0.005155 (22.74 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_evento] ENTRADA PUMP @ 0.005155 (23.01 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen] ENTRADA DOGE @ 0.0830994 (22.76 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_regimen] ENTRADA DOGE @ 0.0830994 (22.74 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_evento] ENTRADA DOGE @ 0.0830994 (23.01 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen] ENTRADA VVV @ 24.043 (22.76 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_regimen] ENTRADA VVV @ 24.043 (22.74 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_evento] ENTRADA VVV @ 24.043 (23.01 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_regimen] ENTRADA ATOM @ 1.5337 (22.74 €, apertura)
- 2026-09-29 18:50 [c_banda_atr] CIERRE VIRTUAL take-profit bruto +2.00% neto +1.50%
- 2026-09-29 18:50 [c_banda_atr_evento] CIERRE VIRTUAL take-profit bruto +2.00% neto +0.90%
- 2026-09-29 18:45 [ruptura_volumen] ENTRADA SHIB @ 5.114e-06 (22.76 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_regimen] ENTRADA SHIB @ 5.114e-06 (22.74 €, apertura)
- 2026-09-29 18:45 [ruptura_volumen_evento] ENTRADA SHIB @ 5.114e-06 (23.01 €, apertura)
- 2026-09-29 18:45 [c_banda_atr] ENTRADA KAS @ 0.03919 (22.75 €, apertura)
- 2026-09-29 18:45 [c_banda_atr_tope] ENTRADA KAS @ 0.03919 (22.89 €, apertura)
- 2026-09-29 18:45 [c_banda_atr_regimen] ENTRADA KAS @ 0.03919 (22.75 €, apertura)
- 2026-09-29 18:45 [c_banda_atr_evento] ENTRADA KAS @ 0.03919 (22.89 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
