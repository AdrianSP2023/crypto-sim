# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 13:01 UTC · vueltas 223 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 895.89 € (-3.07%) | 187 | 19 | 36% | +0.005% | -0.635% | -0.761% | -27.18 € |
| reversion_bb | 918.62 € (-0.61%) | 27 | 6 | 44% | +0.214% | -0.886% | -0.990% | -5.52 € |
| ruptura_volumen | 883.24 € (-4.44%) | 223 | 10 | 23% | -0.185% | -0.802% | -0.911% | -40.63 € |
| rebote_extremo | 922.08 € (-0.23%) | 9 | 0 | 44% | +0.060% | -1.040% | -1.178% | -2.16 € |
| pullback_tendencia | 894.73 € (-3.19%) | 134 | 1 | 14% | -0.268% | -0.965% | -1.071% | -29.45 € |
| macd_momentum | 881.97 € (-4.57%) | 324 | 5 | 21% | -0.002% | -0.582% | -0.691% | -42.69 € |
| estocastico_rebote | 879.58 € (-4.83%) | 261 | 10 | 31% | -0.158% | -0.758% | -0.869% | -44.83 € |
| ruptura_estricta | 887.72 € (-3.95%) | 126 | 9 | 25% | -0.515% | -1.224% | -1.349% | -35.24 € |
| macd_sin_salida | 887.33 € (-3.99%) | 227 | 20 | 36% | -0.089% | -0.704% | -0.819% | -36.46 € |
| c_banda_atr_tope | 913.14 € (-1.20%) | 43 | 4 | 28% | -0.011% | -1.104% | -1.223% | -10.92 € |
| ruptura_volumen_tope | 911.31 € (-1.40%) | 68 | 3 | 28% | +0.074% | -0.814% | -0.926% | -12.72 € |
| c_banda_atr_regimen | 902.27 € (-2.38%) | 109 | 1 | 34% | -0.130% | -0.870% | -1.010% | -21.77 € |
| macd_momentum_regimen | 894.17 € (-3.25%) | 204 | 2 | 22% | -0.022% | -0.650% | -0.762% | -30.24 € |
| ruptura_volumen_regimen | 884.70 € (-4.28%) | 181 | 4 | 20% | -0.313% | -0.957% | -1.072% | -39.37 € |
| c_banda_atr_evento | 901.85 € (-2.42%) | 154 | 19 | 37% | +0.072% | -0.600% | -0.718% | -21.21 € |
| macd_momentum_evento | 886.86 € (-4.04%) | 277 | 5 | 19% | -0.007% | -0.602% | -0.706% | -37.80 € |
| ruptura_volumen_evento | 895.81 € (-3.08%) | 173 | 10 | 24% | -0.058% | -0.710% | -0.807% | -28.04 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 13:00 | ruptura_volumen_evento | SUI | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 13:00 | macd_momentum_evento | KSM | momentum perdido | -0.86% | -1.36% | -0.30 |
| 2026-10-01 13:00 | ruptura_volumen_regimen | SUI | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 13:00 | macd_sin_salida | HYPE | timeout | -0.03% | -0.53% | -0.12 |
| 2026-10-01 13:00 | macd_momentum | KSM | momentum perdido | -0.86% | -1.36% | -0.30 |
| 2026-10-01 13:00 | pullback_tendencia | BNB | rotura de tendencia | +0.02% | -0.48% | -0.11 |
| 2026-10-01 13:00 | ruptura_volumen | SUI | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 12:55 | ruptura_volumen_evento | BCH | timeout | -0.20% | -0.70% | -0.16 |
| 2026-10-01 12:55 | ruptura_volumen_evento | PUMP | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-01 12:55 | c_banda_atr_evento | PENGU | stop-loss | -1.52% | -2.02% | -0.46 |
| 2026-10-01 12:55 | c_banda_atr_evento | SHIB | timeout | +0.41% | -0.09% | -0.02 |
| 2026-10-01 12:55 | c_banda_atr_evento | ALGO | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 12:55 | pullback_tendencia | UNI | rotura de tendencia | -0.65% | -1.15% | -0.26 |
| 2026-10-01 12:55 | pullback_tendencia | BTC | rotura de tendencia | +0.02% | -0.48% | -0.11 |
| 2026-10-01 12:55 | ruptura_volumen | BCH | timeout | -0.20% | -0.70% | -0.15 |

## Eventos de la última vuelta

- 2026-10-01 13:00 [ruptura_volumen] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 13:00 [ruptura_volumen_regimen] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 13:00 [ruptura_volumen_evento] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 13:00 [macd_sin_salida] CIERRE HYPE timeout bruto -0.03% neto -0.53%
- 2026-10-01 12:55 [estocastico_rebote] ENTRADA FET @ 0.2034 (21.99 €, apertura)
- 2026-10-01 13:00 [macd_momentum] CIERRE KSM momentum perdido bruto -0.86% neto -1.36%
- 2026-10-01 13:00 [macd_momentum_evento] CIERRE KSM momentum perdido bruto -0.86% neto -1.36%
- 2026-10-01 13:00 [pullback_tendencia] CIERRE BNB rotura de tendencia bruto +0.02% neto -0.48%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
