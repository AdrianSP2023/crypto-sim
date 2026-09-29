# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 20:21 UTC · vueltas 128 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.71 € (-1.57%) | 59 | 7 | 34% | -0.182% | -1.124% | -1.263% | -15.29 € |
| reversion_bb | 918.90 € (-0.58%) | 15 | 4 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 906.51 € (-1.92%) | 86 | 16 | 26% | -0.100% | -0.904% | -1.043% | -17.83 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.74 € (-1.89%) | 76 | 1 | 24% | -0.160% | -1.004% | -1.122% | -17.50 € |
| macd_momentum | 898.42 € (-2.79%) | 155 | 2 | 21% | -0.071% | -0.740% | -0.858% | -26.22 € |
| estocastico_rebote | 893.94 € (-3.28%) | 149 | 9 | 31% | -0.229% | -0.904% | -1.024% | -30.81 € |
| ruptura_estricta | 911.58 € (-1.37%) | 44 | 4 | 30% | -0.193% | -1.280% | -1.414% | -12.97 € |
| macd_sin_salida | 905.11 € (-2.07%) | 100 | 3 | 32% | -0.095% | -0.856% | -0.984% | -19.64 € |
| c_banda_atr_tope | 915.42 € (-0.95%) | 24 | 5 | 25% | -0.585% | -1.685% | -1.845% | -9.32 € |
| ruptura_volumen_tope | 917.14 € (-0.77%) | 28 | 3 | 18% | -0.034% | -1.134% | -1.258% | -7.31 € |
| c_banda_atr_regimen | 908.93 € (-1.66%) | 52 | 0 | 31% | -0.275% | -1.277% | -1.415% | -15.31 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 907.47 € (-1.81%) | 75 | 11 | 25% | -0.125% | -0.973% | -1.116% | -16.76 € |
| c_banda_atr_evento | 915.17 € (-0.98%) | 27 | 7 | 30% | -0.480% | -1.580% | -1.731% | -9.84 € |
| macd_momentum_evento | 912.29 € (-1.29%) | 35 | 2 | 17% | -0.431% | -1.531% | -1.660% | -12.36 € |
| ruptura_volumen_evento | 914.45 € (-1.06%) | 27 | 16 | 19% | -0.491% | -1.591% | -1.760% | -9.90 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 20:20 | ruptura_volumen_evento | ASTER | timeout | -0.18% | -1.28% | -0.29 |
| 2026-09-29 20:20 | ruptura_volumen_evento | ARB | timeout | -0.16% | -1.26% | -0.29 |
| 2026-09-29 20:20 | ruptura_volumen_tope | ASTER | timeout | -0.18% | -1.28% | -0.29 |
| 2026-09-29 20:20 | ruptura_volumen_tope | ARB | timeout | -0.16% | -1.26% | -0.29 |
| 2026-09-29 20:20 | ruptura_volumen | ASTER | timeout | -0.18% | -0.68% | -0.15 |
| 2026-09-29 20:20 | ruptura_volumen | ARB | timeout | -0.16% | -0.66% | -0.15 |
| 2026-09-29 20:15 | ruptura_volumen_evento | TON | stop-loss | -1.49% | -2.59% | -0.59 |
| 2026-09-29 20:15 | ruptura_volumen_tope | ICP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 20:15 | ruptura_volumen | TON | stop-loss | -1.49% | -1.99% | -0.45 |
| 2026-09-29 20:10 | ruptura_volumen_evento | ICP | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 20:10 | pullback_tendencia | PUMP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 20:10 | ruptura_volumen | ICP | take-profit | +2.50% | +2.00% | +0.46 |
| 2026-09-29 20:05 | ruptura_volumen_evento | VVV | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 20:05 | c_banda_atr_evento | KAS | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 20:05 | ruptura_volumen_regimen | TON | stop-loss | -1.20% | -1.70% | -0.39 |

## Eventos de la última vuelta

- 2026-09-29 20:15 [ruptura_volumen] ENTRADA AVAX @ 10.087 (22.67 €, apertura)
- 2026-09-29 20:15 [ruptura_estricta] ENTRADA AVAX @ 10.087 (22.78 €, apertura)
- 2026-09-29 20:15 [ruptura_volumen_tope] ENTRADA AVAX @ 10.087 (22.94 €, apertura)
- 2026-09-29 20:15 [ruptura_volumen_evento] ENTRADA AVAX @ 10.087 (22.87 €, apertura)
- 2026-09-29 20:20 [ruptura_volumen] CIERRE ARB timeout bruto -0.16% neto -0.66%
- 2026-09-29 20:20 [ruptura_volumen_tope] CIERRE ARB timeout bruto -0.16% neto -1.26%
- 2026-09-29 20:20 [ruptura_volumen_evento] CIERRE ARB timeout bruto -0.16% neto -1.26%
- 2026-09-29 20:15 [pullback_tendencia] ENTRADA INJ @ 6.804 (22.67 €, apertura)
- 2026-09-29 20:20 [ruptura_volumen] CIERRE ASTER timeout bruto -0.18% neto -0.68%
- 2026-09-29 20:20 [ruptura_volumen_tope] CIERRE ASTER timeout bruto -0.18% neto -1.28%
- 2026-09-29 20:20 [ruptura_volumen_evento] CIERRE ASTER timeout bruto -0.18% neto -1.28%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
