# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 16:47 UTC · vueltas 85 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.41 € (-1.50%) | 52 | 3 | 35% | -0.136% | -1.138% | -1.277% | -13.66 € |
| reversion_bb | 920.71 € (-0.38%) | 7 | 8 | 29% | -0.643% | -1.743% | -1.855% | -2.82 € |
| ruptura_volumen | 909.83 € (-1.56%) | 69 | 1 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| rebote_extremo | 923.11 € (-0.12%) | 2 | 1 | 0% | -1.809% | -2.909% | -3.048% | -1.34 € |
| pullback_tendencia | 908.69 € (-1.68%) | 67 | 1 | 25% | -0.112% | -1.001% | -1.116% | -15.41 € |
| macd_momentum | 898.10 € (-2.83%) | 149 | 2 | 19% | -0.087% | -0.762% | -0.879% | -25.97 € |
| estocastico_rebote | 898.10 € (-2.83%) | 101 | 33 | 33% | -0.235% | -0.994% | -1.120% | -23.03 € |
| ruptura_estricta | 912.07 € (-1.32%) | 41 | 1 | 29% | -0.183% | -1.283% | -1.409% | -12.12 € |
| macd_sin_salida | 904.89 € (-2.09%) | 94 | 3 | 31% | -0.102% | -0.880% | -1.005% | -18.97 € |
| c_banda_atr_tope | 916.97 € (-0.79%) | 19 | 3 | 26% | -0.522% | -1.622% | -1.789% | -7.11 € |
| ruptura_volumen_tope | 919.60 € (-0.50%) | 20 | 1 | 20% | +0.103% | -0.997% | -1.127% | -4.60 € |
| c_banda_atr_regimen | 909.84 € (-1.56%) | 50 | 0 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| c_banda_atr_evento | 917.17 € (-0.77%) | 19 | 4 | 32% | -0.411% | -1.511% | -1.672% | -6.64 € |
| macd_momentum_evento | 912.78 € (-1.24%) | 29 | 2 | 14% | -0.585% | -1.685% | -1.807% | -11.28 € |
| ruptura_volumen_evento | 920.14 € (-0.44%) | 10 | 1 | 20% | -0.654% | -1.754% | -1.962% | -4.05 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 16:45 | macd_sin_salida | PUMP | stop-loss | -1.59% | -2.09% | -0.47 |
| 2026-09-29 16:45 | ruptura_estricta | FIL | stop-loss | -2.00% | -3.10% | -0.71 |
| 2026-09-29 16:45 | estocastico_rebote | FET | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 16:45 | estocastico_rebote | USELESS | stop-loss | -1.54% | -2.04% | -0.46 |
| 2026-09-29 16:45 | estocastico_rebote | PEPE | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 16:45 | estocastico_rebote | ZRO | stop-loss | -1.50% | -2.00% | -0.41 |
| 2026-09-29 16:45 | estocastico_rebote | ATOM | stop-loss | -1.72% | -2.21% | -0.51 |
| 2026-09-29 16:45 | estocastico_rebote | XRP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 16:45 | rebote_extremo | FET | stop-loss | -2.00% | -3.10% | -0.72 |
| 2026-09-29 16:45 | reversion_bb | XLM | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 16:40 | macd_momentum_evento | ICP | momentum perdido | -0.47% | -1.57% | -0.36 |
| 2026-09-29 16:40 | macd_momentum_evento | PUMP | momentum perdido | -0.94% | -2.04% | -0.47 |
| 2026-09-29 16:40 | c_banda_atr_evento | JUP | take-profit | +2.22% | +1.12% | +0.26 |
| 2026-09-29 16:40 | c_banda_atr_tope | JUP | take-profit | +2.22% | +1.12% | +0.26 |
| 2026-09-29 16:40 | ruptura_estricta | ICP | timeout | -0.93% | -2.03% | -0.47 |

## Eventos de la última vuelta

- 2026-09-29 16:45 [estocastico_rebote] CIERRE XRP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 16:45 [reversion_bb] CIERRE XLM stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 16:45 [macd_sin_salida] CIERRE PUMP stop-loss bruto -1.59% neto -2.09%
- 2026-09-29 16:40 [c_banda_atr] ENTRADA VVV @ 23.853 (22.76 €, apertura)
- 2026-09-29 16:40 [c_banda_atr_tope] ENTRADA VVV @ 23.853 (22.93 €, apertura)
- 2026-09-29 16:40 [c_banda_atr_evento] ENTRADA VVV @ 23.853 (22.94 €, apertura)
- 2026-09-29 16:45 [estocastico_rebote] CIERRE ATOM stop-loss bruto -1.71% neto -2.21%
- 2026-09-29 16:45 [estocastico_rebote] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 16:45 [estocastico_rebote] CIERRE PEPE stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 16:45 [estocastico_rebote] CIERRE USELESS stop-loss bruto -1.54% neto -2.04%
- 2026-09-29 16:45 [ruptura_estricta] CIERRE FIL stop-loss bruto -2.00% neto -3.10%
- 2026-09-29 16:45 [rebote_extremo] CIERRE FET stop-loss bruto -2.00% neto -3.10%
- 2026-09-29 16:45 [estocastico_rebote] CIERRE FET stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
