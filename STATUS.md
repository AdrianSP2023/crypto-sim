# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 08:36 UTC · vueltas 392 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.38 € (-3.56%) | 338 | 24 | 40% | +0.140% | -0.437% | -0.557% | -33.69 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 863.20 € (-6.60%) | 416 | 24 | 27% | -0.096% | -0.659% | -0.768% | -61.42 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 890.10 € (-3.69%) | 239 | 8 | 21% | -0.032% | -0.642% | -0.729% | -34.86 € |
| macd_momentum | 857.52 € (-7.22%) | 648 | 40 | 23% | +0.052% | -0.488% | -0.590% | -70.46 € |
| estocastico_rebote | 883.50 € (-4.41%) | 394 | 34 | 37% | +0.069% | -0.497% | -0.605% | -44.41 € |
| ruptura_estricta | 882.55 € (-4.51%) | 236 | 7 | 32% | -0.167% | -0.779% | -0.895% | -41.82 € |
| macd_sin_salida | 882.97 € (-4.47%) | 436 | 38 | 40% | +0.114% | -0.445% | -0.556% | -44.22 € |
| c_banda_atr_tope | 913.50 € (-1.16%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 901.48 € (-2.46%) | 128 | 5 | 24% | -0.088% | -0.794% | -0.908% | -23.22 € |
| c_banda_atr_regimen | 904.03 € (-2.19%) | 190 | 24 | 41% | +0.155% | -0.483% | -0.611% | -21.12 € |
| macd_momentum_regimen | 880.48 € (-4.73%) | 411 | 40 | 22% | +0.050% | -0.513% | -0.617% | -47.58 € |
| ruptura_volumen_regimen | 867.88 € (-6.10%) | 339 | 24 | 24% | -0.168% | -0.745% | -0.859% | -56.74 € |
| c_banda_atr_evento | 897.31 € (-2.91%) | 305 | 24 | 41% | +0.189% | -0.398% | -0.513% | -27.76 € |
| macd_momentum_evento | 862.27 € (-6.70%) | 601 | 40 | 21% | +0.054% | -0.490% | -0.589% | -65.73 € |
| ruptura_volumen_evento | 875.48 € (-5.28%) | 366 | 24 | 28% | -0.024% | -0.596% | -0.700% | -49.14 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 08:35 | macd_sin_salida | FIL | timeout | +0.43% | -0.07% | -0.01 |
| 2026-10-02 08:35 | macd_sin_salida | AAVE | stop-loss | -1.55% | -2.05% | -0.45 |
| 2026-10-02 08:35 | ruptura_estricta | ASTER | timeout | +0.70% | +0.20% | +0.04 |
| 2026-10-02 08:30 | estocastico_rebote | TON | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-02 08:30 | pullback_tendencia | AAVE | rotura de tendencia | -1.09% | -1.59% | -0.35 |
| 2026-10-02 08:25 | c_banda_atr_evento | CRV | timeout | +1.61% | +1.11% | +0.25 |
| 2026-10-02 08:25 | c_banda_atr_evento | LTC | timeout | +1.35% | +0.85% | +0.19 |
| 2026-10-02 08:25 | c_banda_atr_evento | HBAR | timeout | +0.33% | -0.17% | -0.04 |
| 2026-10-02 08:25 | c_banda_atr_evento | ADA | timeout | +1.24% | +0.74% | +0.17 |
| 2026-10-02 08:25 | c_banda_atr_regimen | SEI | timeout | +0.38% | -0.12% | -0.03 |
| 2026-10-02 08:25 | c_banda_atr_regimen | CRV | timeout | +1.61% | +1.11% | +0.25 |
| 2026-10-02 08:25 | c_banda_atr_regimen | LTC | timeout | +1.35% | +0.85% | +0.19 |
| 2026-10-02 08:25 | c_banda_atr_regimen | HBAR | timeout | +0.33% | -0.17% | -0.04 |
| 2026-10-02 08:25 | c_banda_atr_tope | ADA | timeout | +1.24% | +0.74% | +0.17 |
| 2026-10-02 08:25 | ruptura_estricta | LTC | timeout | +0.40% | -0.10% | -0.02 |

## Eventos de la última vuelta

- 2026-10-02 08:35 [macd_sin_salida] CIERRE AAVE stop-loss bruto -1.55% neto -2.05%
- 2026-10-02 08:30 [c_banda_atr] ENTRADA UNI @ 8.1032 (22.26 €, apertura)
- 2026-10-02 08:30 [macd_sin_salida] ENTRADA UNI @ 8.1032 (22.00 €, apertura)
- 2026-10-02 08:30 [c_banda_atr_regimen] ENTRADA UNI @ 8.1032 (22.58 €, apertura)
- 2026-10-02 08:30 [c_banda_atr_evento] ENTRADA UNI @ 8.1032 (22.41 €, apertura)
- 2026-10-02 08:35 [macd_sin_salida] CIERRE FIL timeout bruto +0.44% neto -0.06%
- 2026-10-02 08:30 [c_banda_atr] ENTRADA ASTER @ 0.67109 (22.26 €, apertura)
- 2026-10-02 08:35 [ruptura_estricta] CIERRE ASTER timeout bruto +0.70% neto +0.20%
- 2026-10-02 08:30 [c_banda_atr_regimen] ENTRADA ASTER @ 0.67109 (22.58 €, apertura)
- 2026-10-02 08:30 [c_banda_atr_evento] ENTRADA ASTER @ 0.67109 (22.41 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
