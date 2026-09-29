# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 16:12 UTC · vueltas 78 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.55 € (-1.48%) | 50 | 3 | 34% | -0.156% | -1.172% | -1.311% | -13.53 € |
| reversion_bb | 921.66 € (-0.28%) | 5 | 10 | 20% | -0.900% | -2.000% | -2.120% | -2.31 € |
| ruptura_volumen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| rebote_extremo | 923.45 € (-0.09%) | 1 | 2 | 0% | -1.619% | -2.719% | -2.843% | -0.63 € |
| pullback_tendencia | 909.06 € (-1.64%) | 66 | 1 | 26% | -0.108% | -1.003% | -1.118% | -15.21 € |
| macd_momentum | 898.88 € (-2.74%) | 147 | 1 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| estocastico_rebote | 903.50 € (-2.24%) | 93 | 40 | 35% | -0.124% | -0.904% | -1.032% | -19.37 € |
| ruptura_estricta | 913.05 € (-1.21%) | 39 | 2 | 31% | -0.117% | -1.217% | -1.344% | -10.94 € |
| macd_sin_salida | 905.81 € (-1.99%) | 93 | 1 | 31% | -0.086% | -0.867% | -0.991% | -18.50 € |
| c_banda_atr_tope | 916.98 € (-0.79%) | 18 | 2 | 22% | -0.674% | -1.774% | -1.945% | -7.37 € |
| ruptura_volumen_tope | 919.64 € (-0.50%) | 20 | 0 | 20% | +0.103% | -0.997% | -1.127% | -4.60 € |
| c_banda_atr_regimen | 910.10 € (-1.53%) | 49 | 1 | 33% | -0.200% | -1.227% | -1.362% | -13.87 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| c_banda_atr_evento | 917.51 € (-0.73%) | 17 | 4 | 29% | -0.501% | -1.601% | -1.765% | -6.29 € |
| macd_momentum_evento | 913.85 € (-1.12%) | 27 | 1 | 15% | -0.576% | -1.676% | -1.793% | -10.46 € |
| ruptura_volumen_evento | 920.19 € (-0.44%) | 10 | 0 | 20% | -0.654% | -1.754% | -1.962% | -4.05 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 16:05 | c_banda_atr_evento | QNT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 16:05 | c_banda_atr_tope | QNT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 16:05 | c_banda_atr | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 15:55 | ruptura_estricta | TRUMP | timeout | -0.77% | -1.87% | -0.43 |
| 2026-09-29 15:55 | ruptura_estricta | NIGHT | stop-loss | -2.00% | -3.10% | -0.71 |
| 2026-09-29 15:55 | estocastico_rebote | MON | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 15:55 | pullback_tendencia | NIGHT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 15:50 | estocastico_rebote | POL | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-29 15:50 | rebote_extremo | VVV | timeout | -1.62% | -2.72% | -0.63 |
| 2026-09-29 15:50 | reversion_bb | JUP | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-09-29 15:40 | estocastico_rebote | HYPE | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 15:35 | c_banda_atr_regimen | BNB | timeout | -1.20% | -2.00% | -0.46 |
| 2026-09-29 15:35 | c_banda_atr_regimen | SOL | timeout | -1.07% | -1.87% | -0.43 |
| 2026-09-29 15:35 | c_banda_atr | BNB | timeout | -1.20% | -2.00% | -0.46 |
| 2026-09-29 15:35 | c_banda_atr | SOL | timeout | -1.07% | -1.87% | -0.43 |

## Eventos de la última vuelta

- 2026-09-29 16:05 [macd_momentum] ENTRADA MINA @ 0.1328 (22.47 €, apertura)
- 2026-09-29 16:05 [macd_sin_salida] ENTRADA MINA @ 0.1328 (22.64 €, apertura)
- 2026-09-29 16:05 [macd_momentum_evento] ENTRADA MINA @ 0.1328 (22.84 €, apertura)
- 2026-09-29 16:05 [estocastico_rebote] ENTRADA NIGHT @ 0.02828 (22.48 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
