# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 02:46 UTC · vueltas 104 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.00 € (-2.41%) | 102 | 28 | 27% | -0.234% | -0.990% | -1.114% | -23.14 € |
| reversion_bb | 921.40 € (-0.31%) | 13 | 5 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 891.51 € (-3.54%) | 131 | 16 | 18% | -0.398% | -1.097% | -1.212% | -32.79 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.32 € (-2.26%) | 82 | 2 | 16% | -0.314% | -1.136% | -1.257% | -21.34 € |
| macd_momentum | 897.36 € (-2.91%) | 177 | 17 | 20% | -0.047% | -0.695% | -0.802% | -28.07 € |
| estocastico_rebote | 902.45 € (-2.36%) | 146 | 20 | 37% | +0.021% | -0.658% | -0.781% | -22.09 € |
| ruptura_estricta | 898.32 € (-2.80%) | 62 | 17 | 16% | -0.874% | -1.800% | -1.939% | -25.67 € |
| macd_sin_salida | 902.38 € (-2.37%) | 120 | 28 | 35% | -0.070% | -0.787% | -0.905% | -21.71 € |
| c_banda_atr_tope | 917.52 € (-0.73%) | 24 | 5 | 25% | -0.150% | -1.250% | -1.378% | -6.92 € |
| ruptura_volumen_tope | 915.15 € (-0.98%) | 37 | 5 | 22% | +0.042% | -1.058% | -1.151% | -9.02 € |
| c_banda_atr_regimen | 907.19 € (-1.84%) | 52 | 19 | 25% | -0.420% | -1.422% | -1.575% | -17.01 € |
| macd_momentum_regimen | 905.31 € (-2.05%) | 95 | 13 | 20% | -0.103% | -0.878% | -0.993% | -19.15 € |
| ruptura_volumen_regimen | 892.34 € (-3.45%) | 104 | 16 | 13% | -0.575% | -1.326% | -1.446% | -31.50 € |
| c_banda_atr_evento | 908.00 € (-1.76%) | 69 | 28 | 26% | -0.198% | -1.080% | -1.187% | -17.14 € |
| macd_momentum_evento | 902.33 € (-2.37%) | 130 | 17 | 15% | -0.075% | -0.778% | -0.874% | -23.11 € |
| ruptura_volumen_evento | 904.19 € (-2.17%) | 81 | 16 | 17% | -0.257% | -1.082% | -1.176% | -20.10 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 02:45 | macd_momentum_evento | SOL | momentum perdido | -0.06% | -0.56% | -0.13 |
| 2026-10-01 02:45 | macd_momentum_regimen | SOL | momentum perdido | -0.06% | -0.56% | -0.13 |
| 2026-10-01 02:45 | macd_momentum | SOL | momentum perdido | -0.06% | -0.56% | -0.12 |
| 2026-10-01 02:40 | macd_momentum_evento | NIGHT | momentum perdido | -0.36% | -0.86% | -0.20 |
| 2026-10-01 02:40 | macd_momentum | NIGHT | momentum perdido | -0.36% | -0.86% | -0.19 |
| 2026-10-01 02:40 | pullback_tendencia | ETH | rotura de tendencia | -0.07% | -0.57% | -0.13 |
| 2026-10-01 02:35 | macd_momentum_evento | ETH | momentum perdido | +0.21% | -0.29% | -0.07 |
| 2026-10-01 02:35 | c_banda_atr_evento | TRUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 02:35 | c_banda_atr_evento | KSM | timeout | +0.66% | +0.16% | +0.04 |
| 2026-10-01 02:35 | macd_momentum_regimen | ETH | momentum perdido | +0.21% | -0.29% | -0.07 |
| 2026-10-01 02:35 | c_banda_atr_regimen | TRUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 02:35 | c_banda_atr_regimen | KSM | timeout | +0.66% | +0.16% | +0.04 |
| 2026-10-01 02:35 | c_banda_atr_regimen | PEPE | timeout | -0.24% | -0.74% | -0.17 |
| 2026-10-01 02:35 | c_banda_atr_regimen | LINK | timeout | +0.30% | -0.20% | -0.05 |
| 2026-10-01 02:35 | ruptura_volumen_tope | TRUMP | take-profit | +2.50% | +1.40% | +0.32 |

## Eventos de la última vuelta

- 2026-10-01 02:45 [macd_momentum] CIERRE SOL momentum perdido bruto -0.06% neto -0.56%
- 2026-10-01 02:45 [macd_momentum_regimen] CIERRE SOL momentum perdido bruto -0.06% neto -0.56%
- 2026-10-01 02:45 [macd_momentum_evento] CIERRE SOL momentum perdido bruto -0.06% neto -0.56%
- 2026-10-01 02:40 [estocastico_rebote] ENTRADA QNT @ 256.48 (22.55 €, apertura)
- 2026-10-01 02:40 [estocastico_rebote] ENTRADA XLM @ 0.200364 (22.55 €, apertura)
- 2026-10-01 02:40 [macd_momentum] ENTRADA ENA @ 0.235 (22.40 €, apertura)
- 2026-10-01 02:40 [macd_sin_salida] ENTRADA ENA @ 0.235 (22.56 €, apertura)
- 2026-10-01 02:40 [macd_momentum_regimen] ENTRADA ENA @ 0.235 (22.63 €, apertura)
- 2026-10-01 02:40 [macd_momentum_evento] ENTRADA ENA @ 0.235 (22.53 €, apertura)
- 2026-10-01 02:40 [c_banda_atr_regimen] ENTRADA WLD @ 0.4758 (22.68 €, apertura)
- 2026-10-01 02:40 [estocastico_rebote] ENTRADA KAS @ 0.03902 (22.55 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
