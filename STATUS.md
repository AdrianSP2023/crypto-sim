# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 23:46 UTC · vueltas 169 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.67 € (-2.66%) | 77 | 25 | 29% | -0.324% | -1.163% | -1.310% | -20.56 € |
| reversion_bb | 917.44 € (-0.74%) | 18 | 6 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 901.03 € (-2.51%) | 113 | 8 | 23% | -0.134% | -0.865% | -0.992% | -22.36 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.31 € (-2.16%) | 91 | 0 | 22% | -0.169% | -0.956% | -1.077% | -19.93 € |
| macd_momentum | 883.61 € (-4.40%) | 223 | 7 | 15% | -0.174% | -0.791% | -0.902% | -40.04 € |
| estocastico_rebote | 892.07 € (-3.48%) | 162 | 9 | 33% | -0.168% | -0.830% | -0.950% | -30.73 € |
| ruptura_estricta | 908.64 € (-1.69%) | 48 | 9 | 27% | -0.269% | -1.312% | -1.445% | -14.49 € |
| macd_sin_salida | 895.86 € (-3.07%) | 131 | 14 | 27% | -0.183% | -0.883% | -1.008% | -26.42 € |
| c_banda_atr_tope | 912.95 € (-1.22%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 914.23 € (-1.08%) | 37 | 4 | 16% | -0.031% | -1.131% | -1.251% | -9.63 € |
| c_banda_atr_regimen | 902.45 € (-2.36%) | 58 | 18 | 28% | -0.411% | -1.361% | -1.501% | -18.16 € |
| macd_momentum_regimen | 887.68 € (-3.96%) | 190 | 3 | 15% | -0.197% | -0.835% | -0.947% | -36.06 € |
| ruptura_volumen_regimen | 904.08 € (-2.18%) | 94 | 6 | 22% | -0.122% | -0.900% | -1.028% | -19.39 € |
| c_banda_atr_evento | 903.70 € (-2.22%) | 45 | 25 | 22% | -0.604% | -1.597% | -1.756% | -16.51 € |
| macd_momentum_evento | 896.03 € (-3.05%) | 103 | 7 | 8% | -0.417% | -1.173% | -1.278% | -27.61 € |
| ruptura_volumen_evento | 906.58 € (-1.91%) | 54 | 8 | 13% | -0.366% | -1.354% | -1.484% | -16.81 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 23:45 | ruptura_volumen_evento | VVV | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 23:45 | ruptura_volumen_evento | DOT | stop-loss | -1.22% | -1.72% | -0.39 |
| 2026-09-29 23:45 | macd_momentum_evento | TRUMP | momentum perdido | -1.05% | -1.55% | -0.35 |
| 2026-09-29 23:45 | macd_momentum_evento | BNB | momentum perdido | -0.22% | -0.72% | -0.16 |
| 2026-09-29 23:45 | macd_momentum_evento | NIGHT | momentum perdido | -1.28% | -1.78% | -0.40 |
| 2026-09-29 23:45 | macd_momentum_evento | SEI | momentum perdido | -1.48% | -1.98% | -0.45 |
| 2026-09-29 23:45 | macd_momentum_evento | RENDER | momentum perdido | -1.06% | -1.56% | -0.35 |
| 2026-09-29 23:45 | macd_momentum_evento | ICP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 23:45 | macd_momentum_evento | DOT | momentum perdido | -1.29% | -1.79% | -0.40 |
| 2026-09-29 23:45 | macd_momentum_evento | SUI | momentum perdido | -0.94% | -1.44% | -0.33 |
| 2026-09-29 23:45 | macd_momentum_evento | SOL | momentum perdido | -0.12% | -0.62% | -0.14 |
| 2026-09-29 23:45 | c_banda_atr_evento | OP | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 23:45 | c_banda_atr_evento | USELESS | stop-loss | -1.97% | -2.47% | -0.56 |
| 2026-09-29 23:45 | c_banda_atr_evento | VIRTUAL | stop-loss | -1.67% | -2.47% | -0.56 |
| 2026-09-29 23:45 | c_banda_atr_evento | MON | stop-loss | -1.50% | -2.00% | -0.46 |

## Eventos de la última vuelta

- 2026-09-29 23:40 [pullback_tendencia] ENTRADA SOL @ 105.13 (22.63 €, apertura)
- 2026-09-29 23:45 [pullback_tendencia] CIERRE SOL rotura de tendencia bruto -0.16% neto -0.66%
- 2026-09-29 23:45 [macd_momentum] CIERRE SOL momentum perdido bruto -0.12% neto -0.62%
- 2026-09-29 23:45 [macd_momentum_evento] CIERRE SOL momentum perdido bruto -0.12% neto -0.62%
- 2026-09-29 23:45 [macd_momentum] CIERRE SUI momentum perdido bruto -0.94% neto -1.44%
- 2026-09-29 23:45 [macd_momentum_regimen] CIERRE SUI momentum perdido bruto -0.94% neto -1.44%
- 2026-09-29 23:45 [macd_momentum_evento] CIERRE SUI momentum perdido bruto -0.94% neto -1.44%
- 2026-09-29 23:45 [pullback_tendencia] CIERRE AVAX rotura de tendencia bruto +0.01% neto -0.49%
- 2026-09-29 23:45 [pullback_tendencia] CIERRE PUMP rotura de tendencia bruto -0.69% neto -1.19%
- 2026-09-29 23:45 [ruptura_volumen] CIERRE DOT stop-loss bruto -1.22% neto -1.72%
- 2026-09-29 23:45 [macd_momentum] CIERRE DOT momentum perdido bruto -1.29% neto -1.79%
- 2026-09-29 23:45 [macd_momentum_regimen] CIERRE DOT momentum perdido bruto -1.29% neto -1.79%
- 2026-09-29 23:45 [ruptura_volumen_regimen] CIERRE DOT stop-loss bruto -1.22% neto -1.72%
- 2026-09-29 23:45 [macd_momentum_evento] CIERRE DOT momentum perdido bruto -1.29% neto -1.79%
- 2026-09-29 23:45 [ruptura_volumen_evento] CIERRE DOT stop-loss bruto -1.22% neto -1.72%
- 2026-09-29 23:45 [c_banda_atr] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:45 [c_banda_atr_regimen] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:45 [c_banda_atr_evento] CIERRE ENA stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 23:45 [c_banda_atr] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:45 [c_banda_atr_evento] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:45 [macd_momentum] CIERRE ICP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:45 [macd_sin_salida] CIERRE ICP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:45 [macd_momentum_regimen] CIERRE ICP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:45 [macd_momentum_evento] CIERRE ICP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:45 [macd_sin_salida] CIERRE INJ stop-loss bruto -1.51% neto -2.01%
- 2026-09-29 23:45 [ruptura_volumen] CIERRE VVV stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 23:45 [macd_sin_salida] CIERRE VVV stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:45 [ruptura_volumen_tope] CIERRE VVV stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 23:45 [ruptura_volumen_evento] CIERRE VVV stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 23:45 [macd_momentum] CIERRE RENDER momentum perdido bruto -1.06% neto -1.56%
- 2026-09-29 23:45 [macd_momentum_regimen] CIERRE RENDER momentum perdido bruto -1.06% neto -1.56%
- 2026-09-29 23:45 [macd_momentum_evento] CIERRE RENDER momentum perdido bruto -1.06% neto -1.56%
- 2026-09-29 23:45 [c_banda_atr] CIERRE VIRTUAL stop-loss bruto -1.67% neto -2.17%
- 2026-09-29 23:45 [c_banda_atr_evento] CIERRE VIRTUAL stop-loss bruto -1.67% neto -2.47%
- 2026-09-29 23:45 [c_banda_atr] CIERRE USELESS stop-loss bruto -1.97% neto -2.47%
- 2026-09-29 23:45 [pullback_tendencia] CIERRE USELESS rotura de tendencia bruto -1.13% neto -1.63%
- 2026-09-29 23:45 [c_banda_atr_regimen] CIERRE USELESS stop-loss bruto -1.97% neto -2.47%
- 2026-09-29 23:45 [c_banda_atr_evento] CIERRE USELESS stop-loss bruto -1.97% neto -2.47%
- 2026-09-29 23:45 [macd_momentum] CIERRE SEI momentum perdido bruto -1.48% neto -1.98%
- 2026-09-29 23:45 [macd_momentum_regimen] CIERRE SEI momentum perdido bruto -1.48% neto -1.98%
- 2026-09-29 23:45 [macd_momentum_evento] CIERRE SEI momentum perdido bruto -1.48% neto -1.98%
- 2026-09-29 23:45 [c_banda_atr] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:45 [c_banda_atr_regimen] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:45 [c_banda_atr_evento] CIERRE OP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:45 [macd_momentum] CIERRE NIGHT momentum perdido bruto -1.28% neto -1.78%
- 2026-09-29 23:45 [macd_momentum_regimen] CIERRE NIGHT momentum perdido bruto -1.28% neto -1.78%
- 2026-09-29 23:45 [macd_momentum_evento] CIERRE NIGHT momentum perdido bruto -1.28% neto -1.78%
- 2026-09-29 23:40 [reversion_bb] ENTRADA FIL @ 0.932 (22.95 €, apertura)
- 2026-09-29 23:45 [macd_momentum] CIERRE BNB momentum perdido bruto -0.22% neto -0.72%
- 2026-09-29 23:45 [macd_momentum_evento] CIERRE BNB momentum perdido bruto -0.22% neto -0.72%
- 2026-09-29 23:45 [macd_momentum] CIERRE TRUMP momentum perdido bruto -1.05% neto -1.55%
- 2026-09-29 23:45 [macd_momentum_regimen] CIERRE TRUMP momentum perdido bruto -1.05% neto -1.55%
- 2026-09-29 23:45 [macd_momentum_evento] CIERRE TRUMP momentum perdido bruto -1.05% neto -1.55%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
