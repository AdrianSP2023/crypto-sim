# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 19:12 UTC · vueltas 291 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.92 € (-3.61%) | 235 | 21 | 36% | -0.020% | -0.631% | -0.754% | -33.78 € |
| reversion_bb | 916.86 € (-0.80%) | 46 | 2 | 50% | +0.324% | -0.730% | -0.827% | -7.74 € |
| ruptura_volumen | 877.61 € (-5.04%) | 267 | 22 | 25% | -0.178% | -0.776% | -0.885% | -46.85 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 892.60 € (-3.42%) | 165 | 9 | 15% | -0.207% | -0.867% | -0.963% | -32.53 € |
| macd_momentum | 871.06 € (-5.75%) | 436 | 2 | 22% | +0.014% | -0.546% | -0.650% | -53.55 € |
| estocastico_rebote | 877.93 € (-5.01%) | 289 | 13 | 31% | -0.125% | -0.716% | -0.827% | -46.80 € |
| ruptura_estricta | 886.30 € (-4.10%) | 146 | 18 | 25% | -0.463% | -1.144% | -1.264% | -38.07 € |
| macd_sin_salida | 884.21 € (-4.33%) | 294 | 22 | 37% | -0.020% | -0.608% | -0.723% | -40.73 € |
| c_banda_atr_tope | 912.02 € (-1.32%) | 55 | 5 | 31% | +0.014% | -0.966% | -1.084% | -12.21 € |
| ruptura_volumen_tope | 908.71 € (-1.68%) | 89 | 5 | 29% | +0.038% | -0.759% | -0.873% | -15.49 € |
| c_banda_atr_regimen | 902.09 € (-2.40%) | 112 | 17 | 35% | -0.105% | -0.838% | -0.978% | -21.56 € |
| macd_momentum_regimen | 891.88 € (-3.50%) | 236 | 2 | 22% | +0.001% | -0.609% | -0.719% | -32.73 € |
| ruptura_volumen_regimen | 881.14 € (-4.66%) | 199 | 24 | 20% | -0.329% | -0.960% | -1.078% | -43.32 € |
| c_banda_atr_evento | 896.85 € (-2.96%) | 202 | 21 | 37% | +0.028% | -0.603% | -0.720% | -27.85 € |
| macd_momentum_evento | 875.88 € (-5.23%) | 389 | 2 | 20% | +0.012% | -0.556% | -0.656% | -48.73 € |
| ruptura_volumen_evento | 890.10 € (-3.69%) | 217 | 22 | 27% | -0.075% | -0.696% | -0.796% | -34.36 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 19:10 | ruptura_volumen_evento | ZRO | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 19:10 | ruptura_volumen_regimen | ZRO | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 19:10 | ruptura_volumen | ZRO | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-01 19:05 | macd_momentum_evento | LINK | momentum perdido | +0.14% | -0.35% | -0.08 |
| 2026-10-01 19:05 | macd_momentum_regimen | LINK | momentum perdido | +0.14% | -0.35% | -0.08 |
| 2026-10-01 19:05 | ruptura_estricta | SHIB | timeout | +0.53% | +0.03% | +0.01 |
| 2026-10-01 19:05 | macd_momentum | LINK | momentum perdido | +0.14% | -0.35% | -0.08 |
| 2026-10-01 19:05 | pullback_tendencia | ADA | rotura de tendencia | -0.53% | -1.03% | -0.23 |
| 2026-10-01 19:00 | macd_momentum_evento | ASTER | momentum perdido | -0.58% | -1.08% | -0.24 |
| 2026-10-01 19:00 | macd_momentum_regimen | ASTER | momentum perdido | -0.58% | -1.08% | -0.24 |
| 2026-10-01 19:00 | macd_momentum | ASTER | momentum perdido | -0.58% | -1.08% | -0.24 |
| 2026-10-01 18:55 | macd_momentum_evento | TON | momentum perdido | +0.29% | -0.21% | -0.05 |
| 2026-10-01 18:55 | macd_momentum_evento | OP | momentum perdido | -0.87% | -1.37% | -0.30 |
| 2026-10-01 18:55 | macd_momentum_evento | CRV | momentum perdido | +0.38% | -0.12% | -0.03 |
| 2026-10-01 18:55 | macd_momentum_evento | UNI | momentum perdido | -1.01% | -1.51% | -0.33 |

## Eventos de la última vuelta

- 2026-10-01 19:05 [estocastico_rebote] ENTRADA BTC @ 75442.5 (21.94 €, apertura)
- 2026-10-01 19:05 [estocastico_rebote] ENTRADA ADA @ 0.220979 (21.94 €, apertura)
- 2026-10-01 19:05 [estocastico_rebote] ENTRADA SUI @ 1.0432 (21.94 €, apertura)
- 2026-10-01 19:10 [ruptura_volumen] CIERRE ZRO stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 19:05 [pullback_tendencia] ENTRADA ZRO @ 1.603 (22.29 €, apertura)
- 2026-10-01 19:10 [ruptura_volumen_regimen] CIERRE ZRO stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 19:10 [ruptura_volumen_evento] CIERRE ZRO stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 19:05 [estocastico_rebote] ENTRADA DOGE @ 0.084599 (21.94 €, apertura)
- 2026-10-01 19:05 [estocastico_rebote] ENTRADA FIL @ 0.91 (21.94 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
