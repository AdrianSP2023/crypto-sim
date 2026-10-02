# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 08:31 UTC · vueltas 391 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.84 € (-3.51%) | 338 | 22 | 40% | +0.140% | -0.437% | -0.557% | -33.69 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 863.85 € (-6.53%) | 416 | 24 | 27% | -0.096% | -0.659% | -0.768% | -61.42 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 890.26 € (-3.68%) | 239 | 8 | 21% | -0.032% | -0.642% | -0.729% | -34.86 € |
| macd_momentum | 858.08 € (-7.16%) | 648 | 40 | 23% | +0.052% | -0.488% | -0.590% | -70.46 € |
| estocastico_rebote | 884.16 € (-4.34%) | 394 | 34 | 37% | +0.069% | -0.497% | -0.605% | -44.41 € |
| ruptura_estricta | 882.91 € (-4.47%) | 235 | 8 | 31% | -0.171% | -0.783% | -0.900% | -41.87 € |
| macd_sin_salida | 883.98 € (-4.36%) | 434 | 39 | 40% | +0.118% | -0.443% | -0.553% | -43.76 € |
| c_banda_atr_tope | 913.64 € (-1.15%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 901.74 € (-2.43%) | 128 | 5 | 24% | -0.088% | -0.794% | -0.908% | -23.22 € |
| c_banda_atr_regimen | 904.50 € (-2.14%) | 190 | 22 | 41% | +0.155% | -0.483% | -0.611% | -21.12 € |
| macd_momentum_regimen | 881.06 € (-4.67%) | 411 | 40 | 22% | +0.050% | -0.513% | -0.617% | -47.58 € |
| ruptura_volumen_regimen | 868.54 € (-6.03%) | 339 | 24 | 24% | -0.168% | -0.745% | -0.859% | -56.74 € |
| c_banda_atr_evento | 897.78 € (-2.86%) | 305 | 22 | 41% | +0.189% | -0.398% | -0.513% | -27.76 € |
| macd_momentum_evento | 862.84 € (-6.64%) | 601 | 40 | 21% | +0.054% | -0.490% | -0.589% | -65.73 € |
| ruptura_volumen_evento | 876.14 € (-5.20%) | 366 | 24 | 28% | -0.024% | -0.596% | -0.700% | -49.14 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-02 08:25 | estocastico_rebote | PENGU | take-profit | +1.84% | +1.34% | +0.29 |
| 2026-10-02 08:25 | estocastico_rebote | DOGE | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 08:25 | c_banda_atr | CRV | timeout | +1.61% | +1.11% | +0.25 |

## Eventos de la última vuelta

- 2026-10-02 08:30 [pullback_tendencia] CIERRE AAVE rotura de tendencia bruto -1.09% neto -1.59%
- 2026-10-02 08:25 [ruptura_volumen] ENTRADA INJ @ 6.733 (21.57 €, apertura)
- 2026-10-02 08:25 [ruptura_volumen_regimen] ENTRADA INJ @ 6.733 (21.69 €, apertura)
- 2026-10-02 08:25 [ruptura_volumen_evento] ENTRADA INJ @ 6.733 (21.88 €, apertura)
- 2026-10-02 08:25 [c_banda_atr] ENTRADA MINA @ 0.1469 (22.26 €, apertura)
- 2026-10-02 08:25 [c_banda_atr_regimen] ENTRADA MINA @ 0.1469 (22.58 €, apertura)
- 2026-10-02 08:25 [c_banda_atr_evento] ENTRADA MINA @ 0.1469 (22.41 €, apertura)
- 2026-10-02 08:30 [estocastico_rebote] CIERRE TON timeout bruto -0.36% neto -0.86%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
