# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 07:21 UTC · vueltas 377 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.70 € (-3.85%) | 332 | 16 | 39% | +0.129% | -0.450% | -0.571% | -34.03 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 862.85 € (-6.64%) | 406 | 9 | 27% | -0.116% | -0.680% | -0.787% | -61.85 € |
| rebote_extremo | 922.23 € (-0.22%) | 14 | 1 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.22 € (-3.68%) | 231 | 11 | 21% | -0.024% | -0.639% | -0.726% | -33.54 € |
| macd_momentum | 853.77 € (-7.62%) | 640 | 7 | 22% | +0.045% | -0.495% | -0.597% | -70.59 € |
| estocastico_rebote | 877.51 € (-5.06%) | 384 | 32 | 36% | +0.045% | -0.523% | -0.631% | -45.53 € |
| ruptura_estricta | 884.76 € (-4.27%) | 211 | 25 | 34% | -0.153% | -0.778% | -0.893% | -37.46 € |
| macd_sin_salida | 880.59 € (-4.72%) | 419 | 29 | 41% | +0.127% | -0.436% | -0.547% | -41.65 € |
| c_banda_atr_tope | 913.22 € (-1.19%) | 75 | 4 | 37% | +0.236% | -0.616% | -0.732% | -10.63 € |
| ruptura_volumen_tope | 902.16 € (-2.39%) | 122 | 5 | 25% | -0.066% | -0.783% | -0.895% | -21.84 € |
| c_banda_atr_regimen | 901.20 € (-2.49%) | 184 | 17 | 40% | +0.140% | -0.502% | -0.632% | -21.28 € |
| macd_momentum_regimen | 876.63 € (-5.15%) | 403 | 7 | 22% | +0.040% | -0.525% | -0.628% | -47.71 € |
| ruptura_volumen_regimen | 867.53 € (-6.14%) | 329 | 9 | 24% | -0.194% | -0.773% | -0.886% | -57.17 € |
| c_banda_atr_evento | 894.62 € (-3.21%) | 299 | 16 | 40% | +0.177% | -0.411% | -0.528% | -28.11 € |
| macd_momentum_evento | 858.50 € (-7.11%) | 593 | 7 | 21% | +0.047% | -0.498% | -0.596% | -65.86 € |
| ruptura_volumen_evento | 875.13 € (-5.31%) | 356 | 9 | 28% | -0.044% | -0.618% | -0.719% | -49.57 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 07:20 | c_banda_atr_evento | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 07:20 | c_banda_atr_regimen | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 07:20 | macd_sin_salida | AVAX | timeout | +0.10% | -0.40% | -0.09 |
| 2026-10-02 07:20 | estocastico_rebote | HBAR | timeout | +0.04% | -0.46% | -0.10 |
| 2026-10-02 07:20 | estocastico_rebote | ETH | timeout | +0.06% | -0.44% | -0.10 |
| 2026-10-02 07:20 | pullback_tendencia | ONDO | rotura de tendencia | -0.58% | -1.08% | -0.24 |
| 2026-10-02 07:20 | pullback_tendencia | PUMP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 07:20 | c_banda_atr | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 07:15 | pullback_tendencia | AVAX | rotura de tendencia | -0.53% | -1.03% | -0.23 |
| 2026-10-02 07:15 | pullback_tendencia | NEAR | rotura de tendencia | -0.72% | -1.22% | -0.27 |
| 2026-10-02 07:10 | macd_momentum_evento | NIGHT | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 07:10 | macd_momentum_evento | WLD | momentum perdido | -0.06% | -0.56% | -0.12 |
| 2026-10-02 07:10 | macd_momentum_evento | CRV | momentum perdido | -0.43% | -0.94% | -0.20 |
| 2026-10-02 07:10 | macd_momentum_evento | AVAX | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 07:10 | macd_momentum_regimen | NIGHT | take-profit | +2.00% | +1.50% | +0.33 |

## Eventos de la última vuelta

- 2026-10-02 07:20 [estocastico_rebote] CIERRE ETH timeout bruto +0.06% neto -0.44%
- 2026-10-02 07:20 [macd_sin_salida] CIERRE AVAX timeout bruto +0.10% neto -0.40%
- 2026-10-02 07:20 [estocastico_rebote] CIERRE HBAR timeout bruto +0.04% neto -0.46%
- 2026-10-02 07:20 [pullback_tendencia] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 07:20 [c_banda_atr] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 07:20 [c_banda_atr_regimen] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 07:20 [c_banda_atr_evento] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 07:20 [pullback_tendencia] CIERRE ONDO rotura de tendencia bruto -0.58% neto -1.08%
- 2026-10-02 07:15 [macd_momentum] ENTRADA INJ @ 6.664 (21.34 €, apertura)
- 2026-10-02 07:15 [macd_sin_salida] ENTRADA INJ @ 6.664 (22.07 €, apertura)
- 2026-10-02 07:15 [macd_momentum_regimen] ENTRADA INJ @ 6.664 (21.91 €, apertura)
- 2026-10-02 07:15 [macd_momentum_evento] ENTRADA INJ @ 6.664 (21.46 €, apertura)
- 2026-10-02 07:15 [ruptura_estricta] ENTRADA MINA @ 0.1474 (22.17 €, apertura)
- 2026-10-02 07:15 [estocastico_rebote] ENTRADA SEI @ 0.06343 (21.97 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
