# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 19:56 UTC · vueltas 64 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.21 € (-1.84%) | 48 | 18 | 27% | -0.388% | -1.419% | -1.570% | -15.69 € |
| reversion_bb | 922.53 € (-0.19%) | 7 | 5 | 57% | +0.214% | -0.886% | -1.014% | -1.44 € |
| ruptura_volumen | 898.23 € (-2.81%) | 74 | 4 | 14% | -0.665% | -1.518% | -1.656% | -25.76 € |
| rebote_extremo | 924.18 € (-0.01%) | 2 | 1 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 905.31 € (-2.05%) | 57 | 1 | 14% | -0.483% | -1.446% | -1.583% | -18.90 € |
| macd_momentum | 908.64 € (-1.69%) | 77 | 5 | 27% | -0.026% | -0.865% | -1.001% | -15.32 € |
| estocastico_rebote | 904.43 € (-2.14%) | 94 | 26 | 38% | -0.041% | -0.819% | -0.954% | -17.74 € |
| ruptura_estricta | 898.88 € (-2.74%) | 45 | 3 | 9% | -1.346% | -2.426% | -2.575% | -25.13 € |
| macd_sin_salida | 904.76 € (-2.11%) | 64 | 11 | 33% | -0.313% | -1.221% | -1.360% | -18.01 € |
| c_banda_atr_tope | 921.41 € (-0.31%) | 13 | 5 | 38% | +0.095% | -1.005% | -1.154% | -3.02 € |
| ruptura_volumen_tope | 918.05 € (-0.67%) | 18 | 4 | 22% | -0.331% | -1.431% | -1.522% | -5.94 € |
| c_banda_atr_regimen | 909.01 € (-1.65%) | 42 | 3 | 26% | -0.472% | -1.572% | -1.727% | -15.21 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 917.12 € (-0.77%) | 15 | 18 | 20% | -0.611% | -1.711% | -1.842% | -5.93 € |
| macd_momentum_evento | 915.60 € (-0.93%) | 30 | 5 | 20% | -0.111% | -1.211% | -1.344% | -8.36 € |
| ruptura_volumen_evento | 913.76 € (-1.13%) | 24 | 4 | 8% | -0.746% | -1.846% | -1.960% | -10.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 19:55 | estocastico_rebote | SPX | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 19:55 | estocastico_rebote | DASH | stop-loss | -1.56% | -2.06% | -0.47 |
| 2026-09-30 19:55 | estocastico_rebote | USELESS | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 19:55 | pullback_tendencia | HYPE | rotura de tendencia | -0.47% | -0.97% | -0.22 |
| 2026-09-30 19:55 | pullback_tendencia | NEAR | rotura de tendencia | -1.00% | -1.50% | -0.34 |
| 2026-09-30 19:50 | estocastico_rebote | HBAR | take-profit | +1.80% | +1.30% | +0.30 |
| 2026-09-30 19:45 | reversion_bb | CRV | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-09-30 19:35 | c_banda_atr_evento | ICP | timeout | -0.89% | -1.99% | -0.46 |
| 2026-09-30 19:35 | c_banda_atr_evento | UNI | timeout | +0.54% | -0.56% | -0.13 |
| 2026-09-30 19:35 | c_banda_atr_tope | ICP | timeout | -0.89% | -1.99% | -0.46 |
| 2026-09-30 19:35 | c_banda_atr_tope | UNI | timeout | +0.54% | -0.56% | -0.13 |
| 2026-09-30 19:35 | c_banda_atr | ICP | timeout | -0.89% | -1.69% | -0.39 |
| 2026-09-30 19:35 | c_banda_atr | UNI | timeout | +0.54% | -0.26% | -0.06 |
| 2026-09-30 19:30 | macd_momentum_evento | TON | momentum perdido | -0.74% | -1.84% | -0.42 |
| 2026-09-30 19:30 | macd_momentum_evento | HYPE | momentum perdido | -0.29% | -1.39% | -0.32 |

## Eventos de la última vuelta

- 2026-09-30 19:50 [pullback_tendencia] ENTRADA NEAR @ 4.7695 (22.65 €, apertura)
- 2026-09-30 19:55 [pullback_tendencia] CIERRE NEAR rotura de tendencia bruto -1.00% neto -1.50%
- 2026-09-30 19:55 [pullback_tendencia] CIERRE HYPE rotura de tendencia bruto -0.47% neto -0.97%
- 2026-09-30 19:50 [ruptura_volumen] ENTRADA TRX @ 0.298277 (22.46 €, apertura)
- 2026-09-30 19:50 [ruptura_volumen_tope] ENTRADA TRX @ 0.298277 (22.96 €, apertura)
- 2026-09-30 19:50 [ruptura_volumen_evento] ENTRADA TRX @ 0.298277 (22.85 €, apertura)
- 2026-09-30 19:55 [estocastico_rebote] CIERRE USELESS stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 19:50 [c_banda_atr] ENTRADA SHIB @ 5.055e-06 (22.71 €, apertura)
- 2026-09-30 19:50 [c_banda_atr_evento] ENTRADA SHIB @ 5.055e-06 (22.96 €, apertura)
- 2026-09-30 19:55 [estocastico_rebote] CIERRE DASH stop-loss bruto -1.56% neto -2.06%
- 2026-09-30 19:55 [estocastico_rebote] CIERRE SPX stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
