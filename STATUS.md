# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 09:31 UTC · vueltas 184 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.05 € (-2.72%) | 168 | 12 | 36% | -0.001% | -0.656% | -0.778% | -25.26 € |
| reversion_bb | 920.21 € (-0.44%) | 21 | 9 | 38% | +0.128% | -0.972% | -1.079% | -4.71 € |
| ruptura_volumen | 885.62 € (-4.18%) | 205 | 4 | 23% | -0.208% | -0.835% | -0.945% | -38.90 € |
| rebote_extremo | 924.26 € (+0.00%) | 4 | 5 | 50% | +0.185% | -0.915% | -1.054% | -0.84 € |
| pullback_tendencia | 897.16 € (-2.93%) | 122 | 1 | 16% | -0.257% | -0.973% | -1.078% | -27.09 € |
| macd_momentum | 885.25 € (-4.22%) | 293 | 6 | 22% | -0.011% | -0.600% | -0.708% | -39.83 € |
| estocastico_rebote | 888.43 € (-3.87%) | 219 | 36 | 33% | -0.122% | -0.741% | -0.857% | -36.99 € |
| ruptura_estricta | 890.89 € (-3.61%) | 121 | 3 | 26% | -0.481% | -1.199% | -1.325% | -33.21 € |
| macd_sin_salida | 888.83 € (-3.83%) | 217 | 7 | 36% | -0.105% | -0.725% | -0.839% | -35.91 € |
| c_banda_atr_tope | 915.24 € (-0.97%) | 38 | 4 | 29% | +0.062% | -1.038% | -1.154% | -9.08 € |
| ruptura_volumen_tope | 912.56 € (-1.26%) | 58 | 4 | 28% | +0.057% | -0.898% | -1.015% | -11.97 € |
| c_banda_atr_regimen | 902.89 € (-2.31%) | 108 | 1 | 34% | -0.118% | -0.859% | -1.000% | -21.32 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 905.04 € (-2.08%) | 135 | 12 | 37% | +0.075% | -0.621% | -0.734% | -19.27 € |
| macd_momentum_evento | 890.15 € (-3.69%) | 246 | 6 | 19% | -0.018% | -0.625% | -0.728% | -34.92 € |
| ruptura_volumen_evento | 898.22 € (-2.82%) | 155 | 4 | 24% | -0.072% | -0.743% | -0.840% | -26.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 09:30 | c_banda_atr_evento | UNI | take-profit | +2.32% | +1.82% | +0.41 |
| 2026-10-01 09:30 | c_banda_atr_tope | UNI | take-profit | +2.32% | +1.22% | +0.28 |
| 2026-10-01 09:30 | macd_sin_salida | WLFI | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-01 09:30 | c_banda_atr | UNI | take-profit | +2.32% | +1.82% | +0.41 |
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

## Eventos de la última vuelta

- 2026-10-01 09:25 [estocastico_rebote] ENTRADA QNT @ 259.4 (22.18 €, apertura)
- 2026-10-01 09:30 [c_banda_atr] CIERRE UNI take-profit bruto +2.32% neto +1.82%
- 2026-10-01 09:30 [c_banda_atr_tope] CIERRE UNI take-profit bruto +2.32% neto +1.22%
- 2026-10-01 09:30 [c_banda_atr_evento] CIERRE UNI take-profit bruto +2.32% neto +1.82%
- 2026-10-01 09:25 [ruptura_volumen] ENTRADA NIGHT @ 0.03754 (22.13 €, apertura)
- 2026-10-01 09:25 [ruptura_volumen_tope] ENTRADA NIGHT @ 0.03754 (22.81 €, apertura)
- 2026-10-01 09:25 [ruptura_volumen_evento] ENTRADA NIGHT @ 0.03754 (22.45 €, apertura)
- 2026-10-01 09:30 [macd_sin_salida] CIERRE WLFI timeout bruto +0.00% neto -0.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
