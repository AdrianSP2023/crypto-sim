# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 23:31 UTC · vueltas 166 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 904.98 € (-2.08%) | 70 | 32 | 31% | -0.192% | -1.064% | -1.210% | -17.15 € |
| reversion_bb | 918.03 € (-0.67%) | 18 | 4 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 902.19 € (-2.39%) | 111 | 10 | 23% | -0.114% | -0.849% | -0.977% | -21.59 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.81 € (-1.99%) | 86 | 3 | 23% | -0.156% | -0.959% | -1.081% | -18.91 € |
| macd_momentum | 888.90 € (-3.82%) | 201 | 29 | 17% | -0.104% | -0.733% | -0.849% | -33.57 € |
| estocastico_rebote | 893.60 € (-3.31%) | 162 | 9 | 33% | -0.168% | -0.830% | -0.950% | -30.73 € |
| ruptura_estricta | 909.91 € (-1.55%) | 48 | 9 | 27% | -0.269% | -1.312% | -1.445% | -14.49 € |
| macd_sin_salida | 899.81 € (-2.64%) | 122 | 23 | 29% | -0.121% | -0.835% | -0.962% | -23.32 € |
| c_banda_atr_tope | 913.24 € (-1.19%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 915.01 € (-1.00%) | 36 | 5 | 17% | +0.001% | -1.099% | -1.219% | -9.11 € |
| c_banda_atr_regimen | 905.84 € (-1.99%) | 54 | 22 | 30% | -0.322% | -1.305% | -1.444% | -16.23 € |
| macd_momentum_regimen | 891.80 € (-3.51%) | 173 | 20 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 904.77 € (-2.11%) | 93 | 7 | 23% | -0.110% | -0.891% | -1.020% | -19.00 € |
| c_banda_atr_evento | 909.25 € (-1.62%) | 38 | 32 | 26% | -0.412% | -1.472% | -1.631% | -12.88 € |
| macd_momentum_evento | 901.39 € (-2.47%) | 81 | 29 | 10% | -0.307% | -1.133% | -1.247% | -21.04 € |
| ruptura_volumen_evento | 907.75 € (-1.78%) | 52 | 10 | 13% | -0.333% | -1.341% | -1.472% | -16.03 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 23:30 | macd_momentum_evento | HYPE | momentum perdido | +0.05% | -0.45% | -0.10 |
| 2026-09-29 23:30 | c_banda_atr_evento | ARB | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-29 23:30 | c_banda_atr_regimen | ARB | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 23:30 | macd_sin_salida | GRT | timeout | -1.11% | -1.61% | -0.36 |
| 2026-09-29 23:30 | macd_sin_salida | PEPE | timeout | +0.16% | -0.34% | -0.08 |
| 2026-09-29 23:30 | macd_sin_salida | ATOM | timeout | -0.58% | -1.08% | -0.24 |
| 2026-09-29 23:30 | macd_sin_salida | DOT | timeout | -0.45% | -0.95% | -0.22 |
| 2026-09-29 23:30 | macd_sin_salida | DOGE | timeout | +0.06% | -0.44% | -0.10 |
| 2026-09-29 23:30 | macd_sin_salida | ARB | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 23:30 | macd_sin_salida | SUI | timeout | -0.35% | -0.85% | -0.19 |
| 2026-09-29 23:30 | macd_sin_salida | BTC | timeout | +0.09% | -0.41% | -0.09 |
| 2026-09-29 23:30 | macd_momentum | HYPE | momentum perdido | +0.05% | -0.45% | -0.10 |
| 2026-09-29 23:30 | c_banda_atr | ARB | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 23:25 | ruptura_volumen_evento | ZRO | stop-loss | -1.33% | -1.83% | -0.42 |
| 2026-09-29 23:25 | ruptura_volumen_regimen | ZRO | stop-loss | -1.33% | -1.83% | -0.41 |

## Eventos de la última vuelta

- 2026-09-29 23:30 [macd_sin_salida] CIERRE BTC timeout bruto +0.09% neto -0.41%
- 2026-09-29 23:30 [macd_sin_salida] CIERRE SUI timeout bruto -0.35% neto -0.85%
- 2026-09-29 23:30 [macd_momentum] CIERRE HYPE momentum perdido bruto +0.05% neto -0.45%
- 2026-09-29 23:30 [macd_momentum_evento] CIERRE HYPE momentum perdido bruto +0.05% neto -0.45%
- 2026-09-29 23:30 [c_banda_atr] CIERRE ARB stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:30 [macd_sin_salida] CIERRE ARB stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:30 [c_banda_atr_regimen] CIERRE ARB stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 23:30 [c_banda_atr_evento] CIERRE ARB stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 23:30 [macd_sin_salida] CIERRE DOGE timeout bruto +0.06% neto -0.44%
- 2026-09-29 23:30 [macd_sin_salida] CIERRE DOT timeout bruto -0.45% neto -0.95%
- 2026-09-29 23:30 [macd_sin_salida] CIERRE ATOM timeout bruto -0.58% neto -1.08%
- 2026-09-29 23:30 [macd_sin_salida] CIERRE PEPE timeout bruto +0.16% neto -0.34%
- 2026-09-29 23:30 [macd_sin_salida] CIERRE GRT timeout bruto -1.11% neto -1.61%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
