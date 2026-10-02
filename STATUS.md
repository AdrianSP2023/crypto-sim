# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 00:16 UTC · vueltas 338 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.62 € (-4.29%) | 271 | 21 | 34% | -0.055% | -0.651% | -0.773% | -40.07 € |
| reversion_bb | 918.15 € (-0.66%) | 52 | 17 | 50% | +0.317% | -0.685% | -0.782% | -8.21 € |
| ruptura_volumen | 871.85 € (-5.67%) | 297 | 12 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.39 € (-3.88%) | 189 | 5 | 15% | -0.199% | -0.839% | -0.928% | -35.99 € |
| macd_momentum | 863.63 € (-6.56%) | 490 | 14 | 20% | -0.011% | -0.564% | -0.667% | -61.90 € |
| estocastico_rebote | 872.51 € (-5.60%) | 329 | 14 | 31% | -0.122% | -0.701% | -0.811% | -52.04 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 1 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 871.73 € (-5.68%) | 347 | 14 | 34% | -0.103% | -0.678% | -0.790% | -53.17 € |
| c_banda_atr_tope | 911.49 € (-1.38%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.86 € (-1.99%) | 101 | 5 | 27% | -0.042% | -0.803% | -0.919% | -18.58 € |
| c_banda_atr_regimen | 895.77 € (-3.08%) | 138 | 1 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 885.23 € (-4.22%) | 276 | 0 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 874.81 € (-5.35%) | 230 | 5 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 890.50 € (-3.65%) | 238 | 21 | 34% | -0.020% | -0.631% | -0.747% | -34.18 € |
| macd_momentum_evento | 868.42 € (-6.04%) | 443 | 14 | 19% | -0.015% | -0.575% | -0.674% | -57.13 € |
| ruptura_volumen_evento | 884.25 € (-4.33%) | 247 | 12 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 00:15 | estocastico_rebote | FET | take-profit | +2.08% | +1.58% | +0.34 |
| 2026-10-02 00:10 | c_banda_atr_evento | DASH | timeout | -0.87% | -1.37% | -0.31 |
| 2026-10-02 00:10 | pullback_tendencia | AAVE | rotura de tendencia | +0.18% | -0.32% | -0.07 |
| 2026-10-02 00:10 | c_banda_atr | DASH | timeout | -0.87% | -1.37% | -0.30 |
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

## Eventos de la última vuelta

- 2026-10-02 00:10 [ruptura_volumen] ENTRADA SUI @ 1.0534 (21.79 €, apertura)
- 2026-10-02 00:10 [ruptura_volumen_regimen] ENTRADA SUI @ 1.0534 (21.87 €, apertura)
- 2026-10-02 00:10 [ruptura_volumen_evento] ENTRADA SUI @ 1.0534 (22.10 €, apertura)
- 2026-10-02 00:10 [ruptura_volumen] ENTRADA ARB @ 0.1782 (21.79 €, apertura)
- 2026-10-02 00:10 [ruptura_volumen_regimen] ENTRADA ARB @ 0.1782 (21.87 €, apertura)
- 2026-10-02 00:10 [ruptura_volumen_evento] ENTRADA ARB @ 0.1782 (22.10 €, apertura)
- 2026-10-02 00:10 [ruptura_volumen_regimen] ENTRADA ICP @ 2.925 (21.87 €, apertura)
- 2026-10-02 00:15 [estocastico_rebote] CIERRE FET take-profit bruto +2.08% neto +1.58%
- 2026-10-02 00:10 [c_banda_atr] ENTRADA XDC @ 0.0306 (22.10 €, apertura)
- 2026-10-02 00:10 [c_banda_atr_regimen] ENTRADA XDC @ 0.0306 (22.39 €, apertura)
- 2026-10-02 00:10 [c_banda_atr_evento] ENTRADA XDC @ 0.0306 (22.25 €, apertura)
- 2026-10-02 00:10 [pullback_tendencia] ENTRADA JUP @ 0.29071 (22.21 €, apertura)
- 2026-10-02 00:10 [ruptura_volumen_regimen] ENTRADA JUP @ 0.29071 (21.87 €, apertura)
- 2026-10-02 00:10 [ruptura_volumen] ENTRADA SKY @ 0.07504 (21.79 €, apertura)
- 2026-10-02 00:10 [ruptura_volumen_regimen] ENTRADA SKY @ 0.07504 (21.87 €, apertura)
- 2026-10-02 00:10 [ruptura_volumen_evento] ENTRADA SKY @ 0.07504 (22.10 €, apertura)
- 2026-10-02 00:10 [estocastico_rebote] ENTRADA XMR @ 483.77 (21.80 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
