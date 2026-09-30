# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 22:06 UTC · vueltas 90 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.21 € (-2.38%) | 60 | 22 | 22% | -0.542% | -1.477% | -1.627% | -20.35 € |
| reversion_bb | 921.59 € (-0.29%) | 9 | 4 | 44% | -0.167% | -1.267% | -1.401% | -2.64 € |
| ruptura_volumen | 896.72 € (-2.98%) | 82 | 12 | 15% | -0.610% | -1.428% | -1.572% | -26.83 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.59 € (-2.13%) | 65 | 0 | 15% | -0.413% | -1.319% | -1.456% | -19.65 € |
| macd_momentum | 904.87 € (-2.10%) | 98 | 5 | 23% | -0.105% | -0.871% | -1.005% | -19.58 € |
| estocastico_rebote | 901.62 € (-2.45%) | 122 | 7 | 34% | -0.058% | -0.772% | -0.905% | -21.68 € |
| ruptura_estricta | 898.01 € (-2.84%) | 47 | 6 | 11% | -1.267% | -2.328% | -2.477% | -25.19 € |
| macd_sin_salida | 902.76 € (-2.32%) | 78 | 13 | 32% | -0.295% | -1.130% | -1.263% | -20.27 € |
| c_banda_atr_tope | 919.58 € (-0.50%) | 16 | 4 | 31% | +0.009% | -1.091% | -1.253% | -4.03 € |
| ruptura_volumen_tope | 916.43 € (-0.85%) | 24 | 4 | 17% | -0.322% | -1.422% | -1.541% | -7.86 € |
| c_banda_atr_regimen | 908.47 € (-1.71%) | 45 | 0 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 910.30 € (-1.51%) | 28 | 21 | 11% | -0.818% | -1.918% | -2.056% | -12.37 € |
| macd_momentum_evento | 910.16 € (-1.52%) | 51 | 5 | 16% | -0.227% | -1.221% | -1.352% | -14.30 € |
| ruptura_volumen_evento | 911.13 € (-1.42%) | 32 | 12 | 9% | -0.584% | -1.684% | -1.819% | -12.41 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 22:05 | ruptura_volumen_evento | WLD | stop-loss | -1.52% | -2.62% | -0.60 |
| 2026-09-30 22:05 | macd_momentum_evento | JUP | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-09-30 22:05 | macd_momentum_evento | WLD | stop-loss | -1.56% | -2.06% | -0.47 |
| 2026-09-30 22:05 | c_banda_atr_evento | ARB | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 22:05 | c_banda_atr_evento | DOT | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 22:05 | c_banda_atr_evento | ZEC | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 22:05 | ruptura_volumen_tope | KSM | stop-loss | -1.31% | -2.41% | -0.55 |
| 2026-09-30 22:05 | macd_sin_salida | BNB | timeout | -0.18% | -0.68% | -0.15 |
| 2026-09-30 22:05 | macd_sin_salida | KSM | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 22:05 | macd_sin_salida | ARB | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 22:05 | estocastico_rebote | WLD | timeout | -0.51% | -1.01% | -0.23 |
| 2026-09-30 22:05 | estocastico_rebote | HBAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 22:05 | estocastico_rebote | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 22:05 | macd_momentum | JUP | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-09-30 22:05 | macd_momentum | WLD | stop-loss | -1.56% | -2.06% | -0.47 |

## Eventos de la última vuelta

- 2026-09-30 22:05 [estocastico_rebote] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 22:05 [estocastico_rebote] CIERRE HBAR stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 22:05 [c_banda_atr] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 22:05 [c_banda_atr_evento] CIERRE ZEC stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 22:00 [ruptura_volumen] ENTRADA ZRO @ 1.517 (22.45 €, apertura)
- 2026-09-30 22:00 [ruptura_volumen_tope] ENTRADA ZRO @ 1.517 (22.92 €, apertura)
- 2026-09-30 22:00 [ruptura_volumen_evento] ENTRADA ZRO @ 1.517 (22.81 €, apertura)
- 2026-09-30 22:05 [c_banda_atr] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 22:05 [c_banda_atr_evento] CIERRE DOT stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 22:05 [c_banda_atr] CIERRE ARB stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 22:05 [macd_sin_salida] CIERRE ARB stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 22:05 [c_banda_atr_evento] CIERRE ARB stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 22:05 [pullback_tendencia] CIERRE FET rotura de tendencia bruto -0.90% neto -1.40%
- 2026-09-30 22:05 [ruptura_volumen] CIERRE WLD stop-loss bruto -1.52% neto -2.02%
- 2026-09-30 22:05 [macd_momentum] CIERRE WLD stop-loss bruto -1.56% neto -2.06%
- 2026-09-30 22:05 [estocastico_rebote] CIERRE WLD timeout bruto -0.51% neto -1.01%
- 2026-09-30 22:05 [macd_momentum_evento] CIERRE WLD stop-loss bruto -1.56% neto -2.06%
- 2026-09-30 22:05 [ruptura_volumen_evento] CIERRE WLD stop-loss bruto -1.52% neto -2.62%
- 2026-09-30 22:05 [macd_momentum] CIERRE JUP momentum perdido bruto +0.00% neto -0.50%
- 2026-09-30 22:05 [macd_momentum_evento] CIERRE JUP momentum perdido bruto +0.00% neto -0.50%
- 2026-09-30 22:05 [macd_sin_salida] CIERRE KSM stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 22:05 [ruptura_volumen_tope] CIERRE KSM stop-loss bruto -1.31% neto -2.41%
- 2026-09-30 22:05 [macd_sin_salida] CIERRE BNB timeout bruto -0.18% neto -0.68%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
