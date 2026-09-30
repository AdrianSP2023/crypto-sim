# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 19:22 UTC · vueltas 57 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.92 € (-1.77%) | 46 | 11 | 28% | -0.397% | -1.438% | -1.593% | -15.24 € |
| reversion_bb | 922.06 € (-0.24%) | 6 | 4 | 50% | +0.000% | -1.100% | -1.233% | -1.53 € |
| ruptura_volumen | 898.17 € (-2.82%) | 74 | 2 | 14% | -0.665% | -1.518% | -1.656% | -25.76 € |
| rebote_extremo | 924.04 € (-0.02%) | 2 | 1 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 906.06 € (-1.97%) | 55 | 2 | 15% | -0.474% | -1.454% | -1.595% | -18.35 € |
| macd_momentum | 909.04 € (-1.64%) | 75 | 5 | 28% | -0.013% | -0.861% | -0.998% | -14.86 € |
| estocastico_rebote | 904.89 € (-2.09%) | 90 | 29 | 39% | -0.012% | -0.802% | -0.935% | -16.65 € |
| ruptura_estricta | 899.00 € (-2.73%) | 45 | 2 | 9% | -1.346% | -2.426% | -2.575% | -25.13 € |
| macd_sin_salida | 905.25 € (-2.05%) | 64 | 10 | 33% | -0.313% | -1.221% | -1.360% | -18.01 € |
| c_banda_atr_tope | 921.57 € (-0.29%) | 11 | 5 | 45% | +0.144% | -0.956% | -1.120% | -2.43 € |
| ruptura_volumen_tope | 917.98 € (-0.68%) | 18 | 2 | 22% | -0.331% | -1.431% | -1.522% | -5.94 € |
| c_banda_atr_regimen | 908.90 € (-1.66%) | 42 | 3 | 26% | -0.472% | -1.572% | -1.727% | -15.21 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 917.98 € (-0.68%) | 13 | 11 | 23% | -0.677% | -1.777% | -1.919% | -5.34 € |
| macd_momentum_evento | 916.28 € (-0.86%) | 28 | 5 | 21% | -0.082% | -1.182% | -1.319% | -7.62 € |
| ruptura_volumen_evento | 913.69 € (-1.14%) | 24 | 2 | 8% | -0.746% | -1.846% | -1.960% | -10.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 19:20 | ruptura_volumen_evento | MON | timeout | +0.20% | -0.90% | -0.21 |
| 2026-09-30 19:20 | ruptura_volumen_evento | ALGO | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 19:20 | macd_momentum_evento | XMR | momentum perdido | +0.00% | -1.10% | -0.25 |
| 2026-09-30 19:20 | macd_momentum_evento | BNB | momentum perdido | -0.26% | -1.36% | -0.31 |
| 2026-09-30 19:20 | ruptura_volumen_regimen | MON | timeout | +0.20% | -0.30% | -0.07 |
| 2026-09-30 19:20 | ruptura_volumen_tope | ALGO | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 19:20 | estocastico_rebote | TAO | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 19:20 | estocastico_rebote | SOL | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 19:20 | macd_momentum | XMR | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-09-30 19:20 | macd_momentum | BNB | momentum perdido | -0.26% | -0.76% | -0.17 |
| 2026-09-30 19:20 | pullback_tendencia | MON | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 19:20 | ruptura_volumen | MON | timeout | +0.20% | -0.30% | -0.07 |
| 2026-09-30 19:20 | ruptura_volumen | ALGO | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 19:15 | c_banda_atr_evento | WLFI | stop-loss | -1.61% | -2.71% | -0.63 |
| 2026-09-30 19:15 | c_banda_atr_regimen | WLFI | stop-loss | -1.61% | -2.71% | -0.62 |

## Eventos de la última vuelta

- 2026-09-30 19:20 [estocastico_rebote] CIERRE SOL stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 19:20 [estocastico_rebote] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 19:20 [ruptura_volumen] CIERRE ALGO stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 19:20 [ruptura_volumen_tope] CIERRE ALGO stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 19:20 [ruptura_volumen_evento] CIERRE ALGO stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 19:20 [ruptura_volumen] CIERRE MON timeout bruto +0.20% neto -0.30%
- 2026-09-30 19:20 [pullback_tendencia] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 19:20 [ruptura_volumen_regimen] CIERRE MON timeout bruto +0.20% neto -0.30%
- 2026-09-30 19:20 [ruptura_volumen_evento] CIERRE MON timeout bruto +0.20% neto -0.90%
- 2026-09-30 19:20 [macd_momentum] CIERRE BNB momentum perdido bruto -0.26% neto -0.76%
- 2026-09-30 19:20 [macd_momentum_evento] CIERRE BNB momentum perdido bruto -0.26% neto -1.36%
- 2026-09-30 19:20 [macd_momentum] CIERRE XMR momentum perdido bruto +0.00% neto -0.50%
- 2026-09-30 19:20 [macd_momentum_evento] CIERRE XMR momentum perdido bruto +0.00% neto -1.10%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
