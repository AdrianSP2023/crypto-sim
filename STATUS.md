# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 19:42 UTC · vueltas 297 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.11 € (-4.02%) | 243 | 16 | 36% | -0.033% | -0.641% | -0.763% | -35.45 € |
| reversion_bb | 916.64 € (-0.82%) | 48 | 2 | 50% | +0.344% | -0.700% | -0.796% | -7.74 € |
| ruptura_volumen | 873.64 € (-5.47%) | 282 | 7 | 24% | -0.199% | -0.792% | -0.900% | -50.38 € |
| rebote_extremo | 922.12 € (-0.23%) | 13 | 1 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 890.48 € (-3.65%) | 174 | 2 | 15% | -0.215% | -0.866% | -0.960% | -34.25 € |
| macd_momentum | 870.48 € (-5.82%) | 439 | 0 | 22% | +0.015% | -0.545% | -0.649% | -53.76 € |
| estocastico_rebote | 874.40 € (-5.39%) | 290 | 23 | 31% | -0.130% | -0.720% | -0.832% | -47.24 € |
| ruptura_estricta | 882.77 € (-4.49%) | 152 | 13 | 25% | -0.452% | -1.126% | -1.243% | -39.01 € |
| macd_sin_salida | 880.20 € (-4.76%) | 299 | 18 | 36% | -0.044% | -0.632% | -0.748% | -42.93 € |
| c_banda_atr_tope | 911.45 € (-1.38%) | 55 | 5 | 31% | +0.014% | -0.966% | -1.084% | -12.21 € |
| ruptura_volumen_tope | 907.76 € (-1.78%) | 93 | 1 | 29% | +0.019% | -0.765% | -0.878% | -16.32 € |
| c_banda_atr_regimen | 898.62 € (-2.77%) | 116 | 15 | 34% | -0.153% | -0.878% | -1.018% | -23.37 € |
| macd_momentum_regimen | 891.29 € (-3.57%) | 239 | 0 | 22% | +0.003% | -0.606% | -0.715% | -32.95 € |
| ruptura_volumen_regimen | 876.54 € (-5.16%) | 216 | 7 | 19% | -0.351% | -0.972% | -1.088% | -47.47 € |
| c_banda_atr_evento | 893.02 € (-3.38%) | 210 | 16 | 37% | +0.010% | -0.616% | -0.732% | -29.53 € |
| macd_momentum_evento | 875.31 € (-5.29%) | 392 | 0 | 20% | +0.013% | -0.554% | -0.654% | -48.94 € |
| ruptura_volumen_evento | 886.07 € (-4.13%) | 232 | 7 | 25% | -0.107% | -0.721% | -0.820% | -37.94 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 19:40 | c_banda_atr_evento | SEI | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-10-01 19:40 | ruptura_volumen_regimen | PENGU | stop-loss | -1.29% | -1.79% | -0.39 |
| 2026-10-01 19:40 | c_banda_atr_regimen | SEI | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-10-01 19:40 | ruptura_estricta | BNB | timeout | +0.10% | -0.40% | -0.09 |
| 2026-10-01 19:40 | pullback_tendencia | LINK | rotura de tendencia | -0.17% | -0.67% | -0.15 |
| 2026-10-01 19:40 | c_banda_atr | SEI | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-10-01 19:35 | ruptura_volumen_evento | FIL | stop-loss | -1.42% | -1.92% | -0.43 |
| 2026-10-01 19:35 | ruptura_volumen_evento | DOT | timeout | -0.38% | -0.88% | -0.20 |
| 2026-10-01 19:35 | ruptura_volumen_evento | HYPE | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 19:35 | macd_momentum_evento | AVAX | momentum perdido | +0.13% | -0.37% | -0.08 |
| 2026-10-01 19:35 | macd_momentum_evento | LINK | momentum perdido | -0.42% | -0.92% | -0.20 |
| 2026-10-01 19:35 | ruptura_volumen_regimen | FIL | stop-loss | -1.42% | -1.92% | -0.42 |
| 2026-10-01 19:35 | ruptura_volumen_regimen | DOT | timeout | -0.38% | -0.88% | -0.19 |
| 2026-10-01 19:35 | ruptura_volumen_regimen | HYPE | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 19:35 | macd_momentum_regimen | AVAX | momentum perdido | +0.13% | -0.37% | -0.08 |

## Eventos de la última vuelta

- 2026-10-01 19:40 [pullback_tendencia] CIERRE LINK rotura de tendencia bruto -0.17% neto -0.67%
- 2026-10-01 19:40 [ruptura_volumen_regimen] CIERRE PENGU stop-loss bruto -1.29% neto -1.79%
- 2026-10-01 19:40 [ruptura_estricta] CIERRE BNB timeout bruto +0.10% neto -0.40%
- 2026-10-01 19:40 [c_banda_atr] CIERRE SEI stop-loss bruto -1.56% neto -2.06%
- 2026-10-01 19:40 [c_banda_atr_regimen] CIERRE SEI stop-loss bruto -1.56% neto -2.06%
- 2026-10-01 19:40 [c_banda_atr_evento] CIERRE SEI stop-loss bruto -1.56% neto -2.06%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
