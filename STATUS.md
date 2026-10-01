# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 02:51 UTC · vueltas 105 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 901.59 € (-2.45%) | 102 | 28 | 27% | -0.234% | -0.990% | -1.114% | -23.14 € |
| reversion_bb | 921.31 € (-0.32%) | 13 | 5 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 890.98 € (-3.60%) | 135 | 13 | 19% | -0.383% | -1.076% | -1.192% | -33.14 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.22 € (-2.27%) | 82 | 3 | 16% | -0.314% | -1.136% | -1.257% | -21.34 € |
| macd_momentum | 896.34 € (-3.02%) | 179 | 17 | 21% | -0.039% | -0.685% | -0.794% | -27.99 € |
| estocastico_rebote | 902.18 € (-2.39%) | 146 | 21 | 37% | +0.021% | -0.658% | -0.781% | -22.09 € |
| ruptura_estricta | 898.25 € (-2.81%) | 62 | 19 | 16% | -0.874% | -1.800% | -1.939% | -25.67 € |
| macd_sin_salida | 901.79 € (-2.43%) | 120 | 30 | 35% | -0.070% | -0.787% | -0.905% | -21.71 € |
| c_banda_atr_tope | 917.40 € (-0.74%) | 24 | 5 | 25% | -0.150% | -1.250% | -1.378% | -6.92 € |
| ruptura_volumen_tope | 915.11 € (-0.99%) | 38 | 5 | 21% | +0.010% | -1.090% | -1.188% | -9.54 € |
| c_banda_atr_regimen | 906.96 € (-1.87%) | 52 | 19 | 25% | -0.420% | -1.422% | -1.575% | -17.01 € |
| macd_momentum_regimen | 904.65 € (-2.12%) | 97 | 13 | 21% | -0.087% | -0.856% | -0.974% | -19.07 € |
| ruptura_volumen_regimen | 891.74 € (-3.52%) | 108 | 13 | 14% | -0.550% | -1.291% | -1.413% | -31.84 € |
| c_banda_atr_evento | 907.59 € (-1.80%) | 69 | 28 | 26% | -0.198% | -1.080% | -1.187% | -17.14 € |
| macd_momentum_evento | 901.31 € (-2.48%) | 132 | 17 | 15% | -0.064% | -0.764% | -0.862% | -23.03 € |
| ruptura_volumen_evento | 903.66 € (-2.23%) | 85 | 13 | 18% | -0.239% | -1.050% | -1.146% | -20.46 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-01 02:50 | macd_momentum_regimen | KSM | momentum perdido | -0.66% | -1.16% | -0.26 |
| 2026-10-01 02:50 | ruptura_volumen_tope | XDC | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-10-01 02:50 | macd_momentum | TRUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 02:50 | macd_momentum | KSM | momentum perdido | -0.66% | -1.16% | -0.26 |

## Eventos de la última vuelta

- 2026-10-01 02:45 [macd_momentum] ENTRADA ADA @ 0.218681 (22.40 €, apertura)
- 2026-10-01 02:45 [macd_sin_salida] ENTRADA ADA @ 0.218681 (22.56 €, apertura)
- 2026-10-01 02:45 [macd_momentum_regimen] ENTRADA ADA @ 0.218681 (22.63 €, apertura)
- 2026-10-01 02:45 [macd_momentum_evento] ENTRADA ADA @ 0.218681 (22.53 €, apertura)
- 2026-10-01 02:50 [ruptura_volumen] CIERRE SUI timeout bruto -0.07% neto -0.57%
- 2026-10-01 02:50 [ruptura_volumen_regimen] CIERRE SUI timeout bruto -0.07% neto -0.57%
- 2026-10-01 02:50 [ruptura_volumen_evento] CIERRE SUI timeout bruto -0.07% neto -0.57%
- 2026-10-01 02:45 [estocastico_rebote] ENTRADA DOGE @ 0.083757 (22.55 €, apertura)
- 2026-10-01 02:50 [ruptura_volumen] CIERRE FET timeout bruto -0.78% neto -1.28%
- 2026-10-01 02:50 [ruptura_volumen_regimen] CIERRE FET timeout bruto -0.78% neto -1.28%
- 2026-10-01 02:50 [ruptura_volumen_evento] CIERRE FET timeout bruto -0.78% neto -1.28%
- 2026-10-01 02:45 [ruptura_volumen] ENTRADA ALGO @ 0.11145 (22.28 €, apertura)
- 2026-10-01 02:45 [ruptura_estricta] ENTRADA ALGO @ 0.11145 (22.46 €, apertura)
- 2026-10-01 02:45 [ruptura_volumen_regimen] ENTRADA ALGO @ 0.11145 (22.31 €, apertura)
- 2026-10-01 02:45 [ruptura_volumen_evento] ENTRADA ALGO @ 0.11145 (22.59 €, apertura)
- 2026-10-01 02:50 [ruptura_volumen] CIERRE XDC stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 02:50 [ruptura_volumen_tope] CIERRE XDC stop-loss bruto -1.20% neto -2.30%
- 2026-10-01 02:50 [ruptura_volumen_regimen] CIERRE XDC stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 02:50 [ruptura_volumen_evento] CIERRE XDC stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 02:45 [pullback_tendencia] ENTRADA NIGHT @ 0.03549 (22.57 €, apertura)
- 2026-10-01 02:45 [macd_momentum] ENTRADA MON @ 0.02871 (22.40 €, apertura)
- 2026-10-01 02:45 [macd_sin_salida] ENTRADA MON @ 0.02871 (22.56 €, apertura)
- 2026-10-01 02:45 [macd_momentum_regimen] ENTRADA MON @ 0.02871 (22.63 €, apertura)
- 2026-10-01 02:45 [macd_momentum_evento] ENTRADA MON @ 0.02871 (22.53 €, apertura)
- 2026-10-01 02:50 [macd_momentum] CIERRE KSM momentum perdido bruto -0.66% neto -1.16%
- 2026-10-01 02:50 [macd_momentum_regimen] CIERRE KSM momentum perdido bruto -0.66% neto -1.16%
- 2026-10-01 02:50 [macd_momentum_evento] CIERRE KSM momentum perdido bruto -0.66% neto -1.16%
- 2026-10-01 02:50 [ruptura_volumen] CIERRE TRUMP take-profit bruto +2.50% neto +2.00%
- 2026-10-01 02:50 [macd_momentum] CIERRE TRUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-01 02:45 [ruptura_estricta] ENTRADA TRUMP @ 1.906 (22.46 €, apertura)
- 2026-10-01 02:45 [ruptura_volumen_tope] ENTRADA TRUMP @ 1.906 (22.87 €, apertura)
- 2026-10-01 02:50 [macd_momentum_regimen] CIERRE TRUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-01 02:50 [ruptura_volumen_regimen] CIERRE TRUMP take-profit bruto +2.50% neto +2.00%
- 2026-10-01 02:50 [macd_momentum_evento] CIERRE TRUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-01 02:50 [ruptura_volumen_evento] CIERRE TRUMP take-profit bruto +2.50% neto +2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
