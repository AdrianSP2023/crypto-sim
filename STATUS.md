# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 12:46 UTC · vueltas 402 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 886.81 € (-4.05%) | 370 | 22 | 41% | +0.143% | -0.427% | -0.548% | -35.99 € |
| reversion_bb | 919.83 € (-0.48%) | 73 | 3 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 854.61 € (-7.53%) | 462 | 16 | 26% | -0.115% | -0.671% | -0.780% | -69.20 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 886.09 € (-4.13%) | 273 | 6 | 21% | -0.020% | -0.617% | -0.703% | -38.17 € |
| macd_momentum | 844.36 € (-8.64%) | 749 | 28 | 24% | +0.064% | -0.471% | -0.571% | -78.17 € |
| estocastico_rebote | 875.76 € (-5.25%) | 459 | 27 | 37% | +0.102% | -0.455% | -0.562% | -47.31 € |
| ruptura_estricta | 879.98 € (-4.79%) | 252 | 11 | 32% | -0.152% | -0.757% | -0.872% | -43.35 € |
| macd_sin_salida | 873.91 € (-5.45%) | 491 | 31 | 40% | +0.119% | -0.434% | -0.543% | -48.36 € |
| c_banda_atr_tope | 913.18 € (-1.20%) | 84 | 5 | 38% | +0.258% | -0.556% | -0.676% | -10.75 € |
| ruptura_volumen_tope | 898.63 € (-2.77%) | 140 | 5 | 23% | -0.110% | -0.799% | -0.913% | -25.51 € |
| c_banda_atr_regimen | 899.31 € (-2.70%) | 222 | 22 | 42% | +0.160% | -0.457% | -0.586% | -23.33 € |
| macd_momentum_regimen | 866.97 € (-6.20%) | 512 | 28 | 24% | +0.068% | -0.483% | -0.583% | -55.49 € |
| ruptura_volumen_regimen | 859.25 € (-7.03%) | 385 | 16 | 23% | -0.182% | -0.749% | -0.862% | -64.56 € |
| c_banda_atr_evento | 893.67 € (-3.31%) | 335 | 8 | 41% | +0.188% | -0.390% | -0.505% | -29.89 € |
| macd_momentum_evento | 851.69 € (-7.85%) | 698 | 2 | 23% | +0.069% | -0.469% | -0.565% | -72.74 € |
| ruptura_volumen_evento | 867.01 € (-6.19%) | 410 | 4 | 26% | -0.056% | -0.621% | -0.723% | -57.09 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 12:45 | macd_momentum_regimen | ZEC | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 12:45 | macd_sin_salida | PENGU | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 12:45 | macd_sin_salida | ZEC | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 12:45 | ruptura_estricta | ZEC | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-02 12:45 | estocastico_rebote | SPX | timeout | -0.20% | -0.70% | -0.15 |
| 2026-10-02 12:45 | estocastico_rebote | BNB | timeout | +0.50% | -0.00% | -0.00 |
| 2026-10-02 12:45 | estocastico_rebote | PENGU | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 12:45 | estocastico_rebote | CRV | timeout | -0.82% | -1.32% | -0.29 |
| 2026-10-02 12:45 | estocastico_rebote | ZEC | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 12:45 | estocastico_rebote | ETH | timeout | -0.14% | -0.64% | -0.14 |
| 2026-10-02 12:45 | macd_momentum | ZEC | stop-loss | -1.50% | -2.00% | -0.42 |
| 2026-10-02 12:45 | pullback_tendencia | VVV | rotura de tendencia | -1.36% | -1.86% | -0.41 |
| 2026-10-02 12:45 | pullback_tendencia | ALGO | rotura de tendencia | -1.04% | -1.54% | -0.34 |
| 2026-10-02 12:45 | pullback_tendencia | ENA | rotura de tendencia | -0.55% | -1.04% | -0.23 |
| 2026-10-02 12:45 | pullback_tendencia | ZEC | rotura de tendencia | -0.99% | -1.49% | -0.33 |

## Eventos de la última vuelta

- 2026-10-02 12:45 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto -0.21% neto -0.71%
- 2026-10-02 12:45 [estocastico_rebote] CIERRE ETH timeout bruto -0.14% neto -0.64%
- 2026-10-02 12:45 [pullback_tendencia] CIERRE SOL rotura de tendencia bruto -0.11% neto -0.61%
- 2026-10-02 12:45 [pullback_tendencia] CIERRE ZEC rotura de tendencia bruto -0.99% neto -1.49%
- 2026-10-02 12:45 [macd_momentum] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:45 [estocastico_rebote] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:45 [ruptura_estricta] CIERRE ZEC stop-loss bruto -2.00% neto -2.50%
- 2026-10-02 12:45 [macd_sin_salida] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:45 [macd_momentum_regimen] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:40 [estocastico_rebote] ENTRADA DOT @ 1.0841 (21.95 €, apertura)
- 2026-10-02 12:40 [pullback_tendencia] ENTRADA ENA @ 0.2202 (22.18 €, apertura)
- 2026-10-02 12:45 [pullback_tendencia] CIERRE ENA rotura de tendencia bruto -0.54% neto -1.04%
- 2026-10-02 12:40 [macd_momentum] ENTRADA ENA @ 0.2202 (21.15 €, apertura)
- 2026-10-02 12:40 [macd_sin_salida] ENTRADA ENA @ 0.2202 (21.91 €, apertura)
- 2026-10-02 12:40 [macd_momentum_regimen] ENTRADA ENA @ 0.2202 (21.72 €, apertura)
- 2026-10-02 12:45 [pullback_tendencia] CIERRE ALGO rotura de tendencia bruto -1.04% neto -1.54%
- 2026-10-02 12:45 [estocastico_rebote] CIERRE CRV timeout bruto -0.83% neto -1.33%
- 2026-10-02 12:45 [pullback_tendencia] CIERRE VVV rotura de tendencia bruto -1.36% neto -1.86%
- 2026-10-02 12:40 [ruptura_estricta] ENTRADA WLFI @ 0.0503 (22.02 €, apertura)
- 2026-10-02 12:45 [estocastico_rebote] CIERRE PENGU stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:45 [macd_sin_salida] CIERRE PENGU stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:45 [estocastico_rebote] CIERRE BNB timeout bruto +0.50% neto -0.00%
- 2026-10-02 12:40 [macd_momentum] ENTRADA SEI @ 0.0642 (21.15 €, apertura)
- 2026-10-02 12:40 [macd_momentum_regimen] ENTRADA SEI @ 0.0642 (21.72 €, apertura)
- 2026-10-02 12:45 [estocastico_rebote] CIERRE SPX timeout bruto -0.20% neto -0.70%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
