# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 09:06 UTC · vueltas 195 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 894.15 € (-3.26%) | 151 | 30 | 26% | -0.253% | -0.926% | -1.057% | -31.92 € |
| reversion_bb | 915.17 € (-0.98%) | 40 | 6 | 42% | +0.065% | -1.035% | -1.149% | -9.53 € |
| ruptura_volumen | 885.81 € (-4.16%) | 184 | 16 | 18% | -0.302% | -0.944% | -1.076% | -39.41 € |
| rebote_extremo | 923.39 € (-0.09%) | 9 | 1 | 56% | +0.558% | -0.542% | -0.703% | -1.13 € |
| pullback_tendencia | 901.77 € (-2.43%) | 123 | 2 | 24% | -0.094% | -0.806% | -0.933% | -22.68 € |
| macd_momentum | 874.74 € (-5.36%) | 339 | 20 | 17% | -0.086% | -0.663% | -0.774% | -50.70 € |
| estocastico_rebote | 887.88 € (-3.93%) | 225 | 11 | 35% | -0.097% | -0.713% | -0.847% | -36.55 € |
| ruptura_estricta | 901.84 € (-2.42%) | 80 | 8 | 21% | -0.439% | -1.265% | -1.414% | -23.16 € |
| macd_sin_salida | 888.01 € (-3.92%) | 213 | 23 | 28% | -0.157% | -0.779% | -0.900% | -37.71 € |
| c_banda_atr_tope | 909.83 € (-1.56%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.65 € (-1.69%) | 65 | 5 | 17% | -0.181% | -1.087% | -1.213% | -16.21 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 894.86 € (-3.18%) | 128 | 4 | 16% | -0.319% | -1.022% | -1.152% | -29.82 € |
| c_banda_atr_evento | 897.20 € (-2.93%) | 119 | 30 | 24% | -0.340% | -1.062% | -1.194% | -28.88 € |
| macd_momentum_evento | 887.03 € (-4.03%) | 219 | 20 | 14% | -0.152% | -0.773% | -0.881% | -38.41 € |
| ruptura_volumen_evento | 891.27 € (-3.57%) | 125 | 16 | 11% | -0.482% | -1.193% | -1.328% | -33.95 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 09:05 | c_banda_atr_evento | SHIB | timeout | +0.12% | -0.38% | -0.09 |
| 2026-09-30 09:05 | c_banda_atr_evento | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 09:05 | rebote_extremo | JUP | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 09:05 | c_banda_atr | SHIB | timeout | +0.12% | -0.38% | -0.09 |
| 2026-09-30 09:05 | c_banda_atr | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 09:00 | ruptura_volumen_evento | WLD | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 09:00 | macd_momentum_evento | DOT | take-profit | +2.16% | +1.66% | +0.37 |
| 2026-09-30 09:00 | c_banda_atr_evento | RAY | timeout | +0.18% | -0.32% | -0.07 |
| 2026-09-30 09:00 | c_banda_atr_evento | WLD | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 09:00 | macd_sin_salida | WLD | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 09:00 | macd_sin_salida | DOT | take-profit | +2.16% | +1.66% | +0.37 |
| 2026-09-30 09:00 | estocastico_rebote | WLD | take-profit | +2.49% | +1.99% | +0.44 |
| 2026-09-30 09:00 | macd_momentum | DOT | take-profit | +2.16% | +1.66% | +0.36 |
| 2026-09-30 09:00 | ruptura_volumen | WLD | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-09-30 09:00 | c_banda_atr | RAY | timeout | +0.18% | -0.32% | -0.07 |

## Eventos de la última vuelta

- 2026-09-30 09:00 [macd_momentum] ENTRADA XLM @ 0.197535 (21.84 €, apertura)
- 2026-09-30 09:00 [macd_sin_salida] ENTRADA XLM @ 0.197535 (22.16 €, apertura)
- 2026-09-30 09:00 [macd_momentum_evento] ENTRADA XLM @ 0.197535 (22.15 €, apertura)
- 2026-09-30 09:00 [c_banda_atr] ENTRADA XDC @ 0.03051 (22.32 €, apertura)
- 2026-09-30 09:00 [c_banda_atr_evento] ENTRADA XDC @ 0.03051 (22.40 €, apertura)
- 2026-09-30 09:00 [c_banda_atr] ENTRADA DASH @ 53.563 (22.32 €, apertura)
- 2026-09-30 09:00 [c_banda_atr_evento] ENTRADA DASH @ 53.563 (22.40 €, apertura)
- 2026-09-30 09:05 [rebote_extremo] CIERRE JUP take-profit bruto +2.00% neto +0.90%
- 2026-09-30 09:00 [macd_momentum] ENTRADA WLD @ 0.4523 (21.84 €, apertura)
- 2026-09-30 09:00 [macd_momentum_evento] ENTRADA WLD @ 0.4523 (22.15 €, apertura)
- 2026-09-30 09:05 [c_banda_atr] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 09:05 [c_banda_atr_evento] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 09:05 [c_banda_atr] CIERRE SHIB timeout bruto +0.12% neto -0.38%
- 2026-09-30 09:05 [c_banda_atr_evento] CIERRE SHIB timeout bruto +0.12% neto -0.38%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
