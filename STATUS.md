# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 19:57 UTC · vueltas 300 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.64 € (-3.74%) | 243 | 19 | 36% | -0.033% | -0.641% | -0.763% | -35.45 € |
| reversion_bb | 916.97 € (-0.79%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 873.78 € (-5.46%) | 285 | 6 | 25% | -0.199% | -0.791% | -0.898% | -50.85 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.50 € (-3.65%) | 175 | 3 | 15% | -0.201% | -0.852% | -0.945% | -33.89 € |
| macd_momentum | 870.69 € (-5.79%) | 439 | 3 | 22% | +0.015% | -0.545% | -0.649% | -53.76 € |
| estocastico_rebote | 878.32 € (-4.97%) | 291 | 28 | 31% | -0.123% | -0.713% | -0.825% | -46.95 € |
| ruptura_estricta | 884.52 € (-4.30%) | 152 | 13 | 25% | -0.452% | -1.126% | -1.243% | -39.01 € |
| macd_sin_salida | 882.12 € (-4.56%) | 299 | 21 | 36% | -0.044% | -0.632% | -0.748% | -42.93 € |
| c_banda_atr_tope | 912.20 € (-1.30%) | 56 | 5 | 30% | +0.019% | -0.953% | -1.068% | -12.26 € |
| ruptura_volumen_tope | 907.82 € (-1.78%) | 93 | 3 | 29% | +0.019% | -0.765% | -0.878% | -16.32 € |
| c_banda_atr_regimen | 900.63 € (-2.55%) | 116 | 15 | 34% | -0.153% | -0.878% | -1.018% | -23.37 € |
| macd_momentum_regimen | 891.29 € (-3.57%) | 239 | 0 | 22% | +0.003% | -0.606% | -0.715% | -32.95 € |
| ruptura_volumen_regimen | 876.69 € (-5.14%) | 219 | 4 | 19% | -0.349% | -0.968% | -1.083% | -47.94 € |
| c_banda_atr_evento | 895.56 € (-3.10%) | 210 | 19 | 37% | +0.010% | -0.616% | -0.732% | -29.53 € |
| macd_momentum_evento | 875.51 € (-5.27%) | 392 | 3 | 20% | +0.013% | -0.554% | -0.654% | -48.94 € |
| ruptura_volumen_evento | 886.21 € (-4.11%) | 235 | 6 | 26% | -0.108% | -0.721% | -0.819% | -38.41 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 19:55 | ruptura_volumen_evento | JUP | timeout | +0.93% | +0.43% | +0.10 |
| 2026-10-01 19:55 | ruptura_volumen_regimen | JUP | timeout | +0.93% | +0.43% | +0.09 |
| 2026-10-01 19:55 | estocastico_rebote | PUMP | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-01 19:55 | ruptura_volumen | JUP | timeout | +0.93% | +0.43% | +0.09 |
| 2026-10-01 19:50 | c_banda_atr_tope | BTC | timeout | +0.31% | -0.19% | -0.04 |
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

## Eventos de la última vuelta

- 2026-10-01 19:50 [estocastico_rebote] ENTRADA LINK @ 12.8213 (21.92 €, apertura)
- 2026-10-01 19:50 [c_banda_atr] ENTRADA SUI @ 1.0476 (22.22 €, apertura)
- 2026-10-01 19:50 [c_banda_atr_evento] ENTRADA SUI @ 1.0476 (22.37 €, apertura)
- 2026-10-01 19:55 [estocastico_rebote] CIERRE PUMP take-profit bruto +1.80% neto +1.30%
- 2026-10-01 19:50 [macd_momentum] ENTRADA ZRO @ 1.644 (21.76 €, apertura)
- 2026-10-01 19:50 [macd_sin_salida] ENTRADA ZRO @ 1.644 (22.03 €, apertura)
- 2026-10-01 19:50 [macd_momentum_evento] ENTRADA ZRO @ 1.644 (21.88 €, apertura)
- 2026-10-01 19:50 [ruptura_volumen] ENTRADA WLD @ 0.4462 (21.83 €, apertura)
- 2026-10-01 19:50 [macd_momentum] ENTRADA WLD @ 0.4462 (21.76 €, apertura)
- 2026-10-01 19:50 [macd_sin_salida] ENTRADA WLD @ 0.4462 (22.03 €, apertura)
- 2026-10-01 19:50 [ruptura_volumen_tope] ENTRADA WLD @ 0.4462 (22.70 €, apertura)
- 2026-10-01 19:50 [macd_momentum_evento] ENTRADA WLD @ 0.4462 (21.88 €, apertura)
- 2026-10-01 19:50 [ruptura_volumen_evento] ENTRADA WLD @ 0.4462 (22.14 €, apertura)
- 2026-10-01 19:55 [ruptura_volumen] CIERRE JUP timeout bruto +0.93% neto +0.43%
- 2026-10-01 19:50 [estocastico_rebote] ENTRADA JUP @ 0.29271 (21.93 €, apertura)
- 2026-10-01 19:55 [ruptura_volumen_regimen] CIERRE JUP timeout bruto +0.93% neto +0.43%
- 2026-10-01 19:55 [ruptura_volumen_evento] CIERRE JUP timeout bruto +0.93% neto +0.43%
- 2026-10-01 19:50 [ruptura_volumen] ENTRADA KAS @ 0.03748 (21.83 €, apertura)
- 2026-10-01 19:50 [macd_momentum] ENTRADA KAS @ 0.03748 (21.76 €, apertura)
- 2026-10-01 19:50 [macd_sin_salida] ENTRADA KAS @ 0.03748 (22.03 €, apertura)
- 2026-10-01 19:50 [ruptura_volumen_tope] ENTRADA KAS @ 0.03748 (22.70 €, apertura)
- 2026-10-01 19:50 [macd_momentum_evento] ENTRADA KAS @ 0.03748 (21.88 €, apertura)
- 2026-10-01 19:50 [ruptura_volumen_evento] ENTRADA KAS @ 0.03748 (22.15 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
