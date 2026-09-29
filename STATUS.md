# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 18:42 UTC · vueltas 108 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.17 € (-1.52%) | 55 | 7 | 33% | -0.213% | -1.188% | -1.326% | -15.06 € |
| reversion_bb | 918.92 € (-0.58%) | 14 | 4 | 29% | -0.642% | -1.742% | -1.849% | -5.63 € |
| ruptura_volumen | 910.52 € (-1.48%) | 71 | 7 | 28% | -0.008% | -0.876% | -1.014% | -14.30 € |
| rebote_extremo | 922.71 € (-0.17%) | 6 | 1 | 50% | +0.064% | -1.036% | -1.189% | -1.44 € |
| pullback_tendencia | 908.05 € (-1.75%) | 70 | 2 | 24% | -0.161% | -1.034% | -1.149% | -16.61 € |
| macd_momentum | 897.97 € (-2.84%) | 153 | 2 | 20% | -0.090% | -0.760% | -0.879% | -26.60 € |
| estocastico_rebote | 894.40 € (-3.23%) | 140 | 10 | 30% | -0.270% | -0.957% | -1.075% | -30.62 € |
| ruptura_estricta | 911.86 € (-1.34%) | 42 | 1 | 29% | -0.226% | -1.326% | -1.452% | -12.83 € |
| macd_sin_salida | 904.61 € (-2.12%) | 98 | 3 | 31% | -0.123% | -0.890% | -1.017% | -19.99 € |
| c_banda_atr_tope | 916.35 € (-0.85%) | 22 | 5 | 23% | -0.661% | -1.761% | -1.924% | -8.93 € |
| ruptura_volumen_tope | 919.55 € (-0.51%) | 21 | 5 | 19% | +0.041% | -1.059% | -1.189% | -5.13 € |
| c_banda_atr_regimen | 909.84 € (-1.56%) | 50 | 0 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| c_banda_atr_evento | 916.18 € (-0.87%) | 23 | 7 | 26% | -0.607% | -1.707% | -1.858% | -9.06 € |
| macd_momentum_evento | 912.10 € (-1.31%) | 33 | 2 | 15% | -0.539% | -1.639% | -1.769% | -12.47 € |
| ruptura_volumen_evento | 920.57 € (-0.40%) | 12 | 7 | 25% | -0.437% | -1.537% | -1.738% | -4.26 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 18:40 | macd_momentum_evento | PUMP | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 18:40 | macd_sin_salida | PUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 18:40 | estocastico_rebote | VIRTUAL | timeout | -0.68% | -1.18% | -0.27 |
| 2026-09-29 18:40 | estocastico_rebote | INJ | timeout | +0.72% | +0.22% | +0.05 |
| 2026-09-29 18:40 | macd_momentum | PUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 18:40 | rebote_extremo | ZRO | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 18:35 | ruptura_volumen_evento | QNT | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 18:35 | estocastico_rebote | SPX | timeout | +0.25% | -0.25% | -0.06 |
| 2026-09-29 18:35 | estocastico_rebote | ASTER | timeout | +1.44% | +0.94% | +0.21 |
| 2026-09-29 18:35 | estocastico_rebote | SHIB | timeout | -0.22% | -0.72% | -0.16 |
| 2026-09-29 18:35 | estocastico_rebote | BCH | timeout | +0.07% | -0.43% | -0.10 |
| 2026-09-29 18:35 | estocastico_rebote | ARB | timeout | +0.22% | -0.28% | -0.06 |
| 2026-09-29 18:35 | estocastico_rebote | TAO | timeout | +0.57% | +0.07% | +0.01 |
| 2026-09-29 18:35 | estocastico_rebote | PUMP | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-29 18:35 | estocastico_rebote | AVAX | timeout | +0.33% | -0.17% | -0.04 |

## Eventos de la última vuelta

- 2026-09-29 18:35 [ruptura_estricta] ENTRADA QNT @ 234.08 (22.79 €, apertura)
- 2026-09-29 18:40 [macd_momentum] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-09-29 18:40 [macd_sin_salida] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-09-29 18:40 [macd_momentum_evento] CIERRE PUMP take-profit bruto +2.00% neto +0.90%
- 2026-09-29 18:35 [pullback_tendencia] ENTRADA INJ @ 6.747 (22.69 €, apertura)
- 2026-09-29 18:40 [estocastico_rebote] CIERRE INJ timeout bruto +0.72% neto +0.22%
- 2026-09-29 18:40 [rebote_extremo] CIERRE ZRO take-profit bruto +2.00% neto +0.90%
- 2026-09-29 18:40 [estocastico_rebote] CIERRE VIRTUAL timeout bruto -0.68% neto -1.18%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
