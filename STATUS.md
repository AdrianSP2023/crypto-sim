# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 00:41 UTC · vueltas 180 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.94 € (-2.74%) | 88 | 23 | 25% | -0.429% | -1.226% | -1.370% | -24.73 € |
| reversion_bb | 917.86 € (-0.69%) | 20 | 13 | 35% | -0.250% | -1.350% | -1.448% | -6.23 € |
| ruptura_volumen | 900.19 € (-2.60%) | 118 | 7 | 22% | -0.168% | -0.889% | -1.018% | -23.99 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.67 € (-2.12%) | 94 | 1 | 23% | -0.131% | -0.909% | -1.029% | -19.57 € |
| macd_momentum | 882.69 € (-4.50%) | 232 | 12 | 15% | -0.176% | -0.789% | -0.900% | -41.49 € |
| estocastico_rebote | 892.52 € (-3.43%) | 169 | 13 | 33% | -0.165% | -0.819% | -0.937% | -31.64 € |
| ruptura_estricta | 908.73 € (-1.68%) | 52 | 5 | 27% | -0.249% | -1.251% | -1.388% | -14.96 € |
| macd_sin_salida | 895.58 € (-3.10%) | 138 | 16 | 27% | -0.198% | -0.888% | -1.011% | -27.97 € |
| c_banda_atr_tope | 912.64 € (-1.26%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.35 € (-1.18%) | 40 | 5 | 15% | -0.097% | -1.197% | -1.319% | -11.01 € |
| c_banda_atr_regimen | 901.01 € (-2.51%) | 68 | 8 | 24% | -0.518% | -1.401% | -1.535% | -21.87 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.54 € (-2.24%) | 96 | 4 | 22% | -0.151% | -0.922% | -1.053% | -20.29 € |
| c_banda_atr_evento | 902.49 € (-2.35%) | 56 | 23 | 18% | -0.714% | -1.648% | -1.800% | -21.18 € |
| macd_momentum_evento | 895.09 € (-3.15%) | 112 | 12 | 8% | -0.401% | -1.137% | -1.244% | -29.08 € |
| ruptura_volumen_evento | 905.73 € (-2.00%) | 59 | 7 | 12% | -0.415% | -1.362% | -1.495% | -18.45 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 00:40 | estocastico_rebote | TRX | timeout | -0.13% | -0.63% | -0.14 |
| 2026-09-30 00:40 | estocastico_rebote | ICP | timeout | +0.89% | +0.39% | +0.09 |
| 2026-09-30 00:40 | estocastico_rebote | DOT | timeout | +0.00% | -0.50% | -0.11 |
| 2026-09-30 00:35 | c_banda_atr_evento | DASH | timeout | -1.30% | -2.10% | -0.48 |
| 2026-09-30 00:35 | c_banda_atr_regimen | DASH | timeout | -1.30% | -1.80% | -0.41 |
| 2026-09-30 00:35 | ruptura_estricta | ZRO | take-profit | +3.00% | +2.50% | +0.57 |
| 2026-09-30 00:35 | estocastico_rebote | NEAR | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 00:35 | c_banda_atr | DASH | timeout | -1.30% | -1.80% | -0.41 |
| 2026-09-30 00:30 | macd_momentum_evento | SHIB | momentum perdido | -0.55% | -1.05% | -0.23 |
| 2026-09-30 00:30 | macd_momentum_evento | ICP | momentum perdido | -0.36% | -0.86% | -0.19 |
| 2026-09-30 00:30 | macd_momentum | SHIB | momentum perdido | -0.55% | -1.05% | -0.23 |
| 2026-09-30 00:30 | macd_momentum | ICP | momentum perdido | -0.36% | -0.86% | -0.19 |
| 2026-09-30 00:30 | pullback_tendencia | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 00:30 | reversion_bb | ASTER | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-09-30 00:25 | ruptura_volumen_evento | RAY | stop-loss | -1.53% | -2.03% | -0.46 |

## Eventos de la última vuelta

- 2026-09-30 00:35 [macd_momentum] ENTRADA ZEC @ 1261.09 (22.07 €, apertura)
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA ZEC @ 1261.09 (22.41 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA ZEC @ 1261.09 (22.38 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA HYPE @ 76.09 (22.07 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA HYPE @ 76.09 (22.38 €, apertura)
- 2026-09-30 00:35 [c_banda_atr] ENTRADA ARB @ 0.1794 (22.49 €, apertura)
- 2026-09-30 00:35 [c_banda_atr_evento] ENTRADA ARB @ 0.1794 (22.58 €, apertura)
- 2026-09-30 00:35 [c_banda_atr] ENTRADA ONDO @ 0.44528 (22.49 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA ONDO @ 0.44528 (22.07 €, apertura)
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA ONDO @ 0.44528 (22.41 €, apertura)
- 2026-09-30 00:35 [c_banda_atr_evento] ENTRADA ONDO @ 0.44528 (22.58 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA ONDO @ 0.44528 (22.38 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA DOT @ 1.0525 (22.07 €, apertura)
- 2026-09-30 00:40 [estocastico_rebote] CIERRE DOT timeout bruto +0.00% neto -0.50%
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA DOT @ 1.0525 (22.41 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA DOT @ 1.0525 (22.38 €, apertura)
- 2026-09-30 00:35 [c_banda_atr] ENTRADA JUP @ 0.29344 (22.49 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA JUP @ 0.29344 (22.07 €, apertura)
- 2026-09-30 00:35 [estocastico_rebote] ENTRADA JUP @ 0.29344 (22.32 €, apertura)
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA JUP @ 0.29344 (22.41 €, apertura)
- 2026-09-30 00:35 [c_banda_atr_evento] ENTRADA JUP @ 0.29344 (22.58 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA JUP @ 0.29344 (22.38 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA ICP @ 3.061 (22.07 €, apertura)
- 2026-09-30 00:40 [estocastico_rebote] CIERRE ICP timeout bruto +0.89% neto +0.39%
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA ICP @ 3.061 (22.38 €, apertura)
- 2026-09-30 00:40 [estocastico_rebote] CIERRE TRX timeout bruto -0.13% neto -0.63%
- 2026-09-30 00:35 [c_banda_atr] ENTRADA WLD @ 0.4293 (22.49 €, apertura)
- 2026-09-30 00:35 [c_banda_atr_evento] ENTRADA WLD @ 0.4293 (22.58 €, apertura)
- 2026-09-30 00:35 [ruptura_volumen] ENTRADA ZRO @ 1.526 (22.51 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA ZRO @ 1.526 (22.07 €, apertura)
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA ZRO @ 1.526 (22.41 €, apertura)
- 2026-09-30 00:35 [ruptura_volumen_tope] ENTRADA ZRO @ 1.526 (22.83 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA ZRO @ 1.526 (22.38 €, apertura)
- 2026-09-30 00:35 [ruptura_volumen_evento] ENTRADA ZRO @ 1.526 (22.64 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA USELESS @ 0.21256 (22.07 €, apertura)
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA USELESS @ 0.21256 (22.41 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA USELESS @ 0.21256 (22.38 €, apertura)
- 2026-09-30 00:35 [c_banda_atr] ENTRADA SPX @ 0.3692 (22.49 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA SPX @ 0.3692 (22.07 €, apertura)
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA SPX @ 0.3692 (22.41 €, apertura)
- 2026-09-30 00:35 [c_banda_atr_evento] ENTRADA SPX @ 0.3692 (22.58 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA SPX @ 0.3692 (22.38 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
