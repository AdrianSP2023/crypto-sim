# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 10:56 UTC · vueltas 16 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 923.72 € (-0.06%) | 1 | 6 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| reversion_bb | 924.23 € (-0.00%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen | 922.05 € (-0.24%) | 3 | 15 | 0% | -1.225% | -2.325% | -2.449% | -1.61 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 921.81 € (-0.26%) | 5 | 9 | 0% | -0.900% | -2.000% | -2.080% | -2.31 € |
| macd_momentum | 912.74 € (-1.24%) | 38 | 3 | 5% | -0.247% | -1.347% | -1.455% | -11.83 € |
| estocastico_rebote | 923.75 € (-0.05%) | 2 | 12 | 50% | +0.150% | -0.950% | -1.119% | -0.44 € |
| ruptura_estricta | 922.50 € (-0.19%) | 1 | 12 | 0% | -2.000% | -3.100% | -3.312% | -0.72 € |
| macd_sin_salida | 920.41 € (-0.41%) | 5 | 34 | 60% | +0.600% | -0.500% | -0.690% | -0.58 € |
| c_banda_atr_tope | 923.88 € (-0.04%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 922.89 € (-0.15%) | 2 | 5 | 0% | -1.238% | -2.338% | -2.482% | -1.08 € |
| c_banda_atr_regimen | 923.72 € (-0.06%) | 1 | 6 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| macd_momentum_regimen | 912.74 € (-1.24%) | 38 | 3 | 5% | -0.247% | -1.347% | -1.455% | -11.83 € |
| ruptura_volumen_regimen | 922.05 € (-0.24%) | 3 | 15 | 0% | -1.225% | -2.325% | -2.449% | -1.61 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-29 10:45 | macd_momentum_regimen | ZRO | momentum perdido | -0.07% | -1.17% | -0.27 |
| 2026-09-29 10:45 | macd_momentum_regimen | AVAX | momentum perdido | -0.63% | -1.73% | -0.40 |
| 2026-09-29 10:45 | ruptura_volumen_tope | PENGU | stop-loss | -1.28% | -2.38% | -0.55 |
| 2026-09-29 10:45 | macd_sin_salida | XDC | take-profit | +2.00% | +0.90% | +0.21 |

## Eventos de la última vuelta

- 2026-09-29 10:50 [macd_momentum] ENTRADA QNT @ 228.77 (22.82 €, apertura)
- 2026-09-29 10:50 [macd_sin_salida] ENTRADA QNT @ 228.77 (23.09 €, apertura)
- 2026-09-29 10:50 [macd_momentum_regimen] ENTRADA QNT @ 228.77 (22.82 €, apertura)
- 2026-09-29 10:50 [estocastico_rebote] ENTRADA CRV @ 0.34756 (23.10 €, apertura)
- 2026-09-29 10:50 [c_banda_atr] ENTRADA MON @ 0.02558 (23.11 €, apertura)
- 2026-09-29 10:50 [c_banda_atr_tope] ENTRADA MON @ 0.02558 (23.11 €, apertura)
- 2026-09-29 10:50 [c_banda_atr_regimen] ENTRADA MON @ 0.02558 (23.11 €, apertura)
- 2026-09-29 10:55 [macd_momentum] CIERRE VIRTUAL momentum perdido bruto -0.04% neto -1.14%
- 2026-09-29 10:55 [macd_momentum_regimen] CIERRE VIRTUAL momentum perdido bruto -0.04% neto -1.14%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
