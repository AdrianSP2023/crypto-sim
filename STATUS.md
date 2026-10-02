# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 06:36 UTC · vueltas 368 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.32 € (-3.56%) | 327 | 16 | 39% | +0.122% | -0.458% | -0.578% | -34.15 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 864.03 € (-6.51%) | 400 | 11 | 27% | -0.107% | -0.672% | -0.779% | -60.28 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 891.30 € (-3.56%) | 217 | 15 | 20% | -0.063% | -0.684% | -0.770% | -33.74 € |
| macd_momentum | 856.22 € (-7.36%) | 624 | 8 | 23% | +0.049% | -0.492% | -0.594% | -68.51 € |
| estocastico_rebote | 880.54 € (-4.73%) | 377 | 35 | 36% | +0.028% | -0.541% | -0.650% | -46.20 € |
| ruptura_estricta | 886.76 € (-4.06%) | 209 | 25 | 34% | -0.161% | -0.787% | -0.902% | -37.57 € |
| macd_sin_salida | 882.53 € (-4.51%) | 413 | 24 | 40% | +0.110% | -0.453% | -0.564% | -42.69 € |
| c_banda_atr_tope | 913.88 € (-1.12%) | 73 | 5 | 36% | +0.207% | -0.655% | -0.765% | -10.99 € |
| ruptura_volumen_tope | 902.38 € (-2.37%) | 121 | 5 | 26% | -0.062% | -0.780% | -0.893% | -21.58 € |
| c_banda_atr_regimen | 903.78 € (-2.21%) | 180 | 16 | 40% | +0.134% | -0.511% | -0.638% | -21.17 € |
| macd_momentum_regimen | 879.15 € (-4.88%) | 387 | 8 | 22% | +0.046% | -0.521% | -0.625% | -45.58 € |
| ruptura_volumen_regimen | 868.72 € (-6.01%) | 323 | 11 | 24% | -0.184% | -0.765% | -0.877% | -55.59 € |
| c_banda_atr_evento | 897.25 € (-2.92%) | 294 | 16 | 40% | +0.170% | -0.420% | -0.535% | -28.23 € |
| macd_momentum_evento | 860.97 € (-6.85%) | 577 | 8 | 21% | +0.051% | -0.495% | -0.593% | -63.77 € |
| ruptura_volumen_evento | 876.32 € (-5.18%) | 350 | 11 | 28% | -0.033% | -0.608% | -0.709% | -47.99 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 06:35 | estocastico_rebote | MINA | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 06:35 | pullback_tendencia | AAVE | take-profit | +2.04% | +1.54% | +0.34 |
| 2026-10-02 06:30 | ruptura_volumen_evento | ALGO | timeout | -0.61% | -1.11% | -0.24 |
| 2026-10-02 06:30 | ruptura_volumen_evento | XRP | timeout | -0.30% | -0.80% | -0.17 |
| 2026-10-02 06:30 | c_banda_atr_evento | WLD | take-profit | +2.59% | +2.09% | +0.47 |
| 2026-10-02 06:30 | c_banda_atr_evento | ONDO | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 06:30 | ruptura_volumen_regimen | ALGO | timeout | -0.61% | -1.11% | -0.24 |
| 2026-10-02 06:30 | ruptura_volumen_regimen | XRP | timeout | -0.30% | -0.80% | -0.17 |
| 2026-10-02 06:30 | c_banda_atr_regimen | WLD | take-profit | +2.59% | +2.09% | +0.47 |
| 2026-10-02 06:30 | c_banda_atr_regimen | ONDO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 06:30 | c_banda_atr_tope | WLD | take-profit | +2.59% | +2.09% | +0.48 |
| 2026-10-02 06:30 | c_banda_atr_tope | ONDO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 06:30 | macd_sin_salida | WLD | take-profit | +2.28% | +1.78% | +0.39 |
| 2026-10-02 06:30 | ruptura_estricta | VVV | take-profit | +3.00% | +2.50% | +0.55 |
| 2026-10-02 06:30 | ruptura_estricta | WLD | take-profit | +3.32% | +2.82% | +0.62 |

## Eventos de la última vuelta

- 2026-10-02 06:35 [pullback_tendencia] CIERRE AAVE take-profit bruto +2.04% neto +1.54%
- 2026-10-02 06:30 [c_banda_atr] ENTRADA UNI @ 8.1836 (22.25 €, apertura)
- 2026-10-02 06:30 [c_banda_atr_tope] ENTRADA UNI @ 8.1836 (22.83 €, apertura)
- 2026-10-02 06:30 [c_banda_atr_regimen] ENTRADA UNI @ 8.1836 (22.58 €, apertura)
- 2026-10-02 06:30 [c_banda_atr_evento] ENTRADA UNI @ 8.1836 (22.40 €, apertura)
- 2026-10-02 06:30 [c_banda_atr] ENTRADA ARB @ 0.183 (22.25 €, apertura)
- 2026-10-02 06:30 [c_banda_atr_tope] ENTRADA ARB @ 0.183 (22.83 €, apertura)
- 2026-10-02 06:30 [c_banda_atr_regimen] ENTRADA ARB @ 0.183 (22.58 €, apertura)
- 2026-10-02 06:30 [c_banda_atr_evento] ENTRADA ARB @ 0.183 (22.40 €, apertura)
- 2026-10-02 06:30 [macd_momentum] ENTRADA FET @ 0.2106 (21.39 €, apertura)
- 2026-10-02 06:30 [macd_sin_salida] ENTRADA FET @ 0.2106 (22.04 €, apertura)
- 2026-10-02 06:30 [macd_momentum_regimen] ENTRADA FET @ 0.2106 (21.97 €, apertura)
- 2026-10-02 06:30 [macd_momentum_evento] ENTRADA FET @ 0.2106 (21.51 €, apertura)
- 2026-10-02 06:30 [c_banda_atr] ENTRADA POL @ 0.09777 (22.25 €, apertura)
- 2026-10-02 06:30 [c_banda_atr_regimen] ENTRADA POL @ 0.09777 (22.58 €, apertura)
- 2026-10-02 06:30 [c_banda_atr_evento] ENTRADA POL @ 0.09777 (22.40 €, apertura)
- 2026-10-02 06:30 [macd_momentum] ENTRADA ONDO @ 0.45058 (21.39 €, apertura)
- 2026-10-02 06:30 [macd_sin_salida] ENTRADA ONDO @ 0.45058 (22.04 €, apertura)
- 2026-10-02 06:30 [macd_momentum_regimen] ENTRADA ONDO @ 0.45058 (21.97 €, apertura)
- 2026-10-02 06:30 [macd_momentum_evento] ENTRADA ONDO @ 0.45058 (21.51 €, apertura)
- 2026-10-02 06:30 [ruptura_volumen] ENTRADA WLD @ 0.4806 (21.60 €, apertura)
- 2026-10-02 06:30 [ruptura_volumen_regimen] ENTRADA WLD @ 0.4806 (21.72 €, apertura)
- 2026-10-02 06:30 [ruptura_volumen_evento] ENTRADA WLD @ 0.4806 (21.91 €, apertura)
- 2026-10-02 06:35 [estocastico_rebote] CIERRE MINA take-profit bruto +1.80% neto +1.30%
- 2026-10-02 06:30 [ruptura_volumen] ENTRADA KAS @ 0.03809 (21.60 €, apertura)
- 2026-10-02 06:30 [macd_momentum] ENTRADA KAS @ 0.03809 (21.39 €, apertura)
- 2026-10-02 06:30 [macd_momentum_regimen] ENTRADA KAS @ 0.03809 (21.97 €, apertura)
- 2026-10-02 06:30 [ruptura_volumen_regimen] ENTRADA KAS @ 0.03809 (21.72 €, apertura)
- 2026-10-02 06:30 [macd_momentum_evento] ENTRADA KAS @ 0.03809 (21.51 €, apertura)
- 2026-10-02 06:30 [ruptura_volumen_evento] ENTRADA KAS @ 0.03809 (21.91 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
