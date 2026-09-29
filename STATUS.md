# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 14:11 UTC · vueltas 55 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 917.60 € (-0.72%) | 24 | 16 | 46% | +0.186% | -0.914% | -1.051% | -5.07 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 913.51 € (-1.16%) | 53 | 7 | 28% | +0.089% | -0.887% | -1.020% | -10.83 € |
| rebote_extremo | 924.26 € (+0.00%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 914.66 € (-1.04%) | 43 | 5 | 30% | +0.138% | -0.941% | -1.048% | -9.33 € |
| macd_momentum | 905.62 € (-2.01%) | 112 | 9 | 21% | +0.044% | -0.689% | -0.803% | -17.75 € |
| estocastico_rebote | 917.82 € (-0.69%) | 51 | 20 | 55% | +0.659% | -0.288% | -0.405% | -3.39 € |
| ruptura_estricta | 918.86 € (-0.58%) | 25 | 12 | 36% | +0.233% | -0.867% | -1.002% | -5.00 € |
| macd_sin_salida | 914.04 € (-1.10%) | 55 | 24 | 40% | +0.339% | -0.597% | -0.722% | -7.55 € |
| c_banda_atr_tope | 921.30 € (-0.32%) | 9 | 4 | 33% | -0.151% | -1.251% | -1.448% | -2.60 € |
| ruptura_volumen_tope | 921.74 € (-0.27%) | 13 | 5 | 23% | +0.215% | -0.885% | -1.016% | -2.66 € |
| c_banda_atr_regimen | 917.60 € (-0.72%) | 24 | 16 | 46% | +0.186% | -0.914% | -1.051% | -5.07 € |
| macd_momentum_regimen | 905.62 € (-2.01%) | 112 | 9 | 21% | +0.044% | -0.689% | -0.803% | -17.75 € |
| ruptura_volumen_regimen | 913.51 € (-1.16%) | 53 | 7 | 28% | +0.089% | -0.887% | -1.020% | -10.83 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 14:10 | ruptura_volumen_regimen | ENA | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 14:10 | macd_momentum_regimen | XPL | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 14:10 | macd_momentum_regimen | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 14:10 | macd_momentum_regimen | INJ | momentum perdido | -0.19% | -0.69% | -0.16 |
| 2026-09-29 14:10 | macd_momentum_regimen | ZEC | momentum perdido | -1.07% | -1.57% | -0.36 |
| 2026-09-29 14:10 | c_banda_atr_regimen | VIRTUAL | stop-loss | -1.82% | -2.92% | -0.68 |
| 2026-09-29 14:10 | c_banda_atr_regimen | HYPE | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:10 | c_banda_atr_tope | VIRTUAL | stop-loss | -1.51% | -2.61% | -0.60 |
| 2026-09-29 14:10 | macd_sin_salida | XPL | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 14:10 | ruptura_estricta | USELESS | stop-loss | -2.14% | -3.24% | -0.75 |
| 2026-09-29 14:10 | estocastico_rebote | VIRTUAL | stop-loss | -1.82% | -2.62% | -0.61 |
| 2026-09-29 14:10 | estocastico_rebote | BTC | timeout | -0.15% | -0.95% | -0.22 |
| 2026-09-29 14:10 | macd_momentum | XPL | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 14:10 | macd_momentum | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 14:10 | macd_momentum | INJ | momentum perdido | -0.19% | -0.69% | -0.16 |

## Eventos de la última vuelta

- 2026-09-29 14:10 [estocastico_rebote] CIERRE BTC timeout bruto -0.15% neto -0.95%
- 2026-09-29 14:10 [macd_momentum] CIERRE ZEC momentum perdido bruto -1.07% neto -1.57%
- 2026-09-29 14:10 [macd_momentum_regimen] CIERRE ZEC momentum perdido bruto -1.07% neto -1.57%
- 2026-09-29 14:05 [macd_momentum] ENTRADA UNI @ 7.934 (22.69 €, apertura)
- 2026-09-29 14:05 [macd_sin_salida] ENTRADA UNI @ 7.934 (22.93 €, apertura)
- 2026-09-29 14:05 [macd_momentum_regimen] ENTRADA UNI @ 7.934 (22.69 €, apertura)
- 2026-09-29 14:05 [pullback_tendencia] ENTRADA TAO @ 275.498 (22.87 €, apertura)
- 2026-09-29 14:10 [pullback_tendencia] CIERRE TAO rotura de tendencia bruto +0.25% neto -0.25%
- 2026-09-29 14:10 [c_banda_atr] CIERRE HYPE stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 14:10 [c_banda_atr_regimen] CIERRE HYPE stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 14:05 [pullback_tendencia] ENTRADA CRV @ 0.35215 (22.87 €, apertura)
- 2026-09-29 14:05 [macd_momentum] ENTRADA DASH @ 54.194 (22.69 €, apertura)
- 2026-09-29 14:05 [macd_sin_salida] ENTRADA DASH @ 54.194 (22.93 €, apertura)
- 2026-09-29 14:05 [macd_momentum_regimen] ENTRADA DASH @ 54.194 (22.69 €, apertura)
- 2026-09-29 14:10 [ruptura_volumen] CIERRE ENA stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 14:10 [ruptura_volumen_regimen] CIERRE ENA stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 14:10 [macd_momentum] CIERRE INJ momentum perdido bruto -0.19% neto -0.69%
- 2026-09-29 14:10 [macd_momentum_regimen] CIERRE INJ momentum perdido bruto -0.19% neto -0.69%
- 2026-09-29 14:10 [macd_momentum] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 14:10 [macd_momentum_regimen] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 14:10 [c_banda_atr] CIERRE VIRTUAL stop-loss bruto -1.82% neto -2.92%
- 2026-09-29 14:10 [estocastico_rebote] CIERRE VIRTUAL stop-loss bruto -1.82% neto -2.62%
- 2026-09-29 14:10 [c_banda_atr_tope] CIERRE VIRTUAL stop-loss bruto -1.51% neto -2.61%
- 2026-09-29 14:10 [c_banda_atr_regimen] CIERRE VIRTUAL stop-loss bruto -1.82% neto -2.92%
- 2026-09-29 14:10 [ruptura_estricta] CIERRE USELESS stop-loss bruto -2.14% neto -3.24%
- 2026-09-29 14:05 [macd_momentum] ENTRADA NIGHT @ 0.02758 (22.67 €, apertura)
- 2026-09-29 14:05 [macd_sin_salida] ENTRADA NIGHT @ 0.02758 (22.93 €, apertura)
- 2026-09-29 14:05 [macd_momentum_regimen] ENTRADA NIGHT @ 0.02758 (22.67 €, apertura)
- 2026-09-29 14:10 [macd_momentum] CIERRE XPL stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 14:10 [macd_sin_salida] CIERRE XPL stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 14:10 [macd_momentum_regimen] CIERRE XPL stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
