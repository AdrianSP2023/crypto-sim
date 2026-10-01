# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 23:02 UTC · vueltas 337 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.56 € (-4.29%) | 260 | 25 | 35% | -0.053% | -0.653% | -0.775% | -38.57 € |
| reversion_bb | 917.04 € (-0.78%) | 51 | 17 | 49% | +0.294% | -0.718% | -0.815% | -8.44 € |
| ruptura_volumen | 871.72 € (-5.68%) | 296 | 3 | 25% | -0.198% | -0.786% | -0.894% | -52.43 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.07 € (-3.80%) | 185 | 5 | 15% | -0.200% | -0.842% | -0.932% | -35.38 € |
| macd_momentum | 863.94 € (-6.52%) | 480 | 16 | 21% | -0.007% | -0.562% | -0.665% | -60.39 € |
| estocastico_rebote | 871.89 € (-5.66%) | 325 | 12 | 30% | -0.135% | -0.716% | -0.825% | -52.45 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 872.71 € (-5.58%) | 335 | 20 | 35% | -0.089% | -0.667% | -0.780% | -50.55 € |
| c_banda_atr_tope | 911.04 € (-1.43%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.67 € (-2.01%) | 100 | 3 | 27% | -0.043% | -0.807% | -0.922% | -18.48 € |
| c_banda_atr_regimen | 896.34 € (-3.02%) | 131 | 7 | 31% | -0.214% | -0.913% | -1.049% | -27.37 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 275 | 1 | 20% | -0.029% | -0.624% | -0.731% | -38.93 € |
| ruptura_volumen_regimen | 874.93 € (-5.34%) | 229 | 1 | 20% | -0.337% | -0.951% | -1.066% | -49.20 € |
| c_banda_atr_evento | 890.45 € (-3.66%) | 227 | 25 | 35% | -0.015% | -0.631% | -0.748% | -32.67 € |
| macd_momentum_evento | 868.73 € (-6.01%) | 433 | 16 | 19% | -0.011% | -0.572% | -0.671% | -55.60 € |
| ruptura_volumen_evento | 884.12 € (-4.34%) | 246 | 3 | 26% | -0.111% | -0.718% | -0.818% | -40.01 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 23:00 | macd_sin_salida | BCH | timeout | +0.47% | -0.03% | -0.01 |
| 2026-10-01 22:55 | ruptura_volumen_evento | TON | timeout | +0.65% | +0.15% | +0.03 |
| 2026-10-01 22:55 | macd_momentum_evento | SPX | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-10-01 22:55 | ruptura_volumen_regimen | TON | timeout | +0.65% | +0.15% | +0.03 |
| 2026-10-01 22:55 | macd_sin_salida | ARB | timeout | -0.84% | -1.34% | -0.30 |
| 2026-10-01 22:55 | macd_sin_salida | UNI | timeout | -0.53% | -1.03% | -0.23 |
| 2026-10-01 22:55 | estocastico_rebote | MINA | take-profit | +1.89% | +1.39% | +0.30 |
| 2026-10-01 22:55 | macd_momentum | SPX | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-10-01 22:55 | ruptura_volumen | TON | timeout | +0.65% | +0.15% | +0.03 |
| 2026-10-01 22:50 | macd_sin_salida | WLD | timeout | -0.52% | -1.01% | -0.22 |
| 2026-10-01 22:50 | estocastico_rebote | LINK | timeout | -0.97% | -1.47% | -0.32 |
| 2026-10-01 22:50 | reversion_bb | USELESS | stop-loss | -1.52% | -2.02% | -0.46 |
| 2026-10-01 22:45 | ruptura_volumen_evento | BCH | timeout | +0.20% | -0.30% | -0.07 |
| 2026-10-01 22:45 | ruptura_volumen_regimen | BCH | timeout | +0.20% | -0.30% | -0.07 |
| 2026-10-01 22:45 | estocastico_rebote | XMR | timeout | +0.38% | -0.12% | -0.03 |

## Eventos de la última vuelta

- 2026-10-01 22:55 [pullback_tendencia] ENTRADA ETH @ 2403.63 (22.22 €, apertura)
- 2026-10-01 22:55 [pullback_tendencia] ENTRADA PUMP @ 0.005178 (22.22 €, apertura)
- 2026-10-01 22:55 [pullback_tendencia] ENTRADA BCH @ 275.21 (22.22 €, apertura)
- 2026-10-01 23:00 [macd_sin_salida] CIERRE BCH timeout bruto +0.47% neto -0.03%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
