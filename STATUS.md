# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 13:41 UTC · vueltas 413 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.74 € (-3.52%) | 374 | 27 | 40% | +0.147% | -0.422% | -0.544% | -35.99 € |
| reversion_bb | 920.42 € (-0.41%) | 74 | 2 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 859.91 € (-6.96%) | 471 | 19 | 27% | -0.083% | -0.638% | -0.748% | -67.14 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 886.66 € (-4.07%) | 279 | 14 | 20% | -0.023% | -0.617% | -0.703% | -39.04 € |
| macd_momentum | 848.73 € (-8.17%) | 769 | 27 | 24% | +0.068% | -0.466% | -0.565% | -79.31 € |
| estocastico_rebote | 879.01 € (-4.89%) | 472 | 19 | 37% | +0.114% | -0.441% | -0.547% | -47.12 € |
| ruptura_estricta | 882.58 € (-4.51%) | 258 | 15 | 32% | -0.132% | -0.734% | -0.849% | -43.05 € |
| macd_sin_salida | 879.19 € (-4.87%) | 505 | 28 | 40% | +0.127% | -0.425% | -0.534% | -48.65 € |
| c_banda_atr_tope | 913.94 € (-1.11%) | 84 | 5 | 38% | +0.258% | -0.556% | -0.676% | -10.75 € |
| ruptura_volumen_tope | 899.94 € (-2.63%) | 142 | 5 | 23% | -0.095% | -0.780% | -0.894% | -25.29 € |
| c_banda_atr_regimen | 904.31 € (-2.16%) | 226 | 27 | 42% | +0.167% | -0.449% | -0.579% | -23.33 € |
| macd_momentum_regimen | 871.46 € (-5.71%) | 532 | 27 | 24% | +0.074% | -0.475% | -0.575% | -56.67 € |
| ruptura_volumen_regimen | 864.58 € (-6.46%) | 394 | 19 | 24% | -0.142% | -0.708% | -0.822% | -62.49 € |
| c_banda_atr_evento | 894.94 € (-3.17%) | 338 | 5 | 41% | +0.186% | -0.392% | -0.508% | -30.30 € |
| macd_momentum_evento | 851.69 € (-7.85%) | 699 | 1 | 23% | +0.069% | -0.468% | -0.564% | -72.78 € |
| ruptura_volumen_evento | 867.02 € (-6.19%) | 414 | 0 | 26% | -0.052% | -0.616% | -0.719% | -57.21 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 13:40 | ruptura_volumen_evento | JUP | timeout | +1.07% | +0.57% | +0.12 |
| 2026-10-02 13:40 | ruptura_volumen_regimen | JUP | timeout | +1.07% | +0.57% | +0.12 |
| 2026-10-02 13:40 | macd_sin_salida | SEI | timeout | -0.65% | -1.15% | -0.24 |
| 2026-10-02 13:40 | macd_sin_salida | ALGO | timeout | +0.46% | -0.04% | -0.01 |
| 2026-10-02 13:40 | macd_sin_salida | LINK | timeout | -0.13% | -0.63% | -0.14 |
| 2026-10-02 13:40 | estocastico_rebote | FIL | take-profit | +1.85% | +1.35% | +0.30 |
| 2026-10-02 13:40 | ruptura_volumen | JUP | timeout | +1.07% | +0.57% | +0.12 |
| 2026-10-02 13:35 | ruptura_volumen_regimen | APT | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 13:35 | ruptura_volumen_regimen | ZRO | take-profit | +2.68% | +2.18% | +0.47 |
| 2026-10-02 13:35 | macd_momentum_regimen | SEI | momentum perdido | -0.51% | -1.01% | -0.22 |
| 2026-10-02 13:35 | macd_momentum_regimen | SUI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 13:35 | macd_sin_salida | SUI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 13:35 | ruptura_estricta | ONDO | timeout | +0.18% | -0.32% | -0.07 |
| 2026-10-02 13:35 | estocastico_rebote | ARB | timeout | +0.99% | +0.49% | +0.11 |
| 2026-10-02 13:35 | estocastico_rebote | TAO | take-profit | +1.80% | +1.30% | +0.29 |

## Eventos de la última vuelta

- 2026-10-02 13:35 [c_banda_atr] ENTRADA ETH @ 2457.12 (22.21 €, apertura)
- 2026-10-02 13:35 [macd_momentum] ENTRADA ETH @ 2457.12 (21.12 €, apertura)
- 2026-10-02 13:35 [c_banda_atr_regimen] ENTRADA ETH @ 2457.12 (22.52 €, apertura)
- 2026-10-02 13:35 [macd_momentum_regimen] ENTRADA ETH @ 2457.12 (21.69 €, apertura)
- 2026-10-02 13:35 [c_banda_atr] ENTRADA SOL @ 109.36 (22.21 €, apertura)
- 2026-10-02 13:35 [c_banda_atr_regimen] ENTRADA SOL @ 109.36 (22.52 €, apertura)
- 2026-10-02 13:35 [c_banda_atr] ENTRADA NEAR @ 4.4054 (22.21 €, apertura)
- 2026-10-02 13:35 [c_banda_atr_regimen] ENTRADA NEAR @ 4.4054 (22.52 €, apertura)
- 2026-10-02 13:40 [macd_sin_salida] CIERRE LINK timeout bruto -0.13% neto -0.63%
- 2026-10-02 13:35 [macd_momentum] ENTRADA ADA @ 0.229446 (21.12 €, apertura)
- 2026-10-02 13:35 [estocastico_rebote] ENTRADA ADA @ 0.229446 (21.92 €, apertura)
- 2026-10-02 13:35 [macd_sin_salida] ENTRADA ADA @ 0.229446 (21.90 €, apertura)
- 2026-10-02 13:35 [macd_momentum_regimen] ENTRADA ADA @ 0.229446 (21.69 €, apertura)
- 2026-10-02 13:35 [estocastico_rebote] ENTRADA HBAR @ 0.09471 (21.92 €, apertura)
- 2026-10-02 13:35 [c_banda_atr] ENTRADA AAVE @ 163.75 (22.21 €, apertura)
- 2026-10-02 13:35 [macd_momentum] ENTRADA AAVE @ 163.75 (21.12 €, apertura)
- 2026-10-02 13:35 [macd_sin_salida] ENTRADA AAVE @ 163.75 (21.90 €, apertura)
- 2026-10-02 13:35 [c_banda_atr_regimen] ENTRADA AAVE @ 163.75 (22.52 €, apertura)
- 2026-10-02 13:35 [macd_momentum_regimen] ENTRADA AAVE @ 163.75 (21.69 €, apertura)
- 2026-10-02 13:35 [c_banda_atr] ENTRADA ZEC @ 1239.94 (22.21 €, apertura)
- 2026-10-02 13:35 [c_banda_atr_regimen] ENTRADA ZEC @ 1239.94 (22.52 €, apertura)
- 2026-10-02 13:35 [ruptura_volumen] ENTRADA XLM @ 0.201536 (21.42 €, apertura)
- 2026-10-02 13:35 [ruptura_volumen_regimen] ENTRADA XLM @ 0.201536 (21.54 €, apertura)
- 2026-10-02 13:35 [c_banda_atr] ENTRADA TAO @ 280.159 (22.21 €, apertura)
- 2026-10-02 13:35 [ruptura_estricta] ENTRADA TAO @ 280.159 (22.03 €, apertura)
- 2026-10-02 13:35 [c_banda_atr_regimen] ENTRADA TAO @ 280.159 (22.52 €, apertura)
- 2026-10-02 13:40 [macd_sin_salida] CIERRE ALGO timeout bruto +0.46% neto -0.04%
- 2026-10-02 13:35 [macd_sin_salida] ENTRADA CRV @ 0.34117 (21.90 €, apertura)
- 2026-10-02 13:40 [ruptura_volumen] CIERRE JUP timeout bruto +1.07% neto +0.57%
- 2026-10-02 13:35 [pullback_tendencia] ENTRADA JUP @ 0.29714 (22.13 €, apertura)
- 2026-10-02 13:40 [ruptura_volumen_regimen] CIERRE JUP timeout bruto +1.07% neto +0.57%
- 2026-10-02 13:40 [ruptura_volumen_evento] CIERRE JUP timeout bruto +1.07% neto +0.57%
- 2026-10-02 13:35 [pullback_tendencia] ENTRADA FIL @ 0.934 (22.13 €, apertura)
- 2026-10-02 13:40 [estocastico_rebote] CIERRE FIL take-profit bruto +1.85% neto +1.35%
- 2026-10-02 13:35 [ruptura_volumen] ENTRADA ASTER @ 0.66839 (21.43 €, apertura)
- 2026-10-02 13:35 [ruptura_volumen_regimen] ENTRADA ASTER @ 0.66839 (21.54 €, apertura)
- 2026-10-02 13:35 [estocastico_rebote] ENTRADA TRUMP @ 1.941 (21.93 €, apertura)
- 2026-10-02 13:40 [macd_sin_salida] CIERRE SEI timeout bruto -0.65% neto -1.15%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
