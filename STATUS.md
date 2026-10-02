# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 06:41 UTC · vueltas 369 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.71 € (-3.63%) | 328 | 18 | 39% | +0.123% | -0.456% | -0.576% | -34.13 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 863.69 € (-6.55%) | 400 | 11 | 27% | -0.107% | -0.672% | -0.779% | -60.28 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 891.00 € (-3.60%) | 217 | 16 | 20% | -0.063% | -0.684% | -0.770% | -33.74 € |
| macd_momentum | 855.79 € (-7.41%) | 625 | 12 | 23% | +0.049% | -0.493% | -0.594% | -68.66 € |
| estocastico_rebote | 879.51 € (-4.84%) | 378 | 34 | 36% | +0.029% | -0.540% | -0.649% | -46.28 € |
| ruptura_estricta | 886.19 € (-4.12%) | 209 | 25 | 34% | -0.161% | -0.787% | -0.902% | -37.57 € |
| macd_sin_salida | 882.06 € (-4.56%) | 413 | 27 | 40% | +0.110% | -0.453% | -0.564% | -42.69 € |
| c_banda_atr_tope | 913.59 € (-1.15%) | 74 | 5 | 36% | +0.212% | -0.645% | -0.756% | -10.97 € |
| ruptura_volumen_tope | 902.21 € (-2.38%) | 122 | 4 | 25% | -0.066% | -0.783% | -0.895% | -21.84 € |
| c_banda_atr_regimen | 903.18 € (-2.28%) | 181 | 18 | 40% | +0.137% | -0.507% | -0.635% | -21.15 € |
| macd_momentum_regimen | 878.71 € (-4.93%) | 388 | 12 | 22% | +0.045% | -0.522% | -0.625% | -45.73 € |
| ruptura_volumen_regimen | 868.38 € (-6.04%) | 323 | 11 | 24% | -0.184% | -0.765% | -0.877% | -55.59 € |
| c_banda_atr_evento | 896.63 € (-2.99%) | 295 | 18 | 40% | +0.172% | -0.418% | -0.533% | -28.21 € |
| macd_momentum_evento | 860.54 € (-6.89%) | 578 | 12 | 21% | +0.051% | -0.495% | -0.594% | -63.92 € |
| ruptura_volumen_evento | 875.98 € (-5.22%) | 350 | 11 | 28% | -0.033% | -0.608% | -0.709% | -47.99 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 06:40 | macd_momentum_evento | WLFI | momentum perdido | -0.20% | -0.70% | -0.15 |
| 2026-10-02 06:40 | c_banda_atr_evento | WLFI | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-02 06:40 | macd_momentum_regimen | WLFI | momentum perdido | -0.20% | -0.70% | -0.15 |
| 2026-10-02 06:40 | c_banda_atr_regimen | WLFI | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-02 06:40 | ruptura_volumen_tope | BNB | timeout | -0.64% | -1.14% | -0.26 |
| 2026-10-02 06:40 | c_banda_atr_tope | WLFI | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-02 06:40 | estocastico_rebote | LINK | timeout | +0.11% | -0.39% | -0.08 |
| 2026-10-02 06:40 | macd_momentum | WLFI | momentum perdido | -0.20% | -0.70% | -0.15 |
| 2026-10-02 06:40 | c_banda_atr | WLFI | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-02 06:35 | estocastico_rebote | MINA | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 06:35 | pullback_tendencia | AAVE | take-profit | +2.04% | +1.54% | +0.34 |
| 2026-10-02 06:30 | ruptura_volumen_evento | ALGO | timeout | -0.61% | -1.11% | -0.24 |
| 2026-10-02 06:30 | ruptura_volumen_evento | XRP | timeout | -0.30% | -0.80% | -0.17 |
| 2026-10-02 06:30 | c_banda_atr_evento | WLD | take-profit | +2.59% | +2.09% | +0.47 |
| 2026-10-02 06:30 | c_banda_atr_evento | ONDO | take-profit | +2.00% | +1.50% | +0.33 |

## Eventos de la última vuelta

- 2026-10-02 06:35 [macd_momentum] ENTRADA XRP @ 1.35532 (21.39 €, apertura)
- 2026-10-02 06:35 [macd_sin_salida] ENTRADA XRP @ 1.35532 (22.04 €, apertura)
- 2026-10-02 06:35 [macd_momentum_regimen] ENTRADA XRP @ 1.35532 (21.97 €, apertura)
- 2026-10-02 06:35 [macd_momentum_evento] ENTRADA XRP @ 1.35532 (21.51 €, apertura)
- 2026-10-02 06:35 [macd_momentum] ENTRADA ETH @ 2424.91 (21.39 €, apertura)
- 2026-10-02 06:35 [macd_momentum_regimen] ENTRADA ETH @ 2424.91 (21.97 €, apertura)
- 2026-10-02 06:35 [macd_momentum_evento] ENTRADA ETH @ 2424.91 (21.51 €, apertura)
- 2026-10-02 06:40 [estocastico_rebote] CIERRE LINK timeout bruto +0.11% neto -0.39%
- 2026-10-02 06:35 [c_banda_atr] ENTRADA AVAX @ 9.855 (22.25 €, apertura)
- 2026-10-02 06:35 [c_banda_atr_regimen] ENTRADA AVAX @ 9.855 (22.58 €, apertura)
- 2026-10-02 06:35 [c_banda_atr_evento] ENTRADA AVAX @ 9.855 (22.40 €, apertura)
- 2026-10-02 06:35 [macd_momentum] ENTRADA AAVE @ 164.09 (21.39 €, apertura)
- 2026-10-02 06:35 [macd_sin_salida] ENTRADA AAVE @ 164.09 (22.04 €, apertura)
- 2026-10-02 06:35 [macd_momentum_regimen] ENTRADA AAVE @ 164.09 (21.97 €, apertura)
- 2026-10-02 06:35 [macd_momentum_evento] ENTRADA AAVE @ 164.09 (21.51 €, apertura)
- 2026-10-02 06:35 [c_banda_atr] ENTRADA TAO @ 275.487 (22.25 €, apertura)
- 2026-10-02 06:35 [c_banda_atr_regimen] ENTRADA TAO @ 275.487 (22.58 €, apertura)
- 2026-10-02 06:35 [c_banda_atr_evento] ENTRADA TAO @ 275.487 (22.40 €, apertura)
- 2026-10-02 06:35 [pullback_tendencia] ENTRADA FET @ 0.2108 (22.26 €, apertura)
- 2026-10-02 06:35 [macd_momentum] ENTRADA CRV @ 0.33805 (21.39 €, apertura)
- 2026-10-02 06:35 [macd_momentum_regimen] ENTRADA CRV @ 0.33805 (21.97 €, apertura)
- 2026-10-02 06:35 [macd_momentum_evento] ENTRADA CRV @ 0.33805 (21.51 €, apertura)
- 2026-10-02 06:40 [c_banda_atr] CIERRE WLFI timeout bruto +0.60% neto +0.10%
- 2026-10-02 06:40 [macd_momentum] CIERRE WLFI momentum perdido bruto -0.20% neto -0.70%
- 2026-10-02 06:40 [c_banda_atr_tope] CIERRE WLFI timeout bruto +0.60% neto +0.10%
- 2026-10-02 06:40 [c_banda_atr_regimen] CIERRE WLFI timeout bruto +0.60% neto +0.10%
- 2026-10-02 06:40 [macd_momentum_regimen] CIERRE WLFI momentum perdido bruto -0.20% neto -0.70%
- 2026-10-02 06:40 [c_banda_atr_evento] CIERRE WLFI timeout bruto +0.60% neto +0.10%
- 2026-10-02 06:40 [macd_momentum_evento] CIERRE WLFI momentum perdido bruto -0.20% neto -0.70%
- 2026-10-02 06:35 [macd_momentum] ENTRADA SHIB @ 5.243e-06 (21.39 €, apertura)
- 2026-10-02 06:35 [macd_sin_salida] ENTRADA SHIB @ 5.243e-06 (22.04 €, apertura)
- 2026-10-02 06:35 [macd_momentum_regimen] ENTRADA SHIB @ 5.243e-06 (21.96 €, apertura)
- 2026-10-02 06:35 [macd_momentum_evento] ENTRADA SHIB @ 5.243e-06 (21.51 €, apertura)
- 2026-10-02 06:35 [c_banda_atr] ENTRADA TRUMP @ 1.865 (22.25 €, apertura)
- 2026-10-02 06:35 [c_banda_atr_tope] ENTRADA TRUMP @ 1.865 (22.83 €, apertura)
- 2026-10-02 06:35 [c_banda_atr_regimen] ENTRADA TRUMP @ 1.865 (22.58 €, apertura)
- 2026-10-02 06:35 [c_banda_atr_evento] ENTRADA TRUMP @ 1.865 (22.40 €, apertura)
- 2026-10-02 06:40 [ruptura_volumen_tope] CIERRE BNB timeout bruto -0.64% neto -1.14%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
