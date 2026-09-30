# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 09:46 UTC · vueltas 203 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 896.38 € (-3.01%) | 161 | 24 | 29% | -0.161% | -0.823% | -0.951% | -30.28 € |
| reversion_bb | 915.12 € (-0.99%) | 43 | 3 | 42% | +0.124% | -0.962% | -1.072% | -9.52 € |
| ruptura_volumen | 887.43 € (-3.98%) | 190 | 30 | 20% | -0.247% | -0.884% | -1.015% | -38.15 € |
| rebote_extremo | 923.34 € (-0.10%) | 10 | 0 | 60% | +0.710% | -0.389% | -0.540% | -0.90 € |
| pullback_tendencia | 901.79 € (-2.43%) | 123 | 5 | 24% | -0.094% | -0.806% | -0.933% | -22.68 € |
| macd_momentum | 876.81 € (-5.13%) | 347 | 25 | 17% | -0.073% | -0.648% | -0.760% | -50.70 € |
| estocastico_rebote | 888.47 € (-3.87%) | 231 | 7 | 36% | -0.078% | -0.691% | -0.823% | -36.37 € |
| ruptura_estricta | 902.07 € (-2.40%) | 81 | 17 | 22% | -0.396% | -1.218% | -1.368% | -22.60 € |
| macd_sin_salida | 890.44 € (-3.66%) | 216 | 30 | 29% | -0.131% | -0.752% | -0.872% | -36.89 € |
| c_banda_atr_tope | 910.36 € (-1.50%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.72 € (-1.68%) | 69 | 5 | 20% | -0.102% | -0.985% | -1.108% | -15.59 € |
| c_banda_atr_regimen | 900.82 € (-2.53%) | 78 | 6 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.12 € (-4.23%) | 205 | 10 | 14% | -0.224% | -0.852% | -0.966% | -39.61 € |
| ruptura_volumen_regimen | 895.19 € (-3.14%) | 129 | 27 | 17% | -0.297% | -0.999% | -1.130% | -29.37 € |
| c_banda_atr_evento | 899.44 € (-2.68%) | 129 | 24 | 26% | -0.218% | -0.922% | -1.051% | -27.23 € |
| macd_momentum_evento | 889.14 € (-3.80%) | 227 | 25 | 15% | -0.129% | -0.746% | -0.855% | -38.41 € |
| ruptura_volumen_evento | 892.89 € (-3.39%) | 131 | 30 | 15% | -0.394% | -1.095% | -1.228% | -32.69 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 09:45 | macd_momentum_evento | PUMP | momentum perdido | +0.28% | -0.22% | -0.05 |
| 2026-09-30 09:45 | macd_sin_salida | HBAR | timeout | +1.17% | +0.67% | +0.15 |
| 2026-09-30 09:45 | estocastico_rebote | SHIB | timeout | +1.22% | +0.72% | +0.16 |
| 2026-09-30 09:45 | macd_momentum | PUMP | momentum perdido | +0.28% | -0.22% | -0.05 |
| 2026-09-30 09:40 | ruptura_volumen_evento | XLM | timeout | +1.45% | +0.95% | +0.21 |
| 2026-09-30 09:40 | ruptura_volumen_evento | NEAR | timeout | +1.56% | +1.06% | +0.24 |
| 2026-09-30 09:40 | macd_momentum_evento | XPL | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 09:40 | c_banda_atr_evento | XPL | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 09:40 | ruptura_volumen_tope | NEAR | timeout | +1.56% | +1.06% | +0.24 |
| 2026-09-30 09:40 | macd_sin_salida | XPL | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 09:40 | estocastico_rebote | QNT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-09-30 09:40 | estocastico_rebote | XRP | timeout | +0.98% | +0.48% | +0.11 |
| 2026-09-30 09:40 | macd_momentum | XPL | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 09:40 | ruptura_volumen | XLM | timeout | +1.45% | +0.95% | +0.21 |
| 2026-09-30 09:40 | ruptura_volumen | NEAR | timeout | +1.56% | +1.06% | +0.23 |

## Eventos de la última vuelta

- 2026-09-30 09:45 [macd_sin_salida] CIERRE HBAR timeout bruto +1.17% neto +0.67%
- 2026-09-30 09:45 [macd_momentum] CIERRE PUMP momentum perdido bruto +0.28% neto -0.22%
- 2026-09-30 09:45 [macd_momentum_evento] CIERRE PUMP momentum perdido bruto +0.28% neto -0.22%
- 2026-09-30 09:45 [estocastico_rebote] CIERRE SHIB timeout bruto +1.22% neto +0.72%
- 2026-09-30 09:40 [ruptura_volumen] ENTRADA TON @ 1.316 (22.15 €, apertura)
- 2026-09-30 09:40 [ruptura_volumen_regimen] ENTRADA TON @ 1.316 (22.37 €, apertura)
- 2026-09-30 09:40 [ruptura_volumen_evento] ENTRADA TON @ 1.316 (22.29 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
