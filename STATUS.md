# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 08:26 UTC · vueltas 171 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.05 € (-2.73%) | 163 | 6 | 36% | -0.001% | -0.661% | -0.785% | -24.70 € |
| reversion_bb | 918.95 € (-0.57%) | 21 | 8 | 38% | +0.128% | -0.972% | -1.079% | -4.71 € |
| ruptura_volumen | 885.36 € (-4.21%) | 205 | 1 | 23% | -0.208% | -0.835% | -0.945% | -38.90 € |
| rebote_extremo | 923.91 € (-0.04%) | 3 | 5 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 898.01 € (-2.84%) | 119 | 1 | 16% | -0.244% | -0.965% | -1.071% | -26.23 € |
| macd_momentum | 885.05 € (-4.24%) | 291 | 2 | 22% | -0.005% | -0.594% | -0.703% | -39.22 € |
| estocastico_rebote | 886.75 € (-4.06%) | 210 | 39 | 33% | -0.117% | -0.741% | -0.859% | -35.50 € |
| ruptura_estricta | 891.56 € (-3.54%) | 118 | 4 | 26% | -0.456% | -1.179% | -1.305% | -31.87 € |
| macd_sin_salida | 889.12 € (-3.80%) | 212 | 7 | 37% | -0.085% | -0.708% | -0.821% | -34.31 € |
| c_banda_atr_tope | 915.25 € (-0.97%) | 36 | 2 | 28% | +0.005% | -1.095% | -1.215% | -9.08 € |
| ruptura_volumen_tope | 912.29 € (-1.29%) | 58 | 1 | 28% | +0.057% | -0.898% | -1.015% | -11.97 € |
| c_banda_atr_regimen | 903.00 € (-2.30%) | 106 | 3 | 35% | -0.100% | -0.846% | -0.989% | -20.61 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 905.03 € (-2.08%) | 130 | 6 | 38% | +0.078% | -0.626% | -0.741% | -18.70 € |
| macd_momentum_evento | 889.96 € (-3.71%) | 244 | 2 | 19% | -0.011% | -0.619% | -0.722% | -34.31 € |
| ruptura_volumen_evento | 897.95 € (-2.84%) | 155 | 1 | 24% | -0.072% | -0.743% | -0.840% | -26.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-01 08:20 | ruptura_volumen | NIGHT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 08:20 | c_banda_atr | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 08:15 | c_banda_atr_evento | OP | stop-loss | -1.65% | -2.15% | -0.49 |

## Eventos de la última vuelta

- 2026-10-01 08:20 [c_banda_atr] ENTRADA UNI @ 7.8415 (22.49 €, apertura)
- 2026-10-01 08:20 [c_banda_atr_tope] ENTRADA UNI @ 7.8415 (22.88 €, apertura)
- 2026-10-01 08:20 [c_banda_atr_evento] ENTRADA UNI @ 7.8415 (22.64 €, apertura)
- 2026-10-01 08:20 [macd_momentum] ENTRADA LTC @ 59.29 (22.13 €, apertura)
- 2026-10-01 08:20 [macd_sin_salida] ENTRADA LTC @ 59.29 (22.25 €, apertura)
- 2026-10-01 08:20 [macd_momentum_evento] ENTRADA LTC @ 59.29 (22.25 €, apertura)
- 2026-10-01 08:20 [estocastico_rebote] ENTRADA DOT @ 1.0825 (22.23 €, apertura)
- 2026-10-01 08:25 [estocastico_rebote] CIERRE USELESS stop-loss bruto -1.54% neto -2.04%
- 2026-10-01 08:25 [reversion_bb] CIERRE BNB timeout bruto +0.02% neto -1.08%
- 2026-10-01 08:20 [estocastico_rebote] ENTRADA SEI @ 0.06458 (22.22 €, apertura)
- 2026-10-01 08:20 [rebote_extremo] ENTRADA SPX @ 0.3849 (23.10 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
