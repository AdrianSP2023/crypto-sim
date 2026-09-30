# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 06:41 UTC · vueltas 227 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 892.49 € (-3.44%) | 130 | 23 | 27% | -0.272% | -0.972% | -1.106% | -28.91 € |
| reversion_bb | 915.68 € (-0.93%) | 35 | 10 | 46% | +0.183% | -0.917% | -1.027% | -7.39 € |
| ruptura_volumen | 887.37 € (-3.99%) | 165 | 12 | 18% | -0.276% | -0.934% | -1.061% | -35.03 € |
| rebote_extremo | 923.07 € (-0.13%) | 7 | 1 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 903.41 € (-2.25%) | 117 | 2 | 25% | -0.059% | -0.782% | -0.908% | -20.94 € |
| macd_momentum | 874.71 € (-5.36%) | 320 | 1 | 16% | -0.105% | -0.687% | -0.797% | -49.59 € |
| estocastico_rebote | 887.30 € (-4.00%) | 214 | 6 | 34% | -0.129% | -0.751% | -0.883% | -36.59 € |
| ruptura_estricta | 902.74 € (-2.33%) | 70 | 10 | 23% | -0.383% | -1.256% | -1.396% | -20.15 € |
| macd_sin_salida | 888.40 € (-3.88%) | 183 | 25 | 28% | -0.149% | -0.792% | -0.919% | -32.99 € |
| c_banda_atr_tope | 909.60 € (-1.58%) | 39 | 2 | 18% | -0.490% | -1.590% | -1.722% | -14.24 € |
| ruptura_volumen_tope | 908.60 € (-1.69%) | 61 | 2 | 16% | -0.181% | -1.114% | -1.234% | -15.59 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.963% | -38.90 € |
| ruptura_volumen_regimen | 896.11 € (-3.04%) | 120 | 6 | 18% | -0.275% | -0.992% | -1.121% | -27.17 € |
| c_banda_atr_evento | 895.53 € (-3.11%) | 98 | 23 | 23% | -0.383% | -1.152% | -1.287% | -25.85 € |
| macd_momentum_evento | 887.01 € (-4.03%) | 200 | 1 | 13% | -0.189% | -0.821% | -0.927% | -37.29 € |
| ruptura_volumen_evento | 892.83 € (-3.40%) | 106 | 12 | 10% | -0.473% | -1.222% | -1.351% | -29.55 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 06:40 | c_banda_atr_evento | TRUMP | stop-loss | -1.76% | -2.26% | -0.51 |
| 2026-09-30 06:40 | ruptura_volumen_regimen | MON | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 06:40 | macd_sin_salida | SEI | timeout | +0.09% | -0.41% | -0.09 |
| 2026-09-30 06:40 | estocastico_rebote | BNB | timeout | -0.40% | -0.90% | -0.20 |
| 2026-09-30 06:40 | estocastico_rebote | PUMP | timeout | -0.87% | -1.37% | -0.30 |
| 2026-09-30 06:40 | pullback_tendencia | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:40 | c_banda_atr | TRUMP | stop-loss | -1.76% | -2.26% | -0.51 |
| 2026-09-30 06:35 | ruptura_volumen_evento | TRX | timeout | +0.15% | -0.35% | -0.08 |
| 2026-09-30 06:35 | c_banda_atr_evento | POL | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:35 | ruptura_volumen_tope | ICP | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 06:35 | estocastico_rebote | SOL | timeout | -0.93% | -1.43% | -0.32 |
| 2026-09-30 06:35 | ruptura_volumen | TRX | timeout | +0.15% | -0.35% | -0.08 |
| 2026-09-30 06:35 | c_banda_atr | POL | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 06:30 | ruptura_volumen_evento | SEI | timeout | +0.09% | -0.41% | -0.09 |
| 2026-09-30 06:30 | ruptura_volumen_evento | INJ | stop-loss | -1.31% | -1.81% | -0.41 |

## Eventos de la última vuelta

- 2026-09-30 06:40 [estocastico_rebote] CIERRE PUMP timeout bruto -0.87% neto -1.37%
- 2026-09-30 06:40 [ruptura_volumen_regimen] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 06:40 [pullback_tendencia] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 06:40 [macd_sin_salida] CIERRE SEI timeout bruto +0.09% neto -0.41%
- 2026-09-30 06:40 [estocastico_rebote] CIERRE BNB timeout bruto -0.40% neto -0.90%
- 2026-09-30 06:40 [c_banda_atr] CIERRE TRUMP stop-loss bruto -1.76% neto -2.26%
- 2026-09-30 06:40 [c_banda_atr_evento] CIERRE TRUMP stop-loss bruto -1.76% neto -2.26%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
