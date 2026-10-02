# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 07:26 UTC · vueltas 378 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.24 € (-3.89%) | 332 | 16 | 39% | +0.129% | -0.450% | -0.571% | -34.03 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 862.73 € (-6.66%) | 407 | 8 | 27% | -0.116% | -0.680% | -0.787% | -61.99 € |
| rebote_extremo | 922.17 € (-0.22%) | 14 | 1 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.54 € (-3.75%) | 234 | 9 | 21% | -0.030% | -0.643% | -0.730% | -34.20 € |
| macd_momentum | 853.60 € (-7.64%) | 643 | 5 | 22% | +0.044% | -0.496% | -0.598% | -71.03 € |
| estocastico_rebote | 876.42 € (-5.17%) | 385 | 32 | 36% | +0.042% | -0.525% | -0.634% | -45.83 € |
| ruptura_estricta | 882.69 € (-4.50%) | 224 | 12 | 33% | -0.177% | -0.795% | -0.908% | -40.55 € |
| macd_sin_salida | 878.89 € (-4.91%) | 430 | 18 | 40% | +0.111% | -0.450% | -0.560% | -44.04 € |
| c_banda_atr_tope | 913.11 € (-1.20%) | 75 | 4 | 37% | +0.236% | -0.616% | -0.732% | -10.63 € |
| ruptura_volumen_tope | 902.01 € (-2.41%) | 123 | 4 | 25% | -0.067% | -0.782% | -0.894% | -21.99 € |
| c_banda_atr_regimen | 900.77 € (-2.54%) | 184 | 17 | 40% | +0.140% | -0.502% | -0.632% | -21.28 € |
| macd_momentum_regimen | 876.46 € (-5.17%) | 406 | 5 | 22% | +0.038% | -0.526% | -0.629% | -48.16 € |
| ruptura_volumen_regimen | 867.41 € (-6.15%) | 330 | 8 | 24% | -0.194% | -0.773% | -0.885% | -57.31 € |
| c_banda_atr_evento | 894.15 € (-3.26%) | 299 | 16 | 40% | +0.177% | -0.411% | -0.528% | -28.11 € |
| macd_momentum_evento | 858.33 € (-7.13%) | 596 | 5 | 21% | +0.046% | -0.499% | -0.597% | -66.30 € |
| ruptura_volumen_evento | 875.00 € (-5.33%) | 357 | 8 | 27% | -0.044% | -0.618% | -0.719% | -49.72 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 07:25 | ruptura_volumen_evento | LTC | timeout | -0.16% | -0.66% | -0.14 |
| 2026-10-02 07:25 | macd_momentum_evento | INJ | momentum perdido | -0.47% | -0.96% | -0.21 |
| 2026-10-02 07:25 | macd_momentum_evento | AAVE | momentum perdido | +0.09% | -0.41% | -0.09 |
| 2026-10-02 07:25 | macd_momentum_evento | ETH | momentum perdido | -0.17% | -0.68% | -0.14 |
| 2026-10-02 07:25 | ruptura_volumen_regimen | LTC | timeout | -0.16% | -0.66% | -0.14 |
| 2026-10-02 07:25 | macd_momentum_regimen | INJ | momentum perdido | -0.47% | -0.96% | -0.21 |
| 2026-10-02 07:25 | macd_momentum_regimen | AAVE | momentum perdido | +0.09% | -0.41% | -0.09 |
| 2026-10-02 07:25 | macd_momentum_regimen | ETH | momentum perdido | -0.17% | -0.68% | -0.15 |
| 2026-10-02 07:25 | ruptura_volumen_tope | LTC | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-02 07:25 | macd_sin_salida | SEI | timeout | -0.55% | -1.05% | -0.23 |
| 2026-10-02 07:25 | macd_sin_salida | SKY | timeout | -0.71% | -1.21% | -0.27 |
| 2026-10-02 07:25 | macd_sin_salida | POL | timeout | -0.64% | -1.14% | -0.25 |
| 2026-10-02 07:25 | macd_sin_salida | TRX | timeout | -0.39% | -0.89% | -0.20 |
| 2026-10-02 07:25 | macd_sin_salida | ICP | timeout | -0.99% | -1.49% | -0.33 |
| 2026-10-02 07:25 | macd_sin_salida | ENA | timeout | +0.50% | +0.00% | +0.00 |

## Eventos de la última vuelta

- 2026-10-02 07:25 [macd_momentum] CIERRE ETH momentum perdido bruto -0.18% neto -0.68%
- 2026-10-02 07:25 [macd_sin_salida] CIERRE ETH timeout bruto -0.36% neto -0.86%
- 2026-10-02 07:25 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto -0.18% neto -0.68%
- 2026-10-02 07:25 [macd_momentum_evento] CIERRE ETH momentum perdido bruto -0.18% neto -0.68%
- 2026-10-02 07:25 [ruptura_estricta] CIERRE SOL timeout bruto -0.66% neto -1.16%
- 2026-10-02 07:25 [macd_sin_salida] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 07:25 [ruptura_estricta] CIERRE LINK timeout bruto -1.62% neto -2.12%
- 2026-10-02 07:25 [ruptura_estricta] CIERRE ADA timeout bruto +0.06% neto -0.44%
- 2026-10-02 07:25 [ruptura_estricta] CIERRE SUI timeout bruto -1.93% neto -2.43%
- 2026-10-02 07:20 [pullback_tendencia] ENTRADA AAVE @ 163.91 (22.27 €, apertura)
- 2026-10-02 07:25 [macd_momentum] CIERRE AAVE momentum perdido bruto +0.09% neto -0.41%
- 2026-10-02 07:25 [macd_momentum_regimen] CIERRE AAVE momentum perdido bruto +0.09% neto -0.41%
- 2026-10-02 07:25 [macd_momentum_evento] CIERRE AAVE momentum perdido bruto +0.09% neto -0.41%
- 2026-10-02 07:20 [estocastico_rebote] ENTRADA ZEC @ 1221.78 (21.97 €, apertura)
- 2026-10-02 07:20 [macd_momentum] ENTRADA PUMP @ 0.005283 (21.34 €, apertura)
- 2026-10-02 07:20 [macd_momentum_regimen] ENTRADA PUMP @ 0.005283 (21.91 €, apertura)
- 2026-10-02 07:20 [macd_momentum_evento] ENTRADA PUMP @ 0.005283 (21.45 €, apertura)
- 2026-10-02 07:25 [pullback_tendencia] CIERRE TAO rotura de tendencia bruto -0.86% neto -1.36%
- 2026-10-02 07:25 [macd_sin_salida] CIERRE TAO timeout bruto -1.02% neto -1.52%
- 2026-10-02 07:25 [ruptura_estricta] CIERRE UNI timeout bruto -0.78% neto -1.28%
- 2026-10-02 07:25 [ruptura_volumen] CIERRE LTC timeout bruto -0.16% neto -0.66%
- 2026-10-02 07:25 [macd_sin_salida] CIERRE LTC timeout bruto +0.78% neto +0.28%
- 2026-10-02 07:25 [ruptura_volumen_tope] CIERRE LTC timeout bruto -0.16% neto -0.66%
- 2026-10-02 07:25 [ruptura_volumen_regimen] CIERRE LTC timeout bruto -0.16% neto -0.66%
- 2026-10-02 07:25 [ruptura_volumen_evento] CIERRE LTC timeout bruto -0.16% neto -0.66%
- 2026-10-02 07:25 [pullback_tendencia] CIERRE DOGE rotura de tendencia bruto -0.49% neto -0.99%
- 2026-10-02 07:25 [ruptura_estricta] CIERRE DOGE timeout bruto -0.46% neto -0.96%
- 2026-10-02 07:25 [macd_sin_salida] CIERRE DOT timeout bruto -0.51% neto -1.01%
- 2026-10-02 07:25 [ruptura_estricta] CIERRE ENA timeout bruto +0.50% neto +0.00%
- 2026-10-02 07:25 [macd_sin_salida] CIERRE ENA timeout bruto +0.50% neto +0.00%
- 2026-10-02 07:25 [macd_sin_salida] CIERRE ICP timeout bruto -0.99% neto -1.49%
- 2026-10-02 07:25 [macd_sin_salida] CIERRE TRX timeout bruto -0.39% neto -0.89%
- 2026-10-02 07:25 [pullback_tendencia] CIERRE POL rotura de tendencia bruto -0.12% neto -0.62%
- 2026-10-02 07:25 [macd_sin_salida] CIERRE POL timeout bruto -0.64% neto -1.14%
- 2026-10-02 07:25 [ruptura_estricta] CIERRE ONDO timeout bruto -0.62% neto -1.12%
- 2026-10-02 07:25 [ruptura_estricta] CIERRE USELESS stop-loss bruto -2.10% neto -2.60%
- 2026-10-02 07:25 [ruptura_estricta] CIERRE BCH timeout bruto +0.13% neto -0.37%
- 2026-10-02 07:25 [macd_momentum] CIERRE INJ momentum perdido bruto -0.47% neto -0.97%
- 2026-10-02 07:25 [macd_momentum_regimen] CIERRE INJ momentum perdido bruto -0.47% neto -0.97%
- 2026-10-02 07:25 [macd_momentum_evento] CIERRE INJ momentum perdido bruto -0.47% neto -0.97%
- 2026-10-02 07:25 [ruptura_estricta] CIERRE PENGU timeout bruto +0.29% neto -0.21%
- 2026-10-02 07:25 [ruptura_estricta] CIERRE BNB timeout bruto -0.60% neto -1.10%
- 2026-10-02 07:25 [estocastico_rebote] CIERRE KAS timeout bruto -0.90% neto -1.40%
- 2026-10-02 07:25 [macd_sin_salida] CIERRE SKY timeout bruto -0.71% neto -1.21%
- 2026-10-02 07:25 [ruptura_estricta] CIERRE XMR timeout bruto +0.28% neto -0.22%
- 2026-10-02 07:25 [macd_sin_salida] CIERRE SEI timeout bruto -0.55% neto -1.05%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
