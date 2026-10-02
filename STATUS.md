# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 09:41 UTC · vueltas 405 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.78 € (-3.73%) | 341 | 24 | 40% | +0.136% | -0.441% | -0.561% | -34.27 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 860.25 € (-6.92%) | 424 | 24 | 27% | -0.100% | -0.662% | -0.771% | -62.84 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.82 € (-3.72%) | 244 | 10 | 20% | -0.028% | -0.636% | -0.723% | -35.23 € |
| macd_momentum | 851.82 € (-7.84%) | 689 | 11 | 24% | +0.062% | -0.476% | -0.577% | -72.93 € |
| estocastico_rebote | 879.58 € (-4.83%) | 418 | 26 | 37% | +0.088% | -0.474% | -0.581% | -44.95 € |
| ruptura_estricta | 881.84 € (-4.59%) | 237 | 12 | 32% | -0.154% | -0.765% | -0.882% | -41.27 € |
| macd_sin_salida | 879.81 € (-4.81%) | 446 | 33 | 40% | +0.108% | -0.451% | -0.561% | -45.73 € |
| c_banda_atr_tope | 913.39 € (-1.17%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 900.29 € (-2.59%) | 129 | 4 | 24% | -0.097% | -0.802% | -0.916% | -23.62 € |
| c_banda_atr_regimen | 902.41 € (-2.36%) | 193 | 24 | 40% | +0.146% | -0.489% | -0.617% | -21.72 € |
| macd_momentum_regimen | 874.63 € (-5.37%) | 452 | 11 | 24% | +0.066% | -0.492% | -0.594% | -50.11 € |
| ruptura_volumen_regimen | 864.92 € (-6.42%) | 347 | 24 | 24% | -0.171% | -0.746% | -0.861% | -58.17 € |
| c_banda_atr_evento | 895.70 € (-3.09%) | 308 | 24 | 41% | +0.183% | -0.402% | -0.518% | -28.35 € |
| macd_momentum_evento | 856.54 € (-7.32%) | 642 | 11 | 23% | +0.064% | -0.477% | -0.575% | -68.21 € |
| ruptura_volumen_evento | 872.49 € (-5.60%) | 374 | 24 | 28% | -0.030% | -0.601% | -0.705% | -50.58 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 09:40 | ruptura_volumen_evento | SPX | stop-loss | -1.31% | -1.81% | -0.40 |
| 2026-10-02 09:40 | ruptura_volumen_regimen | SPX | stop-loss | -1.31% | -1.81% | -0.39 |
| 2026-10-02 09:40 | ruptura_volumen_tope | SPX | stop-loss | -1.31% | -1.81% | -0.41 |
| 2026-10-02 09:40 | macd_sin_salida | ADA | timeout | +0.12% | -0.38% | -0.08 |
| 2026-10-02 09:40 | estocastico_rebote | PUMP | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 09:40 | estocastico_rebote | HBAR | take-profit | +1.82% | +1.32% | +0.29 |
| 2026-10-02 09:40 | ruptura_volumen | SPX | stop-loss | -1.31% | -1.81% | -0.39 |
| 2026-10-02 09:35 | macd_momentum_evento | DASH | momentum perdido | -0.16% | -0.66% | -0.14 |
| 2026-10-02 09:35 | macd_momentum_evento | ICP | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 09:35 | macd_momentum_evento | TAO | momentum perdido | +0.77% | +0.27% | +0.06 |
| 2026-10-02 09:35 | macd_momentum_regimen | DASH | momentum perdido | -0.16% | -0.66% | -0.14 |
| 2026-10-02 09:35 | macd_momentum_regimen | ICP | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 09:35 | macd_momentum_regimen | TAO | momentum perdido | +0.77% | +0.27% | +0.06 |
| 2026-10-02 09:35 | macd_sin_salida | SHIB | timeout | +0.71% | +0.21% | +0.04 |
| 2026-10-02 09:35 | macd_sin_salida | XRP | timeout | +0.76% | +0.26% | +0.06 |

## Eventos de la última vuelta

- 2026-10-02 09:35 [estocastico_rebote] ENTRADA BTC @ 76750.2 (21.99 €, apertura)
- 2026-10-02 09:40 [macd_sin_salida] CIERRE ADA timeout bruto +0.12% neto -0.38%
- 2026-10-02 09:40 [estocastico_rebote] CIERRE HBAR take-profit bruto +1.82% neto +1.32%
- 2026-10-02 09:40 [estocastico_rebote] CIERRE PUMP stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 09:35 [ruptura_volumen] ENTRADA XLM @ 0.200447 (21.54 €, apertura)
- 2026-10-02 09:35 [macd_momentum] ENTRADA XLM @ 0.200447 (21.28 €, apertura)
- 2026-10-02 09:35 [ruptura_estricta] ENTRADA XLM @ 0.200447 (22.07 €, apertura)
- 2026-10-02 09:35 [macd_momentum_regimen] ENTRADA XLM @ 0.200447 (21.85 €, apertura)
- 2026-10-02 09:35 [ruptura_volumen_regimen] ENTRADA XLM @ 0.200447 (21.66 €, apertura)
- 2026-10-02 09:35 [macd_momentum_evento] ENTRADA XLM @ 0.200447 (21.40 €, apertura)
- 2026-10-02 09:35 [ruptura_volumen_evento] ENTRADA XLM @ 0.200447 (21.85 €, apertura)
- 2026-10-02 09:35 [ruptura_volumen] ENTRADA WLD @ 0.482 (21.54 €, apertura)
- 2026-10-02 09:35 [ruptura_estricta] ENTRADA WLD @ 0.482 (22.07 €, apertura)
- 2026-10-02 09:35 [ruptura_volumen_regimen] ENTRADA WLD @ 0.482 (21.66 €, apertura)
- 2026-10-02 09:35 [ruptura_volumen_evento] ENTRADA WLD @ 0.482 (21.85 €, apertura)
- 2026-10-02 09:35 [ruptura_volumen] ENTRADA NIGHT @ 0.03939 (21.54 €, apertura)
- 2026-10-02 09:35 [macd_momentum] ENTRADA NIGHT @ 0.03939 (21.28 €, apertura)
- 2026-10-02 09:35 [ruptura_estricta] ENTRADA NIGHT @ 0.03939 (22.07 €, apertura)
- 2026-10-02 09:35 [macd_sin_salida] ENTRADA NIGHT @ 0.03939 (21.96 €, apertura)
- 2026-10-02 09:35 [macd_momentum_regimen] ENTRADA NIGHT @ 0.03939 (21.85 €, apertura)
- 2026-10-02 09:35 [ruptura_volumen_regimen] ENTRADA NIGHT @ 0.03939 (21.66 €, apertura)
- 2026-10-02 09:35 [macd_momentum_evento] ENTRADA NIGHT @ 0.03939 (21.40 €, apertura)
- 2026-10-02 09:35 [ruptura_volumen_evento] ENTRADA NIGHT @ 0.03939 (21.85 €, apertura)
- 2026-10-02 09:35 [ruptura_estricta] ENTRADA TRUMP @ 1.887 (22.07 €, apertura)
- 2026-10-02 09:40 [ruptura_volumen] CIERRE SPX stop-loss bruto -1.31% neto -1.81%
- 2026-10-02 09:40 [ruptura_volumen_tope] CIERRE SPX stop-loss bruto -1.31% neto -1.81%
- 2026-10-02 09:40 [ruptura_volumen_regimen] CIERRE SPX stop-loss bruto -1.31% neto -1.81%
- 2026-10-02 09:40 [ruptura_volumen_evento] CIERRE SPX stop-loss bruto -1.31% neto -1.81%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
