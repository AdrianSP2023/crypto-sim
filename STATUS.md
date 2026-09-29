# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 13:21 UTC · vueltas 45 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 925.27 € (+0.11%) | 10 | 24 | 90% | +1.650% | +0.550% | +0.427% | +1.27 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 919.19 € (-0.55%) | 35 | 19 | 34% | +0.345% | -0.746% | -0.887% | -6.03 € |
| rebote_extremo | 924.45 € (+0.02%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 920.28 € (-0.43%) | 26 | 12 | 38% | +0.382% | -0.718% | -0.833% | -4.31 € |
| macd_momentum | 910.28 € (-1.51%) | 90 | 10 | 20% | +0.068% | -0.722% | -0.835% | -14.97 € |
| estocastico_rebote | 926.16 € (+0.21%) | 28 | 36 | 75% | +1.019% | -0.060% | -0.195% | -0.38 € |
| ruptura_estricta | 921.69 € (-0.28%) | 20 | 14 | 35% | +0.299% | -0.801% | -0.935% | -3.70 € |
| macd_sin_salida | 918.71 € (-0.60%) | 44 | 20 | 41% | +0.466% | -0.545% | -0.668% | -5.54 € |
| c_banda_atr_tope | 924.39 € (+0.02%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 923.03 € (-0.13%) | 10 | 5 | 30% | +0.387% | -0.713% | -0.836% | -1.65 € |
| c_banda_atr_regimen | 925.27 € (+0.11%) | 10 | 24 | 90% | +1.650% | +0.550% | +0.427% | +1.27 € |
| macd_momentum_regimen | 910.28 € (-1.51%) | 90 | 10 | 20% | +0.068% | -0.722% | -0.835% | -14.97 € |
| ruptura_volumen_regimen | 919.19 € (-0.55%) | 35 | 19 | 34% | +0.345% | -0.746% | -0.887% | -6.03 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 13:20 | ruptura_volumen_regimen | FET | stop-loss | -1.24% | -2.04% | -0.47 |
| 2026-09-29 13:20 | macd_momentum_regimen | PEPE | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 13:20 | c_banda_atr_regimen | PEPE | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 13:20 | estocastico_rebote | TON | stop-loss | -1.80% | -2.60% | -0.60 |
| 2026-09-29 13:20 | estocastico_rebote | MINA | stop-loss | -1.57% | -2.37% | -0.55 |
| 2026-09-29 13:20 | macd_momentum | PEPE | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 13:20 | ruptura_volumen | FET | stop-loss | -1.24% | -2.04% | -0.47 |
| 2026-09-29 13:20 | c_banda_atr | PEPE | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 13:15 | macd_momentum_regimen | MON | momentum perdido | -0.20% | -0.69% | -0.16 |
| 2026-09-29 13:15 | macd_momentum | MON | momentum perdido | -0.20% | -0.69% | -0.16 |
| 2026-09-29 13:10 | macd_momentum_regimen | SPX | momentum perdido | +0.63% | +0.13% | +0.03 |
| 2026-09-29 13:10 | c_banda_atr_regimen | TRUMP | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 13:10 | ruptura_estricta | RAY | timeout | -0.70% | -1.80% | -0.42 |
| 2026-09-29 13:10 | estocastico_rebote | SHIB | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-29 13:10 | macd_momentum | SPX | momentum perdido | +0.63% | +0.13% | +0.03 |

## Eventos de la última vuelta

- 2026-09-29 13:15 [macd_sin_salida] ENTRADA DOGE @ 0.0845729 (22.97 €, apertura)
- 2026-09-29 13:20 [c_banda_atr] CIERRE PEPE take-profit bruto +2.00% neto +0.90%
- 2026-09-29 13:20 [macd_momentum] CIERRE PEPE take-profit bruto +2.00% neto +1.50%
- 2026-09-29 13:20 [c_banda_atr_regimen] CIERRE PEPE take-profit bruto +2.00% neto +0.90%
- 2026-09-29 13:20 [macd_momentum_regimen] CIERRE PEPE take-profit bruto +2.00% neto +1.50%
- 2026-09-29 13:20 [estocastico_rebote] CIERRE MINA stop-loss bruto -1.57% neto -2.37%
- 2026-09-29 13:20 [estocastico_rebote] CIERRE TON stop-loss bruto -1.80% neto -2.60%
- 2026-09-29 13:15 [macd_momentum] ENTRADA SPX @ 0.3703 (22.73 €, apertura)
- 2026-09-29 13:15 [macd_sin_salida] ENTRADA SPX @ 0.3703 (22.97 €, apertura)
- 2026-09-29 13:15 [macd_momentum_regimen] ENTRADA SPX @ 0.3703 (22.73 €, apertura)
- 2026-09-29 13:20 [ruptura_volumen] CIERRE FET stop-loss bruto -1.24% neto -2.04%
- 2026-09-29 13:20 [ruptura_volumen_regimen] CIERRE FET stop-loss bruto -1.24% neto -2.04%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
