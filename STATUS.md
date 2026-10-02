# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 08:01 UTC · vueltas 385 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.66 € (-3.63%) | 333 | 23 | 39% | +0.124% | -0.454% | -0.575% | -34.48 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 863.16 € (-6.61%) | 414 | 6 | 27% | -0.102% | -0.665% | -0.774% | -61.70 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.93 € (-3.71%) | 237 | 7 | 20% | -0.036% | -0.647% | -0.733% | -34.84 € |
| macd_momentum | 854.78 € (-7.52%) | 645 | 19 | 22% | +0.046% | -0.494% | -0.596% | -70.98 € |
| estocastico_rebote | 880.83 € (-4.70%) | 387 | 40 | 36% | +0.043% | -0.524% | -0.633% | -45.99 € |
| ruptura_estricta | 882.53 € (-4.51%) | 233 | 4 | 32% | -0.174% | -0.787% | -0.903% | -41.73 € |
| macd_sin_salida | 881.04 € (-4.67%) | 432 | 27 | 40% | +0.113% | -0.447% | -0.558% | -44.02 € |
| c_banda_atr_tope | 913.42 € (-1.17%) | 76 | 5 | 37% | +0.213% | -0.634% | -0.750% | -11.08 € |
| ruptura_volumen_tope | 901.44 € (-2.47%) | 127 | 5 | 24% | -0.087% | -0.795% | -0.908% | -23.06 € |
| c_banda_atr_regimen | 903.11 € (-2.29%) | 185 | 23 | 40% | +0.131% | -0.510% | -0.640% | -21.73 € |
| macd_momentum_regimen | 877.66 € (-5.04%) | 408 | 19 | 22% | +0.041% | -0.523% | -0.626% | -48.11 € |
| ruptura_volumen_regimen | 867.85 € (-6.10%) | 337 | 6 | 24% | -0.175% | -0.753% | -0.867% | -57.02 € |
| c_banda_atr_evento | 896.58 € (-2.99%) | 300 | 23 | 40% | +0.172% | -0.416% | -0.533% | -28.56 € |
| macd_momentum_evento | 859.51 € (-7.00%) | 598 | 19 | 21% | +0.048% | -0.497% | -0.595% | -66.25 € |
| ruptura_volumen_evento | 875.44 € (-5.28%) | 364 | 6 | 28% | -0.030% | -0.603% | -0.706% | -49.42 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 08:00 | ruptura_volumen_evento | NIGHT | take-profit | +4.16% | +3.66% | +0.80 |
| 2026-10-02 08:00 | ruptura_volumen_regimen | NIGHT | take-profit | +4.16% | +3.66% | +0.79 |
| 2026-10-02 08:00 | ruptura_estricta | MINA | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-02 08:00 | ruptura_estricta | NIGHT | take-profit | +4.16% | +3.66% | +0.81 |
| 2026-10-02 08:00 | ruptura_volumen | NIGHT | take-profit | +4.16% | +3.66% | +0.79 |
| 2026-10-02 07:55 | ruptura_volumen_evento | VVV | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-02 07:55 | ruptura_volumen_evento | PUMP | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:55 | ruptura_volumen_regimen | VVV | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-02 07:55 | ruptura_volumen_regimen | PUMP | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:55 | ruptura_volumen_tope | PUMP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 07:55 | estocastico_rebote | OP | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 07:55 | ruptura_volumen | VVV | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-02 07:55 | ruptura_volumen | PUMP | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:50 | ruptura_volumen_evento | MINA | take-profit | +2.56% | +2.06% | +0.45 |
| 2026-10-02 07:50 | ruptura_volumen_regimen | MINA | take-profit | +2.56% | +2.06% | +0.45 |

## Eventos de la última vuelta

- 2026-10-02 07:55 [macd_momentum] ENTRADA ETH @ 2427.68 (21.33 €, apertura)
- 2026-10-02 07:55 [macd_sin_salida] ENTRADA ETH @ 2427.68 (22.01 €, apertura)
- 2026-10-02 07:55 [macd_momentum_regimen] ENTRADA ETH @ 2427.68 (21.90 €, apertura)
- 2026-10-02 07:55 [macd_momentum_evento] ENTRADA ETH @ 2427.68 (21.45 €, apertura)
- 2026-10-02 07:55 [macd_momentum] ENTRADA XLM @ 0.197963 (21.33 €, apertura)
- 2026-10-02 07:55 [macd_sin_salida] ENTRADA XLM @ 0.197963 (22.01 €, apertura)
- 2026-10-02 07:55 [macd_momentum_regimen] ENTRADA XLM @ 0.197963 (21.90 €, apertura)
- 2026-10-02 07:55 [macd_momentum_evento] ENTRADA XLM @ 0.197963 (21.45 €, apertura)
- 2026-10-02 07:55 [macd_momentum] ENTRADA TAO @ 275.563 (21.33 €, apertura)
- 2026-10-02 07:55 [macd_sin_salida] ENTRADA TAO @ 275.563 (22.01 €, apertura)
- 2026-10-02 07:55 [macd_momentum_regimen] ENTRADA TAO @ 275.563 (21.90 €, apertura)
- 2026-10-02 07:55 [macd_momentum_evento] ENTRADA TAO @ 275.563 (21.45 €, apertura)
- 2026-10-02 07:55 [macd_momentum] ENTRADA DOGE @ 0.08564 (21.33 €, apertura)
- 2026-10-02 07:55 [macd_sin_salida] ENTRADA DOGE @ 0.08564 (22.01 €, apertura)
- 2026-10-02 07:55 [macd_momentum_regimen] ENTRADA DOGE @ 0.08564 (21.90 €, apertura)
- 2026-10-02 07:55 [macd_momentum_evento] ENTRADA DOGE @ 0.08564 (21.45 €, apertura)
- 2026-10-02 07:55 [macd_momentum] ENTRADA DOT @ 1.0911 (21.33 €, apertura)
- 2026-10-02 07:55 [macd_sin_salida] ENTRADA DOT @ 1.0911 (22.01 €, apertura)
- 2026-10-02 07:55 [macd_momentum_regimen] ENTRADA DOT @ 1.0911 (21.90 €, apertura)
- 2026-10-02 07:55 [macd_momentum_evento] ENTRADA DOT @ 1.0911 (21.45 €, apertura)
- 2026-10-02 07:55 [c_banda_atr] ENTRADA ENA @ 0.2207 (22.24 €, apertura)
- 2026-10-02 07:55 [c_banda_atr_regimen] ENTRADA ENA @ 0.2207 (22.56 €, apertura)
- 2026-10-02 07:55 [c_banda_atr_evento] ENTRADA ENA @ 0.2207 (22.39 €, apertura)
- 2026-10-02 07:55 [c_banda_atr] ENTRADA ICP @ 2.942 (22.24 €, apertura)
- 2026-10-02 07:55 [c_banda_atr_regimen] ENTRADA ICP @ 2.942 (22.56 €, apertura)
- 2026-10-02 07:55 [c_banda_atr_evento] ENTRADA ICP @ 2.942 (22.39 €, apertura)
- 2026-10-02 07:55 [ruptura_volumen] ENTRADA POL @ 0.09842 (21.54 €, apertura)
- 2026-10-02 07:55 [ruptura_volumen_tope] ENTRADA POL @ 0.09842 (22.53 €, apertura)
- 2026-10-02 07:55 [ruptura_volumen_regimen] ENTRADA POL @ 0.09842 (21.66 €, apertura)
- 2026-10-02 07:55 [ruptura_volumen_evento] ENTRADA POL @ 0.09842 (21.85 €, apertura)
- 2026-10-02 08:00 [ruptura_volumen] CIERRE NIGHT take-profit bruto +4.16% neto +3.66%
- 2026-10-02 08:00 [ruptura_estricta] CIERRE NIGHT take-profit bruto +4.16% neto +3.66%
- 2026-10-02 08:00 [ruptura_volumen_regimen] CIERRE NIGHT take-profit bruto +4.16% neto +3.66%
- 2026-10-02 08:00 [ruptura_volumen_evento] CIERRE NIGHT take-profit bruto +4.16% neto +3.66%
- 2026-10-02 07:55 [c_banda_atr] ENTRADA JUP @ 0.29574 (22.24 €, apertura)
- 2026-10-02 07:55 [c_banda_atr_regimen] ENTRADA JUP @ 0.29574 (22.56 €, apertura)
- 2026-10-02 07:55 [c_banda_atr_evento] ENTRADA JUP @ 0.29574 (22.39 €, apertura)
- 2026-10-02 07:55 [ruptura_estricta] ENTRADA OP @ 0.1194 (22.08 €, apertura)
- 2026-10-02 08:00 [ruptura_estricta] CIERRE MINA stop-loss bruto -2.00% neto -2.50%
- 2026-10-02 07:55 [macd_momentum] ENTRADA TRUMP @ 1.868 (21.33 €, apertura)
- 2026-10-02 07:55 [macd_sin_salida] ENTRADA TRUMP @ 1.868 (22.01 €, apertura)
- 2026-10-02 07:55 [macd_momentum_regimen] ENTRADA TRUMP @ 1.868 (21.90 €, apertura)
- 2026-10-02 07:55 [macd_momentum_evento] ENTRADA TRUMP @ 1.868 (21.45 €, apertura)
- 2026-10-02 07:55 [macd_momentum] ENTRADA SPX @ 0.4017 (21.33 €, apertura)
- 2026-10-02 07:55 [macd_sin_salida] ENTRADA SPX @ 0.4017 (22.01 €, apertura)
- 2026-10-02 07:55 [macd_momentum_regimen] ENTRADA SPX @ 0.4017 (21.90 €, apertura)
- 2026-10-02 07:55 [macd_momentum_evento] ENTRADA SPX @ 0.4017 (21.45 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
