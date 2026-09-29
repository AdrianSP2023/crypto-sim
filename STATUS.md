# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 14:22 UTC · vueltas 56 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 917.76 € (-0.70%) | 25 | 15 | 44% | +0.119% | -0.981% | -1.116% | -5.67 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 914.41 € (-1.06%) | 54 | 6 | 28% | +0.097% | -0.876% | -1.007% | -10.90 € |
| rebote_extremo | 924.29 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 915.47 € (-0.95%) | 43 | 9 | 30% | +0.138% | -0.941% | -1.048% | -9.33 € |
| macd_momentum | 905.39 € (-2.04%) | 118 | 3 | 20% | +0.024% | -0.697% | -0.813% | -18.90 € |
| estocastico_rebote | 919.96 € (-0.46%) | 52 | 20 | 54% | +0.617% | -0.321% | -0.436% | -3.86 € |
| ruptura_estricta | 919.55 € (-0.51%) | 26 | 11 | 35% | +0.148% | -0.952% | -1.082% | -5.72 € |
| macd_sin_salida | 914.69 € (-1.03%) | 60 | 19 | 38% | +0.259% | -0.646% | -0.770% | -8.90 € |
| c_banda_atr_tope | 920.72 € (-0.38%) | 10 | 3 | 30% | -0.286% | -1.386% | -1.570% | -3.20 € |
| ruptura_volumen_tope | 922.84 € (-0.15%) | 13 | 5 | 23% | +0.215% | -0.885% | -1.016% | -2.66 € |
| c_banda_atr_regimen | 917.76 € (-0.70%) | 25 | 15 | 44% | +0.119% | -0.981% | -1.116% | -5.67 € |
| macd_momentum_regimen | 905.39 € (-2.04%) | 118 | 3 | 20% | +0.024% | -0.697% | -0.813% | -18.90 € |
| ruptura_volumen_regimen | 914.41 € (-1.06%) | 54 | 6 | 28% | +0.097% | -0.876% | -1.007% | -10.90 € |
| c_banda_atr_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 14:20 | ruptura_volumen_regimen | SHIB | timeout | +0.51% | -0.29% | -0.07 |
| 2026-09-29 14:20 | macd_momentum_regimen | TAO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 14:20 | macd_momentum_regimen | NEAR | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:20 | c_banda_atr_regimen | TAO | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:20 | c_banda_atr_tope | TAO | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:20 | macd_sin_salida | NEAR | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:20 | macd_sin_salida | ZEC | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 14:20 | macd_momentum | TAO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 14:20 | macd_momentum | NEAR | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:20 | ruptura_volumen | SHIB | timeout | +0.51% | -0.29% | -0.07 |
| 2026-09-29 14:20 | c_banda_atr | TAO | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:15 | macd_momentum_regimen | FET | stop-loss | -1.58% | -2.08% | -0.47 |
| 2026-09-29 14:15 | macd_momentum_regimen | VIRTUAL | momentum perdido | -0.89% | -1.39% | -0.31 |
| 2026-09-29 14:15 | macd_momentum_regimen | DASH | momentum perdido | -0.14% | -0.64% | -0.14 |
| 2026-09-29 14:15 | macd_momentum_regimen | UNI | momentum perdido | +0.02% | -0.48% | -0.11 |

## Eventos de la última vuelta

- 2026-09-29 14:15 [estocastico_rebote] ENTRADA QNT @ 221.63 (23.01 €, apertura)
- 2026-09-29 14:20 [macd_sin_salida] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 14:20 [macd_momentum] CIERRE NEAR take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:20 [macd_sin_salida] CIERRE NEAR take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:20 [macd_momentum_regimen] CIERRE NEAR take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:20 [c_banda_atr] CIERRE TAO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 14:20 [macd_momentum] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 14:20 [c_banda_atr_tope] CIERRE TAO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 14:20 [c_banda_atr_regimen] CIERRE TAO stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 14:20 [macd_momentum_regimen] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 14:15 [pullback_tendencia] ENTRADA INJ @ 6.802 (22.87 €, apertura)
- 2026-09-29 14:15 [pullback_tendencia] ENTRADA ZRO @ 1.45 (22.87 €, apertura)
- 2026-09-29 14:20 [ruptura_volumen] CIERRE SHIB timeout bruto +0.51% neto -0.29%
- 2026-09-29 14:20 [ruptura_volumen_regimen] CIERRE SHIB timeout bruto +0.51% neto -0.29%
- 2026-09-29 14:15 [pullback_tendencia] ENTRADA TRUMP @ 1.829 (22.87 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
