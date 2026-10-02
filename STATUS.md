# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 12:31 UTC · vueltas 399 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.92 € (-3.93%) | 370 | 18 | 41% | +0.143% | -0.427% | -0.548% | -35.99 € |
| reversion_bb | 919.93 € (-0.47%) | 73 | 3 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 855.23 € (-7.47%) | 460 | 10 | 26% | -0.118% | -0.675% | -0.783% | -69.26 € |
| rebote_extremo | 922.68 € (-0.17%) | 15 | 1 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 887.88 € (-3.93%) | 266 | 9 | 21% | -0.012% | -0.611% | -0.697% | -36.89 € |
| macd_momentum | 846.62 € (-8.40%) | 748 | 15 | 24% | +0.066% | -0.469% | -0.569% | -77.74 € |
| estocastico_rebote | 878.44 € (-4.96%) | 450 | 35 | 37% | +0.103% | -0.455% | -0.563% | -46.44 € |
| ruptura_estricta | 881.01 € (-4.68%) | 249 | 11 | 32% | -0.159% | -0.765% | -0.880% | -43.27 € |
| macd_sin_salida | 876.47 € (-5.17%) | 487 | 26 | 39% | +0.121% | -0.433% | -0.543% | -47.90 € |
| c_banda_atr_tope | 913.24 € (-1.19%) | 84 | 5 | 38% | +0.258% | -0.556% | -0.676% | -10.75 € |
| ruptura_volumen_tope | 898.50 € (-2.79%) | 139 | 5 | 22% | -0.129% | -0.819% | -0.932% | -25.96 € |
| c_banda_atr_regimen | 900.55 € (-2.56%) | 222 | 19 | 42% | +0.160% | -0.457% | -0.586% | -23.33 € |
| macd_momentum_regimen | 869.29 € (-5.95%) | 511 | 15 | 24% | +0.071% | -0.480% | -0.580% | -55.06 € |
| ruptura_volumen_regimen | 859.87 € (-6.96%) | 383 | 10 | 23% | -0.186% | -0.754% | -0.866% | -64.63 € |
| c_banda_atr_evento | 894.17 € (-3.25%) | 335 | 8 | 41% | +0.188% | -0.390% | -0.505% | -29.89 € |
| macd_momentum_evento | 851.64 € (-7.86%) | 698 | 2 | 23% | +0.069% | -0.469% | -0.565% | -72.74 € |
| ruptura_volumen_evento | 867.14 € (-6.18%) | 410 | 4 | 26% | -0.056% | -0.621% | -0.723% | -57.09 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 12:30 | ruptura_volumen_evento | DASH | timeout | -0.06% | -0.56% | -0.12 |
| 2026-10-02 12:30 | ruptura_volumen_evento | HYPE | timeout | -0.20% | -0.70% | -0.15 |
| 2026-10-02 12:30 | macd_momentum_evento | DOT | momentum perdido | -0.42% | -0.92% | -0.20 |
| 2026-10-02 12:30 | ruptura_volumen_regimen | DASH | timeout | -0.06% | -0.56% | -0.12 |
| 2026-10-02 12:30 | ruptura_volumen_regimen | HYPE | timeout | -0.20% | -0.70% | -0.15 |
| 2026-10-02 12:30 | macd_momentum_regimen | TRUMP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 12:30 | macd_momentum_regimen | MINA | stop-loss | -1.86% | -2.36% | -0.51 |
| 2026-10-02 12:30 | macd_momentum_regimen | DOT | momentum perdido | -0.42% | -0.92% | -0.20 |
| 2026-10-02 12:30 | macd_momentum_regimen | ETH | momentum perdido | -0.11% | -0.61% | -0.13 |
| 2026-10-02 12:30 | c_banda_atr_regimen | TRUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 12:30 | c_banda_atr_regimen | MINA | stop-loss | -1.86% | -2.36% | -0.53 |
| 2026-10-02 12:30 | macd_sin_salida | TRUMP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 12:30 | macd_sin_salida | MINA | stop-loss | -1.86% | -2.36% | -0.52 |
| 2026-10-02 12:30 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 12:30 | estocastico_rebote | XMR | timeout | -0.17% | -0.68% | -0.15 |

## Eventos de la última vuelta

- 2026-10-02 12:25 [macd_momentum] ENTRADA XRP @ 1.3675 (21.18 €, apertura)
- 2026-10-02 12:25 [macd_momentum_regimen] ENTRADA XRP @ 1.3675 (21.74 €, apertura)
- 2026-10-02 12:30 [macd_momentum] CIERRE ETH momentum perdido bruto -0.11% neto -0.61%
- 2026-10-02 12:30 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto -0.11% neto -0.61%
- 2026-10-02 12:25 [pullback_tendencia] ENTRADA ADA @ 0.227717 (22.18 €, apertura)
- 2026-10-02 12:25 [c_banda_atr] ENTRADA AVAX @ 9.96 (22.21 €, apertura)
- 2026-10-02 12:25 [c_banda_atr_regimen] ENTRADA AVAX @ 9.96 (22.53 €, apertura)
- 2026-10-02 12:25 [pullback_tendencia] ENTRADA ZEC @ 1231.59 (22.18 €, apertura)
- 2026-10-02 12:30 [ruptura_volumen] CIERRE HYPE timeout bruto -0.20% neto -0.70%
- 2026-10-02 12:30 [ruptura_volumen_regimen] CIERRE HYPE timeout bruto -0.20% neto -0.70%
- 2026-10-02 12:30 [ruptura_volumen_evento] CIERRE HYPE timeout bruto -0.20% neto -0.70%
- 2026-10-02 12:25 [macd_momentum] ENTRADA XLM @ 0.199845 (21.17 €, apertura)
- 2026-10-02 12:25 [macd_sin_salida] ENTRADA XLM @ 0.199845 (21.91 €, apertura)
- 2026-10-02 12:25 [macd_momentum_regimen] ENTRADA XLM @ 0.199845 (21.74 €, apertura)
- 2026-10-02 12:30 [estocastico_rebote] CIERRE UNI timeout bruto +0.01% neto -0.49%
- 2026-10-02 12:30 [macd_momentum] CIERRE DOT momentum perdido bruto -0.42% neto -0.92%
- 2026-10-02 12:30 [macd_momentum_regimen] CIERRE DOT momentum perdido bruto -0.42% neto -0.92%
- 2026-10-02 12:30 [macd_momentum_evento] CIERRE DOT momentum perdido bruto -0.42% neto -0.92%
- 2026-10-02 12:30 [macd_sin_salida] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:30 [c_banda_atr] CIERRE MINA stop-loss bruto -1.86% neto -2.36%
- 2026-10-02 12:30 [macd_momentum] CIERRE MINA stop-loss bruto -1.86% neto -2.36%
- 2026-10-02 12:30 [macd_sin_salida] CIERRE MINA stop-loss bruto -1.86% neto -2.36%
- 2026-10-02 12:30 [c_banda_atr_regimen] CIERRE MINA stop-loss bruto -1.86% neto -2.36%
- 2026-10-02 12:30 [macd_momentum_regimen] CIERRE MINA stop-loss bruto -1.86% neto -2.36%
- 2026-10-02 12:30 [ruptura_volumen] CIERRE DASH timeout bruto -0.06% neto -0.56%
- 2026-10-02 12:30 [ruptura_volumen_regimen] CIERRE DASH timeout bruto -0.06% neto -0.56%
- 2026-10-02 12:30 [ruptura_volumen_evento] CIERRE DASH timeout bruto -0.06% neto -0.56%
- 2026-10-02 12:30 [c_banda_atr] CIERRE TRUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:30 [macd_momentum] CIERRE TRUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:25 [ruptura_estricta] ENTRADA TRUMP @ 1.952 (22.02 €, apertura)
- 2026-10-02 12:30 [macd_sin_salida] CIERRE TRUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:30 [c_banda_atr_regimen] CIERRE TRUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:30 [macd_momentum_regimen] CIERRE TRUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:30 [estocastico_rebote] CIERRE XMR timeout bruto -0.18% neto -0.68%
- 2026-10-02 12:25 [estocastico_rebote] ENTRADA SEI @ 0.06406 (21.95 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
