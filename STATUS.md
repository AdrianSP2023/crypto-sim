# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 05:26 UTC · vueltas 212 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.58 € (-2.88%) | 122 | 21 | 28% | -0.242% | -0.956% | -1.090% | -26.72 € |
| reversion_bb | 917.87 € (-0.69%) | 32 | 7 | 50% | +0.236% | -0.864% | -0.973% | -6.38 € |
| ruptura_volumen | 891.68 € (-3.52%) | 155 | 12 | 19% | -0.261% | -0.929% | -1.055% | -32.79 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.03 € (-2.08%) | 111 | 2 | 26% | -0.016% | -0.751% | -0.878% | -19.12 € |
| macd_momentum | 879.53 € (-4.84%) | 289 | 10 | 16% | -0.111% | -0.701% | -0.813% | -45.82 € |
| estocastico_rebote | 890.98 € (-3.60%) | 195 | 17 | 34% | -0.111% | -0.744% | -0.877% | -33.14 € |
| ruptura_estricta | 904.57 € (-2.13%) | 69 | 6 | 23% | -0.359% | -1.237% | -1.378% | -19.58 € |
| macd_sin_salida | 893.25 € (-3.35%) | 174 | 21 | 28% | -0.156% | -0.806% | -0.932% | -31.94 € |
| c_banda_atr_tope | 911.01 € (-1.43%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 909.78 € (-1.56%) | 56 | 5 | 16% | -0.186% | -1.158% | -1.275% | -14.88 € |
| c_banda_atr_regimen | 900.69 € (-2.55%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 898.84 € (-2.75%) | 116 | 0 | 18% | -0.234% | -0.959% | -1.087% | -25.40 € |
| c_banda_atr_evento | 900.64 € (-2.55%) | 90 | 21 | 24% | -0.353% | -1.147% | -1.282% | -23.66 € |
| macd_momentum_evento | 891.90 € (-3.50%) | 169 | 10 | 12% | -0.214% | -0.870% | -0.979% | -33.47 € |
| ruptura_volumen_evento | 897.17 € (-2.93%) | 96 | 12 | 11% | -0.470% | -1.245% | -1.370% | -27.29 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 05:25 | macd_momentum_evento | TAO | momentum perdido | -0.07% | -0.57% | -0.13 |
| 2026-09-30 05:25 | macd_momentum_evento | SUI | momentum perdido | +0.07% | -0.43% | -0.10 |
| 2026-09-30 05:25 | macd_sin_salida | BNB | timeout | +0.41% | -0.09% | -0.02 |
| 2026-09-30 05:25 | macd_momentum | TAO | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-09-30 05:25 | macd_momentum | SUI | momentum perdido | +0.07% | -0.43% | -0.10 |
| 2026-09-30 05:20 | ruptura_volumen_evento | TON | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-09-30 05:20 | macd_momentum_evento | OP | momentum perdido | -0.09% | -0.59% | -0.13 |
| 2026-09-30 05:20 | macd_momentum_evento | RENDER | momentum perdido | +0.23% | -0.27% | -0.06 |
| 2026-09-30 05:20 | macd_momentum_evento | DASH | momentum perdido | -0.51% | -1.01% | -0.23 |
| 2026-09-30 05:20 | macd_momentum_evento | LTC | momentum perdido | -0.29% | -0.79% | -0.17 |
| 2026-09-30 05:20 | c_banda_atr_evento | NEAR | stop-loss | -1.54% | -2.04% | -0.46 |
| 2026-09-30 05:20 | macd_sin_salida | NEAR | stop-loss | -1.54% | -2.04% | -0.46 |
| 2026-09-30 05:20 | macd_momentum | OP | momentum perdido | -0.09% | -0.59% | -0.13 |
| 2026-09-30 05:20 | macd_momentum | RENDER | momentum perdido | +0.23% | -0.27% | -0.06 |
| 2026-09-30 05:20 | macd_momentum | DASH | momentum perdido | -0.51% | -1.01% | -0.22 |

## Eventos de la última vuelta

- 2026-09-30 05:20 [estocastico_rebote] ENTRADA QNT @ 250.83 (22.28 €, apertura)
- 2026-09-30 05:25 [macd_momentum] CIERRE SUI momentum perdido bruto +0.07% neto -0.43%
- 2026-09-30 05:25 [macd_momentum_evento] CIERRE SUI momentum perdido bruto +0.07% neto -0.43%
- 2026-09-30 05:25 [macd_momentum] CIERRE TAO momentum perdido bruto -0.07% neto -0.57%
- 2026-09-30 05:25 [macd_momentum_evento] CIERRE TAO momentum perdido bruto -0.07% neto -0.57%
- 2026-09-30 05:25 [macd_sin_salida] CIERRE BNB timeout bruto +0.41% neto -0.09%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
