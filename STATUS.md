# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 21:41 UTC · vueltas 85 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 904.50 € (-2.14%) | 56 | 26 | 23% | -0.471% | -1.437% | -1.587% | -18.50 € |
| reversion_bb | 922.08 € (-0.23%) | 8 | 4 | 50% | +0.000% | -1.100% | -1.225% | -2.04 € |
| ruptura_volumen | 897.77 € (-2.86%) | 78 | 14 | 15% | -0.612% | -1.447% | -1.586% | -25.87 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 905.31 € (-2.05%) | 63 | 2 | 16% | -0.397% | -1.316% | -1.453% | -19.02 € |
| macd_momentum | 906.40 € (-1.93%) | 91 | 6 | 24% | -0.089% | -0.876% | -1.008% | -18.31 € |
| estocastico_rebote | 903.99 € (-2.19%) | 116 | 11 | 35% | -0.029% | -0.754% | -0.887% | -20.15 € |
| ruptura_estricta | 898.83 € (-2.75%) | 46 | 5 | 11% | -1.277% | -2.350% | -2.498% | -24.89 € |
| macd_sin_salida | 904.68 € (-2.12%) | 72 | 14 | 32% | -0.320% | -1.182% | -1.317% | -19.59 € |
| c_banda_atr_tope | 920.61 € (-0.39%) | 15 | 5 | 33% | +0.120% | -0.980% | -1.135% | -3.39 € |
| ruptura_volumen_tope | 917.60 € (-0.72%) | 20 | 5 | 20% | -0.282% | -1.382% | -1.478% | -6.38 € |
| c_banda_atr_regimen | 908.47 € (-1.71%) | 45 | 0 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 913.17 € (-1.20%) | 24 | 25 | 12% | -0.698% | -1.798% | -1.936% | -9.95 € |
| macd_momentum_evento | 911.77 € (-1.35%) | 44 | 6 | 16% | -0.215% | -1.281% | -1.406% | -12.95 € |
| ruptura_volumen_evento | 912.74 € (-1.24%) | 28 | 14 | 11% | -0.585% | -1.685% | -1.805% | -10.89 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 21:40 | ruptura_volumen_evento | NIGHT | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 21:40 | macd_sin_salida | XMR | timeout | -0.81% | -1.31% | -0.30 |
| 2026-09-30 21:40 | estocastico_rebote | MINA | timeout | -0.79% | -1.29% | -0.29 |
| 2026-09-30 21:40 | ruptura_volumen | NIGHT | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 21:35 | macd_momentum_evento | ARB | momentum perdido | -1.10% | -1.90% | -0.44 |
| 2026-09-30 21:35 | c_banda_atr_evento | PENGU | stop-loss | -1.59% | -2.69% | -0.62 |
| 2026-09-30 21:35 | macd_momentum | ARB | momentum perdido | -1.10% | -1.60% | -0.36 |
| 2026-09-30 21:35 | c_banda_atr | PENGU | stop-loss | -1.59% | -2.09% | -0.47 |
| 2026-09-30 21:30 | c_banda_atr_evento | XDC | timeout | +0.40% | -0.70% | -0.16 |
| 2026-09-30 21:30 | c_banda_atr_regimen | XDC | timeout | +0.40% | -0.40% | -0.09 |
| 2026-09-30 21:30 | c_banda_atr_tope | XDC | timeout | +0.40% | -0.70% | -0.16 |
| 2026-09-30 21:30 | c_banda_atr | XDC | timeout | +0.40% | -0.10% | -0.02 |
| 2026-09-30 21:25 | macd_momentum_evento | NEAR | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 21:25 | c_banda_atr_evento | NEAR | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-30 21:25 | macd_sin_salida | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-30 21:35 [estocastico_rebote] ENTRADA FET @ 0.2001 (22.61 €, apertura)
- 2026-09-30 21:35 [c_banda_atr_tope] ENTRADA FET @ 0.2001 (23.02 €, apertura)
- 2026-09-30 21:40 [ruptura_volumen] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%
- 2026-09-30 21:40 [ruptura_volumen_evento] CIERRE NIGHT take-profit bruto +2.50% neto +1.40%
- 2026-09-30 21:40 [estocastico_rebote] CIERRE MINA timeout bruto -0.79% neto -1.29%
- 2026-09-30 21:40 [macd_sin_salida] CIERRE XMR timeout bruto -0.81% neto -1.31%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
