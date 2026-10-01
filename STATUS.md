# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 01:36 UTC · vueltas 90 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.29 € (-2.27%) | 92 | 25 | 27% | -0.264% | -1.048% | -1.175% | -22.12 € |
| reversion_bb | 921.45 € (-0.30%) | 13 | 3 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 893.48 € (-3.33%) | 122 | 19 | 16% | -0.402% | -1.116% | -1.231% | -31.11 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.87 € (-2.20%) | 78 | 4 | 17% | -0.317% | -1.156% | -1.281% | -20.66 € |
| macd_momentum | 902.90 € (-2.31%) | 143 | 29 | 24% | -0.035% | -0.718% | -0.829% | -23.48 € |
| estocastico_rebote | 903.33 € (-2.26%) | 138 | 15 | 37% | +0.021% | -0.668% | -0.791% | -21.23 € |
| ruptura_estricta | 899.12 € (-2.72%) | 57 | 18 | 16% | -0.995% | -1.958% | -2.101% | -25.68 € |
| macd_sin_salida | 903.18 € (-2.28%) | 112 | 20 | 34% | -0.104% | -0.837% | -0.953% | -21.53 € |
| c_banda_atr_tope | 918.01 € (-0.67%) | 22 | 4 | 27% | -0.148% | -1.248% | -1.380% | -6.33 € |
| ruptura_volumen_tope | 915.32 € (-0.97%) | 33 | 5 | 18% | -0.115% | -1.215% | -1.296% | -9.23 € |
| c_banda_atr_regimen | 907.36 € (-1.83%) | 47 | 12 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.26 € (-1.73%) | 80 | 13 | 24% | -0.062% | -0.888% | -1.010% | -16.35 € |
| ruptura_volumen_regimen | 894.23 € (-3.25%) | 99 | 15 | 14% | -0.539% | -1.303% | -1.424% | -29.49 € |
| c_banda_atr_evento | 909.58 € (-1.59%) | 59 | 25 | 25% | -0.239% | -1.166% | -1.275% | -15.84 € |
| macd_momentum_evento | 907.90 € (-1.77%) | 96 | 29 | 18% | -0.066% | -0.841% | -0.940% | -18.50 € |
| ruptura_volumen_evento | 906.19 € (-1.95%) | 72 | 19 | 14% | -0.247% | -1.113% | -1.203% | -18.40 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 01:35 | ruptura_volumen_evento | XLM | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 01:35 | macd_momentum_evento | ENA | momentum perdido | -0.81% | -1.30% | -0.30 |
| 2026-10-01 01:35 | c_banda_atr_evento | NEAR | stop-loss | -1.51% | -2.31% | -0.53 |
| 2026-10-01 01:35 | ruptura_volumen_regimen | XLM | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 01:35 | c_banda_atr_tope | NEAR | stop-loss | -1.51% | -2.61% | -0.60 |
| 2026-10-01 01:35 | macd_sin_salida | PEPE | timeout | -0.03% | -0.53% | -0.12 |
| 2026-10-01 01:35 | macd_sin_salida | WLD | timeout | +0.29% | -0.21% | -0.05 |
| 2026-10-01 01:35 | macd_sin_salida | ARB | timeout | -0.11% | -0.61% | -0.14 |
| 2026-10-01 01:35 | macd_sin_salida | DOGE | timeout | +0.28% | -0.21% | -0.05 |
| 2026-10-01 01:35 | macd_sin_salida | XLM | timeout | +0.15% | -0.35% | -0.08 |
| 2026-10-01 01:35 | macd_sin_salida | AVAX | timeout | -1.04% | -1.54% | -0.35 |
| 2026-10-01 01:35 | ruptura_estricta | WLD | timeout | +0.29% | -0.21% | -0.05 |
| 2026-10-01 01:35 | macd_momentum | ENA | momentum perdido | -0.81% | -1.30% | -0.29 |
| 2026-10-01 01:35 | pullback_tendencia | MON | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 01:35 | pullback_tendencia | ENA | rotura de tendencia | -0.09% | -0.58% | -0.13 |

## Eventos de la última vuelta

- 2026-10-01 01:30 [ruptura_volumen] ENTRADA SOL @ 104.36 (22.34 €, apertura)
- 2026-10-01 01:30 [ruptura_volumen_regimen] ENTRADA SOL @ 104.36 (22.38 €, apertura)
- 2026-10-01 01:30 [ruptura_volumen_evento] ENTRADA SOL @ 104.36 (22.66 €, apertura)
- 2026-10-01 01:35 [c_banda_atr] CIERRE NEAR stop-loss bruto -1.51% neto -2.01%
- 2026-10-01 01:35 [c_banda_atr_tope] CIERRE NEAR stop-loss bruto -1.51% neto -2.61%
- 2026-10-01 01:35 [c_banda_atr_evento] CIERRE NEAR stop-loss bruto -1.51% neto -2.31%
- 2026-10-01 01:35 [macd_sin_salida] CIERRE AVAX timeout bruto -1.04% neto -1.54%
- 2026-10-01 01:35 [ruptura_volumen] CIERRE XLM stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 01:35 [macd_sin_salida] CIERRE XLM timeout bruto +0.15% neto -0.35%
- 2026-10-01 01:35 [ruptura_volumen_regimen] CIERRE XLM stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 01:35 [ruptura_volumen_evento] CIERRE XLM stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 01:35 [macd_sin_salida] CIERRE DOGE timeout bruto +0.28% neto -0.22%
- 2026-10-01 01:35 [macd_sin_salida] CIERRE ARB timeout bruto -0.11% neto -0.61%
- 2026-10-01 01:35 [pullback_tendencia] CIERRE ENA rotura de tendencia bruto -0.09% neto -0.59%
- 2026-10-01 01:35 [macd_momentum] CIERRE ENA momentum perdido bruto -0.81% neto -1.31%
- 2026-10-01 01:35 [macd_momentum_evento] CIERRE ENA momentum perdido bruto -0.81% neto -1.31%
- 2026-10-01 01:35 [ruptura_estricta] CIERRE WLD timeout bruto +0.29% neto -0.21%
- 2026-10-01 01:35 [macd_sin_salida] CIERRE WLD timeout bruto +0.29% neto -0.21%
- 2026-10-01 01:30 [ruptura_estricta] ENTRADA BCH @ 271.01 (22.46 €, apertura)
- 2026-10-01 01:30 [ruptura_volumen_regimen] ENTRADA BCH @ 271.01 (22.37 €, apertura)
- 2026-10-01 01:35 [macd_sin_salida] CIERRE PEPE timeout bruto -0.03% neto -0.53%
- 2026-10-01 01:35 [pullback_tendencia] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 01:30 [ruptura_volumen_regimen] ENTRADA KAS @ 0.03902 (22.37 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
