# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 22:46 UTC · vueltas 157 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 905.37 € (-2.04%) | 68 | 20 | 31% | -0.213% | -1.096% | -1.242% | -17.16 € |
| reversion_bb | 917.73 € (-0.70%) | 18 | 3 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 903.03 € (-2.30%) | 108 | 4 | 23% | -0.128% | -0.869% | -0.997% | -21.50 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.28 € (-2.05%) | 85 | 3 | 22% | -0.181% | -0.988% | -1.111% | -19.25 € |
| macd_momentum | 890.77 € (-3.62%) | 197 | 10 | 17% | -0.114% | -0.746% | -0.863% | -33.48 € |
| estocastico_rebote | 892.60 € (-3.42%) | 156 | 14 | 31% | -0.219% | -0.886% | -1.007% | -31.59 € |
| ruptura_estricta | 909.24 € (-1.62%) | 47 | 6 | 28% | -0.283% | -1.338% | -1.473% | -14.47 € |
| macd_sin_salida | 901.15 € (-2.50%) | 104 | 35 | 32% | -0.095% | -0.846% | -0.978% | -20.17 € |
| c_banda_atr_tope | 912.82 € (-1.24%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 914.95 € (-1.01%) | 34 | 3 | 15% | -0.070% | -1.170% | -1.287% | -9.16 € |
| c_banda_atr_regimen | 907.47 € (-1.81%) | 53 | 9 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.80 € (-3.29%) | 173 | 0 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 905.86 € (-1.99%) | 90 | 2 | 23% | -0.089% | -0.879% | -1.008% | -18.16 € |
| c_banda_atr_evento | 909.70 € (-1.57%) | 36 | 20 | 25% | -0.463% | -1.547% | -1.706% | -12.82 € |
| macd_momentum_evento | 903.29 € (-2.27%) | 77 | 10 | 9% | -0.344% | -1.187% | -1.304% | -20.96 € |
| ruptura_volumen_evento | 908.59 € (-1.69%) | 49 | 4 | 12% | -0.376% | -1.415% | -1.546% | -15.94 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 22:45 | ruptura_volumen_evento | BCH | timeout | -0.15% | -0.95% | -0.22 |
| 2026-09-29 22:45 | macd_momentum_evento | XLM | momentum perdido | -0.28% | -0.78% | -0.18 |
| 2026-09-29 22:45 | ruptura_volumen_regimen | BCH | timeout | -0.15% | -0.65% | -0.15 |
| 2026-09-29 22:45 | macd_momentum | XLM | momentum perdido | -0.28% | -0.78% | -0.17 |
| 2026-09-29 22:45 | ruptura_volumen | BCH | timeout | -0.15% | -0.65% | -0.15 |
| 2026-09-29 22:40 | macd_momentum_evento | ENA | momentum perdido | -0.14% | -0.64% | -0.14 |
| 2026-09-29 22:40 | macd_momentum_evento | DASH | momentum perdido | -0.38% | -0.88% | -0.20 |
| 2026-09-29 22:40 | macd_momentum_evento | DOGE | momentum perdido | -0.02% | -0.52% | -0.12 |
| 2026-09-29 22:40 | macd_momentum | ENA | momentum perdido | -0.14% | -0.64% | -0.14 |
| 2026-09-29 22:40 | macd_momentum | DASH | momentum perdido | -0.38% | -0.88% | -0.20 |
| 2026-09-29 22:40 | macd_momentum | DOGE | momentum perdido | -0.02% | -0.52% | -0.12 |
| 2026-09-29 22:35 | ruptura_volumen_evento | SPX | timeout | -0.05% | -0.85% | -0.20 |
| 2026-09-29 22:35 | ruptura_volumen_evento | XLM | timeout | -0.21% | -1.01% | -0.23 |
| 2026-09-29 22:35 | macd_momentum_evento | POL | momentum perdido | -0.50% | -1.00% | -0.23 |
| 2026-09-29 22:35 | macd_momentum_evento | ARB | momentum perdido | -0.55% | -1.05% | -0.24 |

## Eventos de la última vuelta

- 2026-09-29 22:45 [macd_momentum] CIERRE XLM momentum perdido bruto -0.28% neto -0.78%
- 2026-09-29 22:45 [macd_momentum_evento] CIERRE XLM momentum perdido bruto -0.28% neto -0.78%
- 2026-09-29 22:40 [macd_momentum] ENTRADA AAVE @ 146.93 (22.27 €, apertura)
- 2026-09-29 22:40 [macd_sin_salida] ENTRADA AAVE @ 146.93 (22.60 €, apertura)
- 2026-09-29 22:40 [macd_momentum_evento] ENTRADA AAVE @ 146.93 (22.58 €, apertura)
- 2026-09-29 22:40 [c_banda_atr] ENTRADA MON @ 0.02394 (22.68 €, apertura)
- 2026-09-29 22:40 [c_banda_atr_evento] ENTRADA MON @ 0.02394 (22.79 €, apertura)
- 2026-09-29 22:45 [ruptura_volumen] CIERRE BCH timeout bruto -0.15% neto -0.65%
- 2026-09-29 22:45 [ruptura_volumen_regimen] CIERRE BCH timeout bruto -0.15% neto -0.65%
- 2026-09-29 22:45 [ruptura_volumen_evento] CIERRE BCH timeout bruto -0.15% neto -0.95%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
