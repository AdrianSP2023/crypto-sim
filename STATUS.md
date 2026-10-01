# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 20:36 UTC · vueltas 308 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.37 € (-3.66%) | 245 | 26 | 36% | -0.031% | -0.637% | -0.760% | -35.54 € |
| reversion_bb | 917.21 € (-0.76%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 873.19 € (-5.52%) | 289 | 4 | 25% | -0.192% | -0.783% | -0.891% | -51.03 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.38 € (-3.66%) | 177 | 6 | 15% | -0.200% | -0.849% | -0.942% | -34.15 € |
| macd_momentum | 870.22 € (-5.84%) | 443 | 34 | 22% | +0.012% | -0.547% | -0.650% | -54.44 € |
| estocastico_rebote | 878.83 € (-4.91%) | 296 | 24 | 32% | -0.106% | -0.695% | -0.806% | -46.53 € |
| ruptura_estricta | 884.07 € (-4.35%) | 157 | 9 | 25% | -0.437% | -1.105% | -1.220% | -39.52 € |
| macd_sin_salida | 880.64 € (-4.72%) | 314 | 30 | 37% | -0.021% | -0.604% | -0.718% | -43.12 € |
| c_banda_atr_tope | 912.06 € (-1.32%) | 57 | 4 | 30% | +0.019% | -0.944% | -1.059% | -12.37 € |
| ruptura_volumen_tope | 907.42 € (-1.82%) | 95 | 4 | 28% | +0.008% | -0.770% | -0.884% | -16.78 € |
| c_banda_atr_regimen | 900.79 € (-2.54%) | 119 | 19 | 33% | -0.145% | -0.864% | -1.002% | -23.58 € |
| macd_momentum_regimen | 891.27 € (-3.57%) | 241 | 33 | 22% | +0.000% | -0.608% | -0.717% | -33.33 € |
| ruptura_volumen_regimen | 875.95 € (-5.22%) | 223 | 3 | 20% | -0.340% | -0.957% | -1.072% | -48.21 € |
| c_banda_atr_evento | 896.29 € (-3.02%) | 212 | 26 | 36% | +0.013% | -0.612% | -0.729% | -29.63 € |
| macd_momentum_evento | 875.04 € (-5.32%) | 396 | 34 | 20% | +0.010% | -0.556% | -0.656% | -49.62 € |
| ruptura_volumen_evento | 885.61 € (-4.18%) | 239 | 4 | 26% | -0.102% | -0.712% | -0.811% | -38.60 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 20:35 | ruptura_volumen_evento | MINA | timeout | +0.97% | +0.47% | +0.10 |
| 2026-10-01 20:35 | macd_momentum_evento | KAS | momentum perdido | -1.04% | -1.54% | -0.34 |
| 2026-10-01 20:35 | macd_momentum_evento | ZRO | momentum perdido | +0.67% | +0.17% | +0.04 |
| 2026-10-01 20:35 | c_banda_atr_evento | CRV | timeout | +0.34% | -0.16% | -0.04 |
| 2026-10-01 20:35 | ruptura_volumen_regimen | MINA | timeout | +0.97% | +0.47% | +0.10 |
| 2026-10-01 20:35 | c_banda_atr_regimen | CRV | timeout | +0.34% | -0.16% | -0.04 |
| 2026-10-01 20:35 | c_banda_atr_regimen | XLM | timeout | +0.01% | -0.49% | -0.11 |
| 2026-10-01 20:35 | c_banda_atr_tope | XLM | timeout | +0.01% | -0.49% | -0.11 |
| 2026-10-01 20:35 | macd_momentum | KAS | momentum perdido | -1.04% | -1.54% | -0.34 |
| 2026-10-01 20:35 | macd_momentum | ZRO | momentum perdido | +0.67% | +0.17% | +0.04 |
| 2026-10-01 20:35 | ruptura_volumen | MINA | timeout | +0.97% | +0.47% | +0.10 |
| 2026-10-01 20:35 | c_banda_atr | CRV | timeout | +0.34% | -0.16% | -0.04 |
| 2026-10-01 20:30 | ruptura_volumen_evento | KAS | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 20:30 | macd_momentum_evento | LINK | momentum perdido | -0.57% | -1.07% | -0.23 |
| 2026-10-01 20:30 | ruptura_volumen_regimen | KAS | stop-loss | -1.56% | -2.06% | -0.45 |

## Eventos de la última vuelta

- 2026-10-01 20:35 [c_banda_atr_tope] CIERRE XLM timeout bruto +0.00% neto -0.50%
- 2026-10-01 20:35 [c_banda_atr_regimen] CIERRE XLM timeout bruto +0.00% neto -0.50%
- 2026-10-01 20:35 [macd_momentum] CIERRE ZRO momentum perdido bruto +0.67% neto +0.17%
- 2026-10-01 20:35 [macd_momentum_evento] CIERRE ZRO momentum perdido bruto +0.67% neto +0.17%
- 2026-10-01 20:35 [c_banda_atr] CIERRE CRV timeout bruto +0.34% neto -0.16%
- 2026-10-01 20:35 [c_banda_atr_regimen] CIERRE CRV timeout bruto +0.34% neto -0.16%
- 2026-10-01 20:35 [c_banda_atr_evento] CIERRE CRV timeout bruto +0.34% neto -0.16%
- 2026-10-01 20:35 [ruptura_volumen] CIERRE MINA timeout bruto +0.97% neto +0.47%
- 2026-10-01 20:35 [ruptura_volumen_regimen] CIERRE MINA timeout bruto +0.97% neto +0.47%
- 2026-10-01 20:35 [ruptura_volumen_evento] CIERRE MINA timeout bruto +0.97% neto +0.47%
- 2026-10-01 20:35 [macd_momentum] CIERRE KAS momentum perdido bruto -1.04% neto -1.54%
- 2026-10-01 20:35 [macd_momentum_evento] CIERRE KAS momentum perdido bruto -1.04% neto -1.54%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
