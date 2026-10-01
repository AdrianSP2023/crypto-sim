# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 18:52 UTC · vueltas 287 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.90 € (-3.61%) | 235 | 21 | 36% | -0.020% | -0.631% | -0.754% | -33.78 € |
| reversion_bb | 916.73 € (-0.81%) | 46 | 2 | 50% | +0.324% | -0.730% | -0.827% | -7.74 € |
| ruptura_volumen | 877.41 € (-5.07%) | 266 | 23 | 26% | -0.174% | -0.772% | -0.882% | -46.48 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 892.13 € (-3.47%) | 164 | 6 | 15% | -0.205% | -0.866% | -0.962% | -32.30 € |
| macd_momentum | 872.00 € (-5.65%) | 428 | 10 | 22% | +0.020% | -0.541% | -0.646% | -52.13 € |
| estocastico_rebote | 877.71 € (-5.03%) | 289 | 7 | 31% | -0.125% | -0.716% | -0.827% | -46.80 € |
| ruptura_estricta | 886.16 € (-4.12%) | 144 | 20 | 25% | -0.476% | -1.159% | -1.281% | -38.07 € |
| macd_sin_salida | 884.20 € (-4.33%) | 293 | 23 | 37% | -0.018% | -0.607% | -0.722% | -40.51 € |
| c_banda_atr_tope | 911.89 € (-1.34%) | 55 | 5 | 31% | +0.014% | -0.966% | -1.084% | -12.21 € |
| ruptura_volumen_tope | 908.62 € (-1.69%) | 89 | 5 | 29% | +0.038% | -0.759% | -0.873% | -15.49 € |
| c_banda_atr_regimen | 902.14 € (-2.39%) | 112 | 17 | 35% | -0.105% | -0.838% | -0.978% | -21.56 € |
| macd_momentum_regimen | 892.73 € (-3.41%) | 229 | 9 | 22% | +0.014% | -0.600% | -0.711% | -31.31 € |
| ruptura_volumen_regimen | 880.96 € (-4.68%) | 198 | 25 | 20% | -0.325% | -0.957% | -1.075% | -42.94 € |
| c_banda_atr_evento | 896.83 € (-2.97%) | 202 | 21 | 37% | +0.028% | -0.603% | -0.720% | -27.85 € |
| macd_momentum_evento | 876.83 € (-5.13%) | 381 | 10 | 20% | +0.019% | -0.551% | -0.651% | -47.30 € |
| ruptura_volumen_evento | 889.89 € (-3.72%) | 216 | 23 | 27% | -0.070% | -0.692% | -0.791% | -33.98 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 18:50 | ruptura_volumen_evento | ALGO | stop-loss | -1.38% | -1.88% | -0.42 |
| 2026-10-01 18:50 | ruptura_volumen_evento | AAVE | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 18:50 | macd_momentum_evento | KSM | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 18:50 | macd_momentum_evento | DOGE | momentum perdido | +0.33% | -0.17% | -0.04 |
| 2026-10-01 18:50 | macd_momentum_evento | LTC | momentum perdido | +0.64% | +0.14% | +0.03 |
| 2026-10-01 18:50 | macd_momentum_evento | ETH | momentum perdido | -0.46% | -0.96% | -0.21 |
| 2026-10-01 18:50 | macd_momentum_evento | XRP | momentum perdido | -0.43% | -0.93% | -0.20 |
| 2026-10-01 18:50 | ruptura_volumen_regimen | ALGO | stop-loss | -1.38% | -1.88% | -0.41 |
| 2026-10-01 18:50 | ruptura_volumen_regimen | AAVE | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 18:50 | macd_momentum_regimen | KSM | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 18:50 | macd_momentum_regimen | ETH | momentum perdido | -0.46% | -0.96% | -0.21 |
| 2026-10-01 18:50 | macd_momentum_regimen | XRP | momentum perdido | -0.43% | -0.93% | -0.21 |
| 2026-10-01 18:50 | macd_sin_salida | BTC | timeout | +0.53% | +0.03% | +0.01 |
| 2026-10-01 18:50 | macd_momentum | KSM | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 18:50 | macd_momentum | DOGE | momentum perdido | +0.33% | -0.17% | -0.04 |

## Eventos de la última vuelta

- 2026-10-01 18:50 [macd_sin_salida] CIERRE BTC timeout bruto +0.53% neto +0.03%
- 2026-10-01 18:50 [macd_momentum] CIERRE XRP momentum perdido bruto -0.43% neto -0.93%
- 2026-10-01 18:50 [macd_momentum_regimen] CIERRE XRP momentum perdido bruto -0.43% neto -0.93%
- 2026-10-01 18:50 [macd_momentum_evento] CIERRE XRP momentum perdido bruto -0.43% neto -0.93%
- 2026-10-01 18:50 [macd_momentum] CIERRE ETH momentum perdido bruto -0.46% neto -0.96%
- 2026-10-01 18:50 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto -0.46% neto -0.96%
- 2026-10-01 18:50 [macd_momentum_evento] CIERRE ETH momentum perdido bruto -0.46% neto -0.96%
- 2026-10-01 18:45 [pullback_tendencia] ENTRADA ADA @ 0.222037 (22.32 €, apertura)
- 2026-10-01 18:50 [ruptura_volumen] CIERRE AAVE stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 18:50 [ruptura_volumen_regimen] CIERRE AAVE stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 18:50 [ruptura_volumen_evento] CIERRE AAVE stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 18:50 [pullback_tendencia] CIERRE TAO rotura de tendencia bruto -0.61% neto -1.11%
- 2026-10-01 18:45 [macd_momentum] ENTRADA TAO @ 271.615 (21.81 €, apertura)
- 2026-10-01 18:45 [macd_momentum_regimen] ENTRADA TAO @ 271.615 (22.33 €, apertura)
- 2026-10-01 18:45 [macd_momentum_evento] ENTRADA TAO @ 271.615 (21.93 €, apertura)
- 2026-10-01 18:50 [macd_momentum] CIERRE LTC momentum perdido bruto +0.64% neto +0.14%
- 2026-10-01 18:50 [macd_momentum_evento] CIERRE LTC momentum perdido bruto +0.64% neto +0.14%
- 2026-10-01 18:50 [macd_momentum] CIERRE DOGE momentum perdido bruto +0.33% neto -0.17%
- 2026-10-01 18:50 [macd_momentum_evento] CIERRE DOGE momentum perdido bruto +0.33% neto -0.17%
- 2026-10-01 18:50 [pullback_tendencia] CIERRE ARB rotura de tendencia bruto -0.72% neto -1.22%
- 2026-10-01 18:45 [pullback_tendencia] ENTRADA TRX @ 0.298399 (22.30 €, apertura)
- 2026-10-01 18:50 [ruptura_volumen] CIERRE ALGO stop-loss bruto -1.38% neto -1.88%
- 2026-10-01 18:50 [ruptura_volumen_regimen] CIERRE ALGO stop-loss bruto -1.38% neto -1.88%
- 2026-10-01 18:50 [ruptura_volumen_evento] CIERRE ALGO stop-loss bruto -1.38% neto -1.88%
- 2026-10-01 18:50 [macd_momentum] CIERRE KSM momentum perdido bruto +0.00% neto -0.50%
- 2026-10-01 18:50 [macd_momentum_regimen] CIERRE KSM momentum perdido bruto +0.00% neto -0.50%
- 2026-10-01 18:50 [macd_momentum_evento] CIERRE KSM momentum perdido bruto +0.00% neto -0.50%
- 2026-10-01 18:50 [pullback_tendencia] CIERRE BNB rotura de tendencia bruto -0.21% neto -0.71%
- 2026-10-01 18:45 [c_banda_atr] ENTRADA KAS @ 0.03722 (22.26 €, apertura)
- 2026-10-01 18:45 [c_banda_atr_regimen] ENTRADA KAS @ 0.03722 (22.57 €, apertura)
- 2026-10-01 18:45 [c_banda_atr_evento] ENTRADA KAS @ 0.03722 (22.41 €, apertura)
- 2026-10-01 18:45 [estocastico_rebote] ENTRADA SPX @ 0.3894 (21.94 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
