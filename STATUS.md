# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 04:21 UTC · vueltas 387 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.33 € (-4.21%) | 298 | 26 | 35% | -0.000% | -0.588% | -0.709% | -39.77 € |
| reversion_bb | 919.46 € (-0.52%) | 70 | 3 | 60% | +0.530% | -0.343% | -0.445% | -5.55 € |
| ruptura_volumen | 864.81 € (-6.43%) | 354 | 13 | 24% | -0.172% | -0.746% | -0.854% | -59.25 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.32 € (-3.78%) | 201 | 13 | 16% | -0.161% | -0.792% | -0.880% | -36.13 € |
| macd_momentum | 857.86 € (-7.18%) | 569 | 13 | 21% | +0.013% | -0.533% | -0.635% | -67.65 € |
| estocastico_rebote | 873.73 € (-5.46%) | 352 | 25 | 32% | -0.083% | -0.657% | -0.765% | -52.14 € |
| ruptura_estricta | 882.49 € (-4.52%) | 181 | 20 | 27% | -0.381% | -1.027% | -1.143% | -42.25 € |
| macd_sin_salida | 875.95 € (-5.23%) | 374 | 34 | 35% | -0.043% | -0.613% | -0.723% | -51.85 € |
| c_banda_atr_tope | 912.31 € (-1.29%) | 68 | 5 | 32% | +0.108% | -0.780% | -0.894% | -12.20 € |
| ruptura_volumen_tope | 902.97 € (-2.30%) | 115 | 4 | 25% | -0.076% | -0.806% | -0.921% | -21.20 € |
| c_banda_atr_regimen | 897.83 € (-2.86%) | 146 | 30 | 30% | -0.176% | -0.855% | -0.988% | -28.54 € |
| macd_momentum_regimen | 880.83 € (-4.70%) | 332 | 13 | 19% | -0.017% | -0.596% | -0.699% | -44.70 € |
| ruptura_volumen_regimen | 869.51 € (-5.92%) | 277 | 13 | 21% | -0.281% | -0.875% | -0.988% | -54.56 € |
| c_banda_atr_evento | 891.22 € (-3.57%) | 265 | 26 | 36% | +0.038% | -0.561% | -0.678% | -33.88 € |
| macd_momentum_evento | 862.61 € (-6.67%) | 522 | 13 | 20% | +0.011% | -0.539% | -0.637% | -62.91 € |
| ruptura_volumen_evento | 877.11 € (-5.10%) | 304 | 13 | 25% | -0.097% | -0.684% | -0.785% | -46.94 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 04:20 | ruptura_volumen_evento | ALGO | timeout | +0.46% | -0.04% | -0.01 |
| 2026-10-02 04:20 | ruptura_volumen_evento | FET | timeout | +0.47% | -0.03% | -0.01 |
| 2026-10-02 04:20 | macd_momentum_evento | TON | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 04:20 | c_banda_atr_evento | XLM | timeout | +0.43% | -0.07% | -0.02 |
| 2026-10-02 04:20 | ruptura_volumen_regimen | ALGO | timeout | +0.46% | -0.04% | -0.01 |
| 2026-10-02 04:20 | ruptura_volumen_regimen | FET | timeout | +0.47% | -0.03% | -0.01 |
| 2026-10-02 04:20 | macd_momentum_regimen | TON | momentum perdido | -0.07% | -0.57% | -0.13 |
| 2026-10-02 04:20 | c_banda_atr_regimen | VVV | take-profit | +2.02% | +1.52% | +0.34 |
| 2026-10-02 04:20 | c_banda_atr_regimen | XLM | timeout | +0.43% | -0.07% | -0.02 |
| 2026-10-02 04:20 | macd_momentum | TON | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 04:20 | ruptura_volumen | ALGO | timeout | +0.46% | -0.04% | -0.01 |
| 2026-10-02 04:20 | ruptura_volumen | FET | timeout | +0.47% | -0.03% | -0.01 |
| 2026-10-02 04:20 | c_banda_atr | XLM | timeout | +0.43% | -0.07% | -0.02 |
| 2026-10-02 04:15 | ruptura_volumen_evento | AVAX | timeout | -0.40% | -0.90% | -0.20 |
| 2026-10-02 04:15 | macd_momentum_evento | KSM | momentum perdido | +1.10% | +0.60% | +0.13 |

## Eventos de la última vuelta

- 2026-10-02 04:20 [c_banda_atr] CIERRE XLM timeout bruto +0.43% neto -0.07%
- 2026-10-02 04:20 [c_banda_atr_regimen] CIERRE XLM timeout bruto +0.43% neto -0.07%
- 2026-10-02 04:20 [c_banda_atr_evento] CIERRE XLM timeout bruto +0.43% neto -0.07%
- 2026-10-02 04:20 [ruptura_volumen] CIERRE FET timeout bruto +0.48% neto -0.02%
- 2026-10-02 04:15 [pullback_tendencia] ENTRADA FET @ 0.2109 (22.20 €, apertura)
- 2026-10-02 04:20 [ruptura_volumen_regimen] CIERRE FET timeout bruto +0.48% neto -0.02%
- 2026-10-02 04:20 [ruptura_volumen_evento] CIERRE FET timeout bruto +0.48% neto -0.02%
- 2026-10-02 04:20 [ruptura_volumen] CIERRE ALGO timeout bruto +0.46% neto -0.04%
- 2026-10-02 04:20 [ruptura_volumen_regimen] CIERRE ALGO timeout bruto +0.46% neto -0.04%
- 2026-10-02 04:20 [ruptura_volumen_evento] CIERRE ALGO timeout bruto +0.46% neto -0.04%
- 2026-10-02 04:20 [c_banda_atr_regimen] CIERRE VVV take-profit bruto +2.02% neto +1.52%
- 2026-10-02 04:20 [macd_momentum] CIERRE TON momentum perdido bruto -0.07% neto -0.57%
- 2026-10-02 04:20 [macd_momentum_regimen] CIERRE TON momentum perdido bruto -0.07% neto -0.57%
- 2026-10-02 04:20 [macd_momentum_evento] CIERRE TON momentum perdido bruto -0.07% neto -0.57%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
