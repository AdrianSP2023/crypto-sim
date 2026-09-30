# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 13:56 UTC · vueltas 20 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 916.09 € (-0.88%) | 26 | 8 | 38% | -0.135% | -1.235% | -1.401% | -7.42 € |
| reversion_bb | 924.63 € (+0.04%) | 1 | 2 | 100% | +1.500% | +0.400% | +0.231% | +0.09 € |
| ruptura_volumen | 911.45 € (-1.38%) | 36 | 14 | 22% | -0.391% | -1.491% | -1.653% | -12.39 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 918.31 € (-0.64%) | 21 | 5 | 29% | -0.149% | -1.249% | -1.376% | -6.06 € |
| macd_momentum | 913.30 € (-1.18%) | 46 | 1 | 30% | +0.022% | -1.039% | -1.175% | -11.04 € |
| estocastico_rebote | 923.07 € (-0.13%) | 12 | 9 | 67% | +0.750% | -0.350% | -0.533% | -0.97 € |
| ruptura_estricta | 918.37 € (-0.64%) | 10 | 29 | 40% | +0.049% | -1.051% | -1.277% | -2.43 € |
| macd_sin_salida | 914.19 € (-1.09%) | 35 | 11 | 40% | -0.105% | -1.205% | -1.355% | -9.75 € |
| c_banda_atr_tope | 923.03 € (-0.13%) | 7 | 1 | 57% | +0.502% | -0.598% | -0.771% | -0.97 € |
| ruptura_volumen_tope | 922.16 € (-0.22%) | 7 | 2 | 29% | -0.161% | -1.261% | -1.367% | -2.04 € |
| c_banda_atr_regimen | 916.09 € (-0.88%) | 26 | 8 | 38% | -0.135% | -1.235% | -1.401% | -7.42 € |
| macd_momentum_regimen | 913.30 € (-1.18%) | 46 | 1 | 30% | +0.022% | -1.039% | -1.175% | -11.04 € |
| ruptura_volumen_regimen | 911.45 € (-1.38%) | 36 | 14 | 22% | -0.391% | -1.491% | -1.653% | -12.39 € |
| c_banda_atr_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 13:55 | ruptura_volumen_regimen | XDC | stop-loss | -1.46% | -2.56% | -0.59 |
| 2026-09-30 13:55 | ruptura_volumen_tope | XDC | stop-loss | -1.46% | -2.56% | -0.59 |
| 2026-09-30 13:55 | ruptura_volumen | XDC | stop-loss | -1.46% | -2.56% | -0.59 |
| 2026-09-30 13:45 | ruptura_volumen_regimen | ASTER | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 13:45 | ruptura_volumen_regimen | RENDER | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 13:45 | ruptura_volumen_regimen | BCH | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 13:45 | ruptura_volumen_regimen | ONDO | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 13:45 | macd_momentum_regimen | TRUMP | momentum perdido | -0.33% | -1.13% | -0.26 |
| 2026-09-30 13:45 | macd_momentum_regimen | DASH | momentum perdido | -0.33% | -1.13% | -0.26 |
| 2026-09-30 13:45 | macd_momentum_regimen | SHIB | momentum perdido | -0.35% | -1.15% | -0.27 |
| 2026-09-30 13:45 | macd_momentum_regimen | WLFI | momentum perdido | -0.60% | -1.40% | -0.32 |
| 2026-09-30 13:45 | macd_momentum_regimen | OP | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 13:45 | macd_momentum_regimen | RENDER | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 13:45 | macd_momentum_regimen | BCH | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 13:45 | macd_momentum_regimen | UNI | momentum perdido | -0.72% | -1.82% | -0.42 |

## Eventos de la última vuelta

- 2026-09-30 13:55 [ruptura_volumen] CIERRE XDC stop-loss bruto -1.45% neto -2.55%
- 2026-09-30 13:55 [ruptura_volumen_tope] CIERRE XDC stop-loss bruto -1.45% neto -2.55%
- 2026-09-30 13:55 [ruptura_volumen_regimen] CIERRE XDC stop-loss bruto -1.45% neto -2.55%
- 2026-09-30 13:50 [pullback_tendencia] ENTRADA MON @ 0.02469 (22.95 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
