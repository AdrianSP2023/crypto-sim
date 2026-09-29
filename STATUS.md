# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 20:26 UTC · vueltas 129 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.91 € (-1.55%) | 59 | 8 | 34% | -0.182% | -1.124% | -1.263% | -15.29 € |
| reversion_bb | 919.03 € (-0.56%) | 15 | 4 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 906.87 € (-1.88%) | 88 | 16 | 26% | -0.091% | -0.887% | -1.025% | -17.92 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.86 € (-1.88%) | 76 | 1 | 24% | -0.160% | -1.004% | -1.122% | -17.50 € |
| macd_momentum | 898.51 € (-2.78%) | 155 | 3 | 21% | -0.071% | -0.740% | -0.858% | -26.22 € |
| estocastico_rebote | 894.70 € (-3.20%) | 149 | 10 | 31% | -0.229% | -0.904% | -1.024% | -30.81 € |
| ruptura_estricta | 911.78 € (-1.35%) | 44 | 4 | 30% | -0.193% | -1.280% | -1.414% | -12.97 € |
| macd_sin_salida | 905.19 € (-2.06%) | 100 | 4 | 32% | -0.095% | -0.856% | -0.984% | -19.64 € |
| c_banda_atr_tope | 915.49 € (-0.95%) | 24 | 5 | 25% | -0.585% | -1.685% | -1.845% | -9.32 € |
| ruptura_volumen_tope | 917.13 € (-0.77%) | 28 | 5 | 18% | -0.034% | -1.134% | -1.258% | -7.31 € |
| c_banda_atr_regimen | 908.93 € (-1.66%) | 52 | 0 | 31% | -0.275% | -1.277% | -1.415% | -15.31 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 908.08 € (-1.75%) | 75 | 11 | 25% | -0.125% | -0.973% | -1.116% | -16.76 € |
| c_banda_atr_evento | 915.37 € (-0.96%) | 27 | 8 | 30% | -0.480% | -1.580% | -1.731% | -9.84 € |
| macd_momentum_evento | 912.37 € (-1.28%) | 35 | 3 | 17% | -0.431% | -1.531% | -1.660% | -12.36 € |
| ruptura_volumen_evento | 914.53 € (-1.05%) | 29 | 16 | 21% | -0.436% | -1.536% | -1.699% | -10.26 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 20:25 | ruptura_volumen_evento | SEI | timeout | +1.41% | +0.31% | +0.07 |
| 2026-09-29 20:25 | ruptura_volumen_evento | DASH | timeout | -0.78% | -1.88% | -0.43 |
| 2026-09-29 20:25 | ruptura_volumen | SEI | timeout | +1.41% | +0.91% | +0.21 |
| 2026-09-29 20:25 | ruptura_volumen | DASH | timeout | -0.78% | -1.28% | -0.29 |
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

## Eventos de la última vuelta

- 2026-09-29 20:20 [estocastico_rebote] ENTRADA PUMP @ 0.005183 (22.34 €, apertura)
- 2026-09-29 20:20 [ruptura_volumen] ENTRADA CRV @ 0.34435 (22.66 €, apertura)
- 2026-09-29 20:20 [ruptura_volumen_tope] ENTRADA CRV @ 0.34435 (22.92 €, apertura)
- 2026-09-29 20:20 [ruptura_volumen_evento] ENTRADA CRV @ 0.34435 (22.86 €, apertura)
- 2026-09-29 20:25 [ruptura_volumen] CIERRE DASH timeout bruto -0.78% neto -1.28%
- 2026-09-29 20:25 [ruptura_volumen_evento] CIERRE DASH timeout bruto -0.78% neto -1.88%
- 2026-09-29 20:20 [c_banda_atr] ENTRADA VIRTUAL @ 0.7226 (22.72 €, apertura)
- 2026-09-29 20:20 [c_banda_atr_evento] ENTRADA VIRTUAL @ 0.7226 (22.86 €, apertura)
- 2026-09-29 20:25 [ruptura_volumen] CIERRE SEI timeout bruto +1.41% neto +0.91%
- 2026-09-29 20:25 [ruptura_volumen_evento] CIERRE SEI timeout bruto +1.41% neto +0.31%
- 2026-09-29 20:20 [ruptura_volumen] ENTRADA BNB @ 667.26 (22.66 €, apertura)
- 2026-09-29 20:20 [ruptura_volumen_tope] ENTRADA BNB @ 667.26 (22.92 €, apertura)
- 2026-09-29 20:20 [ruptura_volumen_evento] ENTRADA BNB @ 667.26 (22.85 €, apertura)
- 2026-09-29 20:20 [macd_momentum] ENTRADA SPX @ 0.3659 (22.45 €, apertura)
- 2026-09-29 20:20 [macd_sin_salida] ENTRADA SPX @ 0.3659 (22.62 €, apertura)
- 2026-09-29 20:20 [macd_momentum_evento] ENTRADA SPX @ 0.3659 (22.80 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
