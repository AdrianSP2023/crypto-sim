# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 08:17 UTC · vueltas 185 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.03 € (-3.59%) | 144 | 27 | 26% | -0.295% | -0.976% | -1.106% | -32.09 € |
| reversion_bb | 914.81 € (-1.02%) | 39 | 7 | 41% | +0.017% | -1.083% | -1.197% | -9.72 € |
| ruptura_volumen | 884.15 € (-4.34%) | 179 | 11 | 17% | -0.318% | -0.964% | -1.096% | -39.16 € |
| rebote_extremo | 923.42 € (-0.09%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.889% | -1.33 € |
| pullback_tendencia | 902.33 € (-2.37%) | 121 | 1 | 24% | -0.078% | -0.793% | -0.919% | -21.96 € |
| macd_momentum | 874.15 € (-5.42%) | 328 | 16 | 16% | -0.093% | -0.672% | -0.782% | -49.74 € |
| estocastico_rebote | 886.50 € (-4.08%) | 220 | 14 | 34% | -0.128% | -0.747% | -0.880% | -37.42 € |
| ruptura_estricta | 901.00 € (-2.51%) | 78 | 8 | 22% | -0.442% | -1.277% | -1.425% | -22.80 € |
| macd_sin_salida | 885.62 € (-4.18%) | 204 | 22 | 27% | -0.176% | -0.804% | -0.928% | -37.27 € |
| c_banda_atr_tope | 909.20 € (-1.63%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 907.65 € (-1.79%) | 65 | 3 | 17% | -0.181% | -1.087% | -1.213% | -16.21 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 894.71 € (-3.20%) | 126 | 6 | 17% | -0.305% | -1.012% | -1.143% | -29.06 € |
| c_banda_atr_evento | 894.07 € (-3.26%) | 112 | 27 | 22% | -0.399% | -1.135% | -1.264% | -29.04 € |
| macd_momentum_evento | 886.44 € (-4.09%) | 208 | 16 | 13% | -0.166% | -0.792% | -0.899% | -37.43 € |
| ruptura_volumen_evento | 889.59 € (-3.75%) | 120 | 11 | 10% | -0.514% | -1.234% | -1.368% | -33.71 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 08:15 | macd_momentum_evento | SUI | momentum perdido | -1.06% | -1.56% | -0.34 |
| 2026-09-30 08:15 | macd_momentum_evento | HBAR | momentum perdido | +0.29% | -0.21% | -0.05 |
| 2026-09-30 08:15 | macd_momentum_evento | QNT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 08:15 | macd_sin_salida | QNT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 08:15 | macd_momentum | SUI | momentum perdido | -1.06% | -1.56% | -0.34 |
| 2026-09-30 08:15 | macd_momentum | HBAR | momentum perdido | +0.29% | -0.21% | -0.04 |
| 2026-09-30 08:15 | macd_momentum | QNT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 08:10 | ruptura_volumen_evento | XDC | take-profit | +2.52% | +2.02% | +0.45 |
| 2026-09-30 08:10 | ruptura_volumen_evento | PUMP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 08:10 | c_banda_atr_evento | DASH | timeout | -0.47% | -0.96% | -0.22 |
| 2026-09-30 08:10 | c_banda_atr_evento | CRV | timeout | +0.14% | -0.36% | -0.08 |
| 2026-09-30 08:10 | ruptura_volumen_tope | XDC | take-profit | +2.52% | +2.02% | +0.46 |
| 2026-09-30 08:10 | ruptura_volumen_tope | PUMP | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 08:10 | pullback_tendencia | CRV | rotura de tendencia | -0.64% | -1.14% | -0.26 |
| 2026-09-30 08:10 | pullback_tendencia | XRP | rotura de tendencia | -0.17% | -0.67% | -0.15 |

## Eventos de la última vuelta

- 2026-09-30 08:10 [macd_momentum] ENTRADA QNT @ 251.58 (21.86 €, apertura)
- 2026-09-30 08:15 [macd_momentum] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 08:10 [macd_sin_salida] ENTRADA QNT @ 251.58 (22.17 €, apertura)
- 2026-09-30 08:15 [macd_sin_salida] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 08:10 [macd_momentum_evento] ENTRADA QNT @ 251.58 (22.17 €, apertura)
- 2026-09-30 08:15 [macd_momentum_evento] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 08:15 [macd_momentum] CIERRE HBAR momentum perdido bruto +0.29% neto -0.21%
- 2026-09-30 08:15 [macd_momentum_evento] CIERRE HBAR momentum perdido bruto +0.29% neto -0.21%
- 2026-09-30 08:15 [macd_momentum] CIERRE SUI momentum perdido bruto -1.06% neto -1.56%
- 2026-09-30 08:15 [macd_momentum_evento] CIERRE SUI momentum perdido bruto -1.06% neto -1.56%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
