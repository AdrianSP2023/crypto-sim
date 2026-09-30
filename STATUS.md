# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 02:06 UTC · vueltas 172 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.49 € (-2.35%) | 100 | 19 | 29% | -0.258% | -1.019% | -1.160% | -23.39 € |
| reversion_bb | 919.42 € (-0.52%) | 28 | 6 | 50% | +0.267% | -0.833% | -0.937% | -5.38 € |
| ruptura_volumen | 899.13 € (-2.72%) | 127 | 18 | 22% | -0.169% | -0.874% | -0.999% | -25.37 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.13 € (-1.96%) | 97 | 4 | 26% | -0.049% | -0.818% | -0.947% | -18.20 € |
| macd_momentum | 885.50 € (-4.19%) | 244 | 13 | 17% | -0.113% | -0.720% | -0.834% | -39.89 € |
| estocastico_rebote | 894.26 € (-3.24%) | 178 | 6 | 34% | -0.097% | -0.743% | -0.878% | -30.27 € |
| ruptura_estricta | 908.26 € (-1.73%) | 55 | 11 | 27% | -0.215% | -1.189% | -1.321% | -15.04 € |
| macd_sin_salida | 898.78 € (-2.76%) | 149 | 15 | 30% | -0.105% | -0.780% | -0.906% | -26.57 € |
| c_banda_atr_tope | 911.49 € (-1.38%) | 34 | 2 | 18% | -0.527% | -1.627% | -1.765% | -12.72 € |
| ruptura_volumen_tope | 912.26 € (-1.30%) | 46 | 3 | 17% | -0.087% | -1.154% | -1.272% | -12.20 € |
| c_banda_atr_regimen | 902.89 € (-2.31%) | 68 | 9 | 24% | -0.518% | -1.401% | -1.536% | -21.87 € |
| macd_momentum_regimen | 887.33 € (-3.99%) | 193 | 1 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 902.70 € (-2.33%) | 101 | 11 | 21% | -0.166% | -0.924% | -1.051% | -21.37 € |
| c_banda_atr_evento | 905.57 € (-2.02%) | 68 | 19 | 25% | -0.412% | -1.301% | -1.447% | -20.32 € |
| macd_momentum_evento | 897.95 € (-2.84%) | 124 | 13 | 13% | -0.256% | -0.968% | -1.080% | -27.45 € |
| ruptura_volumen_evento | 904.67 € (-2.12%) | 68 | 18 | 13% | -0.383% | -1.272% | -1.397% | -19.83 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 02:05 | ruptura_volumen_evento | XDC | timeout | -1.12% | -1.62% | -0.37 |
| 2026-09-30 02:05 | ruptura_volumen_evento | ALGO | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 02:05 | macd_momentum_evento | BNB | momentum perdido | +0.01% | -0.49% | -0.11 |
| 2026-09-30 02:05 | macd_momentum_evento | JUP | momentum perdido | -0.01% | -0.51% | -0.11 |
| 2026-09-30 02:05 | c_banda_atr_evento | BNB | timeout | +0.21% | -0.59% | -0.14 |
| 2026-09-30 02:05 | c_banda_atr_evento | PENGU | timeout | +1.93% | +1.13% | +0.26 |
| 2026-09-30 02:05 | c_banda_atr_evento | AVAX | timeout | -0.68% | -1.48% | -0.34 |
| 2026-09-30 02:05 | c_banda_atr_evento | BTC | timeout | -0.08% | -0.88% | -0.20 |
| 2026-09-30 02:05 | ruptura_volumen_tope | XDC | timeout | -1.12% | -1.92% | -0.44 |
| 2026-09-30 02:05 | ruptura_volumen_tope | ALGO | stop-loss | -1.20% | -2.00% | -0.46 |
| 2026-09-30 02:05 | c_banda_atr_tope | DASH | timeout | +0.64% | -0.46% | -0.10 |
| 2026-09-30 02:05 | c_banda_atr_tope | XLM | timeout | -0.99% | -2.09% | -0.48 |
| 2026-09-30 02:05 | c_banda_atr_tope | BTC | timeout | -0.08% | -1.18% | -0.27 |
| 2026-09-30 02:05 | macd_momentum | BNB | momentum perdido | +0.01% | -0.49% | -0.11 |
| 2026-09-30 02:05 | macd_momentum | JUP | momentum perdido | -0.01% | -0.51% | -0.11 |

## Eventos de la última vuelta

- 2026-09-30 02:05 [c_banda_atr] CIERRE BTC timeout bruto -0.08% neto -0.58%
- 2026-09-30 02:05 [c_banda_atr_tope] CIERRE BTC timeout bruto -0.08% neto -1.18%
- 2026-09-30 02:05 [c_banda_atr_evento] CIERRE BTC timeout bruto -0.08% neto -0.88%
- 2026-09-30 02:05 [c_banda_atr_tope] CIERRE XLM timeout bruto -0.99% neto -2.09%
- 2026-09-30 02:05 [c_banda_atr] CIERRE AVAX timeout bruto -0.68% neto -1.18%
- 2026-09-30 02:05 [c_banda_atr_evento] CIERRE AVAX timeout bruto -0.68% neto -1.48%
- 2026-09-30 02:05 [ruptura_volumen] CIERRE ALGO stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 02:05 [ruptura_volumen_tope] CIERRE ALGO stop-loss bruto -1.20% neto -2.00%
- 2026-09-30 02:05 [ruptura_volumen_evento] CIERRE ALGO stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 02:05 [reversion_bb] CIERRE TAO timeout bruto +0.83% neto -0.27%
- 2026-09-30 02:05 [ruptura_volumen] CIERRE XDC timeout bruto -1.12% neto -1.62%
- 2026-09-30 02:05 [ruptura_volumen_tope] CIERRE XDC timeout bruto -1.12% neto -1.92%
- 2026-09-30 02:05 [ruptura_volumen_evento] CIERRE XDC timeout bruto -1.12% neto -1.62%
- 2026-09-30 02:05 [reversion_bb] CIERRE DASH take-profit bruto +1.51% neto +0.41%
- 2026-09-30 02:05 [c_banda_atr_tope] CIERRE DASH timeout bruto +0.64% neto -0.46%
- 2026-09-30 02:05 [macd_momentum] CIERRE JUP momentum perdido bruto -0.01% neto -0.51%
- 2026-09-30 02:05 [macd_momentum_evento] CIERRE JUP momentum perdido bruto -0.01% neto -0.51%
- 2026-09-30 02:05 [c_banda_atr] CIERRE PENGU timeout bruto +1.93% neto +1.43%
- 2026-09-30 02:05 [c_banda_atr_evento] CIERRE PENGU timeout bruto +1.93% neto +1.13%
- 2026-09-30 02:05 [c_banda_atr] CIERRE BNB timeout bruto +0.21% neto -0.29%
- 2026-09-30 02:05 [macd_momentum] CIERRE BNB momentum perdido bruto +0.01% neto -0.49%
- 2026-09-30 02:05 [c_banda_atr_evento] CIERRE BNB timeout bruto +0.21% neto -0.59%
- 2026-09-30 02:05 [macd_momentum_evento] CIERRE BNB momentum perdido bruto +0.01% neto -0.49%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
