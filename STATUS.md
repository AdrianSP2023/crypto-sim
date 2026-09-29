# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 10:51 UTC · vueltas 15 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 923.54 € (-0.08%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| reversion_bb | 924.25 € (+0.00%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen | 921.48 € (-0.30%) | 3 | 15 | 0% | -1.225% | -2.325% | -2.449% | -1.61 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 921.84 € (-0.26%) | 5 | 9 | 0% | -0.900% | -2.000% | -2.080% | -2.31 € |
| macd_momentum | 913.12 € (-1.20%) | 37 | 3 | 5% | -0.253% | -1.353% | -1.456% | -11.56 € |
| estocastico_rebote | 923.36 € (-0.10%) | 2 | 11 | 50% | +0.150% | -0.950% | -1.119% | -0.44 € |
| ruptura_estricta | 921.97 € (-0.25%) | 1 | 12 | 0% | -2.000% | -3.100% | -3.312% | -0.72 € |
| macd_sin_salida | 919.55 € (-0.51%) | 5 | 33 | 60% | +0.600% | -0.500% | -0.690% | -0.58 € |
| c_banda_atr_tope | 923.76 € (-0.05%) | 1 | 4 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 922.81 € (-0.15%) | 2 | 5 | 0% | -1.238% | -2.338% | -2.482% | -1.08 € |
| c_banda_atr_regimen | 923.54 € (-0.08%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| macd_momentum_regimen | 913.12 € (-1.20%) | 37 | 3 | 5% | -0.253% | -1.353% | -1.456% | -11.56 € |
| ruptura_volumen_regimen | 921.48 € (-0.30%) | 3 | 15 | 0% | -1.225% | -2.325% | -2.449% | -1.61 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-29 10:45 | macd_momentum | SPX | momentum perdido | -1.20% | -2.30% | -0.53 |
| 2026-09-29 10:45 | macd_momentum | SEI | momentum perdido | -0.08% | -1.18% | -0.27 |

## Eventos de la última vuelta

- 2026-09-29 10:45 [pullback_tendencia] ENTRADA QNT @ 226.58 (23.05 €, apertura)
- 2026-09-29 10:45 [estocastico_rebote] ENTRADA ADA @ 0.220826 (23.10 €, apertura)
- 2026-09-29 10:45 [ruptura_volumen_tope] ENTRADA XDC @ 0.03227 (23.08 €, apertura)
- 2026-09-29 10:50 [macd_momentum] CIERRE NIGHT take-profit bruto +2.00% neto +0.90%
- 2026-09-29 10:50 [macd_sin_salida] CIERRE NIGHT take-profit bruto +2.00% neto +0.90%
- 2026-09-29 10:50 [macd_momentum_regimen] CIERRE NIGHT take-profit bruto +2.00% neto +0.90%
- 2026-09-29 10:45 [estocastico_rebote] ENTRADA KAS @ 0.04057 (23.10 €, apertura)
- 2026-09-29 10:50 [ruptura_volumen] CIERRE SPX stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 10:50 [ruptura_volumen_regimen] CIERRE SPX stop-loss bruto -1.20% neto -2.30%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
