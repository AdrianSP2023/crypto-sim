# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 21:56 UTC · vueltas 88 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.84 € (-2.21%) | 57 | 25 | 23% | -0.492% | -1.450% | -1.602% | -18.99 € |
| reversion_bb | 921.64 € (-0.28%) | 9 | 3 | 44% | -0.167% | -1.267% | -1.401% | -2.64 € |
| ruptura_volumen | 897.54 € (-2.89%) | 80 | 13 | 15% | -0.599% | -1.425% | -1.562% | -26.13 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.97 € (-2.08%) | 64 | 1 | 16% | -0.405% | -1.317% | -1.455% | -19.33 € |
| macd_momentum | 905.78 € (-2.00%) | 93 | 10 | 25% | -0.068% | -0.849% | -0.979% | -18.13 € |
| estocastico_rebote | 903.22 € (-2.27%) | 119 | 10 | 34% | -0.030% | -0.750% | -0.880% | -20.54 € |
| ruptura_estricta | 898.51 € (-2.78%) | 47 | 6 | 11% | -1.267% | -2.328% | -2.477% | -25.19 € |
| macd_sin_salida | 903.99 € (-2.19%) | 75 | 16 | 33% | -0.265% | -1.113% | -1.246% | -19.21 € |
| c_banda_atr_tope | 920.19 € (-0.44%) | 16 | 4 | 31% | +0.009% | -1.091% | -1.253% | -4.03 € |
| ruptura_volumen_tope | 916.93 € (-0.79%) | 22 | 5 | 18% | -0.264% | -1.364% | -1.458% | -6.92 € |
| c_banda_atr_regimen | 908.47 € (-1.71%) | 45 | 0 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 912.36 € (-1.29%) | 25 | 24 | 12% | -0.736% | -1.836% | -1.980% | -10.58 € |
| macd_momentum_evento | 911.07 € (-1.42%) | 46 | 10 | 17% | -0.167% | -1.214% | -1.337% | -12.83 € |
| ruptura_volumen_evento | 912.23 € (-1.30%) | 30 | 13 | 10% | -0.552% | -1.652% | -1.769% | -11.43 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 21:55 | c_banda_atr_evento | MINA | stop-loss | -1.65% | -2.75% | -0.63 |
| 2026-09-30 21:55 | c_banda_atr_tope | MINA | stop-loss | -1.65% | -2.75% | -0.63 |
| 2026-09-30 21:55 | macd_sin_salida | TON | timeout | -0.81% | -1.31% | -0.30 |
| 2026-09-30 21:55 | ruptura_estricta | TON | timeout | -0.81% | -1.31% | -0.30 |
| 2026-09-30 21:55 | estocastico_rebote | DOT | timeout | -0.58% | -1.08% | -0.25 |
| 2026-09-30 21:55 | estocastico_rebote | ZEC | timeout | +0.22% | -0.28% | -0.06 |
| 2026-09-30 21:55 | pullback_tendencia | KSM | rotura de tendencia | -0.88% | -1.38% | -0.31 |
| 2026-09-30 21:55 | c_banda_atr | MINA | stop-loss | -1.65% | -2.15% | -0.49 |
| 2026-09-30 21:50 | ruptura_volumen_evento | TRX | timeout | -0.07% | -1.17% | -0.27 |
| 2026-09-30 21:50 | macd_momentum_evento | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 21:50 | ruptura_volumen_tope | TRX | timeout | -0.07% | -1.17% | -0.27 |
| 2026-09-30 21:50 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 21:50 | macd_momentum | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 21:50 | ruptura_volumen | TRX | timeout | -0.07% | -0.57% | -0.13 |
| 2026-09-30 21:50 | reversion_bb | WLFI | stop-loss | -1.50% | -2.60% | -0.60 |

## Eventos de la última vuelta

- 2026-09-30 21:55 [estocastico_rebote] CIERRE ZEC timeout bruto +0.22% neto -0.28%
- 2026-09-30 21:55 [estocastico_rebote] CIERRE DOT timeout bruto -0.58% neto -1.08%
- 2026-09-30 21:50 [macd_momentum] ENTRADA JUP @ 0.28819 (22.65 €, apertura)
- 2026-09-30 21:50 [macd_sin_salida] ENTRADA JUP @ 0.28819 (22.63 €, apertura)
- 2026-09-30 21:50 [macd_momentum_evento] ENTRADA JUP @ 0.28819 (22.79 €, apertura)
- 2026-09-30 21:50 [ruptura_volumen] ENTRADA MON @ 0.0264 (22.45 €, apertura)
- 2026-09-30 21:50 [ruptura_volumen_evento] ENTRADA MON @ 0.0264 (22.82 €, apertura)
- 2026-09-30 21:55 [c_banda_atr] CIERRE MINA stop-loss bruto -1.65% neto -2.15%
- 2026-09-30 21:55 [c_banda_atr_tope] CIERRE MINA stop-loss bruto -1.65% neto -2.75%
- 2026-09-30 21:55 [c_banda_atr_evento] CIERRE MINA stop-loss bruto -1.65% neto -2.75%
- 2026-09-30 21:55 [pullback_tendencia] CIERRE KSM rotura de tendencia bruto -0.88% neto -1.38%
- 2026-09-30 21:50 [ruptura_estricta] ENTRADA KSM @ 4.56 (22.48 €, apertura)
- 2026-09-30 21:55 [ruptura_estricta] CIERRE TON timeout bruto -0.81% neto -1.31%
- 2026-09-30 21:55 [macd_sin_salida] CIERRE TON timeout bruto -0.81% neto -1.31%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
