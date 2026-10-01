# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 03:06 UTC · vueltas 108 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 904.18 € (-2.17%) | 104 | 27 | 29% | -0.202% | -0.953% | -1.076% | -22.73 € |
| reversion_bb | 921.38 € (-0.31%) | 13 | 5 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 891.31 € (-3.56%) | 137 | 13 | 18% | -0.386% | -1.077% | -1.193% | -33.63 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.35 € (-2.26%) | 82 | 5 | 16% | -0.314% | -1.136% | -1.257% | -21.34 € |
| macd_momentum | 897.90 € (-2.85%) | 181 | 25 | 21% | -0.036% | -0.680% | -0.789% | -28.10 € |
| estocastico_rebote | 903.14 € (-2.28%) | 150 | 17 | 37% | +0.043% | -0.631% | -0.753% | -21.77 € |
| ruptura_estricta | 899.46 € (-2.68%) | 63 | 19 | 17% | -0.812% | -1.731% | -1.871% | -25.10 € |
| macd_sin_salida | 904.01 € (-2.19%) | 122 | 35 | 35% | -0.051% | -0.765% | -0.881% | -21.44 € |
| c_banda_atr_tope | 917.66 € (-0.71%) | 25 | 5 | 24% | -0.111% | -1.211% | -1.337% | -6.98 € |
| ruptura_volumen_tope | 914.40 € (-1.06%) | 41 | 5 | 22% | +0.040% | -1.060% | -1.161% | -10.00 € |
| c_banda_atr_regimen | 909.01 € (-1.65%) | 53 | 21 | 26% | -0.396% | -1.389% | -1.541% | -16.93 € |
| macd_momentum_regimen | 906.44 € (-1.93%) | 97 | 23 | 21% | -0.087% | -0.856% | -0.974% | -19.07 € |
| ruptura_volumen_regimen | 892.09 € (-3.48%) | 110 | 13 | 14% | -0.551% | -1.288% | -1.409% | -32.34 € |
| c_banda_atr_evento | 910.20 € (-1.52%) | 71 | 27 | 28% | -0.152% | -1.024% | -1.131% | -16.72 € |
| macd_momentum_evento | 902.87 € (-2.31%) | 134 | 25 | 16% | -0.059% | -0.756% | -0.854% | -23.14 € |
| ruptura_volumen_evento | 903.99 € (-2.19%) | 87 | 13 | 17% | -0.248% | -1.051% | -1.148% | -20.96 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 03:05 | ruptura_volumen_evento | TRUMP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 03:05 | macd_momentum_evento | AAVE | take-profit | +2.02% | +1.52% | +0.34 |
| 2026-10-01 03:05 | ruptura_volumen_regimen | TRUMP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 03:05 | ruptura_volumen_tope | TRUMP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-10-01 03:05 | macd_sin_salida | ALGO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 03:05 | estocastico_rebote | ENA | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 03:05 | estocastico_rebote | LINK | timeout | +0.37% | -0.13% | -0.03 |
| 2026-10-01 03:05 | macd_momentum | AAVE | take-profit | +2.02% | +1.52% | +0.34 |
| 2026-10-01 03:05 | ruptura_volumen | TRUMP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 03:00 | ruptura_volumen_evento | XMR | timeout | -0.02% | -0.52% | -0.12 |
| 2026-10-01 03:00 | c_banda_atr_evento | SPX | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 03:00 | c_banda_atr_evento | XMR | timeout | +0.83% | +0.33% | +0.07 |
| 2026-10-01 03:00 | ruptura_volumen_regimen | XMR | timeout | -0.02% | -0.52% | -0.12 |
| 2026-10-01 03:00 | c_banda_atr_regimen | XMR | timeout | +0.83% | +0.33% | +0.07 |
| 2026-10-01 03:00 | ruptura_volumen_tope | XMR | timeout | -0.02% | -1.12% | -0.26 |

## Eventos de la última vuelta

- 2026-10-01 03:00 [macd_momentum] ENTRADA XRP @ 1.31661 (22.39 €, apertura)
- 2026-10-01 03:00 [macd_sin_salida] ENTRADA XRP @ 1.31661 (22.56 €, apertura)
- 2026-10-01 03:00 [macd_momentum_regimen] ENTRADA XRP @ 1.31661 (22.63 €, apertura)
- 2026-10-01 03:00 [macd_momentum_evento] ENTRADA XRP @ 1.31661 (22.52 €, apertura)
- 2026-10-01 03:05 [estocastico_rebote] CIERRE LINK timeout bruto +0.37% neto -0.13%
- 2026-10-01 03:00 [macd_momentum] ENTRADA SUI @ 1.0442 (22.39 €, apertura)
- 2026-10-01 03:00 [macd_sin_salida] ENTRADA SUI @ 1.0442 (22.56 €, apertura)
- 2026-10-01 03:00 [macd_momentum_regimen] ENTRADA SUI @ 1.0442 (22.63 €, apertura)
- 2026-10-01 03:00 [macd_momentum_evento] ENTRADA SUI @ 1.0442 (22.52 €, apertura)
- 2026-10-01 03:05 [macd_momentum] CIERRE AAVE take-profit bruto +2.02% neto +1.52%
- 2026-10-01 03:05 [macd_momentum_evento] CIERRE AAVE take-profit bruto +2.02% neto +1.52%
- 2026-10-01 03:00 [ruptura_volumen] ENTRADA TAO @ 269.302 (22.27 €, apertura)
- 2026-10-01 03:00 [ruptura_volumen_tope] ENTRADA TAO @ 269.302 (22.87 €, apertura)
- 2026-10-01 03:00 [ruptura_volumen_regimen] ENTRADA TAO @ 269.302 (22.31 €, apertura)
- 2026-10-01 03:00 [ruptura_volumen_evento] ENTRADA TAO @ 269.302 (22.59 €, apertura)
- 2026-10-01 03:00 [macd_momentum] ENTRADA DOGE @ 0.0840563 (22.40 €, apertura)
- 2026-10-01 03:00 [macd_momentum_regimen] ENTRADA DOGE @ 0.0840563 (22.63 €, apertura)
- 2026-10-01 03:00 [macd_momentum_evento] ENTRADA DOGE @ 0.0840563 (22.53 €, apertura)
- 2026-10-01 03:05 [estocastico_rebote] CIERRE ENA take-profit bruto +1.80% neto +1.30%
- 2026-10-01 03:00 [pullback_tendencia] ENTRADA TRX @ 0.298187 (22.57 €, apertura)
- 2026-10-01 03:05 [macd_sin_salida] CIERRE ALGO take-profit bruto +2.00% neto +1.50%
- 2026-10-01 03:00 [macd_momentum] ENTRADA WLD @ 0.4758 (22.40 €, apertura)
- 2026-10-01 03:00 [macd_sin_salida] ENTRADA WLD @ 0.4758 (22.57 €, apertura)
- 2026-10-01 03:00 [macd_momentum_regimen] ENTRADA WLD @ 0.4758 (22.63 €, apertura)
- 2026-10-01 03:00 [macd_momentum_evento] ENTRADA WLD @ 0.4758 (22.53 €, apertura)
- 2026-10-01 03:00 [c_banda_atr] ENTRADA USELESS @ 0.20716 (22.54 €, apertura)
- 2026-10-01 03:00 [c_banda_atr_tope] ENTRADA USELESS @ 0.20716 (22.93 €, apertura)
- 2026-10-01 03:00 [c_banda_atr_regimen] ENTRADA USELESS @ 0.20716 (22.68 €, apertura)
- 2026-10-01 03:00 [c_banda_atr_evento] ENTRADA USELESS @ 0.20716 (22.69 €, apertura)
- 2026-10-01 03:00 [macd_momentum] ENTRADA INJ @ 6.541 (22.40 €, apertura)
- 2026-10-01 03:00 [macd_sin_salida] ENTRADA INJ @ 6.541 (22.57 €, apertura)
- 2026-10-01 03:00 [c_banda_atr_regimen] ENTRADA INJ @ 6.541 (22.68 €, apertura)
- 2026-10-01 03:00 [macd_momentum_regimen] ENTRADA INJ @ 6.541 (22.63 €, apertura)
- 2026-10-01 03:00 [macd_momentum_evento] ENTRADA INJ @ 6.541 (22.53 €, apertura)
- 2026-10-01 03:00 [macd_momentum] ENTRADA WLFI @ 0.0492 (22.40 €, apertura)
- 2026-10-01 03:00 [ruptura_estricta] ENTRADA WLFI @ 0.0492 (22.48 €, apertura)
- 2026-10-01 03:00 [macd_sin_salida] ENTRADA WLFI @ 0.0492 (22.57 €, apertura)
- 2026-10-01 03:00 [macd_momentum_regimen] ENTRADA WLFI @ 0.0492 (22.63 €, apertura)
- 2026-10-01 03:00 [macd_momentum_evento] ENTRADA WLFI @ 0.0492 (22.53 €, apertura)
- 2026-10-01 03:05 [ruptura_volumen] CIERRE TRUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 03:00 [ruptura_volumen_tope] ENTRADA TRUMP @ 1.982 (22.87 €, apertura)
- 2026-10-01 03:05 [ruptura_volumen_tope] CIERRE TRUMP stop-loss bruto -1.20% neto -2.30%
- 2026-10-01 03:05 [ruptura_volumen_regimen] CIERRE TRUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 03:05 [ruptura_volumen_evento] CIERRE TRUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 03:00 [ruptura_volumen_tope] ENTRADA SPX @ 0.3973 (22.86 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
