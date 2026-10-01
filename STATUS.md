# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 08:41 UTC · vueltas 174 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.97 € (-2.73%) | 165 | 6 | 36% | -0.010% | -0.668% | -0.792% | -25.27 € |
| reversion_bb | 919.30 € (-0.53%) | 21 | 8 | 38% | +0.128% | -0.972% | -1.079% | -4.71 € |
| ruptura_volumen | 885.34 € (-4.21%) | 205 | 1 | 23% | -0.208% | -0.835% | -0.945% | -38.90 € |
| rebote_extremo | 923.48 € (-0.08%) | 4 | 4 | 50% | +0.185% | -0.915% | -1.054% | -0.84 € |
| pullback_tendencia | 897.68 € (-2.87%) | 120 | 2 | 16% | -0.249% | -0.969% | -1.075% | -26.55 € |
| macd_momentum | 884.82 € (-4.26%) | 292 | 4 | 22% | -0.008% | -0.597% | -0.706% | -39.55 € |
| estocastico_rebote | 885.85 € (-4.15%) | 214 | 37 | 33% | -0.143% | -0.765% | -0.881% | -37.29 € |
| ruptura_estricta | 891.21 € (-3.57%) | 119 | 3 | 26% | -0.468% | -1.190% | -1.316% | -32.43 € |
| macd_sin_salida | 888.63 € (-3.85%) | 215 | 6 | 36% | -0.099% | -0.720% | -0.833% | -35.36 € |
| c_banda_atr_tope | 915.40 € (-0.96%) | 36 | 4 | 28% | +0.005% | -1.095% | -1.215% | -9.08 € |
| ruptura_volumen_tope | 912.27 € (-1.29%) | 58 | 1 | 28% | +0.057% | -0.898% | -1.015% | -11.97 € |
| c_banda_atr_regimen | 902.84 € (-2.32%) | 107 | 2 | 35% | -0.113% | -0.857% | -0.999% | -21.07 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 904.95 € (-2.09%) | 132 | 6 | 37% | +0.065% | -0.635% | -0.751% | -19.28 € |
| macd_momentum_evento | 889.72 € (-3.73%) | 245 | 4 | 19% | -0.015% | -0.623% | -0.725% | -34.64 € |
| ruptura_volumen_evento | 897.94 € (-2.85%) | 155 | 1 | 24% | -0.072% | -0.743% | -0.840% | -26.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 08:40 | macd_momentum_evento | HBAR | momentum perdido | -0.99% | -1.49% | -0.33 |
| 2026-10-01 08:40 | macd_sin_salida | MINA | timeout | -1.00% | -1.50% | -0.34 |
| 2026-10-01 08:40 | macd_sin_salida | BCH | timeout | -0.57% | -1.07% | -0.24 |
| 2026-10-01 08:40 | macd_momentum | HBAR | momentum perdido | -0.99% | -1.49% | -0.33 |
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

## Eventos de la última vuelta

- 2026-10-01 08:40 [macd_momentum] CIERRE HBAR momentum perdido bruto -0.99% neto -1.49%
- 2026-10-01 08:40 [macd_momentum_evento] CIERRE HBAR momentum perdido bruto -0.99% neto -1.49%
- 2026-10-01 08:40 [macd_sin_salida] CIERRE BCH timeout bruto -0.57% neto -1.07%
- 2026-10-01 08:40 [macd_sin_salida] CIERRE MINA timeout bruto -1.00% neto -1.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
