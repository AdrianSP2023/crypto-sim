# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 22:56 UTC · vueltas 100 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.51 € (-1.92%) | 68 | 31 | 24% | -0.485% | -1.368% | -1.512% | -21.36 € |
| reversion_bb | 922.21 € (-0.22%) | 9 | 5 | 44% | -0.167% | -1.267% | -1.401% | -2.64 € |
| ruptura_volumen | 896.29 € (-3.02%) | 93 | 19 | 16% | -0.522% | -1.302% | -1.440% | -27.73 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.70 € (-2.11%) | 65 | 1 | 15% | -0.413% | -1.319% | -1.456% | -19.65 € |
| macd_momentum | 906.13 € (-1.96%) | 102 | 31 | 25% | -0.078% | -0.834% | -0.964% | -19.52 € |
| estocastico_rebote | 903.56 € (-2.24%) | 126 | 9 | 35% | -0.025% | -0.732% | -0.864% | -21.23 € |
| ruptura_estricta | 898.87 € (-2.74%) | 49 | 9 | 12% | -1.233% | -2.272% | -2.420% | -25.61 € |
| macd_sin_salida | 905.81 € (-1.99%) | 82 | 32 | 33% | -0.260% | -1.079% | -1.210% | -20.34 € |
| c_banda_atr_tope | 919.61 € (-0.50%) | 20 | 4 | 30% | -0.007% | -1.107% | -1.258% | -5.10 € |
| ruptura_volumen_tope | 916.92 € (-0.79%) | 25 | 5 | 20% | -0.209% | -1.309% | -1.428% | -7.54 € |
| c_banda_atr_regimen | 908.47 € (-1.71%) | 45 | 4 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.00 € (-1.43%) | 60 | 14 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 897.76 € (-2.87%) | 72 | 19 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 914.07 € (-1.10%) | 35 | 31 | 17% | -0.650% | -1.715% | -1.843% | -13.83 € |
| macd_momentum_evento | 911.21 € (-1.41%) | 55 | 31 | 16% | -0.169% | -1.143% | -1.267% | -14.43 € |
| ruptura_volumen_evento | 909.25 € (-1.62%) | 43 | 19 | 12% | -0.400% | -1.493% | -1.615% | -14.77 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 22:55 | c_banda_atr_evento | XLM | timeout | +0.88% | +0.08% | +0.02 |
| 2026-09-30 22:55 | c_banda_atr_tope | XLM | timeout | +0.88% | -0.22% | -0.05 |
| 2026-09-30 22:55 | c_banda_atr | XLM | timeout | +0.88% | +0.38% | +0.09 |
| 2026-09-30 22:45 | ruptura_estricta | CRV | timeout | +1.10% | +0.60% | +0.14 |
| 2026-09-30 22:40 | ruptura_volumen_evento | SHIB | timeout | +0.22% | -0.58% | -0.13 |
| 2026-09-30 22:40 | macd_momentum_evento | HYPE | momentum perdido | +0.01% | -0.49% | -0.11 |
| 2026-09-30 22:40 | c_banda_atr_evento | ENA | take-profit | +2.04% | +1.24% | +0.28 |
| 2026-09-30 22:40 | macd_momentum | HYPE | momentum perdido | +0.01% | -0.49% | -0.11 |
| 2026-09-30 22:40 | ruptura_volumen | SHIB | timeout | +0.22% | -0.28% | -0.06 |
| 2026-09-30 22:40 | c_banda_atr | ENA | take-profit | +2.04% | +1.54% | +0.35 |
| 2026-09-30 22:35 | ruptura_volumen_evento | ZRO | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 22:35 | macd_momentum_evento | PUMP | take-profit | +2.00% | +1.20% | +0.28 |
| 2026-09-30 22:35 | c_banda_atr_evento | BNB | timeout | +0.08% | -0.72% | -0.17 |
| 2026-09-30 22:35 | c_banda_atr_evento | CRV | take-profit | +2.00% | +1.20% | +0.28 |
| 2026-09-30 22:35 | ruptura_volumen_tope | ZRO | take-profit | +2.50% | +1.40% | +0.32 |

## Eventos de la última vuelta

- 2026-09-30 22:50 [ruptura_volumen] ENTRADA AAVE @ 140.85 (22.41 €, apertura)
- 2026-09-30 22:50 [ruptura_volumen_regimen] ENTRADA AAVE @ 140.85 (22.46 €, apertura)
- 2026-09-30 22:50 [ruptura_volumen_evento] ENTRADA AAVE @ 140.85 (22.74 €, apertura)
- 2026-09-30 22:55 [c_banda_atr] CIERRE XLM timeout bruto +0.88% neto +0.38%
- 2026-09-30 22:55 [c_banda_atr_tope] CIERRE XLM timeout bruto +0.88% neto -0.22%
- 2026-09-30 22:55 [c_banda_atr_evento] CIERRE XLM timeout bruto +0.88% neto +0.08%
- 2026-09-30 22:50 [ruptura_volumen] ENTRADA ONDO @ 0.44284 (22.41 €, apertura)
- 2026-09-30 22:50 [ruptura_volumen_regimen] ENTRADA ONDO @ 0.44284 (22.46 €, apertura)
- 2026-09-30 22:50 [ruptura_volumen_evento] ENTRADA ONDO @ 0.44284 (22.74 €, apertura)
- 2026-09-30 22:50 [ruptura_volumen] ENTRADA SPX @ 0.3905 (22.41 €, apertura)
- 2026-09-30 22:50 [ruptura_volumen_regimen] ENTRADA SPX @ 0.3905 (22.46 €, apertura)
- 2026-09-30 22:50 [ruptura_volumen_evento] ENTRADA SPX @ 0.3905 (22.74 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
