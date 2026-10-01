# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 23:58 UTC · vueltas 334 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

**Avisos:** hueco de 77 min entre vueltas

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.73 € (-4.27%) | 267 | 23 | 34% | -0.048% | -0.645% | -0.766% | -39.14 € |
| reversion_bb | 917.76 € (-0.70%) | 52 | 16 | 50% | +0.317% | -0.685% | -0.782% | -8.21 € |
| ruptura_volumen | 871.82 € (-5.67%) | 297 | 5 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.05 € (-3.81%) | 187 | 5 | 15% | -0.194% | -0.836% | -0.925% | -35.47 € |
| macd_momentum | 863.11 € (-6.61%) | 489 | 11 | 20% | -0.011% | -0.564% | -0.667% | -61.77 € |
| estocastico_rebote | 872.52 € (-5.60%) | 327 | 14 | 31% | -0.130% | -0.709% | -0.819% | -52.33 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 871.33 € (-5.72%) | 347 | 10 | 34% | -0.103% | -0.678% | -0.790% | -53.17 € |
| c_banda_atr_tope | 911.13 € (-1.42%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.89 € (-1.99%) | 101 | 5 | 27% | -0.042% | -0.803% | -0.919% | -18.58 € |
| c_banda_atr_regimen | 896.11 € (-3.04%) | 135 | 3 | 30% | -0.208% | -0.902% | -1.035% | -27.84 € |
| macd_momentum_regimen | 885.23 € (-4.22%) | 276 | 0 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 874.82 € (-5.35%) | 230 | 0 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 890.62 € (-3.64%) | 234 | 23 | 35% | -0.011% | -0.623% | -0.739% | -33.24 € |
| macd_momentum_evento | 867.90 € (-6.10%) | 442 | 11 | 19% | -0.015% | -0.575% | -0.674% | -57.00 € |
| ruptura_volumen_evento | 884.22 € (-4.33%) | 247 | 5 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 23:55 | macd_momentum_evento | AAVE | momentum perdido | +0.45% | -0.05% | -0.01 |
| 2026-10-01 23:55 | c_banda_atr_evento | TRUMP | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 23:55 | c_banda_atr_evento | FET | timeout | +0.24% | -0.26% | -0.06 |
| 2026-10-01 23:55 | c_banda_atr_evento | TAO | timeout | -0.32% | -0.82% | -0.18 |
| 2026-10-01 23:55 | c_banda_atr_evento | XLM | timeout | -0.22% | -0.72% | -0.16 |
| 2026-10-01 23:55 | c_banda_atr_regimen | TRUMP | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 23:55 | c_banda_atr_regimen | FET | timeout | +0.24% | -0.26% | -0.06 |
| 2026-10-01 23:55 | c_banda_atr_regimen | TAO | timeout | -0.32% | -0.82% | -0.19 |
| 2026-10-01 23:55 | macd_sin_salida | NIGHT | stop-loss | -1.64% | -2.14% | -0.47 |
| 2026-10-01 23:55 | macd_momentum | AAVE | momentum perdido | +0.45% | -0.05% | -0.01 |
| 2026-10-01 23:55 | c_banda_atr | TRUMP | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 23:55 | c_banda_atr | FET | timeout | +0.24% | -0.26% | -0.06 |
| 2026-10-01 23:55 | c_banda_atr | TAO | timeout | -0.32% | -0.82% | -0.18 |
| 2026-10-01 23:55 | c_banda_atr | XLM | timeout | -0.22% | -0.72% | -0.16 |
| 2026-10-01 23:50 | macd_momentum_evento | DASH | momentum perdido | -0.65% | -1.15% | -0.25 |

## Eventos de la última vuelta

- 2026-10-01 22:40 [ruptura_volumen] ENTRADA ETH @ 2402.4 (21.80 €, apertura)
- 2026-10-01 22:40 [ruptura_volumen_tope] ENTRADA ETH @ 2402.4 (22.64 €, apertura)
- 2026-10-01 22:40 [ruptura_volumen_evento] ENTRADA ETH @ 2402.4 (22.11 €, apertura)
- 2026-10-01 22:45 [ruptura_volumen] CIERRE BCH timeout bruto +0.20% neto -0.30%
- 2026-10-01 22:40 [macd_momentum] ENTRADA BCH @ 275.17 (21.60 €, apertura)
- 2026-10-01 22:45 [ruptura_volumen_regimen] CIERRE BCH timeout bruto +0.20% neto -0.30%
- 2026-10-01 22:40 [macd_momentum_evento] ENTRADA BCH @ 275.17 (21.72 €, apertura)
- 2026-10-01 22:45 [ruptura_volumen_evento] CIERRE BCH timeout bruto +0.20% neto -0.30%
- 2026-10-01 22:45 [estocastico_rebote] CIERRE XMR timeout bruto +0.38% neto -0.12%
- 2026-10-01 22:50 [estocastico_rebote] CIERRE LINK timeout bruto -0.97% neto -1.47%
- 2026-10-01 22:50 [macd_sin_salida] CIERRE WLD timeout bruto -0.52% neto -1.02%
- 2026-10-01 22:50 [reversion_bb] CIERRE USELESS stop-loss bruto -1.52% neto -2.02%
- 2026-10-01 22:55 [macd_sin_salida] CIERRE UNI timeout bruto -0.53% neto -1.03%
- 2026-10-01 22:55 [macd_sin_salida] CIERRE ARB timeout bruto -0.84% neto -1.34%
- 2026-10-01 22:55 [estocastico_rebote] CIERRE MINA take-profit bruto +1.89% neto +1.39%
- 2026-10-01 22:55 [ruptura_volumen] CIERRE TON timeout bruto +0.65% neto +0.15%
- 2026-10-01 22:55 [ruptura_volumen_regimen] CIERRE TON timeout bruto +0.65% neto +0.15%
- 2026-10-01 22:55 [ruptura_volumen_evento] CIERRE TON timeout bruto +0.65% neto +0.15%
- 2026-10-01 22:55 [macd_momentum] CIERRE SPX momentum perdido bruto -0.13% neto -0.63%
- 2026-10-01 22:55 [macd_momentum_evento] CIERRE SPX momentum perdido bruto -0.13% neto -0.63%
- 2026-10-01 22:55 [pullback_tendencia] ENTRADA ETH @ 2403.63 (22.22 €, apertura)
- 2026-10-01 22:55 [pullback_tendencia] ENTRADA PUMP @ 0.005178 (22.22 €, apertura)
- 2026-10-01 22:55 [pullback_tendencia] ENTRADA BCH @ 275.21 (22.22 €, apertura)
- 2026-10-01 23:00 [macd_sin_salida] CIERRE BCH timeout bruto +0.47% neto -0.03%
- 2026-10-01 23:00 [c_banda_atr] ENTRADA ZEC @ 1186.41 (22.14 €, apertura)
- 2026-10-01 23:00 [c_banda_atr_evento] ENTRADA ZEC @ 1186.41 (22.29 €, apertura)
- 2026-10-01 23:05 [macd_sin_salida] CIERRE SHIB timeout bruto -1.07% neto -1.57%
- 2026-10-01 23:05 [macd_momentum] CIERRE BNB momentum perdido bruto +0.15% neto -0.35%
- 2026-10-01 23:05 [macd_momentum_regimen] CIERRE BNB momentum perdido bruto +0.15% neto -0.35%
- 2026-10-01 23:05 [macd_momentum_evento] CIERRE BNB momentum perdido bruto +0.15% neto -0.35%
- 2026-10-01 23:05 [ruptura_volumen] CIERRE SKY timeout bruto -0.47% neto -0.97%
- 2026-10-01 23:05 [ruptura_volumen_regimen] CIERRE SKY timeout bruto -0.47% neto -0.97%
- 2026-10-01 23:05 [ruptura_volumen_evento] CIERRE SKY timeout bruto -0.47% neto -0.97%
- 2026-10-01 23:05 [pullback_tendencia] ENTRADA BTC @ 75315.7 (22.22 €, apertura)
- 2026-10-01 23:10 [macd_sin_salida] CIERRE ETH timeout bruto -0.08% neto -0.58%
- 2026-10-01 23:10 [macd_sin_salida] CIERRE SOL timeout bruto -0.19% neto -0.69%
- 2026-10-01 23:10 [macd_sin_salida] CIERRE XLM timeout bruto -0.52% neto -1.02%
- 2026-10-01 23:10 [c_banda_atr] CIERRE LTC timeout bruto +0.15% neto -0.35%
- 2026-10-01 23:05 [estocastico_rebote] ENTRADA LTC @ 60.74 (21.79 €, apertura)
- 2026-10-01 23:10 [c_banda_atr_regimen] CIERRE LTC timeout bruto +0.15% neto -0.35%
- 2026-10-01 23:10 [c_banda_atr_evento] CIERRE LTC timeout bruto +0.15% neto -0.35%
- 2026-10-01 23:10 [estocastico_rebote] CIERRE ZRO take-profit bruto +1.80% neto +1.30%
- 2026-10-01 23:10 [macd_momentum] CIERRE POL momentum perdido bruto -0.27% neto -0.77%
- 2026-10-01 23:10 [macd_momentum_evento] CIERRE POL momentum perdido bruto -0.27% neto -0.77%
- 2026-10-01 23:10 [macd_sin_salida] CIERRE BNB timeout bruto +0.15% neto -0.35%
- 2026-10-01 23:05 [c_banda_atr] ENTRADA TON @ 1.404 (22.14 €, apertura)
- 2026-10-01 23:10 [ruptura_volumen_tope] CIERRE TON timeout bruto +0.07% neto -0.43%
- 2026-10-01 23:05 [c_banda_atr_evento] ENTRADA TON @ 1.404 (22.29 €, apertura)
- 2026-10-01 23:05 [c_banda_atr] ENTRADA KAS @ 0.03681 (22.14 €, apertura)
- 2026-10-01 23:05 [c_banda_atr_evento] ENTRADA KAS @ 0.03681 (22.29 €, apertura)
- 2026-10-01 23:10 [macd_sin_salida] CIERRE APT timeout bruto -1.06% neto -1.56%
- 2026-10-01 23:15 [pullback_tendencia] CIERRE BTC rotura de tendencia bruto -0.06% neto -0.56%
- 2026-10-01 23:15 [macd_momentum] CIERRE UNI momentum perdido bruto -1.01% neto -1.51%
- 2026-10-01 23:15 [macd_momentum_evento] CIERRE UNI momentum perdido bruto -1.01% neto -1.51%
- 2026-10-01 23:15 [macd_sin_salida] CIERRE POL timeout bruto -0.66% neto -1.16%
- 2026-10-01 23:10 [macd_momentum] ENTRADA NIGHT @ 0.03467 (21.58 €, apertura)
- 2026-10-01 23:10 [macd_sin_salida] ENTRADA NIGHT @ 0.03467 (21.80 €, apertura)
- 2026-10-01 23:10 [macd_momentum_evento] ENTRADA NIGHT @ 0.03467 (21.70 €, apertura)
- 2026-10-01 23:10 [estocastico_rebote] ENTRADA SHIB @ 5.127e-06 (21.80 €, apertura)
- 2026-10-01 23:20 [macd_sin_salida] CIERRE ICP timeout bruto -0.58% neto -1.08%
- 2026-10-01 23:20 [macd_momentum] CIERRE TRUMP momentum perdido bruto -0.49% neto -0.99%
- 2026-10-01 23:20 [macd_momentum_evento] CIERRE TRUMP momentum perdido bruto -0.49% neto -0.99%
- 2026-10-01 23:20 [macd_sin_salida] CIERRE XMR timeout bruto +0.06% neto -0.44%
- 2026-10-01 23:25 [macd_sin_salida] CIERRE BTC timeout bruto -0.08% neto -0.58%
- 2026-10-01 23:20 [c_banda_atr] ENTRADA DOT @ 1.0453 (22.14 €, apertura)
- 2026-10-01 23:20 [c_banda_atr_evento] ENTRADA DOT @ 1.0453 (22.29 €, apertura)
- 2026-10-01 23:25 [macd_momentum] CIERRE NIGHT momentum perdido bruto -0.37% neto -0.87%
- 2026-10-01 23:25 [macd_momentum_evento] CIERRE NIGHT momentum perdido bruto -0.37% neto -0.87%
- 2026-10-01 23:25 [macd_momentum] CIERRE BCH momentum perdido bruto -0.12% neto -0.62%
- 2026-10-01 23:25 [macd_momentum_evento] CIERRE BCH momentum perdido bruto -0.12% neto -0.62%
- 2026-10-01 23:25 [estocastico_rebote] ENTRADA SUI @ 1.0417 (21.80 €, apertura)
- 2026-10-01 23:35 [macd_sin_salida] CIERRE FET timeout bruto -0.24% neto -0.74%
- 2026-10-01 23:30 [estocastico_rebote] ENTRADA BNB @ 684.53 (21.80 €, apertura)
- 2026-10-01 23:30 [c_banda_atr] ENTRADA SKY @ 0.07458 (22.14 €, apertura)
- 2026-10-01 23:30 [c_banda_atr_evento] ENTRADA SKY @ 0.07458 (22.29 €, apertura)
- 2026-10-01 23:35 [pullback_tendencia] ENTRADA BTC @ 75390.8 (22.22 €, apertura)
- 2026-10-01 23:35 [ruptura_volumen] ENTRADA LINK @ 12.7622 (21.79 €, apertura)
- 2026-10-01 23:35 [ruptura_volumen_tope] ENTRADA LINK @ 12.7622 (22.64 €, apertura)
- 2026-10-01 23:35 [ruptura_volumen_evento] ENTRADA LINK @ 12.7622 (22.10 €, apertura)
- 2026-10-01 23:40 [estocastico_rebote] CIERRE TRX timeout bruto -0.23% neto -0.73%
- 2026-10-01 23:40 [pullback_tendencia] CIERRE SKY timeout bruto +0.65% neto +0.15%
- 2026-10-01 23:35 [macd_momentum] ENTRADA SKY @ 0.07458 (21.57 €, apertura)
- 2026-10-01 23:35 [macd_momentum_evento] ENTRADA SKY @ 0.07458 (21.69 €, apertura)
- 2026-10-01 23:40 [macd_momentum] ENTRADA SUI @ 1.0434 (21.57 €, apertura)
- 2026-10-01 23:40 [macd_sin_salida] ENTRADA SUI @ 1.0434 (21.79 €, apertura)
- 2026-10-01 23:40 [macd_momentum_evento] ENTRADA SUI @ 1.0434 (21.69 €, apertura)
- 2026-10-01 23:45 [reversion_bb] CIERRE ONDO take-profit bruto +1.50% neto +1.00%
- 2026-10-01 23:40 [ruptura_volumen] ENTRADA ONDO @ 0.43947 (21.79 €, apertura)
- 2026-10-01 23:40 [ruptura_volumen_tope] ENTRADA ONDO @ 0.43947 (22.64 €, apertura)
- 2026-10-01 23:40 [ruptura_volumen_evento] ENTRADA ONDO @ 0.43947 (22.10 €, apertura)
- 2026-10-01 23:45 [c_banda_atr] CIERRE WLD timeout bruto +1.78% neto +1.28%
- 2026-10-01 23:45 [c_banda_atr_evento] CIERRE WLD timeout bruto +1.78% neto +1.28%
- 2026-10-01 23:45 [macd_momentum] CIERRE WLFI momentum perdido bruto +0.40% neto -0.10%
- 2026-10-01 23:45 [macd_momentum_evento] CIERRE WLFI momentum perdido bruto +0.40% neto -0.10%
- 2026-10-01 23:50 [c_banda_atr] CIERRE SUI timeout bruto -0.51% neto -1.01%
- 2026-10-01 23:50 [c_banda_atr_evento] CIERRE SUI timeout bruto -0.51% neto -1.01%
- 2026-10-01 23:50 [macd_momentum] CIERRE DASH momentum perdido bruto -0.65% neto -1.15%
- 2026-10-01 23:50 [macd_momentum_evento] CIERRE DASH momentum perdido bruto -0.65% neto -1.15%
- 2026-10-01 23:45 [macd_momentum] ENTRADA SPX @ 0.3905 (21.56 €, apertura)
- 2026-10-01 23:45 [macd_momentum_evento] ENTRADA SPX @ 0.3905 (21.68 €, apertura)
- 2026-10-01 23:50 [ruptura_volumen] ENTRADA AVAX @ 9.769 (21.79 €, apertura)
- 2026-10-01 23:50 [ruptura_volumen_tope] ENTRADA AVAX @ 9.769 (22.64 €, apertura)
- 2026-10-01 23:50 [ruptura_volumen_evento] ENTRADA AVAX @ 9.769 (22.10 €, apertura)
- 2026-10-01 23:55 [macd_momentum] CIERRE AAVE momentum perdido bruto +0.45% neto -0.05%
- 2026-10-01 23:55 [macd_momentum_evento] CIERRE AAVE momentum perdido bruto +0.45% neto -0.05%
- 2026-10-01 23:55 [c_banda_atr] CIERRE XLM timeout bruto -0.22% neto -0.72%
- 2026-10-01 23:55 [c_banda_atr_evento] CIERRE XLM timeout bruto -0.22% neto -0.72%
- 2026-10-01 23:55 [c_banda_atr] CIERRE TAO timeout bruto -0.32% neto -0.82%
- 2026-10-01 23:55 [c_banda_atr_regimen] CIERRE TAO timeout bruto -0.32% neto -0.82%
- 2026-10-01 23:55 [c_banda_atr_evento] CIERRE TAO timeout bruto -0.32% neto -0.82%
- 2026-10-01 23:55 [c_banda_atr] CIERRE FET timeout bruto +0.24% neto -0.26%
- 2026-10-01 23:55 [c_banda_atr_regimen] CIERRE FET timeout bruto +0.24% neto -0.26%
- 2026-10-01 23:55 [c_banda_atr_evento] CIERRE FET timeout bruto +0.24% neto -0.26%
- 2026-10-01 23:55 [macd_sin_salida] CIERRE NIGHT stop-loss bruto -1.64% neto -2.14%
- 2026-10-01 23:55 [c_banda_atr] CIERRE TRUMP timeout bruto -0.16% neto -0.66%
- 2026-10-01 23:55 [c_banda_atr_regimen] CIERRE TRUMP timeout bruto -0.16% neto -0.66%
- 2026-10-01 23:55 [c_banda_atr_evento] CIERRE TRUMP timeout bruto -0.16% neto -0.66%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
