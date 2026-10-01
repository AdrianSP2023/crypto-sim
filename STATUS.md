# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 22:06 UTC · vueltas 326 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.68 € (-4.28%) | 259 | 13 | 35% | -0.054% | -0.655% | -0.777% | -38.54 € |
| reversion_bb | 916.71 € (-0.82%) | 50 | 18 | 50% | +0.330% | -0.692% | -0.789% | -7.97 € |
| ruptura_volumen | 872.61 € (-5.59%) | 292 | 5 | 25% | -0.200% | -0.789% | -0.898% | -51.96 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.17 € (-3.80%) | 185 | 2 | 15% | -0.200% | -0.842% | -0.932% | -35.38 € |
| macd_momentum | 864.26 € (-6.49%) | 477 | 4 | 21% | -0.007% | -0.562% | -0.665% | -60.02 € |
| estocastico_rebote | 872.95 € (-5.55%) | 312 | 23 | 31% | -0.144% | -0.728% | -0.838% | -51.23 € |
| ruptura_estricta | 883.07 € (-4.45%) | 165 | 1 | 25% | -0.432% | -1.092% | -1.208% | -40.99 € |
| macd_sin_salida | 873.19 € (-5.52%) | 331 | 17 | 35% | -0.086% | -0.665% | -0.778% | -49.80 € |
| c_banda_atr_tope | 910.77 € (-1.46%) | 61 | 4 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 906.22 € (-1.95%) | 98 | 3 | 28% | -0.034% | -0.803% | -0.919% | -18.03 € |
| c_banda_atr_regimen | 896.29 € (-3.02%) | 130 | 8 | 31% | -0.218% | -0.919% | -1.055% | -27.34 € |
| macd_momentum_regimen | 885.46 € (-4.20%) | 274 | 2 | 20% | -0.030% | -0.625% | -0.731% | -38.83 € |
| ruptura_volumen_regimen | 875.84 € (-5.24%) | 225 | 5 | 20% | -0.343% | -0.959% | -1.074% | -48.73 € |
| c_banda_atr_evento | 890.57 € (-3.64%) | 226 | 13 | 35% | -0.017% | -0.634% | -0.750% | -32.64 € |
| macd_momentum_evento | 869.05 € (-5.97%) | 430 | 4 | 19% | -0.011% | -0.572% | -0.671% | -55.23 € |
| ruptura_volumen_evento | 885.03 € (-4.24%) | 242 | 5 | 26% | -0.112% | -0.721% | -0.821% | -39.54 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 22:05 | macd_momentum_evento | TON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 22:05 | macd_momentum_regimen | TON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 22:05 | macd_sin_salida | TON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 22:05 | estocastico_rebote | DOGE | timeout | -0.91% | -1.41% | -0.31 |
| 2026-10-01 22:05 | estocastico_rebote | SUI | timeout | +0.09% | -0.41% | -0.09 |
| 2026-10-01 22:05 | estocastico_rebote | BTC | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 22:05 | macd_momentum | TON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 21:55 | estocastico_rebote | USELESS | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 21:55 | estocastico_rebote | ZRO | stop-loss | -1.63% | -2.13% | -0.47 |
| 2026-10-01 21:50 | c_banda_atr_evento | ASTER | stop-loss | -1.54% | -2.04% | -0.46 |
| 2026-10-01 21:50 | c_banda_atr_evento | USELESS | stop-loss | -1.90% | -2.40% | -0.54 |
| 2026-10-01 21:50 | c_banda_atr_regimen | ASTER | stop-loss | -1.54% | -2.04% | -0.46 |
| 2026-10-01 21:50 | c_banda_atr_regimen | USELESS | stop-loss | -1.90% | -2.40% | -0.54 |
| 2026-10-01 21:50 | estocastico_rebote | PUMP | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 21:50 | c_banda_atr | ASTER | stop-loss | -1.54% | -2.04% | -0.45 |

## Eventos de la última vuelta

- 2026-10-01 22:05 [estocastico_rebote] CIERRE BTC timeout bruto -0.16% neto -0.66%
- 2026-10-01 22:05 [estocastico_rebote] CIERRE SUI timeout bruto +0.09% neto -0.41%
- 2026-10-01 22:00 [estocastico_rebote] ENTRADA PUMP @ 0.005065 (21.83 €, apertura)
- 2026-10-01 22:00 [c_banda_atr_tope] ENTRADA LTC @ 60.93 (22.78 €, apertura)
- 2026-10-01 22:00 [estocastico_rebote] ENTRADA ZRO @ 1.572 (21.83 €, apertura)
- 2026-10-01 22:05 [estocastico_rebote] CIERRE DOGE timeout bruto -0.91% neto -1.41%
- 2026-10-01 22:05 [macd_momentum] CIERRE TON take-profit bruto +2.00% neto +1.50%
- 2026-10-01 22:05 [macd_sin_salida] CIERRE TON take-profit bruto +2.00% neto +1.50%
- 2026-10-01 22:05 [macd_momentum_regimen] CIERRE TON take-profit bruto +2.00% neto +1.50%
- 2026-10-01 22:05 [macd_momentum_evento] CIERRE TON take-profit bruto +2.00% neto +1.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
