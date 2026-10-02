# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 06:51 UTC · vueltas 371 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.59 € (-3.64%) | 329 | 17 | 39% | +0.124% | -0.455% | -0.575% | -34.14 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 863.58 € (-6.56%) | 402 | 10 | 27% | -0.107% | -0.672% | -0.779% | -60.60 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.79 € (-3.62%) | 220 | 16 | 20% | -0.062% | -0.682% | -0.768% | -34.11 € |
| macd_momentum | 855.50 € (-7.44%) | 626 | 15 | 23% | +0.049% | -0.493% | -0.594% | -68.80 € |
| estocastico_rebote | 879.36 € (-4.86%) | 380 | 35 | 36% | +0.036% | -0.533% | -0.642% | -45.90 € |
| ruptura_estricta | 886.29 € (-4.11%) | 209 | 25 | 34% | -0.161% | -0.787% | -0.902% | -37.57 € |
| macd_sin_salida | 881.91 € (-4.58%) | 414 | 30 | 40% | +0.110% | -0.453% | -0.563% | -42.75 € |
| c_banda_atr_tope | 913.58 € (-1.15%) | 74 | 5 | 36% | +0.212% | -0.645% | -0.756% | -10.97 € |
| ruptura_volumen_tope | 902.42 € (-2.36%) | 122 | 5 | 25% | -0.066% | -0.783% | -0.895% | -21.84 € |
| c_banda_atr_regimen | 903.12 € (-2.29%) | 182 | 17 | 40% | +0.138% | -0.505% | -0.633% | -21.16 € |
| macd_momentum_regimen | 878.40 € (-4.96%) | 389 | 15 | 22% | +0.045% | -0.522% | -0.625% | -45.88 € |
| ruptura_volumen_regimen | 868.27 € (-6.06%) | 325 | 10 | 24% | -0.185% | -0.765% | -0.877% | -55.91 € |
| c_banda_atr_evento | 896.51 € (-3.00%) | 296 | 17 | 40% | +0.173% | -0.417% | -0.532% | -28.22 € |
| macd_momentum_evento | 860.24 € (-6.93%) | 579 | 15 | 21% | +0.050% | -0.495% | -0.594% | -64.06 € |
| ruptura_volumen_evento | 875.87 € (-5.23%) | 352 | 10 | 28% | -0.034% | -0.609% | -0.710% | -48.30 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 06:50 | ruptura_volumen_evento | APT | timeout | +0.16% | -0.34% | -0.07 |
| 2026-10-02 06:50 | ruptura_volumen_evento | XLM | timeout | -0.61% | -1.11% | -0.24 |
| 2026-10-02 06:50 | c_banda_atr_evento | OP | timeout | +0.43% | -0.07% | -0.02 |
| 2026-10-02 06:50 | ruptura_volumen_regimen | APT | timeout | +0.16% | -0.34% | -0.07 |
| 2026-10-02 06:50 | ruptura_volumen_regimen | XLM | timeout | -0.61% | -1.11% | -0.24 |
| 2026-10-02 06:50 | c_banda_atr_regimen | OP | timeout | +0.43% | -0.07% | -0.02 |
| 2026-10-02 06:50 | macd_sin_salida | BNB | timeout | +0.21% | -0.29% | -0.06 |
| 2026-10-02 06:50 | pullback_tendencia | SUI | rotura de tendencia | -0.11% | -0.61% | -0.14 |
| 2026-10-02 06:50 | ruptura_volumen | APT | timeout | +0.16% | -0.34% | -0.07 |
| 2026-10-02 06:50 | ruptura_volumen | XLM | timeout | -0.61% | -1.11% | -0.24 |
| 2026-10-02 06:50 | c_banda_atr | OP | timeout | +0.43% | -0.07% | -0.02 |
| 2026-10-02 06:45 | macd_momentum_evento | XRP | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-02 06:45 | macd_momentum_regimen | XRP | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-02 06:45 | estocastico_rebote | POL | timeout | +0.94% | +0.44% | +0.10 |
| 2026-10-02 06:45 | estocastico_rebote | AAVE | take-profit | +1.80% | +1.30% | +0.28 |

## Eventos de la última vuelta

- 2026-10-02 06:50 [pullback_tendencia] CIERRE SUI rotura de tendencia bruto -0.11% neto -0.61%
- 2026-10-02 06:45 [macd_momentum] ENTRADA SUI @ 1.0552 (21.39 €, apertura)
- 2026-10-02 06:45 [macd_sin_salida] ENTRADA SUI @ 1.0552 (22.04 €, apertura)
- 2026-10-02 06:45 [macd_momentum_regimen] ENTRADA SUI @ 1.0552 (21.96 €, apertura)
- 2026-10-02 06:45 [macd_momentum_evento] ENTRADA SUI @ 1.0552 (21.50 €, apertura)
- 2026-10-02 06:45 [macd_momentum] ENTRADA PUMP @ 0.005273 (21.39 €, apertura)
- 2026-10-02 06:45 [macd_sin_salida] ENTRADA PUMP @ 0.005273 (22.04 €, apertura)
- 2026-10-02 06:45 [macd_momentum_regimen] ENTRADA PUMP @ 0.005273 (21.96 €, apertura)
- 2026-10-02 06:45 [macd_momentum_evento] ENTRADA PUMP @ 0.005273 (21.50 €, apertura)
- 2026-10-02 06:50 [ruptura_volumen] CIERRE XLM timeout bruto -0.61% neto -1.11%
- 2026-10-02 06:50 [ruptura_volumen_regimen] CIERRE XLM timeout bruto -0.61% neto -1.11%
- 2026-10-02 06:50 [ruptura_volumen_evento] CIERRE XLM timeout bruto -0.61% neto -1.11%
- 2026-10-02 06:45 [pullback_tendencia] ENTRADA ZRO @ 1.683 (22.25 €, apertura)
- 2026-10-02 06:45 [ruptura_volumen] ENTRADA MON @ 0.0304 (21.59 €, apertura)
- 2026-10-02 06:45 [ruptura_volumen_tope] ENTRADA MON @ 0.0304 (22.56 €, apertura)
- 2026-10-02 06:45 [ruptura_volumen_regimen] ENTRADA MON @ 0.0304 (21.71 €, apertura)
- 2026-10-02 06:45 [ruptura_volumen_evento] ENTRADA MON @ 0.0304 (21.90 €, apertura)
- 2026-10-02 06:50 [c_banda_atr] CIERRE OP timeout bruto +0.43% neto -0.07%
- 2026-10-02 06:50 [c_banda_atr_regimen] CIERRE OP timeout bruto +0.43% neto -0.07%
- 2026-10-02 06:50 [c_banda_atr_evento] CIERRE OP timeout bruto +0.43% neto -0.07%
- 2026-10-02 06:45 [macd_momentum] ENTRADA ASTER @ 0.66931 (21.39 €, apertura)
- 2026-10-02 06:45 [estocastico_rebote] ENTRADA ASTER @ 0.66931 (21.96 €, apertura)
- 2026-10-02 06:45 [macd_sin_salida] ENTRADA ASTER @ 0.66931 (22.04 €, apertura)
- 2026-10-02 06:45 [macd_momentum_regimen] ENTRADA ASTER @ 0.66931 (21.96 €, apertura)
- 2026-10-02 06:45 [macd_momentum_evento] ENTRADA ASTER @ 0.66931 (21.50 €, apertura)
- 2026-10-02 06:45 [estocastico_rebote] ENTRADA DASH @ 53.236 (21.96 €, apertura)
- 2026-10-02 06:50 [macd_sin_salida] CIERRE BNB timeout bruto +0.21% neto -0.29%
- 2026-10-02 06:50 [ruptura_volumen] CIERRE APT timeout bruto +0.16% neto -0.34%
- 2026-10-02 06:50 [ruptura_volumen_regimen] CIERRE APT timeout bruto +0.16% neto -0.34%
- 2026-10-02 06:50 [ruptura_volumen_evento] CIERRE APT timeout bruto +0.16% neto -0.34%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
