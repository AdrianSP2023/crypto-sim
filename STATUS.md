# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 19:02 UTC · vueltas 53 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.18 € (-1.63%) | 45 | 9 | 29% | -0.370% | -1.416% | -1.571% | -14.69 € |
| reversion_bb | 922.37 € (-0.20%) | 6 | 4 | 50% | +0.000% | -1.100% | -1.233% | -1.53 € |
| ruptura_volumen | 899.05 € (-2.73%) | 72 | 3 | 14% | -0.670% | -1.532% | -1.672% | -25.31 € |
| rebote_extremo | 924.20 € (-0.00%) | 2 | 1 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 907.14 € (-1.85%) | 52 | 4 | 15% | -0.434% | -1.436% | -1.573% | -17.14 € |
| macd_momentum | 909.66 € (-1.58%) | 73 | 2 | 29% | -0.010% | -0.867% | -1.006% | -14.58 € |
| estocastico_rebote | 907.41 € (-1.82%) | 87 | 31 | 40% | +0.039% | -0.761% | -0.895% | -15.28 € |
| ruptura_estricta | 899.93 € (-2.63%) | 44 | 3 | 9% | -1.331% | -2.418% | -2.568% | -24.50 € |
| macd_sin_salida | 906.33 € (-1.94%) | 63 | 8 | 33% | -0.294% | -1.208% | -1.348% | -17.55 € |
| c_banda_atr_tope | 921.79 € (-0.27%) | 11 | 5 | 45% | +0.144% | -0.956% | -1.120% | -2.43 € |
| ruptura_volumen_tope | 918.64 € (-0.61%) | 17 | 2 | 24% | -0.279% | -1.379% | -1.470% | -5.41 € |
| c_banda_atr_regimen | 909.38 € (-1.61%) | 41 | 4 | 27% | -0.444% | -1.544% | -1.698% | -14.59 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.60 € (-2.77%) | 71 | 1 | 13% | -0.726% | -1.594% | -1.734% | -25.94 € |
| c_banda_atr_evento | 919.32 € (-0.53%) | 12 | 9 | 25% | -0.599% | -1.699% | -1.836% | -4.71 € |
| macd_momentum_evento | 917.18 € (-0.76%) | 26 | 2 | 23% | -0.078% | -1.178% | -1.318% | -7.06 € |
| ruptura_volumen_evento | 914.87 € (-1.01%) | 22 | 3 | 9% | -0.768% | -1.868% | -1.984% | -9.49 € |
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

- 2026-09-30 18:55 [estocastico_rebote] ENTRADA ZEC @ 1249.65 (22.72 €, apertura)
- 2026-09-30 18:55 [c_banda_atr] ENTRADA XLM @ 0.19947 (22.74 €, apertura)
- 2026-09-30 18:55 [c_banda_atr_tope] ENTRADA XLM @ 0.19947 (23.05 €, apertura)
- 2026-09-30 18:55 [c_banda_atr_evento] ENTRADA XLM @ 0.19947 (22.99 €, apertura)
- 2026-09-30 18:55 [estocastico_rebote] ENTRADA DOT @ 1.0846 (22.72 €, apertura)
- 2026-09-30 18:55 [estocastico_rebote] ENTRADA USELESS @ 0.21181 (22.72 €, apertura)
- 2026-09-30 18:55 [ruptura_volumen] ENTRADA TON @ 1.351 (22.47 €, apertura)
- 2026-09-30 18:55 [macd_momentum] ENTRADA TON @ 1.351 (22.74 €, apertura)
- 2026-09-30 18:55 [ruptura_estricta] ENTRADA TON @ 1.351 (22.49 €, apertura)
- 2026-09-30 18:55 [macd_sin_salida] ENTRADA TON @ 1.351 (22.67 €, apertura)
- 2026-09-30 18:55 [ruptura_volumen_tope] ENTRADA TON @ 1.351 (22.97 €, apertura)
- 2026-09-30 18:55 [macd_momentum_evento] ENTRADA TON @ 1.351 (22.93 €, apertura)
- 2026-09-30 18:55 [ruptura_volumen_evento] ENTRADA TON @ 1.351 (22.87 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
