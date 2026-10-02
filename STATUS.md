# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 05:16 UTC · vueltas 398 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.08 € (-3.59%) | 322 | 13 | 39% | +0.113% | -0.469% | -0.589% | -34.39 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.382% | -4.66 € |
| ruptura_volumen | 870.01 € (-5.87%) | 367 | 37 | 27% | -0.100% | -0.671% | -0.779% | -55.40 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 892.16 € (-3.47%) | 209 | 8 | 19% | -0.078% | -0.704% | -0.792% | -33.46 € |
| macd_momentum | 861.11 € (-6.83%) | 586 | 34 | 23% | +0.054% | -0.491% | -0.593% | -64.31 € |
| estocastico_rebote | 879.04 € (-4.89%) | 372 | 10 | 35% | +0.021% | -0.549% | -0.658% | -46.28 € |
| ruptura_estricta | 888.92 € (-3.82%) | 198 | 33 | 33% | -0.190% | -0.823% | -0.937% | -37.22 € |
| macd_sin_salida | 882.86 € (-4.48%) | 410 | 18 | 40% | +0.107% | -0.457% | -0.567% | -42.70 € |
| c_banda_atr_tope | 912.80 € (-1.24%) | 71 | 4 | 34% | +0.148% | -0.724% | -0.833% | -11.81 € |
| ruptura_volumen_tope | 903.43 € (-2.25%) | 117 | 5 | 26% | -0.045% | -0.771% | -0.885% | -20.64 € |
| c_banda_atr_regimen | 903.61 € (-2.23%) | 175 | 12 | 39% | +0.118% | -0.532% | -0.660% | -21.42 € |
| macd_momentum_regimen | 884.16 € (-4.34%) | 349 | 34 | 22% | +0.053% | -0.522% | -0.626% | -41.27 € |
| ruptura_volumen_regimen | 874.73 € (-5.36%) | 290 | 37 | 24% | -0.184% | -0.774% | -0.887% | -50.68 € |
| c_banda_atr_evento | 897.01 € (-2.95%) | 289 | 13 | 40% | +0.161% | -0.431% | -0.546% | -28.47 € |
| macd_momentum_evento | 865.88 € (-6.31%) | 539 | 34 | 22% | +0.056% | -0.493% | -0.592% | -59.55 € |
| ruptura_volumen_evento | 882.39 € (-4.53%) | 317 | 37 | 28% | -0.017% | -0.600% | -0.702% | -43.03 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 05:15 | macd_momentum_evento | MON | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 05:15 | macd_momentum_evento | FET | momentum perdido | -1.03% | -1.53% | -0.33 |
| 2026-10-02 05:15 | c_banda_atr_evento | MON | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 05:15 | macd_momentum_regimen | MON | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 05:15 | macd_momentum_regimen | FET | momentum perdido | -1.03% | -1.53% | -0.34 |
| 2026-10-02 05:15 | c_banda_atr_regimen | MON | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 05:15 | macd_sin_salida | MON | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 05:15 | ruptura_estricta | RENDER | timeout | +2.09% | +1.59% | +0.35 |
| 2026-10-02 05:15 | ruptura_estricta | AVAX | timeout | +0.83% | +0.33% | +0.07 |
| 2026-10-02 05:15 | macd_momentum | MON | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 05:15 | macd_momentum | FET | momentum perdido | -1.03% | -1.53% | -0.33 |
| 2026-10-02 05:15 | c_banda_atr | MON | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 05:10 | ruptura_volumen_evento | USELESS | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 05:10 | ruptura_volumen_evento | ONDO | timeout | +1.70% | +1.20% | +0.26 |
| 2026-10-02 05:10 | ruptura_volumen_evento | ZRO | take-profit | +2.51% | +2.01% | +0.44 |

## Eventos de la última vuelta

- 2026-10-02 05:15 [ruptura_estricta] CIERRE AVAX timeout bruto +0.83% neto +0.33%
- 2026-10-02 05:15 [macd_momentum] CIERRE FET momentum perdido bruto -1.03% neto -1.53%
- 2026-10-02 05:15 [macd_momentum_regimen] CIERRE FET momentum perdido bruto -1.03% neto -1.53%
- 2026-10-02 05:15 [macd_momentum_evento] CIERRE FET momentum perdido bruto -1.03% neto -1.53%
- 2026-10-02 05:15 [c_banda_atr] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:15 [macd_momentum] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:15 [macd_sin_salida] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:15 [c_banda_atr_regimen] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:15 [macd_momentum_regimen] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:15 [c_banda_atr_evento] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:15 [macd_momentum_evento] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:15 [ruptura_estricta] CIERRE RENDER timeout bruto +2.09% neto +1.59%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
