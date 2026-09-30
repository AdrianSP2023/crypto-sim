# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 02:31 UTC · vueltas 177 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.31 € (-2.70%) | 102 | 18 | 28% | -0.282% | -1.038% | -1.179% | -24.29 € |
| reversion_bb | 919.10 € (-0.56%) | 29 | 5 | 48% | +0.205% | -0.895% | -0.997% | -5.98 € |
| ruptura_volumen | 896.05 € (-3.05%) | 134 | 17 | 22% | -0.199% | -0.894% | -1.025% | -27.34 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.61 € (-2.02%) | 101 | 5 | 26% | -0.039% | -0.797% | -0.925% | -18.46 € |
| macd_momentum | 883.93 € (-4.36%) | 252 | 7 | 17% | -0.106% | -0.710% | -0.823% | -40.59 € |
| estocastico_rebote | 893.36 € (-3.34%) | 178 | 6 | 34% | -0.097% | -0.743% | -0.878% | -30.27 € |
| ruptura_estricta | 905.83 € (-1.99%) | 62 | 7 | 26% | -0.268% | -1.189% | -1.333% | -16.93 € |
| macd_sin_salida | 896.33 € (-3.02%) | 152 | 14 | 30% | -0.114% | -0.786% | -0.911% | -27.30 € |
| c_banda_atr_tope | 910.43 € (-1.49%) | 35 | 2 | 17% | -0.565% | -1.665% | -1.801% | -13.39 € |
| ruptura_volumen_tope | 911.25 € (-1.41%) | 49 | 4 | 18% | -0.084% | -1.123% | -1.247% | -12.65 € |
| c_banda_atr_regimen | 901.69 € (-2.44%) | 69 | 9 | 25% | -0.478% | -1.356% | -1.490% | -21.48 € |
| macd_momentum_regimen | 886.93 € (-4.04%) | 194 | 2 | 15% | -0.208% | -0.843% | -0.955% | -37.16 € |
| ruptura_volumen_regimen | 900.13 € (-2.61%) | 105 | 11 | 20% | -0.210% | -0.958% | -1.093% | -23.02 € |
| c_banda_atr_evento | 902.38 € (-2.37%) | 70 | 18 | 24% | -0.443% | -1.321% | -1.466% | -21.22 € |
| macd_momentum_evento | 896.35 € (-3.02%) | 132 | 7 | 14% | -0.234% | -0.934% | -1.045% | -28.16 € |
| ruptura_volumen_evento | 901.56 € (-2.45%) | 75 | 17 | 13% | -0.417% | -1.269% | -1.405% | -21.81 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 02:30 | ruptura_volumen_evento | SEI | timeout | -0.84% | -1.34% | -0.30 |
| 2026-09-30 02:30 | macd_momentum_evento | SHIB | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-09-30 02:30 | macd_momentum_evento | NIGHT | momentum perdido | +1.15% | +0.65% | +0.15 |
| 2026-09-30 02:30 | c_banda_atr_evento | ONDO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 02:30 | ruptura_volumen_tope | SEI | timeout | -0.84% | -1.64% | -0.38 |
| 2026-09-30 02:30 | macd_sin_salida | ONDO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 02:30 | ruptura_estricta | USELESS | stop-loss | -2.16% | -2.66% | -0.60 |
| 2026-09-30 02:30 | ruptura_estricta | JUP | stop-loss | -2.16% | -2.66% | -0.60 |
| 2026-09-30 02:30 | ruptura_estricta | NEAR | stop-loss | -2.00% | -2.50% | -0.57 |
| 2026-09-30 02:30 | macd_momentum | SHIB | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-09-30 02:30 | macd_momentum | NIGHT | momentum perdido | +1.15% | +0.65% | +0.14 |
| 2026-09-30 02:30 | pullback_tendencia | SUI | rotura de tendencia | -0.34% | -0.84% | -0.19 |
| 2026-09-30 02:30 | ruptura_volumen | SEI | timeout | -0.84% | -1.34% | -0.30 |
| 2026-09-30 02:30 | c_banda_atr | ONDO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 02:25 | ruptura_volumen_evento | SUI | stop-loss | -1.24% | -1.74% | -0.39 |

## Eventos de la última vuelta

- 2026-09-30 02:30 [ruptura_estricta] CIERRE NEAR stop-loss bruto -2.00% neto -2.50%
- 2026-09-30 02:30 [pullback_tendencia] CIERRE SUI rotura de tendencia bruto -0.34% neto -0.84%
- 2026-09-30 02:30 [c_banda_atr] CIERRE ONDO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 02:30 [macd_sin_salida] CIERRE ONDO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 02:30 [c_banda_atr_evento] CIERRE ONDO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 02:30 [ruptura_estricta] CIERRE JUP stop-loss bruto -2.16% neto -2.66%
- 2026-09-30 02:30 [ruptura_estricta] CIERRE USELESS stop-loss bruto -2.16% neto -2.66%
- 2026-09-30 02:30 [ruptura_volumen] CIERRE SEI timeout bruto -0.84% neto -1.34%
- 2026-09-30 02:30 [ruptura_volumen_tope] CIERRE SEI timeout bruto -0.84% neto -1.64%
- 2026-09-30 02:30 [ruptura_volumen_evento] CIERRE SEI timeout bruto -0.84% neto -1.34%
- 2026-09-30 02:30 [macd_momentum] CIERRE NIGHT momentum perdido bruto +1.15% neto +0.65%
- 2026-09-30 02:30 [macd_momentum_evento] CIERRE NIGHT momentum perdido bruto +1.15% neto +0.65%
- 2026-09-30 02:30 [macd_momentum] CIERRE SHIB momentum perdido bruto -0.27% neto -0.77%
- 2026-09-30 02:30 [macd_momentum_evento] CIERRE SHIB momentum perdido bruto -0.27% neto -0.77%
- 2026-09-30 02:25 [pullback_tendencia] ENTRADA PENGU @ 0.00893 (22.64 €, apertura)
- 2026-09-30 02:25 [macd_momentum] ENTRADA BNB @ 670.79 (22.09 €, apertura)
- 2026-09-30 02:25 [macd_sin_salida] ENTRADA BNB @ 670.79 (22.42 €, apertura)
- 2026-09-30 02:25 [macd_momentum_evento] ENTRADA BNB @ 670.79 (22.40 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
