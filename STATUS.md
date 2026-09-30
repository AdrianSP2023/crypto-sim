# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 05:31 UTC · vueltas 213 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.94 € (-2.85%) | 122 | 21 | 28% | -0.242% | -0.956% | -1.090% | -26.72 € |
| reversion_bb | 918.03 € (-0.67%) | 32 | 7 | 50% | +0.236% | -0.864% | -0.973% | -6.38 € |
| ruptura_volumen | 891.87 € (-3.50%) | 155 | 13 | 19% | -0.261% | -0.929% | -1.055% | -32.79 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.87 € (-2.10%) | 112 | 2 | 26% | -0.024% | -0.757% | -0.883% | -19.44 € |
| macd_momentum | 879.42 € (-4.85%) | 291 | 9 | 16% | -0.107% | -0.697% | -0.809% | -45.86 € |
| estocastico_rebote | 890.90 € (-3.61%) | 196 | 16 | 34% | -0.118% | -0.751% | -0.883% | -33.59 € |
| ruptura_estricta | 904.42 € (-2.14%) | 70 | 5 | 23% | -0.383% | -1.256% | -1.396% | -20.15 € |
| macd_sin_salida | 893.48 € (-3.33%) | 174 | 21 | 28% | -0.156% | -0.806% | -0.932% | -31.94 € |
| c_banda_atr_tope | 911.06 € (-1.43%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 909.92 € (-1.55%) | 56 | 5 | 16% | -0.186% | -1.158% | -1.275% | -14.88 € |
| c_banda_atr_regimen | 900.78 € (-2.54%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 898.84 € (-2.75%) | 116 | 0 | 18% | -0.234% | -0.959% | -1.087% | -25.40 € |
| c_banda_atr_evento | 901.00 € (-2.51%) | 90 | 21 | 24% | -0.353% | -1.147% | -1.282% | -23.66 € |
| macd_momentum_evento | 891.79 € (-3.51%) | 171 | 9 | 13% | -0.206% | -0.861% | -0.970% | -33.51 € |
| ruptura_volumen_evento | 897.36 € (-2.91%) | 96 | 13 | 11% | -0.470% | -1.245% | -1.370% | -27.29 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 05:30 | macd_momentum_evento | KAS | momentum perdido | +0.81% | +0.31% | +0.07 |
| 2026-09-30 05:30 | macd_momentum_evento | SHIB | momentum perdido | -0.02% | -0.52% | -0.12 |
| 2026-09-30 05:30 | ruptura_estricta | SPX | stop-loss | -2.04% | -2.54% | -0.57 |
| 2026-09-30 05:30 | estocastico_rebote | TRUMP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 05:30 | macd_momentum | KAS | momentum perdido | +0.81% | +0.31% | +0.07 |
| 2026-09-30 05:30 | macd_momentum | SHIB | momentum perdido | -0.02% | -0.52% | -0.11 |
| 2026-09-30 05:30 | pullback_tendencia | NIGHT | rotura de tendencia | -0.93% | -1.43% | -0.32 |
| 2026-09-30 05:25 | macd_momentum_evento | TAO | momentum perdido | -0.07% | -0.57% | -0.13 |
| 2026-09-30 05:25 | macd_momentum_evento | SUI | momentum perdido | +0.07% | -0.43% | -0.10 |
| 2026-09-30 05:25 | macd_sin_salida | BNB | timeout | +0.41% | -0.09% | -0.02 |
| 2026-09-30 05:25 | macd_momentum | TAO | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-09-30 05:25 | macd_momentum | SUI | momentum perdido | +0.07% | -0.43% | -0.10 |
| 2026-09-30 05:20 | ruptura_volumen_evento | TON | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-09-30 05:20 | macd_momentum_evento | OP | momentum perdido | -0.09% | -0.59% | -0.13 |
| 2026-09-30 05:20 | macd_momentum_evento | RENDER | momentum perdido | +0.23% | -0.27% | -0.06 |

## Eventos de la última vuelta

- 2026-09-30 05:25 [macd_momentum] ENTRADA CRV @ 0.34313 (21.96 €, apertura)
- 2026-09-30 05:25 [macd_momentum_evento] ENTRADA CRV @ 0.34313 (22.27 €, apertura)
- 2026-09-30 05:25 [pullback_tendencia] ENTRADA INJ @ 6.795 (22.63 €, apertura)
- 2026-09-30 05:30 [pullback_tendencia] CIERRE NIGHT rotura de tendencia bruto -0.93% neto -1.43%
- 2026-09-30 05:30 [macd_momentum] CIERRE SHIB momentum perdido bruto -0.02% neto -0.52%
- 2026-09-30 05:30 [macd_momentum_evento] CIERRE SHIB momentum perdido bruto -0.02% neto -0.52%
- 2026-09-30 05:30 [estocastico_rebote] CIERRE TRUMP stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 05:25 [ruptura_volumen] ENTRADA ASTER @ 0.66925 (22.29 €, apertura)
- 2026-09-30 05:25 [ruptura_volumen_evento] ENTRADA ASTER @ 0.66925 (22.42 €, apertura)
- 2026-09-30 05:30 [macd_momentum] CIERRE KAS momentum perdido bruto +0.81% neto +0.31%
- 2026-09-30 05:30 [macd_momentum_evento] CIERRE KAS momentum perdido bruto +0.81% neto +0.31%
- 2026-09-30 05:30 [ruptura_estricta] CIERRE SPX stop-loss bruto -2.04% neto -2.54%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
