# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 04:06 UTC · vueltas 196 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.61 € (-2.88%) | 113 | 15 | 27% | -0.285% | -1.016% | -1.150% | -26.30 € |
| reversion_bb | 918.22 € (-0.65%) | 30 | 9 | 47% | +0.137% | -0.963% | -1.068% | -6.66 € |
| ruptura_volumen | 893.47 € (-3.33%) | 148 | 4 | 20% | -0.241% | -0.917% | -1.043% | -30.94 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.93 € (-2.09%) | 109 | 0 | 26% | -0.034% | -0.773% | -0.900% | -19.31 € |
| macd_momentum | 880.68 € (-4.71%) | 270 | 6 | 17% | -0.118% | -0.715% | -0.827% | -43.68 € |
| estocastico_rebote | 890.27 € (-3.68%) | 191 | 17 | 34% | -0.133% | -0.770% | -0.902% | -33.57 € |
| ruptura_estricta | 904.59 € (-2.13%) | 65 | 5 | 25% | -0.348% | -1.249% | -1.393% | -18.63 € |
| macd_sin_salida | 893.09 € (-3.37%) | 165 | 13 | 28% | -0.165% | -0.823% | -0.946% | -30.96 € |
| c_banda_atr_tope | 910.57 € (-1.48%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.52 € (-1.48%) | 52 | 4 | 17% | -0.153% | -1.161% | -1.284% | -13.86 € |
| c_banda_atr_regimen | 900.77 € (-2.54%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 899.19 € (-2.71%) | 113 | 3 | 19% | -0.243% | -0.974% | -1.103% | -25.15 € |
| c_banda_atr_evento | 900.67 € (-2.55%) | 81 | 15 | 22% | -0.425% | -1.251% | -1.388% | -23.24 € |
| macd_momentum_evento | 893.06 € (-3.37%) | 150 | 6 | 13% | -0.239% | -0.915% | -1.025% | -31.30 € |
| ruptura_volumen_evento | 898.97 € (-2.73%) | 89 | 4 | 12% | -0.453% | -1.249% | -1.375% | -25.43 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 04:05 | macd_momentum_evento | ZRO | momentum perdido | +0.06% | -0.44% | -0.10 |
| 2026-09-30 04:05 | c_banda_atr_evento | SHIB | timeout | -0.12% | -0.62% | -0.14 |
| 2026-09-30 04:05 | macd_sin_salida | SHIB | timeout | -0.39% | -0.89% | -0.20 |
| 2026-09-30 04:05 | macd_sin_salida | PEPE | timeout | +0.13% | -0.37% | -0.08 |
| 2026-09-30 04:05 | macd_sin_salida | ATOM | timeout | -1.05% | -1.55% | -0.35 |
| 2026-09-30 04:05 | macd_sin_salida | SUI | timeout | -0.09% | -0.59% | -0.13 |
| 2026-09-30 04:05 | estocastico_rebote | NIGHT | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 04:05 | macd_momentum | ZRO | momentum perdido | +0.06% | -0.44% | -0.10 |
| 2026-09-30 04:05 | reversion_bb | GRT | stop-loss | -1.86% | -2.96% | -0.68 |
| 2026-09-30 04:05 | c_banda_atr | SHIB | timeout | -0.12% | -0.62% | -0.14 |
| 2026-09-30 04:00 | macd_momentum_evento | NIGHT | momentum perdido | -0.28% | -0.78% | -0.17 |
| 2026-09-30 04:00 | macd_sin_salida | ADA | timeout | -0.22% | -0.72% | -0.16 |
| 2026-09-30 04:00 | estocastico_rebote | SUI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 04:00 | estocastico_rebote | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 04:00 | macd_momentum | NIGHT | momentum perdido | -0.28% | -0.78% | -0.17 |

## Eventos de la última vuelta

- 2026-09-30 04:05 [macd_sin_salida] CIERRE SUI timeout bruto -0.09% neto -0.59%
- 2026-09-30 04:05 [macd_sin_salida] CIERRE ATOM timeout bruto -1.05% neto -1.55%
- 2026-09-30 04:05 [macd_momentum] CIERRE ZRO momentum perdido bruto +0.06% neto -0.44%
- 2026-09-30 04:05 [macd_momentum_evento] CIERRE ZRO momentum perdido bruto +0.06% neto -0.44%
- 2026-09-30 04:05 [macd_sin_salida] CIERRE PEPE timeout bruto +0.13% neto -0.37%
- 2026-09-30 04:05 [estocastico_rebote] CIERRE NIGHT take-profit bruto +1.80% neto +1.30%
- 2026-09-30 04:05 [c_banda_atr] CIERRE SHIB timeout bruto -0.12% neto -0.62%
- 2026-09-30 04:05 [macd_sin_salida] CIERRE SHIB timeout bruto -0.39% neto -0.89%
- 2026-09-30 04:05 [c_banda_atr_evento] CIERRE SHIB timeout bruto -0.12% neto -0.62%
- 2026-09-30 04:05 [reversion_bb] CIERRE GRT stop-loss bruto -1.86% neto -2.96%
- 2026-09-30 04:00 [macd_momentum] ENTRADA KAS @ 0.03835 (22.01 €, apertura)
- 2026-09-30 04:00 [macd_sin_salida] ENTRADA KAS @ 0.03835 (22.33 €, apertura)
- 2026-09-30 04:00 [macd_momentum_evento] ENTRADA KAS @ 0.03835 (22.32 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
