# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 09:01 UTC · vueltas 194 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 893.52 € (-3.32%) | 149 | 30 | 27% | -0.247% | -0.922% | -1.054% | -31.39 € |
| reversion_bb | 914.99 € (-1.00%) | 40 | 6 | 42% | +0.065% | -1.035% | -1.149% | -9.53 € |
| ruptura_volumen | 885.04 € (-4.24%) | 184 | 16 | 18% | -0.302% | -0.944% | -1.076% | -39.41 € |
| rebote_extremo | 923.60 € (-0.07%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.889% | -1.33 € |
| pullback_tendencia | 901.60 € (-2.45%) | 123 | 2 | 24% | -0.094% | -0.806% | -0.933% | -22.68 € |
| macd_momentum | 874.22 € (-5.41%) | 339 | 18 | 17% | -0.086% | -0.663% | -0.774% | -50.70 € |
| estocastico_rebote | 887.63 € (-3.96%) | 225 | 11 | 35% | -0.097% | -0.713% | -0.847% | -36.55 € |
| ruptura_estricta | 901.46 € (-2.46%) | 80 | 8 | 21% | -0.439% | -1.265% | -1.414% | -23.16 € |
| macd_sin_salida | 887.30 € (-4.00%) | 213 | 22 | 28% | -0.157% | -0.779% | -0.900% | -37.71 € |
| c_banda_atr_tope | 909.54 € (-1.59%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.22 € (-1.73%) | 65 | 5 | 17% | -0.181% | -1.087% | -1.213% | -16.21 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 894.79 € (-3.19%) | 128 | 4 | 16% | -0.319% | -1.022% | -1.152% | -29.82 € |
| c_banda_atr_evento | 896.57 € (-2.99%) | 117 | 30 | 24% | -0.334% | -1.060% | -1.192% | -28.34 € |
| macd_momentum_evento | 886.51 € (-4.08%) | 219 | 18 | 14% | -0.152% | -0.773% | -0.881% | -38.41 € |
| ruptura_volumen_evento | 890.49 € (-3.65%) | 125 | 16 | 11% | -0.482% | -1.193% | -1.328% | -33.95 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-30 09:00 | c_banda_atr | WLD | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 08:55 | ruptura_volumen_evento | ENA | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 08:55 | macd_momentum_evento | XDC | momentum perdido | +0.80% | +0.30% | +0.07 |
| 2026-09-30 08:55 | ruptura_estricta | WLD | timeout | -0.04% | -0.55% | -0.12 |
| 2026-09-30 08:55 | estocastico_rebote | CRV | take-profit | +1.83% | +1.33% | +0.29 |

## Eventos de la última vuelta

- 2026-09-30 08:55 [macd_momentum] ENTRADA XRP @ 1.319 (21.83 €, apertura)
- 2026-09-30 08:55 [macd_momentum_evento] ENTRADA XRP @ 1.319 (22.14 €, apertura)
- 2026-09-30 08:55 [ruptura_volumen] ENTRADA DOT @ 1.0834 (22.11 €, apertura)
- 2026-09-30 09:00 [macd_momentum] CIERRE DOT take-profit bruto +2.16% neto +1.66%
- 2026-09-30 09:00 [macd_sin_salida] CIERRE DOT take-profit bruto +2.16% neto +1.66%
- 2026-09-30 09:00 [macd_momentum_evento] CIERRE DOT take-profit bruto +2.16% neto +1.66%
- 2026-09-30 08:55 [ruptura_volumen_evento] ENTRADA DOT @ 1.0834 (22.25 €, apertura)
- 2026-09-30 08:55 [macd_momentum] ENTRADA BCH @ 271.48 (21.84 €, apertura)
- 2026-09-30 08:55 [macd_sin_salida] ENTRADA BCH @ 271.48 (22.15 €, apertura)
- 2026-09-30 08:55 [macd_momentum_evento] ENTRADA BCH @ 271.48 (22.15 €, apertura)
- 2026-09-30 09:00 [c_banda_atr] CIERRE WLD take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:00 [ruptura_volumen] CIERRE WLD take-profit bruto +2.50% neto +2.00%
- 2026-09-30 09:00 [estocastico_rebote] CIERRE WLD take-profit bruto +2.49% neto +1.99%
- 2026-09-30 09:00 [macd_sin_salida] CIERRE WLD take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:00 [c_banda_atr_evento] CIERRE WLD take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:00 [ruptura_volumen_evento] CIERRE WLD take-profit bruto +2.50% neto +2.00%
- 2026-09-30 08:55 [macd_momentum] ENTRADA USELESS @ 0.20902 (21.84 €, apertura)
- 2026-09-30 08:55 [macd_sin_salida] ENTRADA USELESS @ 0.20902 (22.16 €, apertura)
- 2026-09-30 08:55 [macd_momentum_evento] ENTRADA USELESS @ 0.20902 (22.15 €, apertura)
- 2026-09-30 09:00 [c_banda_atr] CIERRE RAY timeout bruto +0.18% neto -0.32%
- 2026-09-30 08:55 [macd_momentum] ENTRADA RAY @ 1.659 (21.84 €, apertura)
- 2026-09-30 09:00 [c_banda_atr_evento] CIERRE RAY timeout bruto +0.18% neto -0.32%
- 2026-09-30 08:55 [macd_momentum_evento] ENTRADA RAY @ 1.659 (22.15 €, apertura)
- 2026-09-30 08:55 [estocastico_rebote] ENTRADA SPX @ 0.3743 (22.19 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
