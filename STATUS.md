# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 11:46 UTC · vueltas 390 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.12 € (-3.80%) | 355 | 21 | 41% | +0.158% | -0.416% | -0.535% | -33.66 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 855.90 € (-7.39%) | 449 | 14 | 26% | -0.114% | -0.672% | -0.778% | -67.39 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 888.76 € (-3.84%) | 259 | 11 | 21% | -0.003% | -0.605% | -0.691% | -35.56 € |
| macd_momentum | 847.91 € (-8.26%) | 729 | 16 | 24% | +0.062% | -0.473% | -0.572% | -76.59 € |
| estocastico_rebote | 878.33 € (-4.97%) | 438 | 32 | 38% | +0.116% | -0.444% | -0.551% | -44.12 € |
| ruptura_estricta | 880.56 € (-4.73%) | 246 | 10 | 32% | -0.161% | -0.768% | -0.883% | -42.97 € |
| macd_sin_salida | 876.07 € (-5.21%) | 478 | 27 | 39% | +0.113% | -0.441% | -0.549% | -47.89 € |
| c_banda_atr_tope | 912.86 € (-1.23%) | 82 | 5 | 38% | +0.248% | -0.574% | -0.689% | -10.83 € |
| ruptura_volumen_tope | 898.96 € (-2.74%) | 134 | 5 | 23% | -0.110% | -0.807% | -0.919% | -24.67 € |
| c_banda_atr_regimen | 901.74 € (-2.43%) | 207 | 22 | 43% | +0.187% | -0.440% | -0.567% | -20.96 € |
| macd_momentum_regimen | 870.61 € (-5.80%) | 492 | 16 | 24% | +0.066% | -0.487% | -0.586% | -53.87 € |
| ruptura_volumen_regimen | 860.54 € (-6.89%) | 372 | 14 | 24% | -0.183% | -0.753% | -0.863% | -62.75 € |
| c_banda_atr_evento | 895.04 € (-3.16%) | 322 | 21 | 42% | +0.206% | -0.376% | -0.492% | -27.73 € |
| macd_momentum_evento | 852.61 € (-7.75%) | 682 | 16 | 23% | +0.065% | -0.474% | -0.570% | -71.89 € |
| ruptura_volumen_evento | 868.07 € (-6.08%) | 399 | 14 | 27% | -0.050% | -0.616% | -0.717% | -55.20 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 11:45 | macd_momentum_evento | XDC | momentum perdido | +0.77% | +0.27% | +0.06 |
| 2026-10-02 11:45 | c_banda_atr_evento | SPX | timeout | -0.03% | -0.53% | -0.12 |
| 2026-10-02 11:45 | macd_momentum_regimen | XDC | momentum perdido | +0.77% | +0.27% | +0.06 |
| 2026-10-02 11:45 | estocastico_rebote | MINA | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 11:45 | estocastico_rebote | PEPE | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 11:45 | estocastico_rebote | FET | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 11:45 | macd_momentum | XDC | momentum perdido | +0.77% | +0.27% | +0.06 |
| 2026-10-02 11:45 | pullback_tendencia | ADA | rotura de tendencia | -0.22% | -0.72% | -0.16 |
| 2026-10-02 11:45 | pullback_tendencia | XRP | rotura de tendencia | -0.48% | -0.98% | -0.22 |
| 2026-10-02 11:45 | c_banda_atr | SPX | timeout | -0.03% | -0.53% | -0.12 |
| 2026-10-02 11:40 | macd_momentum_evento | HYPE | momentum perdido | +1.18% | +0.68% | +0.15 |
| 2026-10-02 11:40 | macd_momentum_regimen | HYPE | momentum perdido | +1.18% | +0.68% | +0.15 |
| 2026-10-02 11:40 | c_banda_atr_tope | POL | timeout | -0.23% | -0.73% | -0.17 |
| 2026-10-02 11:40 | ruptura_estricta | NIGHT | take-profit | +3.00% | +2.50% | +0.55 |
| 2026-10-02 11:40 | estocastico_rebote | MON | timeout | +1.10% | +0.60% | +0.13 |

## Eventos de la última vuelta

- 2026-10-02 11:45 [pullback_tendencia] CIERRE XRP rotura de tendencia bruto -0.48% neto -0.98%
- 2026-10-02 11:40 [macd_momentum] ENTRADA ETH @ 2447.27 (21.19 €, apertura)
- 2026-10-02 11:40 [macd_momentum_regimen] ENTRADA ETH @ 2447.27 (21.76 €, apertura)
- 2026-10-02 11:40 [macd_momentum_evento] ENTRADA ETH @ 2447.27 (21.31 €, apertura)
- 2026-10-02 11:45 [pullback_tendencia] CIERRE ADA rotura de tendencia bruto -0.22% neto -0.72%
- 2026-10-02 11:45 [estocastico_rebote] CIERRE FET stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 11:40 [c_banda_atr] ENTRADA WLD @ 0.4836 (22.27 €, apertura)
- 2026-10-02 11:40 [c_banda_atr_tope] ENTRADA WLD @ 0.4836 (22.84 €, apertura)
- 2026-10-02 11:40 [c_banda_atr_regimen] ENTRADA WLD @ 0.4836 (22.58 €, apertura)
- 2026-10-02 11:40 [c_banda_atr_evento] ENTRADA WLD @ 0.4836 (22.42 €, apertura)
- 2026-10-02 11:45 [macd_momentum] CIERRE XDC momentum perdido bruto +0.77% neto +0.27%
- 2026-10-02 11:45 [macd_momentum_regimen] CIERRE XDC momentum perdido bruto +0.77% neto +0.27%
- 2026-10-02 11:45 [macd_momentum_evento] CIERRE XDC momentum perdido bruto +0.77% neto +0.27%
- 2026-10-02 11:40 [macd_momentum] ENTRADA NIGHT @ 0.04057 (21.19 €, apertura)
- 2026-10-02 11:40 [macd_sin_salida] ENTRADA NIGHT @ 0.04057 (21.91 €, apertura)
- 2026-10-02 11:40 [macd_momentum_regimen] ENTRADA NIGHT @ 0.04057 (21.76 €, apertura)
- 2026-10-02 11:40 [macd_momentum_evento] ENTRADA NIGHT @ 0.04057 (21.31 €, apertura)
- 2026-10-02 11:40 [ruptura_volumen] ENTRADA JUP @ 0.29399 (21.42 €, apertura)
- 2026-10-02 11:40 [ruptura_volumen_regimen] ENTRADA JUP @ 0.29399 (21.54 €, apertura)
- 2026-10-02 11:40 [ruptura_volumen_evento] ENTRADA JUP @ 0.29399 (21.73 €, apertura)
- 2026-10-02 11:45 [estocastico_rebote] CIERRE PEPE stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 11:45 [estocastico_rebote] CIERRE MINA stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 11:40 [estocastico_rebote] ENTRADA VVV @ 26.676 (22.00 €, apertura)
- 2026-10-02 11:45 [c_banda_atr] CIERRE SPX timeout bruto -0.02% neto -0.52%
- 2026-10-02 11:45 [c_banda_atr_evento] CIERRE SPX timeout bruto -0.02% neto -0.52%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
