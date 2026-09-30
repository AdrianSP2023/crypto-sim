# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 09:11 UTC · vueltas 196 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 894.54 € (-3.21%) | 151 | 33 | 26% | -0.253% | -0.926% | -1.057% | -31.92 € |
| reversion_bb | 915.28 € (-0.97%) | 40 | 6 | 42% | +0.065% | -1.035% | -1.149% | -9.53 € |
| ruptura_volumen | 885.99 € (-4.14%) | 184 | 17 | 18% | -0.302% | -0.944% | -1.076% | -39.41 € |
| rebote_extremo | 923.46 € (-0.08%) | 9 | 1 | 56% | +0.558% | -0.542% | -0.703% | -1.13 € |
| pullback_tendencia | 901.70 € (-2.44%) | 123 | 2 | 24% | -0.094% | -0.806% | -0.933% | -22.68 € |
| macd_momentum | 874.97 € (-5.33%) | 341 | 25 | 17% | -0.082% | -0.658% | -0.769% | -50.61 € |
| estocastico_rebote | 888.04 € (-3.92%) | 225 | 12 | 35% | -0.097% | -0.713% | -0.847% | -36.55 € |
| ruptura_estricta | 902.05 € (-2.40%) | 80 | 8 | 21% | -0.439% | -1.265% | -1.414% | -23.16 € |
| macd_sin_salida | 888.39 € (-3.88%) | 213 | 29 | 28% | -0.157% | -0.779% | -0.900% | -37.71 € |
| c_banda_atr_tope | 909.70 € (-1.57%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.57 € (-1.70%) | 65 | 5 | 17% | -0.181% | -1.087% | -1.213% | -16.21 € |
| c_banda_atr_regimen | 900.70 € (-2.55%) | 78 | 4 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.13 € (-4.23%) | 202 | 7 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 894.92 € (-3.17%) | 128 | 5 | 16% | -0.319% | -1.022% | -1.152% | -29.82 € |
| c_banda_atr_evento | 897.59 € (-2.88%) | 119 | 33 | 24% | -0.340% | -1.062% | -1.194% | -28.88 € |
| macd_momentum_evento | 887.27 € (-4.00%) | 221 | 25 | 14% | -0.144% | -0.764% | -0.872% | -38.32 € |
| ruptura_volumen_evento | 891.44 € (-3.55%) | 125 | 17 | 11% | -0.482% | -1.193% | -1.328% | -33.95 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 09:10 | macd_momentum_evento | ASTER | momentum perdido | +0.92% | +0.42% | +0.09 |
| 2026-09-30 09:10 | macd_momentum_evento | ICP | momentum perdido | +0.49% | -0.01% | -0.00 |
| 2026-09-30 09:10 | macd_momentum | ASTER | momentum perdido | +0.92% | +0.42% | +0.09 |
| 2026-09-30 09:10 | macd_momentum | ICP | momentum perdido | +0.49% | -0.01% | -0.00 |
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

## Eventos de la última vuelta

- 2026-09-30 09:05 [macd_momentum] ENTRADA ETH @ 2355.35 (21.84 €, apertura)
- 2026-09-30 09:05 [macd_sin_salida] ENTRADA ETH @ 2355.35 (22.16 €, apertura)
- 2026-09-30 09:05 [c_banda_atr_regimen] ENTRADA ETH @ 2355.35 (22.52 €, apertura)
- 2026-09-30 09:05 [macd_momentum_regimen] ENTRADA ETH @ 2355.35 (22.13 €, apertura)
- 2026-09-30 09:05 [macd_momentum_evento] ENTRADA ETH @ 2355.35 (22.15 €, apertura)
- 2026-09-30 09:05 [macd_momentum] ENTRADA HBAR @ 0.09401 (21.84 €, apertura)
- 2026-09-30 09:05 [macd_momentum_regimen] ENTRADA HBAR @ 0.09401 (22.13 €, apertura)
- 2026-09-30 09:05 [macd_momentum_evento] ENTRADA HBAR @ 0.09401 (22.15 €, apertura)
- 2026-09-30 09:05 [macd_momentum] ENTRADA ZEC @ 1240.75 (21.84 €, apertura)
- 2026-09-30 09:05 [macd_sin_salida] ENTRADA ZEC @ 1240.75 (22.16 €, apertura)
- 2026-09-30 09:05 [macd_momentum_regimen] ENTRADA ZEC @ 1240.75 (22.13 €, apertura)
- 2026-09-30 09:05 [macd_momentum_evento] ENTRADA ZEC @ 1240.75 (22.15 €, apertura)
- 2026-09-30 09:05 [macd_momentum] ENTRADA SUI @ 1.0252 (21.84 €, apertura)
- 2026-09-30 09:05 [macd_sin_salida] ENTRADA SUI @ 1.0252 (22.16 €, apertura)
- 2026-09-30 09:05 [macd_momentum_regimen] ENTRADA SUI @ 1.0252 (22.13 €, apertura)
- 2026-09-30 09:05 [macd_momentum_evento] ENTRADA SUI @ 1.0252 (22.15 €, apertura)
- 2026-09-30 09:05 [c_banda_atr] ENTRADA LTC @ 58.93 (22.31 €, apertura)
- 2026-09-30 09:05 [c_banda_atr_regimen] ENTRADA LTC @ 58.93 (22.52 €, apertura)
- 2026-09-30 09:05 [c_banda_atr_evento] ENTRADA LTC @ 58.93 (22.38 €, apertura)
- 2026-09-30 09:05 [macd_momentum] ENTRADA UNI @ 7.7773 (21.84 €, apertura)
- 2026-09-30 09:05 [macd_sin_salida] ENTRADA UNI @ 7.7773 (22.16 €, apertura)
- 2026-09-30 09:05 [macd_momentum_regimen] ENTRADA UNI @ 7.7773 (22.13 €, apertura)
- 2026-09-30 09:05 [macd_momentum_evento] ENTRADA UNI @ 7.7773 (22.15 €, apertura)
- 2026-09-30 09:05 [macd_momentum] ENTRADA DOGE @ 0.0825757 (21.84 €, apertura)
- 2026-09-30 09:05 [macd_sin_salida] ENTRADA DOGE @ 0.0825757 (22.16 €, apertura)
- 2026-09-30 09:05 [macd_momentum_regimen] ENTRADA DOGE @ 0.0825757 (22.13 €, apertura)
- 2026-09-30 09:05 [macd_momentum_evento] ENTRADA DOGE @ 0.0825757 (22.15 €, apertura)
- 2026-09-30 09:10 [macd_momentum] CIERRE ICP momentum perdido bruto +0.50% neto -0.00%
- 2026-09-30 09:10 [macd_momentum_evento] CIERRE ICP momentum perdido bruto +0.50% neto -0.00%
- 2026-09-30 09:05 [estocastico_rebote] ENTRADA TRX @ 0.297786 (22.19 €, apertura)
- 2026-09-30 09:05 [macd_momentum] ENTRADA SEI @ 0.06548 (21.84 €, apertura)
- 2026-09-30 09:05 [macd_sin_salida] ENTRADA SEI @ 0.06548 (22.16 €, apertura)
- 2026-09-30 09:05 [macd_momentum_regimen] ENTRADA SEI @ 0.06548 (22.13 €, apertura)
- 2026-09-30 09:05 [macd_momentum_evento] ENTRADA SEI @ 0.06548 (22.15 €, apertura)
- 2026-09-30 09:05 [c_banda_atr] ENTRADA MINA @ 0.1256 (22.31 €, apertura)
- 2026-09-30 09:05 [c_banda_atr_regimen] ENTRADA MINA @ 0.1256 (22.52 €, apertura)
- 2026-09-30 09:05 [c_banda_atr_evento] ENTRADA MINA @ 0.1256 (22.38 €, apertura)
- 2026-09-30 09:05 [ruptura_volumen] ENTRADA SHIB @ 5.108e-06 (22.12 €, apertura)
- 2026-09-30 09:05 [ruptura_volumen_regimen] ENTRADA SHIB @ 5.108e-06 (22.36 €, apertura)
- 2026-09-30 09:05 [ruptura_volumen_evento] ENTRADA SHIB @ 5.108e-06 (22.26 €, apertura)
- 2026-09-30 09:05 [c_banda_atr] ENTRADA GRT @ 0.0253 (22.31 €, apertura)
- 2026-09-30 09:05 [c_banda_atr_regimen] ENTRADA GRT @ 0.0253 (22.52 €, apertura)
- 2026-09-30 09:05 [c_banda_atr_evento] ENTRADA GRT @ 0.0253 (22.38 €, apertura)
- 2026-09-30 09:10 [macd_momentum] CIERRE ASTER momentum perdido bruto +0.92% neto +0.42%
- 2026-09-30 09:10 [macd_momentum_evento] CIERRE ASTER momentum perdido bruto +0.92% neto +0.42%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
