# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 19:17 UTC · vueltas 56 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.45 € (-1.71%) | 46 | 11 | 28% | -0.397% | -1.438% | -1.593% | -15.24 € |
| reversion_bb | 922.34 € (-0.21%) | 6 | 4 | 50% | +0.000% | -1.100% | -1.233% | -1.53 € |
| ruptura_volumen | 898.59 € (-2.78%) | 72 | 4 | 14% | -0.670% | -1.532% | -1.672% | -25.31 € |
| rebote_extremo | 924.03 € (-0.02%) | 2 | 1 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 906.23 € (-1.95%) | 54 | 3 | 15% | -0.455% | -1.444% | -1.585% | -17.89 € |
| macd_momentum | 909.34 € (-1.61%) | 73 | 7 | 29% | -0.010% | -0.867% | -1.006% | -14.58 € |
| estocastico_rebote | 906.52 € (-1.92%) | 88 | 31 | 40% | +0.022% | -0.775% | -0.910% | -15.74 € |
| ruptura_estricta | 899.04 € (-2.73%) | 45 | 2 | 9% | -1.346% | -2.426% | -2.575% | -25.13 € |
| macd_sin_salida | 905.65 € (-2.01%) | 64 | 10 | 33% | -0.313% | -1.221% | -1.360% | -18.01 € |
| c_banda_atr_tope | 921.80 € (-0.26%) | 11 | 5 | 45% | +0.144% | -0.956% | -1.120% | -2.43 € |
| ruptura_volumen_tope | 918.36 € (-0.64%) | 17 | 3 | 24% | -0.279% | -1.379% | -1.470% | -5.41 € |
| c_banda_atr_regimen | 908.96 € (-1.65%) | 42 | 3 | 26% | -0.472% | -1.572% | -1.727% | -15.21 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.42 € (-2.79%) | 71 | 1 | 13% | -0.726% | -1.594% | -1.734% | -25.94 € |
| c_banda_atr_evento | 918.52 € (-0.62%) | 13 | 11 | 23% | -0.677% | -1.777% | -1.919% | -5.34 € |
| macd_momentum_evento | 916.86 € (-0.80%) | 26 | 7 | 23% | -0.078% | -1.178% | -1.318% | -7.06 € |
| ruptura_volumen_evento | 914.40 € (-1.06%) | 22 | 4 | 9% | -0.768% | -1.868% | -1.984% | -9.49 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 19:15 | c_banda_atr_evento | WLFI | stop-loss | -1.61% | -2.71% | -0.63 |
| 2026-09-30 19:15 | c_banda_atr_regimen | WLFI | stop-loss | -1.61% | -2.71% | -0.62 |
| 2026-09-30 19:15 | macd_sin_salida | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 19:15 | ruptura_estricta | NIGHT | stop-loss | -2.00% | -2.80% | -0.63 |
| 2026-09-30 19:15 | estocastico_rebote | QNT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 19:15 | pullback_tendencia | NEAR | rotura de tendencia | -0.50% | -1.30% | -0.30 |
| 2026-09-30 19:15 | c_banda_atr | WLFI | stop-loss | -1.61% | -2.41% | -0.55 |
| 2026-09-30 19:10 | pullback_tendencia | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 18:55 | macd_momentum_evento | NEAR | momentum perdido | -0.77% | -1.87% | -0.43 |
| 2026-09-30 18:55 | macd_momentum | NEAR | momentum perdido | -0.77% | -1.27% | -0.29 |
| 2026-09-30 18:50 | macd_momentum_evento | ALGO | momentum perdido | -1.14% | -2.24% | -0.52 |
| 2026-09-30 18:50 | c_banda_atr_evento | VVV | timeout | -0.93% | -2.02% | -0.47 |
| 2026-09-30 18:50 | c_banda_atr_tope | VVV | timeout | -0.93% | -2.02% | -0.47 |
| 2026-09-30 18:50 | estocastico_rebote | RENDER | stop-loss | -1.58% | -2.08% | -0.48 |
| 2026-09-30 18:50 | estocastico_rebote | DOT | stop-loss | -1.72% | -2.22% | -0.51 |

## Eventos de la última vuelta

- 2026-09-30 19:15 [estocastico_rebote] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 19:15 [pullback_tendencia] CIERRE NEAR rotura de tendencia bruto -0.50% neto -1.30%
- 2026-09-30 19:15 [macd_sin_salida] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 19:10 [c_banda_atr] ENTRADA FET @ 0.1981 (22.74 €, apertura)
- 2026-09-30 19:10 [macd_momentum] ENTRADA FET @ 0.1981 (22.74 €, apertura)
- 2026-09-30 19:10 [macd_sin_salida] ENTRADA FET @ 0.1981 (22.66 €, apertura)
- 2026-09-30 19:10 [c_banda_atr_evento] ENTRADA FET @ 0.1981 (22.99 €, apertura)
- 2026-09-30 19:10 [macd_momentum_evento] ENTRADA FET @ 0.1981 (22.93 €, apertura)
- 2026-09-30 19:15 [ruptura_estricta] CIERRE NIGHT stop-loss bruto -2.00% neto -2.80%
- 2026-09-30 19:15 [c_banda_atr] CIERRE WLFI stop-loss bruto -1.61% neto -2.41%
- 2026-09-30 19:15 [c_banda_atr_regimen] CIERRE WLFI stop-loss bruto -1.61% neto -2.71%
- 2026-09-30 19:15 [c_banda_atr_evento] CIERRE WLFI stop-loss bruto -1.61% neto -2.71%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
