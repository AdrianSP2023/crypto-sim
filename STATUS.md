# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 03:01 UTC · vueltas 371 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 886.36 € (-4.10%) | 291 | 24 | 35% | -0.007% | -0.596% | -0.717% | -39.42 € |
| reversion_bb | 919.83 € (-0.48%) | 64 | 8 | 56% | +0.482% | -0.426% | -0.533% | -6.29 € |
| ruptura_volumen | 867.69 € (-6.12%) | 335 | 22 | 25% | -0.182% | -0.760% | -0.868% | -57.18 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.83 € (-3.72%) | 195 | 11 | 15% | -0.178% | -0.813% | -0.902% | -35.98 € |
| macd_momentum | 863.70 € (-6.55%) | 529 | 32 | 20% | -0.002% | -0.552% | -0.654% | -65.17 € |
| estocastico_rebote | 873.48 € (-5.49%) | 344 | 15 | 32% | -0.092% | -0.668% | -0.776% | -51.82 € |
| ruptura_estricta | 883.75 € (-4.38%) | 169 | 27 | 25% | -0.452% | -1.108% | -1.225% | -42.57 € |
| macd_sin_salida | 876.18 € (-5.20%) | 364 | 37 | 34% | -0.068% | -0.640% | -0.751% | -52.62 € |
| c_banda_atr_tope | 912.38 € (-1.28%) | 67 | 5 | 31% | +0.080% | -0.815% | -0.929% | -12.54 € |
| ruptura_volumen_tope | 903.61 € (-2.23%) | 111 | 5 | 25% | -0.080% | -0.818% | -0.933% | -20.77 € |
| c_banda_atr_regimen | 897.82 € (-2.86%) | 140 | 29 | 29% | -0.208% | -0.895% | -1.028% | -28.64 € |
| macd_momentum_regimen | 886.14 € (-4.12%) | 296 | 28 | 19% | -0.030% | -0.618% | -0.724% | -41.43 € |
| ruptura_volumen_regimen | 872.24 € (-5.63%) | 262 | 18 | 21% | -0.291% | -0.891% | -1.004% | -52.60 € |
| c_banda_atr_evento | 892.26 € (-3.46%) | 258 | 24 | 36% | +0.032% | -0.570% | -0.686% | -33.53 € |
| macd_momentum_evento | 868.48 € (-6.03%) | 482 | 32 | 19% | -0.005% | -0.560% | -0.659% | -60.41 € |
| ruptura_volumen_evento | 880.04 € (-4.78%) | 285 | 22 | 26% | -0.104% | -0.696% | -0.797% | -44.84 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 03:00 | c_banda_atr_evento | ZEC | timeout | +0.28% | -0.22% | -0.05 |
| 2026-10-02 03:00 | macd_sin_salida | BNB | timeout | +0.27% | -0.23% | -0.05 |
| 2026-10-02 03:00 | reversion_bb | ADA | take-profit | +1.50% | +1.00% | +0.23 |
| 2026-10-02 03:00 | c_banda_atr | ZEC | timeout | +0.28% | -0.22% | -0.05 |
| 2026-10-02 02:55 | ruptura_volumen_evento | HYPE | timeout | +0.04% | -0.46% | -0.10 |
| 2026-10-02 02:55 | macd_momentum_evento | SHIB | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-10-02 02:55 | macd_momentum_evento | WLD | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 02:55 | ruptura_volumen_regimen | HYPE | timeout | +0.04% | -0.46% | -0.10 |
| 2026-10-02 02:55 | macd_momentum_regimen | SHIB | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-10-02 02:55 | macd_momentum_regimen | WLD | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 02:55 | macd_sin_salida | POL | timeout | +1.20% | +0.70% | +0.15 |
| 2026-10-02 02:55 | ruptura_estricta | WLFI | timeout | -0.40% | -0.90% | -0.20 |
| 2026-10-02 02:55 | macd_momentum | SHIB | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-10-02 02:55 | macd_momentum | WLD | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 02:55 | ruptura_volumen | HYPE | timeout | +0.04% | -0.46% | -0.10 |

## Eventos de la última vuelta

- 2026-10-02 02:55 [macd_momentum] ENTRADA ETH @ 2417.98 (21.48 €, apertura)
- 2026-10-02 02:55 [macd_momentum_regimen] ENTRADA ETH @ 2417.98 (22.07 €, apertura)
- 2026-10-02 02:55 [macd_momentum_evento] ENTRADA ETH @ 2417.98 (21.60 €, apertura)
- 2026-10-02 03:00 [reversion_bb] CIERRE ADA take-profit bruto +1.50% neto +1.00%
- 2026-10-02 03:00 [c_banda_atr] CIERRE ZEC timeout bruto +0.28% neto -0.22%
- 2026-10-02 03:00 [c_banda_atr_evento] CIERRE ZEC timeout bruto +0.28% neto -0.22%
- 2026-10-02 02:55 [macd_momentum] ENTRADA ARB @ 0.1802 (21.48 €, apertura)
- 2026-10-02 02:55 [macd_momentum_regimen] ENTRADA ARB @ 0.1802 (22.07 €, apertura)
- 2026-10-02 02:55 [macd_momentum_evento] ENTRADA ARB @ 0.1802 (21.60 €, apertura)
- 2026-10-02 02:55 [c_banda_atr] ENTRADA INJ @ 6.635 (22.12 €, apertura)
- 2026-10-02 02:55 [estocastico_rebote] ENTRADA INJ @ 6.635 (21.81 €, apertura)
- 2026-10-02 02:55 [c_banda_atr_regimen] ENTRADA INJ @ 6.635 (22.39 €, apertura)
- 2026-10-02 02:55 [c_banda_atr_evento] ENTRADA INJ @ 6.635 (22.27 €, apertura)
- 2026-10-02 02:55 [ruptura_volumen] ENTRADA MINA @ 0.1401 (21.68 €, apertura)
- 2026-10-02 02:55 [ruptura_volumen_regimen] ENTRADA MINA @ 0.1401 (21.79 €, apertura)
- 2026-10-02 02:55 [ruptura_volumen_evento] ENTRADA MINA @ 0.1401 (21.98 €, apertura)
- 2026-10-02 02:55 [ruptura_volumen] ENTRADA KSM @ 4.56 (21.68 €, apertura)
- 2026-10-02 02:55 [ruptura_volumen_regimen] ENTRADA KSM @ 4.56 (21.79 €, apertura)
- 2026-10-02 02:55 [ruptura_volumen_evento] ENTRADA KSM @ 4.56 (21.98 €, apertura)
- 2026-10-02 02:55 [ruptura_volumen] ENTRADA TRUMP @ 1.841 (21.68 €, apertura)
- 2026-10-02 02:55 [ruptura_volumen_regimen] ENTRADA TRUMP @ 1.841 (21.79 €, apertura)
- 2026-10-02 02:55 [ruptura_volumen_evento] ENTRADA TRUMP @ 1.841 (21.98 €, apertura)
- 2026-10-02 03:00 [macd_sin_salida] CIERRE BNB timeout bruto +0.27% neto -0.23%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
