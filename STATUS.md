# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 01:41 UTC · vueltas 355 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 883.96 € (-4.36%) | 274 | 26 | 34% | -0.038% | -0.634% | -0.755% | -39.43 € |
| reversion_bb | 916.96 € (-0.79%) | 58 | 14 | 52% | +0.367% | -0.583% | -0.693% | -7.79 € |
| ruptura_volumen | 866.28 € (-6.27%) | 309 | 27 | 24% | -0.226% | -0.811% | -0.918% | -56.32 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.07 € (-3.91%) | 193 | 5 | 15% | -0.201% | -0.837% | -0.925% | -36.66 € |
| macd_momentum | 861.05 € (-6.84%) | 512 | 8 | 21% | +0.001% | -0.550% | -0.652% | -62.94 € |
| estocastico_rebote | 872.15 € (-5.64%) | 339 | 15 | 32% | -0.096% | -0.673% | -0.783% | -51.46 € |
| ruptura_estricta | 881.72 € (-4.60%) | 167 | 13 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 870.32 € (-5.83%) | 356 | 16 | 34% | -0.093% | -0.667% | -0.778% | -53.60 € |
| c_banda_atr_tope | 911.44 € (-1.39%) | 64 | 5 | 30% | +0.028% | -0.884% | -1.001% | -13.00 € |
| ruptura_volumen_tope | 903.86 € (-2.21%) | 106 | 5 | 25% | -0.064% | -0.813% | -0.927% | -19.73 € |
| c_banda_atr_regimen | 895.74 € (-3.08%) | 139 | 7 | 29% | -0.197% | -0.885% | -1.018% | -28.14 € |
| macd_momentum_regimen | 884.34 € (-4.32%) | 285 | 0 | 20% | -0.026% | -0.618% | -0.723% | -39.89 € |
| ruptura_volumen_regimen | 870.33 € (-5.83%) | 239 | 21 | 19% | -0.372% | -0.981% | -1.095% | -52.84 € |
| c_banda_atr_evento | 889.85 € (-3.72%) | 241 | 26 | 34% | -0.001% | -0.611% | -0.727% | -33.53 € |
| macd_momentum_evento | 865.82 € (-6.32%) | 465 | 8 | 19% | -0.001% | -0.558% | -0.657% | -58.17 € |
| ruptura_volumen_evento | 878.61 € (-4.94%) | 259 | 27 | 24% | -0.149% | -0.751% | -0.850% | -43.96 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 01:40 | ruptura_volumen_evento | ONDO | timeout | -0.64% | -1.14% | -0.25 |
| 2026-10-02 01:40 | macd_momentum_evento | USELESS | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 01:40 | ruptura_volumen_tope | ONDO | timeout | -0.64% | -1.14% | -0.26 |
| 2026-10-02 01:40 | macd_momentum | USELESS | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 01:40 | ruptura_volumen | ONDO | timeout | -0.64% | -1.14% | -0.25 |
| 2026-10-02 01:40 | reversion_bb | XDC | timeout | -0.07% | -0.57% | -0.13 |
| 2026-10-02 01:35 | ruptura_volumen_evento | LINK | timeout | -0.70% | -1.20% | -0.27 |
| 2026-10-02 01:35 | macd_momentum_evento | LTC | momentum perdido | +0.89% | +0.39% | +0.08 |
| 2026-10-02 01:35 | macd_momentum_evento | AAVE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 01:35 | c_banda_atr_evento | WLFI | timeout | +0.40% | -0.10% | -0.02 |
| 2026-10-02 01:35 | macd_momentum_regimen | AAVE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 01:35 | c_banda_atr_regimen | AAVE | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 01:35 | ruptura_volumen_tope | LINK | timeout | -0.70% | -1.20% | -0.27 |
| 2026-10-02 01:35 | c_banda_atr_tope | WLFI | timeout | +0.40% | -0.10% | -0.02 |
| 2026-10-02 01:35 | macd_momentum | LTC | momentum perdido | +0.89% | +0.39% | +0.08 |

## Eventos de la última vuelta

- 2026-10-02 01:35 [macd_momentum] ENTRADA TAO @ 269.003 (21.54 €, apertura)
- 2026-10-02 01:35 [macd_momentum_evento] ENTRADA TAO @ 269.003 (21.65 €, apertura)
- 2026-10-02 01:35 [pullback_tendencia] ENTRADA ARB @ 0.1783 (22.19 €, apertura)
- 2026-10-02 01:35 [c_banda_atr] ENTRADA FET @ 0.2069 (22.12 €, apertura)
- 2026-10-02 01:35 [c_banda_atr_tope] ENTRADA FET @ 0.2069 (22.78 €, apertura)
- 2026-10-02 01:35 [c_banda_atr_evento] ENTRADA FET @ 0.2069 (22.27 €, apertura)
- 2026-10-02 01:35 [macd_momentum] ENTRADA POL @ 0.09582 (21.54 €, apertura)
- 2026-10-02 01:35 [macd_momentum_evento] ENTRADA POL @ 0.09582 (21.65 €, apertura)
- 2026-10-02 01:40 [ruptura_volumen] CIERRE ONDO timeout bruto -0.64% neto -1.14%
- 2026-10-02 01:40 [ruptura_volumen_tope] CIERRE ONDO timeout bruto -0.64% neto -1.14%
- 2026-10-02 01:40 [ruptura_volumen_evento] CIERRE ONDO timeout bruto -0.64% neto -1.14%
- 2026-10-02 01:40 [reversion_bb] CIERRE XDC timeout bruto -0.07% neto -0.57%
- 2026-10-02 01:40 [macd_momentum] CIERRE USELESS momentum perdido bruto +0.00% neto -0.50%
- 2026-10-02 01:40 [macd_momentum_evento] CIERRE USELESS momentum perdido bruto +0.00% neto -0.50%
- 2026-10-02 01:35 [macd_momentum] ENTRADA INJ @ 6.625 (21.53 €, apertura)
- 2026-10-02 01:35 [macd_sin_salida] ENTRADA INJ @ 6.625 (21.77 €, apertura)
- 2026-10-02 01:35 [macd_momentum_evento] ENTRADA INJ @ 6.625 (21.65 €, apertura)
- 2026-10-02 01:35 [ruptura_volumen] ENTRADA OP @ 0.1149 (21.70 €, apertura)
- 2026-10-02 01:35 [ruptura_estricta] ENTRADA OP @ 0.1149 (22.06 €, apertura)
- 2026-10-02 01:35 [ruptura_volumen_tope] ENTRADA OP @ 0.1149 (22.61 €, apertura)
- 2026-10-02 01:35 [ruptura_volumen_evento] ENTRADA OP @ 0.1149 (22.01 €, apertura)
- 2026-10-02 01:35 [ruptura_volumen] ENTRADA VVV @ 23.507 (21.70 €, apertura)
- 2026-10-02 01:35 [macd_momentum] ENTRADA VVV @ 23.507 (21.53 €, apertura)
- 2026-10-02 01:35 [ruptura_estricta] ENTRADA VVV @ 23.507 (22.06 €, apertura)
- 2026-10-02 01:35 [macd_sin_salida] ENTRADA VVV @ 23.507 (21.77 €, apertura)
- 2026-10-02 01:35 [macd_momentum_evento] ENTRADA VVV @ 23.507 (21.65 €, apertura)
- 2026-10-02 01:35 [ruptura_volumen_evento] ENTRADA VVV @ 23.507 (22.01 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
