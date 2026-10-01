# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 04:16 UTC · vueltas 122 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 905.99 € (-1.97%) | 112 | 25 | 31% | -0.090% | -0.823% | -0.944% | -21.16 € |
| reversion_bb | 921.58 € (-0.29%) | 14 | 4 | 36% | +0.190% | -0.910% | -1.026% | -2.94 € |
| ruptura_volumen | 891.50 € (-3.54%) | 146 | 28 | 19% | -0.333% | -1.011% | -1.123% | -33.67 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 902.99 € (-2.30%) | 87 | 6 | 16% | -0.297% | -1.101% | -1.219% | -21.92 € |
| macd_momentum | 897.21 € (-2.92%) | 199 | 32 | 21% | -0.037% | -0.668% | -0.778% | -30.29 € |
| estocastico_rebote | 903.19 € (-2.28%) | 155 | 15 | 37% | +0.057% | -0.611% | -0.732% | -21.80 € |
| ruptura_estricta | 901.50 € (-2.46%) | 71 | 26 | 24% | -0.611% | -1.483% | -1.620% | -24.25 € |
| macd_sin_salida | 905.81 € (-1.99%) | 137 | 33 | 39% | +0.027% | -0.664% | -0.779% | -20.91 € |
| c_banda_atr_tope | 917.96 € (-0.68%) | 27 | 5 | 30% | +0.046% | -1.054% | -1.177% | -6.56 € |
| ruptura_volumen_tope | 914.60 € (-1.04%) | 41 | 5 | 22% | +0.040% | -1.060% | -1.161% | -10.00 € |
| c_banda_atr_regimen | 910.43 € (-1.49%) | 58 | 23 | 29% | -0.244% | -1.194% | -1.339% | -15.95 € |
| macd_momentum_regimen | 906.31 € (-1.94%) | 113 | 32 | 20% | -0.088% | -0.819% | -0.938% | -21.22 € |
| ruptura_volumen_regimen | 892.30 € (-3.46%) | 118 | 30 | 14% | -0.499% | -1.220% | -1.338% | -32.84 € |
| c_banda_atr_evento | 912.02 € (-1.32%) | 79 | 25 | 32% | +0.002% | -0.832% | -0.937% | -15.15 € |
| macd_momentum_evento | 902.18 € (-2.39%) | 152 | 32 | 16% | -0.057% | -0.731% | -0.832% | -25.34 € |
| ruptura_volumen_evento | 904.19 € (-2.17%) | 96 | 28 | 19% | -0.179% | -0.954% | -1.047% | -21.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 04:15 | macd_momentum_evento | ICP | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-10-01 04:15 | macd_momentum_evento | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 04:15 | c_banda_atr_evento | WLD | timeout | -0.04% | -0.54% | -0.12 |
| 2026-10-01 04:15 | macd_momentum_regimen | ICP | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-10-01 04:15 | macd_momentum_regimen | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 04:15 | macd_sin_salida | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 04:15 | macd_momentum | ICP | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-10-01 04:15 | macd_momentum | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 04:15 | pullback_tendencia | QNT | rotura de tendencia | -1.30% | -1.80% | -0.41 |
| 2026-10-01 04:15 | c_banda_atr | WLD | timeout | -0.04% | -0.54% | -0.12 |
| 2026-10-01 04:10 | ruptura_volumen_evento | ETH | timeout | +0.12% | -0.38% | -0.09 |
| 2026-10-01 04:10 | macd_momentum_evento | WLD | momentum perdido | -0.71% | -1.21% | -0.27 |
| 2026-10-01 04:10 | macd_momentum_regimen | WLD | momentum perdido | -0.71% | -1.21% | -0.27 |
| 2026-10-01 04:10 | macd_momentum | WLD | momentum perdido | -0.71% | -1.21% | -0.27 |
| 2026-10-01 04:10 | ruptura_volumen | ETH | timeout | +0.12% | -0.38% | -0.09 |

## Eventos de la última vuelta

- 2026-10-01 04:15 [pullback_tendencia] CIERRE QNT rotura de tendencia bruto -1.30% neto -1.80%
- 2026-10-01 04:15 [macd_momentum] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 04:15 [macd_sin_salida] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 04:15 [macd_momentum_regimen] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 04:15 [macd_momentum_evento] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 04:10 [ruptura_volumen] ENTRADA PUMP @ 0.00512 (22.26 €, apertura)
- 2026-10-01 04:10 [ruptura_volumen_regimen] ENTRADA PUMP @ 0.00512 (22.28 €, apertura)
- 2026-10-01 04:10 [ruptura_volumen_evento] ENTRADA PUMP @ 0.00512 (22.58 €, apertura)
- 2026-10-01 04:15 [macd_momentum] CIERRE ICP momentum perdido bruto -0.20% neto -0.70%
- 2026-10-01 04:15 [macd_momentum_regimen] CIERRE ICP momentum perdido bruto -0.20% neto -0.70%
- 2026-10-01 04:15 [macd_momentum_evento] CIERRE ICP momentum perdido bruto -0.20% neto -0.70%
- 2026-10-01 04:10 [macd_momentum] ENTRADA CRV @ 0.35149 (22.35 €, apertura)
- 2026-10-01 04:10 [macd_sin_salida] ENTRADA CRV @ 0.35149 (22.58 €, apertura)
- 2026-10-01 04:10 [macd_momentum_regimen] ENTRADA CRV @ 0.35149 (22.58 €, apertura)
- 2026-10-01 04:10 [macd_momentum_evento] ENTRADA CRV @ 0.35149 (22.47 €, apertura)
- 2026-10-01 04:15 [c_banda_atr] CIERRE WLD timeout bruto -0.04% neto -0.54%
- 2026-10-01 04:15 [c_banda_atr_evento] CIERRE WLD timeout bruto -0.04% neto -0.54%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
