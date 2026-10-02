# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 04:46 UTC · vueltas 392 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.88 € (-3.50%) | 313 | 22 | 38% | +0.090% | -0.494% | -0.613% | -35.21 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.382% | -4.66 € |
| ruptura_volumen | 870.90 € (-5.77%) | 357 | 38 | 25% | -0.150% | -0.723% | -0.830% | -57.95 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 891.95 € (-3.49%) | 205 | 12 | 18% | -0.119% | -0.747% | -0.835% | -34.79 € |
| macd_momentum | 862.98 € (-6.63%) | 579 | 39 | 22% | +0.047% | -0.498% | -0.599% | -64.41 € |
| estocastico_rebote | 878.91 € (-4.90%) | 367 | 15 | 35% | -0.004% | -0.575% | -0.683% | -47.73 € |
| ruptura_estricta | 890.43 € (-3.66%) | 186 | 36 | 29% | -0.293% | -0.935% | -1.052% | -39.63 € |
| macd_sin_salida | 884.26 € (-4.33%) | 398 | 28 | 39% | +0.077% | -0.488% | -0.598% | -44.25 € |
| c_banda_atr_tope | 912.88 € (-1.23%) | 70 | 5 | 33% | +0.134% | -0.743% | -0.854% | -11.95 € |
| ruptura_volumen_tope | 903.92 € (-2.20%) | 117 | 5 | 26% | -0.045% | -0.771% | -0.885% | -20.64 € |
| c_banda_atr_regimen | 904.62 € (-2.12%) | 166 | 21 | 38% | +0.075% | -0.583% | -0.710% | -22.24 € |
| macd_momentum_regimen | 886.09 € (-4.13%) | 342 | 39 | 22% | +0.042% | -0.534% | -0.638% | -41.37 € |
| ruptura_volumen_regimen | 875.63 € (-5.26%) | 280 | 38 | 21% | -0.251% | -0.844% | -0.957% | -53.25 € |
| c_banda_atr_evento | 897.81 € (-2.86%) | 280 | 22 | 39% | +0.137% | -0.458% | -0.573% | -29.29 € |
| macd_momentum_evento | 867.76 € (-6.11%) | 532 | 39 | 21% | +0.049% | -0.501% | -0.599% | -59.65 € |
| ruptura_volumen_evento | 883.30 € (-4.43%) | 307 | 38 | 26% | -0.072% | -0.658% | -0.759% | -45.62 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 04:45 | ruptura_volumen_evento | AAVE | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 04:45 | macd_momentum_evento | INJ | take-profit | +2.06% | +1.56% | +0.34 |
| 2026-10-02 04:45 | ruptura_volumen_regimen | AAVE | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 04:45 | macd_momentum_regimen | INJ | take-profit | +2.06% | +1.56% | +0.34 |
| 2026-10-02 04:45 | ruptura_volumen_tope | ALGO | timeout | +0.99% | +0.49% | +0.11 |
| 2026-10-02 04:45 | macd_sin_salida | SUI | take-profit | +2.01% | +1.51% | +0.33 |
| 2026-10-02 04:45 | ruptura_estricta | USELESS | take-profit | +3.00% | +2.50% | +0.55 |
| 2026-10-02 04:45 | estocastico_rebote | SUI | take-profit | +1.81% | +1.31% | +0.28 |
| 2026-10-02 04:45 | macd_momentum | INJ | take-profit | +2.06% | +1.56% | +0.33 |
| 2026-10-02 04:45 | ruptura_volumen | AAVE | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 04:40 | ruptura_volumen_evento | PEPE | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 04:40 | macd_momentum_evento | ZRO | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 04:40 | c_banda_atr_evento | TRX | timeout | +0.07% | -0.43% | -0.10 |
| 2026-10-02 04:40 | c_banda_atr_evento | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 04:40 | ruptura_volumen_regimen | PEPE | take-profit | +2.50% | +2.00% | +0.44 |

## Eventos de la última vuelta

- 2026-10-02 04:45 [estocastico_rebote] CIERRE SUI take-profit bruto +1.81% neto +1.31%
- 2026-10-02 04:45 [macd_sin_salida] CIERRE SUI take-profit bruto +2.01% neto +1.51%
- 2026-10-02 04:40 [ruptura_volumen_tope] ENTRADA SUI @ 1.0712 (22.59 €, apertura)
- 2026-10-02 04:45 [ruptura_volumen] CIERRE AAVE take-profit bruto +2.50% neto +2.00%
- 2026-10-02 04:45 [ruptura_volumen_regimen] CIERRE AAVE take-profit bruto +2.50% neto +2.00%
- 2026-10-02 04:45 [ruptura_volumen_evento] CIERRE AAVE take-profit bruto +2.50% neto +2.00%
- 2026-10-02 04:40 [pullback_tendencia] ENTRADA PUMP @ 0.005198 (22.24 €, apertura)
- 2026-10-02 04:45 [ruptura_volumen_tope] CIERRE ALGO timeout bruto +1.00% neto +0.50%
- 2026-10-02 04:45 [ruptura_estricta] CIERRE USELESS take-profit bruto +3.00% neto +2.50%
- 2026-10-02 04:45 [macd_momentum] CIERRE INJ take-profit bruto +2.06% neto +1.56%
- 2026-10-02 04:45 [macd_momentum_regimen] CIERRE INJ take-profit bruto +2.06% neto +1.56%
- 2026-10-02 04:45 [macd_momentum_evento] CIERRE INJ take-profit bruto +2.06% neto +1.56%
- 2026-10-02 04:40 [ruptura_volumen_tope] ENTRADA BNB @ 694.87 (22.59 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
