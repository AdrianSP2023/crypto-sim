# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 20:06 UTC · vueltas 125 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.91 € (-1.66%) | 59 | 5 | 34% | -0.182% | -1.124% | -1.263% | -15.29 € |
| reversion_bb | 918.51 € (-0.62%) | 15 | 3 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 904.73 € (-2.11%) | 82 | 19 | 26% | -0.113% | -0.932% | -1.073% | -17.53 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.92 € (-1.87%) | 75 | 1 | 24% | -0.142% | -0.990% | -1.106% | -17.05 € |
| macd_momentum | 898.03 € (-2.84%) | 155 | 1 | 21% | -0.071% | -0.740% | -0.858% | -26.22 € |
| estocastico_rebote | 893.43 € (-3.33%) | 149 | 3 | 31% | -0.229% | -0.904% | -1.024% | -30.81 € |
| ruptura_estricta | 910.84 € (-1.45%) | 44 | 2 | 30% | -0.193% | -1.280% | -1.414% | -12.97 € |
| macd_sin_salida | 904.71 € (-2.11%) | 100 | 2 | 32% | -0.095% | -0.856% | -0.984% | -19.64 € |
| c_banda_atr_tope | 914.86 € (-1.01%) | 24 | 4 | 25% | -0.585% | -1.685% | -1.845% | -9.32 € |
| ruptura_volumen_tope | 917.51 € (-0.73%) | 25 | 4 | 20% | +0.024% | -1.076% | -1.207% | -6.20 € |
| c_banda_atr_regimen | 908.93 € (-1.66%) | 52 | 0 | 31% | -0.275% | -1.277% | -1.415% | -15.31 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 906.24 € (-1.95%) | 75 | 11 | 25% | -0.125% | -0.973% | -1.116% | -16.76 € |
| c_banda_atr_evento | 914.36 € (-1.07%) | 27 | 5 | 30% | -0.480% | -1.580% | -1.731% | -9.84 € |
| macd_momentum_evento | 911.89 € (-1.34%) | 35 | 1 | 17% | -0.431% | -1.531% | -1.660% | -12.36 € |
| ruptura_volumen_evento | 913.20 € (-1.19%) | 23 | 19 | 17% | -0.606% | -1.706% | -1.887% | -9.04 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-29 20:00 | estocastico_rebote | FIL | timeout | +0.75% | +0.25% | +0.06 |
| 2026-09-29 20:00 | estocastico_rebote | XRP | timeout | +0.31% | -0.19% | -0.04 |
| 2026-09-29 20:00 | pullback_tendencia | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-29 20:05 [ruptura_volumen] CIERRE VVV stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 20:05 [ruptura_volumen_regimen] CIERRE VVV stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 20:05 [ruptura_volumen_evento] CIERRE VVV stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 20:05 [estocastico_rebote] CIERRE WLD timeout bruto +0.02% neto -0.48%
- 2026-09-29 20:05 [ruptura_volumen_regimen] CIERRE TON stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 20:05 [estocastico_rebote] CIERRE POL timeout bruto -0.19% neto -0.69%
- 2026-09-29 20:05 [c_banda_atr] CIERRE KAS stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 20:05 [c_banda_atr_tope] CIERRE KAS stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 20:05 [c_banda_atr_regimen] CIERRE KAS stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 20:05 [c_banda_atr_evento] CIERRE KAS stop-loss bruto -1.50% neto -2.60%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
