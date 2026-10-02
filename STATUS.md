# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 07:16 UTC · vueltas 376 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.30 € (-3.78%) | 331 | 17 | 40% | +0.134% | -0.445% | -0.566% | -33.59 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 863.20 € (-6.60%) | 406 | 9 | 27% | -0.116% | -0.680% | -0.787% | -61.85 € |
| rebote_extremo | 922.25 € (-0.22%) | 14 | 1 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.61 € (-3.64%) | 229 | 13 | 21% | -0.031% | -0.646% | -0.734% | -33.64 € |
| macd_momentum | 854.04 € (-7.60%) | 640 | 6 | 22% | +0.045% | -0.495% | -0.597% | -70.59 € |
| estocastico_rebote | 878.81 € (-4.92%) | 382 | 33 | 36% | +0.045% | -0.523% | -0.632% | -45.33 € |
| ruptura_estricta | 885.78 € (-4.16%) | 211 | 24 | 34% | -0.153% | -0.778% | -0.893% | -37.46 € |
| macd_sin_salida | 881.63 € (-4.61%) | 418 | 29 | 41% | +0.127% | -0.436% | -0.547% | -41.56 € |
| c_banda_atr_tope | 913.37 € (-1.18%) | 75 | 4 | 37% | +0.236% | -0.616% | -0.732% | -10.63 € |
| ruptura_volumen_tope | 902.35 € (-2.37%) | 122 | 5 | 25% | -0.066% | -0.783% | -0.895% | -21.84 € |
| c_banda_atr_regimen | 901.82 € (-2.43%) | 183 | 18 | 40% | +0.149% | -0.494% | -0.624% | -20.82 € |
| macd_momentum_regimen | 876.91 € (-5.12%) | 403 | 6 | 22% | +0.040% | -0.525% | -0.628% | -47.71 € |
| ruptura_volumen_regimen | 867.89 € (-6.10%) | 329 | 9 | 24% | -0.194% | -0.773% | -0.886% | -57.17 € |
| c_banda_atr_evento | 895.22 € (-3.14%) | 298 | 17 | 41% | +0.183% | -0.405% | -0.522% | -27.66 € |
| macd_momentum_evento | 858.77 € (-7.08%) | 593 | 6 | 21% | +0.047% | -0.498% | -0.596% | -65.86 € |
| ruptura_volumen_evento | 875.48 € (-5.28%) | 356 | 9 | 28% | -0.044% | -0.618% | -0.719% | -49.57 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 07:15 | pullback_tendencia | AVAX | rotura de tendencia | -0.53% | -1.03% | -0.23 |
| 2026-10-02 07:15 | pullback_tendencia | NEAR | rotura de tendencia | -0.72% | -1.22% | -0.27 |
| 2026-10-02 07:10 | macd_momentum_evento | NIGHT | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 07:10 | macd_momentum_evento | WLD | momentum perdido | -0.06% | -0.56% | -0.12 |
| 2026-10-02 07:10 | macd_momentum_evento | CRV | momentum perdido | -0.43% | -0.94% | -0.20 |
| 2026-10-02 07:10 | macd_momentum_evento | AVAX | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 07:10 | macd_momentum_regimen | NIGHT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 07:10 | macd_momentum_regimen | WLD | momentum perdido | -0.06% | -0.56% | -0.12 |
| 2026-10-02 07:10 | macd_momentum_regimen | CRV | momentum perdido | -0.43% | -0.94% | -0.20 |
| 2026-10-02 07:10 | macd_momentum_regimen | AVAX | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 07:10 | macd_sin_salida | BCH | timeout | +1.39% | +0.89% | +0.20 |
| 2026-10-02 07:10 | macd_sin_salida | NIGHT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 07:10 | macd_momentum | NIGHT | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 07:10 | macd_momentum | WLD | momentum perdido | -0.06% | -0.56% | -0.12 |
| 2026-10-02 07:10 | macd_momentum | CRV | momentum perdido | -0.43% | -0.94% | -0.20 |

## Eventos de la última vuelta

- 2026-10-02 07:15 [pullback_tendencia] CIERRE NEAR rotura de tendencia bruto -0.72% neto -1.22%
- 2026-10-02 07:15 [pullback_tendencia] CIERRE AVAX rotura de tendencia bruto -0.53% neto -1.03%
- 2026-10-02 07:10 [ruptura_volumen] ENTRADA NIGHT @ 0.03655 (21.56 €, apertura)
- 2026-10-02 07:10 [ruptura_estricta] ENTRADA NIGHT @ 0.03655 (22.17 €, apertura)
- 2026-10-02 07:10 [ruptura_volumen_regimen] ENTRADA NIGHT @ 0.03655 (21.68 €, apertura)
- 2026-10-02 07:10 [ruptura_volumen_evento] ENTRADA NIGHT @ 0.03655 (21.87 €, apertura)
- 2026-10-02 07:10 [macd_momentum] ENTRADA OP @ 0.1174 (21.34 €, apertura)
- 2026-10-02 07:10 [macd_sin_salida] ENTRADA OP @ 0.1174 (22.07 €, apertura)
- 2026-10-02 07:10 [macd_momentum_regimen] ENTRADA OP @ 0.1174 (21.91 €, apertura)
- 2026-10-02 07:10 [macd_momentum_evento] ENTRADA OP @ 0.1174 (21.46 €, apertura)
- 2026-10-02 07:10 [ruptura_volumen] ENTRADA MINA @ 0.1447 (21.56 €, apertura)
- 2026-10-02 07:10 [ruptura_volumen_regimen] ENTRADA MINA @ 0.1447 (21.68 €, apertura)
- 2026-10-02 07:10 [ruptura_volumen_evento] ENTRADA MINA @ 0.1447 (21.87 €, apertura)
- 2026-10-02 07:10 [macd_momentum] ENTRADA KSM @ 4.61 (21.34 €, apertura)
- 2026-10-02 07:10 [macd_sin_salida] ENTRADA KSM @ 4.61 (22.07 €, apertura)
- 2026-10-02 07:10 [macd_momentum_regimen] ENTRADA KSM @ 4.61 (21.91 €, apertura)
- 2026-10-02 07:10 [macd_momentum_evento] ENTRADA KSM @ 4.61 (21.46 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
