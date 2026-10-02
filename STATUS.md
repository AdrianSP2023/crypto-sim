# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 12:51 UTC · vueltas 403 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.43 € (-3.98%) | 371 | 21 | 40% | +0.140% | -0.430% | -0.551% | -36.33 € |
| reversion_bb | 920.07 € (-0.45%) | 73 | 3 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 855.49 € (-7.44%) | 462 | 16 | 26% | -0.115% | -0.671% | -0.780% | -69.20 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 886.21 € (-4.11%) | 273 | 6 | 21% | -0.020% | -0.617% | -0.703% | -38.17 € |
| macd_momentum | 844.84 € (-8.59%) | 756 | 21 | 24% | +0.061% | -0.473% | -0.573% | -79.29 € |
| estocastico_rebote | 876.56 € (-5.16%) | 461 | 25 | 37% | +0.098% | -0.459% | -0.566% | -47.90 € |
| ruptura_estricta | 880.19 € (-4.77%) | 254 | 10 | 32% | -0.147% | -0.751% | -0.866% | -43.35 € |
| macd_sin_salida | 875.22 € (-5.30%) | 492 | 30 | 39% | +0.116% | -0.437% | -0.546% | -48.80 € |
| c_banda_atr_tope | 913.32 € (-1.18%) | 84 | 5 | 38% | +0.258% | -0.556% | -0.676% | -10.75 € |
| ruptura_volumen_tope | 898.91 € (-2.74%) | 140 | 5 | 23% | -0.110% | -0.799% | -0.913% | -25.51 € |
| c_banda_atr_regimen | 899.94 € (-2.63%) | 223 | 21 | 42% | +0.155% | -0.462% | -0.591% | -23.67 € |
| macd_momentum_regimen | 867.46 € (-6.14%) | 519 | 21 | 24% | +0.064% | -0.486% | -0.586% | -56.64 € |
| ruptura_volumen_regimen | 860.14 € (-6.94%) | 385 | 16 | 23% | -0.182% | -0.749% | -0.862% | -64.56 € |
| c_banda_atr_evento | 893.79 € (-3.29%) | 336 | 7 | 41% | +0.185% | -0.394% | -0.509% | -30.23 € |
| macd_momentum_evento | 851.60 € (-7.86%) | 699 | 1 | 23% | +0.069% | -0.468% | -0.564% | -72.78 € |
| ruptura_volumen_evento | 867.03 € (-6.19%) | 410 | 4 | 26% | -0.056% | -0.621% | -0.723% | -57.09 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 12:50 | macd_momentum_evento | BNB | momentum perdido | +0.34% | -0.16% | -0.04 |
| 2026-10-02 12:50 | c_banda_atr_evento | ZRO | timeout | -1.02% | -1.52% | -0.34 |
| 2026-10-02 12:50 | macd_momentum_regimen | BNB | momentum perdido | +0.34% | -0.16% | -0.04 |
| 2026-10-02 12:50 | macd_momentum_regimen | CRV | momentum perdido | -0.56% | -1.06% | -0.23 |
| 2026-10-02 12:50 | macd_momentum_regimen | ALGO | momentum perdido | -0.95% | -1.45% | -0.32 |
| 2026-10-02 12:50 | macd_momentum_regimen | ENA | momentum perdido | -0.41% | -0.91% | -0.20 |
| 2026-10-02 12:50 | macd_momentum_regimen | SOL | momentum perdido | -0.03% | -0.53% | -0.12 |
| 2026-10-02 12:50 | macd_momentum_regimen | ETH | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-10-02 12:50 | macd_momentum_regimen | BTC | momentum perdido | -0.06% | -0.56% | -0.12 |
| 2026-10-02 12:50 | c_banda_atr_regimen | ZRO | timeout | -1.02% | -1.52% | -0.34 |
| 2026-10-02 12:50 | macd_sin_salida | VVV | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 12:50 | ruptura_estricta | VVV | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-02 12:50 | ruptura_estricta | NIGHT | take-profit | +3.00% | +2.50% | +0.55 |
| 2026-10-02 12:50 | estocastico_rebote | VVV | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 12:50 | estocastico_rebote | JUP | timeout | -0.15% | -0.65% | -0.14 |

## Eventos de la última vuelta

- 2026-10-02 12:50 [macd_momentum] CIERRE BTC momentum perdido bruto -0.06% neto -0.56%
- 2026-10-02 12:50 [macd_momentum_regimen] CIERRE BTC momentum perdido bruto -0.06% neto -0.56%
- 2026-10-02 12:50 [macd_momentum] CIERRE ETH momentum perdido bruto -0.13% neto -0.63%
- 2026-10-02 12:50 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto -0.13% neto -0.63%
- 2026-10-02 12:50 [macd_momentum] CIERRE SOL momentum perdido bruto -0.03% neto -0.53%
- 2026-10-02 12:50 [macd_momentum_regimen] CIERRE SOL momentum perdido bruto -0.03% neto -0.53%
- 2026-10-02 12:50 [c_banda_atr] CIERRE ZRO timeout bruto -1.03% neto -1.53%
- 2026-10-02 12:50 [c_banda_atr_regimen] CIERRE ZRO timeout bruto -1.03% neto -1.53%
- 2026-10-02 12:50 [c_banda_atr_evento] CIERRE ZRO timeout bruto -1.03% neto -1.53%
- 2026-10-02 12:50 [macd_momentum] CIERRE ENA momentum perdido bruto -0.41% neto -0.91%
- 2026-10-02 12:50 [macd_momentum_regimen] CIERRE ENA momentum perdido bruto -0.41% neto -0.91%
- 2026-10-02 12:45 [ruptura_estricta] ENTRADA POL @ 0.09977 (22.02 €, apertura)
- 2026-10-02 12:50 [macd_momentum] CIERRE ALGO momentum perdido bruto -0.95% neto -1.45%
- 2026-10-02 12:50 [macd_momentum_regimen] CIERRE ALGO momentum perdido bruto -0.95% neto -1.45%
- 2026-10-02 12:50 [macd_momentum] CIERRE CRV momentum perdido bruto -0.56% neto -1.06%
- 2026-10-02 12:50 [macd_momentum_regimen] CIERRE CRV momentum perdido bruto -0.56% neto -1.06%
- 2026-10-02 12:50 [ruptura_estricta] CIERRE NIGHT take-profit bruto +3.00% neto +2.50%
- 2026-10-02 12:50 [estocastico_rebote] CIERRE JUP timeout bruto -0.15% neto -0.65%
- 2026-10-02 12:50 [estocastico_rebote] CIERRE VVV stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:50 [ruptura_estricta] CIERRE VVV stop-loss bruto -2.00% neto -2.50%
- 2026-10-02 12:50 [macd_sin_salida] CIERRE VVV stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:50 [macd_momentum] CIERRE BNB momentum perdido bruto +0.34% neto -0.16%
- 2026-10-02 12:50 [macd_momentum_regimen] CIERRE BNB momentum perdido bruto +0.34% neto -0.16%
- 2026-10-02 12:50 [macd_momentum_evento] CIERRE BNB momentum perdido bruto +0.34% neto -0.16%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
