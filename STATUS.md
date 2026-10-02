# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 13:21 UTC · vueltas 409 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.78 € (-3.84%) | 372 | 23 | 40% | +0.141% | -0.430% | -0.551% | -36.38 € |
| reversion_bb | 920.14 € (-0.44%) | 74 | 2 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 857.58 € (-7.21%) | 465 | 20 | 26% | -0.103% | -0.659% | -0.768% | -68.37 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 885.88 € (-4.15%) | 276 | 12 | 21% | -0.019% | -0.614% | -0.700% | -38.43 € |
| macd_momentum | 846.12 € (-8.45%) | 763 | 27 | 23% | +0.062% | -0.473% | -0.572% | -79.84 € |
| estocastico_rebote | 877.50 € (-5.06%) | 468 | 20 | 37% | +0.105% | -0.451% | -0.557% | -47.77 € |
| ruptura_estricta | 880.44 € (-4.74%) | 255 | 15 | 32% | -0.147% | -0.751% | -0.866% | -43.51 € |
| macd_sin_salida | 876.63 € (-5.15%) | 498 | 30 | 40% | +0.122% | -0.431% | -0.540% | -48.69 € |
| c_banda_atr_tope | 913.42 € (-1.17%) | 84 | 5 | 38% | +0.258% | -0.556% | -0.676% | -10.75 € |
| ruptura_volumen_tope | 899.30 € (-2.70%) | 141 | 5 | 23% | -0.113% | -0.800% | -0.913% | -25.74 € |
| c_banda_atr_regimen | 901.31 € (-2.48%) | 224 | 23 | 42% | +0.156% | -0.461% | -0.590% | -23.73 € |
| macd_momentum_regimen | 868.77 € (-6.00%) | 526 | 27 | 24% | +0.065% | -0.485% | -0.584% | -57.21 € |
| ruptura_volumen_regimen | 862.23 € (-6.71%) | 388 | 20 | 24% | -0.166% | -0.734% | -0.847% | -63.73 € |
| c_banda_atr_evento | 894.33 € (-3.24%) | 337 | 6 | 41% | +0.185% | -0.393% | -0.508% | -30.29 € |
| macd_momentum_evento | 851.60 € (-7.86%) | 699 | 1 | 23% | +0.069% | -0.468% | -0.564% | -72.78 € |
| ruptura_volumen_evento | 867.33 € (-6.16%) | 411 | 3 | 26% | -0.055% | -0.619% | -0.722% | -57.12 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 13:20 | c_banda_atr_evento | SEI | timeout | +0.27% | -0.23% | -0.05 |
| 2026-10-02 13:20 | macd_momentum_regimen | AVAX | momentum perdido | -0.45% | -0.95% | -0.21 |
| 2026-10-02 13:20 | macd_momentum_regimen | LINK | momentum perdido | -0.39% | -0.89% | -0.19 |
| 2026-10-02 13:20 | macd_momentum_regimen | ETH | momentum perdido | -0.21% | -0.71% | -0.15 |
| 2026-10-02 13:20 | c_banda_atr_regimen | SEI | timeout | +0.27% | -0.23% | -0.05 |
| 2026-10-02 13:20 | estocastico_rebote | APT | take-profit | +2.12% | +1.62% | +0.36 |
| 2026-10-02 13:20 | macd_momentum | AVAX | momentum perdido | -0.45% | -0.95% | -0.20 |
| 2026-10-02 13:20 | macd_momentum | LINK | momentum perdido | -0.39% | -0.89% | -0.19 |
| 2026-10-02 13:20 | macd_momentum | ETH | momentum perdido | -0.21% | -0.71% | -0.15 |
| 2026-10-02 13:20 | pullback_tendencia | HBAR | rotura de tendencia | -0.15% | -0.65% | -0.14 |
| 2026-10-02 13:20 | c_banda_atr | SEI | timeout | +0.27% | -0.23% | -0.05 |
| 2026-10-02 13:15 | ruptura_volumen_evento | BNB | timeout | +0.37% | -0.13% | -0.03 |
| 2026-10-02 13:15 | ruptura_volumen_regimen | BNB | timeout | +0.37% | -0.13% | -0.03 |
| 2026-10-02 13:15 | macd_momentum_regimen | BTC | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-10-02 13:15 | macd_momentum | BTC | momentum perdido | -0.17% | -0.67% | -0.14 |

## Eventos de la última vuelta

- 2026-10-02 13:15 [pullback_tendencia] ENTRADA BTC @ 77066.6 (22.15 €, apertura)
- 2026-10-02 13:20 [macd_momentum] CIERRE ETH momentum perdido bruto -0.21% neto -0.71%
- 2026-10-02 13:20 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto -0.21% neto -0.71%
- 2026-10-02 13:20 [macd_momentum] CIERRE LINK momentum perdido bruto -0.39% neto -0.89%
- 2026-10-02 13:20 [macd_momentum_regimen] CIERRE LINK momentum perdido bruto -0.39% neto -0.89%
- 2026-10-02 13:20 [macd_momentum] CIERRE AVAX momentum perdido bruto -0.45% neto -0.95%
- 2026-10-02 13:20 [macd_momentum_regimen] CIERRE AVAX momentum perdido bruto -0.45% neto -0.95%
- 2026-10-02 13:20 [pullback_tendencia] CIERRE HBAR rotura de tendencia bruto -0.15% neto -0.65%
- 2026-10-02 13:15 [c_banda_atr] ENTRADA HYPE @ 81.04 (22.20 €, apertura)
- 2026-10-02 13:15 [c_banda_atr_regimen] ENTRADA HYPE @ 81.04 (22.51 €, apertura)
- 2026-10-02 13:15 [pullback_tendencia] ENTRADA ARB @ 0.1828 (22.15 €, apertura)
- 2026-10-02 13:20 [c_banda_atr] CIERRE SEI timeout bruto +0.27% neto -0.23%
- 2026-10-02 13:20 [c_banda_atr_regimen] CIERRE SEI timeout bruto +0.27% neto -0.23%
- 2026-10-02 13:20 [c_banda_atr_evento] CIERRE SEI timeout bruto +0.27% neto -0.23%
- 2026-10-02 13:20 [estocastico_rebote] CIERRE APT take-profit bruto +2.12% neto +1.62%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
