# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 02:16 UTC · vueltas 174 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.53 € (-2.35%) | 100 | 20 | 29% | -0.258% | -1.019% | -1.160% | -23.39 € |
| reversion_bb | 919.52 € (-0.51%) | 28 | 6 | 50% | +0.267% | -0.833% | -0.937% | -5.38 € |
| ruptura_volumen | 899.29 € (-2.70%) | 129 | 20 | 22% | -0.158% | -0.860% | -0.988% | -25.36 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.93 € (-1.98%) | 98 | 4 | 26% | -0.055% | -0.822% | -0.950% | -18.47 € |
| macd_momentum | 885.58 € (-4.18%) | 246 | 12 | 17% | -0.109% | -0.715% | -0.828% | -39.90 € |
| estocastico_rebote | 894.09 € (-3.26%) | 178 | 6 | 34% | -0.097% | -0.743% | -0.878% | -30.27 € |
| ruptura_estricta | 908.21 € (-1.73%) | 58 | 10 | 28% | -0.143% | -1.093% | -1.231% | -14.58 € |
| macd_sin_salida | 898.89 € (-2.74%) | 150 | 15 | 30% | -0.096% | -0.770% | -0.895% | -26.41 € |
| c_banda_atr_tope | 911.44 € (-1.38%) | 34 | 3 | 18% | -0.527% | -1.627% | -1.765% | -12.72 € |
| ruptura_volumen_tope | 912.40 € (-1.28%) | 47 | 5 | 19% | -0.032% | -1.087% | -1.212% | -11.75 € |
| c_banda_atr_regimen | 902.89 € (-2.31%) | 69 | 9 | 25% | -0.478% | -1.356% | -1.490% | -21.48 € |
| macd_momentum_regimen | 887.25 € (-4.00%) | 193 | 3 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 902.14 € (-2.39%) | 103 | 12 | 20% | -0.189% | -0.942% | -1.075% | -22.21 € |
| c_banda_atr_evento | 905.61 € (-2.02%) | 68 | 20 | 25% | -0.412% | -1.301% | -1.447% | -20.32 € |
| macd_momentum_evento | 898.02 € (-2.84%) | 126 | 12 | 13% | -0.244% | -0.954% | -1.065% | -27.47 € |
| ruptura_volumen_evento | 904.83 € (-2.10%) | 70 | 20 | 14% | -0.357% | -1.234% | -1.365% | -19.82 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 02:15 | ruptura_volumen_evento | USELESS | stop-loss | -1.44% | -1.94% | -0.44 |
| 2026-09-30 02:15 | macd_momentum_evento | SUI | momentum perdido | +0.51% | +0.01% | +0.00 |
| 2026-09-30 02:15 | ruptura_volumen_regimen | CRV | stop-loss | -1.49% | -1.99% | -0.45 |
| 2026-09-30 02:15 | ruptura_volumen_regimen | QNT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 02:15 | ruptura_estricta | BNB | timeout | +0.06% | -0.44% | -0.10 |
| 2026-09-30 02:15 | macd_momentum | SUI | momentum perdido | +0.51% | +0.01% | +0.00 |
| 2026-09-30 02:15 | pullback_tendencia | NEAR | rotura de tendencia | -0.66% | -1.16% | -0.26 |
| 2026-09-30 02:15 | ruptura_volumen | USELESS | stop-loss | -1.44% | -1.94% | -0.44 |
| 2026-09-30 02:10 | ruptura_volumen_evento | QNT | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 02:10 | macd_momentum_evento | ICP | momentum perdido | +0.42% | -0.07% | -0.02 |
| 2026-09-30 02:10 | c_banda_atr_regimen | PENGU | take-profit | +2.21% | +1.71% | +0.39 |
| 2026-09-30 02:10 | ruptura_volumen_tope | QNT | take-profit | +2.50% | +2.00% | +0.46 |
| 2026-09-30 02:10 | macd_sin_salida | RENDER | timeout | +1.24% | +0.74% | +0.17 |
| 2026-09-30 02:10 | ruptura_estricta | RAY | timeout | +0.47% | -0.03% | -0.01 |
| 2026-09-30 02:10 | ruptura_estricta | QNT | take-profit | +3.00% | +2.50% | +0.57 |

## Eventos de la última vuelta

- 2026-09-30 02:10 [ruptura_volumen] ENTRADA SOL @ 105.66 (22.48 €, apertura)
- 2026-09-30 02:10 [ruptura_volumen_tope] ENTRADA SOL @ 105.66 (22.81 €, apertura)
- 2026-09-30 02:10 [ruptura_volumen_regimen] ENTRADA SOL @ 105.66 (22.57 €, apertura)
- 2026-09-30 02:10 [ruptura_volumen_evento] ENTRADA SOL @ 105.66 (22.62 €, apertura)
- 2026-09-30 02:10 [ruptura_volumen_regimen] ENTRADA QNT @ 262.92 (22.57 €, apertura)
- 2026-09-30 02:15 [ruptura_volumen_regimen] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 02:15 [pullback_tendencia] CIERRE NEAR rotura de tendencia bruto -0.66% neto -1.16%
- 2026-09-30 02:15 [macd_momentum] CIERRE SUI momentum perdido bruto +0.51% neto +0.01%
- 2026-09-30 02:15 [macd_momentum_evento] CIERRE SUI momentum perdido bruto +0.51% neto +0.01%
- 2026-09-30 02:10 [c_banda_atr] ENTRADA XLM @ 0.196139 (22.52 €, apertura)
- 2026-09-30 02:10 [c_banda_atr_tope] ENTRADA XLM @ 0.196139 (22.79 €, apertura)
- 2026-09-30 02:10 [c_banda_atr_regimen] ENTRADA XLM @ 0.196139 (22.57 €, apertura)
- 2026-09-30 02:10 [c_banda_atr_evento] ENTRADA XLM @ 0.196139 (22.60 €, apertura)
- 2026-09-30 02:10 [macd_momentum_regimen] ENTRADA PUMP @ 0.005206 (22.18 €, apertura)
- 2026-09-30 02:15 [ruptura_volumen_regimen] CIERRE CRV stop-loss bruto -1.49% neto -1.99%
- 2026-09-30 02:10 [macd_momentum] ENTRADA VVV @ 23.915 (22.11 €, apertura)
- 2026-09-30 02:10 [macd_sin_salida] ENTRADA VVV @ 23.915 (22.45 €, apertura)
- 2026-09-30 02:10 [macd_momentum_regimen] ENTRADA VVV @ 23.915 (22.18 €, apertura)
- 2026-09-30 02:10 [macd_momentum_evento] ENTRADA VVV @ 23.915 (22.42 €, apertura)
- 2026-09-30 02:15 [ruptura_volumen] CIERRE USELESS stop-loss bruto -1.44% neto -1.94%
- 2026-09-30 02:15 [ruptura_volumen_evento] CIERRE USELESS stop-loss bruto -1.44% neto -1.94%
- 2026-09-30 02:10 [ruptura_volumen] ENTRADA TON @ 1.315 (22.47 €, apertura)
- 2026-09-30 02:10 [ruptura_volumen_regimen] ENTRADA TON @ 1.315 (22.55 €, apertura)
- 2026-09-30 02:10 [ruptura_volumen_evento] ENTRADA TON @ 1.315 (22.61 €, apertura)
- 2026-09-30 02:15 [ruptura_estricta] CIERRE BNB timeout bruto +0.06% neto -0.44%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
