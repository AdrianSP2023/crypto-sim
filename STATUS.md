# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 16:32 UTC · vueltas 82 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.48 € (-1.49%) | 51 | 3 | 33% | -0.182% | -1.194% | -1.334% | -14.06 € |
| reversion_bb | 922.27 € (-0.21%) | 5 | 10 | 20% | -0.900% | -2.000% | -2.120% | -2.31 € |
| ruptura_volumen | 909.99 € (-1.54%) | 69 | 1 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| rebote_extremo | 923.66 € (-0.06%) | 1 | 2 | 0% | -1.619% | -2.719% | -2.843% | -0.63 € |
| pullback_tendencia | 909.01 € (-1.65%) | 66 | 1 | 26% | -0.108% | -1.003% | -1.118% | -15.21 € |
| macd_momentum | 898.69 € (-2.76%) | 147 | 3 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| estocastico_rebote | 905.07 € (-2.07%) | 94 | 40 | 35% | -0.138% | -0.916% | -1.044% | -19.82 € |
| ruptura_estricta | 913.20 € (-1.19%) | 39 | 3 | 31% | -0.117% | -1.217% | -1.344% | -10.94 € |
| macd_sin_salida | 905.61 € (-2.02%) | 93 | 3 | 31% | -0.086% | -0.867% | -0.991% | -18.50 € |
| c_banda_atr_tope | 917.17 € (-0.76%) | 18 | 3 | 22% | -0.674% | -1.774% | -1.945% | -7.37 € |
| ruptura_volumen_tope | 919.76 € (-0.48%) | 20 | 1 | 20% | +0.103% | -0.997% | -1.127% | -4.60 € |
| c_banda_atr_regimen | 909.84 € (-1.56%) | 50 | 0 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| c_banda_atr_evento | 917.46 € (-0.73%) | 18 | 4 | 28% | -0.557% | -1.657% | -1.821% | -6.89 € |
| macd_momentum_evento | 913.65 € (-1.15%) | 27 | 3 | 15% | -0.576% | -1.676% | -1.793% | -10.46 € |
| ruptura_volumen_evento | 920.31 € (-0.43%) | 10 | 1 | 20% | -0.654% | -1.754% | -1.962% | -4.05 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 16:15 | c_banda_atr_evento | TON | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 16:15 | c_banda_atr_regimen | TON | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-29 16:15 | estocastico_rebote | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 16:15 | c_banda_atr | TON | stop-loss | -1.50% | -2.30% | -0.53 |
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

## Eventos de la última vuelta

- 2026-09-29 16:25 [ruptura_volumen] ENTRADA JUP @ 0.29238 (22.75 €, apertura)
- 2026-09-29 16:25 [ruptura_estricta] ENTRADA JUP @ 0.29238 (22.83 €, apertura)
- 2026-09-29 16:25 [ruptura_volumen_tope] ENTRADA JUP @ 0.29238 (22.99 €, apertura)
- 2026-09-29 16:25 [ruptura_volumen_evento] ENTRADA JUP @ 0.29238 (23.00 €, apertura)
- 2026-09-29 16:25 [macd_momentum] ENTRADA INJ @ 6.736 (22.47 €, apertura)
- 2026-09-29 16:25 [macd_sin_salida] ENTRADA INJ @ 6.736 (22.64 €, apertura)
- 2026-09-29 16:25 [macd_momentum_evento] ENTRADA INJ @ 6.736 (22.84 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
