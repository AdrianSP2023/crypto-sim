# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 09:41 UTC · vueltas 202 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 896.78 € (-2.97%) | 161 | 24 | 29% | -0.161% | -0.823% | -0.951% | -30.28 € |
| reversion_bb | 915.17 € (-0.98%) | 43 | 3 | 42% | +0.124% | -0.962% | -1.072% | -9.52 € |
| ruptura_volumen | 887.97 € (-3.92%) | 190 | 29 | 20% | -0.247% | -0.884% | -1.015% | -38.15 € |
| rebote_extremo | 923.34 € (-0.10%) | 10 | 0 | 60% | +0.710% | -0.389% | -0.540% | -0.90 € |
| pullback_tendencia | 901.82 € (-2.43%) | 123 | 5 | 24% | -0.094% | -0.806% | -0.933% | -22.68 € |
| macd_momentum | 877.79 € (-5.03%) | 346 | 26 | 17% | -0.074% | -0.649% | -0.761% | -50.65 € |
| estocastico_rebote | 888.71 € (-3.84%) | 230 | 8 | 36% | -0.084% | -0.697% | -0.830% | -36.53 € |
| ruptura_estricta | 902.39 € (-2.36%) | 81 | 17 | 22% | -0.396% | -1.218% | -1.368% | -22.60 € |
| macd_sin_salida | 891.43 € (-3.55%) | 215 | 31 | 28% | -0.137% | -0.758% | -0.879% | -37.04 € |
| c_banda_atr_tope | 910.54 € (-1.48%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.90 € (-1.66%) | 69 | 5 | 20% | -0.102% | -0.985% | -1.108% | -15.59 € |
| c_banda_atr_regimen | 900.94 € (-2.52%) | 78 | 6 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.64 € (-4.18%) | 205 | 10 | 14% | -0.224% | -0.852% | -0.966% | -39.61 € |
| ruptura_volumen_regimen | 895.55 € (-3.10%) | 129 | 26 | 17% | -0.297% | -0.999% | -1.130% | -29.37 € |
| c_banda_atr_evento | 899.83 € (-2.64%) | 129 | 24 | 26% | -0.218% | -0.922% | -1.051% | -27.23 € |
| macd_momentum_evento | 890.13 € (-3.69%) | 226 | 26 | 15% | -0.131% | -0.748% | -0.857% | -38.36 € |
| ruptura_volumen_evento | 893.44 € (-3.33%) | 131 | 29 | 15% | -0.394% | -1.095% | -1.228% | -32.69 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 09:40 | ruptura_volumen_evento | XLM | timeout | +1.45% | +0.95% | +0.21 |
| 2026-09-30 09:40 | ruptura_volumen_evento | NEAR | timeout | +1.56% | +1.06% | +0.24 |
| 2026-09-30 09:40 | macd_momentum_evento | XPL | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 09:40 | c_banda_atr_evento | XPL | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 09:40 | ruptura_volumen_tope | NEAR | timeout | +1.56% | +1.06% | +0.24 |
| 2026-09-30 09:40 | macd_sin_salida | XPL | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 09:40 | estocastico_rebote | QNT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-09-30 09:40 | estocastico_rebote | XRP | timeout | +0.98% | +0.48% | +0.11 |
| 2026-09-30 09:40 | macd_momentum | XPL | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 09:40 | ruptura_volumen | XLM | timeout | +1.45% | +0.95% | +0.21 |
| 2026-09-30 09:40 | ruptura_volumen | NEAR | timeout | +1.56% | +1.06% | +0.23 |
| 2026-09-30 09:40 | c_banda_atr | XPL | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 09:35 | ruptura_volumen_evento | VVV | timeout | +0.77% | +0.27% | +0.06 |
| 2026-09-30 09:35 | c_banda_atr_evento | ATOM | timeout | +0.43% | -0.07% | -0.02 |
| 2026-09-30 09:35 | c_banda_atr_evento | JUP | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-09-30 09:35 [ruptura_volumen] ENTRADA XRP @ 1.33303 (22.14 €, apertura)
- 2026-09-30 09:40 [estocastico_rebote] CIERRE XRP timeout bruto +0.98% neto +0.48%
- 2026-09-30 09:35 [ruptura_estricta] ENTRADA XRP @ 1.33303 (22.54 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_regimen] ENTRADA XRP @ 1.33303 (22.37 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_evento] ENTRADA XRP @ 1.33303 (22.28 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen] ENTRADA ETH @ 2370.52 (22.14 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_regimen] ENTRADA ETH @ 2370.52 (22.37 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_evento] ENTRADA ETH @ 2370.52 (22.28 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen] ENTRADA SOL @ 105.23 (22.14 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_regimen] ENTRADA SOL @ 105.23 (22.37 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_evento] ENTRADA SOL @ 105.23 (22.28 €, apertura)
- 2026-09-30 09:40 [estocastico_rebote] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 09:40 [ruptura_volumen] CIERRE NEAR timeout bruto +1.56% neto +1.06%
- 2026-09-30 09:40 [ruptura_volumen_tope] CIERRE NEAR timeout bruto +1.56% neto +1.06%
- 2026-09-30 09:40 [ruptura_volumen_evento] CIERRE NEAR timeout bruto +1.56% neto +1.06%
- 2026-09-30 09:35 [ruptura_volumen] ENTRADA ADA @ 0.219106 (22.15 €, apertura)
- 2026-09-30 09:35 [ruptura_estricta] ENTRADA ADA @ 0.219106 (22.54 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_tope] ENTRADA ADA @ 0.219106 (22.72 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_regimen] ENTRADA ADA @ 0.219106 (22.37 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_evento] ENTRADA ADA @ 0.219106 (22.28 €, apertura)
- 2026-09-30 09:40 [ruptura_volumen] CIERRE XLM timeout bruto +1.45% neto +0.95%
- 2026-09-30 09:40 [ruptura_volumen_evento] CIERRE XLM timeout bruto +1.45% neto +0.95%
- 2026-09-30 09:35 [ruptura_estricta] ENTRADA HYPE @ 76.23 (22.54 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen] ENTRADA ARB @ 0.1811 (22.15 €, apertura)
- 2026-09-30 09:35 [ruptura_estricta] ENTRADA ARB @ 0.1811 (22.54 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_regimen] ENTRADA ARB @ 0.1811 (22.37 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_evento] ENTRADA ARB @ 0.1811 (22.29 €, apertura)
- 2026-09-30 09:35 [pullback_tendencia] ENTRADA XDC @ 0.03041 (22.54 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen] ENTRADA DOGE @ 0.0832 (22.15 €, apertura)
- 2026-09-30 09:35 [ruptura_estricta] ENTRADA DOGE @ 0.0832 (22.54 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_regimen] ENTRADA DOGE @ 0.0832 (22.37 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_evento] ENTRADA DOGE @ 0.0832 (22.29 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_regimen] ENTRADA DOT @ 1.0967 (22.37 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen] ENTRADA CRV @ 0.36056 (22.15 €, apertura)
- 2026-09-30 09:35 [ruptura_estricta] ENTRADA CRV @ 0.36056 (22.54 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_regimen] ENTRADA CRV @ 0.36056 (22.37 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_evento] ENTRADA CRV @ 0.36056 (22.29 €, apertura)
- 2026-09-30 09:35 [ruptura_estricta] ENTRADA BCH @ 273.31 (22.54 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen] ENTRADA RAY @ 1.675 (22.15 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_regimen] ENTRADA RAY @ 1.675 (22.37 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_evento] ENTRADA RAY @ 1.675 (22.29 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_regimen] ENTRADA OP @ 0.1181 (22.37 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen] ENTRADA FIL @ 0.952 (22.15 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_regimen] ENTRADA FIL @ 0.952 (22.37 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_evento] ENTRADA FIL @ 0.952 (22.29 €, apertura)
- 2026-09-30 09:35 [ruptura_estricta] ENTRADA PENGU @ 0.008777 (22.54 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen] ENTRADA BNB @ 673.78 (22.15 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_regimen] ENTRADA BNB @ 673.78 (22.37 €, apertura)
- 2026-09-30 09:35 [ruptura_volumen_evento] ENTRADA BNB @ 673.78 (22.29 €, apertura)
- 2026-09-30 09:40 [c_banda_atr] CIERRE XPL take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:40 [macd_momentum] CIERRE XPL take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:35 [ruptura_estricta] ENTRADA XPL @ 0.0865 (22.54 €, apertura)
- 2026-09-30 09:40 [macd_sin_salida] CIERRE XPL take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:40 [c_banda_atr_evento] CIERRE XPL take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:40 [macd_momentum_evento] CIERRE XPL take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:35 [macd_momentum] ENTRADA SPX @ 0.3783 (21.84 €, apertura)
- 2026-09-30 09:35 [macd_momentum_regimen] ENTRADA SPX @ 0.3783 (22.12 €, apertura)
- 2026-09-30 09:35 [macd_momentum_evento] ENTRADA SPX @ 0.3783 (22.15 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
