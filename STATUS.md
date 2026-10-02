# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 10:31 UTC · vueltas 415 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.62 € (-3.85%) | 346 | 23 | 40% | +0.132% | -0.444% | -0.564% | -34.99 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 857.92 € (-7.18%) | 444 | 10 | 26% | -0.107% | -0.666% | -0.773% | -66.07 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.83 € (-3.72%) | 251 | 7 | 21% | -0.016% | -0.621% | -0.709% | -35.41 € |
| macd_momentum | 850.34 € (-8.00%) | 703 | 16 | 23% | +0.059% | -0.478% | -0.579% | -74.61 € |
| estocastico_rebote | 879.60 € (-4.83%) | 426 | 36 | 38% | +0.107% | -0.454% | -0.561% | -43.90 € |
| ruptura_estricta | 881.44 € (-4.63%) | 239 | 15 | 32% | -0.149% | -0.760% | -0.876% | -41.31 € |
| macd_sin_salida | 878.85 € (-4.91%) | 453 | 37 | 40% | +0.107% | -0.451% | -0.561% | -46.41 € |
| c_banda_atr_tope | 913.07 € (-1.21%) | 78 | 4 | 37% | +0.216% | -0.622% | -0.737% | -11.17 € |
| ruptura_volumen_tope | 900.09 € (-2.61%) | 133 | 5 | 23% | -0.101% | -0.800% | -0.912% | -24.29 € |
| c_banda_atr_regimen | 901.32 € (-2.48%) | 199 | 22 | 41% | +0.141% | -0.490% | -0.619% | -22.43 € |
| macd_momentum_regimen | 873.11 € (-5.53%) | 466 | 16 | 24% | +0.062% | -0.494% | -0.597% | -51.84 € |
| ruptura_volumen_regimen | 862.58 € (-6.67%) | 367 | 10 | 24% | -0.175% | -0.747% | -0.859% | -61.41 € |
| c_banda_atr_evento | 894.54 € (-3.21%) | 313 | 23 | 41% | +0.178% | -0.406% | -0.523% | -29.08 € |
| macd_momentum_evento | 855.05 € (-7.49%) | 656 | 16 | 23% | +0.062% | -0.479% | -0.577% | -69.90 € |
| ruptura_volumen_evento | 870.12 € (-5.86%) | 394 | 10 | 27% | -0.041% | -0.608% | -0.710% | -53.85 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 10:30 | macd_momentum_evento | FIL | momentum perdido | -0.65% | -1.15% | -0.25 |
| 2026-10-02 10:30 | macd_momentum_evento | HBAR | momentum perdido | +1.45% | +0.94% | +0.20 |
| 2026-10-02 10:30 | macd_momentum_evento | ADA | momentum perdido | -0.17% | -0.68% | -0.14 |
| 2026-10-02 10:30 | c_banda_atr_evento | MINA | stop-loss | -1.57% | -2.07% | -0.46 |
| 2026-10-02 10:30 | c_banda_atr_evento | POL | timeout | -0.38% | -0.88% | -0.20 |
| 2026-10-02 10:30 | c_banda_atr_evento | ARB | timeout | -0.60% | -1.10% | -0.25 |
| 2026-10-02 10:30 | macd_momentum_regimen | FIL | momentum perdido | -0.65% | -1.15% | -0.25 |
| 2026-10-02 10:30 | macd_momentum_regimen | HBAR | momentum perdido | +1.45% | +0.94% | +0.21 |
| 2026-10-02 10:30 | macd_momentum_regimen | ADA | momentum perdido | -0.17% | -0.68% | -0.15 |
| 2026-10-02 10:30 | c_banda_atr_regimen | MINA | stop-loss | -1.57% | -2.07% | -0.47 |
| 2026-10-02 10:30 | c_banda_atr_regimen | POL | timeout | -0.38% | -0.88% | -0.20 |
| 2026-10-02 10:30 | c_banda_atr_regimen | ARB | timeout | -0.60% | -1.10% | -0.25 |
| 2026-10-02 10:30 | c_banda_atr_tope | ARB | timeout | -0.60% | -1.10% | -0.25 |
| 2026-10-02 10:30 | ruptura_estricta | SPX | stop-loss | -2.19% | -2.69% | -0.59 |
| 2026-10-02 10:30 | estocastico_rebote | LINK | timeout | +0.53% | +0.03% | +0.01 |

## Eventos de la última vuelta

- 2026-10-02 10:30 [estocastico_rebote] CIERRE LINK timeout bruto +0.53% neto +0.03%
- 2026-10-02 10:30 [macd_momentum] CIERRE ADA momentum perdido bruto -0.17% neto -0.67%
- 2026-10-02 10:30 [macd_momentum_regimen] CIERRE ADA momentum perdido bruto -0.17% neto -0.67%
- 2026-10-02 10:30 [macd_momentum_evento] CIERRE ADA momentum perdido bruto -0.17% neto -0.67%
- 2026-10-02 10:30 [macd_momentum] CIERRE HBAR momentum perdido bruto +1.44% neto +0.94%
- 2026-10-02 10:30 [macd_momentum_regimen] CIERRE HBAR momentum perdido bruto +1.44% neto +0.94%
- 2026-10-02 10:30 [macd_momentum_evento] CIERRE HBAR momentum perdido bruto +1.44% neto +0.94%
- 2026-10-02 10:30 [c_banda_atr] CIERRE ARB timeout bruto -0.60% neto -1.10%
- 2026-10-02 10:30 [c_banda_atr_tope] CIERRE ARB timeout bruto -0.60% neto -1.10%
- 2026-10-02 10:30 [c_banda_atr_regimen] CIERRE ARB timeout bruto -0.60% neto -1.10%
- 2026-10-02 10:30 [c_banda_atr_evento] CIERRE ARB timeout bruto -0.60% neto -1.10%
- 2026-10-02 10:25 [ruptura_volumen] ENTRADA TRX @ 0.29758 (21.45 €, apertura)
- 2026-10-02 10:25 [macd_momentum] ENTRADA TRX @ 0.29758 (21.25 €, apertura)
- 2026-10-02 10:25 [ruptura_estricta] ENTRADA TRX @ 0.29758 (22.09 €, apertura)
- 2026-10-02 10:25 [macd_sin_salida] ENTRADA TRX @ 0.29758 (21.95 €, apertura)
- 2026-10-02 10:25 [macd_momentum_regimen] ENTRADA TRX @ 0.29758 (21.82 €, apertura)
- 2026-10-02 10:25 [ruptura_volumen_regimen] ENTRADA TRX @ 0.29758 (21.57 €, apertura)
- 2026-10-02 10:25 [macd_momentum_evento] ENTRADA TRX @ 0.29758 (21.36 €, apertura)
- 2026-10-02 10:25 [ruptura_volumen_evento] ENTRADA TRX @ 0.29758 (21.76 €, apertura)
- 2026-10-02 10:30 [c_banda_atr] CIERRE POL timeout bruto -0.38% neto -0.88%
- 2026-10-02 10:30 [c_banda_atr_regimen] CIERRE POL timeout bruto -0.38% neto -0.88%
- 2026-10-02 10:30 [c_banda_atr_evento] CIERRE POL timeout bruto -0.38% neto -0.88%
- 2026-10-02 10:30 [c_banda_atr] CIERRE MINA stop-loss bruto -1.57% neto -2.07%
- 2026-10-02 10:30 [pullback_tendencia] CIERRE MINA rotura de tendencia bruto -0.75% neto -1.25%
- 2026-10-02 10:25 [estocastico_rebote] ENTRADA MINA @ 0.1446 (22.01 €, apertura)
- 2026-10-02 10:30 [c_banda_atr_regimen] CIERRE MINA stop-loss bruto -1.57% neto -2.07%
- 2026-10-02 10:30 [c_banda_atr_evento] CIERRE MINA stop-loss bruto -1.57% neto -2.07%
- 2026-10-02 10:30 [macd_momentum] CIERRE FIL momentum perdido bruto -0.65% neto -1.15%
- 2026-10-02 10:30 [macd_momentum_regimen] CIERRE FIL momentum perdido bruto -0.65% neto -1.15%
- 2026-10-02 10:30 [macd_momentum_evento] CIERRE FIL momentum perdido bruto -0.65% neto -1.15%
- 2026-10-02 10:30 [ruptura_estricta] CIERRE SPX stop-loss bruto -2.19% neto -2.69%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
