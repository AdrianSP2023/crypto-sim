# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 22:01 UTC · vueltas 89 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.70 € (-2.22%) | 57 | 25 | 23% | -0.492% | -1.450% | -1.602% | -18.99 € |
| reversion_bb | 921.66 € (-0.28%) | 9 | 4 | 44% | -0.167% | -1.267% | -1.401% | -2.64 € |
| ruptura_volumen | 897.52 € (-2.89%) | 81 | 12 | 15% | -0.599% | -1.421% | -1.564% | -26.38 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.97 € (-2.08%) | 64 | 1 | 16% | -0.405% | -1.317% | -1.455% | -19.33 € |
| macd_momentum | 905.47 € (-2.03%) | 96 | 7 | 24% | -0.091% | -0.862% | -0.996% | -19.00 € |
| estocastico_rebote | 903.28 € (-2.27%) | 119 | 10 | 34% | -0.030% | -0.750% | -0.880% | -20.54 € |
| ruptura_estricta | 898.55 € (-2.78%) | 47 | 6 | 11% | -1.267% | -2.328% | -2.477% | -25.19 € |
| macd_sin_salida | 904.04 € (-2.19%) | 75 | 16 | 33% | -0.265% | -1.113% | -1.246% | -19.21 € |
| c_banda_atr_tope | 920.19 € (-0.44%) | 16 | 4 | 31% | +0.009% | -1.091% | -1.253% | -4.03 € |
| ruptura_volumen_tope | 916.75 € (-0.81%) | 23 | 4 | 17% | -0.279% | -1.379% | -1.494% | -7.31 € |
| c_banda_atr_regimen | 908.47 € (-1.71%) | 45 | 0 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 912.22 € (-1.30%) | 25 | 24 | 12% | -0.736% | -1.836% | -1.980% | -10.58 € |
| macd_momentum_evento | 910.76 € (-1.46%) | 49 | 7 | 16% | -0.205% | -1.219% | -1.349% | -13.71 € |
| ruptura_volumen_evento | 912.07 € (-1.32%) | 31 | 12 | 10% | -0.553% | -1.653% | -1.785% | -11.82 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 22:00 | ruptura_volumen_evento | KAS | timeout | -0.60% | -1.70% | -0.39 |
| 2026-09-30 22:00 | macd_momentum_evento | TRUMP | momentum perdido | -0.55% | -1.05% | -0.24 |
| 2026-09-30 22:00 | macd_momentum_evento | KSM | momentum perdido | -1.09% | -1.59% | -0.36 |
| 2026-09-30 22:00 | macd_momentum_evento | ONDO | momentum perdido | -0.71% | -1.22% | -0.28 |
| 2026-09-30 22:00 | ruptura_volumen_tope | KAS | timeout | -0.60% | -1.70% | -0.39 |
| 2026-09-30 22:00 | macd_momentum | TRUMP | momentum perdido | -0.55% | -1.05% | -0.24 |
| 2026-09-30 22:00 | macd_momentum | KSM | momentum perdido | -1.09% | -1.59% | -0.36 |
| 2026-09-30 22:00 | macd_momentum | ONDO | momentum perdido | -0.71% | -1.22% | -0.28 |
| 2026-09-30 22:00 | ruptura_volumen | KAS | timeout | -0.60% | -1.10% | -0.25 |
| 2026-09-30 21:55 | c_banda_atr_evento | MINA | stop-loss | -1.65% | -2.75% | -0.63 |
| 2026-09-30 21:55 | c_banda_atr_tope | MINA | stop-loss | -1.65% | -2.75% | -0.63 |
| 2026-09-30 21:55 | macd_sin_salida | TON | timeout | -0.81% | -1.31% | -0.30 |
| 2026-09-30 21:55 | ruptura_estricta | TON | timeout | -0.81% | -1.31% | -0.30 |
| 2026-09-30 21:55 | estocastico_rebote | DOT | timeout | -0.58% | -1.08% | -0.25 |
| 2026-09-30 21:55 | estocastico_rebote | ZEC | timeout | +0.22% | -0.28% | -0.06 |

## Eventos de la última vuelta

- 2026-09-30 22:00 [macd_momentum] CIERRE ONDO momentum perdido bruto -0.72% neto -1.22%
- 2026-09-30 22:00 [macd_momentum_evento] CIERRE ONDO momentum perdido bruto -0.72% neto -1.22%
- 2026-09-30 21:55 [reversion_bb] ENTRADA BCH @ 269.05 (23.04 €, apertura)
- 2026-09-30 22:00 [macd_momentum] CIERRE KSM momentum perdido bruto -1.09% neto -1.59%
- 2026-09-30 22:00 [macd_momentum_evento] CIERRE KSM momentum perdido bruto -1.09% neto -1.59%
- 2026-09-30 22:00 [macd_momentum] CIERRE TRUMP momentum perdido bruto -0.55% neto -1.05%
- 2026-09-30 22:00 [macd_momentum_evento] CIERRE TRUMP momentum perdido bruto -0.55% neto -1.05%
- 2026-09-30 22:00 [ruptura_volumen] CIERRE KAS timeout bruto -0.60% neto -1.10%
- 2026-09-30 22:00 [ruptura_volumen_tope] CIERRE KAS timeout bruto -0.60% neto -1.70%
- 2026-09-30 22:00 [ruptura_volumen_evento] CIERRE KAS timeout bruto -0.60% neto -1.70%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
