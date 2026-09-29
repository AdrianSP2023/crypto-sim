# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 11:01 UTC · vueltas 17 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 923.82 € (-0.05%) | 1 | 9 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| reversion_bb | 924.23 € (-0.00%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen | 921.81 € (-0.26%) | 3 | 15 | 0% | -1.225% | -2.325% | -2.449% | -1.61 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 921.10 € (-0.34%) | 6 | 9 | 0% | -1.000% | -2.100% | -2.225% | -2.91 € |
| macd_momentum | 912.18 € (-1.31%) | 39 | 2 | 5% | -0.279% | -1.379% | -1.495% | -12.42 € |
| estocastico_rebote | 923.92 € (-0.03%) | 2 | 27 | 50% | +0.150% | -0.950% | -1.119% | -0.44 € |
| ruptura_estricta | 922.32 € (-0.21%) | 1 | 12 | 0% | -2.000% | -3.100% | -3.312% | -0.72 € |
| macd_sin_salida | 919.98 € (-0.46%) | 6 | 33 | 50% | +0.250% | -0.850% | -1.072% | -1.18 € |
| c_banda_atr_tope | 923.96 € (-0.03%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 922.83 € (-0.15%) | 2 | 5 | 0% | -1.238% | -2.338% | -2.482% | -1.08 € |
| c_banda_atr_regimen | 923.82 € (-0.05%) | 1 | 9 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| macd_momentum_regimen | 912.18 € (-1.31%) | 39 | 2 | 5% | -0.279% | -1.379% | -1.495% | -12.42 € |
| ruptura_volumen_regimen | 921.81 € (-0.26%) | 3 | 15 | 0% | -1.225% | -2.325% | -2.449% | -1.61 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 11:00 | macd_momentum_regimen | QNT | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 11:00 | macd_sin_salida | QNT | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 11:00 | macd_momentum | QNT | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 11:00 | pullback_tendencia | QNT | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 10:55 | macd_momentum_regimen | VIRTUAL | momentum perdido | -0.04% | -1.14% | -0.26 |
| 2026-09-29 10:55 | macd_momentum | VIRTUAL | momentum perdido | -0.04% | -1.14% | -0.26 |
| 2026-09-29 10:50 | ruptura_volumen_regimen | SPX | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 10:50 | macd_momentum_regimen | NIGHT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 10:50 | macd_sin_salida | NIGHT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 10:50 | macd_momentum | NIGHT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 10:50 | ruptura_volumen | SPX | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 10:45 | ruptura_volumen_regimen | PENGU | stop-loss | -1.28% | -2.38% | -0.55 |
| 2026-09-29 10:45 | macd_momentum_regimen | SPX | momentum perdido | -1.20% | -2.30% | -0.53 |
| 2026-09-29 10:45 | macd_momentum_regimen | SEI | momentum perdido | -0.08% | -1.18% | -0.27 |
| 2026-09-29 10:45 | macd_momentum_regimen | USELESS | momentum perdido | -0.80% | -1.90% | -0.44 |

## Eventos de la última vuelta

- 2026-09-29 10:55 [estocastico_rebote] ENTRADA XRP @ 1.32793 (23.10 €, apertura)
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA SOL @ 105.21 (23.10 €, apertura)
- 2026-09-29 11:00 [pullback_tendencia] CIERRE QNT stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 11:00 [macd_momentum] CIERRE QNT stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 11:00 [macd_sin_salida] CIERRE QNT stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 11:00 [macd_momentum_regimen] CIERRE QNT stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA XLM @ 0.202507 (23.10 €, apertura)
- 2026-09-29 10:55 [pullback_tendencia] ENTRADA AVAX @ 10.213 (23.03 €, apertura)
- 2026-09-29 10:55 [c_banda_atr] ENTRADA AAVE @ 148.06 (23.11 €, apertura)
- 2026-09-29 10:55 [c_banda_atr_regimen] ENTRADA AAVE @ 148.06 (23.11 €, apertura)
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA UNI @ 7.9721 (23.10 €, apertura)
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA HYPE @ 77.87 (23.10 €, apertura)
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA DOGE @ 0.0837607 (23.10 €, apertura)
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA DOT @ 1.0649 (23.10 €, apertura)
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA BCH @ 275.02 (23.10 €, apertura)
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA INJ @ 6.671 (23.10 €, apertura)
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA WLD @ 0.439 (23.10 €, apertura)
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA PEPE @ 3.761e-06 (23.10 €, apertura)
- 2026-09-29 10:55 [c_banda_atr] ENTRADA RAY @ 1.687 (23.11 €, apertura)
- 2026-09-29 10:55 [c_banda_atr_regimen] ENTRADA RAY @ 1.687 (23.11 €, apertura)
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA FIL @ 0.946 (23.10 €, apertura)
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA SHIB @ 5.098e-06 (23.10 €, apertura)
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA TON @ 1.387 (23.10 €, apertura)
- 2026-09-29 10:55 [estocastico_rebote] ENTRADA PENGU @ 0.008458 (23.10 €, apertura)
- 2026-09-29 10:55 [c_banda_atr] ENTRADA ASTER @ 0.63864 (23.11 €, apertura)
- 2026-09-29 10:55 [c_banda_atr_regimen] ENTRADA ASTER @ 0.63864 (23.11 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
