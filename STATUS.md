# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 01:06 UTC · vueltas 348 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.65 € (-4.28%) | 273 | 22 | 34% | -0.040% | -0.636% | -0.757% | -39.41 € |
| reversion_bb | 917.70 € (-0.71%) | 56 | 13 | 54% | +0.408% | -0.558% | -0.666% | -7.21 € |
| ruptura_volumen | 869.50 € (-5.92%) | 301 | 31 | 24% | -0.204% | -0.791% | -0.899% | -53.59 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.46 € (-3.87%) | 191 | 5 | 15% | -0.202% | -0.840% | -0.929% | -36.42 € |
| macd_momentum | 861.99 € (-6.74%) | 505 | 6 | 20% | -0.002% | -0.553% | -0.655% | -62.52 € |
| estocastico_rebote | 872.71 € (-5.58%) | 338 | 11 | 31% | -0.101% | -0.678% | -0.788% | -51.74 € |
| ruptura_estricta | 882.19 € (-4.55%) | 167 | 10 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 872.28 € (-5.62%) | 350 | 16 | 34% | -0.089% | -0.664% | -0.775% | -52.49 € |
| c_banda_atr_tope | 911.87 € (-1.34%) | 62 | 5 | 31% | +0.026% | -0.900% | -1.015% | -12.81 € |
| ruptura_volumen_tope | 904.97 € (-2.08%) | 103 | 5 | 26% | -0.041% | -0.797% | -0.913% | -18.80 € |
| c_banda_atr_regimen | 895.25 € (-3.14%) | 138 | 6 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 884.80 € (-4.27%) | 279 | 6 | 19% | -0.030% | -0.624% | -0.729% | -39.47 € |
| ruptura_volumen_regimen | 873.04 € (-5.54%) | 232 | 28 | 19% | -0.345% | -0.958% | -1.073% | -50.16 € |
| c_banda_atr_evento | 890.54 € (-3.65%) | 240 | 22 | 35% | -0.003% | -0.613% | -0.729% | -33.51 € |
| macd_momentum_evento | 866.76 € (-6.22%) | 458 | 6 | 19% | -0.005% | -0.562% | -0.661% | -57.75 € |
| ruptura_volumen_evento | 881.87 € (-4.58%) | 251 | 31 | 25% | -0.120% | -0.725% | -0.825% | -41.19 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 01:05 | ruptura_volumen_evento | AAVE | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 01:05 | macd_momentum_evento | SPX | momentum perdido | +0.31% | -0.19% | -0.04 |
| 2026-10-02 01:05 | macd_momentum_evento | TAO | momentum perdido | -0.42% | -0.92% | -0.20 |
| 2026-10-02 01:05 | macd_momentum_evento | SUI | momentum perdido | -0.09% | -0.59% | -0.13 |
| 2026-10-02 01:05 | macd_momentum_evento | SOL | timeout | +0.61% | +0.11% | +0.02 |
| 2026-10-02 01:05 | ruptura_volumen_regimen | AAVE | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 01:05 | macd_momentum_regimen | TAO | momentum perdido | -0.42% | -0.92% | -0.20 |
| 2026-10-02 01:05 | estocastico_rebote | PEPE | timeout | -0.48% | -0.98% | -0.21 |
| 2026-10-02 01:05 | macd_momentum | SPX | momentum perdido | +0.31% | -0.19% | -0.04 |
| 2026-10-02 01:05 | macd_momentum | TAO | momentum perdido | -0.42% | -0.92% | -0.20 |
| 2026-10-02 01:05 | macd_momentum | SUI | momentum perdido | -0.09% | -0.59% | -0.13 |
| 2026-10-02 01:05 | macd_momentum | SOL | timeout | +0.61% | +0.11% | +0.02 |
| 2026-10-02 01:05 | pullback_tendencia | PUMP | rotura de tendencia | -0.43% | -0.93% | -0.20 |
| 2026-10-02 01:05 | ruptura_volumen | AAVE | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 01:00 | macd_momentum_evento | BNB | momentum perdido | +0.01% | -0.49% | -0.11 |

## Eventos de la última vuelta

- 2026-10-02 01:05 [macd_momentum] CIERRE SOL timeout bruto +0.61% neto +0.11%
- 2026-10-02 01:05 [macd_momentum_evento] CIERRE SOL timeout bruto +0.61% neto +0.11%
- 2026-10-02 01:05 [macd_momentum] CIERRE SUI momentum perdido bruto -0.09% neto -0.59%
- 2026-10-02 01:05 [macd_momentum_evento] CIERRE SUI momentum perdido bruto -0.09% neto -0.59%
- 2026-10-02 01:00 [estocastico_rebote] ENTRADA AVAX @ 9.729 (21.82 €, apertura)
- 2026-10-02 01:05 [ruptura_volumen] CIERRE AAVE stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 01:05 [ruptura_volumen_regimen] CIERRE AAVE stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 01:05 [ruptura_volumen_evento] CIERRE AAVE stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 01:00 [pullback_tendencia] ENTRADA PUMP @ 0.005169 (22.20 €, apertura)
- 2026-10-02 01:05 [pullback_tendencia] CIERRE PUMP rotura de tendencia bruto -0.43% neto -0.93%
- 2026-10-02 01:05 [macd_momentum] CIERRE TAO momentum perdido bruto -0.42% neto -0.92%
- 2026-10-02 01:05 [macd_momentum_regimen] CIERRE TAO momentum perdido bruto -0.42% neto -0.92%
- 2026-10-02 01:05 [macd_momentum_evento] CIERRE TAO momentum perdido bruto -0.42% neto -0.92%
- 2026-10-02 01:05 [estocastico_rebote] CIERRE PEPE timeout bruto -0.48% neto -0.98%
- 2026-10-02 01:00 [ruptura_estricta] ENTRADA INJ @ 6.624 (22.06 €, apertura)
- 2026-10-02 01:00 [estocastico_rebote] ENTRADA SKY @ 0.07438 (21.81 €, apertura)
- 2026-10-02 01:05 [macd_momentum] CIERRE SPX momentum perdido bruto +0.31% neto -0.19%
- 2026-10-02 01:05 [macd_momentum_evento] CIERRE SPX momentum perdido bruto +0.31% neto -0.19%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
