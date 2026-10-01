# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 02:56 UTC · vueltas 106 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.34 € (-2.37%) | 102 | 28 | 27% | -0.234% | -0.990% | -1.114% | -23.14 € |
| reversion_bb | 921.40 € (-0.31%) | 13 | 5 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 891.29 € (-3.56%) | 135 | 13 | 19% | -0.383% | -1.076% | -1.192% | -33.14 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.20 € (-2.28%) | 82 | 4 | 16% | -0.314% | -1.136% | -1.257% | -21.34 € |
| macd_momentum | 896.64 € (-2.99%) | 180 | 18 | 21% | -0.048% | -0.693% | -0.801% | -28.44 € |
| estocastico_rebote | 902.63 € (-2.34%) | 146 | 21 | 37% | +0.021% | -0.658% | -0.781% | -22.09 € |
| ruptura_estricta | 898.38 € (-2.80%) | 62 | 19 | 16% | -0.874% | -1.800% | -1.939% | -25.67 € |
| macd_sin_salida | 902.17 € (-2.39%) | 121 | 31 | 35% | -0.068% | -0.784% | -0.900% | -21.78 € |
| c_banda_atr_tope | 917.45 € (-0.73%) | 24 | 5 | 25% | -0.150% | -1.250% | -1.378% | -6.92 € |
| ruptura_volumen_tope | 915.12 € (-0.99%) | 39 | 4 | 23% | +0.073% | -1.027% | -1.126% | -9.22 € |
| c_banda_atr_regimen | 907.33 € (-1.83%) | 52 | 19 | 25% | -0.420% | -1.422% | -1.575% | -17.01 € |
| macd_momentum_regimen | 905.12 € (-2.07%) | 97 | 15 | 21% | -0.087% | -0.856% | -0.974% | -19.07 € |
| ruptura_volumen_regimen | 892.04 € (-3.48%) | 108 | 13 | 14% | -0.550% | -1.291% | -1.413% | -31.84 € |
| c_banda_atr_evento | 908.35 € (-1.72%) | 69 | 28 | 26% | -0.198% | -1.080% | -1.187% | -17.14 € |
| macd_momentum_evento | 901.61 € (-2.45%) | 133 | 18 | 15% | -0.074% | -0.773% | -0.871% | -23.48 € |
| ruptura_volumen_evento | 903.98 € (-2.19%) | 85 | 13 | 18% | -0.239% | -1.050% | -1.146% | -20.46 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 02:55 | macd_momentum_evento | XDC | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 02:55 | ruptura_volumen_tope | TRUMP | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-10-01 02:55 | macd_sin_salida | TRX | timeout | +0.17% | -0.33% | -0.07 |
| 2026-10-01 02:55 | macd_momentum | XDC | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 02:50 | ruptura_volumen_evento | TRUMP | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 02:50 | ruptura_volumen_evento | XDC | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 02:50 | ruptura_volumen_evento | FET | timeout | -0.78% | -1.28% | -0.29 |
| 2026-10-01 02:50 | ruptura_volumen_evento | SUI | timeout | -0.07% | -0.57% | -0.13 |
| 2026-10-01 02:50 | macd_momentum_evento | TRUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 02:50 | macd_momentum_evento | KSM | momentum perdido | -0.66% | -1.16% | -0.26 |
| 2026-10-01 02:50 | ruptura_volumen_regimen | TRUMP | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 02:50 | ruptura_volumen_regimen | XDC | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 02:50 | ruptura_volumen_regimen | FET | timeout | -0.78% | -1.28% | -0.29 |
| 2026-10-01 02:50 | ruptura_volumen_regimen | SUI | timeout | -0.07% | -0.57% | -0.13 |
| 2026-10-01 02:50 | macd_momentum_regimen | TRUMP | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-10-01 02:50 [pullback_tendencia] ENTRADA SUI @ 1.0409 (22.57 €, apertura)
- 2026-10-01 02:50 [macd_momentum] ENTRADA DOT @ 1.0847 (22.41 €, apertura)
- 2026-10-01 02:50 [macd_sin_salida] ENTRADA DOT @ 1.0847 (22.56 €, apertura)
- 2026-10-01 02:50 [macd_momentum_regimen] ENTRADA DOT @ 1.0847 (22.63 €, apertura)
- 2026-10-01 02:50 [macd_momentum_evento] ENTRADA DOT @ 1.0847 (22.53 €, apertura)
- 2026-10-01 02:55 [macd_sin_salida] CIERRE TRX timeout bruto +0.17% neto -0.33%
- 2026-10-01 02:50 [macd_momentum] ENTRADA POL @ 0.09989 (22.41 €, apertura)
- 2026-10-01 02:50 [macd_sin_salida] ENTRADA POL @ 0.09989 (22.56 €, apertura)
- 2026-10-01 02:50 [macd_momentum_regimen] ENTRADA POL @ 0.09989 (22.63 €, apertura)
- 2026-10-01 02:50 [macd_momentum_evento] ENTRADA POL @ 0.09989 (22.53 €, apertura)
- 2026-10-01 02:55 [macd_momentum] CIERRE XDC stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 02:55 [macd_momentum_evento] CIERRE XDC stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 02:55 [ruptura_volumen_tope] CIERRE TRUMP take-profit bruto +2.50% neto +1.40%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
