# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 19:51 UTC · vueltas 63 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.55 € (-1.70%) | 48 | 17 | 27% | -0.388% | -1.419% | -1.570% | -15.69 € |
| reversion_bb | 922.70 € (-0.17%) | 7 | 5 | 57% | +0.214% | -0.886% | -1.014% | -1.44 € |
| ruptura_volumen | 898.59 € (-2.77%) | 74 | 3 | 14% | -0.665% | -1.518% | -1.656% | -25.76 € |
| rebote_extremo | 924.24 € (+0.00%) | 2 | 1 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 905.93 € (-1.98%) | 55 | 2 | 15% | -0.474% | -1.454% | -1.595% | -18.35 € |
| macd_momentum | 909.02 € (-1.65%) | 77 | 5 | 27% | -0.026% | -0.865% | -1.001% | -15.32 € |
| estocastico_rebote | 907.05 € (-1.86%) | 91 | 29 | 40% | +0.008% | -0.779% | -0.910% | -16.35 € |
| ruptura_estricta | 899.25 € (-2.70%) | 45 | 3 | 9% | -1.346% | -2.426% | -2.575% | -25.13 € |
| macd_sin_salida | 905.63 € (-2.01%) | 64 | 11 | 33% | -0.313% | -1.221% | -1.360% | -18.01 € |
| c_banda_atr_tope | 921.62 € (-0.28%) | 13 | 5 | 38% | +0.095% | -1.005% | -1.154% | -3.02 € |
| ruptura_volumen_tope | 918.42 € (-0.63%) | 18 | 3 | 22% | -0.331% | -1.431% | -1.522% | -5.94 € |
| c_banda_atr_regimen | 909.06 € (-1.64%) | 42 | 3 | 26% | -0.472% | -1.572% | -1.727% | -15.21 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 918.48 € (-0.62%) | 15 | 17 | 20% | -0.611% | -1.711% | -1.842% | -5.93 € |
| macd_momentum_evento | 915.99 € (-0.89%) | 30 | 5 | 20% | -0.111% | -1.211% | -1.344% | -8.36 € |
| ruptura_volumen_evento | 914.13 € (-1.09%) | 24 | 3 | 8% | -0.746% | -1.846% | -1.960% | -10.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-30 19:30 | macd_momentum | TON | momentum perdido | -0.74% | -1.24% | -0.28 |
| 2026-09-30 19:30 | macd_momentum | HYPE | momentum perdido | -0.29% | -0.79% | -0.18 |
| 2026-09-30 19:20 | ruptura_volumen_evento | MON | timeout | +0.20% | -0.90% | -0.21 |
| 2026-09-30 19:20 | ruptura_volumen_evento | ALGO | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 19:20 | macd_momentum_evento | XMR | momentum perdido | +0.00% | -1.10% | -0.25 |

## Eventos de la última vuelta

- 2026-09-30 19:50 [estocastico_rebote] CIERRE HBAR take-profit bruto +1.80% neto +1.30%
- 2026-09-30 19:45 [ruptura_volumen] ENTRADA CRV @ 0.34557 (22.46 €, apertura)
- 2026-09-30 19:45 [ruptura_estricta] ENTRADA CRV @ 0.34557 (22.48 €, apertura)
- 2026-09-30 19:45 [ruptura_volumen_tope] ENTRADA CRV @ 0.34557 (22.96 €, apertura)
- 2026-09-30 19:45 [ruptura_volumen_evento] ENTRADA CRV @ 0.34557 (22.85 €, apertura)
- 2026-09-30 19:45 [c_banda_atr] ENTRADA OP @ 0.1143 (22.71 €, apertura)
- 2026-09-30 19:45 [c_banda_atr_evento] ENTRADA OP @ 0.1143 (22.96 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
