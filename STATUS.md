# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 10:01 UTC · vueltas 206 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 895.22 € (-3.14%) | 161 | 24 | 29% | -0.161% | -0.823% | -0.951% | -30.28 € |
| reversion_bb | 915.13 € (-0.99%) | 43 | 3 | 42% | +0.124% | -0.962% | -1.072% | -9.52 € |
| ruptura_volumen | 886.02 € (-4.14%) | 194 | 27 | 20% | -0.244% | -0.879% | -1.008% | -38.68 € |
| rebote_extremo | 923.34 € (-0.10%) | 10 | 0 | 60% | +0.710% | -0.389% | -0.540% | -0.90 € |
| pullback_tendencia | 901.48 € (-2.46%) | 124 | 5 | 23% | -0.093% | -0.804% | -0.930% | -22.80 € |
| macd_momentum | 875.11 € (-5.32%) | 351 | 21 | 17% | -0.068% | -0.643% | -0.754% | -50.83 € |
| estocastico_rebote | 887.80 € (-3.94%) | 234 | 7 | 37% | -0.077% | -0.688% | -0.821% | -36.70 € |
| ruptura_estricta | 901.95 € (-2.41%) | 81 | 18 | 22% | -0.396% | -1.218% | -1.368% | -22.60 € |
| macd_sin_salida | 889.23 € (-3.79%) | 217 | 29 | 29% | -0.121% | -0.741% | -0.862% | -36.56 € |
| c_banda_atr_tope | 909.95 € (-1.55%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.18 € (-1.74%) | 70 | 5 | 20% | -0.118% | -0.995% | -1.117% | -15.97 € |
| c_banda_atr_regimen | 900.62 € (-2.56%) | 78 | 6 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 884.64 € (-4.28%) | 207 | 8 | 14% | -0.216% | -0.843% | -0.956% | -39.57 € |
| ruptura_volumen_regimen | 893.93 € (-3.28%) | 133 | 24 | 17% | -0.291% | -0.987% | -1.115% | -29.91 € |
| c_banda_atr_evento | 898.27 € (-2.81%) | 129 | 24 | 26% | -0.218% | -0.922% | -1.051% | -27.23 € |
| macd_momentum_evento | 887.42 € (-3.98%) | 231 | 21 | 15% | -0.121% | -0.735% | -0.844% | -38.55 € |
| ruptura_volumen_evento | 891.48 € (-3.54%) | 135 | 27 | 15% | -0.385% | -1.081% | -1.211% | -33.22 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 10:00 | ruptura_volumen_evento | ENA | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 10:00 | macd_momentum_evento | SPX | momentum perdido | -0.82% | -1.32% | -0.29 |
| 2026-09-30 10:00 | macd_momentum_evento | ATOM | momentum perdido | +0.05% | -0.45% | -0.10 |
| 2026-09-30 10:00 | macd_momentum_evento | INJ | momentum perdido | +0.16% | -0.34% | -0.07 |
| 2026-09-30 10:00 | macd_momentum_evento | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 10:00 | ruptura_volumen_regimen | ENA | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 10:00 | macd_momentum_regimen | SPX | momentum perdido | -0.82% | -1.32% | -0.29 |
| 2026-09-30 10:00 | macd_momentum_regimen | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 10:00 | ruptura_volumen_tope | ENA | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 10:00 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 10:00 | estocastico_rebote | VIRTUAL | timeout | +0.80% | +0.30% | +0.07 |
| 2026-09-30 10:00 | estocastico_rebote | ZRO | stop-loss | -1.72% | -2.22% | -0.49 |
| 2026-09-30 10:00 | macd_momentum | SPX | momentum perdido | -0.82% | -1.32% | -0.29 |
| 2026-09-30 10:00 | macd_momentum | ATOM | momentum perdido | +0.05% | -0.45% | -0.10 |
| 2026-09-30 10:00 | macd_momentum | INJ | momentum perdido | +0.16% | -0.34% | -0.07 |

## Eventos de la última vuelta

- 2026-09-30 09:55 [estocastico_rebote] ENTRADA XDC @ 0.03033 (22.20 €, apertura)
- 2026-09-30 10:00 [ruptura_volumen] CIERRE ENA stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 10:00 [ruptura_volumen_tope] CIERRE ENA stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 10:00 [ruptura_volumen_regimen] CIERRE ENA stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 10:00 [ruptura_volumen_evento] CIERRE ENA stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 09:55 [ruptura_volumen] ENTRADA MON @ 0.02437 (22.14 €, apertura)
- 2026-09-30 10:00 [macd_momentum] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 10:00 [macd_sin_salida] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:55 [ruptura_volumen_tope] ENTRADA MON @ 0.02437 (22.71 €, apertura)
- 2026-09-30 10:00 [macd_momentum_regimen] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:55 [ruptura_volumen_regimen] ENTRADA MON @ 0.02437 (22.36 €, apertura)
- 2026-09-30 10:00 [macd_momentum_evento] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:55 [ruptura_volumen_evento] ENTRADA MON @ 0.02437 (22.28 €, apertura)
- 2026-09-30 10:00 [macd_momentum] CIERRE INJ momentum perdido bruto +0.16% neto -0.34%
- 2026-09-30 10:00 [macd_momentum_evento] CIERRE INJ momentum perdido bruto +0.16% neto -0.34%
- 2026-09-30 10:00 [macd_momentum] CIERRE ATOM momentum perdido bruto +0.05% neto -0.45%
- 2026-09-30 10:00 [macd_momentum_evento] CIERRE ATOM momentum perdido bruto +0.05% neto -0.45%
- 2026-09-30 10:00 [estocastico_rebote] CIERRE ZRO stop-loss bruto -1.72% neto -2.22%
- 2026-09-30 10:00 [estocastico_rebote] CIERRE VIRTUAL timeout bruto +0.80% neto +0.30%
- 2026-09-30 10:00 [macd_momentum] CIERRE SPX momentum perdido bruto -0.82% neto -1.32%
- 2026-09-30 10:00 [macd_momentum_regimen] CIERRE SPX momentum perdido bruto -0.82% neto -1.32%
- 2026-09-30 10:00 [macd_momentum_evento] CIERRE SPX momentum perdido bruto -0.82% neto -1.32%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
