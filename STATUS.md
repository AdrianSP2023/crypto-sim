# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 08:22 UTC · vueltas 186 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 892.99 € (-3.38%) | 145 | 26 | 26% | -0.297% | -0.977% | -1.106% | -32.32 € |
| reversion_bb | 914.99 € (-1.00%) | 40 | 6 | 42% | +0.065% | -1.035% | -1.149% | -9.53 € |
| ruptura_volumen | 884.89 € (-4.26%) | 179 | 11 | 17% | -0.318% | -0.964% | -1.096% | -39.16 € |
| rebote_extremo | 923.50 € (-0.08%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.889% | -1.33 € |
| pullback_tendencia | 901.88 € (-2.42%) | 122 | 1 | 24% | -0.089% | -0.803% | -0.929% | -22.41 € |
| macd_momentum | 874.77 € (-5.35%) | 330 | 14 | 16% | -0.095% | -0.674% | -0.784% | -50.18 € |
| estocastico_rebote | 887.57 € (-3.97%) | 220 | 14 | 34% | -0.128% | -0.747% | -0.880% | -37.42 € |
| ruptura_estricta | 901.50 € (-2.46%) | 78 | 8 | 22% | -0.442% | -1.277% | -1.425% | -22.80 € |
| macd_sin_salida | 887.29 € (-4.00%) | 204 | 22 | 27% | -0.176% | -0.804% | -0.928% | -37.27 € |
| c_banda_atr_tope | 909.42 € (-1.60%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.00 € (-1.76%) | 65 | 3 | 17% | -0.181% | -1.087% | -1.213% | -16.21 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 894.95 € (-3.17%) | 126 | 6 | 17% | -0.305% | -1.012% | -1.143% | -29.06 € |
| c_banda_atr_evento | 896.03 € (-3.05%) | 113 | 26 | 22% | -0.400% | -1.134% | -1.264% | -29.28 € |
| macd_momentum_evento | 887.07 € (-4.02%) | 210 | 14 | 13% | -0.169% | -0.794% | -0.901% | -37.88 € |
| ruptura_volumen_evento | 890.34 € (-3.67%) | 120 | 11 | 10% | -0.514% | -1.234% | -1.368% | -33.71 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 08:20 | macd_momentum_evento | KAS | momentum perdido | -0.77% | -1.27% | -0.28 |
| 2026-09-30 08:20 | macd_momentum_evento | XRP | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-09-30 08:20 | c_banda_atr_evento | ONDO | timeout | -0.56% | -1.06% | -0.24 |
| 2026-09-30 08:20 | macd_momentum | KAS | momentum perdido | -0.77% | -1.27% | -0.28 |
| 2026-09-30 08:20 | macd_momentum | XRP | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-09-30 08:20 | pullback_tendencia | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 08:20 | reversion_bb | OP | take-profit | +1.94% | +0.84% | +0.19 |
| 2026-09-30 08:20 | c_banda_atr | ONDO | timeout | -0.56% | -1.06% | -0.24 |
| 2026-09-30 08:15 | macd_momentum_evento | SUI | momentum perdido | -1.06% | -1.56% | -0.34 |
| 2026-09-30 08:15 | macd_momentum_evento | HBAR | momentum perdido | +0.29% | -0.21% | -0.05 |
| 2026-09-30 08:15 | macd_momentum_evento | QNT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 08:15 | macd_sin_salida | QNT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 08:15 | macd_momentum | SUI | momentum perdido | -1.06% | -1.56% | -0.34 |
| 2026-09-30 08:15 | macd_momentum | HBAR | momentum perdido | +0.29% | -0.21% | -0.04 |
| 2026-09-30 08:15 | macd_momentum | QNT | take-profit | +2.00% | +1.50% | +0.33 |

## Eventos de la última vuelta

- 2026-09-30 08:20 [macd_momentum] CIERRE XRP momentum perdido bruto -0.24% neto -0.74%
- 2026-09-30 08:20 [macd_momentum_evento] CIERRE XRP momentum perdido bruto -0.24% neto -0.74%
- 2026-09-30 08:15 [pullback_tendencia] ENTRADA QNT @ 257.51 (22.56 €, apertura)
- 2026-09-30 08:20 [pullback_tendencia] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 08:20 [c_banda_atr] CIERRE ONDO timeout bruto -0.56% neto -1.06%
- 2026-09-30 08:20 [c_banda_atr_evento] CIERRE ONDO timeout bruto -0.56% neto -1.06%
- 2026-09-30 08:20 [reversion_bb] CIERRE OP take-profit bruto +1.94% neto +0.84%
- 2026-09-30 08:20 [macd_momentum] CIERRE KAS momentum perdido bruto -0.77% neto -1.27%
- 2026-09-30 08:20 [macd_momentum_evento] CIERRE KAS momentum perdido bruto -0.77% neto -1.27%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
