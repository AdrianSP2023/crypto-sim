# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 08:12 UTC · vueltas 184 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.67 € (-3.52%) | 144 | 27 | 26% | -0.295% | -0.976% | -1.106% | -32.09 € |
| reversion_bb | 914.88 € (-1.01%) | 39 | 7 | 41% | +0.017% | -1.083% | -1.197% | -9.72 € |
| ruptura_volumen | 884.29 € (-4.32%) | 179 | 11 | 17% | -0.318% | -0.964% | -1.096% | -39.16 € |
| rebote_extremo | 923.39 € (-0.09%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.889% | -1.33 € |
| pullback_tendencia | 902.34 € (-2.37%) | 121 | 1 | 24% | -0.078% | -0.793% | -0.919% | -21.96 € |
| macd_momentum | 874.39 € (-5.39%) | 325 | 18 | 16% | -0.097% | -0.678% | -0.788% | -49.68 € |
| estocastico_rebote | 886.76 € (-4.06%) | 220 | 14 | 34% | -0.128% | -0.747% | -0.880% | -37.42 € |
| ruptura_estricta | 900.93 € (-2.52%) | 78 | 8 | 22% | -0.442% | -1.277% | -1.425% | -22.80 € |
| macd_sin_salida | 885.59 € (-4.18%) | 203 | 22 | 27% | -0.187% | -0.816% | -0.939% | -37.60 € |
| c_banda_atr_tope | 909.52 € (-1.59%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 907.78 € (-1.78%) | 65 | 3 | 17% | -0.181% | -1.087% | -1.213% | -16.21 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 894.84 € (-3.18%) | 126 | 6 | 17% | -0.305% | -1.012% | -1.143% | -29.06 € |
| c_banda_atr_evento | 894.71 € (-3.20%) | 112 | 27 | 22% | -0.399% | -1.135% | -1.264% | -29.04 € |
| macd_momentum_evento | 886.69 € (-4.06%) | 205 | 18 | 13% | -0.174% | -0.803% | -0.910% | -37.38 € |
| ruptura_volumen_evento | 889.74 € (-3.73%) | 120 | 11 | 10% | -0.514% | -1.234% | -1.368% | -33.71 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 08:10 | ruptura_volumen_evento | XDC | take-profit | +2.52% | +2.02% | +0.45 |
| 2026-09-30 08:10 | ruptura_volumen_evento | PUMP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 08:10 | c_banda_atr_evento | DASH | timeout | -0.47% | -0.96% | -0.22 |
| 2026-09-30 08:10 | c_banda_atr_evento | CRV | timeout | +0.14% | -0.36% | -0.08 |
| 2026-09-30 08:10 | ruptura_volumen_tope | XDC | take-profit | +2.52% | +2.02% | +0.46 |
| 2026-09-30 08:10 | ruptura_volumen_tope | PUMP | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 08:10 | pullback_tendencia | CRV | rotura de tendencia | -0.64% | -1.14% | -0.26 |
| 2026-09-30 08:10 | pullback_tendencia | XRP | rotura de tendencia | -0.17% | -0.67% | -0.15 |
| 2026-09-30 08:10 | ruptura_volumen | XDC | take-profit | +2.52% | +2.02% | +0.45 |
| 2026-09-30 08:10 | ruptura_volumen | PUMP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 08:10 | c_banda_atr | DASH | timeout | -0.47% | -0.96% | -0.22 |
| 2026-09-30 08:10 | c_banda_atr | CRV | timeout | +0.14% | -0.36% | -0.08 |
| 2026-09-30 08:05 | macd_momentum_evento | CRV | momentum perdido | -0.23% | -0.73% | -0.16 |
| 2026-09-30 08:05 | c_banda_atr_evento | BNB | timeout | -0.58% | -1.08% | -0.24 |
| 2026-09-30 08:05 | c_banda_atr_evento | AAVE | timeout | -0.82% | -1.32% | -0.30 |

## Eventos de la última vuelta

- 2026-09-30 08:05 [pullback_tendencia] ENTRADA XRP @ 1.31997 (22.57 €, apertura)
- 2026-09-30 08:10 [pullback_tendencia] CIERRE XRP rotura de tendencia bruto -0.17% neto -0.67%
- 2026-09-30 08:10 [ruptura_volumen] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 08:10 [ruptura_volumen_tope] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 08:10 [ruptura_volumen_evento] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 08:10 [ruptura_volumen] CIERRE XDC take-profit bruto +2.53% neto +2.03%
- 2026-09-30 08:10 [ruptura_volumen_tope] CIERRE XDC take-profit bruto +2.53% neto +2.03%
- 2026-09-30 08:10 [ruptura_volumen_evento] CIERRE XDC take-profit bruto +2.53% neto +2.03%
- 2026-09-30 08:10 [c_banda_atr] CIERRE CRV timeout bruto +0.14% neto -0.36%
- 2026-09-30 08:10 [pullback_tendencia] CIERRE CRV rotura de tendencia bruto -0.64% neto -1.14%
- 2026-09-30 08:10 [c_banda_atr_evento] CIERRE CRV timeout bruto +0.14% neto -0.36%
- 2026-09-30 08:10 [c_banda_atr] CIERRE DASH timeout bruto -0.47% neto -0.97%
- 2026-09-30 08:10 [c_banda_atr_evento] CIERRE DASH timeout bruto -0.47% neto -0.97%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
