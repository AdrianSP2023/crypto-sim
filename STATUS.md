# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 09:51 UTC · vueltas 188 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.29 € (-2.70%) | 168 | 12 | 36% | -0.001% | -0.656% | -0.778% | -25.26 € |
| reversion_bb | 920.01 € (-0.46%) | 21 | 9 | 38% | +0.128% | -0.972% | -1.079% | -4.71 € |
| ruptura_volumen | 885.95 € (-4.14%) | 206 | 7 | 23% | -0.188% | -0.815% | -0.925% | -38.17 € |
| rebote_extremo | 924.04 € (-0.02%) | 5 | 4 | 60% | +0.548% | -0.552% | -0.686% | -0.64 € |
| pullback_tendencia | 897.01 € (-2.95%) | 123 | 1 | 15% | -0.256% | -0.970% | -1.075% | -27.23 € |
| macd_momentum | 885.36 € (-4.21%) | 295 | 4 | 22% | +0.003% | -0.585% | -0.694% | -39.16 € |
| estocastico_rebote | 888.26 € (-3.89%) | 222 | 35 | 34% | -0.104% | -0.722% | -0.838% | -36.56 € |
| ruptura_estricta | 890.83 € (-3.61%) | 121 | 3 | 26% | -0.481% | -1.199% | -1.325% | -33.21 € |
| macd_sin_salida | 889.01 € (-3.81%) | 219 | 5 | 37% | -0.085% | -0.705% | -0.819% | -35.25 € |
| c_banda_atr_tope | 915.08 € (-0.99%) | 38 | 4 | 29% | +0.062% | -1.038% | -1.154% | -9.08 € |
| ruptura_volumen_tope | 912.92 € (-1.22%) | 59 | 4 | 29% | +0.121% | -0.826% | -0.944% | -11.22 € |
| c_banda_atr_regimen | 902.81 € (-2.32%) | 108 | 1 | 34% | -0.118% | -0.859% | -1.000% | -21.32 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 905.28 € (-2.05%) | 135 | 12 | 37% | +0.075% | -0.621% | -0.734% | -19.27 € |
| macd_momentum_evento | 890.27 € (-3.68%) | 248 | 4 | 20% | -0.002% | -0.608% | -0.711% | -34.26 € |
| ruptura_volumen_evento | 898.56 € (-2.78%) | 156 | 7 | 24% | -0.047% | -0.717% | -0.814% | -25.55 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 09:50 | estocastico_rebote | SPX | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 09:50 | pullback_tendencia | LTC | rotura de tendencia | -0.15% | -0.65% | -0.15 |
| 2026-10-01 09:50 | rebote_extremo | SPX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-10-01 09:45 | ruptura_volumen_evento | NIGHT | take-profit | +3.81% | +3.31% | +0.74 |
| 2026-10-01 09:45 | ruptura_volumen_tope | NIGHT | take-profit | +3.81% | +3.31% | +0.76 |
| 2026-10-01 09:45 | estocastico_rebote | AVAX | timeout | -0.17% | -0.67% | -0.15 |
| 2026-10-01 09:45 | ruptura_volumen | NIGHT | take-profit | +3.81% | +3.31% | +0.73 |
| 2026-10-01 09:40 | estocastico_rebote | MINA | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 09:35 | macd_momentum_evento | NIGHT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 09:35 | macd_momentum_evento | UNI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 09:35 | macd_sin_salida | NIGHT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 09:35 | macd_sin_salida | UNI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 09:35 | macd_momentum | NIGHT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 09:35 | macd_momentum | UNI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 09:30 | c_banda_atr_evento | UNI | take-profit | +2.32% | +1.82% | +0.41 |

## Eventos de la última vuelta

- 2026-10-01 09:50 [pullback_tendencia] CIERRE LTC rotura de tendencia bruto -0.15% neto -0.65%
- 2026-10-01 09:50 [rebote_extremo] CIERRE SPX take-profit bruto +2.00% neto +0.90%
- 2026-10-01 09:50 [estocastico_rebote] CIERRE SPX take-profit bruto +1.80% neto +1.30%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
