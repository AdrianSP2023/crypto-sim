# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 05:51 UTC · vueltas 140 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.35 € (-1.72%) | 130 | 24 | 38% | +0.110% | -0.591% | -0.711% | -17.70 € |
| reversion_bb | 921.57 € (-0.29%) | 17 | 2 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 892.10 € (-3.48%) | 172 | 24 | 23% | -0.199% | -0.851% | -0.959% | -33.38 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 902.57 € (-2.34%) | 95 | 9 | 17% | -0.242% | -1.020% | -1.134% | -22.18 € |
| macd_momentum | 894.93 € (-3.17%) | 245 | 15 | 23% | +0.047% | -0.560% | -0.667% | -31.25 € |
| estocastico_rebote | 902.71 € (-2.33%) | 172 | 14 | 39% | +0.111% | -0.541% | -0.660% | -21.41 € |
| ruptura_estricta | 903.23 € (-2.27%) | 84 | 31 | 27% | -0.398% | -1.212% | -1.344% | -23.48 € |
| macd_sin_salida | 906.87 € (-1.88%) | 160 | 29 | 42% | +0.147% | -0.516% | -0.629% | -19.02 € |
| c_banda_atr_tope | 917.26 € (-0.76%) | 30 | 5 | 30% | +0.135% | -0.965% | -1.091% | -6.68 € |
| ruptura_volumen_tope | 915.30 € (-0.97%) | 46 | 5 | 24% | +0.090% | -0.984% | -1.081% | -10.42 € |
| c_banda_atr_regimen | 912.22 € (-1.30%) | 76 | 21 | 39% | +0.101% | -0.743% | -0.882% | -13.04 € |
| macd_momentum_regimen | 904.01 € (-2.19%) | 159 | 15 | 24% | +0.055% | -0.609% | -0.721% | -22.18 € |
| ruptura_volumen_regimen | 892.95 € (-3.39%) | 145 | 24 | 19% | -0.307% | -0.987% | -1.099% | -32.66 € |
| c_banda_atr_evento | 914.39 € (-1.07%) | 97 | 24 | 40% | +0.252% | -0.520% | -0.627% | -11.66 € |
| macd_momentum_evento | 899.89 € (-2.63%) | 198 | 15 | 20% | +0.051% | -0.582% | -0.682% | -26.30 € |
| ruptura_volumen_evento | 904.79 € (-2.10%) | 122 | 24 | 24% | -0.024% | -0.740% | -0.831% | -20.70 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 05:50 | ruptura_volumen_evento | DASH | timeout | -0.04% | -0.54% | -0.12 |
| 2026-10-01 05:50 | macd_momentum_evento | MINA | momentum perdido | +0.23% | -0.27% | -0.06 |
| 2026-10-01 05:50 | macd_momentum_evento | NEAR | momentum perdido | +1.38% | +0.88% | +0.20 |
| 2026-10-01 05:50 | ruptura_volumen_regimen | DASH | timeout | -0.04% | -0.54% | -0.12 |
| 2026-10-01 05:50 | macd_momentum_regimen | MINA | momentum perdido | +0.23% | -0.27% | -0.06 |
| 2026-10-01 05:50 | macd_momentum_regimen | NEAR | momentum perdido | +1.38% | +0.88% | +0.20 |
| 2026-10-01 05:50 | macd_sin_salida | POL | timeout | +0.32% | -0.18% | -0.04 |
| 2026-10-01 05:50 | ruptura_estricta | USELESS | take-profit | +3.00% | +2.50% | +0.56 |
| 2026-10-01 05:50 | ruptura_estricta | NIGHT | stop-loss | -2.00% | -2.50% | -0.56 |
| 2026-10-01 05:50 | macd_momentum | MINA | momentum perdido | +0.23% | -0.27% | -0.06 |
| 2026-10-01 05:50 | macd_momentum | NEAR | momentum perdido | +1.38% | +0.88% | +0.20 |
| 2026-10-01 05:50 | ruptura_volumen | DASH | timeout | -0.04% | -0.54% | -0.12 |
| 2026-10-01 05:45 | ruptura_volumen_evento | SEI | timeout | -0.14% | -0.64% | -0.14 |
| 2026-10-01 05:45 | ruptura_volumen_evento | TON | timeout | +0.07% | -0.42% | -0.10 |
| 2026-10-01 05:45 | ruptura_volumen_evento | MON | take-profit | +2.50% | +2.00% | +0.45 |

## Eventos de la última vuelta

- 2026-10-01 05:50 [macd_momentum] CIERRE NEAR momentum perdido bruto +1.38% neto +0.88%
- 2026-10-01 05:50 [macd_momentum_regimen] CIERRE NEAR momentum perdido bruto +1.38% neto +0.88%
- 2026-10-01 05:50 [macd_momentum_evento] CIERRE NEAR momentum perdido bruto +1.38% neto +0.88%
- 2026-10-01 05:45 [estocastico_rebote] ENTRADA XLM @ 0.201149 (22.57 €, apertura)
- 2026-10-01 05:50 [macd_sin_salida] CIERRE POL timeout bruto +0.32% neto -0.18%
- 2026-10-01 05:45 [ruptura_estricta] ENTRADA XDC @ 0.03161 (22.52 €, apertura)
- 2026-10-01 05:50 [ruptura_estricta] CIERRE NIGHT stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 05:45 [ruptura_volumen] ENTRADA USELESS @ 0.21618 (22.27 €, apertura)
- 2026-10-01 05:50 [ruptura_estricta] CIERRE USELESS take-profit bruto +3.00% neto +2.50%
- 2026-10-01 05:45 [ruptura_volumen_regimen] ENTRADA USELESS @ 0.21618 (22.29 €, apertura)
- 2026-10-01 05:45 [ruptura_volumen_evento] ENTRADA USELESS @ 0.21618 (22.59 €, apertura)
- 2026-10-01 05:45 [ruptura_volumen] ENTRADA INJ @ 6.842 (22.27 €, apertura)
- 2026-10-01 05:45 [ruptura_volumen_regimen] ENTRADA INJ @ 6.842 (22.29 €, apertura)
- 2026-10-01 05:45 [ruptura_volumen_evento] ENTRADA INJ @ 6.842 (22.59 €, apertura)
- 2026-10-01 05:50 [macd_momentum] CIERRE MINA momentum perdido bruto +0.23% neto -0.27%
- 2026-10-01 05:50 [macd_momentum_regimen] CIERRE MINA momentum perdido bruto +0.23% neto -0.27%
- 2026-10-01 05:50 [macd_momentum_evento] CIERRE MINA momentum perdido bruto +0.23% neto -0.27%
- 2026-10-01 05:50 [ruptura_volumen] CIERRE DASH timeout bruto -0.04% neto -0.54%
- 2026-10-01 05:50 [ruptura_volumen_regimen] CIERRE DASH timeout bruto -0.04% neto -0.54%
- 2026-10-01 05:50 [ruptura_volumen_evento] CIERRE DASH timeout bruto -0.04% neto -0.54%
- 2026-10-01 05:45 [pullback_tendencia] ENTRADA PENGU @ 0.008726 (22.55 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
