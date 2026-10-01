# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 08:36 UTC · vueltas 173 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.46 € (-2.79%) | 165 | 6 | 36% | -0.010% | -0.668% | -0.792% | -25.27 € |
| reversion_bb | 918.74 € (-0.60%) | 21 | 8 | 38% | +0.128% | -0.972% | -1.079% | -4.71 € |
| ruptura_volumen | 885.35 € (-4.21%) | 205 | 1 | 23% | -0.208% | -0.835% | -0.945% | -38.90 € |
| rebote_extremo | 923.31 € (-0.10%) | 4 | 4 | 50% | +0.185% | -0.915% | -1.054% | -0.84 € |
| pullback_tendencia | 897.69 € (-2.87%) | 120 | 2 | 16% | -0.249% | -0.969% | -1.075% | -26.55 € |
| macd_momentum | 884.58 € (-4.29%) | 291 | 5 | 22% | -0.005% | -0.594% | -0.703% | -39.22 € |
| estocastico_rebote | 883.97 € (-4.36%) | 214 | 37 | 33% | -0.143% | -0.765% | -0.881% | -37.29 € |
| ruptura_estricta | 891.27 € (-3.57%) | 119 | 3 | 26% | -0.468% | -1.190% | -1.316% | -32.43 € |
| macd_sin_salida | 888.50 € (-3.87%) | 213 | 8 | 37% | -0.092% | -0.715% | -0.827% | -34.78 € |
| c_banda_atr_tope | 914.92 € (-1.01%) | 36 | 4 | 28% | +0.005% | -1.095% | -1.215% | -9.08 € |
| ruptura_volumen_tope | 912.28 € (-1.29%) | 58 | 1 | 28% | +0.057% | -0.898% | -1.015% | -11.97 € |
| c_banda_atr_regimen | 902.81 € (-2.32%) | 107 | 2 | 35% | -0.113% | -0.857% | -0.999% | -21.07 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 904.44 € (-2.14%) | 132 | 6 | 37% | +0.065% | -0.635% | -0.751% | -19.28 € |
| macd_momentum_evento | 889.48 € (-3.76%) | 244 | 5 | 19% | -0.011% | -0.619% | -0.722% | -34.31 € |
| ruptura_volumen_evento | 897.94 € (-2.85%) | 155 | 1 | 24% | -0.072% | -0.743% | -0.840% | -26.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 08:35 | c_banda_atr_evento | SEI | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 08:35 | c_banda_atr_regimen | SEI | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 08:35 | macd_sin_salida | ASTER | stop-loss | -1.55% | -2.05% | -0.46 |
| 2026-10-01 08:35 | ruptura_estricta | SEI | stop-loss | -2.00% | -2.50% | -0.56 |
| 2026-10-01 08:35 | estocastico_rebote | MON | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 08:35 | estocastico_rebote | HBAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 08:35 | estocastico_rebote | ADA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 08:35 | estocastico_rebote | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 08:35 | rebote_extremo | USELESS | stop-loss | -2.00% | -3.10% | -0.72 |
| 2026-10-01 08:35 | c_banda_atr | SEI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 08:30 | c_banda_atr_evento | BCH | timeout | -0.04% | -0.54% | -0.12 |
| 2026-10-01 08:30 | pullback_tendencia | NIGHT | rotura de tendencia | -0.93% | -1.43% | -0.32 |
| 2026-10-01 08:30 | c_banda_atr | BCH | timeout | -0.04% | -0.54% | -0.12 |
| 2026-10-01 08:25 | estocastico_rebote | USELESS | stop-loss | -1.54% | -2.04% | -0.46 |
| 2026-10-01 08:25 | reversion_bb | BNB | timeout | +0.02% | -1.08% | -0.25 |

## Eventos de la última vuelta

- 2026-10-01 08:35 [estocastico_rebote] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 08:35 [estocastico_rebote] CIERRE ADA stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 08:35 [estocastico_rebote] CIERRE HBAR stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 08:35 [rebote_extremo] CIERRE USELESS stop-loss bruto -2.00% neto -3.10%
- 2026-10-01 08:30 [macd_momentum] ENTRADA BCH @ 271.56 (22.13 €, apertura)
- 2026-10-01 08:30 [macd_momentum_evento] ENTRADA BCH @ 271.56 (22.25 €, apertura)
- 2026-10-01 08:35 [estocastico_rebote] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 08:35 [macd_sin_salida] CIERRE ASTER stop-loss bruto -1.55% neto -2.05%
- 2026-10-01 08:30 [pullback_tendencia] ENTRADA WLFI @ 0.049 (22.44 €, apertura)
- 2026-10-01 08:30 [estocastico_rebote] ENTRADA SHIB @ 5.076e-06 (22.17 €, apertura)
- 2026-10-01 08:35 [c_banda_atr] CIERRE SEI stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 08:35 [ruptura_estricta] CIERRE SEI stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 08:35 [c_banda_atr_regimen] CIERRE SEI stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 08:35 [c_banda_atr_evento] CIERRE SEI stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 08:30 [c_banda_atr] ENTRADA APT @ 0.6864 (22.47 €, apertura)
- 2026-10-01 08:30 [c_banda_atr_tope] ENTRADA APT @ 0.6864 (22.88 €, apertura)
- 2026-10-01 08:30 [c_banda_atr_evento] ENTRADA APT @ 0.6864 (22.62 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
