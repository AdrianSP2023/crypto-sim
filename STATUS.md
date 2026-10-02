# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 07:31 UTC · vueltas 379 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.34 € (-3.88%) | 332 | 16 | 39% | +0.129% | -0.450% | -0.571% | -34.03 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 862.67 € (-6.66%) | 407 | 8 | 27% | -0.116% | -0.680% | -0.787% | -61.99 € |
| rebote_extremo | 922.32 € (-0.21%) | 14 | 1 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.59 € (-3.75%) | 235 | 8 | 20% | -0.031% | -0.643% | -0.730% | -34.34 € |
| macd_momentum | 853.65 € (-7.64%) | 645 | 3 | 22% | +0.046% | -0.494% | -0.596% | -70.98 € |
| estocastico_rebote | 876.56 € (-5.16%) | 385 | 32 | 36% | +0.042% | -0.525% | -0.634% | -45.83 € |
| ruptura_estricta | 882.08 € (-4.56%) | 229 | 7 | 32% | -0.182% | -0.797% | -0.911% | -41.54 € |
| macd_sin_salida | 879.05 € (-4.89%) | 432 | 16 | 40% | +0.113% | -0.447% | -0.558% | -44.02 € |
| c_banda_atr_tope | 913.11 € (-1.20%) | 75 | 4 | 37% | +0.236% | -0.616% | -0.732% | -10.63 € |
| ruptura_volumen_tope | 901.97 € (-2.41%) | 123 | 4 | 25% | -0.067% | -0.782% | -0.894% | -21.99 € |
| c_banda_atr_regimen | 900.71 € (-2.55%) | 184 | 17 | 40% | +0.140% | -0.502% | -0.632% | -21.28 € |
| macd_momentum_regimen | 876.51 € (-5.16%) | 408 | 3 | 22% | +0.041% | -0.523% | -0.626% | -48.11 € |
| ruptura_volumen_regimen | 867.35 € (-6.16%) | 330 | 8 | 24% | -0.194% | -0.773% | -0.885% | -57.31 € |
| c_banda_atr_evento | 894.25 € (-3.24%) | 299 | 16 | 40% | +0.177% | -0.411% | -0.528% | -28.11 € |
| macd_momentum_evento | 858.38 € (-7.13%) | 598 | 3 | 21% | +0.048% | -0.497% | -0.595% | -66.25 € |
| ruptura_volumen_evento | 874.94 € (-5.33%) | 357 | 8 | 27% | -0.044% | -0.618% | -0.719% | -49.72 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 07:30 | macd_momentum_evento | ASTER | momentum perdido | -0.76% | -1.26% | -0.27 |
| 2026-10-02 07:30 | macd_momentum_evento | PUMP | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 07:30 | macd_momentum_regimen | ASTER | momentum perdido | -0.76% | -1.26% | -0.28 |
| 2026-10-02 07:30 | macd_momentum_regimen | PUMP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 07:30 | macd_sin_salida | KAS | timeout | -0.93% | -1.43% | -0.31 |
| 2026-10-02 07:30 | macd_sin_salida | PUMP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 07:30 | ruptura_estricta | TRUMP | timeout | +0.22% | -0.28% | -0.06 |
| 2026-10-02 07:30 | ruptura_estricta | KSM | timeout | -0.43% | -0.93% | -0.21 |
| 2026-10-02 07:30 | ruptura_estricta | DASH | timeout | -0.80% | -1.30% | -0.29 |
| 2026-10-02 07:30 | ruptura_estricta | CRV | timeout | -1.00% | -1.50% | -0.33 |
| 2026-10-02 07:30 | ruptura_estricta | HYPE | timeout | +0.05% | -0.45% | -0.10 |
| 2026-10-02 07:30 | macd_momentum | ASTER | momentum perdido | -0.76% | -1.26% | -0.27 |
| 2026-10-02 07:30 | macd_momentum | PUMP | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 07:30 | pullback_tendencia | ETH | rotura de tendencia | -0.12% | -0.62% | -0.14 |
| 2026-10-02 07:25 | ruptura_volumen_evento | LTC | timeout | -0.16% | -0.66% | -0.14 |

## Eventos de la última vuelta

- 2026-10-02 07:30 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto -0.12% neto -0.62%
- 2026-10-02 07:30 [macd_momentum] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 07:30 [macd_sin_salida] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 07:30 [macd_momentum_regimen] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 07:30 [macd_momentum_evento] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 07:30 [ruptura_estricta] CIERRE HYPE timeout bruto +0.05% neto -0.45%
- 2026-10-02 07:30 [ruptura_estricta] CIERRE CRV timeout bruto -1.00% neto -1.50%
- 2026-10-02 07:30 [macd_momentum] CIERRE ASTER momentum perdido bruto -0.76% neto -1.26%
- 2026-10-02 07:30 [macd_momentum_regimen] CIERRE ASTER momentum perdido bruto -0.76% neto -1.26%
- 2026-10-02 07:30 [macd_momentum_evento] CIERRE ASTER momentum perdido bruto -0.76% neto -1.26%
- 2026-10-02 07:30 [ruptura_estricta] CIERRE DASH timeout bruto -0.80% neto -1.30%
- 2026-10-02 07:30 [ruptura_estricta] CIERRE KSM timeout bruto -0.43% neto -0.93%
- 2026-10-02 07:30 [ruptura_estricta] CIERRE TRUMP timeout bruto +0.22% neto -0.28%
- 2026-10-02 07:30 [macd_sin_salida] CIERRE KAS timeout bruto -0.93% neto -1.43%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
