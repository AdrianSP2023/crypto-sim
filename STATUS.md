# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 19:07 UTC · vueltas 54 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.18 € (-1.63%) | 45 | 9 | 29% | -0.370% | -1.416% | -1.571% | -14.69 € |
| reversion_bb | 922.54 € (-0.18%) | 6 | 4 | 50% | +0.000% | -1.100% | -1.233% | -1.53 € |
| ruptura_volumen | 898.97 € (-2.73%) | 72 | 3 | 14% | -0.670% | -1.532% | -1.672% | -25.31 € |
| rebote_extremo | 924.11 € (-0.01%) | 2 | 1 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 907.14 € (-1.85%) | 52 | 5 | 15% | -0.434% | -1.436% | -1.573% | -17.14 € |
| macd_momentum | 909.63 € (-1.58%) | 73 | 3 | 29% | -0.010% | -0.867% | -1.006% | -14.58 € |
| estocastico_rebote | 908.06 € (-1.75%) | 87 | 31 | 40% | +0.039% | -0.761% | -0.895% | -15.28 € |
| ruptura_estricta | 899.84 € (-2.64%) | 44 | 3 | 9% | -1.331% | -2.418% | -2.568% | -24.50 € |
| macd_sin_salida | 906.35 € (-1.94%) | 63 | 8 | 33% | -0.294% | -1.208% | -1.348% | -17.55 € |
| c_banda_atr_tope | 921.87 € (-0.26%) | 11 | 5 | 45% | +0.144% | -0.956% | -1.120% | -2.43 € |
| ruptura_volumen_tope | 918.62 € (-0.61%) | 17 | 2 | 24% | -0.279% | -1.379% | -1.470% | -5.41 € |
| c_banda_atr_regimen | 909.38 € (-1.61%) | 41 | 4 | 27% | -0.444% | -1.544% | -1.698% | -14.59 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.54 € (-2.78%) | 71 | 1 | 13% | -0.726% | -1.594% | -1.734% | -25.94 € |
| c_banda_atr_evento | 919.33 € (-0.53%) | 12 | 9 | 25% | -0.599% | -1.699% | -1.836% | -4.71 € |
| macd_momentum_evento | 917.15 € (-0.77%) | 26 | 3 | 23% | -0.078% | -1.178% | -1.318% | -7.06 € |
| ruptura_volumen_evento | 914.78 € (-1.02%) | 22 | 3 | 9% | -0.768% | -1.868% | -1.984% | -9.49 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 18:55 | macd_momentum_evento | NEAR | momentum perdido | -0.77% | -1.87% | -0.43 |
| 2026-09-30 18:55 | macd_momentum | NEAR | momentum perdido | -0.77% | -1.27% | -0.29 |
| 2026-09-30 18:50 | macd_momentum_evento | ALGO | momentum perdido | -1.14% | -2.24% | -0.52 |
| 2026-09-30 18:50 | c_banda_atr_evento | VVV | timeout | -0.93% | -2.02% | -0.47 |
| 2026-09-30 18:50 | c_banda_atr_tope | VVV | timeout | -0.93% | -2.02% | -0.47 |
| 2026-09-30 18:50 | estocastico_rebote | RENDER | stop-loss | -1.58% | -2.08% | -0.48 |
| 2026-09-30 18:50 | estocastico_rebote | DOT | stop-loss | -1.72% | -2.22% | -0.51 |
| 2026-09-30 18:50 | estocastico_rebote | ZEC | stop-loss | -1.63% | -2.13% | -0.49 |
| 2026-09-30 18:50 | macd_momentum | ALGO | momentum perdido | -1.14% | -1.64% | -0.37 |
| 2026-09-30 18:50 | reversion_bb | TRUMP | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 18:50 | c_banda_atr | VVV | timeout | -0.93% | -1.73% | -0.39 |
| 2026-09-30 18:45 | c_banda_atr_evento | DASH | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 18:45 | c_banda_atr_regimen | DASH | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-30 18:45 | c_banda_atr | DASH | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 18:40 | macd_momentum_evento | MON | momentum perdido | -0.31% | -1.41% | -0.33 |

## Eventos de la última vuelta

- 2026-09-30 19:00 [macd_momentum] ENTRADA XLM @ 0.199623 (22.74 €, apertura)
- 2026-09-30 19:00 [macd_momentum_evento] ENTRADA XLM @ 0.199623 (22.93 €, apertura)
- 2026-09-30 19:00 [pullback_tendencia] ENTRADA MON @ 0.02566 (22.68 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
