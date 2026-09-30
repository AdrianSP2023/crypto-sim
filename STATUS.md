# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 08:47 UTC · vueltas 191 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.25 € (-3.57%) | 146 | 28 | 26% | -0.281% | -0.960% | -1.089% | -31.99 € |
| reversion_bb | 914.62 € (-1.04%) | 40 | 6 | 42% | +0.065% | -1.035% | -1.149% | -9.53 € |
| ruptura_volumen | 883.41 € (-4.42%) | 182 | 14 | 17% | -0.333% | -0.976% | -1.107% | -40.29 € |
| rebote_extremo | 923.34 € (-0.10%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.889% | -1.33 € |
| pullback_tendencia | 901.59 € (-2.45%) | 123 | 2 | 24% | -0.094% | -0.806% | -0.933% | -22.68 € |
| macd_momentum | 873.07 € (-5.54%) | 335 | 13 | 16% | -0.104% | -0.681% | -0.792% | -51.44 € |
| estocastico_rebote | 886.54 € (-4.08%) | 222 | 12 | 34% | -0.126% | -0.744% | -0.877% | -37.57 € |
| ruptura_estricta | 900.78 € (-2.54%) | 79 | 8 | 22% | -0.444% | -1.274% | -1.422% | -23.04 € |
| macd_sin_salida | 885.45 € (-4.20%) | 211 | 17 | 27% | -0.178% | -0.802% | -0.922% | -38.41 € |
| c_banda_atr_tope | 909.24 € (-1.62%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 907.95 € (-1.76%) | 65 | 5 | 17% | -0.181% | -1.087% | -1.213% | -16.21 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 894.67 € (-3.20%) | 128 | 4 | 16% | -0.319% | -1.022% | -1.152% | -29.82 € |
| c_banda_atr_evento | 894.29 € (-3.24%) | 114 | 28 | 23% | -0.379% | -1.111% | -1.240% | -28.94 € |
| macd_momentum_evento | 885.35 € (-4.21%) | 215 | 13 | 13% | -0.180% | -0.803% | -0.911% | -39.16 € |
| ruptura_volumen_evento | 888.85 € (-3.83%) | 123 | 14 | 10% | -0.531% | -1.245% | -1.378% | -34.84 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 08:45 | macd_sin_salida | SUI | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-09-30 08:45 | estocastico_rebote | KAS | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 08:45 | pullback_tendencia | QNT | rotura de tendencia | -0.70% | -1.20% | -0.27 |
| 2026-09-30 08:40 | macd_momentum_evento | MINA | momentum perdido | -1.27% | -1.77% | -0.39 |
| 2026-09-30 08:40 | macd_momentum_evento | WLD | momentum perdido | -0.93% | -1.43% | -0.32 |
| 2026-09-30 08:40 | macd_momentum_evento | XLM | momentum perdido | -0.19% | -0.69% | -0.15 |
| 2026-09-30 08:40 | ruptura_estricta | XRP | timeout | -0.58% | -1.08% | -0.24 |
| 2026-09-30 08:40 | macd_momentum | MINA | momentum perdido | -1.27% | -1.77% | -0.39 |
| 2026-09-30 08:40 | macd_momentum | WLD | momentum perdido | -0.93% | -1.43% | -0.31 |
| 2026-09-30 08:40 | macd_momentum | XLM | momentum perdido | -0.19% | -0.69% | -0.15 |
| 2026-09-30 08:35 | ruptura_volumen_evento | ICP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 08:35 | ruptura_volumen_evento | MON | stop-loss | -1.21% | -1.71% | -0.38 |
| 2026-09-30 08:35 | ruptura_volumen_evento | ZEC | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 08:35 | ruptura_volumen_regimen | MON | stop-loss | -1.21% | -1.71% | -0.38 |
| 2026-09-30 08:35 | ruptura_volumen_regimen | ZEC | stop-loss | -1.20% | -1.70% | -0.38 |

## Eventos de la última vuelta

- 2026-09-30 08:40 [pullback_tendencia] ENTRADA QNT @ 252 (22.55 €, apertura)
- 2026-09-30 08:45 [pullback_tendencia] CIERRE QNT rotura de tendencia bruto -0.70% neto -1.20%
- 2026-09-30 08:45 [macd_sin_salida] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 08:40 [macd_momentum] ENTRADA PUMP @ 0.005066 (21.82 €, apertura)
- 2026-09-30 08:40 [macd_sin_salida] ENTRADA PUMP @ 0.005066 (22.15 €, apertura)
- 2026-09-30 08:40 [macd_momentum_evento] ENTRADA PUMP @ 0.005066 (22.13 €, apertura)
- 2026-09-30 08:45 [estocastico_rebote] CIERRE KAS stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
