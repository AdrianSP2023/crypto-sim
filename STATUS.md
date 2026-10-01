# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 13:56 UTC · vueltas 234 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 894.36 € (-3.23%) | 192 | 24 | 35% | -0.035% | -0.671% | -0.797% | -29.44 € |
| reversion_bb | 918.36 € (-0.64%) | 32 | 11 | 38% | +0.087% | -1.013% | -1.110% | -7.48 € |
| ruptura_volumen | 881.63 € (-4.61%) | 230 | 7 | 23% | -0.195% | -0.809% | -0.917% | -42.18 € |
| rebote_extremo | 922.29 € (-0.21%) | 10 | 0 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 894.08 € (-3.26%) | 137 | 0 | 14% | -0.274% | -0.967% | -1.072% | -30.16 € |
| macd_momentum | 879.66 € (-4.82%) | 331 | 19 | 21% | -0.012% | -0.591% | -0.702% | -44.21 € |
| estocastico_rebote | 878.57 € (-4.94%) | 269 | 15 | 30% | -0.161% | -0.758% | -0.868% | -46.15 € |
| ruptura_estricta | 886.98 € (-4.03%) | 131 | 4 | 24% | -0.535% | -1.237% | -1.359% | -36.98 € |
| macd_sin_salida | 884.10 € (-4.34%) | 243 | 17 | 34% | -0.113% | -0.720% | -0.835% | -39.86 € |
| c_banda_atr_tope | 913.07 € (-1.21%) | 44 | 5 | 27% | -0.045% | -1.131% | -1.251% | -11.45 € |
| ruptura_volumen_tope | 910.39 € (-1.50%) | 70 | 5 | 27% | +0.038% | -0.839% | -0.954% | -13.50 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.97 € (-4.36%) | 184 | 1 | 20% | -0.323% | -0.965% | -1.079% | -40.31 € |
| c_banda_atr_evento | 900.32 € (-2.59%) | 159 | 24 | 36% | +0.022% | -0.644% | -0.763% | -23.48 € |
| macd_momentum_evento | 884.54 € (-4.30%) | 284 | 19 | 18% | -0.019% | -0.612% | -0.718% | -39.34 € |
| ruptura_volumen_evento | 894.17 € (-3.25%) | 180 | 7 | 24% | -0.075% | -0.722% | -0.819% | -29.62 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 13:55 | macd_momentum_evento | MINA | momentum perdido | +0.15% | -0.35% | -0.08 |
| 2026-10-01 13:55 | ruptura_volumen_regimen | PEPE | timeout | -0.18% | -0.68% | -0.15 |
| 2026-10-01 13:55 | macd_momentum_regimen | MINA | momentum perdido | +0.15% | -0.35% | -0.08 |
| 2026-10-01 13:55 | macd_sin_salida | SEI | timeout | +0.05% | -0.45% | -0.10 |
| 2026-10-01 13:55 | ruptura_estricta | BCH | timeout | -0.54% | -1.04% | -0.23 |
| 2026-10-01 13:55 | macd_momentum | MINA | momentum perdido | +0.15% | -0.35% | -0.08 |
| 2026-10-01 13:55 | pullback_tendencia | ALGO | rotura de tendencia | -0.67% | -1.17% | -0.26 |
| 2026-10-01 13:50 | ruptura_volumen_evento | PEPE | timeout | +0.75% | +0.25% | +0.06 |
| 2026-10-01 13:50 | ruptura_volumen_evento | DOGE | timeout | -0.32% | -0.82% | -0.18 |
| 2026-10-01 13:50 | macd_momentum_evento | KSM | momentum perdido | +0.43% | -0.07% | -0.01 |
| 2026-10-01 13:50 | macd_sin_salida | OP | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-01 13:50 | macd_sin_salida | INJ | timeout | +0.32% | -0.18% | -0.04 |
| 2026-10-01 13:50 | macd_sin_salida | SUI | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-01 13:50 | macd_sin_salida | BTC | timeout | -0.30% | -0.80% | -0.18 |
| 2026-10-01 13:50 | macd_momentum | KSM | momentum perdido | +0.43% | -0.07% | -0.01 |

## Eventos de la última vuelta

- 2026-10-01 13:50 [pullback_tendencia] ENTRADA ALGO @ 0.11269 (22.36 €, apertura)
- 2026-10-01 13:55 [pullback_tendencia] CIERRE ALGO rotura de tendencia bruto -0.67% neto -1.17%
- 2026-10-01 13:55 [ruptura_estricta] CIERRE BCH timeout bruto -0.54% neto -1.04%
- 2026-10-01 13:55 [ruptura_volumen_regimen] CIERRE PEPE timeout bruto -0.18% neto -0.68%
- 2026-10-01 13:55 [macd_momentum] CIERRE MINA momentum perdido bruto +0.15% neto -0.35%
- 2026-10-01 13:55 [macd_momentum_regimen] CIERRE MINA momentum perdido bruto +0.15% neto -0.35%
- 2026-10-01 13:55 [macd_momentum_evento] CIERRE MINA momentum perdido bruto +0.15% neto -0.35%
- 2026-10-01 13:55 [macd_sin_salida] CIERRE SEI timeout bruto +0.05% neto -0.45%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
