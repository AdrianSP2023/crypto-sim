# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 19:22 UTC · vueltas 293 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.74 € (-3.73%) | 239 | 19 | 36% | -0.013% | -0.622% | -0.745% | -33.90 € |
| reversion_bb | 916.50 € (-0.84%) | 48 | 0 | 50% | +0.344% | -0.700% | -0.796% | -7.74 € |
| ruptura_volumen | 876.28 € (-5.19%) | 273 | 16 | 25% | -0.182% | -0.777% | -0.885% | -47.97 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 891.93 € (-3.50%) | 165 | 11 | 15% | -0.207% | -0.867% | -0.963% | -32.53 € |
| macd_momentum | 870.90 € (-5.77%) | 437 | 2 | 22% | +0.016% | -0.544% | -0.649% | -53.48 € |
| estocastico_rebote | 877.13 € (-5.10%) | 289 | 23 | 31% | -0.125% | -0.716% | -0.827% | -46.80 € |
| ruptura_estricta | 885.63 € (-4.18%) | 147 | 18 | 26% | -0.456% | -1.136% | -1.255% | -38.07 € |
| macd_sin_salida | 882.93 € (-4.47%) | 295 | 22 | 37% | -0.025% | -0.613% | -0.729% | -41.17 € |
| c_banda_atr_tope | 912.00 € (-1.32%) | 55 | 5 | 31% | +0.014% | -0.966% | -1.084% | -12.21 € |
| ruptura_volumen_tope | 908.46 € (-1.71%) | 90 | 4 | 29% | +0.037% | -0.756% | -0.869% | -15.62 € |
| c_banda_atr_regimen | 901.45 € (-2.47%) | 112 | 19 | 35% | -0.105% | -0.838% | -0.978% | -21.56 € |
| macd_momentum_regimen | 891.71 € (-3.52%) | 237 | 2 | 22% | +0.005% | -0.605% | -0.716% | -32.66 € |
| ruptura_volumen_regimen | 879.77 € (-4.81%) | 205 | 18 | 20% | -0.330% | -0.957% | -1.072% | -44.44 € |
| c_banda_atr_evento | 895.66 € (-3.09%) | 206 | 19 | 37% | +0.034% | -0.594% | -0.710% | -27.97 € |
| macd_momentum_evento | 875.72 € (-5.25%) | 390 | 2 | 20% | +0.014% | -0.554% | -0.654% | -48.66 € |
| ruptura_volumen_evento | 888.75 € (-3.84%) | 223 | 16 | 26% | -0.082% | -0.700% | -0.798% | -35.48 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 19:20 | ruptura_volumen_evento | ICP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 19:20 | ruptura_volumen_evento | LTC | timeout | +0.33% | -0.17% | -0.04 |
| 2026-10-01 19:20 | ruptura_volumen_evento | XLM | timeout | -0.34% | -0.84% | -0.19 |
| 2026-10-01 19:20 | ruptura_volumen_evento | SUI | timeout | -0.10% | -0.60% | -0.13 |
| 2026-10-01 19:20 | ruptura_volumen_evento | ADA | timeout | -0.71% | -1.21% | -0.27 |
| 2026-10-01 19:20 | ruptura_volumen_evento | ETH | timeout | -0.06% | -0.56% | -0.12 |
| 2026-10-01 19:20 | macd_momentum_evento | WLFI | momentum perdido | +0.81% | +0.31% | +0.07 |
| 2026-10-01 19:20 | c_banda_atr_evento | WLFI | timeout | +1.43% | +0.93% | +0.21 |
| 2026-10-01 19:20 | c_banda_atr_evento | ICP | timeout | -0.86% | -1.36% | -0.30 |
| 2026-10-01 19:20 | c_banda_atr_evento | XLM | timeout | +0.30% | -0.20% | -0.04 |
| 2026-10-01 19:20 | c_banda_atr_evento | SOL | timeout | +0.62% | +0.12% | +0.03 |
| 2026-10-01 19:20 | ruptura_volumen_regimen | ICP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 19:20 | ruptura_volumen_regimen | LTC | timeout | +0.33% | -0.17% | -0.04 |
| 2026-10-01 19:20 | ruptura_volumen_regimen | XLM | timeout | -0.34% | -0.84% | -0.18 |
| 2026-10-01 19:20 | ruptura_volumen_regimen | SUI | timeout | -0.10% | -0.60% | -0.13 |

## Eventos de la última vuelta

- 2026-10-01 19:20 [ruptura_estricta] CIERRE BTC timeout bruto +0.52% neto +0.02%
- 2026-10-01 19:20 [ruptura_volumen] CIERRE ETH timeout bruto -0.06% neto -0.56%
- 2026-10-01 19:20 [ruptura_volumen_tope] CIERRE ETH timeout bruto -0.06% neto -0.56%
- 2026-10-01 19:20 [ruptura_volumen_regimen] CIERRE ETH timeout bruto -0.06% neto -0.56%
- 2026-10-01 19:20 [ruptura_volumen_evento] CIERRE ETH timeout bruto -0.06% neto -0.56%
- 2026-10-01 19:20 [c_banda_atr] CIERRE SOL timeout bruto +0.62% neto +0.12%
- 2026-10-01 19:20 [c_banda_atr_evento] CIERRE SOL timeout bruto +0.62% neto +0.12%
- 2026-10-01 19:20 [ruptura_volumen] CIERRE ADA timeout bruto -0.71% neto -1.21%
- 2026-10-01 19:20 [ruptura_volumen_regimen] CIERRE ADA timeout bruto -0.71% neto -1.21%
- 2026-10-01 19:20 [ruptura_volumen_evento] CIERRE ADA timeout bruto -0.71% neto -1.21%
- 2026-10-01 19:20 [ruptura_volumen] CIERRE SUI timeout bruto -0.10% neto -0.60%
- 2026-10-01 19:20 [ruptura_volumen_regimen] CIERRE SUI timeout bruto -0.10% neto -0.60%
- 2026-10-01 19:20 [ruptura_volumen_evento] CIERRE SUI timeout bruto -0.10% neto -0.60%
- 2026-10-01 19:15 [estocastico_rebote] ENTRADA PUMP @ 0.005123 (21.94 €, apertura)
- 2026-10-01 19:20 [c_banda_atr] CIERRE XLM timeout bruto +0.30% neto -0.20%
- 2026-10-01 19:20 [reversion_bb] CIERRE XLM timeout bruto +0.76% neto -0.04%
- 2026-10-01 19:20 [ruptura_volumen] CIERRE XLM timeout bruto -0.34% neto -0.84%
- 2026-10-01 19:20 [ruptura_volumen_regimen] CIERRE XLM timeout bruto -0.34% neto -0.84%
- 2026-10-01 19:20 [c_banda_atr_evento] CIERRE XLM timeout bruto +0.30% neto -0.20%
- 2026-10-01 19:20 [ruptura_volumen_evento] CIERRE XLM timeout bruto -0.34% neto -0.84%
- 2026-10-01 19:15 [estocastico_rebote] ENTRADA UNI @ 8.0831 (21.94 €, apertura)
- 2026-10-01 19:20 [ruptura_volumen] CIERRE LTC timeout bruto +0.33% neto -0.17%
- 2026-10-01 19:20 [ruptura_volumen_regimen] CIERRE LTC timeout bruto +0.33% neto -0.17%
- 2026-10-01 19:20 [ruptura_volumen_evento] CIERRE LTC timeout bruto +0.33% neto -0.17%
- 2026-10-01 19:20 [c_banda_atr] CIERRE ICP timeout bruto -0.86% neto -1.36%
- 2026-10-01 19:20 [ruptura_volumen] CIERRE ICP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 19:20 [ruptura_volumen_regimen] CIERRE ICP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 19:20 [c_banda_atr_evento] CIERRE ICP timeout bruto -0.86% neto -1.36%
- 2026-10-01 19:20 [ruptura_volumen_evento] CIERRE ICP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 19:15 [estocastico_rebote] ENTRADA FET @ 0.205 (21.94 €, apertura)
- 2026-10-01 19:20 [macd_sin_salida] CIERRE VVV stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 19:20 [c_banda_atr] CIERRE WLFI timeout bruto +1.43% neto +0.93%
- 2026-10-01 19:20 [macd_momentum] CIERRE WLFI momentum perdido bruto +0.81% neto +0.31%
- 2026-10-01 19:20 [macd_momentum_regimen] CIERRE WLFI momentum perdido bruto +0.81% neto +0.31%
- 2026-10-01 19:20 [c_banda_atr_evento] CIERRE WLFI timeout bruto +1.43% neto +0.93%
- 2026-10-01 19:20 [macd_momentum_evento] CIERRE WLFI momentum perdido bruto +0.81% neto +0.31%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
