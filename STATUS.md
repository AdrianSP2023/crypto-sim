# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 16:16 UTC · vueltas 48 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 915.94 € (-0.90%) | 32 | 11 | 38% | -0.172% | -1.272% | -1.442% | -9.41 € |
| reversion_bb | 924.04 € (-0.02%) | 3 | 1 | 67% | +0.500% | -0.600% | -0.707% | -0.42 € |
| ruptura_volumen | 905.25 € (-2.05%) | 51 | 5 | 16% | -0.638% | -1.650% | -1.798% | -19.38 € |
| rebote_extremo | 924.47 € (+0.02%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 912.48 € (-1.27%) | 33 | 1 | 18% | -0.461% | -1.561% | -1.697% | -11.86 € |
| macd_momentum | 913.17 € (-1.20%) | 56 | 7 | 32% | +0.060% | -0.906% | -1.052% | -11.71 € |
| estocastico_rebote | 918.32 € (-0.64%) | 58 | 16 | 48% | +0.189% | -0.704% | -0.868% | -9.48 € |
| ruptura_estricta | 902.55 € (-2.35%) | 38 | 3 | 11% | -1.302% | -2.402% | -2.549% | -21.08 € |
| macd_sin_salida | 909.89 € (-1.55%) | 52 | 9 | 35% | -0.228% | -1.224% | -1.372% | -14.71 € |
| c_banda_atr_tope | 923.65 € (-0.06%) | 9 | 5 | 56% | +0.446% | -0.654% | -0.837% | -1.36 € |
| ruptura_volumen_tope | 921.58 € (-0.29%) | 9 | 5 | 22% | -0.373% | -1.473% | -1.564% | -3.06 € |
| c_banda_atr_regimen | 914.76 € (-1.03%) | 30 | 7 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| macd_momentum_regimen | 912.77 € (-1.24%) | 50 | 4 | 30% | +0.002% | -1.020% | -1.162% | -11.78 € |
| ruptura_volumen_regimen | 904.96 € (-2.09%) | 52 | 4 | 15% | -0.649% | -1.651% | -1.798% | -19.76 € |
| c_banda_atr_evento | 926.12 € (+0.20%) | 2 | 9 | 100% | +2.000% | +0.900% | +0.614% | +0.42 € |
| macd_momentum_evento | 923.08 € (-0.13%) | 9 | 7 | 44% | +0.227% | -0.873% | -1.060% | -1.82 € |
| ruptura_volumen_evento | 924.11 € (-0.01%) | 1 | 5 | 0% | -1.200% | -2.300% | -2.340% | -0.53 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 16:15 | ruptura_volumen_evento | MON | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 16:15 | ruptura_volumen_regimen | MON | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 16:15 | estocastico_rebote | ENA | take-profit | +1.80% | +1.30% | +0.30 |
| 2026-09-30 16:15 | ruptura_volumen | MON | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 16:10 | macd_momentum_evento | SPX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:10 | macd_momentum_evento | MON | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:10 | c_banda_atr_evento | SPX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:10 | macd_momentum_regimen | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 16:10 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 16:10 | estocastico_rebote | NIGHT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 16:10 | estocastico_rebote | WLD | take-profit | +2.13% | +1.63% | +0.37 |
| 2026-09-30 16:10 | estocastico_rebote | TAO | take-profit | +1.83% | +1.03% | +0.24 |
| 2026-09-30 16:10 | estocastico_rebote | ZEC | take-profit | +1.80% | +1.30% | +0.26 |
| 2026-09-30 16:10 | estocastico_rebote | ADA | take-profit | +1.80% | +1.30% | +0.30 |
| 2026-09-30 16:10 | macd_momentum | SPX | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-09-30 16:10 [ruptura_volumen] ENTRADA SUI @ 1.0544 (22.63 €, apertura)
- 2026-09-30 16:10 [ruptura_volumen_tope] ENTRADA SUI @ 1.0544 (23.03 €, apertura)
- 2026-09-30 16:10 [ruptura_volumen_regimen] ENTRADA SUI @ 1.0544 (22.62 €, apertura)
- 2026-09-30 16:10 [ruptura_volumen_evento] ENTRADA SUI @ 1.0544 (23.11 €, apertura)
- 2026-09-30 16:15 [estocastico_rebote] CIERRE ENA take-profit bruto +1.80% neto +1.30%
- 2026-09-30 16:10 [ruptura_volumen] ENTRADA MON @ 0.0251 (22.63 €, apertura)
- 2026-09-30 16:15 [ruptura_volumen] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 16:10 [ruptura_estricta] ENTRADA MON @ 0.0251 (22.58 €, apertura)
- 2026-09-30 16:10 [ruptura_volumen_regimen] ENTRADA MON @ 0.0251 (22.62 €, apertura)
- 2026-09-30 16:15 [ruptura_volumen_regimen] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 16:10 [ruptura_volumen_evento] ENTRADA MON @ 0.0251 (23.11 €, apertura)
- 2026-09-30 16:15 [ruptura_volumen_evento] CIERRE MON stop-loss bruto -1.20% neto -2.30%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
