# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 05:01 UTC · vueltas 207 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.72 € (-2.87%) | 118 | 22 | 27% | -0.256% | -0.977% | -1.111% | -26.42 € |
| reversion_bb | 917.84 € (-0.69%) | 32 | 7 | 50% | +0.236% | -0.864% | -0.973% | -6.38 € |
| ruptura_volumen | 892.27 € (-3.46%) | 153 | 11 | 20% | -0.246% | -0.917% | -1.042% | -31.95 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.30 € (-2.05%) | 110 | 2 | 26% | -0.015% | -0.752% | -0.880% | -18.97 € |
| macd_momentum | 880.97 € (-4.68%) | 275 | 21 | 17% | -0.112% | -0.707% | -0.820% | -44.01 € |
| estocastico_rebote | 891.52 € (-3.54%) | 192 | 18 | 34% | -0.123% | -0.759% | -0.891% | -33.28 € |
| ruptura_estricta | 905.17 € (-2.06%) | 68 | 7 | 24% | -0.353% | -1.237% | -1.378% | -19.29 € |
| macd_sin_salida | 893.54 € (-3.32%) | 169 | 24 | 28% | -0.149% | -0.804% | -0.930% | -30.97 € |
| c_banda_atr_tope | 910.62 € (-1.47%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.10 € (-1.53%) | 55 | 5 | 16% | -0.168% | -1.148% | -1.265% | -14.50 € |
| c_banda_atr_regimen | 900.72 € (-2.55%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 898.84 € (-2.75%) | 116 | 0 | 18% | -0.234% | -0.959% | -1.087% | -25.40 € |
| c_banda_atr_evento | 900.78 € (-2.54%) | 86 | 22 | 23% | -0.377% | -1.184% | -1.320% | -23.36 € |
| macd_momentum_evento | 893.36 € (-3.34%) | 155 | 21 | 13% | -0.225% | -0.895% | -1.007% | -31.63 € |
| ruptura_volumen_evento | 897.76 € (-2.86%) | 94 | 11 | 12% | -0.450% | -1.231% | -1.355% | -26.45 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 05:00 | macd_momentum_evento | NIGHT | momentum perdido | +0.45% | -0.05% | -0.01 |
| 2026-09-30 05:00 | c_banda_atr_evento | ADA | timeout | -0.05% | -0.55% | -0.12 |
| 2026-09-30 05:00 | macd_momentum | NIGHT | momentum perdido | +0.45% | -0.05% | -0.01 |
| 2026-09-30 05:00 | c_banda_atr | ADA | timeout | -0.05% | -0.55% | -0.12 |
| 2026-09-30 04:55 | ruptura_volumen_evento | HBAR | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 04:55 | ruptura_volumen_tope | HBAR | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 04:55 | ruptura_volumen | HBAR | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 04:50 | ruptura_volumen_evento | NIGHT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 04:50 | ruptura_estricta | RENDER | timeout | -0.29% | -0.79% | -0.18 |
| 2026-09-30 04:50 | estocastico_rebote | QNT | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 04:50 | ruptura_volumen | NIGHT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 04:45 | macd_momentum_evento | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 04:45 | macd_momentum_evento | HBAR | momentum perdido | +0.35% | -0.15% | -0.03 |
| 2026-09-30 04:45 | c_banda_atr_evento | INJ | timeout | +0.73% | +0.23% | +0.05 |
| 2026-09-30 04:45 | ruptura_estricta | CRV | timeout | +0.01% | -0.49% | -0.11 |

## Eventos de la última vuelta

- 2026-09-30 05:00 [c_banda_atr] CIERRE ADA timeout bruto -0.05% neto -0.55%
- 2026-09-30 05:00 [c_banda_atr_evento] CIERRE ADA timeout bruto -0.05% neto -0.55%
- 2026-09-30 04:55 [pullback_tendencia] ENTRADA PEPE @ 3.777e-06 (22.63 €, apertura)
- 2026-09-30 05:00 [macd_momentum] CIERRE NIGHT momentum perdido bruto +0.45% neto -0.05%
- 2026-09-30 05:00 [macd_momentum_evento] CIERRE NIGHT momentum perdido bruto +0.45% neto -0.05%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
