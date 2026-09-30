# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 05:11 UTC · vueltas 209 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.26 € (-2.81%) | 121 | 22 | 28% | -0.232% | -0.947% | -1.082% | -26.26 € |
| reversion_bb | 917.92 € (-0.68%) | 32 | 7 | 50% | +0.236% | -0.864% | -0.973% | -6.38 € |
| ruptura_volumen | 892.20 € (-3.47%) | 154 | 13 | 19% | -0.252% | -0.922% | -1.047% | -32.33 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.29 € (-2.05%) | 110 | 3 | 26% | -0.015% | -0.752% | -0.880% | -18.97 € |
| macd_momentum | 881.11 € (-4.67%) | 281 | 17 | 17% | -0.107% | -0.700% | -0.813% | -44.50 € |
| estocastico_rebote | 890.98 € (-3.60%) | 194 | 17 | 34% | -0.120% | -0.755% | -0.888% | -33.43 € |
| ruptura_estricta | 905.01 € (-2.08%) | 69 | 6 | 23% | -0.359% | -1.237% | -1.378% | -19.58 € |
| macd_sin_salida | 894.11 € (-3.26%) | 171 | 24 | 29% | -0.143% | -0.796% | -0.923% | -31.02 € |
| c_banda_atr_tope | 911.06 € (-1.43%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 909.96 € (-1.55%) | 56 | 4 | 16% | -0.186% | -1.158% | -1.275% | -14.88 € |
| c_banda_atr_regimen | 900.76 € (-2.54%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 898.84 € (-2.75%) | 116 | 0 | 18% | -0.234% | -0.959% | -1.087% | -25.40 € |
| c_banda_atr_evento | 901.32 € (-2.48%) | 89 | 22 | 25% | -0.340% | -1.137% | -1.273% | -23.20 € |
| macd_momentum_evento | 893.49 € (-3.33%) | 161 | 17 | 13% | -0.212% | -0.876% | -0.987% | -32.13 € |
| ruptura_volumen_evento | 897.69 € (-2.87%) | 95 | 13 | 12% | -0.458% | -1.236% | -1.360% | -26.83 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 05:10 | ruptura_volumen_evento | SPX | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 05:10 | ruptura_volumen_tope | SPX | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 05:10 | estocastico_rebote | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 05:10 | ruptura_volumen | SPX | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 05:05 | macd_momentum_evento | SPX | momentum perdido | -0.69% | -1.19% | -0.27 |
| 2026-09-30 05:05 | macd_momentum_evento | TRUMP | momentum perdido | -0.55% | -1.05% | -0.23 |
| 2026-09-30 05:05 | macd_momentum_evento | TON | take-profit | +2.28% | +1.78% | +0.40 |
| 2026-09-30 05:05 | macd_momentum_evento | DOT | momentum perdido | +0.19% | -0.31% | -0.07 |
| 2026-09-30 05:05 | macd_momentum_evento | ADA | momentum perdido | -0.41% | -0.91% | -0.20 |
| 2026-09-30 05:05 | macd_momentum_evento | XRP | momentum perdido | -0.07% | -0.57% | -0.13 |
| 2026-09-30 05:05 | c_banda_atr_evento | TON | take-profit | +2.28% | +1.78% | +0.40 |
| 2026-09-30 05:05 | c_banda_atr_evento | ATOM | timeout | -1.08% | -1.58% | -0.36 |
| 2026-09-30 05:05 | c_banda_atr_evento | TAO | timeout | +0.99% | +0.49% | +0.11 |
| 2026-09-30 05:05 | macd_sin_salida | TON | take-profit | +2.28% | +1.78% | +0.40 |
| 2026-09-30 05:05 | macd_sin_salida | VVV | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-30 05:05 [estocastico_rebote] ENTRADA QNT @ 250 (22.28 €, apertura)
- 2026-09-30 05:10 [estocastico_rebote] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 05:05 [macd_momentum] ENTRADA LTC @ 59.26 (21.99 €, apertura)
- 2026-09-30 05:05 [macd_sin_salida] ENTRADA LTC @ 59.26 (22.33 €, apertura)
- 2026-09-30 05:05 [macd_momentum_evento] ENTRADA LTC @ 59.26 (22.30 €, apertura)
- 2026-09-30 05:05 [c_banda_atr] ENTRADA MON @ 0.02351 (22.45 €, apertura)
- 2026-09-30 05:05 [c_banda_atr_evento] ENTRADA MON @ 0.02351 (22.53 €, apertura)
- 2026-09-30 05:05 [ruptura_volumen] ENTRADA ICP @ 3.036 (22.31 €, apertura)
- 2026-09-30 05:05 [ruptura_volumen_evento] ENTRADA ICP @ 3.036 (22.44 €, apertura)
- 2026-09-30 05:05 [macd_momentum] ENTRADA TRX @ 0.297127 (21.99 €, apertura)
- 2026-09-30 05:05 [macd_sin_salida] ENTRADA TRX @ 0.297127 (22.33 €, apertura)
- 2026-09-30 05:05 [macd_momentum_evento] ENTRADA TRX @ 0.297127 (22.30 €, apertura)
- 2026-09-30 05:05 [pullback_tendencia] ENTRADA NIGHT @ 0.02912 (22.63 €, apertura)
- 2026-09-30 05:05 [c_banda_atr] ENTRADA SHIB @ 5.102e-06 (22.45 €, apertura)
- 2026-09-30 05:05 [c_banda_atr_evento] ENTRADA SHIB @ 5.102e-06 (22.53 €, apertura)
- 2026-09-30 05:05 [ruptura_volumen] ENTRADA XPL @ 0.0852 (22.31 €, apertura)
- 2026-09-30 05:05 [ruptura_volumen_evento] ENTRADA XPL @ 0.0852 (22.44 €, apertura)
- 2026-09-30 05:10 [ruptura_volumen] CIERRE SPX stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 05:10 [ruptura_volumen_tope] CIERRE SPX stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 05:10 [ruptura_volumen_evento] CIERRE SPX stop-loss bruto -1.20% neto -1.70%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
