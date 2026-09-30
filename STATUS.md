# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 17:41 UTC · vueltas 65 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.87 € (-1.45%) | 40 | 11 | 32% | -0.239% | -1.316% | -1.478% | -12.16 € |
| reversion_bb | 923.89 € (-0.04%) | 4 | 2 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 899.29 € (-2.70%) | 66 | 6 | 14% | -0.701% | -1.597% | -1.738% | -24.19 € |
| rebote_extremo | 923.90 € (-0.04%) | 2 | 0 | 50% | +0.370% | -0.731% | -0.816% | -0.34 € |
| pullback_tendencia | 907.72 € (-1.79%) | 48 | 4 | 15% | -0.448% | -1.485% | -1.610% | -16.37 € |
| macd_momentum | 911.31 € (-1.40%) | 64 | 3 | 31% | +0.014% | -0.894% | -1.036% | -13.19 € |
| estocastico_rebote | 914.81 € (-1.02%) | 72 | 11 | 47% | +0.288% | -0.575% | -0.725% | -9.61 € |
| ruptura_estricta | 900.17 € (-2.60%) | 42 | 3 | 10% | -1.325% | -2.425% | -2.569% | -23.48 € |
| macd_sin_salida | 907.12 € (-1.85%) | 59 | 5 | 32% | -0.303% | -1.245% | -1.386% | -16.95 € |
| c_banda_atr_tope | 922.34 € (-0.21%) | 10 | 5 | 50% | +0.251% | -0.849% | -1.020% | -1.96 € |
| ruptura_volumen_tope | 918.82 € (-0.59%) | 15 | 1 | 20% | -0.403% | -1.503% | -1.599% | -5.21 € |
| c_banda_atr_regimen | 910.83 € (-1.45%) | 37 | 8 | 30% | -0.326% | -1.426% | -1.584% | -12.18 € |
| macd_momentum_regimen | 911.74 € (-1.35%) | 56 | 2 | 30% | -0.021% | -0.987% | -1.129% | -12.75 € |
| ruptura_volumen_regimen | 899.11 € (-2.72%) | 66 | 6 | 14% | -0.714% | -1.609% | -1.751% | -24.37 € |
| c_banda_atr_evento | 921.26 € (-0.32%) | 7 | 12 | 43% | -0.015% | -1.115% | -1.289% | -1.80 € |
| macd_momentum_evento | 920.09 € (-0.45%) | 17 | 3 | 29% | -0.027% | -1.127% | -1.281% | -4.42 € |
| ruptura_volumen_evento | 915.95 € (-0.90%) | 16 | 6 | 6% | -0.934% | -2.034% | -2.148% | -7.51 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 17:40 | ruptura_volumen_evento | KAS | stop-loss | -1.30% | -2.40% | -0.55 |
| 2026-09-30 17:40 | ruptura_volumen_evento | PEPE | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:40 | ruptura_volumen_evento | XDC | timeout | -0.40% | -1.50% | -0.34 |
| 2026-09-30 17:40 | macd_momentum_evento | WLD | stop-loss | -1.59% | -2.69% | -0.62 |
| 2026-09-30 17:40 | c_banda_atr_evento | WLD | stop-loss | -1.61% | -2.71% | -0.63 |
| 2026-09-30 17:40 | ruptura_volumen_regimen | KAS | stop-loss | -1.30% | -1.80% | -0.41 |
| 2026-09-30 17:40 | ruptura_volumen_regimen | PEPE | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 17:40 | macd_momentum_regimen | WLD | stop-loss | -1.59% | -2.09% | -0.48 |
| 2026-09-30 17:40 | c_banda_atr_regimen | WLD | stop-loss | -1.61% | -2.71% | -0.62 |
| 2026-09-30 17:40 | ruptura_volumen_tope | XDC | timeout | -0.40% | -1.50% | -0.34 |
| 2026-09-30 17:40 | macd_sin_salida | WLD | stop-loss | -1.59% | -2.09% | -0.47 |
| 2026-09-30 17:40 | macd_sin_salida | HBAR | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 17:40 | estocastico_rebote | SHIB | timeout | -0.35% | -0.85% | -0.20 |
| 2026-09-30 17:40 | estocastico_rebote | LTC | timeout | +0.49% | -0.30% | -0.07 |
| 2026-09-30 17:40 | estocastico_rebote | SOL | timeout | +0.39% | -0.41% | -0.09 |

## Eventos de la última vuelta

- 2026-09-30 17:40 [estocastico_rebote] CIERRE BTC timeout bruto +0.58% neto -0.22%
- 2026-09-30 17:40 [estocastico_rebote] CIERRE SOL timeout bruto +0.39% neto -0.41%
- 2026-09-30 17:35 [estocastico_rebote] ENTRADA HBAR @ 0.0942 (22.87 €, apertura)
- 2026-09-30 17:40 [macd_sin_salida] CIERRE HBAR stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:40 [pullback_tendencia] CIERRE ZEC rotura de tendencia bruto -0.81% neto -1.31%
- 2026-09-30 17:35 [pullback_tendencia] ENTRADA HYPE @ 78.7 (22.72 €, apertura)
- 2026-09-30 17:40 [estocastico_rebote] CIERRE LTC timeout bruto +0.49% neto -0.31%
- 2026-09-30 17:40 [pullback_tendencia] CIERRE ONDO rotura de tendencia bruto -0.45% neto -0.95%
- 2026-09-30 17:40 [c_banda_atr] CIERRE WLD stop-loss bruto -1.61% neto -2.41%
- 2026-09-30 17:40 [macd_momentum] CIERRE WLD stop-loss bruto -1.59% neto -2.09%
- 2026-09-30 17:40 [macd_sin_salida] CIERRE WLD stop-loss bruto -1.59% neto -2.09%
- 2026-09-30 17:40 [c_banda_atr_regimen] CIERRE WLD stop-loss bruto -1.61% neto -2.71%
- 2026-09-30 17:40 [macd_momentum_regimen] CIERRE WLD stop-loss bruto -1.59% neto -2.09%
- 2026-09-30 17:40 [c_banda_atr_evento] CIERRE WLD stop-loss bruto -1.61% neto -2.71%
- 2026-09-30 17:40 [macd_momentum_evento] CIERRE WLD stop-loss bruto -1.59% neto -2.69%
- 2026-09-30 17:40 [ruptura_volumen] CIERRE XDC timeout bruto -0.39% neto -0.89%
- 2026-09-30 17:35 [macd_momentum] ENTRADA XDC @ 0.03027 (22.78 €, apertura)
- 2026-09-30 17:35 [macd_sin_salida] ENTRADA XDC @ 0.03027 (22.68 €, apertura)
- 2026-09-30 17:40 [ruptura_volumen_tope] CIERRE XDC timeout bruto -0.39% neto -1.49%
- 2026-09-30 17:35 [macd_momentum_regimen] ENTRADA XDC @ 0.03027 (22.79 €, apertura)
- 2026-09-30 17:35 [macd_momentum_evento] ENTRADA XDC @ 0.03027 (23.00 €, apertura)
- 2026-09-30 17:40 [ruptura_volumen_evento] CIERRE XDC timeout bruto -0.39% neto -1.49%
- 2026-09-30 17:40 [ruptura_volumen] CIERRE PEPE stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:40 [ruptura_volumen_regimen] CIERRE PEPE stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:40 [ruptura_volumen_evento] CIERRE PEPE stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:40 [estocastico_rebote] CIERRE SHIB timeout bruto -0.35% neto -0.85%
- 2026-09-30 17:40 [pullback_tendencia] CIERRE KSM rotura de tendencia bruto -1.30% neto -2.10%
- 2026-09-30 17:35 [estocastico_rebote] ENTRADA TRUMP @ 1.806 (22.87 €, apertura)
- 2026-09-30 17:40 [pullback_tendencia] CIERRE BNB rotura de tendencia bruto -0.30% neto -1.10%
- 2026-09-30 17:40 [pullback_tendencia] CIERRE TON rotura de tendencia bruto +0.30% neto -0.50%
- 2026-09-30 17:40 [ruptura_volumen] CIERRE KAS stop-loss bruto -1.30% neto -1.80%
- 2026-09-30 17:40 [ruptura_volumen_regimen] CIERRE KAS stop-loss bruto -1.30% neto -1.80%
- 2026-09-30 17:40 [ruptura_volumen_evento] CIERRE KAS stop-loss bruto -1.30% neto -2.40%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
