# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 23:06 UTC · vueltas 102 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.31 € (-1.83%) | 68 | 32 | 24% | -0.485% | -1.368% | -1.512% | -21.36 € |
| reversion_bb | 922.23 € (-0.22%) | 9 | 5 | 44% | -0.167% | -1.267% | -1.401% | -2.64 € |
| ruptura_volumen | 896.56 € (-2.99%) | 94 | 19 | 16% | -0.513% | -1.290% | -1.426% | -27.77 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.87 € (-2.10%) | 65 | 1 | 15% | -0.413% | -1.319% | -1.456% | -19.65 € |
| macd_momentum | 906.85 € (-1.88%) | 102 | 31 | 25% | -0.078% | -0.834% | -0.964% | -19.52 € |
| estocastico_rebote | 903.55 € (-2.24%) | 126 | 9 | 35% | -0.025% | -0.732% | -0.864% | -21.23 € |
| ruptura_estricta | 898.65 € (-2.77%) | 50 | 8 | 12% | -1.227% | -2.255% | -2.403% | -25.93 € |
| macd_sin_salida | 906.44 € (-1.93%) | 82 | 32 | 33% | -0.260% | -1.079% | -1.210% | -20.34 € |
| c_banda_atr_tope | 919.82 € (-0.48%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.258% | -5.10 € |
| ruptura_volumen_tope | 916.39 € (-0.85%) | 27 | 4 | 19% | -0.185% | -1.285% | -1.398% | -8.00 € |
| c_banda_atr_regimen | 908.52 € (-1.70%) | 45 | 5 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.25 € (-1.41%) | 60 | 14 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 897.98 € (-2.84%) | 73 | 19 | 12% | -0.720% | -1.577% | -1.716% | -26.39 € |
| c_banda_atr_evento | 914.88 € (-1.01%) | 35 | 32 | 17% | -0.650% | -1.715% | -1.843% | -13.83 € |
| macd_momentum_evento | 911.94 € (-1.33%) | 55 | 31 | 16% | -0.169% | -1.143% | -1.267% | -14.43 € |
| ruptura_volumen_evento | 909.46 € (-1.60%) | 44 | 19 | 11% | -0.383% | -1.469% | -1.589% | -14.88 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 23:05 | ruptura_volumen_evento | ETH | timeout | +0.33% | -0.47% | -0.11 |
| 2026-09-30 23:05 | ruptura_volumen_tope | ASTER | timeout | -0.12% | -1.22% | -0.28 |
| 2026-09-30 23:05 | ruptura_volumen_tope | ETH | timeout | +0.33% | -0.77% | -0.18 |
| 2026-09-30 23:05 | ruptura_volumen | ETH | timeout | +0.33% | -0.17% | -0.04 |
| 2026-09-30 23:00 | ruptura_volumen_regimen | ZRO | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 23:00 | ruptura_estricta | KAS | timeout | -0.91% | -1.41% | -0.32 |
| 2026-09-30 22:55 | c_banda_atr_evento | XLM | timeout | +0.88% | +0.08% | +0.02 |
| 2026-09-30 22:55 | c_banda_atr_tope | XLM | timeout | +0.88% | -0.22% | -0.05 |
| 2026-09-30 22:55 | c_banda_atr | XLM | timeout | +0.88% | +0.38% | +0.09 |
| 2026-09-30 22:45 | ruptura_estricta | CRV | timeout | +1.10% | +0.60% | +0.14 |
| 2026-09-30 22:40 | ruptura_volumen_evento | SHIB | timeout | +0.22% | -0.58% | -0.13 |
| 2026-09-30 22:40 | macd_momentum_evento | HYPE | momentum perdido | +0.01% | -0.49% | -0.11 |
| 2026-09-30 22:40 | c_banda_atr_evento | ENA | take-profit | +2.04% | +1.24% | +0.28 |
| 2026-09-30 22:40 | macd_momentum | HYPE | momentum perdido | +0.01% | -0.49% | -0.11 |
| 2026-09-30 22:40 | ruptura_volumen | SHIB | timeout | +0.22% | -0.28% | -0.06 |

## Eventos de la última vuelta

- 2026-09-30 23:05 [ruptura_volumen] CIERRE ETH timeout bruto +0.33% neto -0.17%
- 2026-09-30 23:05 [ruptura_volumen_tope] CIERRE ETH timeout bruto +0.33% neto -0.77%
- 2026-09-30 23:05 [ruptura_volumen_evento] CIERRE ETH timeout bruto +0.33% neto -0.47%
- 2026-09-30 23:00 [ruptura_volumen_tope] ENTRADA BCH @ 270.61 (22.91 €, apertura)
- 2026-09-30 23:05 [ruptura_volumen_tope] CIERRE ASTER timeout bruto -0.12% neto -1.22%
- 2026-09-30 23:00 [c_banda_atr] ENTRADA XMR @ 477.04 (22.57 €, apertura)
- 2026-09-30 23:00 [c_banda_atr_tope] ENTRADA XMR @ 477.04 (22.98 €, apertura)
- 2026-09-30 23:00 [c_banda_atr_regimen] ENTRADA XMR @ 477.04 (22.71 €, apertura)
- 2026-09-30 23:00 [c_banda_atr_evento] ENTRADA XMR @ 477.04 (22.76 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
