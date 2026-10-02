# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 06:46 UTC · vueltas 370 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.91 € (-3.61%) | 328 | 18 | 39% | +0.123% | -0.456% | -0.576% | -34.13 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 863.90 € (-6.53%) | 400 | 11 | 27% | -0.107% | -0.672% | -0.779% | -60.28 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 891.01 € (-3.60%) | 219 | 16 | 20% | -0.062% | -0.683% | -0.769% | -33.97 € |
| macd_momentum | 855.65 € (-7.42%) | 626 | 12 | 23% | +0.049% | -0.493% | -0.594% | -68.80 € |
| estocastico_rebote | 879.54 € (-4.84%) | 380 | 33 | 36% | +0.036% | -0.533% | -0.642% | -45.90 € |
| ruptura_estricta | 886.37 € (-4.10%) | 209 | 25 | 34% | -0.161% | -0.787% | -0.902% | -37.57 € |
| macd_sin_salida | 882.16 € (-4.55%) | 413 | 28 | 40% | +0.110% | -0.453% | -0.564% | -42.69 € |
| c_banda_atr_tope | 913.75 € (-1.14%) | 74 | 5 | 36% | +0.212% | -0.645% | -0.756% | -10.97 € |
| ruptura_volumen_tope | 902.41 € (-2.36%) | 122 | 4 | 25% | -0.066% | -0.783% | -0.895% | -21.84 € |
| c_banda_atr_regimen | 903.40 € (-2.26%) | 181 | 18 | 40% | +0.137% | -0.507% | -0.635% | -21.15 € |
| macd_momentum_regimen | 878.56 € (-4.94%) | 389 | 12 | 22% | +0.045% | -0.522% | -0.625% | -45.88 € |
| ruptura_volumen_regimen | 868.59 € (-6.02%) | 323 | 11 | 24% | -0.184% | -0.765% | -0.877% | -55.59 € |
| c_banda_atr_evento | 896.84 € (-2.96%) | 295 | 18 | 40% | +0.172% | -0.418% | -0.533% | -28.21 € |
| macd_momentum_evento | 860.39 € (-6.91%) | 579 | 12 | 21% | +0.050% | -0.495% | -0.594% | -64.06 € |
| ruptura_volumen_evento | 876.19 € (-5.20%) | 350 | 11 | 28% | -0.033% | -0.608% | -0.709% | -47.99 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 06:45 | macd_momentum_evento | XRP | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-02 06:45 | macd_momentum_regimen | XRP | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-02 06:45 | estocastico_rebote | POL | timeout | +0.94% | +0.44% | +0.10 |
| 2026-10-02 06:45 | estocastico_rebote | AAVE | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 06:45 | macd_momentum | XRP | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-02 06:45 | pullback_tendencia | BNB | timeout | +0.45% | -0.05% | -0.01 |
| 2026-10-02 06:45 | pullback_tendencia | FET | rotura de tendencia | -0.47% | -0.97% | -0.22 |
| 2026-10-02 06:40 | macd_momentum_evento | WLFI | momentum perdido | -0.20% | -0.70% | -0.15 |
| 2026-10-02 06:40 | c_banda_atr_evento | WLFI | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-02 06:40 | macd_momentum_regimen | WLFI | momentum perdido | -0.20% | -0.70% | -0.15 |
| 2026-10-02 06:40 | c_banda_atr_regimen | WLFI | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-02 06:40 | ruptura_volumen_tope | BNB | timeout | -0.64% | -1.14% | -0.26 |
| 2026-10-02 06:40 | c_banda_atr_tope | WLFI | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-02 06:40 | estocastico_rebote | LINK | timeout | +0.11% | -0.39% | -0.08 |
| 2026-10-02 06:40 | macd_momentum | WLFI | momentum perdido | -0.20% | -0.70% | -0.15 |

## Eventos de la última vuelta

- 2026-10-02 06:45 [macd_momentum] CIERRE XRP momentum perdido bruto -0.15% neto -0.65%
- 2026-10-02 06:45 [macd_momentum_regimen] CIERRE XRP momentum perdido bruto -0.15% neto -0.65%
- 2026-10-02 06:45 [macd_momentum_evento] CIERRE XRP momentum perdido bruto -0.15% neto -0.65%
- 2026-10-02 06:40 [macd_momentum] ENTRADA ADA @ 0.227135 (21.39 €, apertura)
- 2026-10-02 06:40 [macd_sin_salida] ENTRADA ADA @ 0.227135 (22.04 €, apertura)
- 2026-10-02 06:40 [macd_momentum_regimen] ENTRADA ADA @ 0.227135 (21.96 €, apertura)
- 2026-10-02 06:40 [macd_momentum_evento] ENTRADA ADA @ 0.227135 (21.50 €, apertura)
- 2026-10-02 06:40 [pullback_tendencia] ENTRADA SUI @ 1.0562 (22.26 €, apertura)
- 2026-10-02 06:45 [estocastico_rebote] CIERRE AAVE take-profit bruto +1.80% neto +1.30%
- 2026-10-02 06:40 [estocastico_rebote] ENTRADA ZRO @ 1.671 (21.96 €, apertura)
- 2026-10-02 06:40 [pullback_tendencia] ENTRADA DOGE @ 0.0852993 (22.26 €, apertura)
- 2026-10-02 06:45 [pullback_tendencia] CIERRE FET rotura de tendencia bruto -0.47% neto -0.97%
- 2026-10-02 06:45 [estocastico_rebote] CIERRE POL timeout bruto +0.94% neto +0.44%
- 2026-10-02 06:45 [pullback_tendencia] CIERRE BNB timeout bruto +0.45% neto -0.05%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
