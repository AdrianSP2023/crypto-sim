# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 08:27 UTC · vueltas 187 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 893.17 € (-3.36%) | 146 | 27 | 26% | -0.281% | -0.960% | -1.089% | -31.99 € |
| reversion_bb | 914.94 € (-1.01%) | 40 | 6 | 42% | +0.065% | -1.035% | -1.149% | -9.53 € |
| ruptura_volumen | 884.93 € (-4.25%) | 179 | 12 | 17% | -0.318% | -0.964% | -1.096% | -39.16 € |
| rebote_extremo | 923.55 € (-0.07%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.889% | -1.33 € |
| pullback_tendencia | 901.88 € (-2.42%) | 122 | 1 | 24% | -0.089% | -0.803% | -0.929% | -22.41 € |
| macd_momentum | 875.07 € (-5.32%) | 331 | 16 | 16% | -0.098% | -0.677% | -0.787% | -50.51 € |
| estocastico_rebote | 887.58 € (-3.97%) | 221 | 13 | 34% | -0.120% | -0.738% | -0.871% | -37.13 € |
| ruptura_estricta | 901.63 € (-2.45%) | 78 | 8 | 22% | -0.442% | -1.277% | -1.425% | -22.80 € |
| macd_sin_salida | 887.77 € (-3.95%) | 205 | 22 | 28% | -0.166% | -0.793% | -0.916% | -36.94 € |
| c_banda_atr_tope | 909.40 € (-1.61%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.19 € (-1.74%) | 65 | 4 | 17% | -0.181% | -1.087% | -1.213% | -16.21 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 894.90 € (-3.17%) | 126 | 6 | 17% | -0.305% | -1.012% | -1.143% | -29.06 € |
| c_banda_atr_evento | 896.22 € (-3.03%) | 114 | 27 | 23% | -0.379% | -1.111% | -1.240% | -28.94 € |
| macd_momentum_evento | 887.37 € (-3.99%) | 211 | 16 | 13% | -0.173% | -0.798% | -0.905% | -38.22 € |
| ruptura_volumen_evento | 890.38 € (-3.66%) | 120 | 12 | 10% | -0.514% | -1.234% | -1.368% | -33.71 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 08:25 | macd_momentum_evento | RAY | momentum perdido | -1.03% | -1.53% | -0.34 |
| 2026-09-30 08:25 | c_banda_atr_evento | ENA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 08:25 | macd_sin_salida | ENA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 08:25 | estocastico_rebote | SPX | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 08:25 | macd_momentum | RAY | momentum perdido | -1.03% | -1.53% | -0.33 |
| 2026-09-30 08:25 | c_banda_atr | ENA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 08:20 | macd_momentum_evento | KAS | momentum perdido | -0.77% | -1.27% | -0.28 |
| 2026-09-30 08:20 | macd_momentum_evento | XRP | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-09-30 08:20 | c_banda_atr_evento | ONDO | timeout | -0.56% | -1.06% | -0.24 |
| 2026-09-30 08:20 | macd_momentum | KAS | momentum perdido | -0.77% | -1.27% | -0.28 |
| 2026-09-30 08:20 | macd_momentum | XRP | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-09-30 08:20 | pullback_tendencia | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 08:20 | reversion_bb | OP | take-profit | +1.94% | +0.84% | +0.19 |
| 2026-09-30 08:20 | c_banda_atr | ONDO | timeout | -0.56% | -1.06% | -0.24 |
| 2026-09-30 08:15 | macd_momentum_evento | SUI | momentum perdido | -1.06% | -1.56% | -0.34 |

## Eventos de la última vuelta

- 2026-09-30 08:20 [c_banda_atr] ENTRADA CRV @ 0.34788 (22.30 €, apertura)
- 2026-09-30 08:20 [macd_momentum] ENTRADA CRV @ 0.34788 (21.85 €, apertura)
- 2026-09-30 08:20 [c_banda_atr_evento] ENTRADA CRV @ 0.34788 (22.37 €, apertura)
- 2026-09-30 08:20 [macd_momentum_evento] ENTRADA CRV @ 0.34788 (22.16 €, apertura)
- 2026-09-30 08:25 [c_banda_atr] CIERRE ENA take-profit bruto +2.00% neto +1.50%
- 2026-09-30 08:20 [macd_momentum] ENTRADA ENA @ 0.2202 (21.85 €, apertura)
- 2026-09-30 08:25 [macd_sin_salida] CIERRE ENA take-profit bruto +2.00% neto +1.50%
- 2026-09-30 08:25 [c_banda_atr_evento] CIERRE ENA take-profit bruto +2.00% neto +1.50%
- 2026-09-30 08:20 [macd_momentum_evento] ENTRADA ENA @ 0.2202 (22.16 €, apertura)
- 2026-09-30 08:20 [ruptura_volumen] ENTRADA ATOM @ 1.5139 (22.13 €, apertura)
- 2026-09-30 08:20 [ruptura_volumen_tope] ENTRADA ATOM @ 1.5139 (22.70 €, apertura)
- 2026-09-30 08:20 [ruptura_volumen_evento] ENTRADA ATOM @ 1.5139 (22.26 €, apertura)
- 2026-09-30 08:25 [macd_momentum] CIERRE RAY momentum perdido bruto -1.03% neto -1.53%
- 2026-09-30 08:25 [macd_momentum_evento] CIERRE RAY momentum perdido bruto -1.03% neto -1.53%
- 2026-09-30 08:20 [c_banda_atr] ENTRADA FIL @ 0.936 (22.31 €, apertura)
- 2026-09-30 08:20 [macd_momentum] ENTRADA FIL @ 0.936 (21.84 €, apertura)
- 2026-09-30 08:20 [macd_sin_salida] ENTRADA FIL @ 0.936 (22.18 €, apertura)
- 2026-09-30 08:20 [c_banda_atr_evento] ENTRADA FIL @ 0.936 (22.38 €, apertura)
- 2026-09-30 08:20 [macd_momentum_evento] ENTRADA FIL @ 0.936 (22.15 €, apertura)
- 2026-09-30 08:25 [estocastico_rebote] CIERRE SPX take-profit bruto +1.80% neto +1.30%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
