# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 16:42 UTC · vueltas 84 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.54 € (-1.48%) | 52 | 2 | 35% | -0.136% | -1.138% | -1.277% | -13.66 € |
| reversion_bb | 921.77 € (-0.27%) | 6 | 9 | 33% | -0.500% | -1.600% | -1.712% | -2.22 € |
| ruptura_volumen | 910.14 € (-1.53%) | 69 | 1 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| rebote_extremo | 923.56 € (-0.07%) | 1 | 2 | 0% | -1.619% | -2.719% | -2.843% | -0.63 € |
| pullback_tendencia | 908.85 € (-1.67%) | 67 | 1 | 25% | -0.112% | -1.001% | -1.116% | -15.41 € |
| macd_momentum | 898.22 € (-2.82%) | 149 | 2 | 19% | -0.087% | -0.762% | -0.879% | -25.97 € |
| estocastico_rebote | 902.87 € (-2.31%) | 95 | 39 | 35% | -0.153% | -0.927% | -1.055% | -20.28 € |
| ruptura_estricta | 912.79 € (-1.24%) | 40 | 2 | 30% | -0.137% | -1.237% | -1.362% | -11.41 € |
| macd_sin_salida | 905.37 € (-2.04%) | 93 | 4 | 31% | -0.086% | -0.867% | -0.991% | -18.50 € |
| c_banda_atr_tope | 917.10 € (-0.77%) | 19 | 2 | 26% | -0.522% | -1.622% | -1.789% | -7.11 € |
| ruptura_volumen_tope | 919.92 € (-0.47%) | 20 | 1 | 20% | +0.103% | -0.997% | -1.127% | -4.60 € |
| c_banda_atr_regimen | 909.84 € (-1.56%) | 50 | 0 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| c_banda_atr_evento | 917.36 € (-0.74%) | 19 | 3 | 32% | -0.411% | -1.511% | -1.672% | -6.64 € |
| macd_momentum_evento | 912.91 € (-1.23%) | 29 | 2 | 14% | -0.585% | -1.685% | -1.807% | -11.28 € |
| ruptura_volumen_evento | 920.46 € (-0.41%) | 10 | 1 | 20% | -0.654% | -1.754% | -1.962% | -4.05 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 16:40 | macd_momentum_evento | ICP | momentum perdido | -0.47% | -1.57% | -0.36 |
| 2026-09-29 16:40 | macd_momentum_evento | PUMP | momentum perdido | -0.94% | -2.04% | -0.47 |
| 2026-09-29 16:40 | c_banda_atr_evento | JUP | take-profit | +2.22% | +1.12% | +0.26 |
| 2026-09-29 16:40 | c_banda_atr_tope | JUP | take-profit | +2.22% | +1.12% | +0.26 |
| 2026-09-29 16:40 | ruptura_estricta | ICP | timeout | -0.93% | -2.03% | -0.47 |
| 2026-09-29 16:40 | estocastico_rebote | XDC | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 16:40 | macd_momentum | ICP | momentum perdido | -0.47% | -0.97% | -0.22 |
| 2026-09-29 16:40 | macd_momentum | PUMP | momentum perdido | -0.94% | -1.44% | -0.32 |
| 2026-09-29 16:40 | reversion_bb | TAO | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-09-29 16:40 | c_banda_atr | JUP | take-profit | +2.22% | +1.72% | +0.39 |
| 2026-09-29 16:35 | pullback_tendencia | ICP | rotura de tendencia | -0.40% | -0.90% | -0.20 |
| 2026-09-29 16:15 | c_banda_atr_evento | TON | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 16:15 | c_banda_atr_regimen | TON | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-29 16:15 | estocastico_rebote | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 16:15 | c_banda_atr | TON | stop-loss | -1.50% | -2.30% | -0.53 |

## Eventos de la última vuelta

- 2026-09-29 16:40 [macd_momentum] CIERRE PUMP momentum perdido bruto -0.94% neto -1.44%
- 2026-09-29 16:40 [macd_momentum_evento] CIERRE PUMP momentum perdido bruto -0.94% neto -2.04%
- 2026-09-29 16:40 [reversion_bb] CIERRE TAO take-profit bruto +1.50% neto +0.40%
- 2026-09-29 16:40 [estocastico_rebote] CIERRE XDC stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 16:40 [c_banda_atr] CIERRE JUP take-profit bruto +2.22% neto +1.72%
- 2026-09-29 16:40 [c_banda_atr_tope] CIERRE JUP take-profit bruto +2.22% neto +1.12%
- 2026-09-29 16:40 [c_banda_atr_evento] CIERRE JUP take-profit bruto +2.22% neto +1.12%
- 2026-09-29 16:40 [macd_momentum] CIERRE ICP momentum perdido bruto -0.47% neto -0.97%
- 2026-09-29 16:40 [ruptura_estricta] CIERRE ICP timeout bruto -0.93% neto -2.03%
- 2026-09-29 16:40 [macd_momentum_evento] CIERRE ICP momentum perdido bruto -0.47% neto -1.57%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
