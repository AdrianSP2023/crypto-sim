# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 10:01 UTC · vueltas 190 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.04 € (-2.73%) | 168 | 12 | 36% | -0.001% | -0.656% | -0.778% | -25.26 € |
| reversion_bb | 919.66 € (-0.50%) | 21 | 9 | 38% | +0.128% | -0.972% | -1.079% | -4.71 € |
| ruptura_volumen | 885.80 € (-4.16%) | 206 | 8 | 23% | -0.188% | -0.815% | -0.925% | -38.17 € |
| rebote_extremo | 923.77 € (-0.05%) | 5 | 4 | 60% | +0.548% | -0.552% | -0.686% | -0.64 € |
| pullback_tendencia | 896.85 € (-2.96%) | 124 | 0 | 15% | -0.255% | -0.968% | -1.073% | -27.39 € |
| macd_momentum | 885.12 € (-4.23%) | 297 | 2 | 22% | +0.002% | -0.586% | -0.694% | -39.45 € |
| estocastico_rebote | 886.13 € (-4.12%) | 224 | 33 | 33% | -0.111% | -0.728% | -0.844% | -37.16 € |
| ruptura_estricta | 890.82 € (-3.62%) | 121 | 3 | 26% | -0.481% | -1.199% | -1.325% | -33.21 € |
| macd_sin_salida | 888.88 € (-3.83%) | 219 | 5 | 37% | -0.085% | -0.705% | -0.819% | -35.25 € |
| c_banda_atr_tope | 914.80 € (-1.02%) | 38 | 4 | 29% | +0.062% | -1.038% | -1.154% | -9.08 € |
| ruptura_volumen_tope | 912.75 € (-1.24%) | 59 | 5 | 29% | +0.121% | -0.826% | -0.944% | -11.22 € |
| c_banda_atr_regimen | 902.84 € (-2.32%) | 108 | 1 | 34% | -0.118% | -0.859% | -1.000% | -21.32 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 905.02 € (-2.08%) | 135 | 12 | 37% | +0.075% | -0.621% | -0.734% | -19.27 € |
| macd_momentum_evento | 890.03 € (-3.70%) | 250 | 2 | 20% | -0.003% | -0.608% | -0.711% | -34.54 € |
| ruptura_volumen_evento | 898.40 € (-2.80%) | 156 | 8 | 24% | -0.047% | -0.717% | -0.814% | -25.55 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 10:00 | estocastico_rebote | QNT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 10:00 | pullback_tendencia | WLFI | rotura de tendencia | -0.20% | -0.70% | -0.16 |
| 2026-10-01 09:55 | macd_momentum_evento | LTC | momentum perdido | +0.15% | -0.35% | -0.08 |
| 2026-10-01 09:55 | macd_momentum_evento | TAO | momentum perdido | -0.43% | -0.93% | -0.21 |
| 2026-10-01 09:55 | estocastico_rebote | BTC | timeout | -0.20% | -0.70% | -0.16 |
| 2026-10-01 09:55 | macd_momentum | LTC | momentum perdido | +0.15% | -0.35% | -0.08 |
| 2026-10-01 09:55 | macd_momentum | TAO | momentum perdido | -0.43% | -0.93% | -0.21 |
| 2026-10-01 09:50 | estocastico_rebote | SPX | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 09:50 | pullback_tendencia | LTC | rotura de tendencia | -0.15% | -0.65% | -0.15 |
| 2026-10-01 09:50 | rebote_extremo | SPX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-10-01 09:45 | ruptura_volumen_evento | NIGHT | take-profit | +3.81% | +3.31% | +0.74 |
| 2026-10-01 09:45 | ruptura_volumen_tope | NIGHT | take-profit | +3.81% | +3.31% | +0.76 |
| 2026-10-01 09:45 | estocastico_rebote | AVAX | timeout | -0.17% | -0.67% | -0.15 |
| 2026-10-01 09:45 | ruptura_volumen | NIGHT | take-profit | +3.81% | +3.31% | +0.73 |
| 2026-10-01 09:40 | estocastico_rebote | MINA | take-profit | +1.80% | +1.30% | +0.29 |

## Eventos de la última vuelta

- 2026-10-01 10:00 [estocastico_rebote] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:00 [pullback_tendencia] CIERRE WLFI rotura de tendencia bruto -0.20% neto -0.70%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
