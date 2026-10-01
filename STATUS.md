# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 20:31 UTC · vueltas 307 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.89 € (-3.72%) | 244 | 27 | 36% | -0.032% | -0.639% | -0.762% | -35.51 € |
| reversion_bb | 917.21 € (-0.76%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 873.04 € (-5.54%) | 288 | 5 | 25% | -0.197% | -0.787% | -0.895% | -51.14 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.33 € (-3.67%) | 177 | 6 | 15% | -0.200% | -0.849% | -0.942% | -34.15 € |
| macd_momentum | 869.86 € (-5.88%) | 441 | 36 | 22% | +0.013% | -0.546% | -0.650% | -54.14 € |
| estocastico_rebote | 878.47 € (-4.95%) | 296 | 24 | 32% | -0.106% | -0.695% | -0.806% | -46.53 € |
| ruptura_estricta | 883.92 € (-4.36%) | 157 | 9 | 25% | -0.437% | -1.105% | -1.220% | -39.52 € |
| macd_sin_salida | 880.21 € (-4.76%) | 314 | 30 | 37% | -0.021% | -0.604% | -0.718% | -43.12 € |
| c_banda_atr_tope | 911.92 € (-1.33%) | 56 | 5 | 30% | +0.019% | -0.953% | -1.068% | -12.26 € |
| ruptura_volumen_tope | 907.16 € (-1.85%) | 95 | 4 | 28% | +0.008% | -0.770% | -0.884% | -16.78 € |
| c_banda_atr_regimen | 900.63 € (-2.55%) | 117 | 21 | 33% | -0.150% | -0.873% | -1.012% | -23.43 € |
| macd_momentum_regimen | 890.81 € (-3.62%) | 241 | 33 | 22% | +0.000% | -0.608% | -0.717% | -33.33 € |
| ruptura_volumen_regimen | 875.90 € (-5.23%) | 222 | 4 | 19% | -0.345% | -0.963% | -1.078% | -48.31 € |
| c_banda_atr_evento | 895.81 € (-3.08%) | 211 | 27 | 36% | +0.011% | -0.614% | -0.731% | -29.59 € |
| macd_momentum_evento | 874.68 € (-5.36%) | 394 | 36 | 20% | +0.011% | -0.556% | -0.655% | -49.32 € |
| ruptura_volumen_evento | 885.46 € (-4.20%) | 238 | 5 | 26% | -0.106% | -0.717% | -0.816% | -38.70 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 20:30 | ruptura_volumen_evento | KAS | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 20:30 | macd_momentum_evento | LINK | momentum perdido | -0.57% | -1.07% | -0.23 |
| 2026-10-01 20:30 | ruptura_volumen_regimen | KAS | stop-loss | -1.56% | -2.06% | -0.45 |
| 2026-10-01 20:30 | macd_momentum_regimen | LINK | momentum perdido | -0.57% | -1.07% | -0.24 |
| 2026-10-01 20:30 | ruptura_volumen_tope | KAS | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 20:30 | macd_sin_salida | KSM | timeout | -0.87% | -1.37% | -0.30 |
| 2026-10-01 20:30 | macd_sin_salida | AAVE | timeout | +1.00% | +0.50% | +0.11 |
| 2026-10-01 20:30 | macd_momentum | LINK | momentum perdido | -0.57% | -1.07% | -0.23 |
| 2026-10-01 20:30 | ruptura_volumen | KAS | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-01 20:25 | ruptura_estricta | SPX | timeout | +0.51% | +0.01% | +0.00 |
| 2026-10-01 20:20 | macd_momentum_evento | AVAX | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-01 20:20 | macd_momentum_regimen | AVAX | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-01 20:20 | ruptura_volumen_tope | DOT | timeout | +0.15% | -0.35% | -0.08 |
| 2026-10-01 20:20 | macd_sin_salida | DASH | timeout | -0.17% | -0.67% | -0.15 |
| 2026-10-01 20:20 | macd_sin_salida | RENDER | timeout | -0.12% | -0.62% | -0.14 |

## Eventos de la última vuelta

- 2026-10-01 20:25 [macd_momentum] ENTRADA BTC @ 75401 (21.76 €, apertura)
- 2026-10-01 20:25 [macd_sin_salida] ENTRADA BTC @ 75401 (22.03 €, apertura)
- 2026-10-01 20:25 [macd_momentum_regimen] ENTRADA BTC @ 75401 (22.28 €, apertura)
- 2026-10-01 20:25 [macd_momentum_evento] ENTRADA BTC @ 75401 (21.88 €, apertura)
- 2026-10-01 20:30 [macd_momentum] CIERRE LINK momentum perdido bruto -0.57% neto -1.07%
- 2026-10-01 20:30 [macd_momentum_regimen] CIERRE LINK momentum perdido bruto -0.57% neto -1.07%
- 2026-10-01 20:30 [macd_momentum_evento] CIERRE LINK momentum perdido bruto -0.57% neto -1.07%
- 2026-10-01 20:30 [macd_sin_salida] CIERRE AAVE timeout bruto +1.00% neto +0.50%
- 2026-10-01 20:25 [macd_momentum] ENTRADA ALGO @ 0.11093 (21.75 €, apertura)
- 2026-10-01 20:25 [macd_sin_salida] ENTRADA ALGO @ 0.11093 (22.04 €, apertura)
- 2026-10-01 20:25 [macd_momentum_regimen] ENTRADA ALGO @ 0.11093 (22.27 €, apertura)
- 2026-10-01 20:25 [macd_momentum_evento] ENTRADA ALGO @ 0.11093 (21.87 €, apertura)
- 2026-10-01 20:25 [estocastico_rebote] ENTRADA MON @ 0.03048 (21.94 €, apertura)
- 2026-10-01 20:30 [macd_sin_salida] CIERRE KSM timeout bruto -0.87% neto -1.37%
- 2026-10-01 20:25 [macd_momentum] ENTRADA TON @ 1.381 (21.75 €, apertura)
- 2026-10-01 20:25 [macd_sin_salida] ENTRADA TON @ 1.381 (22.03 €, apertura)
- 2026-10-01 20:25 [macd_momentum_regimen] ENTRADA TON @ 1.381 (22.27 €, apertura)
- 2026-10-01 20:25 [macd_momentum_evento] ENTRADA TON @ 1.381 (21.87 €, apertura)
- 2026-10-01 20:30 [ruptura_volumen] CIERRE KAS stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 20:30 [ruptura_volumen_tope] CIERRE KAS stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 20:30 [ruptura_volumen_regimen] CIERRE KAS stop-loss bruto -1.56% neto -2.06%
- 2026-10-01 20:30 [ruptura_volumen_evento] CIERRE KAS stop-loss bruto -1.20% neto -1.70%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
