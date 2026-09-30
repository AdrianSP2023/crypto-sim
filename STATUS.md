# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 01:48 UTC · vueltas 168 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

**Avisos:** hueco de 132 min entre vueltas

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.30 € (-2.27%) | 94 | 23 | 29% | -0.289% | -1.067% | -1.214% | -23.02 € |
| reversion_bb | 919.60 € (-0.50%) | 26 | 8 | 50% | +0.198% | -0.902% | -1.006% | -5.42 € |
| ruptura_volumen | 899.67 € (-2.66%) | 124 | 18 | 23% | -0.141% | -0.852% | -0.977% | -24.16 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.17 € (-1.95%) | 97 | 2 | 26% | -0.049% | -0.818% | -0.947% | -18.20 € |
| macd_momentum | 885.92 € (-4.15%) | 240 | 17 | 17% | -0.124% | -0.733% | -0.846% | -39.90 € |
| estocastico_rebote | 894.59 € (-3.21%) | 177 | 7 | 34% | -0.107% | -0.755% | -0.890% | -30.56 € |
| ruptura_estricta | 908.58 € (-1.69%) | 55 | 9 | 27% | -0.215% | -1.189% | -1.321% | -15.04 € |
| macd_sin_salida | 899.19 € (-2.71%) | 149 | 15 | 30% | -0.105% | -0.780% | -0.906% | -26.57 € |
| c_banda_atr_tope | 912.47 € (-1.27%) | 30 | 4 | 20% | -0.556% | -1.656% | -1.801% | -11.43 € |
| ruptura_volumen_tope | 912.77 € (-1.24%) | 44 | 4 | 18% | -0.038% | -1.117% | -1.236% | -11.31 € |
| c_banda_atr_regimen | 902.81 € (-2.32%) | 68 | 8 | 24% | -0.518% | -1.401% | -1.536% | -21.87 € |
| macd_momentum_regimen | 887.21 € (-4.01%) | 193 | 1 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.02 € (-2.30%) | 100 | 8 | 21% | -0.152% | -0.913% | -1.039% | -20.91 € |
| c_banda_atr_evento | 906.79 € (-1.89%) | 62 | 23 | 24% | -0.475% | -1.372% | -1.527% | -19.54 € |
| macd_momentum_evento | 898.37 € (-2.80%) | 120 | 17 | 12% | -0.281% | -1.001% | -1.112% | -27.46 € |
| ruptura_volumen_evento | 905.21 € (-2.06%) | 65 | 18 | 14% | -0.341% | -1.247% | -1.372% | -18.61 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 01:45 | c_banda_atr_evento | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:45 | c_banda_atr_tope | BCH | timeout | -0.41% | -1.51% | -0.35 |
| 2026-09-30 01:45 | c_banda_atr | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:40 | ruptura_volumen_tope | USELESS | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 01:35 | macd_sin_salida | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:35 | pullback_tendencia | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:30 | pullback_tendencia | NEAR | take-profit | +2.27% | +1.77% | +0.40 |
| 2026-09-30 01:30 | reversion_bb | FIL | take-profit | +1.93% | +0.83% | +0.19 |
| 2026-09-30 01:25 | macd_momentum_evento | PENGU | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:25 | macd_momentum_evento | RAY | take-profit | +2.13% | +1.63% | +0.36 |
| 2026-09-30 01:25 | macd_momentum_evento | DOT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:25 | macd_momentum_evento | ZEC | momentum perdido | -0.39% | -0.89% | -0.20 |
| 2026-09-30 01:25 | macd_momentum_evento | QNT | momentum perdido | -0.70% | -1.20% | -0.27 |
| 2026-09-30 01:25 | c_banda_atr_evento | RAY | take-profit | +2.37% | +1.87% | +0.42 |
| 2026-09-30 01:25 | macd_sin_salida | RAY | take-profit | +2.13% | +1.63% | +0.36 |

## Eventos de la última vuelta

- 2026-09-29 23:40 [macd_momentum] CIERRE ADA momentum perdido bruto -0.01% neto -0.51%
- 2026-09-29 23:40 [macd_momentum_regimen] CIERRE ADA momentum perdido bruto -0.64% neto -1.14%
- 2026-09-29 23:40 [macd_momentum_evento] CIERRE ADA momentum perdido bruto -0.01% neto -0.51%
- 2026-09-29 23:35 [pullback_tendencia] ENTRADA PUMP @ 0.005202 (22.63 €, apertura)
- 2026-09-29 23:35 [reversion_bb] ENTRADA ARB @ 0.1784 (22.95 €, apertura)
- 2026-09-29 23:40 [macd_momentum] CIERRE DOGE momentum perdido bruto -0.45% neto -0.95%
- 2026-09-29 23:40 [macd_momentum_regimen] CIERRE DOGE momentum perdido bruto -0.45% neto -0.95%
- 2026-09-29 23:40 [macd_momentum_evento] CIERRE DOGE momentum perdido bruto -0.45% neto -0.95%
- 2026-09-29 23:40 [macd_sin_salida] CIERRE DASH timeout bruto -0.05% neto -0.55%
- 2026-09-29 23:40 [macd_sin_salida] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:40 [macd_momentum] CIERRE BCH momentum perdido bruto -0.62% neto -1.12%
- 2026-09-29 23:40 [macd_momentum_regimen] CIERRE BCH momentum perdido bruto -0.62% neto -1.12%
- 2026-09-29 23:40 [macd_momentum_evento] CIERRE BCH momentum perdido bruto -0.62% neto -1.12%
- 2026-09-29 23:40 [macd_momentum] CIERRE PEPE momentum perdido bruto -0.53% neto -1.03%
- 2026-09-29 23:40 [macd_momentum_regimen] CIERRE PEPE momentum perdido bruto -0.53% neto -1.03%
- 2026-09-29 23:40 [macd_momentum_evento] CIERRE PEPE momentum perdido bruto -0.53% neto -1.03%
- 2026-09-29 23:40 [macd_momentum] CIERRE OP momentum perdido bruto -1.22% neto -1.72%
- 2026-09-29 23:40 [macd_sin_salida] CIERRE OP stop-loss bruto -1.65% neto -2.15%
- 2026-09-29 23:40 [macd_momentum_regimen] CIERRE OP momentum perdido bruto -1.22% neto -1.72%
- 2026-09-29 23:40 [macd_momentum_evento] CIERRE OP momentum perdido bruto -1.22% neto -1.72%
- 2026-09-29 23:40 [pullback_tendencia] CIERRE NIGHT rotura de tendencia bruto -0.04% neto -0.54%
- 2026-09-29 23:40 [c_banda_atr] CIERRE FIL stop-loss bruto -1.89% neto -2.39%
- 2026-09-29 23:40 [c_banda_atr_evento] CIERRE FIL stop-loss bruto -1.89% neto -2.69%
- 2026-09-29 23:40 [macd_momentum] CIERRE PENGU momentum perdido bruto -1.09% neto -1.59%
- 2026-09-29 23:40 [macd_momentum_regimen] CIERRE PENGU momentum perdido bruto -1.09% neto -1.59%
- 2026-09-29 23:40 [macd_momentum_evento] CIERRE PENGU momentum perdido bruto -1.09% neto -1.59%
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
- 2026-09-29 23:50 [macd_momentum] CIERRE BTC momentum perdido bruto +0.16% neto -0.34%
- 2026-09-29 23:50 [macd_momentum_evento] CIERRE BTC momentum perdido bruto +0.16% neto -0.34%
- 2026-09-29 23:50 [ruptura_volumen] CIERRE ZEC timeout bruto -0.05% neto -0.55%
- 2026-09-29 23:50 [ruptura_volumen_tope] CIERRE ZEC timeout bruto -0.05% neto -1.15%
- 2026-09-29 23:50 [ruptura_volumen_evento] CIERRE ZEC timeout bruto -0.05% neto -0.55%
- 2026-09-29 23:45 [reversion_bb] ENTRADA NEAR @ 4.2874 (22.95 €, apertura)
- 2026-09-29 23:50 [macd_momentum] CIERRE PUMP momentum perdido bruto -0.67% neto -1.17%
- 2026-09-29 23:50 [macd_momentum_evento] CIERRE PUMP momentum perdido bruto -0.67% neto -1.17%
- 2026-09-29 23:45 [reversion_bb] ENTRADA ENA @ 0.2184 (22.95 €, apertura)
- 2026-09-29 23:45 [reversion_bb] ENTRADA MON @ 0.02354 (22.95 €, apertura)
- 2026-09-29 23:45 [reversion_bb] ENTRADA INJ @ 6.689 (22.95 €, apertura)
- 2026-09-29 23:50 [macd_momentum] CIERRE ATOM momentum perdido bruto -0.39% neto -0.89%
- 2026-09-29 23:50 [macd_momentum_regimen] CIERRE ATOM momentum perdido bruto -0.39% neto -0.89%
- 2026-09-29 23:50 [macd_momentum_evento] CIERRE ATOM momentum perdido bruto -0.39% neto -0.89%
- 2026-09-29 23:45 [reversion_bb] ENTRADA RENDER @ 1.679 (22.95 €, apertura)
- 2026-09-29 23:45 [reversion_bb] ENTRADA TON @ 1.304 (22.95 €, apertura)
- 2026-09-29 23:50 [macd_momentum] CIERRE POL momentum perdido bruto -0.75% neto -1.25%
- 2026-09-29 23:50 [ruptura_estricta] CIERRE POL timeout bruto -1.11% neto -1.61%
- 2026-09-29 23:50 [macd_momentum_regimen] CIERRE POL momentum perdido bruto -0.75% neto -1.25%
- 2026-09-29 23:50 [macd_momentum_evento] CIERRE POL momentum perdido bruto -0.75% neto -1.25%
- 2026-09-29 23:50 [pullback_tendencia] ENTRADA QNT @ 236.93 (22.61 €, apertura)
- 2026-09-29 23:50 [estocastico_rebote] ENTRADA NEAR @ 4.3209 (22.34 €, apertura)
- 2026-09-29 23:55 [macd_momentum] CIERRE DASH momentum perdido bruto +0.14% neto -0.36%
- 2026-09-29 23:55 [macd_momentum_evento] CIERRE DASH momentum perdido bruto +0.14% neto -0.36%
- 2026-09-29 23:55 [c_banda_atr] ENTRADA ICP @ 3.039 (22.59 €, apertura)
- 2026-09-29 23:55 [macd_momentum] ENTRADA ICP @ 3.039 (22.08 €, apertura)
- 2026-09-29 23:55 [macd_sin_salida] ENTRADA ICP @ 3.039 (22.45 €, apertura)
- 2026-09-29 23:55 [c_banda_atr_evento] ENTRADA ICP @ 3.039 (22.69 €, apertura)
- 2026-09-29 23:55 [macd_momentum_evento] ENTRADA ICP @ 3.039 (22.39 €, apertura)
- 2026-09-29 23:55 [pullback_tendencia] ENTRADA ZRO @ 1.464 (22.61 €, apertura)
- 2026-09-29 23:55 [estocastico_rebote] ENTRADA PEPE @ 3.749e-06 (22.34 €, apertura)
- 2026-09-30 00:00 [c_banda_atr] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:00 [ruptura_estricta] CIERRE NIGHT timeout bruto -0.87% neto -1.37%
- 2026-09-30 00:00 [c_banda_atr_evento] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:55 [estocastico_rebote] ENTRADA PENGU @ 0.00879 (22.34 €, apertura)
- 2026-09-30 00:00 [c_banda_atr] CIERRE XPL stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 00:00 [macd_momentum] CIERRE XPL stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 00:00 [macd_sin_salida] CIERRE XPL stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 00:00 [c_banda_atr_regimen] CIERRE XPL stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 00:00 [macd_momentum_regimen] CIERRE XPL stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 00:00 [c_banda_atr_evento] CIERRE XPL stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 00:00 [macd_momentum_evento] CIERRE XPL stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 00:05 [macd_sin_salida] CIERRE LINK stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:05 [macd_momentum] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 00:05 [macd_sin_salida] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 00:05 [macd_momentum_evento] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 00:00 [reversion_bb] ENTRADA TRX @ 0.294808 (22.95 €, apertura)
- 2026-09-30 00:05 [ruptura_volumen] CIERRE PEPE timeout bruto -0.48% neto -0.98%
- 2026-09-30 00:05 [ruptura_volumen_evento] CIERRE PEPE timeout bruto -0.48% neto -0.98%
- 2026-09-30 00:05 [estocastico_rebote] CIERRE ASTER timeout bruto -0.14% neto -0.64%
- 2026-09-30 00:05 [ruptura_volumen] ENTRADA QNT @ 243.06 (22.54 €, apertura)
- 2026-09-30 00:10 [pullback_tendencia] CIERRE QNT take-profit bruto +2.59% neto +2.09%
- 2026-09-30 00:05 [ruptura_volumen_tope] ENTRADA QNT @ 243.06 (22.86 €, apertura)
- 2026-09-30 00:05 [ruptura_volumen_evento] ENTRADA QNT @ 243.06 (22.68 €, apertura)
- 2026-09-30 00:05 [estocastico_rebote] ENTRADA ZEC @ 1256.37 (22.33 €, apertura)
- 2026-09-30 00:10 [c_banda_atr] CIERRE LTC stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:10 [c_banda_atr_regimen] CIERRE LTC stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:10 [c_banda_atr_evento] CIERRE LTC stop-loss bruto -1.50% neto -2.30%
- 2026-09-30 00:05 [estocastico_rebote] ENTRADA PUMP @ 0.005212 (22.33 €, apertura)
- 2026-09-30 00:05 [ruptura_volumen] ENTRADA XDC @ 0.02947 (22.54 €, apertura)
- 2026-09-30 00:05 [ruptura_volumen_tope] ENTRADA XDC @ 0.02947 (22.86 €, apertura)
- 2026-09-30 00:05 [ruptura_volumen_evento] ENTRADA XDC @ 0.02947 (22.68 €, apertura)
- 2026-09-30 00:05 [c_banda_atr] ENTRADA SHIB @ 5.088e-06 (22.56 €, apertura)
- 2026-09-30 00:10 [macd_sin_salida] CIERRE SHIB timeout bruto +0.02% neto -0.48%
- 2026-09-30 00:05 [c_banda_atr_evento] ENTRADA SHIB @ 5.088e-06 (22.66 €, apertura)
- 2026-09-30 00:05 [macd_momentum] ENTRADA PENGU @ 0.00882 (22.08 €, apertura)
- 2026-09-30 00:05 [macd_momentum_evento] ENTRADA PENGU @ 0.00882 (22.39 €, apertura)
- 2026-09-30 00:15 [ruptura_volumen] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 00:15 [ruptura_volumen_tope] CIERRE QNT stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 00:15 [ruptura_volumen_evento] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 00:15 [ruptura_volumen_tope] CIERRE XLM stop-loss bruto -1.46% neto -2.56%
- 2026-09-30 00:15 [macd_sin_salida] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:15 [c_banda_atr] CIERRE CRV stop-loss bruto -1.67% neto -2.17%
- 2026-09-30 00:15 [c_banda_atr_regimen] CIERRE CRV stop-loss bruto -1.67% neto -2.17%
- 2026-09-30 00:15 [c_banda_atr_evento] CIERRE CRV stop-loss bruto -1.67% neto -2.17%
- 2026-09-30 00:15 [ruptura_volumen] CIERRE DASH stop-loss bruto -1.46% neto -1.96%
- 2026-09-30 00:15 [ruptura_volumen_regimen] CIERRE DASH stop-loss bruto -1.46% neto -1.96%
- 2026-09-30 00:15 [ruptura_volumen_evento] CIERRE DASH stop-loss bruto -1.46% neto -1.96%
- 2026-09-30 00:10 [macd_momentum] ENTRADA SHIB @ 5.088e-06 (22.08 €, apertura)
- 2026-09-30 00:10 [macd_momentum_evento] ENTRADA SHIB @ 5.088e-06 (22.39 €, apertura)
- 2026-09-30 00:10 [c_banda_atr] ENTRADA ASTER @ 0.64169 (22.54 €, apertura)
- 2026-09-30 00:10 [estocastico_rebote] ENTRADA ASTER @ 0.64169 (22.33 €, apertura)
- 2026-09-30 00:10 [c_banda_atr_evento] ENTRADA ASTER @ 0.64169 (22.64 €, apertura)
- 2026-09-30 00:15 [ruptura_estricta] CIERRE SPX timeout bruto -1.08% neto -1.58%
- 2026-09-30 00:20 [reversion_bb] CIERRE NEAR take-profit bruto +1.50% neto +0.40%
- 2026-09-30 00:15 [reversion_bb] ENTRADA DASH @ 53.34 (22.95 €, apertura)
- 2026-09-30 00:15 [macd_momentum] ENTRADA ASTER @ 0.64394 (22.08 €, apertura)
- 2026-09-30 00:20 [macd_sin_salida] CIERRE ASTER timeout bruto +0.75% neto +0.25%
- 2026-09-30 00:15 [macd_momentum_evento] ENTRADA ASTER @ 0.64394 (22.39 €, apertura)
- 2026-09-30 00:20 [pullback_tendencia] ENTRADA QNT @ 241.94 (22.62 €, apertura)
- 2026-09-30 00:25 [pullback_tendencia] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [c_banda_atr] CIERRE XLM timeout bruto -1.13% neto -1.63%
- 2026-09-30 00:25 [c_banda_atr_regimen] CIERRE XLM timeout bruto -1.13% neto -1.63%
- 2026-09-30 00:25 [c_banda_atr_evento] CIERRE XLM timeout bruto -1.13% neto -1.93%
- 2026-09-30 00:20 [reversion_bb] ENTRADA AAVE @ 143.46 (22.95 €, apertura)
- 2026-09-30 00:25 [estocastico_rebote] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [estocastico_rebote] CIERRE PUMP stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [macd_sin_salida] CIERRE PUMP stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [c_banda_atr] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [c_banda_atr_regimen] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [c_banda_atr_evento] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [c_banda_atr] CIERRE ATOM timeout bruto -0.66% neto -1.16%
- 2026-09-30 00:25 [c_banda_atr_regimen] CIERRE ATOM timeout bruto -0.66% neto -1.16%
- 2026-09-30 00:25 [c_banda_atr_evento] CIERRE ATOM timeout bruto -0.66% neto -1.46%
- 2026-09-30 00:25 [c_banda_atr] CIERRE PEPE timeout bruto -0.32% neto -0.82%
- 2026-09-30 00:25 [c_banda_atr_regimen] CIERRE PEPE timeout bruto -0.32% neto -0.82%
- 2026-09-30 00:25 [c_banda_atr_evento] CIERRE PEPE timeout bruto -0.32% neto -1.12%
- 2026-09-30 00:25 [ruptura_volumen] CIERRE RAY stop-loss bruto -1.53% neto -2.03%
- 2026-09-30 00:20 [pullback_tendencia] ENTRADA RAY @ 1.671 (22.61 €, apertura)
- 2026-09-30 00:25 [ruptura_volumen_regimen] CIERRE RAY stop-loss bruto -1.53% neto -2.03%
- 2026-09-30 00:25 [ruptura_volumen_evento] CIERRE RAY stop-loss bruto -1.53% neto -2.03%
- 2026-09-30 00:25 [c_banda_atr] CIERRE TRUMP timeout bruto -0.83% neto -1.33%
- 2026-09-30 00:25 [c_banda_atr_regimen] CIERRE TRUMP timeout bruto -0.83% neto -1.33%
- 2026-09-30 00:25 [c_banda_atr_evento] CIERRE TRUMP timeout bruto -0.83% neto -1.63%
- 2026-09-30 00:25 [c_banda_atr] CIERRE GRT timeout bruto -0.81% neto -1.31%
- 2026-09-30 00:25 [c_banda_atr_regimen] CIERRE GRT timeout bruto -0.81% neto -1.31%
- 2026-09-30 00:25 [c_banda_atr_evento] CIERRE GRT timeout bruto -0.81% neto -1.61%
- 2026-09-30 00:25 [estocastico_rebote] ENTRADA BTC @ 73592.6 (22.31 €, apertura)
- 2026-09-30 00:30 [macd_momentum] CIERRE ICP momentum perdido bruto -0.36% neto -0.86%
- 2026-09-30 00:30 [macd_momentum_evento] CIERRE ICP momentum perdido bruto -0.36% neto -0.86%
- 2026-09-30 00:30 [pullback_tendencia] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-30 00:30 [macd_momentum] CIERRE SHIB momentum perdido bruto -0.55% neto -1.05%
- 2026-09-30 00:30 [macd_momentum_evento] CIERRE SHIB momentum perdido bruto -0.55% neto -1.05%
- 2026-09-30 00:30 [reversion_bb] CIERRE ASTER take-profit bruto +1.50% neto +0.40%
- 2026-09-30 00:35 [estocastico_rebote] CIERRE NEAR take-profit bruto +1.80% neto +1.30%
- 2026-09-30 00:30 [estocastico_rebote] ENTRADA AVAX @ 10.062 (22.32 €, apertura)
- 2026-09-30 00:30 [estocastico_rebote] ENTRADA PUMP @ 0.005092 (22.32 €, apertura)
- 2026-09-30 00:35 [c_banda_atr] CIERRE DASH timeout bruto -1.30% neto -1.80%
- 2026-09-30 00:35 [c_banda_atr_regimen] CIERRE DASH timeout bruto -1.30% neto -1.80%
- 2026-09-30 00:35 [c_banda_atr_evento] CIERRE DASH timeout bruto -1.30% neto -2.10%
- 2026-09-30 00:30 [c_banda_atr] ENTRADA ZRO @ 1.5 (22.49 €, apertura)
- 2026-09-30 00:35 [ruptura_estricta] CIERRE ZRO take-profit bruto +3.00% neto +2.50%
- 2026-09-30 00:30 [c_banda_atr_evento] ENTRADA ZRO @ 1.5 (22.58 €, apertura)
- 2026-09-30 00:30 [estocastico_rebote] ENTRADA USELESS @ 0.21415 (22.32 €, apertura)
- 2026-09-30 00:30 [ruptura_volumen] ENTRADA SEI @ 0.06515 (22.51 €, apertura)
- 2026-09-30 00:30 [macd_momentum] ENTRADA SEI @ 0.06515 (22.07 €, apertura)
- 2026-09-30 00:30 [macd_sin_salida] ENTRADA SEI @ 0.06515 (22.41 €, apertura)
- 2026-09-30 00:30 [ruptura_volumen_tope] ENTRADA SEI @ 0.06515 (22.83 €, apertura)
- 2026-09-30 00:30 [macd_momentum_evento] ENTRADA SEI @ 0.06515 (22.38 €, apertura)
- 2026-09-30 00:30 [ruptura_volumen_evento] ENTRADA SEI @ 0.06515 (22.64 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA ZEC @ 1261.09 (22.07 €, apertura)
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA ZEC @ 1261.09 (22.41 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA ZEC @ 1261.09 (22.38 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA HYPE @ 76.09 (22.07 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA HYPE @ 76.09 (22.38 €, apertura)
- 2026-09-30 00:35 [c_banda_atr] ENTRADA ARB @ 0.1794 (22.49 €, apertura)
- 2026-09-30 00:35 [c_banda_atr_evento] ENTRADA ARB @ 0.1794 (22.58 €, apertura)
- 2026-09-30 00:35 [c_banda_atr] ENTRADA ONDO @ 0.44528 (22.49 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA ONDO @ 0.44528 (22.07 €, apertura)
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA ONDO @ 0.44528 (22.41 €, apertura)
- 2026-09-30 00:35 [c_banda_atr_evento] ENTRADA ONDO @ 0.44528 (22.58 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA ONDO @ 0.44528 (22.38 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA DOT @ 1.0525 (22.07 €, apertura)
- 2026-09-30 00:40 [estocastico_rebote] CIERRE DOT timeout bruto +0.00% neto -0.50%
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA DOT @ 1.0525 (22.41 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA DOT @ 1.0525 (22.38 €, apertura)
- 2026-09-30 00:35 [c_banda_atr] ENTRADA JUP @ 0.29344 (22.49 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA JUP @ 0.29344 (22.07 €, apertura)
- 2026-09-30 00:35 [estocastico_rebote] ENTRADA JUP @ 0.29344 (22.32 €, apertura)
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA JUP @ 0.29344 (22.41 €, apertura)
- 2026-09-30 00:35 [c_banda_atr_evento] ENTRADA JUP @ 0.29344 (22.58 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA JUP @ 0.29344 (22.38 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA ICP @ 3.061 (22.07 €, apertura)
- 2026-09-30 00:40 [estocastico_rebote] CIERRE ICP timeout bruto +0.89% neto +0.39%
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA ICP @ 3.061 (22.38 €, apertura)
- 2026-09-30 00:40 [estocastico_rebote] CIERRE TRX timeout bruto -0.13% neto -0.63%
- 2026-09-30 00:35 [c_banda_atr] ENTRADA WLD @ 0.4293 (22.49 €, apertura)
- 2026-09-30 00:35 [c_banda_atr_evento] ENTRADA WLD @ 0.4293 (22.58 €, apertura)
- 2026-09-30 00:35 [ruptura_volumen] ENTRADA ZRO @ 1.526 (22.51 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA ZRO @ 1.526 (22.07 €, apertura)
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA ZRO @ 1.526 (22.41 €, apertura)
- 2026-09-30 00:35 [ruptura_volumen_tope] ENTRADA ZRO @ 1.526 (22.83 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA ZRO @ 1.526 (22.38 €, apertura)
- 2026-09-30 00:35 [ruptura_volumen_evento] ENTRADA ZRO @ 1.526 (22.64 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA USELESS @ 0.21256 (22.07 €, apertura)
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA USELESS @ 0.21256 (22.41 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA USELESS @ 0.21256 (22.38 €, apertura)
- 2026-09-30 00:35 [c_banda_atr] ENTRADA SPX @ 0.3692 (22.49 €, apertura)
- 2026-09-30 00:35 [macd_momentum] ENTRADA SPX @ 0.3692 (22.07 €, apertura)
- 2026-09-30 00:35 [macd_sin_salida] ENTRADA SPX @ 0.3692 (22.41 €, apertura)
- 2026-09-30 00:35 [c_banda_atr_evento] ENTRADA SPX @ 0.3692 (22.58 €, apertura)
- 2026-09-30 00:35 [macd_momentum_evento] ENTRADA SPX @ 0.3692 (22.38 €, apertura)
- 2026-09-30 00:40 [ruptura_volumen] ENTRADA NEAR @ 4.4438 (22.51 €, apertura)
- 2026-09-30 00:40 [ruptura_estricta] ENTRADA NEAR @ 4.4438 (22.73 €, apertura)
- 2026-09-30 00:40 [ruptura_volumen_evento] ENTRADA NEAR @ 4.4438 (22.64 €, apertura)
- 2026-09-30 00:45 [c_banda_atr] CIERRE ASTER take-profit bruto +2.14% neto +1.64%
- 2026-09-30 00:45 [estocastico_rebote] CIERRE ASTER take-profit bruto +2.14% neto +1.64%
- 2026-09-30 00:45 [c_banda_atr_evento] CIERRE ASTER take-profit bruto +2.14% neto +1.64%
- 2026-09-30 00:50 [ruptura_volumen] CIERRE NEAR stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 00:50 [ruptura_volumen_evento] CIERRE NEAR stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 00:50 [ruptura_estricta] CIERRE BCH timeout bruto -0.64% neto -1.14%
- 2026-09-30 00:45 [c_banda_atr] ENTRADA INJ @ 6.73 (22.50 €, apertura)
- 2026-09-30 00:50 [estocastico_rebote] CIERRE INJ timeout bruto -0.88% neto -1.38%
- 2026-09-30 00:45 [c_banda_atr_evento] ENTRADA INJ @ 6.73 (22.59 €, apertura)
- 2026-09-30 00:45 [ruptura_volumen] ENTRADA SPX @ 0.3706 (22.50 €, apertura)
- 2026-09-30 00:45 [ruptura_volumen_evento] ENTRADA SPX @ 0.3706 (22.64 €, apertura)
- 2026-09-30 00:50 [estocastico_rebote] ENTRADA QNT @ 237.41 (22.32 €, apertura)
- 2026-09-30 00:50 [pullback_tendencia] ENTRADA ZEC @ 1250.5 (22.62 €, apertura)
- 2026-09-30 00:50 [c_banda_atr] ENTRADA RAY @ 1.686 (22.50 €, apertura)
- 2026-09-30 00:50 [estocastico_rebote] ENTRADA RAY @ 1.686 (22.32 €, apertura)
- 2026-09-30 00:50 [c_banda_atr_evento] ENTRADA RAY @ 1.686 (22.59 €, apertura)
- 2026-09-30 00:50 [macd_momentum] ENTRADA NIGHT @ 0.02866 (22.07 €, apertura)
- 2026-09-30 00:50 [macd_momentum_evento] ENTRADA NIGHT @ 0.02866 (22.38 €, apertura)
- 2026-09-30 00:55 [estocastico_rebote] CIERRE SPX timeout bruto +0.38% neto -0.12%
- 2026-09-30 00:55 [pullback_tendencia] ENTRADA NEAR @ 4.3829 (22.62 €, apertura)
- 2026-09-30 01:00 [estocastico_rebote] CIERRE SUI timeout bruto -0.56% neto -1.06%
- 2026-09-30 00:55 [c_banda_atr] ENTRADA CRV @ 0.33508 (22.50 €, apertura)
- 2026-09-30 00:55 [c_banda_atr_evento] ENTRADA CRV @ 0.33508 (22.59 €, apertura)
- 2026-09-30 00:55 [reversion_bb] ENTRADA ATOM @ 1.5149 (22.95 €, apertura)
- 2026-09-30 01:00 [c_banda_atr] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:00 [c_banda_atr_evento] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:05 [macd_sin_salida] CIERRE SOL timeout bruto -0.13% neto -0.63%
- 2026-09-30 01:00 [pullback_tendencia] ENTRADA QNT @ 240 (22.62 €, apertura)
- 2026-09-30 01:00 [c_banda_atr] ENTRADA ADA @ 0.215429 (22.51 €, apertura)
- 2026-09-30 01:00 [macd_momentum] ENTRADA ADA @ 0.215429 (22.07 €, apertura)
- 2026-09-30 01:00 [macd_sin_salida] ENTRADA ADA @ 0.215429 (22.40 €, apertura)
- 2026-09-30 01:00 [c_banda_atr_evento] ENTRADA ADA @ 0.215429 (22.59 €, apertura)
- 2026-09-30 01:00 [macd_momentum_evento] ENTRADA ADA @ 0.215429 (22.38 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] CIERRE XLM timeout bruto -0.81% neto -1.31%
- 2026-09-30 01:05 [estocastico_rebote] CIERRE PUMP take-profit bruto +1.80% neto +1.30%
- 2026-09-30 01:05 [macd_sin_salida] CIERRE HYPE timeout bruto +0.18% neto -0.32%
- 2026-09-30 01:05 [reversion_bb] CIERRE MON take-profit bruto +1.53% neto +0.43%
- 2026-09-30 01:05 [macd_sin_salida] CIERRE NIGHT timeout bruto +0.76% neto +0.26%
- 2026-09-30 01:05 [ruptura_volumen] CIERRE ASTER timeout bruto +1.25% neto +0.75%
- 2026-09-30 01:05 [ruptura_volumen_tope] CIERRE ASTER timeout bruto +1.25% neto +0.15%
- 2026-09-30 01:05 [ruptura_volumen_evento] CIERRE ASTER timeout bruto +1.25% neto +0.75%
- 2026-09-30 01:10 [ruptura_volumen] CIERRE BTC timeout bruto -0.35% neto -0.85%
- 2026-09-30 01:10 [ruptura_volumen_tope] CIERRE BTC timeout bruto -0.35% neto -1.45%
- 2026-09-30 01:10 [ruptura_volumen_regimen] CIERRE BTC timeout bruto -0.35% neto -0.85%
- 2026-09-30 01:10 [ruptura_volumen_evento] CIERRE BTC timeout bruto -0.35% neto -0.85%
- 2026-09-30 01:05 [macd_momentum] ENTRADA SUI @ 1.0196 (22.07 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA SUI @ 1.0196 (22.40 €, apertura)
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA SUI @ 1.0196 (22.38 €, apertura)
- 2026-09-30 01:05 [macd_momentum] ENTRADA AVAX @ 10.087 (22.07 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA AVAX @ 10.087 (22.40 €, apertura)
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA AVAX @ 10.087 (22.38 €, apertura)
- 2026-09-30 01:05 [macd_momentum] ENTRADA PUMP @ 0.005187 (22.07 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA PUMP @ 0.005187 (22.40 €, apertura)
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA PUMP @ 0.005187 (22.38 €, apertura)
- 2026-09-30 01:10 [reversion_bb] CIERRE ALGO take-profit bruto +1.50% neto +0.40%
- 2026-09-30 01:05 [ruptura_volumen] ENTRADA ALGO @ 0.11196 (22.50 €, apertura)
- 2026-09-30 01:05 [ruptura_estricta] ENTRADA ALGO @ 0.11196 (22.73 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen_tope] ENTRADA ALGO @ 0.11196 (22.82 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen_evento] ENTRADA ALGO @ 0.11196 (22.63 €, apertura)
- 2026-09-30 01:05 [c_banda_atr] ENTRADA TAO @ 266.461 (22.51 €, apertura)
- 2026-09-30 01:05 [c_banda_atr_evento] ENTRADA TAO @ 266.461 (22.59 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen] ENTRADA ICP @ 3.077 (22.50 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen_tope] ENTRADA ICP @ 3.077 (22.82 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen_evento] ENTRADA ICP @ 3.077 (22.63 €, apertura)
- 2026-09-30 01:10 [reversion_bb] CIERRE INJ take-profit bruto +2.12% neto +1.02%
- 2026-09-30 01:05 [c_banda_atr] ENTRADA ATOM @ 1.5302 (22.51 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen] ENTRADA ATOM @ 1.5302 (22.50 €, apertura)
- 2026-09-30 01:05 [macd_momentum] ENTRADA ATOM @ 1.5302 (22.07 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA ATOM @ 1.5302 (22.40 €, apertura)
- 2026-09-30 01:05 [c_banda_atr_evento] ENTRADA ATOM @ 1.5302 (22.59 €, apertura)
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA ATOM @ 1.5302 (22.38 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen_evento] ENTRADA ATOM @ 1.5302 (22.63 €, apertura)
- 2026-09-30 01:05 [macd_momentum] ENTRADA PEPE @ 3.767e-06 (22.07 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA PEPE @ 3.767e-06 (22.40 €, apertura)
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA PEPE @ 3.767e-06 (22.38 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen] ENTRADA USELESS @ 0.21587 (22.50 €, apertura)
- 2026-09-30 01:10 [macd_momentum] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:05 [ruptura_estricta] ENTRADA USELESS @ 0.21587 (22.73 €, apertura)
- 2026-09-30 01:10 [macd_sin_salida] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:10 [macd_momentum_evento] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:05 [ruptura_volumen_evento] ENTRADA USELESS @ 0.21587 (22.63 €, apertura)
- 2026-09-30 01:05 [macd_momentum] ENTRADA RAY @ 1.69 (22.08 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA RAY @ 1.69 (22.40 €, apertura)
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA RAY @ 1.69 (22.39 €, apertura)
- 2026-09-30 01:10 [ruptura_volumen] CIERRE SHIB timeout bruto +0.06% neto -0.44%
- 2026-09-30 01:05 [macd_momentum] ENTRADA SHIB @ 5.102e-06 (22.08 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA SHIB @ 5.102e-06 (22.40 €, apertura)
- 2026-09-30 01:10 [ruptura_volumen_regimen] CIERRE SHIB timeout bruto +0.06% neto -0.44%
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA SHIB @ 5.102e-06 (22.39 €, apertura)
- 2026-09-30 01:10 [ruptura_volumen_evento] CIERRE SHIB timeout bruto +0.06% neto -0.44%
- 2026-09-30 01:10 [macd_sin_salida] CIERRE PENGU timeout bruto +1.41% neto +0.91%
- 2026-09-30 01:05 [macd_momentum] ENTRADA BNB @ 670.3 (22.08 €, apertura)
- 2026-09-30 01:10 [macd_sin_salida] CIERRE BNB timeout bruto +0.20% neto -0.30%
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA BNB @ 670.3 (22.39 €, apertura)
- 2026-09-30 01:10 [macd_momentum] CIERRE ASTER take-profit bruto +2.18% neto +1.68%
- 2026-09-30 01:10 [macd_momentum_evento] CIERRE ASTER take-profit bruto +2.18% neto +1.68%
- 2026-09-30 01:15 [estocastico_rebote] CIERRE QNT take-profit bruto +1.80% neto +1.30%
- 2026-09-30 01:15 [ruptura_estricta] CIERRE XLM timeout bruto -1.20% neto -1.70%
- 2026-09-30 01:10 [ruptura_volumen] ENTRADA TAO @ 267.772 (22.49 €, apertura)
- 2026-09-30 01:10 [ruptura_volumen_evento] ENTRADA TAO @ 267.772 (22.63 €, apertura)
- 2026-09-30 01:15 [reversion_bb] CIERRE ARB take-profit bruto +1.50% neto +0.40%
- 2026-09-30 01:15 [reversion_bb] CIERRE RENDER take-profit bruto +1.55% neto +0.45%
- 2026-09-30 01:15 [c_banda_atr] CIERRE WLD take-profit bruto +2.26% neto +1.76%
- 2026-09-30 01:15 [c_banda_atr_evento] CIERRE WLD take-profit bruto +2.26% neto +1.76%
- 2026-09-30 01:15 [ruptura_volumen] CIERRE ZRO take-profit bruto +2.50% neto +2.00%
- 2026-09-30 01:15 [macd_momentum] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:15 [macd_sin_salida] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:15 [ruptura_volumen_tope] CIERRE ZRO take-profit bruto +2.50% neto +1.70%
- 2026-09-30 01:15 [macd_momentum_evento] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:15 [ruptura_volumen_evento] CIERRE ZRO take-profit bruto +2.50% neto +2.00%
- 2026-09-30 01:15 [ruptura_volumen_regimen] CIERRE PEPE timeout bruto -0.45% neto -0.95%
- 2026-09-30 01:10 [ruptura_volumen_tope] ENTRADA USELESS @ 0.21697 (22.83 €, apertura)
- 2026-09-30 01:10 [ruptura_volumen] ENTRADA PENGU @ 0.008933 (22.50 €, apertura)
- 2026-09-30 01:15 [estocastico_rebote] CIERRE PENGU take-profit bruto +1.80% neto +1.30%
- 2026-09-30 01:10 [ruptura_estricta] ENTRADA PENGU @ 0.008933 (22.72 €, apertura)
- 2026-09-30 01:10 [ruptura_volumen_evento] ENTRADA PENGU @ 0.008933 (22.64 €, apertura)
- 2026-09-30 01:15 [ruptura_volumen] CIERRE BNB timeout bruto +0.02% neto -0.48%
- 2026-09-30 01:15 [ruptura_volumen_regimen] CIERRE BNB timeout bruto +0.02% neto -0.48%
- 2026-09-30 01:15 [ruptura_volumen_evento] CIERRE BNB timeout bruto +0.02% neto -0.48%
- 2026-09-30 01:10 [ruptura_volumen] ENTRADA TRUMP @ 1.82 (22.50 €, apertura)
- 2026-09-30 01:10 [ruptura_volumen_evento] ENTRADA TRUMP @ 1.82 (22.64 €, apertura)
- 2026-09-30 01:15 [ruptura_estricta] CIERRE ASTER take-profit bruto +3.00% neto +2.50%
- 2026-09-30 01:15 [macd_momentum] ENTRADA QNT @ 240.68 (22.09 €, apertura)
- 2026-09-30 01:15 [macd_sin_salida] ENTRADA QNT @ 240.68 (22.42 €, apertura)
- 2026-09-30 01:15 [macd_momentum_evento] ENTRADA QNT @ 240.68 (22.41 €, apertura)
- 2026-09-30 01:15 [ruptura_volumen] ENTRADA SUI @ 1.032 (22.50 €, apertura)
- 2026-09-30 01:15 [ruptura_estricta] ENTRADA SUI @ 1.032 (22.73 €, apertura)
- 2026-09-30 01:15 [ruptura_volumen_evento] ENTRADA SUI @ 1.032 (22.64 €, apertura)
- 2026-09-30 01:20 [c_banda_atr] CIERRE BCH timeout bruto -0.21% neto -0.71%
- 2026-09-30 01:20 [c_banda_atr_evento] CIERRE BCH timeout bruto -0.21% neto -1.01%
- 2026-09-30 01:15 [ruptura_estricta] ENTRADA WLD @ 0.4396 (22.73 €, apertura)
- 2026-09-30 01:25 [macd_momentum] CIERRE QNT momentum perdido bruto -0.70% neto -1.20%
- 2026-09-30 01:25 [macd_momentum_evento] CIERRE QNT momentum perdido bruto -0.70% neto -1.20%
- 2026-09-30 01:25 [macd_momentum] CIERRE ZEC momentum perdido bruto -0.39% neto -0.89%
- 2026-09-30 01:25 [macd_momentum_evento] CIERRE ZEC momentum perdido bruto -0.39% neto -0.89%
- 2026-09-30 01:25 [macd_momentum] CIERRE DOT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:25 [macd_sin_salida] CIERRE DOT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:25 [macd_momentum_evento] CIERRE DOT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:25 [c_banda_atr] CIERRE RAY take-profit bruto +2.37% neto +1.87%
- 2026-09-30 01:25 [pullback_tendencia] CIERRE RAY take-profit bruto +3.29% neto +2.79%
- 2026-09-30 01:25 [macd_momentum] CIERRE RAY take-profit bruto +2.13% neto +1.63%
- 2026-09-30 01:25 [estocastico_rebote] CIERRE RAY take-profit bruto +2.37% neto +1.87%
- 2026-09-30 01:25 [macd_sin_salida] CIERRE RAY take-profit bruto +2.13% neto +1.63%
- 2026-09-30 01:25 [c_banda_atr_evento] CIERRE RAY take-profit bruto +2.37% neto +1.87%
- 2026-09-30 01:25 [macd_momentum_evento] CIERRE RAY take-profit bruto +2.13% neto +1.63%
- 2026-09-30 01:25 [macd_momentum] CIERRE PENGU take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:25 [macd_momentum_evento] CIERRE PENGU take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:25 [ruptura_volumen] ENTRADA XRP @ 1.32249 (22.50 €, apertura)
- 2026-09-30 01:25 [ruptura_volumen_regimen] ENTRADA XRP @ 1.32249 (22.58 €, apertura)
- 2026-09-30 01:25 [ruptura_volumen_evento] ENTRADA XRP @ 1.32249 (22.64 €, apertura)
- 2026-09-30 01:30 [pullback_tendencia] CIERRE NEAR take-profit bruto +2.27% neto +1.77%
- 2026-09-30 01:25 [ruptura_volumen] ENTRADA DOT @ 1.0701 (22.50 €, apertura)
- 2026-09-30 01:25 [ruptura_volumen_regimen] ENTRADA DOT @ 1.0701 (22.58 €, apertura)
- 2026-09-30 01:25 [ruptura_volumen_evento] ENTRADA DOT @ 1.0701 (22.64 €, apertura)
- 2026-09-30 01:25 [macd_momentum] ENTRADA DASH @ 53.979 (22.11 €, apertura)
- 2026-09-30 01:25 [macd_sin_salida] ENTRADA DASH @ 53.979 (22.43 €, apertura)
- 2026-09-30 01:25 [macd_momentum_regimen] ENTRADA DASH @ 53.979 (22.18 €, apertura)
- 2026-09-30 01:25 [macd_momentum_evento] ENTRADA DASH @ 53.979 (22.42 €, apertura)
- 2026-09-30 01:30 [reversion_bb] CIERRE FIL take-profit bruto +1.93% neto +0.83%
- 2026-09-30 01:25 [ruptura_volumen_regimen] ENTRADA PENGU @ 0.008966 (22.58 €, apertura)
- 2026-09-30 01:35 [pullback_tendencia] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:35 [macd_sin_salida] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:30 [ruptura_volumen] ENTRADA HBAR @ 0.09119 (22.50 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen_regimen] ENTRADA HBAR @ 0.09119 (22.58 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen_evento] ENTRADA HBAR @ 0.09119 (22.64 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen] ENTRADA JUP @ 0.29764 (22.50 €, apertura)
- 2026-09-30 01:30 [ruptura_estricta] ENTRADA JUP @ 0.29764 (22.73 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen_regimen] ENTRADA JUP @ 0.29764 (22.58 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen_evento] ENTRADA JUP @ 0.29764 (22.64 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen] ENTRADA INJ @ 6.837 (22.50 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen_regimen] ENTRADA INJ @ 6.837 (22.58 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen_evento] ENTRADA INJ @ 6.837 (22.64 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen] ENTRADA RENDER @ 1.716 (22.50 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen_regimen] ENTRADA RENDER @ 1.716 (22.58 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen_evento] ENTRADA RENDER @ 1.716 (22.64 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen] ENTRADA SHIB @ 5.115e-06 (22.50 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen_regimen] ENTRADA SHIB @ 5.115e-06 (22.58 €, apertura)
- 2026-09-30 01:30 [ruptura_volumen_evento] ENTRADA SHIB @ 5.115e-06 (22.64 €, apertura)
- 2026-09-30 01:35 [macd_momentum] ENTRADA QNT @ 244.67 (22.11 €, apertura)
- 2026-09-30 01:35 [macd_momentum_evento] ENTRADA QNT @ 244.67 (22.42 €, apertura)
- 2026-09-30 01:40 [ruptura_volumen_tope] CIERRE USELESS stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 01:40 [pullback_tendencia] ENTRADA SOL @ 105.11 (22.65 €, apertura)
- 2026-09-30 01:45 [c_banda_atr] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:45 [c_banda_atr_evento] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:45 [c_banda_atr_tope] CIERRE BCH timeout bruto -0.41% neto -1.51%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
