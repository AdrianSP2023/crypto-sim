# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 06:01 UTC · vueltas 361 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.45 € (-3.66%) | 323 | 13 | 39% | +0.108% | -0.473% | -0.592% | -34.84 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 865.06 € (-6.40%) | 378 | 30 | 27% | -0.115% | -0.684% | -0.794% | -58.10 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.07 € (-3.70%) | 215 | 14 | 20% | -0.069% | -0.691% | -0.778% | -33.79 € |
| macd_momentum | 856.32 € (-7.35%) | 619 | 7 | 23% | +0.048% | -0.494% | -0.595% | -68.19 € |
| estocastico_rebote | 878.15 € (-4.99%) | 376 | 22 | 36% | +0.024% | -0.546% | -0.654% | -46.48 € |
| ruptura_estricta | 884.78 € (-4.27%) | 205 | 29 | 33% | -0.203% | -0.832% | -0.947% | -38.89 € |
| macd_sin_salida | 880.95 € (-4.68%) | 412 | 22 | 40% | +0.105% | -0.459% | -0.569% | -43.08 € |
| c_banda_atr_tope | 913.03 € (-1.21%) | 71 | 5 | 34% | +0.148% | -0.724% | -0.833% | -11.81 € |
| ruptura_volumen_tope | 902.64 € (-2.34%) | 120 | 5 | 26% | -0.063% | -0.783% | -0.897% | -21.49 € |
| c_banda_atr_regimen | 903.09 € (-2.29%) | 176 | 12 | 39% | +0.108% | -0.540% | -0.667% | -21.87 € |
| macd_momentum_regimen | 879.25 € (-4.87%) | 382 | 7 | 22% | +0.044% | -0.524% | -0.627% | -45.25 € |
| ruptura_volumen_regimen | 869.76 € (-5.89%) | 301 | 30 | 24% | -0.201% | -0.788% | -0.903% | -53.40 € |
| c_banda_atr_evento | 896.38 € (-3.01%) | 290 | 13 | 40% | +0.155% | -0.436% | -0.551% | -28.92 € |
| macd_momentum_evento | 861.07 € (-6.84%) | 572 | 7 | 22% | +0.050% | -0.496% | -0.595% | -63.45 € |
| ruptura_volumen_evento | 877.37 € (-5.07%) | 328 | 30 | 28% | -0.037% | -0.618% | -0.721% | -45.77 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 06:00 | ruptura_volumen_evento | HBAR | stop-loss | -1.23% | -1.73% | -0.38 |
| 2026-10-02 06:00 | macd_momentum_evento | ENA | momentum perdido | +0.64% | +0.14% | +0.03 |
| 2026-10-02 06:00 | ruptura_volumen_regimen | HBAR | stop-loss | -1.23% | -1.73% | -0.38 |
| 2026-10-02 06:00 | macd_momentum_regimen | ENA | momentum perdido | +0.64% | +0.14% | +0.03 |
| 2026-10-02 06:00 | ruptura_estricta | FIL | timeout | +0.99% | +0.49% | +0.11 |
| 2026-10-02 06:00 | macd_momentum | ENA | momentum perdido | +0.64% | +0.14% | +0.03 |
| 2026-10-02 06:00 | ruptura_volumen | HBAR | stop-loss | -1.23% | -1.73% | -0.37 |
| 2026-10-02 05:55 | pullback_tendencia | HYPE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 05:50 | c_banda_atr_regimen | TON | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 05:50 | ruptura_estricta | HBAR | timeout | +0.10% | -0.40% | -0.09 |
| 2026-10-02 05:45 | macd_momentum_evento | TRUMP | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 05:45 | macd_momentum_evento | FIL | momentum perdido | +0.11% | -0.39% | -0.08 |
| 2026-10-02 05:45 | c_banda_atr_evento | FET | stop-loss | -1.51% | -2.01% | -0.45 |
| 2026-10-02 05:45 | macd_momentum_regimen | TRUMP | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 05:45 | macd_momentum_regimen | FIL | momentum perdido | +0.11% | -0.39% | -0.09 |

## Eventos de la última vuelta

- 2026-10-02 05:55 [estocastico_rebote] ENTRADA XRP @ 1.34658 (21.94 €, apertura)
- 2026-10-02 05:55 [estocastico_rebote] ENTRADA NEAR @ 4.4194 (21.94 €, apertura)
- 2026-10-02 05:55 [estocastico_rebote] ENTRADA SUI @ 1.0521 (21.94 €, apertura)
- 2026-10-02 06:00 [ruptura_volumen] CIERRE HBAR stop-loss bruto -1.23% neto -1.73%
- 2026-10-02 06:00 [ruptura_volumen_regimen] CIERRE HBAR stop-loss bruto -1.23% neto -1.73%
- 2026-10-02 06:00 [ruptura_volumen_evento] CIERRE HBAR stop-loss bruto -1.23% neto -1.73%
- 2026-10-02 05:55 [macd_momentum] ENTRADA HYPE @ 79.95 (21.40 €, apertura)
- 2026-10-02 05:55 [macd_sin_salida] ENTRADA HYPE @ 79.95 (22.03 €, apertura)
- 2026-10-02 05:55 [macd_momentum_regimen] ENTRADA HYPE @ 79.95 (21.97 €, apertura)
- 2026-10-02 05:55 [macd_momentum_evento] ENTRADA HYPE @ 79.95 (21.52 €, apertura)
- 2026-10-02 05:55 [estocastico_rebote] ENTRADA XLM @ 0.197279 (21.94 €, apertura)
- 2026-10-02 05:55 [estocastico_rebote] ENTRADA UNI @ 8.1201 (21.94 €, apertura)
- 2026-10-02 05:55 [estocastico_rebote] ENTRADA DOGE @ 0.0851147 (21.94 €, apertura)
- 2026-10-02 05:55 [estocastico_rebote] ENTRADA ARB @ 0.182 (21.94 €, apertura)
- 2026-10-02 06:00 [macd_momentum] CIERRE ENA momentum perdido bruto +0.64% neto +0.14%
- 2026-10-02 06:00 [macd_momentum_regimen] CIERRE ENA momentum perdido bruto +0.64% neto +0.14%
- 2026-10-02 06:00 [macd_momentum_evento] CIERRE ENA momentum perdido bruto +0.64% neto +0.14%
- 2026-10-02 05:55 [estocastico_rebote] ENTRADA BCH @ 278.49 (21.94 €, apertura)
- 2026-10-02 05:55 [estocastico_rebote] ENTRADA INJ @ 6.679 (21.94 €, apertura)
- 2026-10-02 06:00 [ruptura_estricta] CIERRE FIL timeout bruto +0.99% neto +0.49%
- 2026-10-02 05:55 [ruptura_volumen] ENTRADA VVV @ 24.975 (21.65 €, apertura)
- 2026-10-02 05:55 [ruptura_volumen_regimen] ENTRADA VVV @ 24.975 (21.77 €, apertura)
- 2026-10-02 05:55 [ruptura_volumen_evento] ENTRADA VVV @ 24.975 (21.96 €, apertura)
- 2026-10-02 05:55 [estocastico_rebote] ENTRADA SHIB @ 5.212e-06 (21.94 €, apertura)
- 2026-10-02 05:55 [estocastico_rebote] ENTRADA SKY @ 0.07528 (21.94 €, apertura)
- 2026-10-02 05:55 [macd_momentum] ENTRADA XMR @ 487.46 (21.40 €, apertura)
- 2026-10-02 05:55 [macd_sin_salida] ENTRADA XMR @ 487.46 (22.03 €, apertura)
- 2026-10-02 05:55 [macd_momentum_regimen] ENTRADA XMR @ 487.46 (21.97 €, apertura)
- 2026-10-02 05:55 [macd_momentum_evento] ENTRADA XMR @ 487.46 (21.52 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
