# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 22:16 UTC · vueltas 328 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.47 € (-4.30%) | 259 | 25 | 35% | -0.054% | -0.655% | -0.777% | -38.54 € |
| reversion_bb | 917.24 € (-0.76%) | 50 | 18 | 50% | +0.330% | -0.692% | -0.789% | -7.97 € |
| ruptura_volumen | 872.30 € (-5.62%) | 292 | 5 | 25% | -0.200% | -0.789% | -0.898% | -51.96 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.22 € (-3.79%) | 185 | 2 | 15% | -0.200% | -0.842% | -0.932% | -35.38 € |
| macd_momentum | 864.10 € (-6.51%) | 478 | 10 | 21% | -0.007% | -0.562% | -0.665% | -60.16 € |
| estocastico_rebote | 872.09 € (-5.64%) | 318 | 18 | 30% | -0.151% | -0.733% | -0.842% | -52.56 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 873.39 € (-5.50%) | 331 | 18 | 35% | -0.086% | -0.665% | -0.778% | -49.80 € |
| c_banda_atr_tope | 910.66 € (-1.47%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.89 € (-1.99%) | 98 | 3 | 28% | -0.034% | -0.803% | -0.919% | -18.03 € |
| c_banda_atr_regimen | 896.38 € (-3.01%) | 130 | 8 | 31% | -0.218% | -0.919% | -1.055% | -27.34 € |
| macd_momentum_regimen | 885.47 € (-4.20%) | 274 | 2 | 20% | -0.030% | -0.625% | -0.731% | -38.83 € |
| ruptura_volumen_regimen | 875.52 € (-5.27%) | 225 | 5 | 20% | -0.343% | -0.959% | -1.074% | -48.73 € |
| c_banda_atr_evento | 890.36 € (-3.67%) | 226 | 25 | 35% | -0.017% | -0.634% | -0.750% | -32.64 € |
| macd_momentum_evento | 868.89 € (-5.99%) | 431 | 10 | 19% | -0.011% | -0.572% | -0.671% | -55.37 € |
| ruptura_volumen_evento | 884.71 € (-4.28%) | 242 | 5 | 26% | -0.112% | -0.721% | -0.821% | -39.54 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 22:15 | estocastico_rebote | UNI | timeout | -0.21% | -0.71% | -0.16 |
| 2026-10-01 22:10 | macd_momentum_evento | SKY | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-10-01 22:10 | ruptura_estricta | AVAX | timeout | -0.75% | -1.25% | -0.28 |
| 2026-10-01 22:10 | estocastico_rebote | TRUMP | timeout | -0.44% | -0.94% | -0.20 |
| 2026-10-01 22:10 | estocastico_rebote | RENDER | timeout | -0.82% | -1.32% | -0.29 |
| 2026-10-01 22:10 | estocastico_rebote | SOL | timeout | -0.61% | -1.11% | -0.24 |
| 2026-10-01 22:10 | estocastico_rebote | ETH | timeout | -0.32% | -0.82% | -0.18 |
| 2026-10-01 22:10 | estocastico_rebote | XRP | timeout | -0.67% | -1.17% | -0.26 |
| 2026-10-01 22:10 | macd_momentum | SKY | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-10-01 22:05 | macd_momentum_evento | TON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 22:05 | macd_momentum_regimen | TON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 22:05 | macd_sin_salida | TON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 22:05 | estocastico_rebote | DOGE | timeout | -0.91% | -1.41% | -0.31 |
| 2026-10-01 22:05 | estocastico_rebote | SUI | timeout | +0.09% | -0.41% | -0.09 |
| 2026-10-01 22:05 | estocastico_rebote | BTC | timeout | -0.16% | -0.66% | -0.15 |

## Eventos de la última vuelta

- 2026-10-01 22:10 [macd_momentum] ENTRADA AAVE @ 152.14 (21.60 €, apertura)
- 2026-10-01 22:10 [macd_sin_salida] ENTRADA AAVE @ 152.14 (21.86 €, apertura)
- 2026-10-01 22:10 [macd_momentum_evento] ENTRADA AAVE @ 152.14 (21.72 €, apertura)
- 2026-10-01 22:10 [macd_momentum] ENTRADA UNI @ 8.09 (21.60 €, apertura)
- 2026-10-01 22:15 [estocastico_rebote] CIERRE UNI timeout bruto -0.21% neto -0.71%
- 2026-10-01 22:10 [macd_momentum_evento] ENTRADA UNI @ 8.09 (21.72 €, apertura)
- 2026-10-01 22:10 [macd_momentum] ENTRADA POL @ 0.09584 (21.60 €, apertura)
- 2026-10-01 22:10 [macd_momentum_evento] ENTRADA POL @ 0.09584 (21.72 €, apertura)
- 2026-10-01 22:10 [c_banda_atr] ENTRADA ALGO @ 0.10913 (22.14 €, apertura)
- 2026-10-01 22:10 [c_banda_atr_evento] ENTRADA ALGO @ 0.10913 (22.29 €, apertura)
- 2026-10-01 22:10 [c_banda_atr] ENTRADA RENDER @ 1.695 (22.14 €, apertura)
- 2026-10-01 22:10 [c_banda_atr_evento] ENTRADA RENDER @ 1.695 (22.29 €, apertura)
- 2026-10-01 22:10 [c_banda_atr] ENTRADA INJ @ 6.536 (22.14 €, apertura)
- 2026-10-01 22:10 [c_banda_atr_evento] ENTRADA INJ @ 6.536 (22.29 €, apertura)
- 2026-10-01 22:10 [c_banda_atr] ENTRADA SHIB @ 5.134e-06 (22.14 €, apertura)
- 2026-10-01 22:10 [c_banda_atr_evento] ENTRADA SHIB @ 5.134e-06 (22.29 €, apertura)
- 2026-10-01 22:10 [c_banda_atr] ENTRADA PENGU @ 0.008367 (22.14 €, apertura)
- 2026-10-01 22:10 [c_banda_atr_evento] ENTRADA PENGU @ 0.008367 (22.29 €, apertura)
- 2026-10-01 22:10 [c_banda_atr] ENTRADA KSM @ 4.53 (22.14 €, apertura)
- 2026-10-01 22:10 [c_banda_atr_evento] ENTRADA KSM @ 4.53 (22.29 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
