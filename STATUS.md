# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 04:01 UTC · vueltas 119 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.47 € (-1.92%) | 111 | 24 | 32% | -0.090% | -0.825% | -0.946% | -21.04 € |
| reversion_bb | 921.53 € (-0.29%) | 14 | 4 | 36% | +0.190% | -0.910% | -1.026% | -2.94 € |
| ruptura_volumen | 891.93 € (-3.50%) | 145 | 24 | 19% | -0.336% | -1.016% | -1.129% | -33.59 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.38 € (-2.26%) | 86 | 7 | 16% | -0.285% | -1.092% | -1.210% | -21.51 € |
| macd_momentum | 898.20 € (-2.82%) | 195 | 34 | 21% | -0.024% | -0.658% | -0.766% | -29.26 € |
| estocastico_rebote | 903.26 € (-2.27%) | 155 | 15 | 37% | +0.057% | -0.611% | -0.732% | -21.80 € |
| ruptura_estricta | 901.93 € (-2.41%) | 71 | 22 | 24% | -0.611% | -1.483% | -1.620% | -24.25 € |
| macd_sin_salida | 906.60 € (-1.91%) | 135 | 34 | 39% | +0.034% | -0.660% | -0.775% | -20.48 € |
| c_banda_atr_tope | 917.72 € (-0.71%) | 27 | 5 | 30% | +0.046% | -1.054% | -1.177% | -6.56 € |
| ruptura_volumen_tope | 914.92 € (-1.01%) | 41 | 5 | 22% | +0.040% | -1.060% | -1.161% | -10.00 € |
| c_banda_atr_regimen | 910.80 € (-1.45%) | 58 | 21 | 29% | -0.244% | -1.194% | -1.339% | -15.95 € |
| macd_momentum_regimen | 907.31 € (-1.83%) | 109 | 34 | 21% | -0.068% | -0.807% | -0.923% | -20.18 € |
| ruptura_volumen_regimen | 892.80 € (-3.40%) | 118 | 24 | 14% | -0.499% | -1.220% | -1.338% | -32.84 € |
| c_banda_atr_evento | 912.51 € (-1.27%) | 78 | 24 | 32% | +0.002% | -0.836% | -0.940% | -15.02 € |
| macd_momentum_evento | 903.18 € (-2.28%) | 148 | 34 | 16% | -0.041% | -0.719% | -0.818% | -24.30 € |
| ruptura_volumen_evento | 904.62 € (-2.12%) | 95 | 24 | 19% | -0.182% | -0.960% | -1.054% | -20.91 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-01 03:50 | macd_momentum_regimen | PENGU | take-profit | +2.22% | +1.72% | +0.39 |
| 2026-10-01 03:50 | c_banda_atr_regimen | PENGU | take-profit | +2.22% | +1.72% | +0.39 |
| 2026-10-01 03:50 | macd_sin_salida | PENGU | take-profit | +2.22% | +1.72% | +0.39 |
| 2026-10-01 03:50 | ruptura_estricta | ONDO | timeout | +0.34% | -0.15% | -0.04 |

## Eventos de la última vuelta

- 2026-10-01 03:55 [ruptura_volumen] ENTRADA XRP @ 1.32449 (22.27 €, apertura)
- 2026-10-01 03:55 [ruptura_estricta] ENTRADA XRP @ 1.32449 (22.50 €, apertura)
- 2026-10-01 03:55 [ruptura_volumen_regimen] ENTRADA XRP @ 1.32449 (22.28 €, apertura)
- 2026-10-01 03:55 [ruptura_volumen_evento] ENTRADA XRP @ 1.32449 (22.58 €, apertura)
- 2026-10-01 03:55 [ruptura_estricta] ENTRADA SOL @ 104.61 (22.50 €, apertura)
- 2026-10-01 03:55 [pullback_tendencia] ENTRADA XLM @ 0.201566 (22.56 €, apertura)
- 2026-10-01 03:55 [macd_momentum] ENTRADA ARB @ 0.1807 (22.37 €, apertura)
- 2026-10-01 03:55 [macd_momentum_regimen] ENTRADA ARB @ 0.1807 (22.60 €, apertura)
- 2026-10-01 03:55 [macd_momentum_evento] ENTRADA ARB @ 0.1807 (22.50 €, apertura)
- 2026-10-01 03:55 [estocastico_rebote] ENTRADA ICP @ 3.016 (22.56 €, apertura)
- 2026-10-01 03:55 [ruptura_estricta] ENTRADA SHIB @ 5.129e-06 (22.50 €, apertura)
- 2026-10-01 03:55 [ruptura_estricta] ENTRADA DASH @ 53.567 (22.50 €, apertura)
- 2026-10-01 04:00 [pullback_tendencia] CIERRE KAS take-profit bruto +2.00% neto +1.50%
- 2026-10-01 03:55 [macd_momentum] ENTRADA KAS @ 0.03919 (22.37 €, apertura)
- 2026-10-01 03:55 [macd_sin_salida] ENTRADA KAS @ 0.03919 (22.59 €, apertura)
- 2026-10-01 03:55 [macd_momentum_regimen] ENTRADA KAS @ 0.03919 (22.60 €, apertura)
- 2026-10-01 03:55 [macd_momentum_evento] ENTRADA KAS @ 0.03919 (22.50 €, apertura)
- 2026-10-01 04:00 [ruptura_estricta] CIERRE XMR timeout bruto -0.02% neto -0.52%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
