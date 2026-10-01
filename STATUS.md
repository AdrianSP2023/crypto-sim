# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 10:51 UTC · vueltas 200 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.04 € (-2.94%) | 174 | 15 | 34% | -0.052% | -0.702% | -0.824% | -27.96 € |
| reversion_bb | 919.52 € (-0.51%) | 24 | 9 | 38% | +0.050% | -1.050% | -1.157% | -5.81 € |
| ruptura_volumen | 884.93 € (-4.25%) | 211 | 6 | 23% | -0.201% | -0.825% | -0.935% | -39.54 € |
| rebote_extremo | 922.08 € (-0.23%) | 9 | 0 | 44% | +0.060% | -1.040% | -1.178% | -2.16 € |
| pullback_tendencia | 896.97 € (-2.95%) | 124 | 2 | 15% | -0.255% | -0.968% | -1.073% | -27.39 € |
| macd_momentum | 884.62 € (-4.29%) | 300 | 8 | 22% | -0.000% | -0.587% | -0.696% | -39.94 € |
| estocastico_rebote | 880.59 € (-4.72%) | 253 | 13 | 30% | -0.177% | -0.780% | -0.891% | -44.73 € |
| ruptura_estricta | 890.68 € (-3.63%) | 122 | 5 | 25% | -0.486% | -1.202% | -1.328% | -33.55 € |
| macd_sin_salida | 888.73 € (-3.84%) | 221 | 10 | 36% | -0.096% | -0.714% | -0.829% | -36.03 € |
| c_banda_atr_tope | 913.77 € (-1.13%) | 41 | 5 | 27% | -0.052% | -1.152% | -1.266% | -10.86 € |
| ruptura_volumen_tope | 912.17 € (-1.31%) | 63 | 5 | 29% | +0.074% | -0.845% | -0.961% | -12.23 € |
| c_banda_atr_regimen | 902.48 € (-2.35%) | 109 | 0 | 34% | -0.130% | -0.870% | -1.010% | -21.77 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 903.01 € (-2.30%) | 141 | 15 | 35% | +0.008% | -0.679% | -0.792% | -21.99 € |
| macd_momentum_evento | 889.52 € (-3.76%) | 253 | 8 | 19% | -0.006% | -0.610% | -0.713% | -35.04 € |
| ruptura_volumen_evento | 897.52 € (-2.89%) | 161 | 6 | 24% | -0.069% | -0.733% | -0.831% | -26.94 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 10:50 | ruptura_volumen_evento | UNI | timeout | +0.56% | +0.06% | +0.01 |
| 2026-10-01 10:50 | ruptura_volumen_tope | UNI | timeout | +0.56% | +0.06% | +0.01 |
| 2026-10-01 10:50 | ruptura_volumen | UNI | timeout | +0.56% | +0.06% | +0.01 |
| 2026-10-01 10:45 | estocastico_rebote | XDC | timeout | -0.86% | -1.36% | -0.30 |
| 2026-10-01 10:45 | rebote_extremo | TRUMP | timeout | +1.11% | +0.01% | +0.00 |
| 2026-10-01 10:40 | estocastico_rebote | APT | timeout | -0.89% | -1.39% | -0.31 |
| 2026-10-01 10:40 | estocastico_rebote | RENDER | timeout | +0.77% | +0.27% | +0.06 |
| 2026-10-01 10:40 | estocastico_rebote | PEPE | timeout | +0.10% | -0.40% | -0.09 |
| 2026-10-01 10:40 | estocastico_rebote | ARB | timeout | -0.11% | -0.61% | -0.14 |
| 2026-10-01 10:40 | estocastico_rebote | TAO | timeout | -0.49% | -0.99% | -0.22 |
| 2026-10-01 10:35 | estocastico_rebote | TON | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 10:35 | estocastico_rebote | PENGU | timeout | -0.58% | -1.08% | -0.24 |
| 2026-10-01 10:35 | estocastico_rebote | OP | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-01 10:35 | estocastico_rebote | BCH | timeout | +0.09% | -0.41% | -0.09 |
| 2026-10-01 10:35 | estocastico_rebote | DOGE | timeout | -0.31% | -0.81% | -0.18 |

## Eventos de la última vuelta

- 2026-10-01 10:45 [macd_momentum] ENTRADA XRP @ 1.31878 (22.11 €, apertura)
- 2026-10-01 10:45 [macd_sin_salida] ENTRADA XRP @ 1.31878 (22.21 €, apertura)
- 2026-10-01 10:45 [macd_momentum_evento] ENTRADA XRP @ 1.31878 (22.23 €, apertura)
- 2026-10-01 10:45 [macd_momentum] ENTRADA ETH @ 2385.54 (22.11 €, apertura)
- 2026-10-01 10:45 [macd_sin_salida] ENTRADA ETH @ 2385.54 (22.21 €, apertura)
- 2026-10-01 10:45 [macd_momentum_evento] ENTRADA ETH @ 2385.54 (22.23 €, apertura)
- 2026-10-01 10:45 [macd_momentum] ENTRADA LINK @ 12.6467 (22.11 €, apertura)
- 2026-10-01 10:45 [macd_sin_salida] ENTRADA LINK @ 12.6467 (22.21 €, apertura)
- 2026-10-01 10:45 [macd_momentum_evento] ENTRADA LINK @ 12.6467 (22.23 €, apertura)
- 2026-10-01 10:45 [ruptura_volumen] ENTRADA HYPE @ 79.52 (22.12 €, apertura)
- 2026-10-01 10:45 [ruptura_estricta] ENTRADA HYPE @ 79.52 (22.27 €, apertura)
- 2026-10-01 10:45 [ruptura_volumen_tope] ENTRADA HYPE @ 79.52 (22.80 €, apertura)
- 2026-10-01 10:45 [ruptura_volumen_evento] ENTRADA HYPE @ 79.52 (22.43 €, apertura)
- 2026-10-01 10:50 [ruptura_volumen] CIERRE UNI timeout bruto +0.56% neto +0.06%
- 2026-10-01 10:50 [ruptura_volumen_tope] CIERRE UNI timeout bruto +0.56% neto +0.06%
- 2026-10-01 10:50 [ruptura_volumen_evento] CIERRE UNI timeout bruto +0.56% neto +0.06%
- 2026-10-01 10:45 [c_banda_atr] ENTRADA ONDO @ 0.44385 (22.41 €, apertura)
- 2026-10-01 10:45 [c_banda_atr_evento] ENTRADA ONDO @ 0.44385 (22.56 €, apertura)
- 2026-10-01 10:45 [macd_momentum] ENTRADA BCH @ 272.65 (22.11 €, apertura)
- 2026-10-01 10:45 [macd_sin_salida] ENTRADA BCH @ 272.65 (22.21 €, apertura)
- 2026-10-01 10:45 [macd_momentum_evento] ENTRADA BCH @ 272.65 (22.23 €, apertura)
- 2026-10-01 10:45 [c_banda_atr] ENTRADA PEPE @ 3.829e-06 (22.41 €, apertura)
- 2026-10-01 10:45 [c_banda_atr_evento] ENTRADA PEPE @ 3.829e-06 (22.56 €, apertura)
- 2026-10-01 10:45 [c_banda_atr] ENTRADA MON @ 0.02859 (22.41 €, apertura)
- 2026-10-01 10:45 [c_banda_atr_evento] ENTRADA MON @ 0.02859 (22.56 €, apertura)
- 2026-10-01 10:45 [c_banda_atr] ENTRADA VVV @ 24.585 (22.41 €, apertura)
- 2026-10-01 10:45 [c_banda_atr_evento] ENTRADA VVV @ 24.585 (22.56 €, apertura)
- 2026-10-01 10:45 [c_banda_atr] ENTRADA PENGU @ 0.008594 (22.41 €, apertura)
- 2026-10-01 10:45 [c_banda_atr_evento] ENTRADA PENGU @ 0.008594 (22.56 €, apertura)
- 2026-10-01 10:45 [ruptura_estricta] ENTRADA BNB @ 682.79 (22.27 €, apertura)
- 2026-10-01 10:45 [ruptura_volumen_tope] ENTRADA BNB @ 682.79 (22.80 €, apertura)
- 2026-10-01 10:45 [c_banda_atr] ENTRADA KAS @ 0.03797 (22.41 €, apertura)
- 2026-10-01 10:45 [c_banda_atr_evento] ENTRADA KAS @ 0.03797 (22.56 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
