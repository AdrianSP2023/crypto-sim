# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 11:41 UTC · vueltas 389 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.80 € (-3.73%) | 354 | 21 | 41% | +0.158% | -0.415% | -0.535% | -33.54 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 856.50 € (-7.33%) | 449 | 13 | 26% | -0.114% | -0.672% | -0.778% | -67.39 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.51 € (-3.76%) | 257 | 13 | 21% | -0.000% | -0.603% | -0.689% | -35.19 € |
| macd_momentum | 848.49 € (-8.20%) | 728 | 15 | 23% | +0.061% | -0.475% | -0.573% | -76.64 € |
| estocastico_rebote | 879.88 € (-4.80%) | 435 | 34 | 39% | +0.127% | -0.433% | -0.540% | -42.80 € |
| ruptura_estricta | 880.96 € (-4.68%) | 246 | 10 | 32% | -0.161% | -0.768% | -0.883% | -42.97 € |
| macd_sin_salida | 876.71 € (-5.14%) | 478 | 26 | 39% | +0.113% | -0.441% | -0.549% | -47.89 € |
| c_banda_atr_tope | 913.03 € (-1.21%) | 82 | 4 | 38% | +0.248% | -0.574% | -0.689% | -10.83 € |
| ruptura_volumen_tope | 899.20 € (-2.71%) | 134 | 5 | 23% | -0.110% | -0.807% | -0.919% | -24.67 € |
| c_banda_atr_regimen | 902.31 € (-2.37%) | 207 | 21 | 43% | +0.187% | -0.440% | -0.567% | -20.96 € |
| macd_momentum_regimen | 871.21 € (-5.74%) | 491 | 15 | 24% | +0.065% | -0.489% | -0.588% | -53.93 € |
| ruptura_volumen_regimen | 861.15 € (-6.83%) | 372 | 13 | 24% | -0.183% | -0.753% | -0.863% | -62.75 € |
| c_banda_atr_evento | 895.72 € (-3.09%) | 321 | 21 | 42% | +0.207% | -0.376% | -0.492% | -27.62 € |
| macd_momentum_evento | 853.19 € (-7.69%) | 681 | 15 | 23% | +0.064% | -0.475% | -0.571% | -71.94 € |
| ruptura_volumen_evento | 868.69 € (-6.01%) | 399 | 13 | 27% | -0.050% | -0.616% | -0.717% | -55.20 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 11:40 | macd_momentum_evento | HYPE | momentum perdido | +1.18% | +0.68% | +0.15 |
| 2026-10-02 11:40 | macd_momentum_regimen | HYPE | momentum perdido | +1.18% | +0.68% | +0.15 |
| 2026-10-02 11:40 | c_banda_atr_tope | POL | timeout | -0.23% | -0.73% | -0.17 |
| 2026-10-02 11:40 | ruptura_estricta | NIGHT | take-profit | +3.00% | +2.50% | +0.55 |
| 2026-10-02 11:40 | estocastico_rebote | MON | timeout | +1.10% | +0.60% | +0.13 |
| 2026-10-02 11:40 | macd_momentum | HYPE | momentum perdido | +1.18% | +0.68% | +0.14 |
| 2026-10-02 11:35 | ruptura_volumen_evento | WLD | timeout | -0.85% | -1.35% | -0.29 |
| 2026-10-02 11:35 | ruptura_volumen_evento | XLM | timeout | -0.45% | -0.94% | -0.21 |
| 2026-10-02 11:35 | macd_momentum_evento | ONDO | momentum perdido | +0.70% | +0.20% | +0.04 |
| 2026-10-02 11:35 | macd_momentum_evento | ALGO | momentum perdido | -0.48% | -0.98% | -0.21 |
| 2026-10-02 11:35 | macd_momentum_evento | BTC | momentum perdido | -0.05% | -0.55% | -0.12 |
| 2026-10-02 11:35 | c_banda_atr_evento | WLFI | timeout | +0.20% | -0.30% | -0.07 |
| 2026-10-02 11:35 | ruptura_volumen_regimen | WLD | timeout | -0.85% | -1.35% | -0.29 |
| 2026-10-02 11:35 | ruptura_volumen_regimen | XLM | timeout | -0.45% | -0.94% | -0.20 |
| 2026-10-02 11:35 | macd_momentum_regimen | ONDO | momentum perdido | +0.70% | +0.20% | +0.04 |

## Eventos de la última vuelta

- 2026-10-02 11:40 [macd_momentum] CIERRE HYPE momentum perdido bruto +1.18% neto +0.68%
- 2026-10-02 11:40 [macd_momentum_regimen] CIERRE HYPE momentum perdido bruto +1.18% neto +0.68%
- 2026-10-02 11:40 [macd_momentum_evento] CIERRE HYPE momentum perdido bruto +1.18% neto +0.68%
- 2026-10-02 11:35 [estocastico_rebote] ENTRADA XLM @ 0.199555 (22.03 €, apertura)
- 2026-10-02 11:40 [c_banda_atr_tope] CIERRE POL timeout bruto -0.23% neto -0.73%
- 2026-10-02 11:40 [ruptura_estricta] CIERRE NIGHT take-profit bruto +3.00% neto +2.50%
- 2026-10-02 11:40 [estocastico_rebote] CIERRE MON timeout bruto +1.10% neto +0.60%
- 2026-10-02 11:35 [macd_momentum] ENTRADA KAS @ 0.03825 (21.19 €, apertura)
- 2026-10-02 11:35 [macd_momentum_regimen] ENTRADA KAS @ 0.03825 (21.76 €, apertura)
- 2026-10-02 11:35 [macd_momentum_evento] ENTRADA KAS @ 0.03825 (21.31 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
