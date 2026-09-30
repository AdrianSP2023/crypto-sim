# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 04:01 UTC · vueltas 195 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 896.64 € (-2.99%) | 112 | 16 | 27% | -0.286% | -1.020% | -1.155% | -26.16 € |
| reversion_bb | 918.10 € (-0.66%) | 29 | 10 | 48% | +0.205% | -0.895% | -0.997% | -5.98 € |
| ruptura_volumen | 893.11 € (-3.37%) | 148 | 4 | 20% | -0.241% | -0.917% | -1.043% | -30.94 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.93 € (-2.09%) | 109 | 0 | 26% | -0.034% | -0.773% | -0.900% | -19.31 € |
| macd_momentum | 880.55 € (-4.73%) | 269 | 6 | 17% | -0.119% | -0.716% | -0.828% | -43.59 € |
| estocastico_rebote | 888.88 € (-3.83%) | 190 | 18 | 33% | -0.144% | -0.781% | -0.912% | -33.86 € |
| ruptura_estricta | 904.14 € (-2.17%) | 65 | 5 | 25% | -0.348% | -1.249% | -1.393% | -18.63 € |
| macd_sin_salida | 892.37 € (-3.45%) | 161 | 16 | 29% | -0.160% | -0.822% | -0.948% | -30.20 € |
| c_banda_atr_tope | 910.21 € (-1.52%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.14 € (-1.53%) | 52 | 4 | 17% | -0.153% | -1.161% | -1.284% | -13.86 € |
| c_banda_atr_regimen | 900.67 € (-2.55%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 898.90 € (-2.74%) | 113 | 3 | 19% | -0.243% | -0.974% | -1.103% | -25.15 € |
| c_banda_atr_evento | 899.70 € (-2.66%) | 80 | 16 | 22% | -0.429% | -1.259% | -1.397% | -23.10 € |
| macd_momentum_evento | 892.93 € (-3.39%) | 149 | 6 | 13% | -0.241% | -0.918% | -1.027% | -31.20 € |
| ruptura_volumen_evento | 898.60 € (-2.77%) | 89 | 4 | 12% | -0.453% | -1.249% | -1.375% | -25.43 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 04:00 | macd_momentum_evento | NIGHT | momentum perdido | -0.28% | -0.78% | -0.17 |
| 2026-09-30 04:00 | macd_sin_salida | ADA | timeout | -0.22% | -0.72% | -0.16 |
| 2026-09-30 04:00 | estocastico_rebote | SUI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 04:00 | estocastico_rebote | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 04:00 | macd_momentum | NIGHT | momentum perdido | -0.28% | -0.78% | -0.17 |
| 2026-09-30 03:55 | ruptura_volumen_evento | TRX | timeout | +0.39% | -0.11% | -0.02 |
| 2026-09-30 03:55 | ruptura_volumen_regimen | TRX | timeout | +0.39% | -0.11% | -0.02 |
| 2026-09-30 03:55 | ruptura_volumen | TRX | timeout | +0.39% | -0.11% | -0.02 |
| 2026-09-30 03:35 | macd_momentum_evento | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 03:35 | macd_sin_salida | SPX | timeout | +0.81% | +0.31% | +0.07 |
| 2026-09-30 03:35 | macd_sin_salida | JUP | timeout | -1.05% | -1.55% | -0.35 |
| 2026-09-30 03:35 | macd_sin_salida | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 03:35 | estocastico_rebote | JUP | timeout | -1.05% | -1.55% | -0.34 |
| 2026-09-30 03:35 | estocastico_rebote | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 03:35 | macd_momentum | QNT | stop-loss | -1.50% | -2.00% | -0.44 |

## Eventos de la última vuelta

- 2026-09-30 04:00 [estocastico_rebote] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 04:00 [macd_sin_salida] CIERRE ADA timeout bruto -0.22% neto -0.72%
- 2026-09-30 04:00 [estocastico_rebote] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 03:55 [macd_momentum] ENTRADA WLD @ 0.4331 (22.02 €, apertura)
- 2026-09-30 03:55 [macd_sin_salida] ENTRADA WLD @ 0.4331 (22.35 €, apertura)
- 2026-09-30 03:55 [macd_momentum_evento] ENTRADA WLD @ 0.4331 (22.33 €, apertura)
- 2026-09-30 04:00 [macd_momentum] CIERRE NIGHT momentum perdido bruto -0.28% neto -0.78%
- 2026-09-30 04:00 [macd_momentum_evento] CIERRE NIGHT momentum perdido bruto -0.28% neto -0.78%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
