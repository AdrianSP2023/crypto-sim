# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 17:07 UTC · vueltas 89 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.98 € (-1.54%) | 52 | 3 | 35% | -0.136% | -1.138% | -1.277% | -13.66 € |
| reversion_bb | 919.64 € (-0.50%) | 9 | 7 | 22% | -0.837% | -1.937% | -2.043% | -4.02 € |
| ruptura_volumen | 909.81 € (-1.56%) | 69 | 1 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| rebote_extremo | 922.63 € (-0.17%) | 4 | 2 | 25% | -0.905% | -2.005% | -2.191% | -1.85 € |
| pullback_tendencia | 908.45 € (-1.71%) | 68 | 0 | 25% | -0.127% | -1.011% | -1.125% | -15.79 € |
| macd_momentum | 897.81 € (-2.86%) | 150 | 1 | 19% | -0.090% | -0.764% | -0.882% | -26.22 € |
| estocastico_rebote | 896.60 € (-2.99%) | 109 | 30 | 30% | -0.314% | -1.053% | -1.177% | -26.31 € |
| ruptura_estricta | 912.05 € (-1.32%) | 41 | 1 | 29% | -0.183% | -1.283% | -1.409% | -12.12 € |
| macd_sin_salida | 904.86 € (-2.10%) | 94 | 3 | 31% | -0.102% | -0.880% | -1.005% | -18.97 € |
| c_banda_atr_tope | 916.53 € (-0.83%) | 19 | 3 | 26% | -0.522% | -1.622% | -1.789% | -7.11 € |
| ruptura_volumen_tope | 919.58 € (-0.50%) | 20 | 1 | 20% | +0.103% | -0.997% | -1.127% | -4.60 € |
| c_banda_atr_regimen | 909.84 € (-1.56%) | 50 | 0 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| c_banda_atr_evento | 916.72 € (-0.81%) | 19 | 4 | 32% | -0.411% | -1.511% | -1.672% | -6.64 € |
| macd_momentum_evento | 912.36 € (-1.29%) | 30 | 1 | 13% | -0.587% | -1.687% | -1.809% | -11.68 € |
| ruptura_volumen_evento | 920.12 € (-0.45%) | 10 | 1 | 20% | -0.654% | -1.754% | -1.962% | -4.05 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 17:05 | estocastico_rebote | RAY | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:05 | estocastico_rebote | ENA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:05 | estocastico_rebote | AAVE | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:05 | rebote_extremo | HBAR | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 17:05 | reversion_bb | ENA | stop-loss | -1.50% | -2.60% | -0.60 |
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

## Eventos de la última vuelta

- 2026-09-29 17:00 [estocastico_rebote] ENTRADA XRP @ 1.31303 (22.48 €, apertura)
- 2026-09-29 17:05 [rebote_extremo] CIERRE HBAR take-profit bruto +2.00% neto +0.90%
- 2026-09-29 17:05 [estocastico_rebote] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 17:05 [reversion_bb] CIERRE ENA stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 17:05 [estocastico_rebote] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 17:00 [estocastico_rebote] ENTRADA USELESS @ 0.20455 (22.46 €, apertura)
- 2026-09-29 17:05 [estocastico_rebote] CIERRE RAY stop-loss bruto -1.51% neto -2.01%
- 2026-09-29 17:00 [estocastico_rebote] ENTRADA FIL @ 0.936 (22.45 €, apertura)
- 2026-09-29 17:00 [estocastico_rebote] ENTRADA TRUMP @ 1.787 (22.45 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
