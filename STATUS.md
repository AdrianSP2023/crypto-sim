# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 22:26 UTC · vueltas 153 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.76 € (-1.89%) | 67 | 19 | 31% | -0.193% | -1.083% | -1.230% | -16.71 € |
| reversion_bb | 917.70 € (-0.71%) | 18 | 3 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 903.57 € (-2.24%) | 105 | 7 | 24% | -0.127% | -0.876% | -1.005% | -21.07 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.59 € (-2.02%) | 83 | 3 | 23% | -0.173% | -0.988% | -1.111% | -18.79 € |
| macd_momentum | 892.07 € (-3.48%) | 189 | 16 | 17% | -0.106% | -0.744% | -0.860% | -32.04 € |
| estocastico_rebote | 892.78 € (-3.40%) | 156 | 13 | 31% | -0.219% | -0.886% | -1.007% | -31.59 € |
| ruptura_estricta | 909.86 € (-1.56%) | 46 | 7 | 28% | -0.245% | -1.313% | -1.447% | -13.90 € |
| macd_sin_salida | 902.17 € (-2.39%) | 104 | 33 | 32% | -0.095% | -0.846% | -0.978% | -20.17 € |
| c_banda_atr_tope | 913.15 € (-1.20%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 915.45 € (-0.95%) | 33 | 4 | 15% | -0.071% | -1.171% | -1.287% | -8.90 € |
| c_banda_atr_regimen | 908.06 € (-1.75%) | 53 | 9 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.80 € (-3.29%) | 173 | 0 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 906.52 € (-1.92%) | 87 | 5 | 24% | -0.088% | -0.888% | -1.018% | -17.72 € |
| c_banda_atr_evento | 911.17 € (-1.41%) | 35 | 19 | 26% | -0.434% | -1.525% | -1.688% | -12.29 € |
| macd_momentum_evento | 904.61 € (-2.12%) | 69 | 16 | 10% | -0.348% | -1.231% | -1.348% | -19.50 € |
| ruptura_volumen_evento | 909.34 € (-1.61%) | 46 | 7 | 13% | -0.392% | -1.446% | -1.579% | -15.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 22:25 | macd_momentum_evento | NIGHT | momentum perdido | -0.14% | -0.64% | -0.14 |
| 2026-09-29 22:25 | macd_momentum_evento | DOT | momentum perdido | -0.67% | -1.17% | -0.27 |
| 2026-09-29 22:25 | c_banda_atr_evento | WLD | timeout | -0.53% | -1.33% | -0.30 |
| 2026-09-29 22:25 | ruptura_volumen_regimen | BNB | timeout | +0.19% | -0.31% | -0.07 |
| 2026-09-29 22:25 | macd_momentum | NIGHT | momentum perdido | -0.14% | -0.64% | -0.14 |
| 2026-09-29 22:25 | macd_momentum | DOT | momentum perdido | -0.67% | -1.17% | -0.26 |
| 2026-09-29 22:25 | pullback_tendencia | INJ | rotura de tendencia | -0.16% | -0.66% | -0.15 |
| 2026-09-29 22:25 | c_banda_atr | WLD | timeout | -0.53% | -1.03% | -0.23 |
| 2026-09-29 22:20 | ruptura_volumen_evento | BNB | timeout | +0.19% | -0.61% | -0.14 |
| 2026-09-29 22:20 | ruptura_volumen_tope | BNB | timeout | +0.19% | -0.91% | -0.21 |
| 2026-09-29 22:20 | estocastico_rebote | USELESS | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-29 22:20 | pullback_tendencia | FIL | rotura de tendencia | -0.10% | -0.60% | -0.14 |
| 2026-09-29 22:20 | ruptura_volumen | BNB | timeout | +0.19% | -0.31% | -0.07 |
| 2026-09-29 22:15 | ruptura_volumen_evento | AVAX | timeout | +0.56% | -0.24% | -0.06 |
| 2026-09-29 22:15 | ruptura_volumen_tope | AVAX | timeout | +0.56% | -0.55% | -0.12 |

## Eventos de la última vuelta

- 2026-09-29 22:25 [macd_momentum] CIERRE DOT momentum perdido bruto -0.67% neto -1.17%
- 2026-09-29 22:25 [macd_momentum_evento] CIERRE DOT momentum perdido bruto -0.67% neto -1.17%
- 2026-09-29 22:20 [pullback_tendencia] ENTRADA INJ @ 6.806 (22.64 €, apertura)
- 2026-09-29 22:25 [pullback_tendencia] CIERRE INJ rotura de tendencia bruto -0.16% neto -0.66%
- 2026-09-29 22:25 [c_banda_atr] CIERRE WLD timeout bruto -0.53% neto -1.03%
- 2026-09-29 22:25 [c_banda_atr_evento] CIERRE WLD timeout bruto -0.53% neto -1.33%
- 2026-09-29 22:20 [macd_momentum] ENTRADA ZRO @ 1.441 (22.31 €, apertura)
- 2026-09-29 22:20 [macd_sin_salida] ENTRADA ZRO @ 1.441 (22.60 €, apertura)
- 2026-09-29 22:20 [macd_momentum_evento] ENTRADA ZRO @ 1.441 (22.62 €, apertura)
- 2026-09-29 22:25 [macd_momentum] CIERRE NIGHT momentum perdido bruto -0.14% neto -0.64%
- 2026-09-29 22:25 [macd_momentum_evento] CIERRE NIGHT momentum perdido bruto -0.14% neto -0.64%
- 2026-09-29 22:25 [ruptura_volumen_regimen] CIERRE BNB timeout bruto +0.19% neto -0.31%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
