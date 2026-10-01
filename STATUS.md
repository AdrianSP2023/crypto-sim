# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 09:26 UTC · vueltas 183 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.09 € (-2.72%) | 167 | 13 | 35% | -0.015% | -0.671% | -0.793% | -25.67 € |
| reversion_bb | 920.41 € (-0.41%) | 21 | 9 | 38% | +0.128% | -0.972% | -1.079% | -4.71 € |
| ruptura_volumen | 885.13 € (-4.23%) | 205 | 3 | 23% | -0.208% | -0.835% | -0.945% | -38.90 € |
| rebote_extremo | 924.26 € (+0.00%) | 4 | 5 | 50% | +0.185% | -0.915% | -1.054% | -0.84 € |
| pullback_tendencia | 897.16 € (-2.93%) | 122 | 1 | 16% | -0.257% | -0.973% | -1.078% | -27.09 € |
| macd_momentum | 884.80 € (-4.27%) | 293 | 6 | 22% | -0.011% | -0.600% | -0.708% | -39.83 € |
| estocastico_rebote | 888.54 € (-3.86%) | 219 | 35 | 33% | -0.122% | -0.741% | -0.857% | -36.99 € |
| ruptura_estricta | 890.71 € (-3.63%) | 121 | 3 | 26% | -0.481% | -1.199% | -1.325% | -33.21 € |
| macd_sin_salida | 888.50 € (-3.87%) | 216 | 8 | 36% | -0.105% | -0.726% | -0.839% | -35.80 € |
| c_banda_atr_tope | 915.41 € (-0.96%) | 37 | 5 | 27% | +0.001% | -1.099% | -1.216% | -9.36 € |
| ruptura_volumen_tope | 912.05 € (-1.32%) | 58 | 3 | 28% | +0.057% | -0.898% | -1.015% | -11.97 € |
| c_banda_atr_regimen | 902.94 € (-2.30%) | 108 | 1 | 34% | -0.118% | -0.859% | -1.000% | -21.32 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 905.08 € (-2.07%) | 134 | 13 | 37% | +0.058% | -0.639% | -0.753% | -19.69 € |
| macd_momentum_evento | 889.70 € (-3.74%) | 246 | 6 | 19% | -0.018% | -0.625% | -0.728% | -34.92 € |
| ruptura_volumen_evento | 897.72 € (-2.87%) | 155 | 3 | 24% | -0.072% | -0.743% | -0.840% | -26.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 09:15 | c_banda_atr_evento | TRX | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 09:15 | c_banda_atr | TRX | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 09:10 | estocastico_rebote | KAS | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 09:10 | estocastico_rebote | MON | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 09:10 | pullback_tendencia | TRX | rotura de tendencia | -0.18% | -0.69% | -0.15 |
| 2026-10-01 09:05 | macd_sin_salida | XDC | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 09:05 | estocastico_rebote | LTC | timeout | -0.02% | -0.52% | -0.12 |
| 2026-10-01 09:05 | pullback_tendencia | QNT | rotura de tendencia | -1.20% | -1.70% | -0.38 |
| 2026-10-01 09:00 | estocastico_rebote | VVV | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 08:55 | macd_momentum_evento | XDC | momentum perdido | -0.76% | -1.26% | -0.28 |
| 2026-10-01 08:55 | macd_momentum | XDC | momentum perdido | -0.76% | -1.26% | -0.28 |
| 2026-10-01 08:50 | c_banda_atr_evento | LTC | timeout | -0.60% | -1.10% | -0.25 |
| 2026-10-01 08:50 | c_banda_atr_regimen | LTC | timeout | -0.60% | -1.10% | -0.25 |
| 2026-10-01 08:50 | c_banda_atr_tope | HYPE | timeout | -0.11% | -1.21% | -0.28 |
| 2026-10-01 08:50 | estocastico_rebote | UNI | take-profit | +1.80% | +1.30% | +0.29 |

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
