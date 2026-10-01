# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 22:21 UTC · vueltas 329 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.66 € (-4.28%) | 259 | 25 | 35% | -0.054% | -0.655% | -0.777% | -38.54 € |
| reversion_bb | 917.23 € (-0.76%) | 50 | 18 | 50% | +0.330% | -0.692% | -0.789% | -7.97 € |
| ruptura_volumen | 872.12 € (-5.64%) | 293 | 4 | 25% | -0.201% | -0.790% | -0.899% | -52.20 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.08 € (-3.80%) | 185 | 2 | 15% | -0.200% | -0.842% | -0.932% | -35.38 € |
| macd_momentum | 864.09 € (-6.51%) | 478 | 13 | 21% | -0.007% | -0.562% | -0.665% | -60.16 € |
| estocastico_rebote | 872.01 € (-5.65%) | 319 | 17 | 30% | -0.150% | -0.731% | -0.841% | -52.61 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 873.36 € (-5.50%) | 331 | 21 | 35% | -0.086% | -0.665% | -0.778% | -49.80 € |
| c_banda_atr_tope | 910.95 € (-1.44%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.82 € (-1.99%) | 99 | 2 | 27% | -0.039% | -0.806% | -0.922% | -18.28 € |
| c_banda_atr_regimen | 896.40 € (-3.01%) | 130 | 8 | 31% | -0.218% | -0.919% | -1.055% | -27.34 € |
| macd_momentum_regimen | 885.47 € (-4.19%) | 274 | 2 | 20% | -0.030% | -0.625% | -0.731% | -38.83 € |
| ruptura_volumen_regimen | 875.34 € (-5.29%) | 226 | 4 | 19% | -0.344% | -0.959% | -1.074% | -48.97 € |
| c_banda_atr_evento | 890.54 € (-3.65%) | 226 | 25 | 35% | -0.017% | -0.634% | -0.750% | -32.64 € |
| macd_momentum_evento | 868.88 € (-5.99%) | 431 | 13 | 19% | -0.011% | -0.572% | -0.671% | -55.37 € |
| ruptura_volumen_evento | 884.53 € (-4.30%) | 243 | 4 | 26% | -0.114% | -0.722% | -0.822% | -39.78 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 22:20 | ruptura_volumen_evento | ICP | timeout | -0.58% | -1.08% | -0.24 |
| 2026-10-01 22:20 | ruptura_volumen_regimen | ICP | timeout | -0.58% | -1.08% | -0.24 |
| 2026-10-01 22:20 | ruptura_volumen_tope | ICP | timeout | -0.58% | -1.08% | -0.25 |
| 2026-10-01 22:20 | estocastico_rebote | VVV | timeout | +0.30% | -0.20% | -0.04 |
| 2026-10-01 22:20 | ruptura_volumen | ICP | timeout | -0.58% | -1.08% | -0.24 |
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

## Eventos de la última vuelta

- 2026-10-01 22:15 [macd_momentum] ENTRADA AVAX @ 9.765 (21.60 €, apertura)
- 2026-10-01 22:15 [macd_sin_salida] ENTRADA AVAX @ 9.765 (21.86 €, apertura)
- 2026-10-01 22:15 [macd_momentum_evento] ENTRADA AVAX @ 9.765 (21.72 €, apertura)
- 2026-10-01 22:20 [ruptura_volumen] CIERRE ICP timeout bruto -0.58% neto -1.08%
- 2026-10-01 22:20 [ruptura_volumen_tope] CIERRE ICP timeout bruto -0.58% neto -1.08%
- 2026-10-01 22:20 [ruptura_volumen_regimen] CIERRE ICP timeout bruto -0.58% neto -1.08%
- 2026-10-01 22:20 [ruptura_volumen_evento] CIERRE ICP timeout bruto -0.58% neto -1.08%
- 2026-10-01 22:15 [macd_momentum] ENTRADA FIL @ 0.901 (21.60 €, apertura)
- 2026-10-01 22:15 [macd_sin_salida] ENTRADA FIL @ 0.901 (21.86 €, apertura)
- 2026-10-01 22:15 [macd_momentum_evento] ENTRADA FIL @ 0.901 (21.72 €, apertura)
- 2026-10-01 22:20 [estocastico_rebote] CIERRE VVV timeout bruto +0.30% neto -0.20%
- 2026-10-01 22:15 [macd_momentum] ENTRADA TRUMP @ 1.833 (21.60 €, apertura)
- 2026-10-01 22:15 [macd_sin_salida] ENTRADA TRUMP @ 1.833 (21.86 €, apertura)
- 2026-10-01 22:15 [macd_momentum_evento] ENTRADA TRUMP @ 1.833 (21.72 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
