# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 05:11 UTC · vueltas 397 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.59 € (-3.53%) | 321 | 14 | 39% | +0.118% | -0.464% | -0.584% | -33.95 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.382% | -4.66 € |
| ruptura_volumen | 870.61 € (-5.80%) | 367 | 37 | 27% | -0.100% | -0.671% | -0.779% | -55.40 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 892.23 € (-3.46%) | 209 | 8 | 19% | -0.078% | -0.704% | -0.792% | -33.46 € |
| macd_momentum | 862.27 € (-6.71%) | 584 | 36 | 23% | +0.058% | -0.487% | -0.588% | -63.55 € |
| estocastico_rebote | 879.21 € (-4.87%) | 372 | 10 | 35% | +0.021% | -0.549% | -0.658% | -46.28 € |
| ruptura_estricta | 889.53 € (-3.76%) | 196 | 35 | 32% | -0.207% | -0.841% | -0.956% | -37.64 € |
| macd_sin_salida | 883.21 € (-4.44%) | 409 | 19 | 40% | +0.111% | -0.453% | -0.563% | -42.26 € |
| c_banda_atr_tope | 912.86 € (-1.23%) | 71 | 4 | 34% | +0.148% | -0.724% | -0.833% | -11.81 € |
| ruptura_volumen_tope | 903.63 € (-2.23%) | 117 | 5 | 26% | -0.045% | -0.771% | -0.885% | -20.64 € |
| c_banda_atr_regimen | 904.21 € (-2.17%) | 174 | 13 | 40% | +0.127% | -0.523% | -0.651% | -20.97 € |
| macd_momentum_regimen | 885.35 € (-4.21%) | 347 | 36 | 22% | +0.060% | -0.515% | -0.619% | -40.49 € |
| ruptura_volumen_regimen | 875.33 € (-5.29%) | 290 | 37 | 24% | -0.184% | -0.774% | -0.887% | -50.68 € |
| c_banda_atr_evento | 897.53 € (-2.89%) | 288 | 14 | 40% | +0.166% | -0.425% | -0.541% | -28.02 € |
| macd_momentum_evento | 867.04 € (-6.19%) | 537 | 36 | 22% | +0.061% | -0.489% | -0.587% | -58.79 € |
| ruptura_volumen_evento | 882.99 € (-4.46%) | 317 | 37 | 28% | -0.017% | -0.600% | -0.702% | -43.03 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 05:10 | ruptura_volumen_evento | USELESS | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 05:10 | ruptura_volumen_evento | ONDO | timeout | +1.70% | +1.20% | +0.26 |
| 2026-10-02 05:10 | ruptura_volumen_evento | ZRO | take-profit | +2.51% | +2.01% | +0.44 |
| 2026-10-02 05:10 | ruptura_volumen_regimen | USELESS | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 05:10 | ruptura_volumen_regimen | ONDO | timeout | +1.70% | +1.20% | +0.26 |
| 2026-10-02 05:10 | ruptura_volumen_regimen | ZRO | take-profit | +2.51% | +2.01% | +0.44 |
| 2026-10-02 05:10 | macd_sin_salida | SPX | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-02 05:10 | macd_sin_salida | TON | timeout | +0.14% | -0.36% | -0.08 |
| 2026-10-02 05:10 | ruptura_estricta | SPX | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-02 05:10 | ruptura_estricta | SEI | timeout | +1.25% | +0.75% | +0.17 |
| 2026-10-02 05:10 | ruptura_estricta | SHIB | timeout | +1.30% | +0.80% | +0.18 |
| 2026-10-02 05:10 | ruptura_estricta | POL | timeout | +1.40% | +0.90% | +0.20 |
| 2026-10-02 05:10 | ruptura_estricta | TAO | timeout | +1.27% | +0.77% | +0.17 |
| 2026-10-02 05:10 | ruptura_volumen | USELESS | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 05:10 | ruptura_volumen | ONDO | timeout | +1.70% | +1.20% | +0.26 |

## Eventos de la última vuelta

- 2026-10-02 05:10 [ruptura_estricta] CIERRE TAO timeout bruto +1.27% neto +0.77%
- 2026-10-02 05:10 [ruptura_volumen] CIERRE ZRO take-profit bruto +2.51% neto +2.01%
- 2026-10-02 05:10 [ruptura_volumen_regimen] CIERRE ZRO take-profit bruto +2.51% neto +2.01%
- 2026-10-02 05:10 [ruptura_volumen_evento] CIERRE ZRO take-profit bruto +2.51% neto +2.01%
- 2026-10-02 05:10 [ruptura_estricta] CIERRE POL timeout bruto +1.40% neto +0.90%
- 2026-10-02 05:10 [ruptura_volumen] CIERRE ONDO timeout bruto +1.70% neto +1.20%
- 2026-10-02 05:10 [ruptura_volumen_regimen] CIERRE ONDO timeout bruto +1.70% neto +1.20%
- 2026-10-02 05:10 [ruptura_volumen_evento] CIERRE ONDO timeout bruto +1.70% neto +1.20%
- 2026-10-02 05:05 [ruptura_volumen] ENTRADA NIGHT @ 0.03581 (21.71 €, apertura)
- 2026-10-02 05:05 [ruptura_estricta] ENTRADA NIGHT @ 0.03581 (22.15 €, apertura)
- 2026-10-02 05:05 [ruptura_volumen_regimen] ENTRADA NIGHT @ 0.03581 (21.83 €, apertura)
- 2026-10-02 05:05 [ruptura_volumen_evento] ENTRADA NIGHT @ 0.03581 (22.02 €, apertura)
- 2026-10-02 05:10 [ruptura_volumen] CIERRE USELESS take-profit bruto +2.50% neto +2.00%
- 2026-10-02 05:10 [ruptura_volumen_regimen] CIERRE USELESS take-profit bruto +2.50% neto +2.00%
- 2026-10-02 05:10 [ruptura_volumen_evento] CIERRE USELESS take-profit bruto +2.50% neto +2.00%
- 2026-10-02 05:10 [ruptura_estricta] CIERRE SHIB timeout bruto +1.30% neto +0.80%
- 2026-10-02 05:10 [macd_sin_salida] CIERRE TON timeout bruto +0.14% neto -0.36%
- 2026-10-02 05:05 [ruptura_volumen] ENTRADA SEI @ 0.06392 (21.72 €, apertura)
- 2026-10-02 05:10 [ruptura_estricta] CIERRE SEI timeout bruto +1.25% neto +0.75%
- 2026-10-02 05:05 [ruptura_volumen_regimen] ENTRADA SEI @ 0.06392 (21.84 €, apertura)
- 2026-10-02 05:05 [ruptura_volumen_evento] ENTRADA SEI @ 0.06392 (22.03 €, apertura)
- 2026-10-02 05:10 [ruptura_estricta] CIERRE SPX timeout bruto +0.91% neto +0.41%
- 2026-10-02 05:10 [macd_sin_salida] CIERRE SPX timeout bruto +0.91% neto +0.41%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
