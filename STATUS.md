# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 17:26 UTC · vueltas 62 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 912.64 € (-1.25%) | 39 | 11 | 33% | -0.204% | -1.288% | -1.449% | -11.61 € |
| reversion_bb | 923.92 € (-0.04%) | 4 | 1 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 901.86 € (-2.42%) | 55 | 17 | 16% | -0.613% | -1.588% | -1.737% | -20.10 € |
| rebote_extremo | 924.40 € (+0.02%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 910.22 € (-1.52%) | 40 | 9 | 18% | -0.373% | -1.473% | -1.596% | -13.55 € |
| macd_momentum | 911.84 € (-1.34%) | 62 | 4 | 31% | +0.031% | -0.890% | -1.030% | -12.72 € |
| estocastico_rebote | 916.48 € (-0.84%) | 66 | 12 | 52% | +0.318% | -0.559% | -0.720% | -8.59 € |
| ruptura_estricta | 900.32 € (-2.59%) | 42 | 3 | 10% | -1.325% | -2.425% | -2.569% | -23.48 € |
| macd_sin_salida | 908.21 € (-1.73%) | 56 | 7 | 34% | -0.237% | -1.203% | -1.346% | -15.56 € |
| c_banda_atr_tope | 923.02 € (-0.13%) | 10 | 4 | 50% | +0.251% | -0.849% | -1.020% | -1.96 € |
| ruptura_volumen_tope | 920.18 € (-0.44%) | 11 | 5 | 27% | -0.187% | -1.287% | -1.378% | -3.27 € |
| c_banda_atr_regimen | 912.24 € (-1.30%) | 36 | 8 | 31% | -0.290% | -1.390% | -1.546% | -11.56 € |
| macd_momentum_regimen | 912.15 € (-1.31%) | 54 | 3 | 30% | -0.002% | -0.986% | -1.126% | -12.28 € |
| ruptura_volumen_regimen | 901.67 € (-2.44%) | 56 | 16 | 16% | -0.624% | -1.590% | -1.739% | -20.49 € |
| c_banda_atr_evento | 923.69 € (-0.06%) | 5 | 13 | 60% | +0.600% | -0.500% | -0.688% | -0.58 € |
| macd_momentum_evento | 920.90 € (-0.36%) | 15 | 4 | 33% | +0.041% | -1.059% | -1.208% | -3.67 € |
| ruptura_volumen_evento | 920.09 € (-0.45%) | 5 | 17 | 20% | -0.480% | -1.580% | -1.719% | -1.82 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 17:25 | macd_momentum_evento | QNT | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 17:25 | macd_momentum_regimen | QNT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 17:25 | macd_sin_salida | QNT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 17:25 | macd_momentum | QNT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 17:25 | pullback_tendencia | ADA | rotura de tendencia | -0.22% | -1.32% | -0.30 |
| 2026-09-30 17:20 | ruptura_volumen_evento | ZEC | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:20 | c_banda_atr_evento | ASTER | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 17:20 | ruptura_volumen_regimen | ZEC | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 17:20 | c_banda_atr_tope | ASTER | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 17:20 | macd_sin_salida | ASTER | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 17:20 | ruptura_estricta | SPX | stop-loss | -2.00% | -3.10% | -0.70 |
| 2026-09-30 17:20 | ruptura_estricta | NEAR | stop-loss | -2.00% | -3.10% | -0.70 |
| 2026-09-30 17:20 | pullback_tendencia | MON | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-30 17:20 | pullback_tendencia | LTC | rotura de tendencia | -0.35% | -1.45% | -0.33 |
| 2026-09-30 17:20 | ruptura_volumen | ZEC | stop-loss | -1.20% | -1.70% | -0.39 |

## Eventos de la última vuelta

- 2026-09-30 17:25 [macd_momentum] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:25 [macd_sin_salida] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:25 [macd_momentum_regimen] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:25 [macd_momentum_evento] CIERRE QNT stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:20 [pullback_tendencia] ENTRADA ADA @ 0.218582 (22.77 €, apertura)
- 2026-09-30 17:25 [pullback_tendencia] CIERRE ADA rotura de tendencia bruto -0.22% neto -1.32%
- 2026-09-30 17:20 [pullback_tendencia] ENTRADA ZEC @ 1288.89 (22.77 €, apertura)
- 2026-09-30 17:20 [estocastico_rebote] ENTRADA XDC @ 0.03023 (22.89 €, apertura)
- 2026-09-30 17:20 [ruptura_volumen] ENTRADA MON @ 0.02532 (22.60 €, apertura)
- 2026-09-30 17:20 [ruptura_estricta] ENTRADA MON @ 0.02532 (22.52 €, apertura)
- 2026-09-30 17:20 [ruptura_volumen_regimen] ENTRADA MON @ 0.02532 (22.59 €, apertura)
- 2026-09-30 17:20 [ruptura_volumen_evento] ENTRADA MON @ 0.02532 (23.06 €, apertura)
- 2026-09-30 17:20 [reversion_bb] ENTRADA ASTER @ 0.66973 (23.10 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
