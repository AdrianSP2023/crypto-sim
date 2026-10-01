# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 09:41 UTC · vueltas 186 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.72 € (-2.65%) | 168 | 12 | 36% | -0.001% | -0.656% | -0.778% | -25.26 € |
| reversion_bb | 920.26 € (-0.43%) | 21 | 9 | 38% | +0.128% | -0.972% | -1.079% | -4.71 € |
| ruptura_volumen | 886.03 € (-4.13%) | 205 | 7 | 23% | -0.208% | -0.835% | -0.945% | -38.90 € |
| rebote_extremo | 924.22 € (-0.00%) | 4 | 5 | 50% | +0.185% | -0.915% | -1.054% | -0.84 € |
| pullback_tendencia | 897.16 € (-2.93%) | 122 | 1 | 16% | -0.257% | -0.973% | -1.078% | -27.09 € |
| macd_momentum | 885.54 € (-4.19%) | 295 | 4 | 22% | +0.003% | -0.585% | -0.694% | -39.16 € |
| estocastico_rebote | 888.99 € (-3.81%) | 220 | 36 | 34% | -0.113% | -0.731% | -0.848% | -36.70 € |
| ruptura_estricta | 891.02 € (-3.59%) | 121 | 3 | 26% | -0.481% | -1.199% | -1.325% | -33.21 € |
| macd_sin_salida | 889.16 € (-3.80%) | 219 | 5 | 37% | -0.085% | -0.705% | -0.819% | -35.25 € |
| c_banda_atr_tope | 915.34 € (-0.96%) | 38 | 4 | 29% | +0.062% | -1.038% | -1.154% | -9.08 € |
| ruptura_volumen_tope | 912.88 € (-1.23%) | 58 | 5 | 28% | +0.057% | -0.898% | -1.015% | -11.97 € |
| c_banda_atr_regimen | 902.85 € (-2.31%) | 108 | 1 | 34% | -0.118% | -0.859% | -1.000% | -21.32 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 905.71 € (-2.00%) | 135 | 12 | 37% | +0.075% | -0.621% | -0.734% | -19.27 € |
| macd_momentum_evento | 890.45 € (-3.66%) | 248 | 4 | 20% | -0.002% | -0.608% | -0.711% | -34.26 € |
| ruptura_volumen_evento | 898.63 € (-2.77%) | 155 | 7 | 24% | -0.072% | -0.743% | -0.840% | -26.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 09:40 | estocastico_rebote | MINA | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 09:35 | macd_momentum_evento | NIGHT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 09:35 | macd_momentum_evento | UNI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 09:35 | macd_sin_salida | NIGHT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 09:35 | macd_sin_salida | UNI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 09:35 | macd_momentum | NIGHT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 09:35 | macd_momentum | UNI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 09:30 | c_banda_atr_evento | UNI | take-profit | +2.32% | +1.82% | +0.41 |
| 2026-10-01 09:30 | c_banda_atr_tope | UNI | take-profit | +2.32% | +1.22% | +0.28 |
| 2026-10-01 09:30 | macd_sin_salida | WLFI | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-01 09:30 | c_banda_atr | UNI | take-profit | +2.32% | +1.82% | +0.41 |
| 2026-10-01 09:15 | c_banda_atr_evento | TRX | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 09:15 | c_banda_atr | TRX | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 09:10 | estocastico_rebote | KAS | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 09:10 | estocastico_rebote | MON | take-profit | +1.80% | +1.30% | +0.29 |

## Eventos de la última vuelta

- 2026-10-01 09:35 [ruptura_volumen] ENTRADA XRP @ 1.32086 (22.13 €, apertura)
- 2026-10-01 09:35 [ruptura_volumen_tope] ENTRADA XRP @ 1.32086 (22.81 €, apertura)
- 2026-10-01 09:35 [ruptura_volumen_evento] ENTRADA XRP @ 1.32086 (22.45 €, apertura)
- 2026-10-01 09:35 [ruptura_volumen] ENTRADA MINA @ 0.1313 (22.13 €, apertura)
- 2026-10-01 09:40 [estocastico_rebote] CIERRE MINA take-profit bruto +1.80% neto +1.30%
- 2026-10-01 09:35 [ruptura_volumen_evento] ENTRADA MINA @ 0.1313 (22.45 €, apertura)
- 2026-10-01 09:35 [ruptura_volumen] ENTRADA TON @ 1.331 (22.13 €, apertura)
- 2026-10-01 09:35 [ruptura_volumen_evento] ENTRADA TON @ 1.331 (22.45 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
