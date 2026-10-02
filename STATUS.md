# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 07:06 UTC · vueltas 374 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.33 € (-3.78%) | 331 | 17 | 40% | +0.134% | -0.445% | -0.566% | -33.59 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 862.76 € (-6.65%) | 406 | 7 | 27% | -0.116% | -0.680% | -0.787% | -61.85 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.93 € (-3.60%) | 227 | 12 | 21% | -0.026% | -0.642% | -0.730% | -33.14 € |
| macd_momentum | 854.03 € (-7.60%) | 636 | 7 | 22% | +0.043% | -0.498% | -0.599% | -70.47 € |
| estocastico_rebote | 878.49 € (-4.95%) | 382 | 33 | 36% | +0.045% | -0.523% | -0.632% | -45.33 € |
| ruptura_estricta | 885.60 € (-4.18%) | 211 | 23 | 34% | -0.153% | -0.778% | -0.893% | -37.46 € |
| macd_sin_salida | 881.24 € (-4.65%) | 416 | 28 | 41% | +0.119% | -0.443% | -0.555% | -42.09 € |
| c_banda_atr_tope | 913.26 € (-1.19%) | 75 | 4 | 37% | +0.236% | -0.616% | -0.732% | -10.63 € |
| ruptura_volumen_tope | 902.39 € (-2.36%) | 122 | 5 | 25% | -0.066% | -0.783% | -0.895% | -21.84 € |
| c_banda_atr_regimen | 901.78 € (-2.43%) | 183 | 18 | 40% | +0.149% | -0.494% | -0.624% | -20.82 € |
| macd_momentum_regimen | 876.90 € (-5.12%) | 399 | 7 | 22% | +0.037% | -0.529% | -0.632% | -47.59 € |
| ruptura_volumen_regimen | 867.44 € (-6.15%) | 329 | 7 | 24% | -0.194% | -0.773% | -0.886% | -57.17 € |
| c_banda_atr_evento | 895.25 € (-3.14%) | 298 | 17 | 41% | +0.183% | -0.405% | -0.522% | -27.66 € |
| macd_momentum_evento | 858.76 € (-7.08%) | 589 | 7 | 21% | +0.045% | -0.500% | -0.598% | -65.74 € |
| ruptura_volumen_evento | 875.03 € (-5.32%) | 356 | 7 | 28% | -0.044% | -0.618% | -0.719% | -49.57 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 07:05 | ruptura_volumen_evento | SEI | timeout | -1.17% | -1.67% | -0.37 |
| 2026-10-02 07:05 | ruptura_volumen_evento | KAS | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:05 | macd_momentum_evento | KAS | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 07:05 | macd_momentum_evento | MINA | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 07:05 | macd_momentum_evento | SUI | momentum perdido | -0.66% | -1.16% | -0.25 |
| 2026-10-02 07:05 | c_banda_atr_evento | SPX | timeout | +1.50% | +1.00% | +0.22 |
| 2026-10-02 07:05 | ruptura_volumen_regimen | SEI | timeout | -1.17% | -1.67% | -0.36 |
| 2026-10-02 07:05 | ruptura_volumen_regimen | KAS | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:05 | macd_momentum_regimen | KAS | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 07:05 | macd_momentum_regimen | MINA | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 07:05 | macd_momentum_regimen | SUI | momentum perdido | -0.66% | -1.16% | -0.26 |
| 2026-10-02 07:05 | macd_sin_salida | MINA | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 07:05 | ruptura_estricta | ALGO | take-profit | +3.00% | +2.50% | +0.55 |
| 2026-10-02 07:05 | macd_momentum | KAS | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 07:05 | macd_momentum | MINA | take-profit | +2.00% | +1.50% | +0.32 |

## Eventos de la última vuelta

- 2026-10-02 07:00 [pullback_tendencia] ENTRADA ETH @ 2422.98 (22.27 €, apertura)
- 2026-10-02 07:05 [macd_momentum] CIERRE SUI momentum perdido bruto -0.66% neto -1.16%
- 2026-10-02 07:05 [macd_momentum_regimen] CIERRE SUI momentum perdido bruto -0.66% neto -1.16%
- 2026-10-02 07:05 [macd_momentum_evento] CIERRE SUI momentum perdido bruto -0.66% neto -1.16%
- 2026-10-02 07:00 [macd_momentum] ENTRADA AVAX @ 9.85 (21.35 €, apertura)
- 2026-10-02 07:00 [macd_momentum_regimen] ENTRADA AVAX @ 9.85 (21.92 €, apertura)
- 2026-10-02 07:00 [macd_momentum_evento] ENTRADA AVAX @ 9.85 (21.47 €, apertura)
- 2026-10-02 07:00 [pullback_tendencia] ENTRADA HYPE @ 80.06 (22.27 €, apertura)
- 2026-10-02 07:05 [pullback_tendencia] CIERRE XLM rotura de tendencia bruto -0.20% neto -0.70%
- 2026-10-02 07:05 [ruptura_estricta] CIERRE ALGO take-profit bruto +3.00% neto +2.50%
- 2026-10-02 07:05 [pullback_tendencia] CIERRE NIGHT take-profit bruto +2.49% neto +1.99%
- 2026-10-02 07:05 [pullback_tendencia] CIERRE PEPE rotura de tendencia bruto -0.84% neto -1.34%
- 2026-10-02 07:05 [pullback_tendencia] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-02 07:05 [macd_momentum] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-02 07:05 [macd_sin_salida] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-02 07:05 [macd_momentum_regimen] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-02 07:05 [macd_momentum_evento] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-02 07:05 [ruptura_volumen] CIERRE KAS stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:05 [macd_momentum] CIERRE KAS stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 07:05 [macd_momentum_regimen] CIERRE KAS stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 07:05 [ruptura_volumen_regimen] CIERRE KAS stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:05 [macd_momentum_evento] CIERRE KAS stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 07:05 [ruptura_volumen_evento] CIERRE KAS stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:05 [ruptura_volumen] CIERRE SEI timeout bruto -1.17% neto -1.67%
- 2026-10-02 07:05 [ruptura_volumen_regimen] CIERRE SEI timeout bruto -1.17% neto -1.67%
- 2026-10-02 07:05 [ruptura_volumen_evento] CIERRE SEI timeout bruto -1.17% neto -1.67%
- 2026-10-02 07:05 [c_banda_atr] CIERRE SPX timeout bruto +1.50% neto +1.00%
- 2026-10-02 07:05 [c_banda_atr_evento] CIERRE SPX timeout bruto +1.50% neto +1.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
