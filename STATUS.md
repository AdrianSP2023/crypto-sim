# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 14:57 UTC · vueltas 63 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 917.77 € (-0.70%) | 35 | 14 | 46% | +0.303% | -0.797% | -0.949% | -6.44 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 914.18 € (-1.09%) | 57 | 12 | 30% | +0.124% | -0.834% | -0.961% | -10.96 € |
| rebote_extremo | 924.29 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 914.76 € (-1.03%) | 49 | 9 | 33% | +0.150% | -0.871% | -0.982% | -9.83 € |
| macd_momentum | 906.92 € (-1.87%) | 124 | 23 | 23% | +0.076% | -0.634% | -0.752% | -18.08 € |
| estocastico_rebote | 919.42 € (-0.52%) | 60 | 32 | 53% | +0.580% | -0.325% | -0.457% | -4.49 € |
| ruptura_estricta | 917.98 € (-0.68%) | 32 | 9 | 34% | +0.108% | -0.992% | -1.115% | -7.33 € |
| macd_sin_salida | 916.42 € (-0.85%) | 70 | 23 | 41% | +0.389% | -0.484% | -0.613% | -7.79 € |
| c_banda_atr_tope | 920.05 € (-0.45%) | 12 | 4 | 25% | -0.491% | -1.591% | -1.772% | -4.41 € |
| ruptura_volumen_tope | 922.01 € (-0.24%) | 15 | 5 | 20% | +0.300% | -0.800% | -0.920% | -2.77 € |
| c_banda_atr_regimen | 917.77 € (-0.70%) | 35 | 14 | 46% | +0.303% | -0.797% | -0.949% | -6.44 € |
| macd_momentum_regimen | 906.92 € (-1.87%) | 124 | 23 | 23% | +0.076% | -0.634% | -0.752% | -18.08 € |
| ruptura_volumen_regimen | 914.18 € (-1.09%) | 57 | 12 | 30% | +0.124% | -0.834% | -0.961% | -10.96 € |
| c_banda_atr_evento | 924.07 € (-0.02%) | 5 | 12 | 60% | +0.585% | -0.515% | -0.742% | -0.59 € |
| macd_momentum_evento | 925.25 € (+0.11%) | 4 | 23 | 75% | +1.310% | +0.210% | +0.038% | +0.19 € |
| ruptura_volumen_evento | 924.75 € (+0.05%) | 0 | 10 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 14:55 | macd_momentum_evento | AVAX | momentum perdido | -0.76% | -1.86% | -0.43 |
| 2026-09-29 14:55 | c_banda_atr_evento | ENA | stop-loss | -1.53% | -2.63% | -0.61 |
| 2026-09-29 14:55 | ruptura_volumen_regimen | TRUMP | timeout | +1.32% | +0.82% | +0.19 |
| 2026-09-29 14:55 | macd_momentum_regimen | AVAX | momentum perdido | -0.76% | -1.26% | -0.29 |
| 2026-09-29 14:55 | c_banda_atr_regimen | ASTER | timeout | +0.71% | -0.39% | -0.09 |
| 2026-09-29 14:55 | c_banda_atr_regimen | RAY | timeout | +1.07% | -0.03% | -0.01 |
| 2026-09-29 14:55 | c_banda_atr_regimen | ENA | stop-loss | -1.53% | -2.63% | -0.60 |
| 2026-09-29 14:55 | c_banda_atr_tope | ENA | stop-loss | -1.53% | -2.63% | -0.61 |
| 2026-09-29 14:55 | macd_sin_salida | TRX | timeout | -0.06% | -0.86% | -0.20 |
| 2026-09-29 14:55 | ruptura_estricta | POL | stop-loss | -2.12% | -3.22% | -0.74 |
| 2026-09-29 14:55 | ruptura_estricta | PENGU | timeout | +1.39% | +0.28% | +0.07 |
| 2026-09-29 14:55 | ruptura_estricta | SOL | timeout | +0.21% | -0.89% | -0.21 |
| 2026-09-29 14:55 | ruptura_estricta | ETH | timeout | -0.64% | -1.74% | -0.40 |
| 2026-09-29 14:55 | estocastico_rebote | ENA | stop-loss | -1.53% | -2.03% | -0.47 |
| 2026-09-29 14:55 | macd_momentum | AVAX | momentum perdido | -0.76% | -1.26% | -0.29 |

## Eventos de la última vuelta

- 2026-09-29 14:55 [ruptura_estricta] CIERRE ETH timeout bruto -0.64% neto -1.74%
- 2026-09-29 14:55 [ruptura_estricta] CIERRE SOL timeout bruto +0.21% neto -0.89%
- 2026-09-29 14:50 [macd_momentum] ENTRADA XLM @ 0.204082 (22.66 €, apertura)
- 2026-09-29 14:50 [macd_sin_salida] ENTRADA XLM @ 0.204082 (22.92 €, apertura)
- 2026-09-29 14:50 [macd_momentum_regimen] ENTRADA XLM @ 0.204082 (22.66 €, apertura)
- 2026-09-29 14:50 [macd_momentum_evento] ENTRADA XLM @ 0.204082 (23.12 €, apertura)
- 2026-09-29 14:55 [macd_momentum] CIERRE AVAX momentum perdido bruto -0.76% neto -1.26%
- 2026-09-29 14:55 [macd_momentum_regimen] CIERRE AVAX momentum perdido bruto -0.76% neto -1.26%
- 2026-09-29 14:55 [macd_momentum_evento] CIERRE AVAX momentum perdido bruto -0.76% neto -1.86%
- 2026-09-29 14:50 [macd_momentum] ENTRADA DOGE @ 0.0843942 (22.65 €, apertura)
- 2026-09-29 14:50 [macd_momentum_regimen] ENTRADA DOGE @ 0.0843942 (22.65 €, apertura)
- 2026-09-29 14:50 [macd_momentum_evento] ENTRADA DOGE @ 0.0843942 (23.11 €, apertura)
- 2026-09-29 14:55 [c_banda_atr] CIERRE ENA stop-loss bruto -1.53% neto -2.63%
- 2026-09-29 14:55 [estocastico_rebote] CIERRE ENA stop-loss bruto -1.53% neto -2.03%
- 2026-09-29 14:55 [c_banda_atr_tope] CIERRE ENA stop-loss bruto -1.53% neto -2.63%
- 2026-09-29 14:55 [c_banda_atr_regimen] CIERRE ENA stop-loss bruto -1.53% neto -2.63%
- 2026-09-29 14:55 [c_banda_atr_evento] CIERRE ENA stop-loss bruto -1.53% neto -2.63%
- 2026-09-29 14:55 [macd_sin_salida] CIERRE TRX timeout bruto -0.06% neto -0.86%
- 2026-09-29 14:55 [c_banda_atr] CIERRE RAY timeout bruto +1.07% neto -0.03%
- 2026-09-29 14:55 [c_banda_atr_regimen] CIERRE RAY timeout bruto +1.07% neto -0.03%
- 2026-09-29 14:55 [ruptura_estricta] CIERRE PENGU timeout bruto +1.38% neto +0.28%
- 2026-09-29 14:55 [ruptura_estricta] CIERRE POL stop-loss bruto -2.12% neto -3.22%
- 2026-09-29 14:55 [ruptura_volumen] CIERRE TRUMP timeout bruto +1.32% neto +0.82%
- 2026-09-29 14:55 [ruptura_volumen_regimen] CIERRE TRUMP timeout bruto +1.32% neto +0.82%
- 2026-09-29 14:50 [ruptura_volumen_evento] ENTRADA TRUMP @ 1.842 (23.11 €, apertura)
- 2026-09-29 14:55 [c_banda_atr] CIERRE ASTER timeout bruto +0.71% neto -0.39%
- 2026-09-29 14:50 [macd_momentum] ENTRADA ASTER @ 0.64317 (22.65 €, apertura)
- 2026-09-29 14:55 [c_banda_atr_regimen] CIERRE ASTER timeout bruto +0.71% neto -0.39%
- 2026-09-29 14:50 [macd_momentum_regimen] ENTRADA ASTER @ 0.64317 (22.65 €, apertura)
- 2026-09-29 14:50 [macd_momentum_evento] ENTRADA ASTER @ 0.64317 (23.11 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
