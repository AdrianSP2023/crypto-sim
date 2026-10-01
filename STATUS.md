# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 14:41 UTC · vueltas 243 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 893.45 € (-3.33%) | 199 | 18 | 35% | -0.046% | -0.677% | -0.803% | -30.75 € |
| reversion_bb | 917.99 € (-0.68%) | 33 | 10 | 39% | +0.133% | -0.967% | -1.063% | -7.36 € |
| ruptura_volumen | 880.47 € (-4.74%) | 236 | 7 | 23% | -0.211% | -0.822% | -0.929% | -43.95 € |
| rebote_extremo | 922.25 € (-0.22%) | 10 | 1 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 894.07 € (-3.26%) | 138 | 3 | 14% | -0.274% | -0.965% | -1.070% | -30.34 € |
| macd_momentum | 878.35 € (-4.97%) | 342 | 15 | 20% | -0.023% | -0.600% | -0.710% | -46.32 € |
| estocastico_rebote | 878.31 € (-4.97%) | 272 | 13 | 30% | -0.164% | -0.759% | -0.872% | -46.75 € |
| ruptura_estricta | 886.70 € (-4.06%) | 132 | 6 | 23% | -0.548% | -1.248% | -1.371% | -37.57 € |
| macd_sin_salida | 883.11 € (-4.45%) | 249 | 15 | 34% | -0.130% | -0.735% | -0.851% | -41.62 € |
| c_banda_atr_tope | 912.74 € (-1.24%) | 47 | 4 | 28% | +0.005% | -1.057% | -1.172% | -11.42 € |
| ruptura_volumen_tope | 909.45 € (-1.60%) | 74 | 5 | 26% | -0.019% | -0.876% | -0.991% | -14.88 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 899.40 € (-2.69%) | 166 | 18 | 36% | +0.007% | -0.652% | -0.772% | -24.80 € |
| macd_momentum_evento | 883.21 € (-4.44%) | 295 | 15 | 18% | -0.032% | -0.621% | -0.727% | -41.46 € |
| ruptura_volumen_evento | 892.99 € (-3.38%) | 186 | 7 | 24% | -0.100% | -0.742% | -0.838% | -31.41 € |
| rebote_desplome | 924.45 € (+0.02%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.45 € (+0.02%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 14:40 | c_banda_atr_evento | BCH | timeout | -0.21% | -0.71% | -0.16 |
| 2026-10-01 14:40 | c_banda_atr_evento | TAO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 14:40 | c_banda_atr_tope | SHIB | timeout | +0.41% | -0.39% | -0.09 |
| 2026-10-01 14:40 | c_banda_atr_tope | BCH | timeout | -0.21% | -1.01% | -0.23 |
| 2026-10-01 14:40 | c_banda_atr | BCH | timeout | -0.21% | -0.71% | -0.16 |
| 2026-10-01 14:40 | c_banda_atr | TAO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 14:35 | ruptura_volumen_evento | LINK | timeout | -0.05% | -0.55% | -0.12 |
| 2026-10-01 14:35 | ruptura_volumen | LINK | timeout | -0.05% | -0.55% | -0.12 |
| 2026-10-01 14:25 | macd_momentum_evento | APT | momentum perdido | -0.45% | -0.95% | -0.21 |
| 2026-10-01 14:25 | macd_momentum_evento | SEI | momentum perdido | -0.45% | -0.95% | -0.21 |
| 2026-10-01 14:25 | macd_momentum_evento | UNI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 14:25 | c_banda_atr_evento | UNI | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 14:25 | c_banda_atr_tope | UNI | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 14:25 | macd_sin_salida | UNI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 14:25 | macd_momentum | APT | momentum perdido | -0.45% | -0.95% | -0.21 |

## Eventos de la última vuelta

- 2026-10-01 14:35 [macd_momentum] ENTRADA ADA @ 0.219142 (21.95 €, apertura)
- 2026-10-01 14:35 [macd_sin_salida] ENTRADA ADA @ 0.219142 (22.07 €, apertura)
- 2026-10-01 14:35 [macd_momentum_evento] ENTRADA ADA @ 0.219142 (22.07 €, apertura)
- 2026-10-01 14:40 [c_banda_atr] CIERRE TAO take-profit bruto +2.00% neto +1.50%
- 2026-10-01 14:40 [c_banda_atr_evento] CIERRE TAO take-profit bruto +2.00% neto +1.50%
- 2026-10-01 14:40 [c_banda_atr] CIERRE BCH timeout bruto -0.21% neto -0.71%
- 2026-10-01 14:40 [c_banda_atr_tope] CIERRE BCH timeout bruto -0.21% neto -1.01%
- 2026-10-01 14:40 [c_banda_atr_evento] CIERRE BCH timeout bruto -0.21% neto -0.71%
- 2026-10-01 14:35 [pullback_tendencia] ENTRADA PEPE @ 3.881e-06 (22.35 €, apertura)
- 2026-10-01 14:35 [macd_momentum] ENTRADA MINA @ 0.1327 (21.95 €, apertura)
- 2026-10-01 14:35 [macd_momentum_evento] ENTRADA MINA @ 0.1327 (22.07 €, apertura)
- 2026-10-01 14:40 [c_banda_atr_tope] CIERRE SHIB timeout bruto +0.41% neto -0.39%
- 2026-10-01 14:35 [ruptura_volumen] ENTRADA SKY @ 0.07044 (22.01 €, apertura)
- 2026-10-01 14:35 [ruptura_volumen_evento] ENTRADA SKY @ 0.07044 (22.32 €, apertura)
- 2026-10-01 14:35 [macd_momentum] ENTRADA APT @ 0.6826 (21.95 €, apertura)
- 2026-10-01 14:35 [c_banda_atr_tope] ENTRADA APT @ 0.6826 (22.82 €, apertura)
- 2026-10-01 14:35 [macd_momentum_evento] ENTRADA APT @ 0.6826 (22.07 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
