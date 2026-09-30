# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 22:51 UTC · vueltas 99 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.45 € (-1.92%) | 67 | 32 | 22% | -0.505% | -1.395% | -1.540% | -21.44 € |
| reversion_bb | 922.17 € (-0.22%) | 9 | 5 | 44% | -0.167% | -1.267% | -1.401% | -2.64 € |
| ruptura_volumen | 896.23 € (-3.03%) | 93 | 16 | 16% | -0.522% | -1.302% | -1.440% | -27.73 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.74 € (-2.11%) | 65 | 1 | 15% | -0.413% | -1.319% | -1.456% | -19.65 € |
| macd_momentum | 906.26 € (-1.95%) | 102 | 31 | 25% | -0.078% | -0.834% | -0.964% | -19.52 € |
| estocastico_rebote | 903.73 € (-2.22%) | 126 | 9 | 35% | -0.025% | -0.732% | -0.864% | -21.23 € |
| ruptura_estricta | 898.98 € (-2.73%) | 49 | 9 | 12% | -1.233% | -2.272% | -2.420% | -25.61 € |
| macd_sin_salida | 905.88 € (-1.99%) | 82 | 32 | 33% | -0.260% | -1.079% | -1.210% | -20.34 € |
| c_banda_atr_tope | 919.81 € (-0.48%) | 19 | 5 | 32% | -0.054% | -1.154% | -1.311% | -5.05 € |
| ruptura_volumen_tope | 916.97 € (-0.79%) | 25 | 5 | 20% | -0.209% | -1.309% | -1.428% | -7.54 € |
| c_banda_atr_regimen | 908.48 € (-1.71%) | 45 | 4 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.09 € (-1.42%) | 60 | 14 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 897.72 € (-2.87%) | 72 | 16 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 914.08 € (-1.10%) | 34 | 32 | 15% | -0.695% | -1.768% | -1.898% | -13.85 € |
| macd_momentum_evento | 911.35 € (-1.39%) | 55 | 31 | 16% | -0.169% | -1.143% | -1.267% | -14.43 € |
| ruptura_volumen_evento | 909.19 € (-1.63%) | 43 | 16 | 12% | -0.400% | -1.493% | -1.615% | -14.77 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-30 22:35 | c_banda_atr_tope | CRV | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 22:35 | macd_sin_salida | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 22:35 | macd_sin_salida | PUMP | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-09-30 22:45 [ruptura_volumen_regimen] ENTRADA ETH @ 2373.01 (22.46 €, apertura)
- 2026-09-30 22:45 [ruptura_volumen] ENTRADA SUI @ 1.036 (22.41 €, apertura)
- 2026-09-30 22:45 [ruptura_estricta] ENTRADA SUI @ 1.036 (22.47 €, apertura)
- 2026-09-30 22:45 [ruptura_volumen_regimen] ENTRADA SUI @ 1.036 (22.46 €, apertura)
- 2026-09-30 22:45 [ruptura_volumen_evento] ENTRADA SUI @ 1.036 (22.74 €, apertura)
- 2026-09-30 22:45 [ruptura_volumen] ENTRADA ZEC @ 1264.62 (22.41 €, apertura)
- 2026-09-30 22:45 [ruptura_volumen_regimen] ENTRADA ZEC @ 1264.62 (22.46 €, apertura)
- 2026-09-30 22:45 [ruptura_volumen_evento] ENTRADA ZEC @ 1264.62 (22.74 €, apertura)
- 2026-09-30 22:45 [macd_momentum] ENTRADA KSM @ 4.57 (22.62 €, apertura)
- 2026-09-30 22:45 [macd_sin_salida] ENTRADA KSM @ 4.57 (22.60 €, apertura)
- 2026-09-30 22:45 [macd_momentum_regimen] ENTRADA KSM @ 4.57 (22.78 €, apertura)
- 2026-09-30 22:45 [macd_momentum_evento] ENTRADA KSM @ 4.57 (22.75 €, apertura)
- 2026-09-30 22:45 [ruptura_volumen] ENTRADA BNB @ 678.18 (22.41 €, apertura)
- 2026-09-30 22:45 [ruptura_volumen_regimen] ENTRADA BNB @ 678.18 (22.46 €, apertura)
- 2026-09-30 22:45 [ruptura_volumen_evento] ENTRADA BNB @ 678.18 (22.74 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
