# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 21:31 UTC · vueltas 83 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 904.22 € (-2.17%) | 55 | 27 | 24% | -0.451% | -1.425% | -1.577% | -18.02 € |
| reversion_bb | 922.16 € (-0.23%) | 8 | 4 | 50% | +0.000% | -1.100% | -1.225% | -2.04 € |
| ruptura_volumen | 897.23 € (-2.92%) | 77 | 14 | 14% | -0.652% | -1.491% | -1.629% | -26.32 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.95 € (-2.09%) | 63 | 2 | 16% | -0.397% | -1.316% | -1.453% | -19.02 € |
| macd_momentum | 906.08 € (-1.96%) | 90 | 7 | 24% | -0.078% | -0.868% | -1.000% | -17.95 € |
| estocastico_rebote | 903.79 € (-2.21%) | 115 | 9 | 36% | -0.023% | -0.750% | -0.880% | -19.86 € |
| ruptura_estricta | 898.60 € (-2.77%) | 46 | 5 | 11% | -1.277% | -2.350% | -2.498% | -24.89 € |
| macd_sin_salida | 903.99 € (-2.19%) | 71 | 15 | 32% | -0.313% | -1.181% | -1.315% | -19.30 € |
| c_banda_atr_tope | 920.49 € (-0.41%) | 15 | 4 | 33% | +0.120% | -0.980% | -1.135% | -3.39 € |
| ruptura_volumen_tope | 917.67 € (-0.71%) | 20 | 5 | 20% | -0.282% | -1.382% | -1.478% | -6.38 € |
| c_banda_atr_regimen | 908.47 € (-1.71%) | 45 | 0 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 913.02 € (-1.21%) | 23 | 26 | 13% | -0.659% | -1.759% | -1.900% | -9.34 € |
| macd_momentum_evento | 911.51 € (-1.38%) | 43 | 7 | 16% | -0.195% | -1.267% | -1.392% | -12.51 € |
| ruptura_volumen_evento | 912.33 € (-1.29%) | 27 | 14 | 7% | -0.700% | -1.800% | -1.915% | -11.21 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 21:30 | c_banda_atr_evento | XDC | timeout | +0.40% | -0.70% | -0.16 |
| 2026-09-30 21:30 | c_banda_atr_regimen | XDC | timeout | +0.40% | -0.40% | -0.09 |
| 2026-09-30 21:30 | c_banda_atr_tope | XDC | timeout | +0.40% | -0.70% | -0.16 |
| 2026-09-30 21:30 | c_banda_atr | XDC | timeout | +0.40% | -0.10% | -0.02 |
| 2026-09-30 21:25 | macd_momentum_evento | NEAR | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 21:25 | c_banda_atr_evento | NEAR | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-30 21:25 | macd_sin_salida | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 21:25 | estocastico_rebote | ENA | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 21:25 | macd_momentum | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 21:25 | pullback_tendencia | MON | take-profit | +2.03% | +1.53% | +0.35 |
| 2026-09-30 21:25 | pullback_tendencia | HBAR | rotura de tendencia | -0.92% | -1.42% | -0.32 |
| 2026-09-30 21:25 | c_banda_atr | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 21:20 | ruptura_volumen_evento | FET | stop-loss | -1.29% | -2.40% | -0.55 |
| 2026-09-30 21:20 | macd_momentum_evento | WLD | momentum perdido | -0.19% | -0.99% | -0.23 |
| 2026-09-30 21:20 | macd_momentum_evento | CRV | momentum perdido | +0.90% | +0.10% | +0.02 |

## Eventos de la última vuelta

- 2026-09-30 21:30 [c_banda_atr] CIERRE XDC timeout bruto +0.40% neto -0.10%
- 2026-09-30 21:30 [c_banda_atr_tope] CIERRE XDC timeout bruto +0.40% neto -0.70%
- 2026-09-30 21:30 [c_banda_atr_regimen] CIERRE XDC timeout bruto +0.40% neto -0.40%
- 2026-09-30 21:30 [c_banda_atr_evento] CIERRE XDC timeout bruto +0.40% neto -0.70%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
