# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 20:22 UTC · vueltas 305 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.14 € (-3.69%) | 244 | 27 | 36% | -0.032% | -0.639% | -0.762% | -35.51 € |
| reversion_bb | 917.25 € (-0.76%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 873.51 € (-5.49%) | 287 | 5 | 25% | -0.193% | -0.784% | -0.891% | -50.76 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.33 € (-3.67%) | 177 | 6 | 15% | -0.200% | -0.849% | -0.942% | -34.15 € |
| macd_momentum | 870.33 € (-5.83%) | 440 | 32 | 22% | +0.014% | -0.545% | -0.649% | -53.90 € |
| estocastico_rebote | 878.65 € (-4.93%) | 296 | 23 | 32% | -0.106% | -0.695% | -0.806% | -46.53 € |
| ruptura_estricta | 884.14 € (-4.34%) | 156 | 10 | 25% | -0.443% | -1.112% | -1.227% | -39.52 € |
| macd_sin_salida | 880.86 € (-4.69%) | 312 | 27 | 37% | -0.022% | -0.605% | -0.719% | -42.93 € |
| c_banda_atr_tope | 911.98 € (-1.33%) | 56 | 5 | 30% | +0.019% | -0.953% | -1.068% | -12.26 € |
| ruptura_volumen_tope | 907.62 € (-1.80%) | 94 | 4 | 29% | +0.020% | -0.760% | -0.873% | -16.39 € |
| c_banda_atr_regimen | 900.95 € (-2.52%) | 117 | 21 | 33% | -0.150% | -0.873% | -1.012% | -23.43 € |
| macd_momentum_regimen | 891.08 € (-3.59%) | 240 | 29 | 22% | +0.003% | -0.606% | -0.715% | -33.10 € |
| ruptura_volumen_regimen | 876.30 € (-5.19%) | 221 | 4 | 19% | -0.340% | -0.958% | -1.073% | -47.86 € |
| c_banda_atr_evento | 896.06 € (-3.05%) | 211 | 27 | 36% | +0.011% | -0.614% | -0.731% | -29.59 € |
| macd_momentum_evento | 875.15 € (-5.31%) | 393 | 32 | 20% | +0.013% | -0.554% | -0.654% | -49.08 € |
| ruptura_volumen_evento | 885.94 € (-4.14%) | 237 | 5 | 26% | -0.101% | -0.713% | -0.811% | -38.33 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-01 20:15 | macd_sin_salida | SPX | timeout | +0.90% | +0.40% | +0.09 |

## Eventos de la última vuelta

- 2026-10-01 20:15 [pullback_tendencia] ENTRADA BTC @ 75372.3 (22.26 €, apertura)
- 2026-10-01 20:15 [pullback_tendencia] ENTRADA ETH @ 2401.49 (22.26 €, apertura)
- 2026-10-01 20:20 [ruptura_estricta] CIERRE ETH timeout bruto -0.06% neto -0.56%
- 2026-10-01 20:15 [pullback_tendencia] ENTRADA ADA @ 0.220978 (22.26 €, apertura)
- 2026-10-01 20:20 [pullback_tendencia] CIERRE ADA rotura de tendencia bruto -0.16% neto -0.66%
- 2026-10-01 20:20 [ruptura_estricta] CIERRE ADA timeout bruto -0.91% neto -1.41%
- 2026-10-01 20:20 [macd_momentum] CIERRE AVAX momentum perdido bruto -0.15% neto -0.65%
- 2026-10-01 20:20 [macd_sin_salida] CIERRE AVAX timeout bruto +0.61% neto +0.11%
- 2026-10-01 20:20 [macd_momentum_regimen] CIERRE AVAX momentum perdido bruto -0.15% neto -0.65%
- 2026-10-01 20:20 [macd_momentum_evento] CIERRE AVAX momentum perdido bruto -0.15% neto -0.65%
- 2026-10-01 20:20 [ruptura_estricta] CIERRE XLM timeout bruto -0.37% neto -0.87%
- 2026-10-01 20:20 [ruptura_estricta] CIERRE LTC timeout bruto +1.00% neto +0.50%
- 2026-10-01 20:15 [macd_momentum] ENTRADA DOGE @ 0.08441 (21.76 €, apertura)
- 2026-10-01 20:15 [macd_momentum_regimen] ENTRADA DOGE @ 0.08441 (22.28 €, apertura)
- 2026-10-01 20:15 [macd_momentum_evento] ENTRADA DOGE @ 0.08441 (21.88 €, apertura)
- 2026-10-01 20:20 [ruptura_volumen_tope] CIERRE DOT timeout bruto +0.15% neto -0.35%
- 2026-10-01 20:15 [macd_momentum] ENTRADA POL @ 0.09593 (21.76 €, apertura)
- 2026-10-01 20:15 [macd_sin_salida] ENTRADA POL @ 0.09593 (22.04 €, apertura)
- 2026-10-01 20:15 [macd_momentum_regimen] ENTRADA POL @ 0.09593 (22.28 €, apertura)
- 2026-10-01 20:15 [macd_momentum_evento] ENTRADA POL @ 0.09593 (21.88 €, apertura)
- 2026-10-01 20:20 [macd_sin_salida] CIERRE RENDER timeout bruto -0.12% neto -0.62%
- 2026-10-01 20:15 [macd_momentum] ENTRADA FIL @ 0.906 (21.76 €, apertura)
- 2026-10-01 20:15 [macd_momentum_regimen] ENTRADA FIL @ 0.906 (22.28 €, apertura)
- 2026-10-01 20:15 [macd_momentum_evento] ENTRADA FIL @ 0.906 (21.88 €, apertura)
- 2026-10-01 20:20 [estocastico_rebote] CIERRE WLFI timeout bruto +0.61% neto +0.11%
- 2026-10-01 20:20 [macd_sin_salida] CIERRE DASH timeout bruto -0.17% neto -0.67%
- 2026-10-01 20:15 [pullback_tendencia] ENTRADA BNB @ 684.5 (22.26 €, apertura)
- 2026-10-01 20:20 [pullback_tendencia] CIERRE BNB rotura de tendencia bruto -0.02% neto -0.52%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
