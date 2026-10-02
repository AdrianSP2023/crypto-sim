# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 06:06 UTC · vueltas 362 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.78 € (-3.62%) | 323 | 14 | 39% | +0.108% | -0.473% | -0.592% | -34.84 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 865.82 € (-6.32%) | 379 | 29 | 27% | -0.112% | -0.681% | -0.790% | -57.95 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.61 € (-3.64%) | 215 | 14 | 20% | -0.069% | -0.691% | -0.778% | -33.79 € |
| macd_momentum | 856.08 € (-7.37%) | 621 | 5 | 23% | +0.048% | -0.494% | -0.595% | -68.39 € |
| estocastico_rebote | 879.12 € (-4.88%) | 376 | 29 | 36% | +0.024% | -0.546% | -0.654% | -46.48 € |
| ruptura_estricta | 885.63 € (-4.18%) | 207 | 27 | 33% | -0.193% | -0.821% | -0.935% | -38.75 € |
| macd_sin_salida | 881.20 € (-4.66%) | 412 | 22 | 40% | +0.105% | -0.459% | -0.569% | -43.08 € |
| c_banda_atr_tope | 912.99 € (-1.22%) | 71 | 5 | 34% | +0.148% | -0.724% | -0.833% | -11.81 € |
| ruptura_volumen_tope | 902.64 € (-2.34%) | 120 | 5 | 26% | -0.063% | -0.783% | -0.897% | -21.49 € |
| c_banda_atr_regimen | 903.28 € (-2.27%) | 176 | 13 | 39% | +0.108% | -0.540% | -0.667% | -21.87 € |
| macd_momentum_regimen | 879.00 € (-4.89%) | 384 | 5 | 22% | +0.044% | -0.524% | -0.627% | -45.46 € |
| ruptura_volumen_regimen | 870.52 € (-5.81%) | 302 | 29 | 24% | -0.196% | -0.783% | -0.898% | -53.25 € |
| c_banda_atr_evento | 896.70 € (-2.98%) | 290 | 14 | 40% | +0.155% | -0.436% | -0.551% | -28.92 € |
| macd_momentum_evento | 860.83 € (-6.86%) | 574 | 5 | 21% | +0.050% | -0.496% | -0.595% | -63.65 € |
| ruptura_volumen_evento | 878.14 € (-4.99%) | 329 | 29 | 28% | -0.034% | -0.614% | -0.717% | -45.62 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 06:05 | ruptura_volumen_evento | DOGE | timeout | +1.20% | +0.70% | +0.15 |
| 2026-10-02 06:05 | macd_momentum_evento | DASH | momentum perdido | +0.28% | -0.22% | -0.05 |
| 2026-10-02 06:05 | macd_momentum_evento | ICP | momentum perdido | -0.20% | -0.70% | -0.15 |
| 2026-10-02 06:05 | ruptura_volumen_regimen | DOGE | timeout | +1.20% | +0.70% | +0.15 |
| 2026-10-02 06:05 | macd_momentum_regimen | DASH | momentum perdido | +0.28% | -0.22% | -0.05 |
| 2026-10-02 06:05 | macd_momentum_regimen | ICP | momentum perdido | -0.20% | -0.70% | -0.15 |
| 2026-10-02 06:05 | ruptura_estricta | XRP | timeout | +1.01% | +0.51% | +0.11 |
| 2026-10-02 06:05 | ruptura_estricta | BTC | timeout | +0.66% | +0.16% | +0.04 |
| 2026-10-02 06:05 | macd_momentum | DASH | momentum perdido | +0.28% | -0.22% | -0.05 |
| 2026-10-02 06:05 | macd_momentum | ICP | momentum perdido | -0.20% | -0.70% | -0.15 |
| 2026-10-02 06:05 | ruptura_volumen | DOGE | timeout | +1.20% | +0.70% | +0.15 |
| 2026-10-02 06:00 | ruptura_volumen_evento | HBAR | stop-loss | -1.23% | -1.73% | -0.38 |
| 2026-10-02 06:00 | macd_momentum_evento | ENA | momentum perdido | +0.64% | +0.14% | +0.03 |
| 2026-10-02 06:00 | ruptura_volumen_regimen | HBAR | stop-loss | -1.23% | -1.73% | -0.38 |
| 2026-10-02 06:00 | macd_momentum_regimen | ENA | momentum perdido | +0.64% | +0.14% | +0.03 |

## Eventos de la última vuelta

- 2026-10-02 06:05 [ruptura_estricta] CIERRE BTC timeout bruto +0.66% neto +0.16%
- 2026-10-02 06:05 [ruptura_estricta] CIERRE XRP timeout bruto +1.01% neto +0.51%
- 2026-10-02 06:00 [estocastico_rebote] ENTRADA AAVE @ 161.82 (21.94 €, apertura)
- 2026-10-02 06:00 [estocastico_rebote] ENTRADA TAO @ 274.9 (21.94 €, apertura)
- 2026-10-02 06:05 [ruptura_volumen] CIERRE DOGE timeout bruto +1.20% neto +0.70%
- 2026-10-02 06:05 [ruptura_volumen_regimen] CIERRE DOGE timeout bruto +1.20% neto +0.70%
- 2026-10-02 06:05 [ruptura_volumen_evento] CIERRE DOGE timeout bruto +1.20% neto +0.70%
- 2026-10-02 06:00 [estocastico_rebote] ENTRADA DOT @ 1.0812 (21.94 €, apertura)
- 2026-10-02 06:05 [macd_momentum] CIERRE ICP momentum perdido bruto -0.20% neto -0.70%
- 2026-10-02 06:05 [macd_momentum_regimen] CIERRE ICP momentum perdido bruto -0.20% neto -0.70%
- 2026-10-02 06:05 [macd_momentum_evento] CIERRE ICP momentum perdido bruto -0.20% neto -0.70%
- 2026-10-02 06:00 [estocastico_rebote] ENTRADA ALGO @ 0.11246 (21.94 €, apertura)
- 2026-10-02 06:00 [estocastico_rebote] ENTRADA PEPE @ 4.055e-06 (21.94 €, apertura)
- 2026-10-02 06:00 [estocastico_rebote] ENTRADA RENDER @ 1.751 (21.94 €, apertura)
- 2026-10-02 06:05 [macd_momentum] CIERRE DASH momentum perdido bruto +0.28% neto -0.22%
- 2026-10-02 06:05 [macd_momentum_regimen] CIERRE DASH momentum perdido bruto +0.28% neto -0.22%
- 2026-10-02 06:05 [macd_momentum_evento] CIERRE DASH momentum perdido bruto +0.28% neto -0.22%
- 2026-10-02 06:00 [estocastico_rebote] ENTRADA KSM @ 4.58 (21.94 €, apertura)
- 2026-10-02 06:00 [c_banda_atr] ENTRADA SKY @ 0.07528 (22.23 €, apertura)
- 2026-10-02 06:00 [c_banda_atr_regimen] ENTRADA SKY @ 0.07528 (22.56 €, apertura)
- 2026-10-02 06:00 [c_banda_atr_evento] ENTRADA SKY @ 0.07528 (22.38 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
