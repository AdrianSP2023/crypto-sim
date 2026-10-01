# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 03:56 UTC · vueltas 118 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.31 € (-1.94%) | 111 | 24 | 32% | -0.090% | -0.825% | -0.946% | -21.04 € |
| reversion_bb | 921.55 € (-0.29%) | 14 | 4 | 36% | +0.190% | -0.910% | -1.026% | -2.94 € |
| ruptura_volumen | 891.93 € (-3.50%) | 145 | 23 | 19% | -0.336% | -1.016% | -1.129% | -33.59 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.60 € (-2.23%) | 85 | 7 | 15% | -0.312% | -1.123% | -1.240% | -21.85 € |
| macd_momentum | 897.86 € (-2.85%) | 195 | 32 | 21% | -0.024% | -0.658% | -0.766% | -29.26 € |
| estocastico_rebote | 903.24 € (-2.27%) | 155 | 14 | 37% | +0.057% | -0.611% | -0.732% | -21.80 € |
| ruptura_estricta | 902.11 € (-2.39%) | 70 | 19 | 24% | -0.619% | -1.496% | -1.635% | -24.13 € |
| macd_sin_salida | 906.32 € (-1.94%) | 135 | 33 | 39% | +0.034% | -0.660% | -0.775% | -20.48 € |
| c_banda_atr_tope | 917.77 € (-0.70%) | 27 | 5 | 30% | +0.046% | -1.054% | -1.177% | -6.56 € |
| ruptura_volumen_tope | 914.95 € (-1.00%) | 41 | 5 | 22% | +0.040% | -1.060% | -1.161% | -10.00 € |
| c_banda_atr_regimen | 910.78 € (-1.46%) | 58 | 21 | 29% | -0.244% | -1.194% | -1.339% | -15.95 € |
| macd_momentum_regimen | 906.96 € (-1.87%) | 109 | 32 | 21% | -0.068% | -0.807% | -0.923% | -20.18 € |
| ruptura_volumen_regimen | 892.82 € (-3.40%) | 118 | 23 | 14% | -0.499% | -1.220% | -1.338% | -32.84 € |
| c_banda_atr_evento | 912.34 € (-1.29%) | 78 | 24 | 32% | +0.002% | -0.836% | -0.940% | -15.02 € |
| macd_momentum_evento | 902.83 € (-2.32%) | 148 | 32 | 16% | -0.041% | -0.719% | -0.818% | -24.30 € |
| ruptura_volumen_evento | 904.62 € (-2.12%) | 95 | 23 | 19% | -0.182% | -0.960% | -1.054% | -20.91 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-01 03:50 | ruptura_estricta | FET | timeout | +0.73% | +0.23% | +0.05 |
| 2026-10-01 03:50 | macd_momentum | PENGU | take-profit | +2.22% | +1.72% | +0.39 |

## Eventos de la última vuelta

- 2026-10-01 03:55 [c_banda_atr] CIERRE TRX timeout bruto +0.31% neto -0.19%
- 2026-10-01 03:55 [c_banda_atr_evento] CIERRE TRX timeout bruto +0.31% neto -0.19%
- 2026-10-01 03:55 [macd_momentum] CIERRE XDC stop-loss bruto -1.85% neto -2.35%
- 2026-10-01 03:55 [macd_sin_salida] CIERRE XDC stop-loss bruto -1.85% neto -2.35%
- 2026-10-01 03:55 [macd_momentum_regimen] CIERRE XDC stop-loss bruto -1.85% neto -2.35%
- 2026-10-01 03:55 [macd_momentum_evento] CIERRE XDC stop-loss bruto -1.85% neto -2.35%
- 2026-10-01 03:55 [reversion_bb] CIERRE BCH timeout bruto +1.00% neto -0.10%
- 2026-10-01 03:50 [macd_momentum] ENTRADA MON @ 0.02879 (22.37 €, apertura)
- 2026-10-01 03:50 [macd_momentum_regimen] ENTRADA MON @ 0.02879 (22.60 €, apertura)
- 2026-10-01 03:50 [macd_momentum_evento] ENTRADA MON @ 0.02879 (22.50 €, apertura)
- 2026-10-01 03:50 [ruptura_volumen] ENTRADA INJ @ 6.593 (22.27 €, apertura)
- 2026-10-01 03:50 [ruptura_volumen_regimen] ENTRADA INJ @ 6.593 (22.28 €, apertura)
- 2026-10-01 03:50 [ruptura_volumen_evento] ENTRADA INJ @ 6.593 (22.58 €, apertura)
- 2026-10-01 03:50 [ruptura_volumen] ENTRADA DASH @ 53.619 (22.27 €, apertura)
- 2026-10-01 03:50 [ruptura_volumen_regimen] ENTRADA DASH @ 53.619 (22.28 €, apertura)
- 2026-10-01 03:50 [ruptura_volumen_evento] ENTRADA DASH @ 53.619 (22.58 €, apertura)
- 2026-10-01 03:50 [ruptura_estricta] ENTRADA SEI @ 0.06539 (22.50 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
