# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 19:17 UTC · vueltas 292 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.91 € (-3.61%) | 235 | 23 | 36% | -0.020% | -0.631% | -0.754% | -33.78 € |
| reversion_bb | 916.68 € (-0.82%) | 47 | 1 | 51% | +0.335% | -0.714% | -0.811% | -7.74 € |
| ruptura_volumen | 877.37 € (-5.07%) | 267 | 22 | 25% | -0.178% | -0.776% | -0.885% | -46.85 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 892.20 € (-3.47%) | 165 | 11 | 15% | -0.207% | -0.867% | -0.963% | -32.53 € |
| macd_momentum | 871.07 € (-5.75%) | 436 | 3 | 22% | +0.014% | -0.546% | -0.650% | -53.55 € |
| estocastico_rebote | 877.50 € (-5.06%) | 289 | 20 | 31% | -0.125% | -0.716% | -0.827% | -46.80 € |
| ruptura_estricta | 886.13 € (-4.12%) | 146 | 19 | 25% | -0.463% | -1.144% | -1.264% | -38.07 € |
| macd_sin_salida | 883.89 € (-4.37%) | 294 | 23 | 37% | -0.020% | -0.608% | -0.723% | -40.73 € |
| c_banda_atr_tope | 912.07 € (-1.32%) | 55 | 5 | 31% | +0.014% | -0.966% | -1.084% | -12.21 € |
| ruptura_volumen_tope | 908.64 € (-1.69%) | 89 | 5 | 29% | +0.038% | -0.759% | -0.873% | -15.49 € |
| c_banda_atr_regimen | 902.03 € (-2.40%) | 112 | 19 | 35% | -0.105% | -0.838% | -0.978% | -21.56 € |
| macd_momentum_regimen | 891.89 € (-3.50%) | 236 | 3 | 22% | +0.001% | -0.609% | -0.719% | -32.73 € |
| ruptura_volumen_regimen | 880.87 € (-4.69%) | 199 | 24 | 20% | -0.329% | -0.960% | -1.078% | -43.32 € |
| c_banda_atr_evento | 896.84 € (-2.96%) | 202 | 23 | 37% | +0.028% | -0.603% | -0.720% | -27.85 € |
| macd_momentum_evento | 875.90 € (-5.23%) | 389 | 3 | 20% | +0.012% | -0.556% | -0.656% | -48.73 € |
| ruptura_volumen_evento | 889.86 € (-3.72%) | 217 | 22 | 27% | -0.075% | -0.696% | -0.796% | -34.36 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 19:15 | reversion_bb | ONDO | timeout | +0.81% | +0.01% | +0.00 |
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

## Eventos de la última vuelta

- 2026-10-01 19:10 [estocastico_rebote] ENTRADA XRP @ 1.33696 (21.94 €, apertura)
- 2026-10-01 19:10 [estocastico_rebote] ENTRADA ETH @ 2405.89 (21.94 €, apertura)
- 2026-10-01 19:10 [estocastico_rebote] ENTRADA SOL @ 105.5 (21.94 €, apertura)
- 2026-10-01 19:10 [c_banda_atr] ENTRADA LINK @ 12.8598 (22.26 €, apertura)
- 2026-10-01 19:10 [macd_momentum] ENTRADA LINK @ 12.8598 (21.77 €, apertura)
- 2026-10-01 19:10 [macd_sin_salida] ENTRADA LINK @ 12.8598 (22.09 €, apertura)
- 2026-10-01 19:10 [c_banda_atr_regimen] ENTRADA LINK @ 12.8598 (22.57 €, apertura)
- 2026-10-01 19:10 [macd_momentum_regimen] ENTRADA LINK @ 12.8598 (22.29 €, apertura)
- 2026-10-01 19:10 [c_banda_atr_evento] ENTRADA LINK @ 12.8598 (22.41 €, apertura)
- 2026-10-01 19:10 [macd_momentum_evento] ENTRADA LINK @ 12.8598 (21.89 €, apertura)
- 2026-10-01 19:10 [ruptura_estricta] ENTRADA AVAX @ 9.835 (22.15 €, apertura)
- 2026-10-01 19:10 [c_banda_atr] ENTRADA LTC @ 60.5 (22.26 €, apertura)
- 2026-10-01 19:10 [c_banda_atr_regimen] ENTRADA LTC @ 60.5 (22.57 €, apertura)
- 2026-10-01 19:10 [c_banda_atr_evento] ENTRADA LTC @ 60.5 (22.41 €, apertura)
- 2026-10-01 19:10 [pullback_tendencia] ENTRADA DOGE @ 0.0846425 (22.29 €, apertura)
- 2026-10-01 19:10 [estocastico_rebote] ENTRADA ARB @ 0.1785 (21.94 €, apertura)
- 2026-10-01 19:15 [reversion_bb] CIERRE ONDO timeout bruto +0.81% neto +0.01%
- 2026-10-01 19:10 [estocastico_rebote] ENTRADA RENDER @ 1.707 (21.94 €, apertura)
- 2026-10-01 19:10 [estocastico_rebote] ENTRADA TRUMP @ 1.836 (21.94 €, apertura)
- 2026-10-01 19:10 [estocastico_rebote] ENTRADA TON @ 1.377 (21.94 €, apertura)
- 2026-10-01 19:10 [pullback_tendencia] ENTRADA XMR @ 487.01 (22.29 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
