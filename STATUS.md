# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 16:57 UTC · vueltas 87 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.22 € (-1.52%) | 52 | 3 | 35% | -0.136% | -1.138% | -1.277% | -13.66 € |
| reversion_bb | 919.96 € (-0.46%) | 7 | 9 | 29% | -0.643% | -1.743% | -1.855% | -2.82 € |
| ruptura_volumen | 909.77 € (-1.57%) | 69 | 1 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| rebote_extremo | 922.23 € (-0.22%) | 3 | 2 | 0% | -1.873% | -2.973% | -3.162% | -2.06 € |
| pullback_tendencia | 908.45 € (-1.71%) | 68 | 0 | 25% | -0.127% | -1.011% | -1.125% | -15.79 € |
| macd_momentum | 898.01 € (-2.84%) | 149 | 2 | 19% | -0.087% | -0.762% | -0.879% | -25.97 € |
| estocastico_rebote | 895.08 € (-3.15%) | 106 | 28 | 31% | -0.280% | -1.027% | -1.149% | -24.95 € |
| ruptura_estricta | 912.02 € (-1.32%) | 41 | 1 | 29% | -0.183% | -1.283% | -1.409% | -12.12 € |
| macd_sin_salida | 904.83 € (-2.10%) | 94 | 3 | 31% | -0.102% | -0.880% | -1.005% | -18.97 € |
| c_banda_atr_tope | 916.78 € (-0.81%) | 19 | 3 | 26% | -0.522% | -1.622% | -1.789% | -7.11 € |
| ruptura_volumen_tope | 919.54 € (-0.51%) | 20 | 1 | 20% | +0.103% | -0.997% | -1.127% | -4.60 € |
| c_banda_atr_regimen | 909.84 € (-1.56%) | 50 | 0 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| c_banda_atr_evento | 916.96 € (-0.79%) | 19 | 4 | 32% | -0.411% | -1.511% | -1.672% | -6.64 € |
| macd_momentum_evento | 912.69 € (-1.25%) | 29 | 2 | 14% | -0.585% | -1.685% | -1.807% | -11.28 € |
| ruptura_volumen_evento | 920.09 € (-0.45%) | 10 | 1 | 20% | -0.654% | -1.754% | -1.962% | -4.05 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-29 16:45 | estocastico_rebote | ZRO | stop-loss | -1.50% | -2.00% | -0.41 |
| 2026-09-29 16:45 | estocastico_rebote | ATOM | stop-loss | -1.72% | -2.21% | -0.51 |
| 2026-09-29 16:45 | estocastico_rebote | XRP | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-29 16:55 [estocastico_rebote] CIERRE TRX timeout bruto +0.03% neto -0.47%
- 2026-09-29 16:50 [reversion_bb] ENTRADA ZRO @ 1.414 (23.04 €, apertura)
- 2026-09-29 16:55 [estocastico_rebote] CIERRE PENGU stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 16:55 [estocastico_rebote] CIERRE TRUMP stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
