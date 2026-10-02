# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 12:01 UTC · vueltas 393 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.04 € (-3.92%) | 361 | 15 | 41% | +0.152% | -0.420% | -0.539% | -34.58 € |
| reversion_bb | 919.63 € (-0.50%) | 73 | 1 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 854.75 € (-7.52%) | 455 | 9 | 26% | -0.122% | -0.680% | -0.787% | -68.99 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 888.19 € (-3.90%) | 263 | 8 | 21% | -0.006% | -0.606% | -0.692% | -36.20 € |
| macd_momentum | 847.07 € (-8.35%) | 739 | 8 | 24% | +0.062% | -0.473% | -0.571% | -77.53 € |
| estocastico_rebote | 877.47 € (-5.06%) | 438 | 35 | 38% | +0.116% | -0.444% | -0.551% | -44.12 € |
| ruptura_estricta | 880.12 € (-4.77%) | 247 | 10 | 32% | -0.164% | -0.771% | -0.886% | -43.27 € |
| macd_sin_salida | 875.58 € (-5.27%) | 480 | 25 | 39% | +0.116% | -0.439% | -0.546% | -47.82 € |
| c_banda_atr_tope | 912.78 € (-1.24%) | 82 | 5 | 38% | +0.248% | -0.574% | -0.689% | -10.83 € |
| ruptura_volumen_tope | 898.16 € (-2.82%) | 139 | 1 | 22% | -0.129% | -0.819% | -0.932% | -25.96 € |
| c_banda_atr_regimen | 900.54 € (-2.56%) | 213 | 16 | 42% | +0.176% | -0.447% | -0.572% | -21.90 € |
| macd_momentum_regimen | 869.75 € (-5.90%) | 502 | 8 | 24% | +0.066% | -0.486% | -0.584% | -54.83 € |
| ruptura_volumen_regimen | 859.39 € (-7.02%) | 378 | 9 | 23% | -0.192% | -0.761% | -0.872% | -64.36 € |
| c_banda_atr_evento | 893.95 € (-3.28%) | 328 | 15 | 42% | +0.199% | -0.382% | -0.497% | -28.66 € |
| macd_momentum_evento | 851.76 € (-7.84%) | 692 | 8 | 23% | +0.065% | -0.474% | -0.569% | -72.83 € |
| ruptura_volumen_evento | 866.91 € (-6.20%) | 405 | 9 | 26% | -0.060% | -0.625% | -0.727% | -56.82 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 12:00 | ruptura_volumen_evento | QNT | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 12:00 | macd_momentum_evento | SKY | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 12:00 | macd_momentum_evento | TRX | momentum perdido | +0.11% | -0.39% | -0.08 |
| 2026-10-02 12:00 | ruptura_volumen_regimen | QNT | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 12:00 | macd_momentum_regimen | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 12:00 | macd_momentum_regimen | TRX | momentum perdido | +0.11% | -0.39% | -0.08 |
| 2026-10-02 12:00 | ruptura_volumen_tope | QNT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 12:00 | macd_sin_salida | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 12:00 | macd_momentum | SKY | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 12:00 | macd_momentum | TRX | momentum perdido | +0.11% | -0.39% | -0.08 |
| 2026-10-02 12:00 | pullback_tendencia | ONDO | rotura de tendencia | -0.35% | -0.85% | -0.19 |
| 2026-10-02 12:00 | pullback_tendencia | DOGE | rotura de tendencia | -0.28% | -0.78% | -0.17 |
| 2026-10-02 12:00 | pullback_tendencia | AAVE | rotura de tendencia | -0.70% | -1.20% | -0.27 |
| 2026-10-02 12:00 | pullback_tendencia | AVAX | rotura de tendencia | +0.47% | -0.03% | -0.01 |
| 2026-10-02 12:00 | ruptura_volumen | QNT | stop-loss | -1.20% | -1.70% | -0.36 |

## Eventos de la última vuelta

- 2026-10-02 11:55 [macd_momentum] ENTRADA ETH @ 2447.87 (21.16 €, apertura)
- 2026-10-02 11:55 [macd_momentum_regimen] ENTRADA ETH @ 2447.87 (21.73 €, apertura)
- 2026-10-02 11:55 [macd_momentum_evento] ENTRADA ETH @ 2447.87 (21.28 €, apertura)
- 2026-10-02 12:00 [ruptura_volumen] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 12:00 [ruptura_volumen_tope] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 12:00 [ruptura_volumen_regimen] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 12:00 [ruptura_volumen_evento] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 11:55 [estocastico_rebote] ENTRADA ADA @ 0.227471 (22.00 €, apertura)
- 2026-10-02 12:00 [pullback_tendencia] CIERRE AVAX rotura de tendencia bruto +0.47% neto -0.03%
- 2026-10-02 12:00 [pullback_tendencia] CIERRE AAVE rotura de tendencia bruto -0.70% neto -1.20%
- 2026-10-02 12:00 [pullback_tendencia] CIERRE DOGE rotura de tendencia bruto -0.28% neto -0.78%
- 2026-10-02 12:00 [macd_momentum] CIERRE TRX momentum perdido bruto +0.11% neto -0.39%
- 2026-10-02 12:00 [macd_momentum_regimen] CIERRE TRX momentum perdido bruto +0.11% neto -0.39%
- 2026-10-02 12:00 [macd_momentum_evento] CIERRE TRX momentum perdido bruto +0.11% neto -0.39%
- 2026-10-02 12:00 [pullback_tendencia] CIERRE ONDO rotura de tendencia bruto -0.35% neto -0.85%
- 2026-10-02 12:00 [macd_momentum] CIERRE SKY take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:00 [macd_sin_salida] CIERRE SKY take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:00 [macd_momentum_regimen] CIERRE SKY take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:00 [macd_momentum_evento] CIERRE SKY take-profit bruto +2.00% neto +1.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
