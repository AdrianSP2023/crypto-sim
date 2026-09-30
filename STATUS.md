# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 19:12 UTC · vueltas 55 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.41 € (-1.60%) | 45 | 11 | 29% | -0.370% | -1.416% | -1.571% | -14.69 € |
| reversion_bb | 922.53 € (-0.19%) | 6 | 4 | 50% | +0.000% | -1.100% | -1.233% | -1.53 € |
| ruptura_volumen | 899.01 € (-2.73%) | 72 | 4 | 14% | -0.670% | -1.532% | -1.672% | -25.31 € |
| rebote_extremo | 924.05 € (-0.02%) | 2 | 1 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 906.93 € (-1.87%) | 53 | 4 | 15% | -0.454% | -1.446% | -1.589% | -17.59 € |
| macd_momentum | 909.67 € (-1.58%) | 73 | 6 | 29% | -0.010% | -0.867% | -1.006% | -14.58 € |
| estocastico_rebote | 908.17 € (-1.74%) | 87 | 32 | 40% | +0.039% | -0.761% | -0.895% | -15.28 € |
| ruptura_estricta | 899.70 € (-2.66%) | 44 | 3 | 9% | -1.331% | -2.418% | -2.568% | -24.50 € |
| macd_sin_salida | 906.45 € (-1.92%) | 63 | 10 | 33% | -0.294% | -1.208% | -1.348% | -17.55 € |
| c_banda_atr_tope | 922.09 € (-0.23%) | 11 | 5 | 45% | +0.144% | -0.956% | -1.120% | -2.43 € |
| ruptura_volumen_tope | 918.54 € (-0.62%) | 17 | 3 | 24% | -0.279% | -1.379% | -1.470% | -5.41 € |
| c_banda_atr_regimen | 909.38 € (-1.61%) | 41 | 4 | 27% | -0.444% | -1.544% | -1.698% | -14.59 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.66 € (-2.77%) | 71 | 1 | 13% | -0.726% | -1.594% | -1.734% | -25.94 € |
| c_banda_atr_evento | 919.56 € (-0.51%) | 12 | 11 | 25% | -0.599% | -1.699% | -1.836% | -4.71 € |
| macd_momentum_evento | 917.19 € (-0.76%) | 26 | 6 | 23% | -0.078% | -1.178% | -1.318% | -7.06 € |
| ruptura_volumen_evento | 914.83 € (-1.02%) | 22 | 4 | 9% | -0.768% | -1.868% | -1.984% | -9.49 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 19:10 | pullback_tendencia | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
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

## Eventos de la última vuelta

- 2026-09-30 19:05 [ruptura_volumen] ENTRADA HBAR @ 0.09514 (22.47 €, apertura)
- 2026-09-30 19:05 [ruptura_volumen_tope] ENTRADA HBAR @ 0.09514 (22.97 €, apertura)
- 2026-09-30 19:05 [ruptura_volumen_evento] ENTRADA HBAR @ 0.09514 (22.87 €, apertura)
- 2026-09-30 19:05 [macd_momentum] ENTRADA HYPE @ 79.38 (22.74 €, apertura)
- 2026-09-30 19:05 [macd_sin_salida] ENTRADA HYPE @ 79.38 (22.67 €, apertura)
- 2026-09-30 19:05 [macd_momentum_evento] ENTRADA HYPE @ 79.38 (22.93 €, apertura)
- 2026-09-30 19:05 [c_banda_atr] ENTRADA ENA @ 0.2344 (22.74 €, apertura)
- 2026-09-30 19:05 [c_banda_atr_evento] ENTRADA ENA @ 0.2344 (22.99 €, apertura)
- 2026-09-30 19:05 [estocastico_rebote] ENTRADA WLD @ 0.4692 (22.72 €, apertura)
- 2026-09-30 19:05 [macd_momentum] ENTRADA XDC @ 0.03028 (22.74 €, apertura)
- 2026-09-30 19:05 [macd_momentum_evento] ENTRADA XDC @ 0.03028 (22.93 €, apertura)
- 2026-09-30 19:10 [pullback_tendencia] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 19:05 [c_banda_atr] ENTRADA RENDER @ 1.7 (22.74 €, apertura)
- 2026-09-30 19:05 [c_banda_atr_evento] ENTRADA RENDER @ 1.7 (22.99 €, apertura)
- 2026-09-30 19:05 [macd_momentum] ENTRADA BNB @ 677.68 (22.74 €, apertura)
- 2026-09-30 19:05 [macd_sin_salida] ENTRADA BNB @ 677.68 (22.67 €, apertura)
- 2026-09-30 19:05 [macd_momentum_evento] ENTRADA BNB @ 677.68 (22.93 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
