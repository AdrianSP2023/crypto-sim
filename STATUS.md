# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 00:26 UTC · vueltas 76 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.01 € (-2.41%) | 84 | 21 | 26% | -0.320% | -1.131% | -1.260% | -21.79 € |
| reversion_bb | 921.86 € (-0.26%) | 10 | 5 | 40% | -0.070% | -1.170% | -1.295% | -2.71 € |
| ruptura_volumen | 894.36 € (-3.23%) | 98 | 22 | 17% | -0.467% | -1.233% | -1.357% | -27.67 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.52 € (-2.24%) | 74 | 2 | 15% | -0.373% | -1.229% | -1.355% | -20.84 € |
| macd_momentum | 901.20 € (-2.49%) | 135 | 4 | 24% | -0.056% | -0.750% | -0.864% | -23.17 € |
| estocastico_rebote | 902.18 € (-2.39%) | 131 | 12 | 34% | -0.041% | -0.741% | -0.864% | -22.31 € |
| ruptura_estricta | 898.00 € (-2.84%) | 53 | 8 | 15% | -1.035% | -2.034% | -2.177% | -24.82 € |
| macd_sin_salida | 902.22 € (-2.38%) | 90 | 28 | 33% | -0.220% | -1.010% | -1.138% | -20.91 € |
| c_banda_atr_tope | 918.99 € (-0.57%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.248% | -5.10 € |
| ruptura_volumen_tope | 915.75 € (-0.92%) | 30 | 3 | 20% | -0.069% | -1.169% | -1.253% | -8.08 € |
| c_banda_atr_regimen | 906.93 € (-1.87%) | 47 | 7 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.47 € (-1.71%) | 76 | 0 | 25% | -0.058% | -0.902% | -1.028% | -15.78 € |
| ruptura_volumen_regimen | 895.89 € (-3.07%) | 77 | 20 | 14% | -0.651% | -1.490% | -1.625% | -26.29 € |
| c_banda_atr_evento | 908.63 € (-1.69%) | 51 | 21 | 24% | -0.327% | -1.292% | -1.401% | -15.16 € |
| macd_momentum_evento | 906.20 € (-1.95%) | 88 | 4 | 17% | -0.102% | -0.902% | -1.004% | -18.18 € |
| ruptura_volumen_evento | 907.22 € (-1.84%) | 48 | 22 | 15% | -0.300% | -1.338% | -1.435% | -14.78 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 00:25 | ruptura_volumen_evento | MON | take-profit | +2.50% | +2.00% | +0.46 |
| 2026-10-01 00:25 | c_banda_atr_evento | VVV | timeout | +0.05% | -0.75% | -0.17 |
| 2026-10-01 00:25 | c_banda_atr_evento | POL | timeout | +0.46% | -0.34% | -0.08 |
| 2026-10-01 00:25 | c_banda_atr_evento | AVAX | timeout | -0.46% | -1.25% | -0.29 |
| 2026-10-01 00:25 | ruptura_volumen_regimen | MON | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 00:25 | ruptura_volumen_tope | MON | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-10-01 00:25 | ruptura_estricta | MON | take-profit | +3.00% | +2.50% | +0.56 |
| 2026-10-01 00:25 | estocastico_rebote | NIGHT | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 00:25 | pullback_tendencia | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 00:25 | ruptura_volumen | MON | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 00:25 | c_banda_atr | VVV | timeout | +0.05% | -0.45% | -0.10 |
| 2026-10-01 00:25 | c_banda_atr | POL | timeout | +0.46% | -0.04% | -0.01 |
| 2026-10-01 00:25 | c_banda_atr | AVAX | timeout | -0.46% | -0.95% | -0.22 |
| 2026-10-01 00:20 | c_banda_atr_evento | PEPE | timeout | -1.08% | -1.88% | -0.43 |
| 2026-10-01 00:20 | c_banda_atr_evento | JUP | timeout | +0.29% | -0.51% | -0.12 |

## Eventos de la última vuelta

- 2026-10-01 00:20 [estocastico_rebote] ENTRADA ETH @ 2365.05 (22.54 €, apertura)
- 2026-10-01 00:25 [c_banda_atr] CIERRE AVAX timeout bruto -0.46% neto -0.96%
- 2026-10-01 00:25 [c_banda_atr_evento] CIERRE AVAX timeout bruto -0.46% neto -1.26%
- 2026-10-01 00:25 [c_banda_atr] CIERRE POL timeout bruto +0.46% neto -0.04%
- 2026-10-01 00:25 [c_banda_atr_evento] CIERRE POL timeout bruto +0.46% neto -0.34%
- 2026-10-01 00:25 [pullback_tendencia] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-10-01 00:25 [estocastico_rebote] CIERRE NIGHT take-profit bruto +1.80% neto +1.30%
- 2026-10-01 00:25 [ruptura_volumen] CIERRE MON take-profit bruto +2.50% neto +2.00%
- 2026-10-01 00:25 [ruptura_estricta] CIERRE MON take-profit bruto +3.00% neto +2.50%
- 2026-10-01 00:25 [ruptura_volumen_tope] CIERRE MON take-profit bruto +2.50% neto +1.40%
- 2026-10-01 00:25 [ruptura_volumen_regimen] CIERRE MON take-profit bruto +2.50% neto +2.00%
- 2026-10-01 00:25 [ruptura_volumen_evento] CIERRE MON take-profit bruto +2.50% neto +2.00%
- 2026-10-01 00:25 [c_banda_atr] CIERRE VVV timeout bruto +0.05% neto -0.45%
- 2026-10-01 00:25 [c_banda_atr_evento] CIERRE VVV timeout bruto +0.05% neto -0.75%
- 2026-10-01 00:20 [macd_momentum] ENTRADA APT @ 0.6847 (22.53 €, apertura)
- 2026-10-01 00:20 [macd_sin_salida] ENTRADA APT @ 0.6847 (22.58 €, apertura)
- 2026-10-01 00:20 [macd_momentum_evento] ENTRADA APT @ 0.6847 (22.65 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
