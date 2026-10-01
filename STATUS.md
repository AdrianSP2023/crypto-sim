# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 04:06 UTC · vueltas 120 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.37 € (-1.93%) | 111 | 25 | 32% | -0.090% | -0.825% | -0.946% | -21.04 € |
| reversion_bb | 921.55 € (-0.29%) | 14 | 4 | 36% | +0.190% | -0.910% | -1.026% | -2.94 € |
| ruptura_volumen | 891.97 € (-3.49%) | 145 | 26 | 19% | -0.336% | -1.016% | -1.129% | -33.59 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.53 € (-2.24%) | 86 | 7 | 16% | -0.285% | -1.092% | -1.210% | -21.51 € |
| macd_momentum | 897.99 € (-2.84%) | 196 | 33 | 21% | -0.025% | -0.658% | -0.767% | -29.42 € |
| estocastico_rebote | 903.35 € (-2.26%) | 155 | 15 | 37% | +0.057% | -0.611% | -0.732% | -21.80 € |
| ruptura_estricta | 901.87 € (-2.42%) | 71 | 24 | 24% | -0.611% | -1.483% | -1.620% | -24.25 € |
| macd_sin_salida | 906.51 € (-1.92%) | 136 | 33 | 39% | +0.038% | -0.654% | -0.769% | -20.46 € |
| c_banda_atr_tope | 917.90 € (-0.69%) | 27 | 5 | 30% | +0.046% | -1.054% | -1.177% | -6.56 € |
| ruptura_volumen_tope | 914.90 € (-1.01%) | 41 | 5 | 22% | +0.040% | -1.060% | -1.161% | -10.00 € |
| c_banda_atr_regimen | 910.77 € (-1.46%) | 58 | 22 | 29% | -0.244% | -1.194% | -1.339% | -15.95 € |
| macd_momentum_regimen | 907.10 € (-1.85%) | 110 | 33 | 21% | -0.069% | -0.806% | -0.924% | -20.34 € |
| ruptura_volumen_regimen | 892.84 € (-3.40%) | 118 | 27 | 14% | -0.499% | -1.220% | -1.338% | -32.84 € |
| c_banda_atr_evento | 912.40 € (-1.28%) | 78 | 25 | 32% | +0.002% | -0.836% | -0.940% | -15.02 € |
| macd_momentum_evento | 902.97 € (-2.30%) | 149 | 33 | 16% | -0.042% | -0.719% | -0.819% | -24.46 € |
| ruptura_volumen_evento | 904.66 € (-2.12%) | 95 | 26 | 19% | -0.182% | -0.960% | -1.054% | -20.91 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 04:05 | macd_momentum_evento | WLFI | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-10-01 04:05 | macd_momentum_regimen | WLFI | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-10-01 04:05 | macd_sin_salida | SEI | timeout | +0.61% | +0.11% | +0.03 |
| 2026-10-01 04:05 | macd_momentum | WLFI | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-10-01 04:00 | ruptura_estricta | XMR | timeout | -0.02% | -0.52% | -0.12 |
| 2026-10-01 04:00 | pullback_tendencia | KAS | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 03:55 | macd_momentum_evento | XDC | stop-loss | -1.85% | -2.35% | -0.53 |
| 2026-10-01 03:55 | c_banda_atr_evento | TRX | timeout | +0.31% | -0.19% | -0.04 |
| 2026-10-01 03:55 | macd_momentum_regimen | XDC | stop-loss | -1.85% | -2.35% | -0.53 |
| 2026-10-01 03:55 | macd_sin_salida | XDC | stop-loss | -1.85% | -2.35% | -0.53 |
| 2026-10-01 03:55 | macd_momentum | XDC | stop-loss | -1.85% | -2.35% | -0.53 |
| 2026-10-01 03:55 | reversion_bb | BCH | timeout | +1.00% | -0.10% | -0.02 |
| 2026-10-01 03:55 | c_banda_atr | TRX | timeout | +0.31% | -0.19% | -0.04 |
| 2026-10-01 03:50 | macd_momentum_evento | PENGU | take-profit | +2.22% | +1.72% | +0.39 |
| 2026-10-01 03:50 | c_banda_atr_evento | PENGU | take-profit | +2.22% | +1.72% | +0.39 |

## Eventos de la última vuelta

- 2026-10-01 04:00 [ruptura_estricta] ENTRADA ETH @ 2378.21 (22.50 €, apertura)
- 2026-10-01 04:00 [ruptura_volumen_regimen] ENTRADA ETH @ 2378.21 (22.28 €, apertura)
- 2026-10-01 04:00 [c_banda_atr] ENTRADA POL @ 0.09994 (22.58 €, apertura)
- 2026-10-01 04:00 [c_banda_atr_regimen] ENTRADA POL @ 0.09994 (22.71 €, apertura)
- 2026-10-01 04:00 [c_banda_atr_evento] ENTRADA POL @ 0.09994 (22.73 €, apertura)
- 2026-10-01 04:00 [ruptura_volumen] ENTRADA FIL @ 0.932 (22.27 €, apertura)
- 2026-10-01 04:00 [ruptura_volumen_regimen] ENTRADA FIL @ 0.932 (22.28 €, apertura)
- 2026-10-01 04:00 [ruptura_volumen_evento] ENTRADA FIL @ 0.932 (22.58 €, apertura)
- 2026-10-01 04:05 [macd_momentum] CIERRE WLFI momentum perdido bruto -0.20% neto -0.70%
- 2026-10-01 04:05 [macd_momentum_regimen] CIERRE WLFI momentum perdido bruto -0.20% neto -0.70%
- 2026-10-01 04:05 [macd_momentum_evento] CIERRE WLFI momentum perdido bruto -0.20% neto -0.70%
- 2026-10-01 04:00 [ruptura_volumen] ENTRADA KAS @ 0.03927 (22.27 €, apertura)
- 2026-10-01 04:00 [ruptura_estricta] ENTRADA KAS @ 0.03927 (22.50 €, apertura)
- 2026-10-01 04:00 [ruptura_volumen_regimen] ENTRADA KAS @ 0.03927 (22.28 €, apertura)
- 2026-10-01 04:00 [ruptura_volumen_evento] ENTRADA KAS @ 0.03927 (22.58 €, apertura)
- 2026-10-01 04:05 [macd_sin_salida] CIERRE SEI timeout bruto +0.61% neto +0.11%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
