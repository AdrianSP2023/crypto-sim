# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 22:46 UTC · vueltas 98 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.57 € (-1.91%) | 67 | 32 | 22% | -0.505% | -1.395% | -1.540% | -21.44 € |
| reversion_bb | 922.20 € (-0.22%) | 9 | 5 | 44% | -0.167% | -1.267% | -1.401% | -2.64 € |
| ruptura_volumen | 896.71 € (-2.98%) | 93 | 13 | 16% | -0.522% | -1.302% | -1.440% | -27.73 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.86 € (-2.10%) | 65 | 1 | 15% | -0.413% | -1.319% | -1.456% | -19.65 € |
| macd_momentum | 906.65 € (-1.90%) | 102 | 30 | 25% | -0.078% | -0.834% | -0.964% | -19.52 € |
| estocastico_rebote | 903.65 € (-2.23%) | 126 | 9 | 35% | -0.025% | -0.732% | -0.864% | -21.23 € |
| ruptura_estricta | 899.11 € (-2.72%) | 49 | 8 | 12% | -1.233% | -2.272% | -2.420% | -25.61 € |
| macd_sin_salida | 906.26 € (-1.95%) | 82 | 31 | 33% | -0.260% | -1.079% | -1.210% | -20.34 € |
| c_banda_atr_tope | 919.90 € (-0.47%) | 19 | 5 | 32% | -0.054% | -1.154% | -1.311% | -5.05 € |
| ruptura_volumen_tope | 917.07 € (-0.78%) | 25 | 5 | 20% | -0.209% | -1.309% | -1.428% | -7.54 € |
| c_banda_atr_regimen | 908.47 € (-1.71%) | 45 | 4 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.34 € (-1.40%) | 60 | 13 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.20 € (-2.82%) | 72 | 12 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 914.20 € (-1.09%) | 34 | 32 | 15% | -0.695% | -1.768% | -1.898% | -13.85 € |
| macd_momentum_evento | 911.75 € (-1.35%) | 55 | 30 | 16% | -0.169% | -1.143% | -1.267% | -14.43 € |
| ruptura_volumen_evento | 909.67 € (-1.58%) | 43 | 13 | 12% | -0.400% | -1.493% | -1.615% | -14.77 € |
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

- 2026-09-30 22:40 [ruptura_volumen] ENTRADA SOL @ 104.54 (22.41 €, apertura)
- 2026-09-30 22:40 [ruptura_volumen_regimen] ENTRADA SOL @ 104.54 (22.46 €, apertura)
- 2026-09-30 22:40 [ruptura_volumen_evento] ENTRADA SOL @ 104.54 (22.74 €, apertura)
- 2026-09-30 22:40 [ruptura_volumen] ENTRADA ENA @ 0.2352 (22.41 €, apertura)
- 2026-09-30 22:40 [ruptura_volumen_regimen] ENTRADA ENA @ 0.2352 (22.46 €, apertura)
- 2026-09-30 22:40 [ruptura_volumen_evento] ENTRADA ENA @ 0.2352 (22.74 €, apertura)
- 2026-09-30 22:40 [ruptura_volumen] ENTRADA ALGO @ 0.11088 (22.41 €, apertura)
- 2026-09-30 22:40 [ruptura_estricta] ENTRADA ALGO @ 0.11088 (22.46 €, apertura)
- 2026-09-30 22:40 [ruptura_volumen_regimen] ENTRADA ALGO @ 0.11088 (22.46 €, apertura)
- 2026-09-30 22:40 [ruptura_volumen_evento] ENTRADA ALGO @ 0.11088 (22.74 €, apertura)
- 2026-09-30 22:45 [ruptura_estricta] CIERRE CRV timeout bruto +1.10% neto +0.60%
- 2026-09-30 22:40 [macd_momentum] ENTRADA FIL @ 0.919 (22.62 €, apertura)
- 2026-09-30 22:40 [macd_sin_salida] ENTRADA FIL @ 0.919 (22.60 €, apertura)
- 2026-09-30 22:40 [macd_momentum_regimen] ENTRADA FIL @ 0.919 (22.78 €, apertura)
- 2026-09-30 22:40 [macd_momentum_evento] ENTRADA FIL @ 0.919 (22.75 €, apertura)
- 2026-09-30 22:40 [macd_momentum] ENTRADA SHIB @ 5.097e-06 (22.62 €, apertura)
- 2026-09-30 22:40 [macd_sin_salida] ENTRADA SHIB @ 5.097e-06 (22.60 €, apertura)
- 2026-09-30 22:40 [macd_momentum_regimen] ENTRADA SHIB @ 5.097e-06 (22.78 €, apertura)
- 2026-09-30 22:40 [macd_momentum_evento] ENTRADA SHIB @ 5.097e-06 (22.75 €, apertura)
- 2026-09-30 22:40 [c_banda_atr] ENTRADA DASH @ 53.485 (22.57 €, apertura)
- 2026-09-30 22:40 [ruptura_volumen] ENTRADA DASH @ 53.485 (22.41 €, apertura)
- 2026-09-30 22:40 [macd_momentum] ENTRADA DASH @ 53.485 (22.62 €, apertura)
- 2026-09-30 22:40 [macd_sin_salida] ENTRADA DASH @ 53.485 (22.60 €, apertura)
- 2026-09-30 22:40 [c_banda_atr_regimen] ENTRADA DASH @ 53.485 (22.71 €, apertura)
- 2026-09-30 22:40 [macd_momentum_regimen] ENTRADA DASH @ 53.485 (22.78 €, apertura)
- 2026-09-30 22:40 [ruptura_volumen_regimen] ENTRADA DASH @ 53.485 (22.46 €, apertura)
- 2026-09-30 22:40 [c_banda_atr_evento] ENTRADA DASH @ 53.485 (22.76 €, apertura)
- 2026-09-30 22:40 [macd_momentum_evento] ENTRADA DASH @ 53.485 (22.75 €, apertura)
- 2026-09-30 22:40 [ruptura_volumen_evento] ENTRADA DASH @ 53.485 (22.74 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
