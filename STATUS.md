# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 20:27 UTC · vueltas 306 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.11 € (-3.69%) | 244 | 27 | 36% | -0.032% | -0.639% | -0.762% | -35.51 € |
| reversion_bb | 917.18 € (-0.76%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 873.44 € (-5.50%) | 287 | 6 | 25% | -0.193% | -0.784% | -0.891% | -50.76 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.29 € (-3.67%) | 177 | 6 | 15% | -0.200% | -0.849% | -0.942% | -34.15 € |
| macd_momentum | 870.19 € (-5.85%) | 440 | 34 | 22% | +0.014% | -0.545% | -0.649% | -53.90 € |
| estocastico_rebote | 878.64 € (-4.93%) | 296 | 23 | 32% | -0.106% | -0.695% | -0.806% | -46.53 € |
| ruptura_estricta | 884.11 € (-4.34%) | 157 | 9 | 25% | -0.437% | -1.105% | -1.220% | -39.52 € |
| macd_sin_salida | 880.69 € (-4.71%) | 312 | 29 | 37% | -0.022% | -0.605% | -0.719% | -42.93 € |
| c_banda_atr_tope | 911.95 € (-1.33%) | 56 | 5 | 30% | +0.019% | -0.953% | -1.068% | -12.26 € |
| ruptura_volumen_tope | 907.59 € (-1.80%) | 94 | 5 | 29% | +0.020% | -0.760% | -0.873% | -16.39 € |
| c_banda_atr_regimen | 900.89 € (-2.53%) | 117 | 21 | 33% | -0.150% | -0.873% | -1.012% | -23.43 € |
| macd_momentum_regimen | 890.98 € (-3.60%) | 240 | 31 | 22% | +0.003% | -0.606% | -0.715% | -33.10 € |
| ruptura_volumen_regimen | 876.24 € (-5.19%) | 221 | 5 | 19% | -0.340% | -0.958% | -1.073% | -47.86 € |
| c_banda_atr_evento | 896.03 € (-3.05%) | 211 | 27 | 36% | +0.011% | -0.614% | -0.731% | -29.59 € |
| macd_momentum_evento | 875.01 € (-5.33%) | 393 | 34 | 20% | +0.013% | -0.554% | -0.654% | -49.08 € |
| ruptura_volumen_evento | 885.87 € (-4.15%) | 237 | 6 | 26% | -0.101% | -0.713% | -0.811% | -38.33 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 20:25 | ruptura_estricta | SPX | timeout | +0.51% | +0.01% | +0.00 |
| 2026-10-01 20:20 | macd_momentum_evento | AVAX | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-01 20:20 | macd_momentum_regimen | AVAX | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-01 20:20 | ruptura_volumen_tope | DOT | timeout | +0.15% | -0.35% | -0.08 |
| 2026-10-01 20:20 | macd_sin_salida | DASH | timeout | -0.17% | -0.67% | -0.15 |
| 2026-10-01 20:20 | macd_sin_salida | RENDER | timeout | -0.12% | -0.62% | -0.14 |
| 2026-10-01 20:20 | macd_sin_salida | AVAX | timeout | +0.61% | +0.11% | +0.02 |
| 2026-10-01 20:20 | ruptura_estricta | LTC | timeout | +1.00% | +0.50% | +0.11 |
| 2026-10-01 20:20 | ruptura_estricta | XLM | timeout | -0.37% | -0.87% | -0.19 |
| 2026-10-01 20:20 | ruptura_estricta | ADA | timeout | -0.91% | -1.41% | -0.31 |
| 2026-10-01 20:20 | ruptura_estricta | ETH | timeout | -0.07% | -0.56% | -0.12 |
| 2026-10-01 20:20 | estocastico_rebote | WLFI | timeout | +0.61% | +0.11% | +0.02 |
| 2026-10-01 20:20 | macd_momentum | AVAX | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-01 20:20 | pullback_tendencia | BNB | rotura de tendencia | -0.02% | -0.52% | -0.12 |
| 2026-10-01 20:20 | pullback_tendencia | ADA | rotura de tendencia | -0.16% | -0.66% | -0.15 |

## Eventos de la última vuelta

- 2026-10-01 20:20 [ruptura_volumen] ENTRADA ICP @ 2.918 (21.84 €, apertura)
- 2026-10-01 20:20 [macd_momentum] ENTRADA ICP @ 2.918 (21.76 €, apertura)
- 2026-10-01 20:20 [macd_sin_salida] ENTRADA ICP @ 2.918 (22.03 €, apertura)
- 2026-10-01 20:20 [ruptura_volumen_tope] ENTRADA ICP @ 2.918 (22.70 €, apertura)
- 2026-10-01 20:20 [macd_momentum_regimen] ENTRADA ICP @ 2.918 (22.28 €, apertura)
- 2026-10-01 20:20 [ruptura_volumen_regimen] ENTRADA ICP @ 2.918 (21.91 €, apertura)
- 2026-10-01 20:20 [macd_momentum_evento] ENTRADA ICP @ 2.918 (21.88 €, apertura)
- 2026-10-01 20:20 [ruptura_volumen_evento] ENTRADA ICP @ 2.918 (22.15 €, apertura)
- 2026-10-01 20:20 [macd_momentum] ENTRADA XMR @ 485.23 (21.76 €, apertura)
- 2026-10-01 20:20 [macd_sin_salida] ENTRADA XMR @ 485.23 (22.03 €, apertura)
- 2026-10-01 20:20 [macd_momentum_regimen] ENTRADA XMR @ 485.23 (22.28 €, apertura)
- 2026-10-01 20:20 [macd_momentum_evento] ENTRADA XMR @ 485.23 (21.88 €, apertura)
- 2026-10-01 20:25 [ruptura_estricta] CIERRE SPX timeout bruto +0.51% neto +0.01%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
