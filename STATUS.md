# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 03:06 UTC · vueltas 372 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 886.88 € (-4.04%) | 295 | 22 | 35% | -0.002% | -0.590% | -0.711% | -39.54 € |
| reversion_bb | 919.88 € (-0.47%) | 66 | 6 | 58% | +0.515% | -0.381% | -0.486% | -5.81 € |
| ruptura_volumen | 868.70 € (-6.01%) | 336 | 21 | 25% | -0.174% | -0.751% | -0.860% | -56.74 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.02 € (-3.70%) | 196 | 10 | 16% | -0.167% | -0.801% | -0.890% | -35.65 € |
| macd_momentum | 864.10 € (-6.51%) | 532 | 31 | 21% | +0.004% | -0.545% | -0.647% | -64.74 € |
| estocastico_rebote | 874.43 € (-5.39%) | 344 | 15 | 32% | -0.092% | -0.668% | -0.776% | -51.82 € |
| ruptura_estricta | 885.30 € (-4.21%) | 170 | 27 | 25% | -0.432% | -1.087% | -1.204% | -42.02 € |
| macd_sin_salida | 877.19 € (-5.09%) | 368 | 33 | 35% | -0.052% | -0.623% | -0.734% | -51.84 € |
| c_banda_atr_tope | 912.40 € (-1.28%) | 68 | 5 | 32% | +0.108% | -0.780% | -0.894% | -12.20 € |
| ruptura_volumen_tope | 903.84 € (-2.21%) | 111 | 5 | 25% | -0.080% | -0.818% | -0.933% | -20.77 € |
| c_banda_atr_regimen | 898.79 € (-2.75%) | 142 | 29 | 30% | -0.202% | -0.886% | -1.018% | -28.75 € |
| macd_momentum_regimen | 886.40 € (-4.09%) | 298 | 28 | 19% | -0.025% | -0.613% | -0.718% | -41.35 € |
| ruptura_volumen_regimen | 872.82 € (-5.56%) | 263 | 17 | 22% | -0.281% | -0.880% | -0.993% | -52.17 € |
| c_banda_atr_evento | 892.78 € (-3.40%) | 262 | 22 | 36% | +0.037% | -0.564% | -0.680% | -33.65 € |
| macd_momentum_evento | 868.89 € (-5.99%) | 485 | 31 | 19% | +0.002% | -0.552% | -0.651% | -59.98 € |
| ruptura_volumen_evento | 881.06 € (-4.67%) | 286 | 21 | 26% | -0.094% | -0.687% | -0.788% | -44.40 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 03:05 | ruptura_volumen_evento | NEAR | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 03:05 | macd_momentum_evento | KAS | take-profit | +2.18% | +1.68% | +0.36 |
| 2026-10-02 03:05 | macd_momentum_evento | MON | momentum perdido | -0.66% | -1.16% | -0.25 |
| 2026-10-02 03:05 | macd_momentum_evento | DOT | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 03:05 | c_banda_atr_evento | KAS | take-profit | +2.01% | +1.51% | +0.34 |
| 2026-10-02 03:05 | c_banda_atr_evento | TON | timeout | -1.07% | -1.57% | -0.35 |
| 2026-10-02 03:05 | c_banda_atr_evento | XDC | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 03:05 | c_banda_atr_evento | DOT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 03:05 | ruptura_volumen_regimen | NEAR | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 03:05 | macd_momentum_regimen | MON | momentum perdido | -0.66% | -1.16% | -0.26 |
| 2026-10-02 03:05 | macd_momentum_regimen | DOT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 03:05 | c_banda_atr_regimen | XDC | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 03:05 | c_banda_atr_regimen | DOT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 03:05 | c_banda_atr_tope | DOT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 03:05 | macd_sin_salida | KAS | take-profit | +2.18% | +1.68% | +0.36 |

## Eventos de la última vuelta

- 2026-10-02 03:05 [ruptura_volumen] CIERRE NEAR take-profit bruto +2.50% neto +2.00%
- 2026-10-02 03:05 [ruptura_estricta] CIERRE NEAR take-profit bruto +3.00% neto +2.50%
- 2026-10-02 03:05 [ruptura_volumen_regimen] CIERRE NEAR take-profit bruto +2.50% neto +2.00%
- 2026-10-02 03:05 [ruptura_volumen_evento] CIERRE NEAR take-profit bruto +2.50% neto +2.00%
- 2026-10-02 03:05 [reversion_bb] CIERRE AVAX take-profit bruto +1.62% neto +1.12%
- 2026-10-02 03:00 [macd_momentum] ENTRADA HYPE @ 78.91 (21.48 €, apertura)
- 2026-10-02 03:00 [macd_momentum_regimen] ENTRADA HYPE @ 78.91 (22.07 €, apertura)
- 2026-10-02 03:00 [macd_momentum_evento] ENTRADA HYPE @ 78.91 (21.60 €, apertura)
- 2026-10-02 03:05 [reversion_bb] CIERRE XLM take-profit bruto +1.50% neto +1.00%
- 2026-10-02 03:05 [macd_sin_salida] CIERRE LTC timeout bruto +1.12% neto +0.62%
- 2026-10-02 03:05 [c_banda_atr] CIERRE DOT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 03:05 [macd_momentum] CIERRE DOT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 03:05 [macd_sin_salida] CIERRE DOT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 03:05 [c_banda_atr_tope] CIERRE DOT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 03:05 [c_banda_atr_regimen] CIERRE DOT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 03:05 [macd_momentum_regimen] CIERRE DOT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 03:05 [c_banda_atr_evento] CIERRE DOT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 03:05 [macd_momentum_evento] CIERRE DOT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 03:05 [macd_sin_salida] CIERRE ICP timeout bruto +0.31% neto -0.19%
- 2026-10-02 03:00 [c_banda_atr] ENTRADA ONDO @ 0.44352 (22.13 €, apertura)
- 2026-10-02 03:00 [c_banda_atr_tope] ENTRADA ONDO @ 0.44352 (22.80 €, apertura)
- 2026-10-02 03:00 [c_banda_atr_regimen] ENTRADA ONDO @ 0.44352 (22.40 €, apertura)
- 2026-10-02 03:00 [c_banda_atr_evento] ENTRADA ONDO @ 0.44352 (22.28 €, apertura)
- 2026-10-02 03:00 [c_banda_atr] ENTRADA WLD @ 0.4572 (22.13 €, apertura)
- 2026-10-02 03:00 [c_banda_atr_regimen] ENTRADA WLD @ 0.4572 (22.40 €, apertura)
- 2026-10-02 03:00 [c_banda_atr_evento] ENTRADA WLD @ 0.4572 (22.28 €, apertura)
- 2026-10-02 03:05 [c_banda_atr] CIERRE XDC stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 03:05 [c_banda_atr_regimen] CIERRE XDC stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 03:05 [c_banda_atr_evento] CIERRE XDC stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 03:05 [macd_momentum] CIERRE MON momentum perdido bruto -0.66% neto -1.16%
- 2026-10-02 03:05 [macd_momentum_regimen] CIERRE MON momentum perdido bruto -0.66% neto -1.16%
- 2026-10-02 03:05 [macd_momentum_evento] CIERRE MON momentum perdido bruto -0.66% neto -1.16%
- 2026-10-02 03:05 [pullback_tendencia] CIERRE OP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 03:00 [ruptura_estricta] ENTRADA FIL @ 0.911 (22.06 €, apertura)
- 2026-10-02 03:00 [macd_momentum] ENTRADA SHIB @ 5.164e-06 (21.48 €, apertura)
- 2026-10-02 03:00 [macd_momentum_regimen] ENTRADA SHIB @ 5.164e-06 (22.07 €, apertura)
- 2026-10-02 03:00 [macd_momentum_evento] ENTRADA SHIB @ 5.164e-06 (21.60 €, apertura)
- 2026-10-02 03:05 [c_banda_atr] CIERRE TON timeout bruto -1.07% neto -1.57%
- 2026-10-02 03:05 [c_banda_atr_evento] CIERRE TON timeout bruto -1.07% neto -1.57%
- 2026-10-02 03:05 [c_banda_atr] CIERRE KAS take-profit bruto +2.01% neto +1.51%
- 2026-10-02 03:05 [macd_momentum] CIERRE KAS take-profit bruto +2.18% neto +1.68%
- 2026-10-02 03:05 [macd_sin_salida] CIERRE KAS take-profit bruto +2.18% neto +1.68%
- 2026-10-02 03:05 [c_banda_atr_evento] CIERRE KAS take-profit bruto +2.01% neto +1.51%
- 2026-10-02 03:05 [macd_momentum_evento] CIERRE KAS take-profit bruto +2.18% neto +1.68%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
