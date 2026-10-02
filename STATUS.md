# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 00:06 UTC · vueltas 336 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 883.92 € (-4.36%) | 270 | 21 | 34% | -0.052% | -0.649% | -0.770% | -39.77 € |
| reversion_bb | 917.53 € (-0.73%) | 52 | 16 | 50% | +0.317% | -0.685% | -0.782% | -8.21 € |
| ruptura_volumen | 871.59 € (-5.70%) | 297 | 7 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.27 € (-3.89%) | 188 | 4 | 15% | -0.201% | -0.842% | -0.931% | -35.92 € |
| macd_momentum | 862.95 € (-6.63%) | 490 | 13 | 20% | -0.011% | -0.564% | -0.667% | -61.90 € |
| estocastico_rebote | 871.96 € (-5.66%) | 328 | 14 | 30% | -0.129% | -0.708% | -0.818% | -52.39 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 1 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 871.06 € (-5.75%) | 347 | 12 | 34% | -0.103% | -0.678% | -0.790% | -53.17 € |
| c_banda_atr_tope | 911.12 € (-1.42%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.70 € (-2.01%) | 101 | 5 | 27% | -0.042% | -0.803% | -0.919% | -18.58 € |
| c_banda_atr_regimen | 895.77 € (-3.08%) | 138 | 0 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 885.23 € (-4.22%) | 276 | 0 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 874.82 € (-5.35%) | 230 | 0 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 889.80 € (-3.73%) | 237 | 21 | 34% | -0.016% | -0.627% | -0.744% | -33.87 € |
| macd_momentum_evento | 867.73 € (-6.11%) | 443 | 13 | 19% | -0.015% | -0.575% | -0.674% | -57.13 € |
| ruptura_volumen_evento | 883.99 € (-4.35%) | 247 | 7 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 00:05 | macd_momentum_evento | PUMP | momentum perdido | -0.10% | -0.60% | -0.13 |
| 2026-10-02 00:05 | c_banda_atr_evento | APT | timeout | -0.86% | -1.36% | -0.30 |
| 2026-10-02 00:05 | c_banda_atr_evento | FIL | timeout | -0.22% | -0.72% | -0.16 |
| 2026-10-02 00:05 | c_banda_atr_regimen | APT | timeout | -0.86% | -1.36% | -0.30 |
| 2026-10-02 00:05 | c_banda_atr_regimen | FIL | timeout | -0.22% | -0.72% | -0.16 |
| 2026-10-02 00:05 | macd_momentum | PUMP | momentum perdido | -0.10% | -0.60% | -0.13 |
| 2026-10-02 00:05 | pullback_tendencia | BCH | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 00:05 | c_banda_atr | APT | timeout | -0.86% | -1.36% | -0.30 |
| 2026-10-02 00:05 | c_banda_atr | FIL | timeout | -0.22% | -0.72% | -0.16 |
| 2026-10-02 00:00 | c_banda_atr_evento | XMR | timeout | -0.25% | -0.75% | -0.17 |
| 2026-10-02 00:00 | c_banda_atr_regimen | XMR | timeout | -0.25% | -0.75% | -0.17 |
| 2026-10-02 00:00 | estocastico_rebote | SKY | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-02 00:00 | c_banda_atr | XMR | timeout | -0.25% | -0.75% | -0.17 |
| 2026-10-01 23:55 | macd_momentum_evento | AAVE | momentum perdido | +0.45% | -0.05% | -0.01 |
| 2026-10-01 23:55 | c_banda_atr_evento | TRUMP | timeout | -0.16% | -0.66% | -0.15 |

## Eventos de la última vuelta

- 2026-10-02 00:05 [macd_momentum] CIERRE PUMP momentum perdido bruto -0.10% neto -0.60%
- 2026-10-02 00:05 [macd_momentum_evento] CIERRE PUMP momentum perdido bruto -0.10% neto -0.60%
- 2026-10-02 00:05 [pullback_tendencia] CIERRE BCH stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 00:00 [ruptura_volumen] ENTRADA JUP @ 0.29002 (21.79 €, apertura)
- 2026-10-02 00:00 [ruptura_volumen_evento] ENTRADA JUP @ 0.29002 (22.10 €, apertura)
- 2026-10-02 00:00 [estocastico_rebote] ENTRADA MINA @ 0.1349 (21.80 €, apertura)
- 2026-10-02 00:05 [c_banda_atr] CIERRE FIL timeout bruto -0.22% neto -0.72%
- 2026-10-02 00:05 [c_banda_atr_regimen] CIERRE FIL timeout bruto -0.22% neto -0.72%
- 2026-10-02 00:05 [c_banda_atr_evento] CIERRE FIL timeout bruto -0.22% neto -0.72%
- 2026-10-02 00:00 [macd_momentum] ENTRADA BNB @ 685.93 (21.56 €, apertura)
- 2026-10-02 00:00 [macd_sin_salida] ENTRADA BNB @ 685.93 (21.78 €, apertura)
- 2026-10-02 00:00 [macd_momentum_evento] ENTRADA BNB @ 685.93 (21.68 €, apertura)
- 2026-10-02 00:05 [c_banda_atr] CIERRE APT timeout bruto -0.86% neto -1.36%
- 2026-10-02 00:05 [c_banda_atr_regimen] CIERRE APT timeout bruto -0.86% neto -1.36%
- 2026-10-02 00:05 [c_banda_atr_evento] CIERRE APT timeout bruto -0.86% neto -1.36%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
