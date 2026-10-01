# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 03:36 UTC · vueltas 114 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 904.16 € (-2.17%) | 106 | 27 | 29% | -0.175% | -0.921% | -1.044% | -22.40 € |
| reversion_bb | 921.56 € (-0.29%) | 13 | 5 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 890.99 € (-3.60%) | 144 | 12 | 19% | -0.355% | -1.037% | -1.149% | -34.03 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.05 € (-2.29%) | 85 | 5 | 15% | -0.312% | -1.123% | -1.240% | -21.85 € |
| macd_momentum | 896.18 € (-3.04%) | 190 | 28 | 21% | -0.029% | -0.667% | -0.775% | -28.89 € |
| estocastico_rebote | 902.73 € (-2.33%) | 154 | 15 | 38% | +0.063% | -0.607% | -0.727% | -21.50 € |
| ruptura_estricta | 900.37 € (-2.58%) | 67 | 17 | 22% | -0.708% | -1.602% | -1.741% | -24.71 € |
| macd_sin_salida | 903.70 € (-2.22%) | 126 | 38 | 37% | -0.035% | -0.742% | -0.859% | -21.49 € |
| c_banda_atr_tope | 917.93 € (-0.68%) | 26 | 5 | 27% | -0.029% | -1.129% | -1.255% | -6.77 € |
| ruptura_volumen_tope | 914.45 € (-1.06%) | 41 | 5 | 22% | +0.040% | -1.060% | -1.161% | -10.00 € |
| c_banda_atr_regimen | 908.93 € (-1.66%) | 55 | 22 | 25% | -0.370% | -1.345% | -1.492% | -17.02 € |
| macd_momentum_regimen | 905.26 € (-2.05%) | 103 | 29 | 19% | -0.099% | -0.853% | -0.969% | -20.15 € |
| ruptura_volumen_regimen | 891.75 € (-3.52%) | 117 | 12 | 13% | -0.524% | -1.247% | -1.365% | -33.29 € |
| c_banda_atr_evento | 910.17 € (-1.52%) | 73 | 27 | 29% | -0.114% | -0.976% | -1.082% | -16.39 € |
| macd_momentum_evento | 901.15 € (-2.50%) | 143 | 28 | 15% | -0.048% | -0.733% | -0.831% | -23.93 € |
| ruptura_volumen_evento | 903.67 € (-2.23%) | 94 | 12 | 18% | -0.211% | -0.992% | -1.085% | -21.36 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 03:35 | macd_momentum_evento | BNB | momentum perdido | -0.06% | -0.56% | -0.13 |
| 2026-10-01 03:35 | macd_momentum_evento | WLD | momentum perdido | +0.38% | -0.12% | -0.03 |
| 2026-10-01 03:35 | macd_momentum_regimen | BNB | momentum perdido | -0.06% | -0.56% | -0.13 |
| 2026-10-01 03:35 | macd_momentum_regimen | WLD | momentum perdido | +0.38% | -0.12% | -0.03 |
| 2026-10-01 03:35 | macd_sin_salida | SKY | timeout | +0.66% | +0.15% | +0.04 |
| 2026-10-01 03:35 | macd_sin_salida | CRV | timeout | +0.67% | +0.17% | +0.04 |
| 2026-10-01 03:35 | ruptura_estricta | APT | timeout | +0.89% | +0.39% | +0.09 |
| 2026-10-01 03:35 | macd_momentum | BNB | momentum perdido | -0.06% | -0.56% | -0.12 |
| 2026-10-01 03:35 | macd_momentum | WLD | momentum perdido | +0.38% | -0.12% | -0.03 |
| 2026-10-01 03:30 | ruptura_volumen_evento | SOL | timeout | -0.12% | -0.62% | -0.14 |
| 2026-10-01 03:30 | macd_momentum_evento | ALGO | take-profit | +2.01% | +1.51% | +0.34 |
| 2026-10-01 03:30 | c_banda_atr_evento | ALGO | take-profit | +2.01% | +1.51% | +0.34 |
| 2026-10-01 03:30 | ruptura_volumen_regimen | KAS | timeout | -0.38% | -0.88% | -0.20 |
| 2026-10-01 03:30 | ruptura_volumen_regimen | BCH | timeout | -0.48% | -0.98% | -0.22 |
| 2026-10-01 03:30 | ruptura_volumen_regimen | SOL | timeout | -0.12% | -0.62% | -0.14 |

## Eventos de la última vuelta

- 2026-10-01 03:30 [macd_momentum] ENTRADA BTC @ 73722.8 (22.39 €, apertura)
- 2026-10-01 03:30 [macd_sin_salida] ENTRADA BTC @ 73722.8 (22.57 €, apertura)
- 2026-10-01 03:30 [macd_momentum_regimen] ENTRADA BTC @ 73722.8 (22.61 €, apertura)
- 2026-10-01 03:30 [macd_momentum_evento] ENTRADA BTC @ 73722.8 (22.51 €, apertura)
- 2026-10-01 03:30 [macd_momentum] ENTRADA XLM @ 0.200578 (22.39 €, apertura)
- 2026-10-01 03:30 [macd_momentum_regimen] ENTRADA XLM @ 0.200578 (22.61 €, apertura)
- 2026-10-01 03:30 [macd_momentum_evento] ENTRADA XLM @ 0.200578 (22.51 €, apertura)
- 2026-10-01 03:30 [pullback_tendencia] ENTRADA LTC @ 59.31 (22.56 €, apertura)
- 2026-10-01 03:30 [c_banda_atr_tope] ENTRADA TRX @ 0.298498 (22.94 €, apertura)
- 2026-10-01 03:30 [c_banda_atr_regimen] ENTRADA TRX @ 0.298498 (22.68 €, apertura)
- 2026-10-01 03:35 [macd_sin_salida] CIERRE CRV timeout bruto +0.67% neto +0.17%
- 2026-10-01 03:35 [macd_momentum] CIERRE WLD momentum perdido bruto +0.38% neto -0.12%
- 2026-10-01 03:35 [macd_momentum_regimen] CIERRE WLD momentum perdido bruto +0.38% neto -0.12%
- 2026-10-01 03:35 [macd_momentum_evento] CIERRE WLD momentum perdido bruto +0.38% neto -0.12%
- 2026-10-01 03:30 [macd_momentum] ENTRADA XDC @ 0.03131 (22.39 €, apertura)
- 2026-10-01 03:30 [macd_sin_salida] ENTRADA XDC @ 0.03131 (22.57 €, apertura)
- 2026-10-01 03:30 [macd_momentum_regimen] ENTRADA XDC @ 0.03131 (22.61 €, apertura)
- 2026-10-01 03:30 [macd_momentum_evento] ENTRADA XDC @ 0.03131 (22.51 €, apertura)
- 2026-10-01 03:35 [macd_momentum] CIERRE BNB momentum perdido bruto -0.06% neto -0.56%
- 2026-10-01 03:35 [macd_momentum_regimen] CIERRE BNB momentum perdido bruto -0.06% neto -0.56%
- 2026-10-01 03:35 [macd_momentum_evento] CIERRE BNB momentum perdido bruto -0.06% neto -0.56%
- 2026-10-01 03:35 [macd_sin_salida] CIERRE SKY timeout bruto +0.65% neto +0.15%
- 2026-10-01 03:30 [c_banda_atr] ENTRADA APT @ 0.6915 (22.55 €, apertura)
- 2026-10-01 03:35 [ruptura_estricta] CIERRE APT timeout bruto +0.89% neto +0.39%
- 2026-10-01 03:30 [c_banda_atr_regimen] ENTRADA APT @ 0.6915 (22.68 €, apertura)
- 2026-10-01 03:30 [c_banda_atr_evento] ENTRADA APT @ 0.6915 (22.70 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
