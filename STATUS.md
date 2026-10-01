# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 09:01 UTC · vueltas 178 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.36 € (-2.69%) | 166 | 13 | 36% | -0.014% | -0.671% | -0.794% | -25.52 € |
| reversion_bb | 920.07 € (-0.45%) | 21 | 8 | 38% | +0.128% | -0.972% | -1.079% | -4.71 € |
| ruptura_volumen | 885.36 € (-4.21%) | 205 | 2 | 23% | -0.208% | -0.835% | -0.945% | -38.90 € |
| rebote_extremo | 924.28 € (+0.00%) | 4 | 5 | 50% | +0.185% | -0.915% | -1.054% | -0.84 € |
| pullback_tendencia | 897.54 € (-2.89%) | 120 | 3 | 16% | -0.249% | -0.969% | -1.075% | -26.55 € |
| macd_momentum | 884.60 € (-4.29%) | 293 | 6 | 22% | -0.011% | -0.600% | -0.708% | -39.83 € |
| estocastico_rebote | 888.52 € (-3.86%) | 216 | 37 | 33% | -0.125% | -0.745% | -0.862% | -36.71 € |
| ruptura_estricta | 890.84 € (-3.61%) | 121 | 3 | 26% | -0.481% | -1.199% | -1.325% | -33.21 € |
| macd_sin_salida | 888.70 € (-3.85%) | 215 | 9 | 36% | -0.099% | -0.720% | -0.833% | -35.36 € |
| c_banda_atr_tope | 915.48 € (-0.95%) | 37 | 5 | 27% | +0.001% | -1.099% | -1.216% | -9.36 € |
| ruptura_volumen_tope | 912.29 € (-1.29%) | 58 | 2 | 28% | +0.057% | -0.898% | -1.015% | -11.97 € |
| c_banda_atr_regimen | 902.97 € (-2.30%) | 108 | 1 | 34% | -0.118% | -0.859% | -1.000% | -21.32 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 905.35 € (-2.04%) | 133 | 13 | 37% | +0.060% | -0.639% | -0.753% | -19.53 € |
| macd_momentum_evento | 889.50 € (-3.76%) | 246 | 6 | 19% | -0.018% | -0.625% | -0.728% | -34.92 € |
| ruptura_volumen_evento | 897.96 € (-2.84%) | 155 | 2 | 24% | -0.072% | -0.743% | -0.840% | -26.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 09:00 | estocastico_rebote | VVV | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 08:55 | macd_momentum_evento | XDC | momentum perdido | -0.76% | -1.26% | -0.28 |
| 2026-10-01 08:55 | macd_momentum | XDC | momentum perdido | -0.76% | -1.26% | -0.28 |
| 2026-10-01 08:50 | c_banda_atr_evento | LTC | timeout | -0.60% | -1.10% | -0.25 |
| 2026-10-01 08:50 | c_banda_atr_regimen | LTC | timeout | -0.60% | -1.10% | -0.25 |
| 2026-10-01 08:50 | c_banda_atr_tope | HYPE | timeout | -0.11% | -1.21% | -0.28 |
| 2026-10-01 08:50 | estocastico_rebote | UNI | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 08:50 | c_banda_atr | LTC | timeout | -0.60% | -1.10% | -0.25 |
| 2026-10-01 08:45 | ruptura_estricta | ASTER | stop-loss | -2.00% | -2.50% | -0.56 |
| 2026-10-01 08:45 | ruptura_estricta | XDC | timeout | -0.47% | -0.97% | -0.22 |
| 2026-10-01 08:40 | macd_momentum_evento | HBAR | momentum perdido | -0.99% | -1.49% | -0.33 |
| 2026-10-01 08:40 | macd_sin_salida | MINA | timeout | -1.00% | -1.50% | -0.34 |
| 2026-10-01 08:40 | macd_sin_salida | BCH | timeout | -0.57% | -1.07% | -0.24 |
| 2026-10-01 08:40 | macd_momentum | HBAR | momentum perdido | -0.99% | -1.49% | -0.33 |
| 2026-10-01 08:35 | c_banda_atr_evento | SEI | stop-loss | -1.50% | -2.00% | -0.46 |

## Eventos de la última vuelta

- 2026-10-01 08:55 [pullback_tendencia] ENTRADA QNT @ 264.09 (22.44 €, apertura)
- 2026-10-01 08:55 [c_banda_atr] ENTRADA ALGO @ 0.11295 (22.47 €, apertura)
- 2026-10-01 08:55 [c_banda_atr_evento] ENTRADA ALGO @ 0.11295 (22.62 €, apertura)
- 2026-10-01 08:55 [macd_momentum] ENTRADA NIGHT @ 0.0374 (22.11 €, apertura)
- 2026-10-01 08:55 [macd_sin_salida] ENTRADA NIGHT @ 0.0374 (22.22 €, apertura)
- 2026-10-01 08:55 [macd_momentum_evento] ENTRADA NIGHT @ 0.0374 (22.23 €, apertura)
- 2026-10-01 09:00 [estocastico_rebote] CIERRE VVV take-profit bruto +1.80% neto +1.30%
- 2026-10-01 08:55 [c_banda_atr] ENTRADA SHIB @ 5.089e-06 (22.47 €, apertura)
- 2026-10-01 08:55 [c_banda_atr_evento] ENTRADA SHIB @ 5.089e-06 (22.62 €, apertura)
- 2026-10-01 08:55 [c_banda_atr] ENTRADA SKY @ 0.06888 (22.47 €, apertura)
- 2026-10-01 08:55 [c_banda_atr_evento] ENTRADA SKY @ 0.06888 (22.62 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
