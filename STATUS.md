# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 19:52 UTC · vueltas 122 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.73 € (-1.57%) | 58 | 6 | 34% | -0.159% | -1.109% | -1.248% | -14.83 € |
| reversion_bb | 918.74 € (-0.60%) | 15 | 3 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 906.69 € (-1.90%) | 79 | 21 | 27% | -0.068% | -0.898% | -1.038% | -16.30 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 907.91 € (-1.77%) | 72 | 3 | 25% | -0.132% | -0.994% | -1.111% | -16.44 € |
| macd_momentum | 898.10 € (-2.83%) | 155 | 1 | 21% | -0.071% | -0.740% | -0.858% | -26.22 € |
| estocastico_rebote | 894.63 € (-3.20%) | 144 | 8 | 31% | -0.244% | -0.925% | -1.045% | -30.47 € |
| ruptura_estricta | 911.35 € (-1.39%) | 44 | 1 | 30% | -0.193% | -1.280% | -1.414% | -12.97 € |
| macd_sin_salida | 904.78 € (-2.11%) | 100 | 2 | 32% | -0.095% | -0.856% | -0.984% | -19.64 € |
| c_banda_atr_tope | 915.65 € (-0.93%) | 23 | 5 | 26% | -0.546% | -1.646% | -1.804% | -8.72 € |
| ruptura_volumen_tope | 918.41 € (-0.63%) | 24 | 4 | 21% | +0.087% | -1.013% | -1.135% | -5.61 € |
| c_banda_atr_regimen | 909.26 € (-1.62%) | 51 | 1 | 31% | -0.251% | -1.263% | -1.400% | -14.85 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 907.29 € (-1.83%) | 72 | 14 | 26% | -0.076% | -0.939% | -1.079% | -15.53 € |
| c_banda_atr_evento | 915.33 € (-0.96%) | 26 | 6 | 31% | -0.440% | -1.540% | -1.691% | -9.24 € |
| macd_momentum_evento | 911.96 € (-1.33%) | 35 | 1 | 17% | -0.431% | -1.531% | -1.660% | -12.36 € |
| ruptura_volumen_evento | 915.59 € (-0.94%) | 20 | 21 | 20% | -0.501% | -1.601% | -1.781% | -7.38 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 19:50 | ruptura_volumen_evento | ENA | stop-loss | -1.21% | -2.31% | -0.53 |
| 2026-09-29 19:50 | ruptura_volumen_evento | ZEC | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 19:50 | c_banda_atr_evento | XPL | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 19:50 | ruptura_volumen_regimen | NEAR | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 19:50 | c_banda_atr_regimen | XPL | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 19:50 | ruptura_volumen_tope | ZEC | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 19:50 | ruptura_volumen | ENA | stop-loss | -1.21% | -1.71% | -0.39 |
| 2026-09-29 19:50 | ruptura_volumen | ZEC | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 19:50 | c_banda_atr | XPL | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 19:45 | ruptura_volumen_evento | PUMP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 19:45 | rebote_extremo | XDC | timeout | +0.64% | -0.46% | -0.11 |
| 2026-09-29 19:45 | ruptura_volumen | PUMP | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 19:40 | ruptura_estricta | USELESS | stop-loss | -2.00% | -2.50% | -0.57 |
| 2026-09-29 19:35 | macd_momentum_evento | ASTER | momentum perdido | +0.69% | -0.41% | -0.09 |
| 2026-09-29 19:35 | macd_momentum | ASTER | momentum perdido | +0.69% | +0.19% | +0.04 |

## Eventos de la última vuelta

- 2026-09-29 19:50 [ruptura_volumen] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 19:50 [ruptura_volumen_tope] CIERRE ZEC stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 19:50 [ruptura_volumen_evento] CIERRE ZEC stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 19:45 [pullback_tendencia] ENTRADA NEAR @ 4.4473 (22.70 €, apertura)
- 2026-09-29 19:50 [ruptura_volumen_regimen] CIERRE NEAR stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 19:50 [ruptura_volumen] CIERRE ENA stop-loss bruto -1.21% neto -1.71%
- 2026-09-29 19:50 [ruptura_volumen_evento] CIERRE ENA stop-loss bruto -1.21% neto -2.31%
- 2026-09-29 19:45 [pullback_tendencia] ENTRADA NIGHT @ 0.02804 (22.70 €, apertura)
- 2026-09-29 19:45 [macd_momentum] ENTRADA NIGHT @ 0.02804 (22.45 €, apertura)
- 2026-09-29 19:45 [macd_sin_salida] ENTRADA NIGHT @ 0.02804 (22.62 €, apertura)
- 2026-09-29 19:45 [macd_momentum_evento] ENTRADA NIGHT @ 0.02804 (22.80 €, apertura)
- 2026-09-29 19:50 [c_banda_atr] CIERRE XPL stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 19:50 [c_banda_atr_regimen] CIERRE XPL stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 19:50 [c_banda_atr_evento] CIERRE XPL stop-loss bruto -1.50% neto -2.60%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
