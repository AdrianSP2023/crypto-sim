# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 15:41 UTC · vueltas 255 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.89 € (-3.82%) | 211 | 22 | 33% | -0.092% | -0.716% | -0.840% | -34.41 € |
| reversion_bb | 915.38 € (-0.96%) | 37 | 10 | 38% | +0.028% | -1.072% | -1.174% | -9.13 € |
| ruptura_volumen | 878.85 € (-4.91%) | 240 | 8 | 22% | -0.230% | -0.839% | -0.947% | -45.59 € |
| rebote_extremo | 921.85 € (-0.26%) | 11 | 2 | 45% | +0.049% | -1.051% | -1.228% | -2.67 € |
| pullback_tendencia | 892.90 € (-3.39%) | 143 | 5 | 13% | -0.280% | -0.965% | -1.066% | -31.39 € |
| macd_momentum | 873.97 € (-5.44%) | 358 | 22 | 20% | -0.043% | -0.616% | -0.724% | -49.69 € |
| estocastico_rebote | 878.09 € (-4.99%) | 277 | 10 | 31% | -0.145% | -0.739% | -0.852% | -46.34 € |
| ruptura_estricta | 885.00 € (-4.25%) | 137 | 5 | 23% | -0.562% | -1.254% | -1.376% | -39.15 € |
| macd_sin_salida | 880.19 € (-4.77%) | 256 | 23 | 33% | -0.149% | -0.751% | -0.867% | -43.66 € |
| c_banda_atr_tope | 912.13 € (-1.31%) | 49 | 5 | 27% | -0.057% | -1.095% | -1.209% | -12.33 € |
| ruptura_volumen_tope | 907.50 € (-1.81%) | 79 | 5 | 24% | -0.102% | -0.936% | -1.051% | -16.96 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 894.81 € (-3.18%) | 178 | 22 | 34% | -0.052% | -0.700% | -0.818% | -28.48 € |
| macd_momentum_evento | 878.81 € (-4.91%) | 311 | 22 | 17% | -0.054% | -0.639% | -0.743% | -44.84 € |
| ruptura_volumen_evento | 891.35 € (-3.56%) | 190 | 8 | 23% | -0.126% | -0.765% | -0.862% | -33.07 € |
| rebote_desplome | 925.20 € (+0.10%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 925.20 € (+0.10%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 15:40 | macd_momentum_evento | ETH | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-01 15:40 | c_banda_atr_evento | USELESS | stop-loss | -1.53% | -2.03% | -0.45 |
| 2026-10-01 15:40 | c_banda_atr_evento | DOGE | timeout | -0.13% | -0.63% | -0.14 |
| 2026-10-01 15:40 | c_banda_atr_evento | LINK | timeout | -0.10% | -0.60% | -0.14 |
| 2026-10-01 15:40 | macd_momentum | ETH | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-01 15:40 | c_banda_atr | USELESS | stop-loss | -1.53% | -2.03% | -0.45 |
| 2026-10-01 15:40 | c_banda_atr | DOGE | timeout | -0.13% | -0.63% | -0.14 |
| 2026-10-01 15:40 | c_banda_atr | LINK | timeout | -0.10% | -0.60% | -0.13 |
| 2026-10-01 15:35 | ruptura_volumen_tope | TAO | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 15:30 | estocastico_rebote | BNB | timeout | +0.05% | -0.45% | -0.10 |
| 2026-10-01 15:25 | macd_momentum_evento | TON | take-profit | +2.25% | +1.75% | +0.39 |
| 2026-10-01 15:25 | c_banda_atr_evento | TON | take-profit | +2.17% | +1.67% | +0.38 |
| 2026-10-01 15:25 | macd_sin_salida | TON | take-profit | +2.25% | +1.75% | +0.39 |
| 2026-10-01 15:25 | estocastico_rebote | TON | take-profit | +2.17% | +1.67% | +0.37 |
| 2026-10-01 15:25 | estocastico_rebote | PEPE | take-profit | +1.83% | +1.33% | +0.29 |

## Eventos de la última vuelta

- 2026-10-01 15:40 [macd_momentum] CIERRE ETH momentum perdido bruto -0.24% neto -0.74%
- 2026-10-01 15:40 [macd_momentum_evento] CIERRE ETH momentum perdido bruto -0.24% neto -0.74%
- 2026-10-01 15:40 [c_banda_atr] CIERRE LINK timeout bruto -0.10% neto -0.60%
- 2026-10-01 15:40 [c_banda_atr_evento] CIERRE LINK timeout bruto -0.10% neto -0.60%
- 2026-10-01 15:35 [pullback_tendencia] ENTRADA AAVE @ 149.3 (22.32 €, apertura)
- 2026-10-01 15:35 [pullback_tendencia] ENTRADA UNI @ 8.0625 (22.32 €, apertura)
- 2026-10-01 15:40 [c_banda_atr] CIERRE DOGE timeout bruto -0.13% neto -0.63%
- 2026-10-01 15:40 [c_banda_atr_evento] CIERRE DOGE timeout bruto -0.13% neto -0.63%
- 2026-10-01 15:40 [c_banda_atr] CIERRE USELESS stop-loss bruto -1.53% neto -2.03%
- 2026-10-01 15:35 [macd_momentum] ENTRADA USELESS @ 0.19882 (21.86 €, apertura)
- 2026-10-01 15:35 [macd_sin_salida] ENTRADA USELESS @ 0.19882 (22.01 €, apertura)
- 2026-10-01 15:40 [c_banda_atr_evento] CIERRE USELESS stop-loss bruto -1.53% neto -2.03%
- 2026-10-01 15:35 [macd_momentum_evento] ENTRADA USELESS @ 0.19882 (21.99 €, apertura)
- 2026-10-01 15:35 [pullback_tendencia] ENTRADA BNB @ 681.47 (22.32 €, apertura)
- 2026-10-01 15:35 [ruptura_estricta] ENTRADA SKY @ 0.07097 (22.13 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
