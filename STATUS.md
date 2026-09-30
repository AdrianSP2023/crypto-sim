# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 00:06 UTC · vueltas 173 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 900.22 € (-2.60%) | 79 | 24 | 28% | -0.355% | -1.186% | -1.336% | -21.50 € |
| reversion_bb | 918.51 € (-0.62%) | 18 | 13 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 900.80 € (-2.54%) | 115 | 6 | 23% | -0.136% | -0.863% | -0.989% | -22.71 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.81 € (-2.10%) | 91 | 2 | 22% | -0.169% | -0.956% | -1.077% | -19.93 € |
| macd_momentum | 883.10 € (-4.45%) | 230 | 1 | 15% | -0.174% | -0.787% | -0.899% | -41.07 € |
| estocastico_rebote | 892.72 € (-3.41%) | 163 | 11 | 33% | -0.168% | -0.828% | -0.948% | -30.88 € |
| ruptura_estricta | 908.34 € (-1.72%) | 50 | 7 | 26% | -0.297% | -1.319% | -1.455% | -15.17 € |
| macd_sin_salida | 896.38 € (-3.01%) | 134 | 12 | 27% | -0.188% | -0.882% | -1.008% | -27.01 € |
| c_banda_atr_tope | 912.90 € (-1.23%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.95 € (-1.11%) | 38 | 3 | 16% | -0.032% | -1.132% | -1.250% | -9.90 € |
| c_banda_atr_regimen | 902.84 € (-2.32%) | 59 | 17 | 27% | -0.432% | -1.374% | -1.515% | -18.64 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 904.12 € (-2.18%) | 94 | 6 | 22% | -0.122% | -0.900% | -1.028% | -19.39 € |
| c_banda_atr_evento | 904.25 € (-2.16%) | 47 | 24 | 21% | -0.645% | -1.617% | -1.781% | -17.45 € |
| macd_momentum_evento | 895.52 € (-3.11%) | 110 | 1 | 8% | -0.400% | -1.140% | -1.248% | -28.65 € |
| ruptura_volumen_evento | 906.34 € (-1.94%) | 56 | 6 | 12% | -0.362% | -1.333% | -1.460% | -17.16 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 00:05 | ruptura_volumen_evento | PEPE | timeout | -0.48% | -0.98% | -0.22 |
| 2026-09-30 00:05 | macd_momentum_evento | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 00:05 | macd_sin_salida | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 00:05 | macd_sin_salida | LINK | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 00:05 | estocastico_rebote | ASTER | timeout | -0.14% | -0.64% | -0.14 |
| 2026-09-30 00:05 | macd_momentum | QNT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 00:05 | ruptura_volumen | PEPE | timeout | -0.48% | -0.98% | -0.22 |
| 2026-09-30 00:00 | macd_momentum_evento | XPL | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-09-30 00:00 | c_banda_atr_evento | XPL | stop-loss | -1.63% | -2.13% | -0.49 |
| 2026-09-30 00:00 | c_banda_atr_evento | NIGHT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 00:00 | macd_momentum_regimen | XPL | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-09-30 00:00 | c_banda_atr_regimen | XPL | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-09-30 00:00 | macd_sin_salida | XPL | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-09-30 00:00 | ruptura_estricta | NIGHT | timeout | -0.87% | -1.37% | -0.31 |
| 2026-09-30 00:00 | macd_momentum | XPL | stop-loss | -1.63% | -2.13% | -0.47 |

## Eventos de la última vuelta

- 2026-09-30 00:05 [macd_sin_salida] CIERRE LINK stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:05 [macd_momentum] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 00:05 [macd_sin_salida] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 00:05 [macd_momentum_evento] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 00:00 [reversion_bb] ENTRADA TRX @ 0.294808 (22.95 €, apertura)
- 2026-09-30 00:05 [ruptura_volumen] CIERRE PEPE timeout bruto -0.48% neto -0.98%
- 2026-09-30 00:05 [ruptura_volumen_evento] CIERRE PEPE timeout bruto -0.48% neto -0.98%
- 2026-09-30 00:05 [estocastico_rebote] CIERRE ASTER timeout bruto -0.14% neto -0.64%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
