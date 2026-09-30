# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 02:11 UTC · vueltas 173 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.04 € (-2.29%) | 100 | 19 | 29% | -0.258% | -1.019% | -1.160% | -23.39 € |
| reversion_bb | 919.58 € (-0.50%) | 28 | 6 | 50% | +0.267% | -0.833% | -0.937% | -5.38 € |
| ruptura_volumen | 900.28 € (-2.59%) | 128 | 19 | 23% | -0.148% | -0.852% | -0.979% | -24.92 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.13 € (-1.96%) | 97 | 5 | 26% | -0.049% | -0.818% | -0.947% | -18.20 € |
| macd_momentum | 886.12 € (-4.12%) | 245 | 12 | 17% | -0.111% | -0.718% | -0.832% | -39.90 € |
| estocastico_rebote | 894.35 € (-3.23%) | 178 | 6 | 34% | -0.097% | -0.743% | -0.878% | -30.27 € |
| ruptura_estricta | 908.85 € (-1.66%) | 57 | 11 | 28% | -0.146% | -1.104% | -1.245% | -14.48 € |
| macd_sin_salida | 899.47 € (-2.68%) | 150 | 14 | 30% | -0.096% | -0.770% | -0.895% | -26.41 € |
| c_banda_atr_tope | 911.49 € (-1.38%) | 34 | 2 | 18% | -0.527% | -1.627% | -1.765% | -12.72 € |
| ruptura_volumen_tope | 912.72 € (-1.25%) | 47 | 4 | 19% | -0.032% | -1.087% | -1.212% | -11.75 € |
| c_banda_atr_regimen | 903.12 € (-2.29%) | 69 | 8 | 25% | -0.478% | -1.356% | -1.490% | -21.48 € |
| macd_momentum_regimen | 887.33 € (-3.99%) | 193 | 1 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.22 € (-2.27%) | 101 | 11 | 21% | -0.166% | -0.924% | -1.051% | -21.37 € |
| c_banda_atr_evento | 906.12 € (-1.96%) | 68 | 19 | 25% | -0.412% | -1.301% | -1.447% | -20.32 € |
| macd_momentum_evento | 898.58 € (-2.78%) | 125 | 12 | 13% | -0.250% | -0.961% | -1.073% | -27.47 € |
| ruptura_volumen_evento | 905.82 € (-1.99%) | 69 | 19 | 14% | -0.342% | -1.224% | -1.354% | -19.38 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 02:10 | ruptura_volumen_evento | QNT | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 02:10 | macd_momentum_evento | ICP | momentum perdido | +0.42% | -0.07% | -0.02 |
| 2026-09-30 02:10 | c_banda_atr_regimen | PENGU | take-profit | +2.21% | +1.71% | +0.39 |
| 2026-09-30 02:10 | ruptura_volumen_tope | QNT | take-profit | +2.50% | +2.00% | +0.46 |
| 2026-09-30 02:10 | macd_sin_salida | RENDER | timeout | +1.24% | +0.74% | +0.17 |
| 2026-09-30 02:10 | ruptura_estricta | RAY | timeout | +0.47% | -0.03% | -0.01 |
| 2026-09-30 02:10 | ruptura_estricta | QNT | take-profit | +3.00% | +2.50% | +0.57 |
| 2026-09-30 02:10 | macd_momentum | ICP | momentum perdido | +0.42% | -0.07% | -0.02 |
| 2026-09-30 02:10 | ruptura_volumen | QNT | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 02:05 | ruptura_volumen_evento | XDC | timeout | -1.12% | -1.62% | -0.37 |
| 2026-09-30 02:05 | ruptura_volumen_evento | ALGO | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 02:05 | macd_momentum_evento | BNB | momentum perdido | +0.01% | -0.49% | -0.11 |
| 2026-09-30 02:05 | macd_momentum_evento | JUP | momentum perdido | -0.01% | -0.51% | -0.11 |
| 2026-09-30 02:05 | c_banda_atr_evento | BNB | timeout | +0.21% | -0.59% | -0.14 |
| 2026-09-30 02:05 | c_banda_atr_evento | PENGU | timeout | +1.93% | +1.13% | +0.26 |

## Eventos de la última vuelta

- 2026-09-30 02:05 [ruptura_volumen] ENTRADA QNT @ 252.9 (22.47 €, apertura)
- 2026-09-30 02:10 [ruptura_volumen] CIERRE QNT take-profit bruto +2.50% neto +2.00%
- 2026-09-30 02:05 [ruptura_estricta] ENTRADA QNT @ 252.9 (22.73 €, apertura)
- 2026-09-30 02:10 [ruptura_estricta] CIERRE QNT take-profit bruto +3.00% neto +2.50%
- 2026-09-30 02:05 [ruptura_volumen_tope] ENTRADA QNT @ 252.9 (22.80 €, apertura)
- 2026-09-30 02:10 [ruptura_volumen_tope] CIERRE QNT take-profit bruto +2.50% neto +2.00%
- 2026-09-30 02:05 [ruptura_volumen_evento] ENTRADA QNT @ 252.9 (22.61 €, apertura)
- 2026-09-30 02:10 [ruptura_volumen_evento] CIERRE QNT take-profit bruto +2.50% neto +2.00%
- 2026-09-30 02:05 [ruptura_volumen] ENTRADA DASH @ 54.221 (22.48 €, apertura)
- 2026-09-30 02:05 [ruptura_estricta] ENTRADA DASH @ 54.221 (22.74 €, apertura)
- 2026-09-30 02:05 [ruptura_volumen_tope] ENTRADA DASH @ 54.221 (22.81 €, apertura)
- 2026-09-30 02:05 [ruptura_volumen_evento] ENTRADA DASH @ 54.221 (22.62 €, apertura)
- 2026-09-30 02:10 [macd_momentum] CIERRE ICP momentum perdido bruto +0.42% neto -0.08%
- 2026-09-30 02:10 [macd_momentum_evento] CIERRE ICP momentum perdido bruto +0.42% neto -0.08%
- 2026-09-30 02:10 [macd_sin_salida] CIERRE RENDER timeout bruto +1.24% neto +0.74%
- 2026-09-30 02:10 [ruptura_estricta] CIERRE RAY timeout bruto +0.47% neto -0.03%
- 2026-09-30 02:05 [pullback_tendencia] ENTRADA NIGHT @ 0.02898 (22.65 €, apertura)
- 2026-09-30 02:10 [c_banda_atr_regimen] CIERRE PENGU take-profit bruto +2.21% neto +1.71%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
