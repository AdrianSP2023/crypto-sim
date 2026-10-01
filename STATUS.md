# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 16:36 UTC · vueltas 266 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.42 € (-3.77%) | 218 | 19 | 33% | -0.098% | -0.718% | -0.842% | -35.62 € |
| reversion_bb | 916.71 € (-0.81%) | 38 | 9 | 39% | +0.067% | -1.033% | -1.133% | -9.04 € |
| ruptura_volumen | 879.26 € (-4.87%) | 245 | 10 | 23% | -0.209% | -0.816% | -0.924% | -45.25 € |
| rebote_extremo | 922.12 € (-0.23%) | 12 | 1 | 50% | +0.217% | -0.883% | -1.057% | -2.45 € |
| pullback_tendencia | 893.26 € (-3.35%) | 147 | 9 | 14% | -0.268% | -0.948% | -1.048% | -31.70 € |
| macd_momentum | 873.78 € (-5.46%) | 375 | 14 | 20% | -0.039% | -0.608% | -0.716% | -51.37 € |
| estocastico_rebote | 877.75 € (-5.03%) | 284 | 3 | 31% | -0.134% | -0.726% | -0.838% | -46.66 € |
| ruptura_estricta | 886.18 € (-4.12%) | 138 | 9 | 23% | -0.536% | -1.227% | -1.349% | -38.60 € |
| macd_sin_salida | 882.95 € (-4.47%) | 262 | 22 | 34% | -0.111% | -0.711% | -0.827% | -42.34 € |
| c_banda_atr_tope | 911.86 € (-1.34%) | 51 | 4 | 27% | -0.046% | -1.063% | -1.178% | -12.46 € |
| ruptura_volumen_tope | 908.72 € (-1.68%) | 82 | 5 | 27% | -0.024% | -0.846% | -0.960% | -15.91 € |
| c_banda_atr_regimen | 902.06 € (-2.40%) | 110 | 2 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.70 € (-3.30%) | 207 | 1 | 22% | -0.021% | -0.647% | -0.760% | -30.54 € |
| ruptura_volumen_regimen | 882.93 € (-4.47%) | 186 | 4 | 19% | -0.327% | -0.968% | -1.083% | -40.85 € |
| c_banda_atr_evento | 895.34 € (-3.13%) | 185 | 19 | 34% | -0.060% | -0.703% | -0.822% | -29.70 € |
| macd_momentum_evento | 878.62 € (-4.94%) | 328 | 14 | 18% | -0.048% | -0.629% | -0.732% | -46.53 € |
| ruptura_volumen_evento | 891.77 € (-3.51%) | 195 | 10 | 24% | -0.102% | -0.738% | -0.835% | -32.74 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 16:35 | macd_momentum_evento | APT | momentum perdido | +0.09% | -0.41% | -0.09 |
| 2026-10-01 16:35 | macd_momentum_evento | INJ | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-10-01 16:35 | macd_momentum | APT | momentum perdido | +0.09% | -0.41% | -0.09 |
| 2026-10-01 16:35 | macd_momentum | INJ | momentum perdido | -0.17% | -0.67% | -0.14 |
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

## Eventos de la última vuelta

- 2026-10-01 16:30 [ruptura_estricta] ENTRADA ZRO @ 1.579 (22.14 €, apertura)
- 2026-10-01 16:30 [ruptura_volumen_tope] ENTRADA ZRO @ 1.579 (22.71 €, apertura)
- 2026-10-01 16:30 [pullback_tendencia] ENTRADA PEPE @ 3.913e-06 (22.31 €, apertura)
- 2026-10-01 16:35 [macd_momentum] CIERRE INJ momentum perdido bruto -0.17% neto -0.67%
- 2026-10-01 16:35 [macd_momentum_evento] CIERRE INJ momentum perdido bruto -0.17% neto -0.67%
- 2026-10-01 16:35 [macd_momentum] CIERRE APT momentum perdido bruto +0.09% neto -0.41%
- 2026-10-01 16:35 [macd_momentum_evento] CIERRE APT momentum perdido bruto +0.09% neto -0.41%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
