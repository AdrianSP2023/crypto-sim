# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 14:36 UTC · vueltas 242 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 893.33 € (-3.34%) | 197 | 20 | 35% | -0.055% | -0.688% | -0.815% | -30.93 € |
| reversion_bb | 917.63 € (-0.72%) | 33 | 10 | 39% | +0.133% | -0.967% | -1.063% | -7.36 € |
| ruptura_volumen | 880.12 € (-4.77%) | 236 | 6 | 23% | -0.211% | -0.822% | -0.929% | -43.95 € |
| rebote_extremo | 922.22 € (-0.22%) | 10 | 1 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 894.07 € (-3.26%) | 138 | 2 | 14% | -0.274% | -0.965% | -1.070% | -30.34 € |
| macd_momentum | 878.00 € (-5.00%) | 342 | 12 | 20% | -0.023% | -0.600% | -0.710% | -46.32 € |
| estocastico_rebote | 878.10 € (-4.99%) | 272 | 13 | 30% | -0.164% | -0.759% | -0.872% | -46.75 € |
| ruptura_estricta | 886.53 € (-4.08%) | 132 | 6 | 23% | -0.548% | -1.248% | -1.371% | -37.57 € |
| macd_sin_salida | 882.60 € (-4.51%) | 249 | 14 | 34% | -0.130% | -0.735% | -0.851% | -41.62 € |
| c_banda_atr_tope | 913.02 € (-1.21%) | 45 | 5 | 29% | +0.001% | -1.073% | -1.191% | -11.10 € |
| ruptura_volumen_tope | 909.10 € (-1.64%) | 74 | 5 | 26% | -0.019% | -0.876% | -0.991% | -14.88 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 899.27 € (-2.70%) | 164 | 20 | 35% | -0.004% | -0.665% | -0.786% | -24.98 € |
| macd_momentum_evento | 882.86 € (-4.48%) | 295 | 12 | 18% | -0.032% | -0.621% | -0.727% | -41.46 € |
| ruptura_volumen_evento | 892.64 € (-3.42%) | 186 | 6 | 24% | -0.100% | -0.742% | -0.838% | -31.41 € |
| rebote_desplome | 924.50 € (+0.03%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.50 € (+0.03%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 14:35 | ruptura_volumen_evento | LINK | timeout | -0.05% | -0.55% | -0.12 |
| 2026-10-01 14:35 | ruptura_volumen | LINK | timeout | -0.05% | -0.55% | -0.12 |
| 2026-10-01 14:25 | macd_momentum_evento | APT | momentum perdido | -0.45% | -0.95% | -0.21 |
| 2026-10-01 14:25 | macd_momentum_evento | SEI | momentum perdido | -0.45% | -0.95% | -0.21 |
| 2026-10-01 14:25 | macd_momentum_evento | UNI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 14:25 | c_banda_atr_evento | UNI | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 14:25 | c_banda_atr_tope | UNI | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 14:25 | macd_sin_salida | UNI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 14:25 | macd_momentum | APT | momentum perdido | -0.45% | -0.95% | -0.21 |
| 2026-10-01 14:25 | macd_momentum | SEI | momentum perdido | -0.45% | -0.95% | -0.21 |
| 2026-10-01 14:25 | macd_momentum | UNI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 14:25 | c_banda_atr | UNI | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 14:20 | macd_momentum_evento | ZEC | momentum perdido | -0.75% | -1.25% | -0.28 |
| 2026-10-01 14:20 | macd_sin_salida | SKY | timeout | -0.47% | -0.97% | -0.21 |
| 2026-10-01 14:20 | macd_momentum | ZEC | momentum perdido | -0.75% | -1.25% | -0.28 |

## Eventos de la última vuelta

- 2026-10-01 14:35 [ruptura_volumen] CIERRE LINK timeout bruto -0.05% neto -0.55%
- 2026-10-01 14:35 [ruptura_volumen_evento] CIERRE LINK timeout bruto -0.05% neto -0.55%
- 2026-10-01 14:30 [ruptura_volumen] ENTRADA TAO @ 272.125 (22.01 €, apertura)
- 2026-10-01 14:30 [ruptura_estricta] ENTRADA TAO @ 272.125 (22.17 €, apertura)
- 2026-10-01 14:30 [ruptura_volumen_evento] ENTRADA TAO @ 272.125 (22.32 €, apertura)
- 2026-10-01 14:30 [c_banda_atr] ENTRADA FET @ 0.2007 (22.33 €, apertura)
- 2026-10-01 14:30 [c_banda_atr_tope] ENTRADA FET @ 0.2007 (22.83 €, apertura)
- 2026-10-01 14:30 [c_banda_atr_evento] ENTRADA FET @ 0.2007 (22.48 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
