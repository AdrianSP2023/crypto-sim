# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 01:06 UTC · vueltas 185 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 901.82 € (-2.43%) | 90 | 25 | 27% | -0.374% | -1.164% | -1.308% | -24.02 € |
| reversion_bb | 919.75 € (-0.49%) | 21 | 13 | 38% | -0.165% | -1.265% | -1.361% | -6.13 € |
| ruptura_volumen | 900.32 € (-2.59%) | 120 | 7 | 22% | -0.165% | -0.882% | -1.010% | -24.21 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.48 € (-2.03%) | 94 | 4 | 23% | -0.131% | -0.909% | -1.029% | -19.57 € |
| macd_momentum | 884.80 € (-4.27%) | 232 | 14 | 15% | -0.176% | -0.789% | -0.900% | -41.49 € |
| estocastico_rebote | 893.96 € (-3.28%) | 174 | 10 | 33% | -0.144% | -0.794% | -0.924% | -31.56 € |
| ruptura_estricta | 908.99 € (-1.65%) | 53 | 5 | 26% | -0.257% | -1.249% | -1.386% | -15.22 € |
| macd_sin_salida | 897.57 € (-2.89%) | 142 | 13 | 27% | -0.193% | -0.877% | -1.000% | -28.42 € |
| c_banda_atr_tope | 912.71 € (-1.25%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.65 € (-1.15%) | 41 | 4 | 17% | -0.064% | -1.164% | -1.284% | -10.98 € |
| c_banda_atr_regimen | 902.08 € (-2.40%) | 68 | 8 | 24% | -0.518% | -1.401% | -1.535% | -21.87 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.69 € (-2.22%) | 96 | 4 | 22% | -0.151% | -0.922% | -1.053% | -20.29 € |
| c_banda_atr_evento | 905.38 € (-2.04%) | 58 | 25 | 21% | -0.618% | -1.537% | -1.690% | -20.47 € |
| macd_momentum_evento | 897.24 € (-2.92%) | 112 | 14 | 8% | -0.401% | -1.137% | -1.244% | -29.08 € |
| ruptura_volumen_evento | 905.86 € (-1.99%) | 61 | 7 | 13% | -0.400% | -1.333% | -1.463% | -18.66 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 01:05 | ruptura_volumen_evento | ASTER | timeout | +1.25% | +0.75% | +0.17 |
| 2026-09-30 01:05 | ruptura_volumen_tope | ASTER | timeout | +1.25% | +0.15% | +0.03 |
| 2026-09-30 01:05 | macd_sin_salida | NIGHT | timeout | +0.77% | +0.27% | +0.06 |
| 2026-09-30 01:05 | macd_sin_salida | HYPE | timeout | +0.18% | -0.32% | -0.07 |
| 2026-09-30 01:05 | macd_sin_salida | XLM | timeout | -0.81% | -1.31% | -0.30 |
| 2026-09-30 01:05 | macd_sin_salida | SOL | timeout | -0.13% | -0.63% | -0.14 |
| 2026-09-30 01:05 | estocastico_rebote | PUMP | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 01:05 | ruptura_volumen | ASTER | timeout | +1.25% | +0.75% | +0.17 |
| 2026-09-30 01:05 | reversion_bb | MON | take-profit | +1.53% | +0.43% | +0.10 |
| 2026-09-30 01:00 | c_banda_atr_evento | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:00 | estocastico_rebote | SUI | timeout | -0.56% | -1.06% | -0.24 |
| 2026-09-30 01:00 | c_banda_atr | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 00:55 | estocastico_rebote | SPX | timeout | +0.38% | -0.12% | -0.03 |
| 2026-09-30 00:50 | ruptura_volumen_evento | NEAR | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 00:50 | ruptura_estricta | BCH | timeout | -0.64% | -1.14% | -0.26 |

## Eventos de la última vuelta

- 2026-09-30 01:05 [macd_sin_salida] CIERRE SOL timeout bruto -0.13% neto -0.63%
- 2026-09-30 01:00 [pullback_tendencia] ENTRADA QNT @ 240 (22.62 €, apertura)
- 2026-09-30 01:00 [c_banda_atr] ENTRADA ADA @ 0.215429 (22.51 €, apertura)
- 2026-09-30 01:00 [macd_momentum] ENTRADA ADA @ 0.215429 (22.07 €, apertura)
- 2026-09-30 01:00 [macd_sin_salida] ENTRADA ADA @ 0.215429 (22.40 €, apertura)
- 2026-09-30 01:00 [c_banda_atr_evento] ENTRADA ADA @ 0.215429 (22.59 €, apertura)
- 2026-09-30 01:00 [macd_momentum_evento] ENTRADA ADA @ 0.215429 (22.38 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] CIERRE XLM timeout bruto -0.81% neto -1.31%
- 2026-09-30 01:05 [estocastico_rebote] CIERRE PUMP take-profit bruto +1.80% neto +1.30%
- 2026-09-30 01:05 [macd_sin_salida] CIERRE HYPE timeout bruto +0.18% neto -0.32%
- 2026-09-30 01:05 [reversion_bb] CIERRE MON take-profit bruto +1.53% neto +0.43%
- 2026-09-30 01:05 [macd_sin_salida] CIERRE NIGHT timeout bruto +0.76% neto +0.26%
- 2026-09-30 01:05 [ruptura_volumen] CIERRE ASTER timeout bruto +1.25% neto +0.75%
- 2026-09-30 01:05 [ruptura_volumen_tope] CIERRE ASTER timeout bruto +1.25% neto +0.15%
- 2026-09-30 01:05 [ruptura_volumen_evento] CIERRE ASTER timeout bruto +1.25% neto +0.75%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
