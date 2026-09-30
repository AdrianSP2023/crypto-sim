# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 18:06 UTC · vueltas 70 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.08 € (-1.53%) | 43 | 8 | 30% | -0.331% | -1.389% | -1.547% | -13.77 € |
| reversion_bb | 923.26 € (-0.11%) | 4 | 4 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 899.43 € (-2.68%) | 71 | 2 | 14% | -0.684% | -1.552% | -1.694% | -25.28 € |
| rebote_extremo | 923.90 € (-0.04%) | 2 | 0 | 50% | +0.370% | -0.731% | -0.816% | -0.34 € |
| pullback_tendencia | 907.37 € (-1.83%) | 51 | 3 | 16% | -0.416% | -1.428% | -1.555% | -16.72 € |
| macd_momentum | 911.27 € (-1.40%) | 68 | 3 | 31% | +0.035% | -0.849% | -0.993% | -13.30 € |
| estocastico_rebote | 912.60 € (-1.26%) | 74 | 33 | 47% | +0.293% | -0.560% | -0.707% | -9.62 € |
| ruptura_estricta | 900.59 € (-2.56%) | 43 | 3 | 9% | -1.345% | -2.438% | -2.586% | -24.15 € |
| macd_sin_salida | 907.19 € (-1.84%) | 62 | 5 | 34% | -0.262% | -1.183% | -1.329% | -16.92 € |
| c_banda_atr_tope | 922.31 € (-0.21%) | 10 | 5 | 50% | +0.251% | -0.849% | -1.020% | -1.96 € |
| ruptura_volumen_tope | 918.83 € (-0.59%) | 17 | 0 | 24% | -0.279% | -1.379% | -1.489% | -5.41 € |
| c_banda_atr_regimen | 909.99 € (-1.54%) | 40 | 5 | 28% | -0.418% | -1.518% | -1.672% | -14.00 € |
| macd_momentum_regimen | 911.47 € (-1.38%) | 59 | 1 | 31% | +0.004% | -0.938% | -1.081% | -12.76 € |
| ruptura_volumen_regimen | 898.81 € (-2.75%) | 70 | 2 | 13% | -0.741% | -1.614% | -1.756% | -25.91 € |
| c_banda_atr_evento | 920.37 € (-0.42%) | 10 | 9 | 30% | -0.477% | -1.577% | -1.730% | -3.64 € |
| macd_momentum_evento | 919.50 € (-0.51%) | 21 | 3 | 29% | +0.051% | -1.049% | -1.209% | -5.08 € |
| ruptura_volumen_evento | 915.40 € (-0.96%) | 21 | 2 | 10% | -0.821% | -1.921% | -2.046% | -9.32 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 18:05 | ruptura_volumen_evento | JUP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 18:05 | ruptura_volumen_evento | NIGHT | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 18:05 | ruptura_volumen_evento | ONDO | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 18:05 | ruptura_volumen_evento | PUMP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 18:05 | macd_momentum_evento | AVAX | momentum perdido | -0.31% | -1.41% | -0.32 |
| 2026-09-30 18:05 | c_banda_atr_evento | KAS | stop-loss | -1.53% | -2.63% | -0.61 |
| 2026-09-30 18:05 | c_banda_atr_evento | OP | stop-loss | -1.63% | -2.73% | -0.63 |
| 2026-09-30 18:05 | ruptura_volumen_regimen | JUP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 18:05 | ruptura_volumen_regimen | ONDO | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 18:05 | ruptura_volumen_regimen | PUMP | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 18:05 | macd_momentum_regimen | AVAX | momentum perdido | -0.31% | -0.81% | -0.18 |
| 2026-09-30 18:05 | c_banda_atr_regimen | KAS | stop-loss | -1.53% | -2.63% | -0.60 |
| 2026-09-30 18:05 | c_banda_atr_regimen | OP | stop-loss | -1.63% | -2.73% | -0.62 |
| 2026-09-30 18:05 | ruptura_volumen_tope | NIGHT | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 18:05 | macd_sin_salida | TON | timeout | +1.13% | +0.63% | +0.14 |

## Eventos de la última vuelta

- 2026-09-30 18:05 [macd_momentum] CIERRE AVAX momentum perdido bruto -0.31% neto -0.81%
- 2026-09-30 18:05 [macd_momentum_regimen] CIERRE AVAX momentum perdido bruto -0.31% neto -0.81%
- 2026-09-30 18:05 [macd_momentum_evento] CIERRE AVAX momentum perdido bruto -0.31% neto -1.41%
- 2026-09-30 18:05 [ruptura_volumen] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 18:05 [ruptura_volumen_regimen] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 18:05 [ruptura_volumen_evento] CIERRE PUMP stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 18:05 [pullback_tendencia] CIERRE DOT rotura de tendencia bruto -0.65% neto -1.15%
- 2026-09-30 18:05 [ruptura_volumen] CIERRE ONDO stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 18:05 [ruptura_volumen_regimen] CIERRE ONDO stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 18:05 [ruptura_volumen_evento] CIERRE ONDO stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 18:05 [ruptura_volumen] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%
- 2026-09-30 18:05 [ruptura_volumen_tope] CIERRE NIGHT take-profit bruto +2.50% neto +1.40%
- 2026-09-30 18:05 [ruptura_volumen_evento] CIERRE NIGHT take-profit bruto +2.50% neto +1.40%
- 2026-09-30 18:05 [ruptura_volumen] CIERRE JUP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 18:05 [ruptura_volumen_regimen] CIERRE JUP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 18:05 [ruptura_volumen_evento] CIERRE JUP stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 18:05 [c_banda_atr] CIERRE OP stop-loss bruto -1.63% neto -2.43%
- 2026-09-30 18:05 [c_banda_atr_regimen] CIERRE OP stop-loss bruto -1.63% neto -2.73%
- 2026-09-30 18:05 [c_banda_atr_evento] CIERRE OP stop-loss bruto -1.63% neto -2.73%
- 2026-09-30 18:00 [reversion_bb] ENTRADA MINA @ 0.1287 (23.10 €, apertura)
- 2026-09-30 18:00 [estocastico_rebote] ENTRADA VVV @ 24.401 (22.87 €, apertura)
- 2026-09-30 18:05 [macd_sin_salida] CIERRE TON timeout bruto +1.13% neto +0.63%
- 2026-09-30 18:05 [c_banda_atr] CIERRE KAS stop-loss bruto -1.53% neto -2.33%
- 2026-09-30 18:05 [c_banda_atr_regimen] CIERRE KAS stop-loss bruto -1.53% neto -2.63%
- 2026-09-30 18:05 [c_banda_atr_evento] CIERRE KAS stop-loss bruto -1.53% neto -2.63%
- 2026-09-30 18:00 [estocastico_rebote] ENTRADA XMR @ 481.1 (22.87 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
