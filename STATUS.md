# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 20:16 UTC · vueltas 127 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.89 € (-1.66%) | 59 | 7 | 34% | -0.182% | -1.124% | -1.263% | -15.29 € |
| reversion_bb | 918.60 € (-0.61%) | 15 | 4 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 905.43 € (-2.04%) | 84 | 17 | 26% | -0.099% | -0.909% | -1.050% | -17.53 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.74 € (-1.89%) | 76 | 0 | 24% | -0.160% | -1.004% | -1.122% | -17.50 € |
| macd_momentum | 898.28 € (-2.81%) | 155 | 2 | 21% | -0.071% | -0.740% | -0.858% | -26.22 € |
| estocastico_rebote | 893.46 € (-3.33%) | 149 | 9 | 31% | -0.229% | -0.904% | -1.024% | -30.81 € |
| ruptura_estricta | 910.80 € (-1.45%) | 44 | 3 | 30% | -0.193% | -1.280% | -1.414% | -12.97 € |
| macd_sin_salida | 904.96 € (-2.09%) | 100 | 3 | 32% | -0.095% | -0.856% | -0.984% | -19.64 € |
| c_banda_atr_tope | 915.00 € (-1.00%) | 24 | 5 | 25% | -0.585% | -1.685% | -1.845% | -9.32 € |
| ruptura_volumen_tope | 917.28 € (-0.75%) | 26 | 4 | 19% | -0.023% | -1.123% | -1.252% | -6.73 € |
| c_banda_atr_regimen | 908.93 € (-1.66%) | 52 | 0 | 31% | -0.275% | -1.277% | -1.415% | -15.31 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 906.48 € (-1.92%) | 75 | 11 | 25% | -0.125% | -0.973% | -1.116% | -16.76 € |
| c_banda_atr_evento | 914.34 € (-1.07%) | 27 | 7 | 30% | -0.480% | -1.580% | -1.731% | -9.84 € |
| macd_momentum_evento | 912.14 € (-1.31%) | 35 | 2 | 17% | -0.431% | -1.531% | -1.660% | -12.36 € |
| ruptura_volumen_evento | 913.63 € (-1.15%) | 25 | 17 | 20% | -0.517% | -1.617% | -1.794% | -9.31 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 20:15 | ruptura_volumen_evento | TON | stop-loss | -1.49% | -2.59% | -0.59 |
| 2026-09-29 20:15 | ruptura_volumen_tope | ICP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 20:15 | ruptura_volumen | TON | stop-loss | -1.49% | -1.99% | -0.45 |
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

## Eventos de la última vuelta

- 2026-09-29 20:10 [estocastico_rebote] ENTRADA NEAR @ 4.3691 (22.34 €, apertura)
- 2026-09-29 20:10 [macd_momentum] ENTRADA AVAX @ 10.029 (22.45 €, apertura)
- 2026-09-29 20:10 [macd_sin_salida] ENTRADA AVAX @ 10.029 (22.62 €, apertura)
- 2026-09-29 20:10 [macd_momentum_evento] ENTRADA AVAX @ 10.029 (22.80 €, apertura)
- 2026-09-29 20:10 [c_banda_atr] ENTRADA CRV @ 0.34136 (22.72 €, apertura)
- 2026-09-29 20:10 [c_banda_atr_tope] ENTRADA CRV @ 0.34136 (22.87 €, apertura)
- 2026-09-29 20:10 [c_banda_atr_evento] ENTRADA CRV @ 0.34136 (22.86 €, apertura)
- 2026-09-29 20:10 [ruptura_estricta] ENTRADA ICP @ 3.077 (22.78 €, apertura)
- 2026-09-29 20:10 [ruptura_volumen_tope] ENTRADA ICP @ 3.077 (22.95 €, apertura)
- 2026-09-29 20:15 [ruptura_volumen_tope] CIERRE ICP stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 20:10 [c_banda_atr] ENTRADA NIGHT @ 0.02826 (22.72 €, apertura)
- 2026-09-29 20:10 [c_banda_atr_evento] ENTRADA NIGHT @ 0.02826 (22.86 €, apertura)
- 2026-09-29 20:10 [estocastico_rebote] ENTRADA FIL @ 0.945 (22.34 €, apertura)
- 2026-09-29 20:15 [ruptura_volumen] CIERRE TON stop-loss bruto -1.49% neto -1.99%
- 2026-09-29 20:15 [ruptura_volumen_evento] CIERRE TON stop-loss bruto -1.49% neto -2.59%
- 2026-09-29 20:10 [estocastico_rebote] ENTRADA PENGU @ 0.008717 (22.34 €, apertura)
- 2026-09-29 20:10 [estocastico_rebote] ENTRADA TRUMP @ 1.794 (22.34 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
