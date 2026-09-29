# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 17:02 UTC · vueltas 88 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.25 € (-1.51%) | 52 | 3 | 35% | -0.136% | -1.138% | -1.277% | -13.66 € |
| reversion_bb | 920.19 € (-0.44%) | 8 | 8 | 25% | -0.754% | -1.854% | -1.959% | -3.42 € |
| ruptura_volumen | 909.69 € (-1.57%) | 69 | 1 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| rebote_extremo | 922.57 € (-0.18%) | 3 | 3 | 0% | -1.873% | -2.973% | -3.162% | -2.06 € |
| pullback_tendencia | 908.45 € (-1.71%) | 68 | 0 | 25% | -0.127% | -1.011% | -1.125% | -15.79 € |
| macd_momentum | 897.98 € (-2.84%) | 150 | 1 | 19% | -0.090% | -0.764% | -0.882% | -26.22 € |
| estocastico_rebote | 896.66 € (-2.98%) | 106 | 29 | 31% | -0.280% | -1.027% | -1.149% | -24.95 € |
| ruptura_estricta | 911.94 € (-1.33%) | 41 | 1 | 29% | -0.183% | -1.283% | -1.409% | -12.12 € |
| macd_sin_salida | 904.98 € (-2.08%) | 94 | 3 | 31% | -0.102% | -0.880% | -1.005% | -18.97 € |
| c_banda_atr_tope | 916.80 € (-0.80%) | 19 | 3 | 26% | -0.522% | -1.622% | -1.789% | -7.11 € |
| ruptura_volumen_tope | 919.46 € (-0.52%) | 20 | 1 | 20% | +0.103% | -0.997% | -1.127% | -4.60 € |
| c_banda_atr_regimen | 909.84 € (-1.56%) | 50 | 0 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| c_banda_atr_evento | 916.99 € (-0.78%) | 19 | 4 | 32% | -0.411% | -1.511% | -1.672% | -6.64 € |
| macd_momentum_evento | 912.53 € (-1.27%) | 30 | 1 | 13% | -0.587% | -1.687% | -1.809% | -11.68 € |
| ruptura_volumen_evento | 920.01 € (-0.46%) | 10 | 1 | 20% | -0.654% | -1.754% | -1.962% | -4.05 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 17:00 | macd_momentum_evento | INJ | momentum perdido | -0.64% | -1.74% | -0.40 |
| 2026-09-29 17:00 | macd_momentum | INJ | momentum perdido | -0.64% | -1.14% | -0.26 |
| 2026-09-29 17:00 | reversion_bb | DOGE | stop-loss | -1.53% | -2.63% | -0.61 |
| 2026-09-29 16:55 | estocastico_rebote | TRUMP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 16:55 | estocastico_rebote | PENGU | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 16:55 | estocastico_rebote | TRX | timeout | +0.03% | -0.47% | -0.11 |
| 2026-09-29 16:50 | estocastico_rebote | XLM | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 16:50 | estocastico_rebote | ADA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 16:50 | pullback_tendencia | NEAR | rotura de tendencia | -1.16% | -1.66% | -0.38 |
| 2026-09-29 16:50 | rebote_extremo | HBAR | stop-loss | -2.00% | -3.10% | -0.71 |
| 2026-09-29 16:45 | macd_sin_salida | PUMP | stop-loss | -1.59% | -2.09% | -0.47 |
| 2026-09-29 16:45 | ruptura_estricta | FIL | stop-loss | -2.00% | -3.10% | -0.71 |
| 2026-09-29 16:45 | estocastico_rebote | FET | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 16:45 | estocastico_rebote | USELESS | stop-loss | -1.54% | -2.04% | -0.46 |
| 2026-09-29 16:45 | estocastico_rebote | PEPE | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-29 16:55 [rebote_extremo] ENTRADA HBAR @ 0.09194 (23.05 €, apertura)
- 2026-09-29 17:00 [reversion_bb] CIERRE DOGE stop-loss bruto -1.53% neto -2.63%
- 2026-09-29 17:00 [macd_momentum] CIERRE INJ momentum perdido bruto -0.64% neto -1.14%
- 2026-09-29 17:00 [macd_momentum_evento] CIERRE INJ momentum perdido bruto -0.64% neto -1.74%
- 2026-09-29 16:55 [estocastico_rebote] ENTRADA ZRO @ 1.419 (22.48 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
