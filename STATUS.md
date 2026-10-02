# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 06:31 UTC · vueltas 367 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.09 € (-3.59%) | 327 | 13 | 39% | +0.122% | -0.458% | -0.578% | -34.15 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 864.17 € (-6.50%) | 400 | 9 | 27% | -0.107% | -0.672% | -0.779% | -60.28 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.82 € (-3.62%) | 216 | 16 | 19% | -0.072% | -0.694% | -0.781% | -34.09 € |
| macd_momentum | 856.09 € (-7.37%) | 624 | 5 | 23% | +0.049% | -0.492% | -0.594% | -68.51 € |
| estocastico_rebote | 879.97 € (-4.79%) | 376 | 36 | 36% | +0.024% | -0.546% | -0.654% | -46.48 € |
| ruptura_estricta | 886.57 € (-4.08%) | 209 | 25 | 34% | -0.161% | -0.787% | -0.902% | -37.57 € |
| macd_sin_salida | 882.17 € (-4.55%) | 413 | 22 | 40% | +0.110% | -0.453% | -0.564% | -42.69 € |
| c_banda_atr_tope | 913.73 € (-1.14%) | 73 | 3 | 36% | +0.207% | -0.655% | -0.765% | -10.99 € |
| ruptura_volumen_tope | 902.50 € (-2.35%) | 121 | 5 | 26% | -0.062% | -0.780% | -0.893% | -21.58 € |
| c_banda_atr_regimen | 903.59 € (-2.23%) | 180 | 13 | 40% | +0.134% | -0.511% | -0.638% | -21.17 € |
| macd_momentum_regimen | 879.01 € (-4.89%) | 387 | 5 | 22% | +0.046% | -0.521% | -0.625% | -45.58 € |
| ruptura_volumen_regimen | 868.86 € (-5.99%) | 323 | 9 | 24% | -0.184% | -0.765% | -0.877% | -55.59 € |
| c_banda_atr_evento | 897.02 € (-2.95%) | 294 | 13 | 40% | +0.170% | -0.420% | -0.535% | -28.23 € |
| macd_momentum_evento | 860.83 € (-6.86%) | 577 | 5 | 21% | +0.051% | -0.495% | -0.593% | -63.77 € |
| ruptura_volumen_evento | 876.46 € (-5.17%) | 350 | 9 | 28% | -0.033% | -0.608% | -0.709% | -47.99 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 06:30 | ruptura_volumen_evento | ALGO | timeout | -0.61% | -1.11% | -0.24 |
| 2026-10-02 06:30 | ruptura_volumen_evento | XRP | timeout | -0.30% | -0.80% | -0.17 |
| 2026-10-02 06:30 | c_banda_atr_evento | WLD | take-profit | +2.59% | +2.09% | +0.47 |
| 2026-10-02 06:30 | c_banda_atr_evento | ONDO | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 06:30 | ruptura_volumen_regimen | ALGO | timeout | -0.61% | -1.11% | -0.24 |
| 2026-10-02 06:30 | ruptura_volumen_regimen | XRP | timeout | -0.30% | -0.80% | -0.17 |
| 2026-10-02 06:30 | c_banda_atr_regimen | WLD | take-profit | +2.59% | +2.09% | +0.47 |
| 2026-10-02 06:30 | c_banda_atr_regimen | ONDO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 06:30 | c_banda_atr_tope | WLD | take-profit | +2.59% | +2.09% | +0.48 |
| 2026-10-02 06:30 | c_banda_atr_tope | ONDO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 06:30 | macd_sin_salida | WLD | take-profit | +2.28% | +1.78% | +0.39 |
| 2026-10-02 06:30 | ruptura_estricta | VVV | take-profit | +3.00% | +2.50% | +0.55 |
| 2026-10-02 06:30 | ruptura_estricta | WLD | take-profit | +3.32% | +2.82% | +0.62 |
| 2026-10-02 06:30 | ruptura_volumen | ALGO | timeout | -0.61% | -1.11% | -0.24 |
| 2026-10-02 06:30 | ruptura_volumen | XRP | timeout | -0.30% | -0.80% | -0.17 |

## Eventos de la última vuelta

- 2026-10-02 06:30 [ruptura_volumen] CIERRE XRP timeout bruto -0.30% neto -0.80%
- 2026-10-02 06:30 [ruptura_volumen_regimen] CIERRE XRP timeout bruto -0.30% neto -0.80%
- 2026-10-02 06:30 [ruptura_volumen_evento] CIERRE XRP timeout bruto -0.30% neto -0.80%
- 2026-10-02 06:25 [estocastico_rebote] ENTRADA ENA @ 0.22 (21.94 €, apertura)
- 2026-10-02 06:25 [c_banda_atr] ENTRADA FET @ 0.211 (22.23 €, apertura)
- 2026-10-02 06:25 [c_banda_atr_regimen] ENTRADA FET @ 0.211 (22.56 €, apertura)
- 2026-10-02 06:25 [c_banda_atr_evento] ENTRADA FET @ 0.211 (22.38 €, apertura)
- 2026-10-02 06:30 [ruptura_volumen] CIERRE ALGO timeout bruto -0.61% neto -1.11%
- 2026-10-02 06:30 [ruptura_volumen_regimen] CIERRE ALGO timeout bruto -0.61% neto -1.11%
- 2026-10-02 06:30 [ruptura_volumen_evento] CIERRE ALGO timeout bruto -0.61% neto -1.11%
- 2026-10-02 06:30 [c_banda_atr] CIERRE ONDO take-profit bruto +2.00% neto +1.50%
- 2026-10-02 06:30 [c_banda_atr_tope] CIERRE ONDO take-profit bruto +2.00% neto +1.50%
- 2026-10-02 06:30 [c_banda_atr_regimen] CIERRE ONDO take-profit bruto +2.00% neto +1.50%
- 2026-10-02 06:30 [c_banda_atr_evento] CIERRE ONDO take-profit bruto +2.00% neto +1.50%
- 2026-10-02 06:30 [c_banda_atr] CIERRE WLD take-profit bruto +2.59% neto +2.09%
- 2026-10-02 06:30 [ruptura_estricta] CIERRE WLD take-profit bruto +3.32% neto +2.82%
- 2026-10-02 06:30 [macd_sin_salida] CIERRE WLD take-profit bruto +2.28% neto +1.78%
- 2026-10-02 06:30 [c_banda_atr_tope] CIERRE WLD take-profit bruto +2.59% neto +2.09%
- 2026-10-02 06:30 [c_banda_atr_regimen] CIERRE WLD take-profit bruto +2.59% neto +2.09%
- 2026-10-02 06:30 [c_banda_atr_evento] CIERRE WLD take-profit bruto +2.59% neto +2.09%
- 2026-10-02 06:25 [estocastico_rebote] ENTRADA OP @ 0.117 (21.94 €, apertura)
- 2026-10-02 06:30 [ruptura_estricta] CIERRE VVV take-profit bruto +3.00% neto +2.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
