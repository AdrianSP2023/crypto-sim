# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 14:32 UTC · vueltas 58 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 917.62 € (-0.72%) | 26 | 20 | 42% | +0.056% | -1.044% | -1.182% | -6.27 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 914.25 € (-1.08%) | 54 | 7 | 28% | +0.097% | -0.876% | -1.007% | -10.90 € |
| rebote_extremo | 924.34 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 915.95 € (-0.90%) | 43 | 11 | 30% | +0.138% | -0.941% | -1.048% | -9.33 € |
| macd_momentum | 905.50 € (-2.03%) | 120 | 7 | 21% | +0.035% | -0.682% | -0.798% | -18.81 € |
| estocastico_rebote | 919.62 € (-0.50%) | 54 | 36 | 54% | +0.584% | -0.349% | -0.472% | -4.36 € |
| ruptura_estricta | 919.71 € (-0.49%) | 26 | 11 | 35% | +0.148% | -0.952% | -1.082% | -5.72 € |
| macd_sin_salida | 915.30 € (-0.97%) | 62 | 20 | 39% | +0.287% | -0.610% | -0.734% | -8.70 € |
| c_banda_atr_tope | 920.19 € (-0.44%) | 11 | 4 | 27% | -0.397% | -1.497% | -1.686% | -3.80 € |
| ruptura_volumen_tope | 922.63 € (-0.17%) | 13 | 5 | 23% | +0.215% | -0.885% | -1.016% | -2.66 € |
| c_banda_atr_regimen | 917.62 € (-0.72%) | 26 | 20 | 42% | +0.056% | -1.044% | -1.182% | -6.27 € |
| macd_momentum_regimen | 905.50 € (-2.03%) | 120 | 7 | 21% | +0.035% | -0.682% | -0.798% | -18.81 € |
| ruptura_volumen_regimen | 914.25 € (-1.08%) | 54 | 7 | 28% | +0.097% | -0.876% | -1.007% | -10.90 € |
| c_banda_atr_evento | 923.78 € (-0.05%) | 0 | 8 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 924.35 € (+0.01%) | 0 | 7 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen_evento | 924.20 € (-0.00%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 14:30 | macd_momentum_regimen | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:30 | macd_sin_salida | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:30 | estocastico_rebote | RAY | timeout | +0.94% | +0.14% | +0.03 |
| 2026-09-29 14:30 | macd_momentum | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:25 | macd_momentum_regimen | ASTER | momentum perdido | -0.60% | -1.10% | -0.25 |
| 2026-09-29 14:25 | c_banda_atr_regimen | FET | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:25 | c_banda_atr_tope | FET | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:25 | macd_sin_salida | FIL | timeout | +0.21% | -0.59% | -0.14 |
| 2026-09-29 14:25 | estocastico_rebote | FET | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-29 14:25 | macd_momentum | ASTER | momentum perdido | -0.60% | -1.10% | -0.25 |
| 2026-09-29 14:25 | c_banda_atr | FET | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:20 | ruptura_volumen_regimen | SHIB | timeout | +0.51% | -0.29% | -0.07 |
| 2026-09-29 14:20 | macd_momentum_regimen | TAO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 14:20 | macd_momentum_regimen | NEAR | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:20 | c_banda_atr_regimen | TAO | stop-loss | -1.50% | -2.60% | -0.60 |

## Eventos de la última vuelta

- 2026-09-29 14:25 [estocastico_rebote] ENTRADA ONDO @ 0.45453 (23.00 €, apertura)
- 2026-09-29 14:25 [estocastico_rebote] ENTRADA BCH @ 274.35 (23.00 €, apertura)
- 2026-09-29 14:25 [estocastico_rebote] ENTRADA VIRTUAL @ 0.7215 (23.00 €, apertura)
- 2026-09-29 14:25 [ruptura_volumen] ENTRADA RAY @ 1.712 (22.83 €, apertura)
- 2026-09-29 14:25 [macd_momentum] ENTRADA RAY @ 1.712 (22.63 €, apertura)
- 2026-09-29 14:30 [estocastico_rebote] CIERRE RAY timeout bruto +0.95% neto +0.15%
- 2026-09-29 14:25 [macd_momentum_regimen] ENTRADA RAY @ 1.712 (22.63 €, apertura)
- 2026-09-29 14:25 [ruptura_volumen_regimen] ENTRADA RAY @ 1.712 (22.83 €, apertura)
- 2026-09-29 14:25 [c_banda_atr_evento] ENTRADA RAY @ 1.712 (23.11 €, apertura)
- 2026-09-29 14:25 [macd_momentum_evento] ENTRADA RAY @ 1.712 (23.11 €, apertura)
- 2026-09-29 14:25 [ruptura_volumen_evento] ENTRADA RAY @ 1.712 (23.11 €, apertura)
- 2026-09-29 14:30 [macd_momentum] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:30 [macd_sin_salida] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:30 [macd_momentum_regimen] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:25 [estocastico_rebote] ENTRADA PENGU @ 0.008769 (23.00 €, apertura)
- 2026-09-29 14:25 [estocastico_rebote] ENTRADA BNB @ 673.56 (23.00 €, apertura)
- 2026-09-29 14:25 [estocastico_rebote] ENTRADA SPX @ 0.3658 (23.00 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
