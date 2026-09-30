# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 03:21 UTC · vueltas 187 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 895.84 € (-3.07%) | 112 | 14 | 27% | -0.286% | -1.020% | -1.155% | -26.16 € |
| reversion_bb | 917.99 € (-0.68%) | 29 | 6 | 48% | +0.205% | -0.895% | -0.997% | -5.98 € |
| ruptura_volumen | 893.47 € (-3.33%) | 142 | 9 | 21% | -0.229% | -0.912% | -1.041% | -29.55 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.93 € (-2.09%) | 109 | 0 | 26% | -0.034% | -0.773% | -0.900% | -19.31 € |
| macd_momentum | 881.46 € (-4.63%) | 264 | 4 | 17% | -0.106% | -0.705% | -0.817% | -42.19 € |
| estocastico_rebote | 890.19 € (-3.68%) | 184 | 17 | 34% | -0.109% | -0.751% | -0.883% | -31.57 € |
| ruptura_estricta | 904.28 € (-2.16%) | 65 | 4 | 25% | -0.348% | -1.249% | -1.393% | -18.63 € |
| macd_sin_salida | 893.11 € (-3.37%) | 155 | 16 | 29% | -0.141% | -0.810% | -0.934% | -28.65 € |
| c_banda_atr_tope | 909.87 € (-1.55%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.35 € (-1.50%) | 51 | 3 | 18% | -0.128% | -1.146% | -1.269% | -13.42 € |
| c_banda_atr_regimen | 900.48 € (-2.57%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 899.07 € (-2.72%) | 108 | 8 | 19% | -0.238% | -0.980% | -1.113% | -24.19 € |
| c_banda_atr_evento | 898.90 € (-2.74%) | 80 | 14 | 22% | -0.429% | -1.259% | -1.397% | -23.10 € |
| macd_momentum_evento | 893.85 € (-3.29%) | 144 | 4 | 13% | -0.223% | -0.906% | -1.014% | -29.79 € |
| ruptura_volumen_evento | 898.98 € (-2.73%) | 83 | 9 | 13% | -0.447% | -1.265% | -1.397% | -24.03 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 03:20 | ruptura_volumen_evento | RENDER | stop-loss | -1.28% | -1.78% | -0.40 |
| 2026-09-30 03:20 | ruptura_volumen_evento | DASH | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 03:20 | c_banda_atr_evento | ENA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 03:20 | ruptura_volumen_regimen | RENDER | stop-loss | -1.28% | -1.78% | -0.40 |
| 2026-09-30 03:20 | ruptura_volumen_tope | DASH | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 03:20 | macd_sin_salida | ENA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 03:20 | macd_sin_salida | AVAX | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 03:20 | macd_sin_salida | ZEC | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 03:20 | estocastico_rebote | AVAX | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 03:20 | pullback_tendencia | SPX | rotura de tendencia | -1.07% | -1.57% | -0.35 |
| 2026-09-30 03:20 | pullback_tendencia | BNB | rotura de tendencia | -0.30% | -0.80% | -0.18 |
| 2026-09-30 03:20 | pullback_tendencia | SOL | rotura de tendencia | -0.23% | -0.73% | -0.17 |
| 2026-09-30 03:20 | ruptura_volumen | RENDER | stop-loss | -1.28% | -1.78% | -0.40 |
| 2026-09-30 03:20 | ruptura_volumen | DASH | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 03:20 | c_banda_atr | ENA | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-30 03:20 [pullback_tendencia] CIERRE SOL rotura de tendencia bruto -0.23% neto -0.73%
- 2026-09-30 03:15 [estocastico_rebote] ENTRADA QNT @ 258 (22.33 €, apertura)
- 2026-09-30 03:20 [macd_sin_salida] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 03:20 [estocastico_rebote] CIERRE AVAX stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 03:20 [macd_sin_salida] CIERRE AVAX stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 03:20 [ruptura_volumen] CIERRE DASH stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 03:20 [ruptura_volumen_tope] CIERRE DASH stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 03:20 [ruptura_volumen_evento] CIERRE DASH stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 03:20 [c_banda_atr] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 03:20 [macd_sin_salida] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 03:20 [c_banda_atr_evento] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 03:20 [ruptura_volumen] CIERRE RENDER stop-loss bruto -1.28% neto -1.78%
- 2026-09-30 03:20 [ruptura_volumen_regimen] CIERRE RENDER stop-loss bruto -1.28% neto -1.78%
- 2026-09-30 03:20 [ruptura_volumen_evento] CIERRE RENDER stop-loss bruto -1.28% neto -1.78%
- 2026-09-30 03:20 [pullback_tendencia] CIERRE BNB rotura de tendencia bruto -0.30% neto -0.80%
- 2026-09-30 03:20 [pullback_tendencia] CIERRE SPX rotura de tendencia bruto -1.07% neto -1.57%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
