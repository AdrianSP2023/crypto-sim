# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 20:11 UTC · vueltas 126 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.07 € (-1.64%) | 59 | 5 | 34% | -0.182% | -1.124% | -1.263% | -15.29 € |
| reversion_bb | 918.75 € (-0.59%) | 15 | 4 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 906.05 € (-1.97%) | 83 | 18 | 27% | -0.082% | -0.896% | -1.037% | -17.08 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.74 € (-1.89%) | 76 | 0 | 24% | -0.160% | -1.004% | -1.122% | -17.50 € |
| macd_momentum | 898.27 € (-2.81%) | 155 | 1 | 21% | -0.071% | -0.740% | -0.858% | -26.22 € |
| estocastico_rebote | 893.79 € (-3.30%) | 149 | 5 | 31% | -0.229% | -0.904% | -1.024% | -30.81 € |
| ruptura_estricta | 911.21 € (-1.41%) | 44 | 2 | 30% | -0.193% | -1.280% | -1.414% | -12.97 € |
| macd_sin_salida | 904.95 € (-2.09%) | 100 | 2 | 32% | -0.095% | -0.856% | -0.984% | -19.64 € |
| c_banda_atr_tope | 915.05 € (-0.99%) | 24 | 4 | 25% | -0.585% | -1.685% | -1.845% | -9.32 € |
| ruptura_volumen_tope | 917.90 € (-0.69%) | 25 | 4 | 20% | +0.024% | -1.076% | -1.207% | -6.20 € |
| c_banda_atr_regimen | 908.93 € (-1.66%) | 52 | 0 | 31% | -0.275% | -1.277% | -1.415% | -15.31 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 907.08 € (-1.86%) | 75 | 11 | 25% | -0.125% | -0.973% | -1.116% | -16.76 € |
| c_banda_atr_evento | 914.52 € (-1.05%) | 27 | 5 | 30% | -0.480% | -1.580% | -1.731% | -9.84 € |
| macd_momentum_evento | 912.13 € (-1.31%) | 35 | 1 | 17% | -0.431% | -1.531% | -1.660% | -12.36 € |
| ruptura_volumen_evento | 914.40 € (-1.06%) | 24 | 18 | 21% | -0.476% | -1.577% | -1.755% | -8.72 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 20:10 | ruptura_volumen_evento | ICP | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 20:10 | pullback_tendencia | PUMP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 20:10 | ruptura_volumen | ICP | take-profit | +2.50% | +2.00% | +0.46 |
| 2026-09-29 20:05 | ruptura_volumen_evento | VVV | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 20:05 | c_banda_atr_evento | KAS | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 20:05 | ruptura_volumen_regimen | TON | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 20:05 | ruptura_volumen_regimen | VVV | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 20:05 | c_banda_atr_regimen | KAS | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 20:05 | c_banda_atr_tope | KAS | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 20:05 | estocastico_rebote | POL | timeout | -0.19% | -0.69% | -0.16 |
| 2026-09-29 20:05 | estocastico_rebote | WLD | timeout | +0.02% | -0.48% | -0.11 |
| 2026-09-29 20:05 | ruptura_volumen | VVV | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 20:05 | c_banda_atr | KAS | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 20:00 | ruptura_volumen_evento | PENGU | stop-loss | -1.22% | -2.32% | -0.53 |
| 2026-09-29 20:00 | estocastico_rebote | TRUMP | timeout | +0.11% | -0.39% | -0.09 |

## Eventos de la última vuelta

- 2026-09-29 20:10 [pullback_tendencia] CIERRE PUMP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 20:05 [reversion_bb] ENTRADA TAO @ 266.378 (22.97 €, apertura)
- 2026-09-29 20:05 [estocastico_rebote] ENTRADA JUP @ 0.29387 (22.34 €, apertura)
- 2026-09-29 20:10 [ruptura_volumen] CIERRE ICP take-profit bruto +2.50% neto +2.00%
- 2026-09-29 20:10 [ruptura_volumen_evento] CIERRE ICP take-profit bruto +2.50% neto +1.40%
- 2026-09-29 20:05 [estocastico_rebote] ENTRADA USELESS @ 0.21095 (22.34 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
