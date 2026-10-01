# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 19:47 UTC · vueltas 298 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.50 € (-3.98%) | 243 | 16 | 36% | -0.033% | -0.641% | -0.763% | -35.45 € |
| reversion_bb | 916.74 € (-0.81%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 873.48 € (-5.49%) | 284 | 5 | 24% | -0.203% | -0.795% | -0.903% | -50.94 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.38 € (-3.66%) | 175 | 2 | 15% | -0.201% | -0.852% | -0.945% | -33.89 € |
| macd_momentum | 870.48 € (-5.82%) | 439 | 0 | 22% | +0.015% | -0.545% | -0.649% | -53.76 € |
| estocastico_rebote | 875.57 € (-5.27%) | 290 | 25 | 31% | -0.130% | -0.720% | -0.832% | -47.24 € |
| ruptura_estricta | 883.05 € (-4.46%) | 152 | 13 | 25% | -0.452% | -1.126% | -1.243% | -39.01 € |
| macd_sin_salida | 880.64 € (-4.72%) | 299 | 18 | 36% | -0.044% | -0.632% | -0.748% | -42.93 € |
| c_banda_atr_tope | 911.54 € (-1.37%) | 55 | 5 | 31% | +0.014% | -0.966% | -1.084% | -12.21 € |
| ruptura_volumen_tope | 907.76 € (-1.78%) | 93 | 1 | 29% | +0.019% | -0.765% | -0.878% | -16.32 € |
| c_banda_atr_regimen | 899.07 € (-2.72%) | 116 | 15 | 34% | -0.153% | -0.878% | -1.018% | -23.37 € |
| macd_momentum_regimen | 891.29 € (-3.57%) | 239 | 0 | 22% | +0.003% | -0.606% | -0.715% | -32.95 € |
| ruptura_volumen_regimen | 876.39 € (-5.18%) | 218 | 5 | 19% | -0.355% | -0.975% | -1.090% | -48.03 € |
| c_banda_atr_evento | 893.40 € (-3.34%) | 210 | 16 | 37% | +0.010% | -0.616% | -0.732% | -29.53 € |
| macd_momentum_evento | 875.31 € (-5.29%) | 392 | 0 | 20% | +0.013% | -0.554% | -0.654% | -48.94 € |
| ruptura_volumen_evento | 885.91 € (-4.15%) | 234 | 5 | 25% | -0.113% | -0.725% | -0.824% | -38.50 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 19:45 | ruptura_volumen_evento | BCH | timeout | -0.93% | -1.43% | -0.32 |
| 2026-10-01 19:45 | ruptura_volumen_evento | XRP | timeout | -0.61% | -1.11% | -0.25 |
| 2026-10-01 19:45 | ruptura_volumen_regimen | BCH | timeout | -0.93% | -1.43% | -0.32 |
| 2026-10-01 19:45 | ruptura_volumen_regimen | XRP | timeout | -0.61% | -1.11% | -0.24 |
| 2026-10-01 19:45 | pullback_tendencia | ZRO | take-profit | +2.12% | +1.62% | +0.36 |
| 2026-10-01 19:45 | rebote_extremo | VVV | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-10-01 19:45 | ruptura_volumen | BCH | timeout | -0.93% | -1.43% | -0.31 |
| 2026-10-01 19:45 | ruptura_volumen | XRP | timeout | -0.61% | -1.11% | -0.24 |
| 2026-10-01 19:45 | reversion_bb | NEAR | take-profit | +1.50% | +1.00% | +0.23 |
| 2026-10-01 19:40 | c_banda_atr_evento | SEI | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-10-01 19:40 | ruptura_volumen_regimen | PENGU | stop-loss | -1.29% | -1.79% | -0.39 |
| 2026-10-01 19:40 | c_banda_atr_regimen | SEI | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-10-01 19:40 | ruptura_estricta | BNB | timeout | +0.10% | -0.40% | -0.09 |
| 2026-10-01 19:40 | pullback_tendencia | LINK | rotura de tendencia | -0.17% | -0.67% | -0.15 |
| 2026-10-01 19:40 | c_banda_atr | SEI | stop-loss | -1.56% | -2.06% | -0.46 |

## Eventos de la última vuelta

- 2026-10-01 19:45 [ruptura_volumen] CIERRE XRP timeout bruto -0.61% neto -1.11%
- 2026-10-01 19:45 [ruptura_volumen_regimen] CIERRE XRP timeout bruto -0.61% neto -1.11%
- 2026-10-01 19:45 [ruptura_volumen_evento] CIERRE XRP timeout bruto -0.61% neto -1.11%
- 2026-10-01 19:45 [reversion_bb] CIERRE NEAR take-profit bruto +1.50% neto +1.00%
- 2026-10-01 19:40 [estocastico_rebote] ENTRADA LTC @ 60.25 (21.92 €, apertura)
- 2026-10-01 19:45 [pullback_tendencia] CIERRE ZRO take-profit bruto +2.12% neto +1.62%
- 2026-10-01 19:40 [reversion_bb] ENTRADA XDC @ 0.03042 (22.92 €, apertura)
- 2026-10-01 19:45 [ruptura_volumen] CIERRE BCH timeout bruto -0.93% neto -1.43%
- 2026-10-01 19:45 [ruptura_volumen_regimen] CIERRE BCH timeout bruto -0.93% neto -1.43%
- 2026-10-01 19:45 [ruptura_volumen_evento] CIERRE BCH timeout bruto -0.93% neto -1.43%
- 2026-10-01 19:45 [rebote_extremo] CIERRE VVV take-profit bruto +2.00% neto +0.90%
- 2026-10-01 19:40 [estocastico_rebote] ENTRADA SHIB @ 5.128e-06 (21.92 €, apertura)
- 2026-10-01 19:40 [pullback_tendencia] ENTRADA SKY @ 0.0741 (22.26 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
