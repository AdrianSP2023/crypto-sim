# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 13:51 UTC · vueltas 415 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.91 € (-3.93%) | 375 | 28 | 40% | +0.143% | -0.427% | -0.548% | -36.43 € |
| reversion_bb | 920.10 € (-0.45%) | 74 | 2 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 858.14 € (-7.15%) | 472 | 23 | 27% | -0.077% | -0.633% | -0.743% | -66.71 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 885.11 € (-4.23%) | 282 | 12 | 20% | -0.026% | -0.619% | -0.704% | -39.57 € |
| macd_momentum | 845.14 € (-8.56%) | 770 | 34 | 24% | +0.069% | -0.465% | -0.564% | -79.29 € |
| estocastico_rebote | 876.60 € (-5.15%) | 473 | 19 | 37% | +0.114% | -0.441% | -0.547% | -47.27 € |
| ruptura_estricta | 880.98 € (-4.68%) | 258 | 17 | 32% | -0.132% | -0.734% | -0.849% | -43.05 € |
| macd_sin_salida | 875.49 € (-5.27%) | 507 | 31 | 40% | +0.130% | -0.421% | -0.531% | -48.49 € |
| c_banda_atr_tope | 913.34 € (-1.18%) | 84 | 5 | 38% | +0.258% | -0.556% | -0.676% | -10.75 € |
| ruptura_volumen_tope | 899.24 € (-2.70%) | 142 | 5 | 23% | -0.095% | -0.780% | -0.894% | -25.29 € |
| c_banda_atr_regimen | 900.42 € (-2.58%) | 227 | 28 | 41% | +0.159% | -0.456% | -0.585% | -23.78 € |
| macd_momentum_regimen | 867.77 € (-6.11%) | 533 | 34 | 24% | +0.075% | -0.474% | -0.574% | -56.65 € |
| ruptura_volumen_regimen | 862.80 € (-6.65%) | 395 | 23 | 25% | -0.135% | -0.701% | -0.816% | -62.06 € |
| c_banda_atr_evento | 894.38 € (-3.23%) | 338 | 5 | 41% | +0.186% | -0.392% | -0.508% | -30.30 € |
| macd_momentum_evento | 851.50 € (-7.87%) | 700 | 0 | 23% | +0.070% | -0.468% | -0.564% | -72.75 € |
| ruptura_volumen_evento | 867.02 € (-6.19%) | 414 | 0 | 26% | -0.052% | -0.616% | -0.719% | -57.21 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 13:50 | macd_momentum_evento | WLFI | momentum perdido | +0.60% | +0.10% | +0.02 |
| 2026-10-02 13:50 | macd_momentum_regimen | WLFI | momentum perdido | +0.60% | +0.10% | +0.02 |
| 2026-10-02 13:50 | macd_sin_salida | WLFI | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-02 13:50 | macd_sin_salida | OP | timeout | +1.10% | +0.60% | +0.13 |
| 2026-10-02 13:50 | macd_momentum | WLFI | momentum perdido | +0.60% | +0.10% | +0.02 |
| 2026-10-02 13:50 | pullback_tendencia | BCH | rotura de tendencia | -0.19% | -0.69% | -0.15 |
| 2026-10-02 13:50 | pullback_tendencia | XLM | rotura de tendencia | -0.31% | -0.81% | -0.18 |
| 2026-10-02 13:50 | pullback_tendencia | HYPE | rotura de tendencia | -0.41% | -0.91% | -0.20 |
| 2026-10-02 13:45 | ruptura_volumen_regimen | WLD | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 13:45 | c_banda_atr_regimen | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 13:45 | estocastico_rebote | ASTER | timeout | -0.20% | -0.69% | -0.15 |
| 2026-10-02 13:45 | ruptura_volumen | WLD | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 13:45 | c_banda_atr | QNT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 13:40 | ruptura_volumen_evento | JUP | timeout | +1.07% | +0.57% | +0.12 |
| 2026-10-02 13:40 | ruptura_volumen_regimen | JUP | timeout | +1.07% | +0.57% | +0.12 |

## Eventos de la última vuelta

- 2026-10-02 13:45 [pullback_tendencia] ENTRADA HYPE @ 81.06 (22.13 €, apertura)
- 2026-10-02 13:50 [pullback_tendencia] CIERRE HYPE rotura de tendencia bruto -0.41% neto -0.91%
- 2026-10-02 13:50 [pullback_tendencia] CIERRE XLM rotura de tendencia bruto -0.31% neto -0.81%
- 2026-10-02 13:45 [macd_momentum] ENTRADA XDC @ 0.03027 (21.12 €, apertura)
- 2026-10-02 13:45 [macd_sin_salida] ENTRADA XDC @ 0.03027 (21.89 €, apertura)
- 2026-10-02 13:45 [macd_momentum_regimen] ENTRADA XDC @ 0.03027 (21.69 €, apertura)
- 2026-10-02 13:50 [pullback_tendencia] CIERRE BCH rotura de tendencia bruto -0.19% neto -0.69%
- 2026-10-02 13:50 [macd_sin_salida] CIERRE OP timeout bruto +1.10% neto +0.60%
- 2026-10-02 13:45 [macd_momentum] ENTRADA VVV @ 26.662 (21.12 €, apertura)
- 2026-10-02 13:45 [macd_sin_salida] ENTRADA VVV @ 26.662 (21.89 €, apertura)
- 2026-10-02 13:45 [macd_momentum_regimen] ENTRADA VVV @ 26.662 (21.69 €, apertura)
- 2026-10-02 13:50 [macd_momentum] CIERRE WLFI momentum perdido bruto +0.60% neto +0.10%
- 2026-10-02 13:50 [macd_sin_salida] CIERRE WLFI timeout bruto +0.60% neto +0.10%
- 2026-10-02 13:50 [macd_momentum_regimen] CIERRE WLFI momentum perdido bruto +0.60% neto +0.10%
- 2026-10-02 13:50 [macd_momentum_evento] CIERRE WLFI momentum perdido bruto +0.60% neto +0.10%
- 2026-10-02 13:45 [c_banda_atr] ENTRADA SHIB @ 5.28e-06 (22.19 €, apertura)
- 2026-10-02 13:45 [macd_momentum] ENTRADA SHIB @ 5.28e-06 (21.12 €, apertura)
- 2026-10-02 13:45 [macd_sin_salida] ENTRADA SHIB @ 5.28e-06 (21.89 €, apertura)
- 2026-10-02 13:45 [c_banda_atr_regimen] ENTRADA SHIB @ 5.28e-06 (22.51 €, apertura)
- 2026-10-02 13:45 [macd_momentum_regimen] ENTRADA SHIB @ 5.28e-06 (21.69 €, apertura)
- 2026-10-02 13:45 [ruptura_estricta] ENTRADA KSM @ 4.68 (22.03 €, apertura)
- 2026-10-02 13:45 [estocastico_rebote] ENTRADA SKY @ 0.08178 (21.92 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
