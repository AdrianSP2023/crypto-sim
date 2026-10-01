# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 06:01 UTC · vueltas 142 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.56 € (-1.70%) | 131 | 24 | 38% | +0.124% | -0.575% | -0.695% | -17.36 € |
| reversion_bb | 921.61 € (-0.29%) | 17 | 2 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 892.28 € (-3.46%) | 176 | 22 | 23% | -0.181% | -0.829% | -0.937% | -33.29 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 902.77 € (-2.32%) | 95 | 11 | 17% | -0.242% | -1.020% | -1.134% | -22.18 € |
| macd_momentum | 894.17 € (-3.25%) | 253 | 8 | 24% | +0.063% | -0.540% | -0.646% | -31.15 € |
| estocastico_rebote | 902.88 € (-2.31%) | 173 | 14 | 39% | +0.102% | -0.549% | -0.669% | -21.86 € |
| ruptura_estricta | 903.63 € (-2.23%) | 85 | 32 | 27% | -0.403% | -1.214% | -1.347% | -23.77 € |
| macd_sin_salida | 906.39 € (-1.93%) | 164 | 26 | 43% | +0.153% | -0.506% | -0.619% | -19.10 € |
| c_banda_atr_tope | 917.43 € (-0.74%) | 30 | 5 | 30% | +0.135% | -0.965% | -1.091% | -6.68 € |
| ruptura_volumen_tope | 915.27 € (-0.97%) | 47 | 5 | 26% | +0.141% | -0.921% | -1.019% | -9.96 € |
| c_banda_atr_regimen | 912.47 € (-1.27%) | 77 | 20 | 40% | +0.126% | -0.713% | -0.852% | -12.70 € |
| macd_momentum_regimen | 903.24 € (-2.27%) | 167 | 8 | 25% | +0.079% | -0.577% | -0.687% | -22.08 € |
| ruptura_volumen_regimen | 893.02 € (-3.38%) | 150 | 21 | 20% | -0.275% | -0.949% | -1.060% | -32.48 € |
| c_banda_atr_evento | 914.61 € (-1.04%) | 98 | 24 | 41% | +0.270% | -0.499% | -0.606% | -11.32 € |
| macd_momentum_evento | 899.12 € (-2.72%) | 206 | 8 | 21% | +0.070% | -0.558% | -0.656% | -26.20 € |
| ruptura_volumen_evento | 904.98 € (-2.08%) | 126 | 22 | 25% | -0.004% | -0.713% | -0.805% | -20.60 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 06:00 | ruptura_volumen_evento | KAS | timeout | -0.41% | -0.91% | -0.20 |
| 2026-10-01 06:00 | ruptura_volumen_evento | VVV | take-profit | +2.59% | +2.09% | +0.47 |
| 2026-10-01 06:00 | ruptura_volumen_evento | FIL | timeout | -0.43% | -0.93% | -0.21 |
| 2026-10-01 06:00 | macd_momentum_evento | RENDER | momentum perdido | -0.23% | -0.73% | -0.17 |
| 2026-10-01 06:00 | macd_momentum_evento | ZRO | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-10-01 06:00 | macd_momentum_evento | XRP | timeout | +1.15% | +0.65% | +0.15 |
| 2026-10-01 06:00 | ruptura_volumen_regimen | KAS | timeout | -0.41% | -0.91% | -0.20 |
| 2026-10-01 06:00 | ruptura_volumen_regimen | VVV | take-profit | +2.59% | +2.09% | +0.47 |
| 2026-10-01 06:00 | ruptura_volumen_regimen | FIL | timeout | -0.43% | -0.93% | -0.21 |
| 2026-10-01 06:00 | ruptura_volumen_regimen | ETH | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-01 06:00 | macd_momentum_regimen | RENDER | momentum perdido | -0.23% | -0.73% | -0.17 |
| 2026-10-01 06:00 | macd_momentum_regimen | ZRO | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-10-01 06:00 | macd_momentum_regimen | XRP | timeout | +1.15% | +0.65% | +0.15 |
| 2026-10-01 06:00 | macd_sin_salida | WLFI | timeout | -0.81% | -1.31% | -0.30 |
| 2026-10-01 06:00 | macd_sin_salida | SUI | timeout | -0.73% | -1.23% | -0.28 |

## Eventos de la última vuelta

- 2026-10-01 05:55 [ruptura_volumen] ENTRADA BTC @ 74465 (22.27 €, apertura)
- 2026-10-01 05:55 [ruptura_volumen_regimen] ENTRADA BTC @ 74465 (22.29 €, apertura)
- 2026-10-01 05:55 [ruptura_volumen_evento] ENTRADA BTC @ 74465 (22.59 €, apertura)
- 2026-10-01 06:00 [macd_momentum] CIERRE XRP timeout bruto +1.15% neto +0.65%
- 2026-10-01 06:00 [macd_sin_salida] CIERRE XRP timeout bruto +1.15% neto +0.65%
- 2026-10-01 06:00 [macd_momentum_regimen] CIERRE XRP timeout bruto +1.15% neto +0.65%
- 2026-10-01 06:00 [macd_momentum_evento] CIERRE XRP timeout bruto +1.15% neto +0.65%
- 2026-10-01 06:00 [ruptura_volumen_regimen] CIERRE ETH timeout bruto +0.91% neto +0.41%
- 2026-10-01 06:00 [macd_sin_salida] CIERRE SUI timeout bruto -0.73% neto -1.23%
- 2026-10-01 06:00 [macd_momentum] CIERRE ZRO momentum perdido bruto -0.20% neto -0.70%
- 2026-10-01 06:00 [macd_momentum_regimen] CIERRE ZRO momentum perdido bruto -0.20% neto -0.70%
- 2026-10-01 06:00 [macd_momentum_evento] CIERRE ZRO momentum perdido bruto -0.20% neto -0.70%
- 2026-10-01 05:55 [estocastico_rebote] ENTRADA ICP @ 2.96 (22.56 €, apertura)
- 2026-10-01 06:00 [macd_momentum] CIERRE RENDER momentum perdido bruto -0.23% neto -0.73%
- 2026-10-01 06:00 [macd_momentum_regimen] CIERRE RENDER momentum perdido bruto -0.23% neto -0.73%
- 2026-10-01 06:00 [macd_momentum_evento] CIERRE RENDER momentum perdido bruto -0.23% neto -0.73%
- 2026-10-01 06:00 [ruptura_volumen] CIERRE FIL timeout bruto -0.43% neto -0.93%
- 2026-10-01 06:00 [ruptura_volumen_regimen] CIERRE FIL timeout bruto -0.43% neto -0.93%
- 2026-10-01 06:00 [ruptura_volumen_evento] CIERRE FIL timeout bruto -0.43% neto -0.93%
- 2026-10-01 06:00 [ruptura_volumen] CIERRE VVV take-profit bruto +2.59% neto +2.09%
- 2026-10-01 06:00 [ruptura_volumen_regimen] CIERRE VVV take-profit bruto +2.59% neto +2.09%
- 2026-10-01 06:00 [ruptura_volumen_evento] CIERRE VVV take-profit bruto +2.59% neto +2.09%
- 2026-10-01 06:00 [ruptura_estricta] CIERRE WLFI timeout bruto -0.81% neto -1.31%
- 2026-10-01 06:00 [macd_sin_salida] CIERRE WLFI timeout bruto -0.81% neto -1.31%
- 2026-10-01 06:00 [ruptura_volumen] CIERRE KAS timeout bruto -0.41% neto -0.91%
- 2026-10-01 06:00 [ruptura_volumen_regimen] CIERRE KAS timeout bruto -0.41% neto -0.91%
- 2026-10-01 06:00 [ruptura_volumen_evento] CIERRE KAS timeout bruto -0.41% neto -0.91%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
