# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 12:56 UTC · vueltas 222 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 895.99 € (-3.06%) | 187 | 19 | 36% | +0.005% | -0.635% | -0.761% | -27.18 € |
| reversion_bb | 918.73 € (-0.60%) | 27 | 6 | 44% | +0.214% | -0.886% | -0.990% | -5.52 € |
| ruptura_volumen | 883.80 € (-4.38%) | 222 | 11 | 23% | -0.181% | -0.798% | -0.908% | -40.25 € |
| rebote_extremo | 922.08 € (-0.23%) | 9 | 0 | 44% | +0.060% | -1.040% | -1.178% | -2.16 € |
| pullback_tendencia | 894.87 € (-3.18%) | 133 | 2 | 14% | -0.270% | -0.968% | -1.075% | -29.35 € |
| macd_momentum | 882.31 € (-4.54%) | 323 | 6 | 21% | +0.001% | -0.580% | -0.688% | -42.39 € |
| estocastico_rebote | 879.86 € (-4.80%) | 261 | 9 | 31% | -0.158% | -0.758% | -0.869% | -44.83 € |
| ruptura_estricta | 888.13 € (-3.91%) | 126 | 9 | 25% | -0.515% | -1.224% | -1.349% | -35.24 € |
| macd_sin_salida | 887.99 € (-3.92%) | 226 | 21 | 36% | -0.089% | -0.704% | -0.819% | -36.34 € |
| c_banda_atr_tope | 913.12 € (-1.20%) | 43 | 4 | 28% | -0.011% | -1.104% | -1.223% | -10.92 € |
| ruptura_volumen_tope | 911.45 € (-1.38%) | 68 | 3 | 28% | +0.074% | -0.814% | -0.926% | -12.72 € |
| c_banda_atr_regimen | 902.35 € (-2.37%) | 109 | 1 | 34% | -0.130% | -0.870% | -1.010% | -21.77 € |
| macd_momentum_regimen | 894.19 € (-3.25%) | 204 | 2 | 22% | -0.022% | -0.650% | -0.762% | -30.24 € |
| ruptura_volumen_regimen | 884.99 € (-4.25%) | 180 | 5 | 20% | -0.308% | -0.953% | -1.068% | -38.99 € |
| c_banda_atr_evento | 901.95 € (-2.41%) | 154 | 19 | 37% | +0.072% | -0.600% | -0.718% | -21.21 € |
| macd_momentum_evento | 887.20 € (-4.01%) | 276 | 6 | 19% | -0.004% | -0.599% | -0.703% | -37.50 € |
| ruptura_volumen_evento | 896.38 € (-3.01%) | 172 | 11 | 24% | -0.051% | -0.705% | -0.802% | -27.66 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 12:55 | ruptura_volumen_evento | BCH | timeout | -0.20% | -0.70% | -0.16 |
| 2026-10-01 12:55 | ruptura_volumen_evento | PUMP | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-01 12:55 | c_banda_atr_evento | PENGU | stop-loss | -1.52% | -2.02% | -0.46 |
| 2026-10-01 12:55 | c_banda_atr_evento | SHIB | timeout | +0.41% | -0.09% | -0.02 |
| 2026-10-01 12:55 | c_banda_atr_evento | ALGO | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 12:55 | pullback_tendencia | UNI | rotura de tendencia | -0.65% | -1.15% | -0.26 |
| 2026-10-01 12:55 | pullback_tendencia | BTC | rotura de tendencia | +0.02% | -0.48% | -0.11 |
| 2026-10-01 12:55 | ruptura_volumen | BCH | timeout | -0.20% | -0.70% | -0.15 |
| 2026-10-01 12:55 | ruptura_volumen | PUMP | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-01 12:55 | c_banda_atr | PENGU | stop-loss | -1.52% | -2.02% | -0.45 |
| 2026-10-01 12:55 | c_banda_atr | SHIB | timeout | +0.41% | -0.09% | -0.02 |
| 2026-10-01 12:55 | c_banda_atr | ALGO | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 12:50 | ruptura_volumen_evento | BTC | timeout | -0.12% | -0.62% | -0.14 |
| 2026-10-01 12:50 | macd_momentum_evento | INJ | momentum perdido | +1.16% | +0.66% | +0.15 |
| 2026-10-01 12:50 | macd_momentum_evento | UNI | momentum perdido | -0.03% | -0.53% | -0.12 |

## Eventos de la última vuelta

- 2026-10-01 12:55 [pullback_tendencia] CIERRE BTC rotura de tendencia bruto +0.02% neto -0.48%
- 2026-10-01 12:55 [ruptura_volumen] CIERRE PUMP timeout bruto +0.60% neto +0.10%
- 2026-10-01 12:55 [ruptura_volumen_evento] CIERRE PUMP timeout bruto +0.60% neto +0.10%
- 2026-10-01 12:55 [pullback_tendencia] CIERRE UNI rotura de tendencia bruto -0.65% neto -1.15%
- 2026-10-01 12:55 [c_banda_atr] CIERRE ALGO timeout bruto +0.23% neto -0.27%
- 2026-10-01 12:55 [c_banda_atr_evento] CIERRE ALGO timeout bruto +0.23% neto -0.27%
- 2026-10-01 12:55 [ruptura_volumen] CIERRE BCH timeout bruto -0.20% neto -0.70%
- 2026-10-01 12:55 [ruptura_volumen_evento] CIERRE BCH timeout bruto -0.20% neto -0.70%
- 2026-10-01 12:55 [c_banda_atr] CIERRE SHIB timeout bruto +0.41% neto -0.09%
- 2026-10-01 12:55 [c_banda_atr_evento] CIERRE SHIB timeout bruto +0.41% neto -0.09%
- 2026-10-01 12:55 [c_banda_atr] CIERRE PENGU stop-loss bruto -1.52% neto -2.02%
- 2026-10-01 12:55 [c_banda_atr_evento] CIERRE PENGU stop-loss bruto -1.52% neto -2.02%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
