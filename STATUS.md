# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 06:46 UTC · vueltas 151 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.19 € (-1.84%) | 139 | 19 | 40% | +0.148% | -0.540% | -0.656% | -17.29 € |
| reversion_bb | 921.48 € (-0.30%) | 17 | 2 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 890.58 € (-3.64%) | 183 | 18 | 24% | -0.158% | -0.801% | -0.908% | -33.43 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 902.16 € (-2.39%) | 100 | 15 | 17% | -0.224% | -0.988% | -1.099% | -22.60 € |
| macd_momentum | 892.29 € (-3.46%) | 264 | 11 | 24% | +0.072% | -0.527% | -0.631% | -31.67 € |
| estocastico_rebote | 901.57 € (-2.45%) | 175 | 23 | 39% | +0.110% | -0.539% | -0.660% | -21.71 € |
| ruptura_estricta | 901.30 € (-2.48%) | 92 | 27 | 32% | -0.310% | -1.097% | -1.227% | -23.28 € |
| macd_sin_salida | 903.51 € (-2.24%) | 176 | 28 | 44% | +0.165% | -0.483% | -0.593% | -19.58 € |
| c_banda_atr_tope | 917.34 € (-0.75%) | 30 | 5 | 30% | +0.135% | -0.965% | -1.091% | -6.68 € |
| ruptura_volumen_tope | 915.15 € (-0.98%) | 50 | 3 | 30% | +0.225% | -0.803% | -0.901% | -9.25 € |
| c_banda_atr_regimen | 911.53 € (-1.38%) | 82 | 18 | 41% | +0.146% | -0.672% | -0.808% | -12.74 € |
| macd_momentum_regimen | 901.34 € (-2.48%) | 178 | 11 | 25% | +0.092% | -0.555% | -0.663% | -22.61 € |
| ruptura_volumen_regimen | 891.33 € (-3.56%) | 157 | 17 | 21% | -0.244% | -0.910% | -1.020% | -32.61 € |
| c_banda_atr_evento | 913.23 € (-1.19%) | 106 | 19 | 42% | +0.291% | -0.458% | -0.562% | -11.25 € |
| macd_momentum_evento | 897.24 € (-2.92%) | 217 | 11 | 21% | +0.081% | -0.540% | -0.637% | -26.73 € |
| ruptura_volumen_evento | 903.25 € (-2.27%) | 133 | 18 | 26% | +0.018% | -0.681% | -0.771% | -20.74 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 06:45 | ruptura_volumen_evento | INJ | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-10-01 06:45 | ruptura_volumen_regimen | INJ | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-10-01 06:45 | ruptura_estricta | BTC | timeout | +0.64% | +0.14% | +0.03 |
| 2026-10-01 06:45 | pullback_tendencia | PENGU | rotura de tendencia | -0.64% | -1.14% | -0.26 |
| 2026-10-01 06:45 | pullback_tendencia | SUI | rotura de tendencia | -0.17% | -0.67% | -0.15 |
| 2026-10-01 06:45 | ruptura_volumen | INJ | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-10-01 06:40 | macd_momentum_evento | BNB | momentum perdido | +0.19% | -0.31% | -0.07 |
| 2026-10-01 06:40 | macd_momentum_evento | PENGU | momentum perdido | -0.08% | -0.58% | -0.13 |
| 2026-10-01 06:40 | macd_momentum_regimen | BNB | momentum perdido | +0.19% | -0.31% | -0.07 |
| 2026-10-01 06:40 | macd_momentum_regimen | PENGU | momentum perdido | -0.08% | -0.58% | -0.13 |
| 2026-10-01 06:40 | macd_sin_salida | ETH | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-01 06:40 | ruptura_estricta | PEPE | timeout | +0.86% | +0.36% | +0.08 |
| 2026-10-01 06:40 | ruptura_estricta | TAO | timeout | +0.88% | +0.38% | +0.09 |
| 2026-10-01 06:40 | macd_momentum | BNB | momentum perdido | +0.19% | -0.31% | -0.07 |
| 2026-10-01 06:40 | macd_momentum | PENGU | momentum perdido | -0.08% | -0.58% | -0.13 |

## Eventos de la última vuelta

- 2026-10-01 06:45 [ruptura_estricta] CIERRE BTC timeout bruto +0.64% neto +0.14%
- 2026-10-01 06:45 [pullback_tendencia] CIERRE SUI rotura de tendencia bruto -0.17% neto -0.67%
- 2026-10-01 06:45 [ruptura_volumen] CIERRE INJ stop-loss bruto -1.33% neto -1.83%
- 2026-10-01 06:45 [ruptura_volumen_regimen] CIERRE INJ stop-loss bruto -1.33% neto -1.83%
- 2026-10-01 06:45 [ruptura_volumen_evento] CIERRE INJ stop-loss bruto -1.33% neto -1.83%
- 2026-10-01 06:45 [pullback_tendencia] CIERRE PENGU rotura de tendencia bruto -0.64% neto -1.14%
- 2026-10-01 06:40 [macd_momentum] ENTRADA APT @ 0.6935 (22.31 €, apertura)
- 2026-10-01 06:40 [macd_sin_salida] ENTRADA APT @ 0.6935 (22.62 €, apertura)
- 2026-10-01 06:40 [macd_momentum_regimen] ENTRADA APT @ 0.6935 (22.54 €, apertura)
- 2026-10-01 06:40 [macd_momentum_evento] ENTRADA APT @ 0.6935 (22.44 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
