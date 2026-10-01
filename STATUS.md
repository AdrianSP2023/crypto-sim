# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 12:01 UTC · vueltas 211 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.03 € (-2.84%) | 177 | 26 | 35% | -0.037% | -0.685% | -0.809% | -27.73 € |
| reversion_bb | 919.26 € (-0.54%) | 27 | 6 | 44% | +0.214% | -0.886% | -0.990% | -5.52 € |
| ruptura_volumen | 884.97 € (-4.25%) | 216 | 12 | 23% | -0.195% | -0.815% | -0.925% | -40.01 € |
| rebote_extremo | 922.08 € (-0.23%) | 9 | 0 | 44% | +0.060% | -1.040% | -1.178% | -2.16 € |
| pullback_tendencia | 896.30 € (-3.02%) | 126 | 2 | 15% | -0.265% | -0.975% | -1.082% | -28.00 € |
| macd_momentum | 884.34 € (-4.32%) | 308 | 17 | 21% | -0.012% | -0.597% | -0.705% | -41.61 € |
| estocastico_rebote | 880.71 € (-4.71%) | 259 | 7 | 31% | -0.149% | -0.750% | -0.860% | -44.01 € |
| ruptura_estricta | 890.09 € (-3.70%) | 125 | 8 | 25% | -0.501% | -1.212% | -1.337% | -34.64 € |
| macd_sin_salida | 889.60 € (-3.75%) | 224 | 20 | 36% | -0.092% | -0.709% | -0.824% | -36.24 € |
| c_banda_atr_tope | 913.93 € (-1.12%) | 42 | 5 | 29% | -0.003% | -1.103% | -1.222% | -10.66 € |
| ruptura_volumen_tope | 911.80 € (-1.35%) | 66 | 4 | 29% | +0.072% | -0.828% | -0.943% | -12.56 € |
| c_banda_atr_regimen | 902.48 € (-2.35%) | 109 | 0 | 34% | -0.130% | -0.870% | -1.010% | -21.77 € |
| macd_momentum_regimen | 894.22 € (-3.25%) | 203 | 2 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.59 € (-4.07%) | 177 | 5 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 904.01 € (-2.19%) | 144 | 26 | 36% | +0.025% | -0.658% | -0.774% | -21.76 € |
| macd_momentum_evento | 889.24 € (-3.79%) | 261 | 17 | 19% | -0.019% | -0.620% | -0.723% | -36.72 € |
| ruptura_volumen_evento | 897.56 € (-2.89%) | 166 | 12 | 24% | -0.064% | -0.723% | -0.821% | -27.42 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 12:00 | ruptura_volumen_evento | SKY | timeout | +1.54% | +1.04% | +0.23 |
| 2026-10-01 12:00 | ruptura_volumen_tope | SKY | timeout | +1.54% | +1.04% | +0.24 |
| 2026-10-01 12:00 | ruptura_volumen | SKY | timeout | +1.54% | +1.04% | +0.23 |
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

## Eventos de la última vuelta

- 2026-10-01 11:55 [macd_momentum] ENTRADA UNI @ 7.9879 (22.07 €, apertura)
- 2026-10-01 11:55 [macd_sin_salida] ENTRADA UNI @ 7.9879 (22.20 €, apertura)
- 2026-10-01 11:55 [macd_momentum_regimen] ENTRADA UNI @ 7.9879 (22.35 €, apertura)
- 2026-10-01 11:55 [macd_momentum_evento] ENTRADA UNI @ 7.9879 (22.19 €, apertura)
- 2026-10-01 11:55 [ruptura_volumen] ENTRADA FET @ 0.2108 (22.10 €, apertura)
- 2026-10-01 11:55 [ruptura_estricta] ENTRADA FET @ 0.2108 (22.24 €, apertura)
- 2026-10-01 11:55 [ruptura_volumen_regimen] ENTRADA FET @ 0.2108 (22.16 €, apertura)
- 2026-10-01 11:55 [ruptura_volumen_evento] ENTRADA FET @ 0.2108 (22.41 €, apertura)
- 2026-10-01 11:55 [macd_momentum] ENTRADA ALGO @ 0.11224 (22.07 €, apertura)
- 2026-10-01 11:55 [macd_sin_salida] ENTRADA ALGO @ 0.11224 (22.20 €, apertura)
- 2026-10-01 11:55 [macd_momentum_regimen] ENTRADA ALGO @ 0.11224 (22.35 €, apertura)
- 2026-10-01 11:55 [macd_momentum_evento] ENTRADA ALGO @ 0.11224 (22.19 €, apertura)
- 2026-10-01 11:55 [ruptura_volumen_regimen] ENTRADA PEPE @ 3.87e-06 (22.16 €, apertura)
- 2026-10-01 11:55 [ruptura_volumen] ENTRADA OP @ 0.1149 (22.10 €, apertura)
- 2026-10-01 11:55 [ruptura_volumen_regimen] ENTRADA OP @ 0.1149 (22.16 €, apertura)
- 2026-10-01 11:55 [ruptura_volumen_evento] ENTRADA OP @ 0.1149 (22.41 €, apertura)
- 2026-10-01 11:55 [ruptura_volumen_regimen] ENTRADA KSM @ 4.7 (22.16 €, apertura)
- 2026-10-01 11:55 [ruptura_volumen_regimen] ENTRADA KAS @ 0.0382 (22.16 €, apertura)
- 2026-10-01 12:00 [ruptura_volumen] CIERRE SKY timeout bruto +1.54% neto +1.04%
- 2026-10-01 12:00 [ruptura_volumen_tope] CIERRE SKY timeout bruto +1.54% neto +1.04%
- 2026-10-01 12:00 [ruptura_volumen_evento] CIERRE SKY timeout bruto +1.54% neto +1.04%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
