# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 19:36 UTC · vueltas 60 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.42 € (-1.71%) | 48 | 10 | 27% | -0.388% | -1.419% | -1.570% | -15.69 € |
| reversion_bb | 922.75 € (-0.16%) | 6 | 6 | 50% | +0.000% | -1.100% | -1.233% | -1.53 € |
| ruptura_volumen | 898.43 € (-2.79%) | 74 | 2 | 14% | -0.665% | -1.518% | -1.656% | -25.76 € |
| rebote_extremo | 924.26 € (+0.00%) | 2 | 1 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 906.01 € (-1.97%) | 55 | 2 | 15% | -0.474% | -1.454% | -1.595% | -18.35 € |
| macd_momentum | 908.93 € (-1.66%) | 77 | 3 | 27% | -0.026% | -0.865% | -1.001% | -15.32 € |
| estocastico_rebote | 907.67 € (-1.79%) | 90 | 30 | 39% | -0.012% | -0.802% | -0.935% | -16.65 € |
| ruptura_estricta | 899.09 € (-2.72%) | 45 | 2 | 9% | -1.346% | -2.426% | -2.575% | -25.13 € |
| macd_sin_salida | 905.69 € (-2.01%) | 64 | 10 | 33% | -0.313% | -1.221% | -1.360% | -18.01 € |
| c_banda_atr_tope | 921.53 € (-0.29%) | 13 | 3 | 38% | +0.095% | -1.005% | -1.154% | -3.02 € |
| ruptura_volumen_tope | 918.25 € (-0.65%) | 18 | 2 | 22% | -0.331% | -1.431% | -1.522% | -5.94 € |
| c_banda_atr_regimen | 908.91 € (-1.66%) | 42 | 3 | 26% | -0.472% | -1.572% | -1.727% | -15.21 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 918.35 € (-0.64%) | 15 | 10 | 20% | -0.611% | -1.711% | -1.842% | -5.93 € |
| macd_momentum_evento | 915.90 € (-0.90%) | 30 | 3 | 20% | -0.111% | -1.211% | -1.344% | -8.36 € |
| ruptura_volumen_evento | 913.96 € (-1.11%) | 24 | 2 | 8% | -0.746% | -1.846% | -1.960% | -10.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 19:35 | c_banda_atr_evento | ICP | timeout | -0.89% | -1.99% | -0.46 |
| 2026-09-30 19:35 | c_banda_atr_evento | UNI | timeout | +0.54% | -0.56% | -0.13 |
| 2026-09-30 19:35 | c_banda_atr_tope | ICP | timeout | -0.89% | -1.99% | -0.46 |
| 2026-09-30 19:35 | c_banda_atr_tope | UNI | timeout | +0.54% | -0.56% | -0.13 |
| 2026-09-30 19:35 | c_banda_atr | ICP | timeout | -0.89% | -1.69% | -0.39 |
| 2026-09-30 19:35 | c_banda_atr | UNI | timeout | +0.54% | -0.26% | -0.06 |
| 2026-09-30 19:30 | macd_momentum_evento | TON | momentum perdido | -0.74% | -1.84% | -0.42 |
| 2026-09-30 19:30 | macd_momentum_evento | HYPE | momentum perdido | -0.29% | -1.39% | -0.32 |
| 2026-09-30 19:30 | macd_momentum | TON | momentum perdido | -0.74% | -1.24% | -0.28 |
| 2026-09-30 19:30 | macd_momentum | HYPE | momentum perdido | -0.29% | -0.79% | -0.18 |
| 2026-09-30 19:20 | ruptura_volumen_evento | MON | timeout | +0.20% | -0.90% | -0.21 |
| 2026-09-30 19:20 | ruptura_volumen_evento | ALGO | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 19:20 | macd_momentum_evento | XMR | momentum perdido | +0.00% | -1.10% | -0.25 |
| 2026-09-30 19:20 | macd_momentum_evento | BNB | momentum perdido | -0.26% | -1.36% | -0.31 |
| 2026-09-30 19:20 | ruptura_volumen_regimen | MON | timeout | +0.20% | -0.30% | -0.07 |

## Eventos de la última vuelta

- 2026-09-30 19:35 [c_banda_atr] CIERRE UNI timeout bruto +0.54% neto -0.26%
- 2026-09-30 19:35 [c_banda_atr_tope] CIERRE UNI timeout bruto +0.54% neto -0.56%
- 2026-09-30 19:35 [c_banda_atr_evento] CIERRE UNI timeout bruto +0.54% neto -0.56%
- 2026-09-30 19:35 [c_banda_atr] CIERRE ICP timeout bruto -0.89% neto -1.69%
- 2026-09-30 19:35 [c_banda_atr_tope] CIERRE ICP timeout bruto -0.89% neto -1.99%
- 2026-09-30 19:35 [c_banda_atr_evento] CIERRE ICP timeout bruto -0.89% neto -1.99%
- 2026-09-30 19:30 [estocastico_rebote] ENTRADA NIGHT @ 0.03304 (22.69 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
