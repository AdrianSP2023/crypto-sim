# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 16:31 UTC · vueltas 265 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.11 € (-3.91%) | 218 | 19 | 33% | -0.098% | -0.718% | -0.842% | -35.62 € |
| reversion_bb | 915.90 € (-0.90%) | 38 | 9 | 39% | +0.067% | -1.033% | -1.133% | -9.04 € |
| ruptura_volumen | 879.02 € (-4.89%) | 245 | 10 | 23% | -0.209% | -0.816% | -0.924% | -45.25 € |
| rebote_extremo | 921.96 € (-0.25%) | 12 | 1 | 50% | +0.217% | -0.883% | -1.057% | -2.45 € |
| pullback_tendencia | 892.75 € (-3.41%) | 147 | 8 | 14% | -0.268% | -0.948% | -1.048% | -31.70 € |
| macd_momentum | 873.05 € (-5.54%) | 373 | 16 | 20% | -0.039% | -0.609% | -0.717% | -51.14 € |
| estocastico_rebote | 877.55 € (-5.05%) | 284 | 3 | 31% | -0.134% | -0.726% | -0.838% | -46.66 € |
| ruptura_estricta | 885.68 € (-4.17%) | 138 | 8 | 23% | -0.536% | -1.227% | -1.349% | -38.60 € |
| macd_sin_salida | 881.65 € (-4.61%) | 262 | 22 | 34% | -0.111% | -0.711% | -0.827% | -42.34 € |
| c_banda_atr_tope | 911.70 € (-1.36%) | 51 | 4 | 27% | -0.046% | -1.063% | -1.178% | -12.46 € |
| ruptura_volumen_tope | 908.49 € (-1.70%) | 82 | 4 | 27% | -0.024% | -0.846% | -0.960% | -15.91 € |
| c_banda_atr_regimen | 901.79 € (-2.43%) | 110 | 2 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.62 € (-3.31%) | 207 | 1 | 22% | -0.021% | -0.647% | -0.760% | -30.54 € |
| ruptura_volumen_regimen | 882.89 € (-4.47%) | 186 | 4 | 19% | -0.327% | -0.968% | -1.083% | -40.85 € |
| c_banda_atr_evento | 894.02 € (-3.27%) | 185 | 19 | 34% | -0.060% | -0.703% | -0.822% | -29.70 € |
| macd_momentum_evento | 877.89 € (-5.01%) | 326 | 16 | 18% | -0.049% | -0.629% | -0.733% | -46.30 € |
| ruptura_volumen_evento | 891.53 € (-3.54%) | 195 | 10 | 24% | -0.102% | -0.738% | -0.835% | -32.74 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 16:30 | ruptura_volumen_evento | TAO | timeout | -0.79% | -1.29% | -0.29 |
| 2026-10-01 16:30 | macd_momentum_evento | PEPE | momentum perdido | +0.51% | +0.01% | +0.00 |
| 2026-10-01 16:30 | macd_momentum_evento | ARB | momentum perdido | -0.61% | -1.11% | -0.24 |
| 2026-10-01 16:30 | c_banda_atr_evento | OP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 16:30 | macd_sin_salida | OP | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 16:30 | macd_momentum | PEPE | momentum perdido | +0.51% | +0.01% | +0.00 |
| 2026-10-01 16:30 | macd_momentum | ARB | momentum perdido | -0.61% | -1.11% | -0.24 |
| 2026-10-01 16:30 | pullback_tendencia | UNI | rotura de tendencia | -0.22% | -0.72% | -0.16 |
| 2026-10-01 16:30 | ruptura_volumen | TAO | timeout | -0.79% | -1.29% | -0.28 |
| 2026-10-01 16:30 | c_banda_atr | OP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 16:25 | ruptura_volumen_evento | TON | timeout | +1.12% | +0.62% | +0.14 |
| 2026-10-01 16:25 | macd_momentum_evento | OP | momentum perdido | -1.31% | -1.81% | -0.40 |
| 2026-10-01 16:25 | macd_momentum_evento | DOGE | momentum perdido | -0.55% | -1.05% | -0.23 |
| 2026-10-01 16:25 | c_banda_atr_evento | KAS | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-10-01 16:25 | ruptura_volumen_tope | TON | timeout | +1.12% | +0.62% | +0.14 |

## Eventos de la última vuelta

- 2026-10-01 16:25 [pullback_tendencia] ENTRADA XRP @ 1.32274 (22.32 €, apertura)
- 2026-10-01 16:25 [pullback_tendencia] ENTRADA LINK @ 12.7267 (22.32 €, apertura)
- 2026-10-01 16:30 [ruptura_volumen] CIERRE TAO timeout bruto -0.79% neto -1.29%
- 2026-10-01 16:30 [ruptura_volumen_evento] CIERRE TAO timeout bruto -0.79% neto -1.29%
- 2026-10-01 16:30 [pullback_tendencia] CIERRE UNI rotura de tendencia bruto -0.22% neto -0.72%
- 2026-10-01 16:30 [macd_momentum] CIERRE ARB momentum perdido bruto -0.61% neto -1.11%
- 2026-10-01 16:30 [macd_momentum_evento] CIERRE ARB momentum perdido bruto -0.61% neto -1.11%
- 2026-10-01 16:25 [pullback_tendencia] ENTRADA BCH @ 273.26 (22.31 €, apertura)
- 2026-10-01 16:30 [macd_momentum] CIERRE PEPE momentum perdido bruto +0.51% neto +0.01%
- 2026-10-01 16:30 [macd_momentum_evento] CIERRE PEPE momentum perdido bruto +0.51% neto +0.01%
- 2026-10-01 16:30 [c_banda_atr] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 16:30 [macd_sin_salida] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 16:30 [c_banda_atr_evento] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 16:25 [macd_momentum] ENTRADA TON @ 1.353 (21.83 €, apertura)
- 2026-10-01 16:25 [macd_sin_salida] ENTRADA TON @ 1.353 (22.05 €, apertura)
- 2026-10-01 16:25 [macd_momentum_evento] ENTRADA TON @ 1.353 (21.95 €, apertura)
- 2026-10-01 16:25 [ruptura_estricta] ENTRADA XMR @ 481.77 (22.14 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
