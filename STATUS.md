# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 14:31 UTC · vueltas 241 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 893.36 € (-3.34%) | 197 | 19 | 35% | -0.055% | -0.688% | -0.815% | -30.93 € |
| reversion_bb | 917.84 € (-0.69%) | 33 | 10 | 39% | +0.133% | -0.967% | -1.063% | -7.36 € |
| ruptura_volumen | 880.42 € (-4.74%) | 235 | 6 | 23% | -0.212% | -0.823% | -0.931% | -43.82 € |
| rebote_extremo | 922.29 € (-0.21%) | 10 | 1 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 894.05 € (-3.27%) | 138 | 2 | 14% | -0.274% | -0.965% | -1.070% | -30.34 € |
| macd_momentum | 878.09 € (-4.99%) | 342 | 12 | 20% | -0.023% | -0.600% | -0.710% | -46.32 € |
| estocastico_rebote | 877.95 € (-5.01%) | 272 | 13 | 30% | -0.164% | -0.759% | -0.872% | -46.75 € |
| ruptura_estricta | 886.60 € (-4.07%) | 132 | 5 | 23% | -0.548% | -1.248% | -1.371% | -37.57 € |
| macd_sin_salida | 882.55 € (-4.51%) | 249 | 14 | 34% | -0.130% | -0.735% | -0.851% | -41.62 € |
| c_banda_atr_tope | 913.13 € (-1.20%) | 45 | 4 | 29% | +0.001% | -1.073% | -1.191% | -11.10 € |
| ruptura_volumen_tope | 909.39 € (-1.61%) | 74 | 5 | 26% | -0.019% | -0.876% | -0.991% | -14.88 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 899.31 € (-2.70%) | 164 | 19 | 35% | -0.004% | -0.665% | -0.786% | -24.98 € |
| macd_momentum_evento | 882.95 € (-4.47%) | 295 | 12 | 18% | -0.032% | -0.621% | -0.727% | -41.46 € |
| ruptura_volumen_evento | 892.94 € (-3.39%) | 185 | 6 | 24% | -0.100% | -0.743% | -0.839% | -31.29 € |
| rebote_desplome | 924.40 € (+0.02%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.40 € (+0.02%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-01 14:15 | ruptura_volumen_evento | MINA | timeout | -0.15% | -0.65% | -0.15 |
| 2026-10-01 14:15 | ruptura_volumen_evento | AAVE | stop-loss | -1.20% | -1.70% | -0.38 |

## Eventos de la última vuelta

- 2026-10-01 14:25 [pullback_tendencia] ENTRADA LINK @ 12.7084 (22.35 €, apertura)
- 2026-10-01 14:25 [macd_momentum] ENTRADA LINK @ 12.7084 (21.95 €, apertura)
- 2026-10-01 14:25 [macd_sin_salida] ENTRADA LINK @ 12.7084 (22.07 €, apertura)
- 2026-10-01 14:25 [macd_momentum_evento] ENTRADA LINK @ 12.7084 (22.07 €, apertura)
- 2026-10-01 14:25 [ruptura_volumen] ENTRADA UNI @ 8.1736 (22.01 €, apertura)
- 2026-10-01 14:25 [ruptura_estricta] ENTRADA UNI @ 8.1736 (22.17 €, apertura)
- 2026-10-01 14:25 [ruptura_volumen_tope] ENTRADA UNI @ 8.1736 (22.73 €, apertura)
- 2026-10-01 14:25 [ruptura_volumen_evento] ENTRADA UNI @ 8.1736 (22.32 €, apertura)
- 2026-10-01 14:25 [ruptura_volumen] ENTRADA TON @ 1.34 (22.01 €, apertura)
- 2026-10-01 14:25 [ruptura_volumen_tope] ENTRADA TON @ 1.34 (22.73 €, apertura)
- 2026-10-01 14:25 [ruptura_volumen_evento] ENTRADA TON @ 1.34 (22.32 €, apertura)
- 2026-10-01 14:25 [macd_momentum] ENTRADA SKY @ 0.07021 (21.95 €, apertura)
- 2026-10-01 14:25 [macd_sin_salida] ENTRADA SKY @ 0.07021 (22.07 €, apertura)
- 2026-10-01 14:25 [macd_momentum_evento] ENTRADA SKY @ 0.07021 (22.07 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
