# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 15:27 UTC · vueltas 69 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 911.37 € (-1.39%) | 44 | 6 | 36% | -0.067% | -1.119% | -1.259% | -11.36 € |
| reversion_bb | 921.30 € (-0.32%) | 4 | 3 | 0% | -1.500% | -2.600% | -2.715% | -2.40 € |
| ruptura_volumen | 910.29 € (-1.51%) | 67 | 2 | 28% | +0.013% | -0.876% | -1.013% | -13.51 € |
| rebote_extremo | 923.86 € (-0.04%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 909.46 € (-1.60%) | 65 | 1 | 26% | -0.086% | -0.988% | -1.102% | -14.75 € |
| macd_momentum | 899.14 € (-2.72%) | 146 | 1 | 20% | -0.069% | -0.747% | -0.862% | -24.97 € |
| estocastico_rebote | 904.96 € (-2.09%) | 88 | 7 | 36% | -0.083% | -0.879% | -1.009% | -17.84 € |
| ruptura_estricta | 914.39 € (-1.07%) | 35 | 6 | 34% | +0.070% | -1.030% | -1.161% | -8.32 € |
| macd_sin_salida | 906.67 € (-1.90%) | 89 | 4 | 33% | -0.019% | -0.812% | -0.936% | -16.59 € |
| c_banda_atr_tope | 917.31 € (-0.75%) | 15 | 2 | 20% | -0.730% | -1.830% | -2.012% | -6.33 € |
| ruptura_volumen_tope | 919.98 € (-0.46%) | 19 | 1 | 21% | +0.172% | -0.928% | -1.062% | -4.07 € |
| c_banda_atr_regimen | 911.37 € (-1.39%) | 44 | 6 | 36% | -0.067% | -1.119% | -1.259% | -11.36 € |
| macd_momentum_regimen | 899.14 € (-2.72%) | 146 | 1 | 20% | -0.069% | -0.747% | -0.862% | -24.97 € |
| ruptura_volumen_regimen | 910.29 € (-1.51%) | 67 | 2 | 28% | +0.013% | -0.876% | -1.013% | -13.51 € |
| c_banda_atr_evento | 918.02 € (-0.67%) | 14 | 4 | 29% | -0.530% | -1.630% | -1.800% | -5.27 € |
| macd_momentum_evento | 914.25 € (-1.08%) | 26 | 1 | 15% | -0.540% | -1.640% | -1.748% | -9.86 € |
| ruptura_volumen_evento | 920.55 € (-0.40%) | 9 | 1 | 22% | -0.552% | -1.652% | -1.851% | -3.43 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 15:25 | ruptura_volumen_evento | TRUMP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 15:25 | macd_momentum_evento | ATOM | momentum perdido | -1.41% | -2.51% | -0.58 |
| 2026-09-29 15:25 | c_banda_atr_evento | BCH | stop-loss | -1.53% | -2.63% | -0.61 |
| 2026-09-29 15:25 | ruptura_volumen_regimen | ICP | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 15:25 | macd_momentum_regimen | ATOM | momentum perdido | -1.41% | -1.91% | -0.43 |
| 2026-09-29 15:25 | c_banda_atr_regimen | SPX | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-29 15:25 | c_banda_atr_regimen | DOT | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-29 15:25 | ruptura_volumen_tope | ICP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 15:25 | c_banda_atr_tope | RAY | stop-loss | -2.06% | -3.16% | -0.73 |
| 2026-09-29 15:25 | macd_sin_salida | OP | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 15:25 | macd_sin_salida | RENDER | stop-loss | -1.56% | -2.06% | -0.47 |
| 2026-09-29 15:25 | macd_sin_salida | INJ | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 15:25 | macd_sin_salida | DASH | stop-loss | -1.65% | -2.15% | -0.49 |
| 2026-09-29 15:25 | macd_sin_salida | DOT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 15:25 | macd_sin_salida | TAO | stop-loss | -1.50% | -2.00% | -0.46 |

## Eventos de la última vuelta

- 2026-09-29 15:25 [macd_sin_salida] CIERRE BTC stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [estocastico_rebote] CIERRE LINK stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [estocastico_rebote] CIERRE ETH stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [pullback_tendencia] CIERRE NEAR rotura de tendencia bruto -1.44% neto -1.94%
- 2026-09-29 15:25 [estocastico_rebote] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [estocastico_rebote] CIERRE LTC stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 15:25 [reversion_bb] CIERRE AVAX stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:25 [macd_sin_salida] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [macd_sin_salida] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:20 [reversion_bb] ENTRADA DOGE @ 0.0833397 (23.06 €, apertura)
- 2026-09-29 15:25 [estocastico_rebote] CIERRE DOGE stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [c_banda_atr] CIERRE DOT stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 15:25 [estocastico_rebote] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [macd_sin_salida] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [c_banda_atr_regimen] CIERRE DOT stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 15:25 [macd_sin_salida] CIERRE DASH stop-loss bruto -1.65% neto -2.15%
- 2026-09-29 15:25 [ruptura_volumen] CIERRE ICP stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 15:25 [pullback_tendencia] CIERRE ICP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [ruptura_volumen_tope] CIERRE ICP stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 15:25 [ruptura_volumen_regimen] CIERRE ICP stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 15:25 [estocastico_rebote] CIERRE BCH stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [c_banda_atr_evento] CIERRE BCH stop-loss bruto -1.53% neto -2.63%
- 2026-09-29 15:25 [pullback_tendencia] CIERRE INJ rotura de tendencia bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [macd_sin_salida] CIERRE INJ stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [macd_momentum] CIERRE ATOM momentum perdido bruto -1.41% neto -1.91%
- 2026-09-29 15:25 [macd_momentum_regimen] CIERRE ATOM momentum perdido bruto -1.41% neto -1.91%
- 2026-09-29 15:25 [macd_momentum_evento] CIERRE ATOM momentum perdido bruto -1.41% neto -2.51%
- 2026-09-29 15:25 [estocastico_rebote] CIERRE RENDER stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 15:25 [macd_sin_salida] CIERRE RENDER stop-loss bruto -1.56% neto -2.06%
- 2026-09-29 15:25 [ruptura_estricta] CIERRE WLD stop-loss bruto -2.00% neto -3.10%
- 2026-09-29 15:20 [estocastico_rebote] ENTRADA USELESS @ 0.21 (22.71 €, apertura)
- 2026-09-29 15:25 [estocastico_rebote] CIERRE USELESS stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [c_banda_atr_tope] CIERRE RAY stop-loss bruto -2.06% neto -3.16%
- 2026-09-29 15:25 [macd_sin_salida] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:20 [pullback_tendencia] ENTRADA NIGHT @ 0.02835 (22.76 €, apertura)
- 2026-09-29 15:25 [estocastico_rebote] CIERRE SHIB stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [estocastico_rebote] CIERRE PENGU stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:25 [pullback_tendencia] CIERRE TRUMP rotura de tendencia bruto -1.15% neto -1.65%
- 2026-09-29 15:25 [ruptura_volumen_evento] CIERRE TRUMP stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 15:20 [pullback_tendencia] ENTRADA XPL @ 0.0891 (22.75 €, apertura)
- 2026-09-29 15:25 [pullback_tendencia] CIERRE XPL rotura de tendencia bruto -1.46% neto -1.96%
- 2026-09-29 15:25 [c_banda_atr] CIERRE SPX stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 15:25 [c_banda_atr_regimen] CIERRE SPX stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 15:25 [reversion_bb] CIERRE FET stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:20 [rebote_extremo] ENTRADA FET @ 0.1995 (23.11 €, apertura)
- 2026-09-29 15:25 [estocastico_rebote] CIERRE FET stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
