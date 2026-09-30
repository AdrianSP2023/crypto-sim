# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 22:26 UTC · vueltas 94 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.45 € (-2.36%) | 64 | 23 | 20% | -0.593% | -1.501% | -1.650% | -22.04 € |
| reversion_bb | 921.98 € (-0.24%) | 9 | 5 | 44% | -0.167% | -1.267% | -1.401% | -2.64 € |
| ruptura_volumen | 896.49 € (-3.00%) | 89 | 5 | 16% | -0.568% | -1.361% | -1.502% | -27.73 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.68 € (-2.12%) | 65 | 1 | 15% | -0.413% | -1.319% | -1.456% | -19.65 € |
| macd_momentum | 904.82 € (-2.10%) | 100 | 7 | 24% | -0.100% | -0.861% | -0.993% | -19.75 € |
| estocastico_rebote | 902.58 € (-2.34%) | 123 | 11 | 33% | -0.071% | -0.783% | -0.916% | -22.15 € |
| ruptura_estricta | 898.31 € (-2.81%) | 48 | 6 | 10% | -1.282% | -2.332% | -2.480% | -25.75 € |
| macd_sin_salida | 903.44 € (-2.25%) | 80 | 14 | 31% | -0.317% | -1.143% | -1.276% | -21.02 € |
| c_banda_atr_tope | 919.07 € (-0.56%) | 18 | 5 | 28% | -0.168% | -1.268% | -1.428% | -5.26 € |
| ruptura_volumen_tope | 916.78 € (-0.81%) | 24 | 5 | 17% | -0.322% | -1.422% | -1.541% | -7.86 € |
| c_banda_atr_regimen | 908.47 € (-1.71%) | 45 | 0 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 910.24 € (-1.51%) | 31 | 23 | 10% | -0.895% | -1.995% | -2.132% | -14.24 € |
| macd_momentum_evento | 909.97 € (-1.54%) | 53 | 7 | 15% | -0.213% | -1.200% | -1.327% | -14.60 € |
| ruptura_volumen_evento | 909.93 € (-1.55%) | 39 | 5 | 10% | -0.492% | -1.592% | -1.721% | -14.29 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 22:25 | ruptura_volumen_evento | ASTER | timeout | +0.45% | -0.65% | -0.15 |
| 2026-09-30 22:25 | ruptura_volumen_evento | XDC | timeout | +0.13% | -0.97% | -0.22 |
| 2026-09-30 22:25 | ruptura_volumen_evento | POL | timeout | -0.38% | -1.48% | -0.34 |
| 2026-09-30 22:25 | ruptura_volumen_evento | LTC | timeout | +0.63% | -0.47% | -0.11 |
| 2026-09-30 22:25 | ruptura_volumen_evento | HYPE | timeout | +1.18% | +0.08% | +0.02 |
| 2026-09-30 22:25 | ruptura_volumen | ASTER | timeout | +0.45% | -0.05% | -0.01 |
| 2026-09-30 22:25 | ruptura_volumen | XDC | timeout | +0.13% | -0.37% | -0.08 |
| 2026-09-30 22:25 | ruptura_volumen | POL | timeout | -0.38% | -0.88% | -0.20 |
| 2026-09-30 22:25 | ruptura_volumen | LTC | timeout | +0.63% | +0.13% | +0.03 |
| 2026-09-30 22:25 | ruptura_volumen | HYPE | timeout | +1.18% | +0.68% | +0.15 |
| 2026-09-30 22:15 | macd_momentum_evento | HYPE | momentum perdido | +0.68% | -0.12% | -0.03 |
| 2026-09-30 22:15 | macd_momentum_evento | LINK | momentum perdido | -0.39% | -1.19% | -0.27 |
| 2026-09-30 22:15 | macd_momentum | HYPE | momentum perdido | +0.68% | +0.18% | +0.04 |
| 2026-09-30 22:15 | macd_momentum | LINK | momentum perdido | -0.39% | -0.89% | -0.20 |
| 2026-09-30 22:10 | ruptura_volumen_evento | KSM | stop-loss | -1.32% | -2.42% | -0.55 |

## Eventos de la última vuelta

- 2026-09-30 22:20 [c_banda_atr] ENTRADA NEAR @ 4.7149 (22.56 €, apertura)
- 2026-09-30 22:20 [macd_momentum] ENTRADA NEAR @ 4.7149 (22.61 €, apertura)
- 2026-09-30 22:20 [macd_sin_salida] ENTRADA NEAR @ 4.7149 (22.58 €, apertura)
- 2026-09-30 22:20 [c_banda_atr_tope] ENTRADA NEAR @ 4.7149 (22.97 €, apertura)
- 2026-09-30 22:20 [c_banda_atr_evento] ENTRADA NEAR @ 4.7149 (22.75 €, apertura)
- 2026-09-30 22:20 [macd_momentum_evento] ENTRADA NEAR @ 4.7149 (22.74 €, apertura)
- 2026-09-30 22:20 [c_banda_atr] ENTRADA HYPE @ 80.58 (22.56 €, apertura)
- 2026-09-30 22:25 [ruptura_volumen] CIERRE HYPE timeout bruto +1.18% neto +0.68%
- 2026-09-30 22:20 [macd_momentum] ENTRADA HYPE @ 80.58 (22.61 €, apertura)
- 2026-09-30 22:20 [macd_sin_salida] ENTRADA HYPE @ 80.58 (22.58 €, apertura)
- 2026-09-30 22:20 [c_banda_atr_tope] ENTRADA HYPE @ 80.58 (22.97 €, apertura)
- 2026-09-30 22:20 [c_banda_atr_evento] ENTRADA HYPE @ 80.58 (22.75 €, apertura)
- 2026-09-30 22:20 [macd_momentum_evento] ENTRADA HYPE @ 80.58 (22.74 €, apertura)
- 2026-09-30 22:25 [ruptura_volumen_evento] CIERRE HYPE timeout bruto +1.18% neto +0.08%
- 2026-09-30 22:25 [ruptura_volumen] CIERRE LTC timeout bruto +0.63% neto +0.13%
- 2026-09-30 22:20 [ruptura_volumen_tope] ENTRADA LTC @ 59.12 (22.91 €, apertura)
- 2026-09-30 22:25 [ruptura_volumen_evento] CIERRE LTC timeout bruto +0.63% neto -0.47%
- 2026-09-30 22:20 [c_banda_atr] ENTRADA ENA @ 0.2303 (22.56 €, apertura)
- 2026-09-30 22:20 [c_banda_atr_evento] ENTRADA ENA @ 0.2303 (22.75 €, apertura)
- 2026-09-30 22:25 [ruptura_volumen] CIERRE POL timeout bruto -0.38% neto -0.88%
- 2026-09-30 22:25 [ruptura_volumen_evento] CIERRE POL timeout bruto -0.38% neto -1.48%
- 2026-09-30 22:20 [c_banda_atr] ENTRADA ALGO @ 0.10986 (22.56 €, apertura)
- 2026-09-30 22:20 [c_banda_atr_evento] ENTRADA ALGO @ 0.10986 (22.75 €, apertura)
- 2026-09-30 22:20 [estocastico_rebote] ENTRADA WLD @ 0.4702 (22.55 €, apertura)
- 2026-09-30 22:25 [ruptura_volumen] CIERRE XDC timeout bruto +0.13% neto -0.37%
- 2026-09-30 22:25 [ruptura_volumen_evento] CIERRE XDC timeout bruto +0.13% neto -0.97%
- 2026-09-30 22:20 [macd_momentum] ENTRADA JUP @ 0.28929 (22.61 €, apertura)
- 2026-09-30 22:20 [macd_momentum_evento] ENTRADA JUP @ 0.28929 (22.74 €, apertura)
- 2026-09-30 22:20 [c_banda_atr] ENTRADA MINA @ 0.1258 (22.56 €, apertura)
- 2026-09-30 22:20 [c_banda_atr_evento] ENTRADA MINA @ 0.1258 (22.75 €, apertura)
- 2026-09-30 22:25 [ruptura_volumen] CIERRE ASTER timeout bruto +0.45% neto -0.05%
- 2026-09-30 22:25 [ruptura_volumen_evento] CIERRE ASTER timeout bruto +0.45% neto -0.65%
- 2026-09-30 22:20 [macd_momentum] ENTRADA SPX @ 0.3867 (22.61 €, apertura)
- 2026-09-30 22:20 [macd_sin_salida] ENTRADA SPX @ 0.3867 (22.58 €, apertura)
- 2026-09-30 22:20 [macd_momentum_evento] ENTRADA SPX @ 0.3867 (22.74 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
