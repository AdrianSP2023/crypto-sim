# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 06:31 UTC · vueltas 225 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 893.33 € (-3.34%) | 128 | 25 | 27% | -0.250% | -0.954% | -1.088% | -27.95 € |
| reversion_bb | 915.81 € (-0.91%) | 35 | 9 | 46% | +0.183% | -0.917% | -1.027% | -7.39 € |
| ruptura_volumen | 887.60 € (-3.96%) | 164 | 13 | 18% | -0.278% | -0.937% | -1.066% | -34.96 € |
| rebote_extremo | 922.91 € (-0.14%) | 7 | 1 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 903.51 € (-2.24%) | 116 | 3 | 25% | -0.046% | -0.771% | -0.898% | -20.49 € |
| macd_momentum | 874.71 € (-5.36%) | 320 | 1 | 16% | -0.105% | -0.687% | -0.797% | -49.59 € |
| estocastico_rebote | 887.65 € (-3.96%) | 211 | 8 | 35% | -0.120% | -0.744% | -0.878% | -35.77 € |
| ruptura_estricta | 902.73 € (-2.33%) | 70 | 10 | 23% | -0.383% | -1.256% | -1.396% | -20.15 € |
| macd_sin_salida | 888.90 € (-3.82%) | 182 | 26 | 29% | -0.150% | -0.794% | -0.921% | -32.90 € |
| c_banda_atr_tope | 909.67 € (-1.58%) | 39 | 2 | 18% | -0.490% | -1.590% | -1.722% | -14.24 € |
| ruptura_volumen_tope | 908.81 € (-1.67%) | 60 | 3 | 17% | -0.164% | -1.104% | -1.225% | -15.20 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.963% | -38.90 € |
| ruptura_volumen_regimen | 896.27 € (-3.03%) | 119 | 7 | 18% | -0.267% | -0.986% | -1.116% | -26.79 € |
| c_banda_atr_evento | 896.37 € (-3.01%) | 96 | 25 | 24% | -0.357% | -1.132% | -1.268% | -24.89 € |
| macd_momentum_evento | 887.01 € (-4.03%) | 200 | 1 | 13% | -0.189% | -0.821% | -0.927% | -37.29 € |
| ruptura_volumen_evento | 893.06 € (-3.37%) | 105 | 13 | 10% | -0.479% | -1.230% | -1.360% | -29.47 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 06:30 | ruptura_volumen_evento | SEI | timeout | +0.09% | -0.41% | -0.09 |
| 2026-09-30 06:30 | ruptura_volumen_evento | INJ | stop-loss | -1.31% | -1.81% | -0.41 |
| 2026-09-30 06:30 | ruptura_volumen_evento | MON | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 06:30 | ruptura_volumen_evento | TAO | timeout | -0.78% | -1.28% | -0.29 |
| 2026-09-30 06:30 | macd_momentum_evento | PEPE | momentum perdido | -0.11% | -0.61% | -0.14 |
| 2026-09-30 06:30 | macd_momentum_evento | XDC | momentum perdido | -0.07% | -0.57% | -0.13 |
| 2026-09-30 06:30 | c_banda_atr_evento | ALGO | stop-loss | -1.55% | -2.05% | -0.46 |
| 2026-09-30 06:30 | c_banda_atr_evento | AVAX | stop-loss | -1.53% | -2.03% | -0.46 |
| 2026-09-30 06:30 | ruptura_volumen_regimen | XPL | stop-loss | -1.74% | -2.24% | -0.50 |
| 2026-09-30 06:30 | macd_momentum_regimen | XDC | momentum perdido | -0.07% | -0.57% | -0.13 |
| 2026-09-30 06:30 | c_banda_atr_tope | DOT | stop-loss | -1.59% | -2.69% | -0.61 |
| 2026-09-30 06:30 | macd_sin_salida | TRUMP | stop-loss | -1.64% | -2.14% | -0.48 |
| 2026-09-30 06:30 | macd_sin_salida | DASH | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:30 | estocastico_rebote | SPX | timeout | -1.05% | -1.55% | -0.34 |
| 2026-09-30 06:30 | estocastico_rebote | USELESS | stop-loss | -1.54% | -2.04% | -0.45 |

## Eventos de la última vuelta

- 2026-09-30 06:25 [ruptura_volumen] ENTRADA QNT @ 258.11 (22.26 €, apertura)
- 2026-09-30 06:25 [ruptura_volumen_tope] ENTRADA QNT @ 258.11 (22.73 €, apertura)
- 2026-09-30 06:25 [ruptura_volumen_evento] ENTRADA QNT @ 258.11 (22.40 €, apertura)
- 2026-09-30 06:25 [reversion_bb] ENTRADA LTC @ 58.75 (22.92 €, apertura)
- 2026-09-30 06:30 [c_banda_atr] CIERRE AVAX stop-loss bruto -1.53% neto -2.03%
- 2026-09-30 06:30 [c_banda_atr_evento] CIERRE AVAX stop-loss bruto -1.53% neto -2.03%
- 2026-09-30 06:30 [c_banda_atr] CIERRE ALGO stop-loss bruto -1.55% neto -2.05%
- 2026-09-30 06:30 [c_banda_atr_evento] CIERRE ALGO stop-loss bruto -1.55% neto -2.05%
- 2026-09-30 06:30 [ruptura_volumen] CIERRE TAO timeout bruto -0.78% neto -1.28%
- 2026-09-30 06:30 [ruptura_volumen_evento] CIERRE TAO timeout bruto -0.78% neto -1.28%
- 2026-09-30 06:30 [macd_momentum] CIERRE XDC momentum perdido bruto -0.07% neto -0.57%
- 2026-09-30 06:30 [macd_momentum_regimen] CIERRE XDC momentum perdido bruto -0.07% neto -0.57%
- 2026-09-30 06:30 [macd_momentum_evento] CIERRE XDC momentum perdido bruto -0.07% neto -0.57%
- 2026-09-30 06:30 [c_banda_atr_tope] CIERRE DOT stop-loss bruto -1.60% neto -2.70%
- 2026-09-30 06:30 [macd_sin_salida] CIERRE DASH stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:30 [ruptura_volumen] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 06:30 [ruptura_volumen_evento] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 06:30 [ruptura_volumen] CIERRE INJ stop-loss bruto -1.31% neto -1.81%
- 2026-09-30 06:30 [ruptura_volumen_evento] CIERRE INJ stop-loss bruto -1.31% neto -1.81%
- 2026-09-30 06:25 [estocastico_rebote] ENTRADA ZRO @ 1.615 (22.23 €, apertura)
- 2026-09-30 06:30 [pullback_tendencia] CIERRE PEPE rotura de tendencia bruto -0.13% neto -0.63%
- 2026-09-30 06:30 [macd_momentum] CIERRE PEPE momentum perdido bruto -0.11% neto -0.61%
- 2026-09-30 06:30 [macd_momentum_evento] CIERRE PEPE momentum perdido bruto -0.11% neto -0.61%
- 2026-09-30 06:30 [estocastico_rebote] CIERRE USELESS stop-loss bruto -1.54% neto -2.04%
- 2026-09-30 06:30 [ruptura_volumen] CIERRE SEI timeout bruto +0.09% neto -0.41%
- 2026-09-30 06:30 [ruptura_volumen_evento] CIERRE SEI timeout bruto +0.09% neto -0.41%
- 2026-09-30 06:30 [macd_sin_salida] CIERRE TRUMP stop-loss bruto -1.64% neto -2.14%
- 2026-09-30 06:30 [ruptura_volumen_regimen] CIERRE XPL stop-loss bruto -1.74% neto -2.24%
- 2026-09-30 06:30 [estocastico_rebote] CIERRE SPX timeout bruto -1.05% neto -1.55%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
