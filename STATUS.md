# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 08:31 UTC · vueltas 172 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.09 € (-2.72%) | 164 | 6 | 36% | -0.001% | -0.660% | -0.784% | -24.82 € |
| reversion_bb | 919.43 € (-0.52%) | 21 | 8 | 38% | +0.128% | -0.972% | -1.079% | -4.71 € |
| ruptura_volumen | 885.34 € (-4.21%) | 205 | 1 | 23% | -0.208% | -0.835% | -0.945% | -38.90 € |
| rebote_extremo | 924.39 € (+0.02%) | 3 | 5 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 897.68 € (-2.87%) | 120 | 1 | 16% | -0.249% | -0.969% | -1.075% | -26.55 € |
| macd_momentum | 885.06 € (-4.24%) | 291 | 4 | 22% | -0.005% | -0.594% | -0.703% | -39.22 € |
| estocastico_rebote | 887.67 € (-3.96%) | 210 | 40 | 33% | -0.117% | -0.741% | -0.859% | -35.50 € |
| ruptura_estricta | 891.62 € (-3.53%) | 118 | 4 | 26% | -0.456% | -1.179% | -1.305% | -31.87 € |
| macd_sin_salida | 889.21 € (-3.79%) | 212 | 9 | 37% | -0.085% | -0.708% | -0.821% | -34.31 € |
| c_banda_atr_tope | 915.30 € (-0.97%) | 36 | 3 | 28% | +0.005% | -1.095% | -1.215% | -9.08 € |
| ruptura_volumen_tope | 912.27 € (-1.29%) | 58 | 1 | 28% | +0.057% | -0.898% | -1.015% | -11.97 € |
| c_banda_atr_regimen | 903.10 € (-2.29%) | 106 | 3 | 35% | -0.100% | -0.846% | -0.989% | -20.61 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 905.07 € (-2.07%) | 131 | 6 | 37% | +0.077% | -0.625% | -0.740% | -18.83 € |
| macd_momentum_evento | 889.97 € (-3.71%) | 244 | 4 | 19% | -0.011% | -0.619% | -0.722% | -34.31 € |
| ruptura_volumen_evento | 897.94 € (-2.85%) | 155 | 1 | 24% | -0.072% | -0.743% | -0.840% | -26.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 08:30 | c_banda_atr_evento | BCH | timeout | -0.04% | -0.54% | -0.12 |
| 2026-10-01 08:30 | pullback_tendencia | NIGHT | rotura de tendencia | -0.93% | -1.43% | -0.32 |
| 2026-10-01 08:30 | c_banda_atr | BCH | timeout | -0.04% | -0.54% | -0.12 |
| 2026-10-01 08:25 | estocastico_rebote | USELESS | stop-loss | -1.54% | -2.04% | -0.46 |
| 2026-10-01 08:25 | reversion_bb | BNB | timeout | +0.02% | -1.08% | -0.25 |
| 2026-10-01 08:20 | ruptura_volumen_evento | NIGHT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 08:20 | macd_momentum_evento | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 08:20 | macd_momentum_evento | QNT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 08:20 | c_banda_atr_evento | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 08:20 | ruptura_volumen_tope | NIGHT | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 08:20 | c_banda_atr_tope | QNT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-10-01 08:20 | macd_sin_salida | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 08:20 | macd_sin_salida | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 08:20 | macd_momentum | NIGHT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 08:20 | macd_momentum | QNT | take-profit | +2.00% | +1.50% | +0.33 |

## Eventos de la última vuelta

- 2026-10-01 08:25 [macd_momentum] ENTRADA HBAR @ 0.09329 (22.13 €, apertura)
- 2026-10-01 08:25 [macd_sin_salida] ENTRADA HBAR @ 0.09329 (22.25 €, apertura)
- 2026-10-01 08:25 [macd_momentum_evento] ENTRADA HBAR @ 0.09329 (22.25 €, apertura)
- 2026-10-01 08:25 [macd_momentum] ENTRADA UNI @ 7.8976 (22.13 €, apertura)
- 2026-10-01 08:25 [macd_sin_salida] ENTRADA UNI @ 7.8976 (22.25 €, apertura)
- 2026-10-01 08:25 [macd_momentum_evento] ENTRADA UNI @ 7.8976 (22.25 €, apertura)
- 2026-10-01 08:25 [c_banda_atr] ENTRADA ICP @ 2.936 (22.49 €, apertura)
- 2026-10-01 08:25 [c_banda_atr_tope] ENTRADA ICP @ 2.936 (22.88 €, apertura)
- 2026-10-01 08:25 [c_banda_atr_evento] ENTRADA ICP @ 2.936 (22.64 €, apertura)
- 2026-10-01 08:25 [estocastico_rebote] ENTRADA FET @ 0.207 (17.37 €, apertura)
- 2026-10-01 08:25 [pullback_tendencia] ENTRADA TRX @ 0.298743 (22.45 €, apertura)
- 2026-10-01 08:30 [pullback_tendencia] CIERRE NIGHT rotura de tendencia bruto -0.93% neto -1.43%
- 2026-10-01 08:30 [c_banda_atr] CIERRE BCH timeout bruto -0.04% neto -0.54%
- 2026-10-01 08:30 [c_banda_atr_evento] CIERRE BCH timeout bruto -0.04% neto -0.54%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
