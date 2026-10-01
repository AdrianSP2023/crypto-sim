# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 16:26 UTC · vueltas 264 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.46 € (-3.87%) | 217 | 20 | 33% | -0.092% | -0.712% | -0.837% | -35.18 € |
| reversion_bb | 915.99 € (-0.89%) | 38 | 9 | 39% | +0.067% | -1.033% | -1.133% | -9.04 € |
| ruptura_volumen | 879.36 € (-4.86%) | 244 | 11 | 23% | -0.207% | -0.814% | -0.922% | -44.97 € |
| rebote_extremo | 921.87 € (-0.26%) | 12 | 1 | 50% | +0.217% | -0.883% | -1.057% | -2.45 € |
| pullback_tendencia | 893.03 € (-3.38%) | 146 | 6 | 14% | -0.268% | -0.949% | -1.050% | -31.54 € |
| macd_momentum | 873.23 € (-5.52%) | 371 | 17 | 20% | -0.039% | -0.609% | -0.717% | -50.90 € |
| estocastico_rebote | 877.77 € (-5.03%) | 284 | 3 | 31% | -0.134% | -0.726% | -0.838% | -46.66 € |
| ruptura_estricta | 885.99 € (-4.14%) | 138 | 7 | 23% | -0.536% | -1.227% | -1.349% | -38.60 € |
| macd_sin_salida | 881.84 € (-4.59%) | 261 | 22 | 34% | -0.106% | -0.706% | -0.822% | -41.90 € |
| c_banda_atr_tope | 911.84 € (-1.34%) | 51 | 4 | 27% | -0.046% | -1.063% | -1.178% | -12.46 € |
| ruptura_volumen_tope | 908.52 € (-1.70%) | 82 | 4 | 27% | -0.024% | -0.846% | -0.960% | -15.91 € |
| c_banda_atr_regimen | 901.79 € (-2.43%) | 110 | 2 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.64 € (-3.31%) | 207 | 1 | 22% | -0.021% | -0.647% | -0.760% | -30.54 € |
| ruptura_volumen_regimen | 883.29 € (-4.43%) | 186 | 4 | 19% | -0.327% | -0.968% | -1.083% | -40.85 € |
| c_banda_atr_evento | 894.37 € (-3.23%) | 184 | 20 | 34% | -0.052% | -0.696% | -0.815% | -29.25 € |
| macd_momentum_evento | 878.07 € (-5.00%) | 324 | 17 | 18% | -0.048% | -0.630% | -0.733% | -46.06 € |
| ruptura_volumen_evento | 891.87 € (-3.50%) | 194 | 11 | 24% | -0.099% | -0.735% | -0.832% | -32.45 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 16:25 | ruptura_volumen_evento | TON | timeout | +1.12% | +0.62% | +0.14 |
| 2026-10-01 16:25 | macd_momentum_evento | OP | momentum perdido | -1.31% | -1.81% | -0.40 |
| 2026-10-01 16:25 | macd_momentum_evento | DOGE | momentum perdido | -0.55% | -1.05% | -0.23 |
| 2026-10-01 16:25 | c_banda_atr_evento | KAS | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-10-01 16:25 | ruptura_volumen_tope | TON | timeout | +1.12% | +0.62% | +0.14 |
| 2026-10-01 16:25 | c_banda_atr_tope | KAS | stop-loss | -1.56% | -2.06% | -0.47 |
| 2026-10-01 16:25 | estocastico_rebote | INJ | timeout | +0.12% | -0.38% | -0.08 |
| 2026-10-01 16:25 | macd_momentum | OP | momentum perdido | -1.31% | -1.81% | -0.40 |
| 2026-10-01 16:25 | macd_momentum | DOGE | momentum perdido | -0.55% | -1.05% | -0.23 |
| 2026-10-01 16:25 | ruptura_volumen | TON | timeout | +1.12% | +0.62% | +0.14 |
| 2026-10-01 16:25 | c_banda_atr | KAS | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-10-01 16:20 | macd_momentum_evento | UNI | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-10-01 16:20 | macd_momentum_regimen | UNI | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-10-01 16:20 | ruptura_volumen_tope | ZRO | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 16:20 | ruptura_estricta | ZRO | take-profit | +3.00% | +2.50% | +0.55 |

## Eventos de la última vuelta

- 2026-10-01 16:20 [ruptura_volumen] ENTRADA BTC @ 75021.2 (21.98 €, apertura)
- 2026-10-01 16:20 [ruptura_estricta] ENTRADA BTC @ 75021.2 (22.14 €, apertura)
- 2026-10-01 16:20 [ruptura_volumen_tope] ENTRADA BTC @ 75021.2 (22.70 €, apertura)
- 2026-10-01 16:20 [ruptura_volumen_evento] ENTRADA BTC @ 75021.2 (22.29 €, apertura)
- 2026-10-01 16:20 [ruptura_volumen] ENTRADA ZRO @ 1.561 (21.98 €, apertura)
- 2026-10-01 16:20 [ruptura_volumen_evento] ENTRADA ZRO @ 1.561 (22.29 €, apertura)
- 2026-10-01 16:25 [macd_momentum] CIERRE DOGE momentum perdido bruto -0.55% neto -1.05%
- 2026-10-01 16:25 [macd_momentum_evento] CIERRE DOGE momentum perdido bruto -0.55% neto -1.05%
- 2026-10-01 16:25 [estocastico_rebote] CIERRE INJ timeout bruto +0.12% neto -0.38%
- 2026-10-01 16:25 [macd_momentum] CIERRE OP momentum perdido bruto -1.31% neto -1.81%
- 2026-10-01 16:25 [macd_momentum_evento] CIERRE OP momentum perdido bruto -1.31% neto -1.81%
- 2026-10-01 16:25 [ruptura_volumen] CIERRE TON timeout bruto +1.12% neto +0.62%
- 2026-10-01 16:25 [ruptura_volumen_tope] CIERRE TON timeout bruto +1.12% neto +0.62%
- 2026-10-01 16:25 [ruptura_volumen_evento] CIERRE TON timeout bruto +1.12% neto +0.62%
- 2026-10-01 16:25 [c_banda_atr] CIERRE KAS stop-loss bruto -1.56% neto -2.06%
- 2026-10-01 16:25 [c_banda_atr_tope] CIERRE KAS stop-loss bruto -1.56% neto -2.06%
- 2026-10-01 16:25 [c_banda_atr_evento] CIERRE KAS stop-loss bruto -1.56% neto -2.06%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
