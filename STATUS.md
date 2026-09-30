# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 00:01 UTC · vueltas 172 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 900.08 € (-2.61%) | 79 | 24 | 28% | -0.355% | -1.186% | -1.336% | -21.50 € |
| reversion_bb | 918.35 € (-0.64%) | 18 | 12 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 900.90 € (-2.53%) | 114 | 7 | 23% | -0.133% | -0.862% | -0.988% | -22.49 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.23 € (-2.17%) | 91 | 2 | 22% | -0.169% | -0.956% | -1.077% | -19.93 € |
| macd_momentum | 882.89 € (-4.47%) | 229 | 2 | 15% | -0.183% | -0.797% | -0.909% | -41.41 € |
| estocastico_rebote | 892.51 € (-3.43%) | 162 | 12 | 33% | -0.168% | -0.830% | -0.950% | -30.73 € |
| ruptura_estricta | 908.24 € (-1.73%) | 50 | 7 | 26% | -0.297% | -1.319% | -1.455% | -15.17 € |
| macd_sin_salida | 896.00 € (-3.06%) | 132 | 14 | 27% | -0.194% | -0.892% | -1.018% | -26.90 € |
| c_banda_atr_tope | 912.95 € (-1.22%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.95 € (-1.11%) | 38 | 3 | 16% | -0.032% | -1.132% | -1.250% | -9.90 € |
| c_banda_atr_regimen | 902.86 € (-2.31%) | 59 | 17 | 27% | -0.432% | -1.374% | -1.515% | -18.64 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 904.09 € (-2.18%) | 94 | 6 | 22% | -0.122% | -0.900% | -1.028% | -19.39 € |
| c_banda_atr_evento | 904.11 € (-2.18%) | 47 | 24 | 21% | -0.645% | -1.617% | -1.781% | -17.45 € |
| macd_momentum_evento | 895.30 € (-3.13%) | 109 | 2 | 7% | -0.422% | -1.165% | -1.271% | -28.99 € |
| ruptura_volumen_evento | 906.45 € (-1.93%) | 55 | 7 | 13% | -0.360% | -1.340% | -1.468% | -16.93 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 00:00 | macd_momentum_evento | XPL | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-09-30 00:00 | c_banda_atr_evento | XPL | stop-loss | -1.63% | -2.13% | -0.49 |
| 2026-09-30 00:00 | c_banda_atr_evento | NIGHT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 00:00 | macd_momentum_regimen | XPL | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-09-30 00:00 | c_banda_atr_regimen | XPL | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-09-30 00:00 | macd_sin_salida | XPL | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-09-30 00:00 | ruptura_estricta | NIGHT | timeout | -0.87% | -1.37% | -0.31 |
| 2026-09-30 00:00 | macd_momentum | XPL | stop-loss | -1.63% | -2.13% | -0.47 |
| 2026-09-30 00:00 | c_banda_atr | XPL | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-09-30 00:00 | c_banda_atr | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 23:55 | macd_momentum_evento | DASH | momentum perdido | +0.14% | -0.36% | -0.08 |
| 2026-09-29 23:55 | macd_momentum | DASH | momentum perdido | +0.14% | -0.36% | -0.08 |
| 2026-09-29 23:50 | ruptura_volumen_evento | ZEC | timeout | -0.05% | -0.55% | -0.12 |
| 2026-09-29 23:50 | macd_momentum_evento | POL | momentum perdido | -0.75% | -1.25% | -0.28 |
| 2026-09-29 23:50 | macd_momentum_evento | ATOM | momentum perdido | -0.39% | -0.89% | -0.20 |

## Eventos de la última vuelta

- 2026-09-29 23:55 [c_banda_atr] ENTRADA ICP @ 3.039 (22.59 €, apertura)
- 2026-09-29 23:55 [macd_momentum] ENTRADA ICP @ 3.039 (22.08 €, apertura)
- 2026-09-29 23:55 [macd_sin_salida] ENTRADA ICP @ 3.039 (22.45 €, apertura)
- 2026-09-29 23:55 [c_banda_atr_evento] ENTRADA ICP @ 3.039 (22.69 €, apertura)
- 2026-09-29 23:55 [macd_momentum_evento] ENTRADA ICP @ 3.039 (22.39 €, apertura)
- 2026-09-29 23:55 [pullback_tendencia] ENTRADA ZRO @ 1.464 (22.61 €, apertura)
- 2026-09-29 23:55 [estocastico_rebote] ENTRADA PEPE @ 3.749e-06 (22.34 €, apertura)
- 2026-09-30 00:00 [c_banda_atr] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:00 [ruptura_estricta] CIERRE NIGHT timeout bruto -0.87% neto -1.37%
- 2026-09-30 00:00 [c_banda_atr_evento] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:55 [estocastico_rebote] ENTRADA PENGU @ 0.00879 (22.34 €, apertura)
- 2026-09-30 00:00 [c_banda_atr] CIERRE XPL stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 00:00 [macd_momentum] CIERRE XPL stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 00:00 [macd_sin_salida] CIERRE XPL stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 00:00 [c_banda_atr_regimen] CIERRE XPL stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 00:00 [macd_momentum_regimen] CIERRE XPL stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 00:00 [c_banda_atr_evento] CIERRE XPL stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 00:00 [macd_momentum_evento] CIERRE XPL stop-loss bruto -1.63% neto -2.13%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
