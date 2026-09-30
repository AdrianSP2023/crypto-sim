# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 08:37 UTC · vueltas 189 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.93 € (-3.60%) | 146 | 28 | 26% | -0.281% | -0.960% | -1.089% | -31.99 € |
| reversion_bb | 914.60 € (-1.04%) | 40 | 6 | 42% | +0.065% | -1.035% | -1.149% | -9.53 € |
| ruptura_volumen | 883.14 € (-4.45%) | 182 | 14 | 17% | -0.333% | -0.976% | -1.107% | -40.29 € |
| rebote_extremo | 923.36 € (-0.10%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.889% | -1.33 € |
| pullback_tendencia | 901.87 € (-2.42%) | 122 | 1 | 24% | -0.089% | -0.803% | -0.929% | -22.41 € |
| macd_momentum | 873.79 € (-5.46%) | 332 | 15 | 16% | -0.097% | -0.676% | -0.786% | -50.59 € |
| estocastico_rebote | 886.49 € (-4.08%) | 221 | 13 | 34% | -0.120% | -0.738% | -0.871% | -37.13 € |
| ruptura_estricta | 900.85 € (-2.53%) | 78 | 9 | 22% | -0.442% | -1.277% | -1.425% | -22.80 € |
| macd_sin_salida | 885.71 € (-4.17%) | 210 | 17 | 27% | -0.172% | -0.796% | -0.917% | -37.97 € |
| c_banda_atr_tope | 909.43 € (-1.60%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 907.75 € (-1.78%) | 65 | 5 | 17% | -0.181% | -1.087% | -1.213% | -16.21 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 894.45 € (-3.22%) | 128 | 4 | 16% | -0.319% | -1.022% | -1.152% | -29.82 € |
| c_banda_atr_evento | 893.97 € (-3.28%) | 114 | 28 | 23% | -0.379% | -1.111% | -1.240% | -28.94 € |
| macd_momentum_evento | 886.07 € (-4.13%) | 212 | 15 | 13% | -0.171% | -0.796% | -0.903% | -38.30 € |
| ruptura_volumen_evento | 888.57 € (-3.86%) | 123 | 14 | 10% | -0.531% | -1.245% | -1.378% | -34.84 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 08:35 | ruptura_volumen_evento | ICP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 08:35 | ruptura_volumen_evento | MON | stop-loss | -1.21% | -1.71% | -0.38 |
| 2026-09-30 08:35 | ruptura_volumen_evento | ZEC | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 08:35 | ruptura_volumen_regimen | MON | stop-loss | -1.21% | -1.71% | -0.38 |
| 2026-09-30 08:35 | ruptura_volumen_regimen | ZEC | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 08:35 | macd_sin_salida | BNB | timeout | -0.76% | -1.26% | -0.28 |
| 2026-09-30 08:35 | macd_sin_salida | XLM | timeout | -0.16% | -0.66% | -0.15 |
| 2026-09-30 08:35 | macd_sin_salida | ETH | timeout | -0.52% | -1.02% | -0.23 |
| 2026-09-30 08:35 | ruptura_volumen | ICP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 08:35 | ruptura_volumen | MON | stop-loss | -1.21% | -1.71% | -0.38 |
| 2026-09-30 08:35 | ruptura_volumen | ZEC | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 08:30 | macd_momentum_evento | TRX | momentum perdido | +0.11% | -0.39% | -0.09 |
| 2026-09-30 08:30 | macd_sin_salida | DOGE | timeout | -0.26% | -0.76% | -0.17 |
| 2026-09-30 08:30 | macd_sin_salida | BTC | timeout | -0.41% | -0.92% | -0.20 |
| 2026-09-30 08:30 | macd_momentum | TRX | momentum perdido | +0.11% | -0.39% | -0.09 |

## Eventos de la última vuelta

- 2026-09-30 08:35 [macd_sin_salida] CIERRE ETH timeout bruto -0.52% neto -1.02%
- 2026-09-30 08:35 [ruptura_volumen] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 08:35 [ruptura_volumen_regimen] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 08:35 [ruptura_volumen_evento] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 08:35 [macd_sin_salida] CIERRE XLM timeout bruto -0.16% neto -0.66%
- 2026-09-30 08:35 [ruptura_volumen] CIERRE MON stop-loss bruto -1.21% neto -1.71%
- 2026-09-30 08:35 [ruptura_volumen_regimen] CIERRE MON stop-loss bruto -1.21% neto -1.71%
- 2026-09-30 08:35 [ruptura_volumen_evento] CIERRE MON stop-loss bruto -1.21% neto -1.71%
- 2026-09-30 08:35 [ruptura_volumen] CIERRE ICP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 08:35 [ruptura_volumen_evento] CIERRE ICP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 08:35 [macd_sin_salida] CIERRE BNB timeout bruto -0.76% neto -1.26%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
