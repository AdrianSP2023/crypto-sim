# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 11:56 UTC · vueltas 210 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.66 € (-2.88%) | 177 | 26 | 35% | -0.037% | -0.685% | -0.809% | -27.73 € |
| reversion_bb | 919.28 € (-0.54%) | 27 | 6 | 44% | +0.214% | -0.886% | -0.990% | -5.52 € |
| ruptura_volumen | 884.90 € (-4.26%) | 215 | 11 | 23% | -0.203% | -0.824% | -0.934% | -40.24 € |
| rebote_extremo | 922.08 € (-0.23%) | 9 | 0 | 44% | +0.060% | -1.040% | -1.178% | -2.16 € |
| pullback_tendencia | 896.31 € (-3.02%) | 126 | 2 | 15% | -0.265% | -0.975% | -1.082% | -28.00 € |
| macd_momentum | 883.79 € (-4.38%) | 308 | 15 | 21% | -0.012% | -0.597% | -0.705% | -41.61 € |
| estocastico_rebote | 880.60 € (-4.72%) | 259 | 7 | 31% | -0.149% | -0.750% | -0.860% | -44.01 € |
| ruptura_estricta | 889.95 € (-3.71%) | 125 | 7 | 25% | -0.501% | -1.212% | -1.337% | -34.64 € |
| macd_sin_salida | 889.03 € (-3.81%) | 224 | 18 | 36% | -0.092% | -0.709% | -0.824% | -36.24 € |
| c_banda_atr_tope | 913.87 € (-1.12%) | 42 | 5 | 29% | -0.003% | -1.103% | -1.222% | -10.66 € |
| ruptura_volumen_tope | 911.97 € (-1.33%) | 65 | 5 | 28% | +0.049% | -0.857% | -0.972% | -12.80 € |
| c_banda_atr_regimen | 902.48 € (-2.35%) | 109 | 0 | 34% | -0.130% | -0.870% | -1.010% | -21.77 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 903.64 € (-2.23%) | 144 | 26 | 36% | +0.025% | -0.658% | -0.774% | -21.76 € |
| macd_momentum_evento | 888.68 € (-3.85%) | 261 | 15 | 19% | -0.019% | -0.620% | -0.723% | -36.72 € |
| ruptura_volumen_evento | 897.49 € (-2.89%) | 165 | 11 | 24% | -0.074% | -0.734% | -0.832% | -27.65 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 11:55 | ruptura_estricta | NIGHT | stop-loss | -2.00% | -2.50% | -0.56 |
| 2026-10-01 11:55 | pullback_tendencia | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 11:50 | ruptura_volumen_evento | BNB | timeout | +0.16% | -0.34% | -0.08 |
| 2026-10-01 11:50 | macd_sin_salida | MINA | timeout | +1.00% | +0.50% | +0.11 |
| 2026-10-01 11:50 | ruptura_estricta | TRX | timeout | -1.37% | -1.87% | -0.42 |
| 2026-10-01 11:50 | ruptura_estricta | UNI | timeout | -0.01% | -0.51% | -0.11 |
| 2026-10-01 11:50 | estocastico_rebote | INJ | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 11:50 | ruptura_volumen | BNB | timeout | +0.16% | -0.34% | -0.08 |
| 2026-10-01 11:45 | ruptura_volumen_evento | NIGHT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 11:45 | c_banda_atr_evento | SKY | take-profit | +2.03% | +1.53% | +0.35 |
| 2026-10-01 11:45 | c_banda_atr_evento | KSM | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 11:45 | ruptura_volumen_tope | NIGHT | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 11:45 | c_banda_atr_tope | KSM | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-10-01 11:45 | estocastico_rebote | KSM | take-profit | +1.98% | +1.48% | +0.33 |
| 2026-10-01 11:45 | ruptura_volumen | NIGHT | stop-loss | -1.20% | -1.70% | -0.38 |

## Eventos de la última vuelta

- 2026-10-01 11:50 [ruptura_volumen] ENTRADA DOGE @ 0.0838962 (22.10 €, apertura)
- 2026-10-01 11:50 [ruptura_estricta] ENTRADA DOGE @ 0.0838962 (22.25 €, apertura)
- 2026-10-01 11:50 [ruptura_volumen_evento] ENTRADA DOGE @ 0.0838962 (22.41 €, apertura)
- 2026-10-01 11:55 [pullback_tendencia] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 11:55 [ruptura_estricta] CIERRE NIGHT stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 11:50 [ruptura_volumen] ENTRADA PEPE @ 3.851e-06 (22.10 €, apertura)
- 2026-10-01 11:50 [ruptura_estricta] ENTRADA PEPE @ 3.851e-06 (22.24 €, apertura)
- 2026-10-01 11:50 [ruptura_volumen_evento] ENTRADA PEPE @ 3.851e-06 (22.41 €, apertura)
- 2026-10-01 11:50 [ruptura_volumen] ENTRADA MON @ 0.02901 (22.10 €, apertura)
- 2026-10-01 11:50 [ruptura_volumen_evento] ENTRADA MON @ 0.02901 (22.41 €, apertura)
- 2026-10-01 11:50 [macd_momentum] ENTRADA MINA @ 0.1307 (22.07 €, apertura)
- 2026-10-01 11:50 [macd_momentum_evento] ENTRADA MINA @ 0.1307 (22.19 €, apertura)
- 2026-10-01 11:50 [c_banda_atr] ENTRADA DASH @ 52.577 (22.41 €, apertura)
- 2026-10-01 11:50 [c_banda_atr_evento] ENTRADA DASH @ 52.577 (22.56 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
