# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 08:52 UTC · vueltas 192 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 893.78 € (-3.30%) | 147 | 27 | 27% | -0.265% | -0.943% | -1.072% | -31.65 € |
| reversion_bb | 915.19 € (-0.98%) | 40 | 6 | 42% | +0.065% | -1.035% | -1.149% | -9.53 € |
| ruptura_volumen | 885.01 € (-4.24%) | 182 | 14 | 17% | -0.333% | -0.976% | -1.107% | -40.29 € |
| rebote_extremo | 923.62 € (-0.07%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.889% | -1.33 € |
| pullback_tendencia | 901.68 € (-2.44%) | 123 | 2 | 24% | -0.094% | -0.806% | -0.933% | -22.68 € |
| macd_momentum | 874.57 € (-5.37%) | 337 | 11 | 16% | -0.096% | -0.673% | -0.784% | -51.12 € |
| estocastico_rebote | 887.94 € (-3.93%) | 223 | 11 | 35% | -0.117% | -0.734% | -0.867% | -37.29 € |
| ruptura_estricta | 902.05 € (-2.40%) | 79 | 8 | 22% | -0.444% | -1.274% | -1.422% | -23.04 € |
| macd_sin_salida | 886.93 € (-4.04%) | 211 | 17 | 27% | -0.178% | -0.802% | -0.922% | -38.41 € |
| c_banda_atr_tope | 909.74 € (-1.57%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.46 € (-1.71%) | 65 | 5 | 17% | -0.181% | -1.087% | -1.213% | -16.21 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 894.73 € (-3.19%) | 128 | 4 | 16% | -0.319% | -1.022% | -1.152% | -29.82 € |
| c_banda_atr_evento | 896.83 € (-2.97%) | 115 | 27 | 23% | -0.359% | -1.088% | -1.218% | -28.61 € |
| macd_momentum_evento | 886.86 € (-4.04%) | 217 | 11 | 13% | -0.167% | -0.789% | -0.897% | -38.84 € |
| ruptura_volumen_evento | 890.46 € (-3.65%) | 123 | 14 | 10% | -0.531% | -1.245% | -1.378% | -34.84 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 08:50 | macd_momentum_evento | SPX | momentum perdido | +0.46% | -0.04% | -0.01 |
| 2026-09-30 08:50 | macd_momentum_evento | ENA | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 08:50 | c_banda_atr_evento | OP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 08:50 | estocastico_rebote | DOT | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 08:50 | macd_momentum | SPX | momentum perdido | +0.46% | -0.04% | -0.01 |
| 2026-09-30 08:50 | macd_momentum | ENA | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 08:50 | c_banda_atr | OP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 08:45 | macd_sin_salida | SUI | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-09-30 08:45 | estocastico_rebote | KAS | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 08:45 | pullback_tendencia | QNT | rotura de tendencia | -0.70% | -1.20% | -0.27 |
| 2026-09-30 08:40 | macd_momentum_evento | MINA | momentum perdido | -1.27% | -1.77% | -0.39 |
| 2026-09-30 08:40 | macd_momentum_evento | WLD | momentum perdido | -0.93% | -1.43% | -0.32 |
| 2026-09-30 08:40 | macd_momentum_evento | XLM | momentum perdido | -0.19% | -0.69% | -0.15 |
| 2026-09-30 08:40 | ruptura_estricta | XRP | timeout | -0.58% | -1.08% | -0.24 |
| 2026-09-30 08:40 | macd_momentum | MINA | momentum perdido | -1.27% | -1.77% | -0.39 |

## Eventos de la última vuelta

- 2026-09-30 08:50 [estocastico_rebote] CIERRE DOT take-profit bruto +1.80% neto +1.30%
- 2026-09-30 08:50 [macd_momentum] CIERRE ENA take-profit bruto +2.00% neto +1.50%
- 2026-09-30 08:50 [macd_momentum_evento] CIERRE ENA take-profit bruto +2.00% neto +1.50%
- 2026-09-30 08:50 [c_banda_atr] CIERRE OP take-profit bruto +2.00% neto +1.50%
- 2026-09-30 08:50 [c_banda_atr_evento] CIERRE OP take-profit bruto +2.00% neto +1.50%
- 2026-09-30 08:50 [macd_momentum] CIERRE SPX momentum perdido bruto +0.46% neto -0.04%
- 2026-09-30 08:50 [macd_momentum_evento] CIERRE SPX momentum perdido bruto +0.46% neto -0.04%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
