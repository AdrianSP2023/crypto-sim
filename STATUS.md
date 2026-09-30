# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 21:51 UTC · vueltas 87 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 904.94 € (-2.09%) | 56 | 26 | 23% | -0.471% | -1.437% | -1.587% | -18.50 € |
| reversion_bb | 921.64 € (-0.28%) | 9 | 3 | 44% | -0.167% | -1.267% | -1.401% | -2.64 € |
| ruptura_volumen | 898.17 € (-2.82%) | 80 | 12 | 15% | -0.599% | -1.425% | -1.562% | -26.13 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 905.38 € (-2.04%) | 63 | 2 | 16% | -0.397% | -1.316% | -1.453% | -19.02 € |
| macd_momentum | 906.45 € (-1.92%) | 93 | 9 | 25% | -0.068% | -0.849% | -0.979% | -18.13 € |
| estocastico_rebote | 903.91 € (-2.20%) | 117 | 12 | 35% | -0.028% | -0.751% | -0.882% | -20.23 € |
| ruptura_estricta | 898.86 € (-2.75%) | 46 | 6 | 11% | -1.277% | -2.350% | -2.498% | -24.89 € |
| macd_sin_salida | 904.98 € (-2.08%) | 74 | 16 | 34% | -0.257% | -1.110% | -1.242% | -18.91 € |
| c_banda_atr_tope | 920.77 € (-0.38%) | 15 | 5 | 33% | +0.120% | -0.980% | -1.135% | -3.39 € |
| ruptura_volumen_tope | 917.43 € (-0.74%) | 22 | 5 | 18% | -0.264% | -1.364% | -1.458% | -6.92 € |
| c_banda_atr_regimen | 908.47 € (-1.71%) | 45 | 0 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 913.61 € (-1.15%) | 24 | 25 | 12% | -0.698% | -1.798% | -1.936% | -9.95 € |
| macd_momentum_evento | 911.75 € (-1.35%) | 46 | 9 | 17% | -0.167% | -1.214% | -1.337% | -12.83 € |
| ruptura_volumen_evento | 912.88 € (-1.23%) | 30 | 12 | 10% | -0.552% | -1.652% | -1.769% | -11.43 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 21:50 | ruptura_volumen_evento | TRX | timeout | -0.07% | -1.17% | -0.27 |
| 2026-09-30 21:50 | macd_momentum_evento | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 21:50 | ruptura_volumen_tope | TRX | timeout | -0.07% | -1.17% | -0.27 |
| 2026-09-30 21:50 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 21:50 | macd_momentum | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 21:50 | ruptura_volumen | TRX | timeout | -0.07% | -0.57% | -0.13 |
| 2026-09-30 21:50 | reversion_bb | WLFI | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 21:45 | ruptura_volumen_evento | CRV | timeout | -0.09% | -1.19% | -0.27 |
| 2026-09-30 21:45 | macd_momentum_evento | POL | momentum perdido | -0.19% | -0.99% | -0.23 |
| 2026-09-30 21:45 | ruptura_volumen_tope | CRV | timeout | -0.09% | -1.19% | -0.27 |
| 2026-09-30 21:45 | macd_sin_salida | HYPE | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 21:45 | estocastico_rebote | SUI | timeout | +0.16% | -0.34% | -0.08 |
| 2026-09-30 21:45 | macd_momentum | POL | momentum perdido | -0.19% | -0.69% | -0.16 |
| 2026-09-30 21:45 | ruptura_volumen | CRV | timeout | -0.09% | -0.59% | -0.13 |
| 2026-09-30 21:40 | ruptura_volumen_evento | NIGHT | take-profit | +2.50% | +1.40% | +0.32 |

## Eventos de la última vuelta

- 2026-09-30 21:45 [estocastico_rebote] ENTRADA HBAR @ 0.09452 (22.60 €, apertura)
- 2026-09-30 21:45 [ruptura_estricta] ENTRADA HYPE @ 80.42 (22.48 €, apertura)
- 2026-09-30 21:50 [ruptura_volumen] CIERRE TRX timeout bruto -0.07% neto -0.57%
- 2026-09-30 21:50 [ruptura_volumen_tope] CIERRE TRX timeout bruto -0.07% neto -1.17%
- 2026-09-30 21:50 [ruptura_volumen_evento] CIERRE TRX timeout bruto -0.07% neto -1.17%
- 2026-09-30 21:45 [macd_momentum] ENTRADA WLD @ 0.4742 (22.64 €, apertura)
- 2026-09-30 21:45 [macd_momentum_evento] ENTRADA WLD @ 0.4742 (22.78 €, apertura)
- 2026-09-30 21:50 [macd_momentum] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 21:50 [macd_sin_salida] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 21:50 [macd_momentum_evento] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 21:50 [reversion_bb] CIERRE WLFI stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 21:45 [macd_momentum] ENTRADA KSM @ 4.58 (22.65 €, apertura)
- 2026-09-30 21:45 [macd_sin_salida] ENTRADA KSM @ 4.58 (22.63 €, apertura)
- 2026-09-30 21:45 [ruptura_volumen_tope] ENTRADA KSM @ 4.58 (22.93 €, apertura)
- 2026-09-30 21:45 [macd_momentum_evento] ENTRADA KSM @ 4.58 (22.79 €, apertura)
- 2026-09-30 21:45 [macd_momentum] ENTRADA TRUMP @ 1.808 (22.65 €, apertura)
- 2026-09-30 21:45 [macd_sin_salida] ENTRADA TRUMP @ 1.808 (22.63 €, apertura)
- 2026-09-30 21:45 [macd_momentum_evento] ENTRADA TRUMP @ 1.808 (22.79 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
