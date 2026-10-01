# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 00:16 UTC · vueltas 74 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.96 € (-2.30%) | 78 | 26 | 28% | -0.315% | -1.150% | -1.281% | -20.59 € |
| reversion_bb | 921.89 € (-0.25%) | 10 | 5 | 40% | -0.070% | -1.170% | -1.295% | -2.71 € |
| ruptura_volumen | 894.56 € (-3.21%) | 97 | 23 | 16% | -0.498% | -1.267% | -1.391% | -28.12 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.47 € (-2.25%) | 71 | 3 | 14% | -0.416% | -1.288% | -1.415% | -20.94 € |
| macd_momentum | 901.15 € (-2.50%) | 135 | 2 | 24% | -0.056% | -0.750% | -0.864% | -23.17 € |
| estocastico_rebote | 902.32 € (-2.37%) | 129 | 12 | 34% | -0.044% | -0.747% | -0.869% | -22.15 € |
| ruptura_estricta | 897.76 € (-2.86%) | 52 | 9 | 13% | -1.113% | -2.121% | -2.266% | -25.38 € |
| macd_sin_salida | 902.38 € (-2.37%) | 90 | 27 | 33% | -0.220% | -1.010% | -1.138% | -20.91 € |
| c_banda_atr_tope | 918.87 € (-0.58%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.248% | -5.10 € |
| ruptura_volumen_tope | 916.11 € (-0.88%) | 28 | 5 | 18% | -0.171% | -1.271% | -1.357% | -8.20 € |
| c_banda_atr_regimen | 907.10 € (-1.85%) | 47 | 7 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.47 € (-1.71%) | 76 | 0 | 25% | -0.058% | -0.902% | -1.028% | -15.78 € |
| ruptura_volumen_regimen | 896.16 € (-3.04%) | 76 | 21 | 13% | -0.692% | -1.536% | -1.672% | -26.74 € |
| c_banda_atr_evento | 909.94 € (-1.55%) | 45 | 26 | 27% | -0.319% | -1.313% | -1.424% | -13.61 € |
| macd_momentum_evento | 906.15 € (-1.96%) | 88 | 2 | 17% | -0.102% | -0.902% | -1.004% | -18.18 € |
| ruptura_volumen_evento | 907.43 € (-1.82%) | 47 | 23 | 13% | -0.360% | -1.409% | -1.507% | -15.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 00:15 | c_banda_atr_evento | SUI | timeout | -0.09% | -0.89% | -0.20 |
| 2026-10-01 00:15 | estocastico_rebote | HBAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 00:15 | c_banda_atr | SUI | timeout | -0.09% | -0.59% | -0.13 |
| 2026-10-01 00:10 | macd_sin_salida | XDC | timeout | +0.76% | +0.26% | +0.06 |
| 2026-10-01 00:05 | ruptura_volumen_evento | ALGO | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-10-01 00:05 | ruptura_volumen_evento | SUI | stop-loss | -1.24% | -1.74% | -0.40 |
| 2026-10-01 00:05 | macd_momentum_evento | XDC | momentum perdido | +0.79% | -0.01% | -0.00 |
| 2026-10-01 00:05 | c_banda_atr_evento | MINA | take-profit | +2.00% | +1.20% | +0.27 |
| 2026-10-01 00:05 | ruptura_volumen_regimen | ALGO | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-10-01 00:05 | ruptura_volumen_regimen | SUI | stop-loss | -1.24% | -1.74% | -0.39 |
| 2026-10-01 00:05 | estocastico_rebote | XDC | timeout | +0.49% | -0.01% | -0.00 |
| 2026-10-01 00:05 | macd_momentum | XDC | momentum perdido | +0.79% | +0.29% | +0.07 |
| 2026-10-01 00:05 | pullback_tendencia | ENA | rotura de tendencia | -0.21% | -0.71% | -0.16 |
| 2026-10-01 00:05 | pullback_tendencia | ZRO | rotura de tendencia | -1.29% | -1.79% | -0.41 |
| 2026-10-01 00:05 | pullback_tendencia | ETH | rotura de tendencia | -0.22% | -0.72% | -0.16 |

## Eventos de la última vuelta

- 2026-10-01 00:15 [c_banda_atr] CIERRE SUI timeout bruto -0.09% neto -0.59%
- 2026-10-01 00:15 [c_banda_atr_evento] CIERRE SUI timeout bruto -0.09% neto -0.89%
- 2026-10-01 00:15 [estocastico_rebote] CIERRE HBAR stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
