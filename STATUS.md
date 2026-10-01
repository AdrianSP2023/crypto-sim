# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 08:01 UTC · vueltas 166 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.99 € (-2.73%) | 159 | 9 | 36% | +0.007% | -0.657% | -0.780% | -23.95 € |
| reversion_bb | 919.19 € (-0.55%) | 20 | 9 | 40% | +0.134% | -0.966% | -1.078% | -4.46 € |
| ruptura_volumen | 885.72 € (-4.17%) | 204 | 0 | 23% | -0.203% | -0.831% | -0.940% | -38.53 € |
| rebote_extremo | 924.12 € (-0.01%) | 3 | 3 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 898.07 € (-2.83%) | 119 | 1 | 16% | -0.244% | -0.965% | -1.071% | -26.23 € |
| macd_momentum | 885.17 € (-4.23%) | 289 | 1 | 22% | -0.006% | -0.597% | -0.705% | -39.11 € |
| estocastico_rebote | 886.83 € (-4.05%) | 206 | 36 | 34% | -0.091% | -0.718% | -0.835% | -33.77 € |
| ruptura_estricta | 892.09 € (-3.48%) | 114 | 8 | 27% | -0.430% | -1.161% | -1.287% | -30.34 € |
| macd_sin_salida | 890.06 € (-3.70%) | 207 | 9 | 37% | -0.068% | -0.694% | -0.807% | -32.84 € |
| c_banda_atr_tope | 914.85 € (-1.02%) | 35 | 2 | 26% | -0.052% | -1.152% | -1.273% | -9.28 € |
| ruptura_volumen_tope | 912.66 € (-1.25%) | 57 | 0 | 28% | +0.080% | -0.884% | -0.999% | -11.58 € |
| c_banda_atr_regimen | 903.27 € (-2.27%) | 104 | 5 | 36% | -0.086% | -0.837% | -0.978% | -20.01 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 904.97 € (-2.08%) | 126 | 9 | 38% | +0.090% | -0.619% | -0.734% | -17.95 € |
| macd_momentum_evento | 890.07 € (-3.70%) | 242 | 1 | 19% | -0.013% | -0.622% | -0.725% | -34.20 € |
| ruptura_volumen_evento | 898.32 € (-2.80%) | 154 | 0 | 24% | -0.065% | -0.736% | -0.833% | -25.91 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 08:00 | macd_momentum_evento | WLFI | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 08:00 | c_banda_atr_evento | POL | timeout | -0.96% | -1.46% | -0.33 |
| 2026-10-01 08:00 | macd_momentum_regimen | WLFI | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 08:00 | c_banda_atr_regimen | POL | timeout | -0.96% | -1.46% | -0.33 |
| 2026-10-01 08:00 | estocastico_rebote | SEI | stop-loss | -1.55% | -2.05% | -0.46 |
| 2026-10-01 08:00 | macd_momentum | WLFI | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 08:00 | c_banda_atr | POL | timeout | -0.96% | -1.46% | -0.33 |
| 2026-10-01 07:55 | ruptura_volumen_evento | BTC | timeout | -0.85% | -1.35% | -0.30 |
| 2026-10-01 07:55 | ruptura_volumen_regimen | BTC | timeout | -0.85% | -1.35% | -0.30 |
| 2026-10-01 07:55 | macd_sin_salida | SEI | timeout | -0.90% | -1.40% | -0.32 |
| 2026-10-01 07:55 | macd_sin_salida | LTC | timeout | -0.75% | -1.25% | -0.28 |
| 2026-10-01 07:55 | ruptura_estricta | VVV | timeout | +0.38% | -0.12% | -0.03 |
| 2026-10-01 07:55 | ruptura_volumen | BTC | timeout | -0.85% | -1.35% | -0.30 |
| 2026-10-01 07:50 | ruptura_volumen_evento | ASTER | timeout | -0.38% | -0.88% | -0.20 |
| 2026-10-01 07:50 | ruptura_volumen_regimen | ASTER | timeout | -0.38% | -0.88% | -0.20 |

## Eventos de la última vuelta

- 2026-10-01 08:00 [c_banda_atr] CIERRE POL timeout bruto -0.96% neto -1.46%
- 2026-10-01 08:00 [c_banda_atr_regimen] CIERRE POL timeout bruto -0.96% neto -1.46%
- 2026-10-01 08:00 [c_banda_atr_evento] CIERRE POL timeout bruto -0.96% neto -1.46%
- 2026-10-01 08:00 [macd_momentum] CIERRE WLFI momentum perdido bruto +0.00% neto -0.50%
- 2026-10-01 08:00 [macd_momentum_regimen] CIERRE WLFI momentum perdido bruto +0.00% neto -0.50%
- 2026-10-01 08:00 [macd_momentum_evento] CIERRE WLFI momentum perdido bruto +0.00% neto -0.50%
- 2026-10-01 07:55 [estocastico_rebote] ENTRADA TRUMP @ 1.814 (22.27 €, apertura)
- 2026-10-01 08:00 [estocastico_rebote] CIERRE SEI stop-loss bruto -1.55% neto -2.05%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
