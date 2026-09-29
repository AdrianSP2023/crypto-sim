# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 12:36 UTC · vueltas 36 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 925.67 € (+0.15%) | 8 | 24 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| reversion_bb | 923.64 € (-0.07%) | 1 | 0 | 0% | -1.500% | -2.600% | -2.784% | -0.60 € |
| ruptura_volumen | 919.01 € (-0.57%) | 32 | 19 | 38% | +0.491% | -0.609% | -0.742% | -4.50 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 923.35 € (-0.10%) | 17 | 11 | 47% | +0.530% | -0.570% | -0.686% | -2.24 € |
| macd_momentum | 911.56 € (-1.37%) | 75 | 15 | 17% | +0.049% | -0.799% | -0.910% | -13.82 € |
| estocastico_rebote | 927.01 € (+0.30%) | 21 | 29 | 81% | +1.185% | +0.085% | -0.060% | +0.42 € |
| ruptura_estricta | 924.37 € (+0.01%) | 8 | 23 | 50% | +0.552% | -0.548% | -0.733% | -1.01 € |
| macd_sin_salida | 923.71 € (-0.06%) | 22 | 33 | 68% | +0.902% | -0.198% | -0.344% | -1.01 € |
| c_banda_atr_tope | 924.70 € (+0.05%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 922.99 € (-0.13%) | 9 | 3 | 33% | +0.563% | -0.537% | -0.664% | -1.12 € |
| c_banda_atr_regimen | 925.67 € (+0.15%) | 8 | 24 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| macd_momentum_regimen | 911.56 € (-1.37%) | 75 | 15 | 17% | +0.049% | -0.799% | -0.910% | -13.82 € |
| ruptura_volumen_regimen | 919.01 € (-0.57%) | 32 | 19 | 38% | +0.491% | -0.609% | -0.742% | -4.50 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 12:35 | ruptura_volumen_regimen | POL | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 12:35 | macd_momentum_regimen | BNB | momentum perdido | -0.14% | -0.64% | -0.14 |
| 2026-09-29 12:35 | macd_momentum_regimen | OP | momentum perdido | +0.85% | +0.35% | +0.08 |
| 2026-09-29 12:35 | ruptura_estricta | HBAR | stop-loss | -2.00% | -3.10% | -0.72 |
| 2026-09-29 12:35 | estocastico_rebote | XRP | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-29 12:35 | macd_momentum | BNB | momentum perdido | -0.14% | -0.64% | -0.14 |
| 2026-09-29 12:35 | macd_momentum | OP | momentum perdido | +0.85% | +0.35% | +0.08 |
| 2026-09-29 12:35 | pullback_tendencia | TAO | rotura de tendencia | -0.31% | -1.41% | -0.33 |
| 2026-09-29 12:35 | ruptura_volumen | POL | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 12:30 | ruptura_volumen_regimen | OP | stop-loss | -1.26% | -2.36% | -0.54 |
| 2026-09-29 12:30 | ruptura_volumen_regimen | XDC | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 12:30 | ruptura_volumen_regimen | UNI | stop-loss | -1.30% | -2.40% | -0.55 |
| 2026-09-29 12:30 | macd_momentum_regimen | TRX | momentum perdido | -0.03% | -0.53% | -0.12 |
| 2026-09-29 12:30 | macd_momentum_regimen | BCH | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-09-29 12:30 | macd_momentum_regimen | JUP | momentum perdido | +0.12% | -0.38% | -0.09 |

## Eventos de la última vuelta

- 2026-09-29 12:35 [estocastico_rebote] CIERRE XRP take-profit bruto +1.80% neto +0.70%
- 2026-09-29 12:35 [ruptura_estricta] CIERRE HBAR stop-loss bruto -2.00% neto -3.10%
- 2026-09-29 12:35 [pullback_tendencia] CIERRE TAO rotura de tendencia bruto -0.31% neto -1.41%
- 2026-09-29 12:30 [estocastico_rebote] ENTRADA VVV @ 24.26 (23.12 €, apertura)
- 2026-09-29 12:35 [macd_momentum] CIERRE OP momentum perdido bruto +0.86% neto +0.36%
- 2026-09-29 12:35 [macd_momentum_regimen] CIERRE OP momentum perdido bruto +0.86% neto +0.36%
- 2026-09-29 12:30 [pullback_tendencia] ENTRADA NIGHT @ 0.02718 (23.05 €, apertura)
- 2026-09-29 12:35 [ruptura_volumen] CIERRE POL take-profit bruto +2.50% neto +1.40%
- 2026-09-29 12:30 [ruptura_estricta] ENTRADA POL @ 0.10923 (23.08 €, apertura)
- 2026-09-29 12:35 [ruptura_volumen_regimen] CIERRE POL take-profit bruto +2.50% neto +1.40%
- 2026-09-29 12:35 [macd_momentum] CIERRE BNB momentum perdido bruto -0.14% neto -0.64%
- 2026-09-29 12:35 [macd_momentum_regimen] CIERRE BNB momentum perdido bruto -0.14% neto -0.64%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
