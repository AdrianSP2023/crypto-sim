# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 10:16 UTC · vueltas 412 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.58 € (-3.75%) | 342 | 27 | 40% | +0.139% | -0.438% | -0.557% | -34.14 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 859.09 € (-7.05%) | 436 | 16 | 27% | -0.100% | -0.660% | -0.768% | -64.34 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.86 € (-3.72%) | 249 | 8 | 21% | -0.012% | -0.618% | -0.705% | -34.96 € |
| macd_momentum | 851.77 € (-7.84%) | 695 | 21 | 24% | +0.065% | -0.473% | -0.573% | -73.05 € |
| estocastico_rebote | 879.91 € (-4.80%) | 424 | 36 | 38% | +0.102% | -0.459% | -0.567% | -44.19 € |
| ruptura_estricta | 881.81 € (-4.59%) | 238 | 14 | 32% | -0.140% | -0.751% | -0.868% | -40.72 € |
| macd_sin_salida | 879.51 € (-4.84%) | 452 | 37 | 40% | +0.110% | -0.447% | -0.557% | -45.98 € |
| c_banda_atr_tope | 913.24 € (-1.19%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 899.96 € (-2.63%) | 133 | 4 | 23% | -0.101% | -0.800% | -0.912% | -24.29 € |
| c_banda_atr_regimen | 902.16 € (-2.39%) | 195 | 26 | 41% | +0.153% | -0.480% | -0.608% | -21.57 € |
| macd_momentum_regimen | 874.58 € (-5.37%) | 458 | 21 | 24% | +0.070% | -0.487% | -0.589% | -50.24 € |
| ruptura_volumen_regimen | 863.75 € (-6.54%) | 359 | 16 | 24% | -0.168% | -0.741% | -0.854% | -59.68 € |
| c_banda_atr_evento | 895.50 € (-3.11%) | 309 | 27 | 41% | +0.186% | -0.399% | -0.514% | -28.22 € |
| macd_momentum_evento | 856.49 € (-7.33%) | 648 | 21 | 23% | +0.067% | -0.473% | -0.571% | -68.33 € |
| ruptura_volumen_evento | 871.31 € (-5.73%) | 386 | 16 | 27% | -0.032% | -0.600% | -0.703% | -52.11 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 10:15 | macd_momentum_evento | SEI | momentum perdido | +0.87% | +0.37% | +0.08 |
| 2026-10-02 10:15 | macd_momentum_regimen | SEI | momentum perdido | +0.87% | +0.37% | +0.08 |
| 2026-10-02 10:15 | macd_sin_salida | INJ | timeout | +0.57% | +0.07% | +0.01 |
| 2026-10-02 10:15 | estocastico_rebote | SEI | timeout | +0.93% | +0.43% | +0.09 |
| 2026-10-02 10:15 | macd_momentum | SEI | momentum perdido | +0.87% | +0.37% | +0.08 |
| 2026-10-02 10:15 | pullback_tendencia | SOL | rotura de tendencia | -0.15% | -0.65% | -0.14 |
| 2026-10-02 10:10 | macd_momentum_evento | ICP | momentum perdido | +0.07% | -0.43% | -0.09 |
| 2026-10-02 10:10 | macd_momentum_evento | XLM | momentum perdido | +0.17% | -0.33% | -0.07 |
| 2026-10-02 10:10 | macd_momentum_evento | AAVE | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 10:10 | c_banda_atr_evento | SHIB | timeout | +1.11% | +0.61% | +0.14 |
| 2026-10-02 10:10 | macd_momentum_regimen | ICP | momentum perdido | +0.07% | -0.43% | -0.09 |
| 2026-10-02 10:10 | macd_momentum_regimen | XLM | momentum perdido | +0.17% | -0.33% | -0.07 |
| 2026-10-02 10:10 | macd_momentum_regimen | AAVE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 10:10 | c_banda_atr_regimen | SHIB | timeout | +1.11% | +0.61% | +0.14 |
| 2026-10-02 10:10 | macd_sin_salida | KSM | timeout | -0.65% | -1.15% | -0.25 |

## Eventos de la última vuelta

- 2026-10-02 10:15 [pullback_tendencia] CIERRE SOL rotura de tendencia bruto -0.15% neto -0.65%
- 2026-10-02 10:10 [macd_momentum] ENTRADA CRV @ 0.34053 (21.28 €, apertura)
- 2026-10-02 10:10 [macd_sin_salida] ENTRADA CRV @ 0.34053 (21.96 €, apertura)
- 2026-10-02 10:10 [macd_momentum_regimen] ENTRADA CRV @ 0.34053 (21.85 €, apertura)
- 2026-10-02 10:10 [macd_momentum_evento] ENTRADA CRV @ 0.34053 (21.40 €, apertura)
- 2026-10-02 10:10 [macd_momentum] ENTRADA MON @ 0.03 (21.28 €, apertura)
- 2026-10-02 10:10 [macd_sin_salida] ENTRADA MON @ 0.03 (21.96 €, apertura)
- 2026-10-02 10:10 [macd_momentum_regimen] ENTRADA MON @ 0.03 (21.85 €, apertura)
- 2026-10-02 10:10 [macd_momentum_evento] ENTRADA MON @ 0.03 (21.40 €, apertura)
- 2026-10-02 10:15 [macd_sin_salida] CIERRE INJ timeout bruto +0.57% neto +0.07%
- 2026-10-02 10:10 [c_banda_atr] ENTRADA FIL @ 0.923 (22.25 €, apertura)
- 2026-10-02 10:10 [macd_momentum] ENTRADA FIL @ 0.923 (21.28 €, apertura)
- 2026-10-02 10:10 [macd_sin_salida] ENTRADA FIL @ 0.923 (21.96 €, apertura)
- 2026-10-02 10:10 [c_banda_atr_regimen] ENTRADA FIL @ 0.923 (22.57 €, apertura)
- 2026-10-02 10:10 [macd_momentum_regimen] ENTRADA FIL @ 0.923 (21.85 €, apertura)
- 2026-10-02 10:10 [c_banda_atr_evento] ENTRADA FIL @ 0.923 (22.40 €, apertura)
- 2026-10-02 10:10 [macd_momentum_evento] ENTRADA FIL @ 0.923 (21.40 €, apertura)
- 2026-10-02 10:10 [ruptura_estricta] ENTRADA SKY @ 0.0802 (22.09 €, apertura)
- 2026-10-02 10:15 [macd_momentum] CIERRE SEI momentum perdido bruto +0.87% neto +0.37%
- 2026-10-02 10:15 [estocastico_rebote] CIERRE SEI timeout bruto +0.93% neto +0.43%
- 2026-10-02 10:15 [macd_momentum_regimen] CIERRE SEI momentum perdido bruto +0.87% neto +0.37%
- 2026-10-02 10:15 [macd_momentum_evento] CIERRE SEI momentum perdido bruto +0.87% neto +0.37%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
