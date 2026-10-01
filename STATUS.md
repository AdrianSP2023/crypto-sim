# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 19:37 UTC · vueltas 296 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.34 € (-3.99%) | 242 | 17 | 36% | -0.027% | -0.635% | -0.757% | -34.99 € |
| reversion_bb | 916.63 € (-0.82%) | 48 | 2 | 50% | +0.344% | -0.700% | -0.796% | -7.74 € |
| ruptura_volumen | 873.79 € (-5.46%) | 282 | 7 | 24% | -0.199% | -0.792% | -0.900% | -50.38 € |
| rebote_extremo | 922.04 € (-0.24%) | 13 | 1 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 890.49 € (-3.65%) | 173 | 3 | 15% | -0.215% | -0.867% | -0.961% | -34.10 € |
| macd_momentum | 870.48 € (-5.82%) | 439 | 0 | 22% | +0.015% | -0.545% | -0.649% | -53.76 € |
| estocastico_rebote | 874.59 € (-5.37%) | 290 | 23 | 31% | -0.130% | -0.720% | -0.832% | -47.24 € |
| ruptura_estricta | 883.01 € (-4.46%) | 151 | 14 | 25% | -0.456% | -1.131% | -1.249% | -38.92 € |
| macd_sin_salida | 880.23 € (-4.76%) | 299 | 18 | 36% | -0.044% | -0.632% | -0.748% | -42.93 € |
| c_banda_atr_tope | 911.45 € (-1.38%) | 55 | 5 | 31% | +0.014% | -0.966% | -1.084% | -12.21 € |
| ruptura_volumen_tope | 907.76 € (-1.78%) | 93 | 1 | 29% | +0.019% | -0.765% | -0.878% | -16.32 € |
| c_banda_atr_regimen | 898.83 € (-2.75%) | 115 | 16 | 34% | -0.141% | -0.868% | -1.008% | -22.91 € |
| macd_momentum_regimen | 891.29 € (-3.57%) | 239 | 0 | 22% | +0.003% | -0.606% | -0.715% | -32.95 € |
| ruptura_volumen_regimen | 876.83 € (-5.13%) | 215 | 8 | 19% | -0.347% | -0.968% | -1.084% | -47.08 € |
| c_banda_atr_evento | 893.24 € (-3.35%) | 209 | 17 | 37% | +0.018% | -0.609% | -0.726% | -29.07 € |
| macd_momentum_evento | 875.31 € (-5.29%) | 392 | 0 | 20% | +0.013% | -0.554% | -0.654% | -48.94 € |
| ruptura_volumen_evento | 886.22 € (-4.11%) | 232 | 7 | 25% | -0.107% | -0.721% | -0.820% | -37.94 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 19:35 | ruptura_volumen_evento | FIL | stop-loss | -1.42% | -1.92% | -0.43 |
| 2026-10-01 19:35 | ruptura_volumen_evento | DOT | timeout | -0.38% | -0.88% | -0.20 |
| 2026-10-01 19:35 | ruptura_volumen_evento | HYPE | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 19:35 | macd_momentum_evento | AVAX | momentum perdido | +0.13% | -0.37% | -0.08 |
| 2026-10-01 19:35 | macd_momentum_evento | LINK | momentum perdido | -0.42% | -0.92% | -0.20 |
| 2026-10-01 19:35 | ruptura_volumen_regimen | FIL | stop-loss | -1.42% | -1.92% | -0.42 |
| 2026-10-01 19:35 | ruptura_volumen_regimen | DOT | timeout | -0.38% | -0.88% | -0.19 |
| 2026-10-01 19:35 | ruptura_volumen_regimen | HYPE | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 19:35 | macd_momentum_regimen | AVAX | momentum perdido | +0.13% | -0.37% | -0.08 |
| 2026-10-01 19:35 | macd_momentum_regimen | LINK | momentum perdido | -0.42% | -0.92% | -0.20 |
| 2026-10-01 19:35 | ruptura_volumen_tope | HYPE | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 19:35 | ruptura_estricta | SUI | timeout | +0.03% | -0.47% | -0.10 |
| 2026-10-01 19:35 | ruptura_estricta | SOL | timeout | -0.10% | -0.59% | -0.13 |
| 2026-10-01 19:35 | estocastico_rebote | ARB | stop-loss | -1.51% | -2.01% | -0.44 |
| 2026-10-01 19:35 | macd_momentum | AVAX | momentum perdido | +0.13% | -0.37% | -0.08 |

## Eventos de la última vuelta

- 2026-10-01 19:35 [ruptura_estricta] CIERRE SOL timeout bruto -0.10% neto -0.60%
- 2026-10-01 19:30 [reversion_bb] ENTRADA NEAR @ 4.2321 (22.91 €, apertura)
- 2026-10-01 19:35 [macd_momentum] CIERRE LINK momentum perdido bruto -0.42% neto -0.92%
- 2026-10-01 19:35 [macd_momentum_regimen] CIERRE LINK momentum perdido bruto -0.42% neto -0.92%
- 2026-10-01 19:35 [macd_momentum_evento] CIERRE LINK momentum perdido bruto -0.42% neto -0.92%
- 2026-10-01 19:35 [ruptura_estricta] CIERRE SUI timeout bruto +0.03% neto -0.47%
- 2026-10-01 19:35 [macd_momentum] CIERRE AVAX momentum perdido bruto +0.13% neto -0.37%
- 2026-10-01 19:35 [macd_momentum_regimen] CIERRE AVAX momentum perdido bruto +0.13% neto -0.37%
- 2026-10-01 19:35 [macd_momentum_evento] CIERRE AVAX momentum perdido bruto +0.13% neto -0.37%
- 2026-10-01 19:35 [ruptura_volumen] CIERRE HYPE stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 19:35 [ruptura_volumen_tope] CIERRE HYPE stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 19:35 [ruptura_volumen_regimen] CIERRE HYPE stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 19:35 [ruptura_volumen_evento] CIERRE HYPE stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 19:35 [ruptura_volumen] CIERRE DOT timeout bruto -0.38% neto -0.88%
- 2026-10-01 19:35 [ruptura_volumen_regimen] CIERRE DOT timeout bruto -0.38% neto -0.88%
- 2026-10-01 19:35 [ruptura_volumen_evento] CIERRE DOT timeout bruto -0.38% neto -0.88%
- 2026-10-01 19:35 [estocastico_rebote] CIERRE ARB stop-loss bruto -1.51% neto -2.01%
- 2026-10-01 19:30 [reversion_bb] ENTRADA INJ @ 6.522 (22.91 €, apertura)
- 2026-10-01 19:35 [ruptura_volumen] CIERRE FIL stop-loss bruto -1.42% neto -1.92%
- 2026-10-01 19:35 [ruptura_volumen_regimen] CIERRE FIL stop-loss bruto -1.42% neto -1.92%
- 2026-10-01 19:35 [ruptura_volumen_evento] CIERRE FIL stop-loss bruto -1.42% neto -1.92%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
