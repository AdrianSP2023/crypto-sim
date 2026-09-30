# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 00:31 UTC · vueltas 178 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.48 € (-2.79%) | 87 | 18 | 25% | -0.419% | -1.219% | -1.363% | -24.32 € |
| reversion_bb | 917.55 € (-0.72%) | 20 | 13 | 35% | -0.250% | -1.350% | -1.448% | -6.23 € |
| ruptura_volumen | 900.22 € (-2.60%) | 118 | 5 | 22% | -0.168% | -0.889% | -1.018% | -23.99 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.67 € (-2.12%) | 94 | 1 | 23% | -0.131% | -0.909% | -1.029% | -19.57 € |
| macd_momentum | 882.88 € (-4.48%) | 232 | 2 | 15% | -0.176% | -0.789% | -0.900% | -41.49 € |
| estocastico_rebote | 892.30 € (-3.46%) | 165 | 13 | 32% | -0.184% | -0.843% | -0.962% | -31.77 € |
| ruptura_estricta | 908.82 € (-1.67%) | 51 | 6 | 25% | -0.313% | -1.325% | -1.459% | -15.53 € |
| macd_sin_salida | 895.23 € (-3.14%) | 138 | 8 | 27% | -0.198% | -0.888% | -1.011% | -27.97 € |
| c_banda_atr_tope | 912.62 € (-1.26%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.44 € (-1.17%) | 40 | 3 | 15% | -0.097% | -1.197% | -1.319% | -11.01 € |
| c_banda_atr_regimen | 900.99 € (-2.52%) | 67 | 9 | 24% | -0.506% | -1.395% | -1.529% | -21.46 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.44 € (-2.25%) | 96 | 4 | 22% | -0.151% | -0.922% | -1.053% | -20.29 € |
| c_banda_atr_evento | 902.09 € (-2.40%) | 55 | 18 | 18% | -0.704% | -1.640% | -1.793% | -20.70 € |
| macd_momentum_evento | 895.29 € (-3.13%) | 112 | 2 | 8% | -0.401% | -1.137% | -1.244% | -29.08 € |
| ruptura_volumen_evento | 905.76 € (-2.00%) | 59 | 5 | 12% | -0.415% | -1.362% | -1.495% | -18.45 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 00:30 | macd_momentum_evento | SHIB | momentum perdido | -0.55% | -1.05% | -0.23 |
| 2026-09-30 00:30 | macd_momentum_evento | ICP | momentum perdido | -0.36% | -0.86% | -0.19 |
| 2026-09-30 00:30 | macd_momentum | SHIB | momentum perdido | -0.55% | -1.05% | -0.23 |
| 2026-09-30 00:30 | macd_momentum | ICP | momentum perdido | -0.36% | -0.86% | -0.19 |
| 2026-09-30 00:30 | pullback_tendencia | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 00:30 | reversion_bb | ASTER | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-09-30 00:25 | ruptura_volumen_evento | RAY | stop-loss | -1.53% | -2.03% | -0.46 |
| 2026-09-30 00:25 | c_banda_atr_evento | GRT | timeout | -0.81% | -1.60% | -0.37 |
| 2026-09-30 00:25 | c_banda_atr_evento | TRUMP | timeout | -0.83% | -1.63% | -0.37 |
| 2026-09-30 00:25 | c_banda_atr_evento | PEPE | timeout | -0.32% | -1.12% | -0.26 |
| 2026-09-30 00:25 | c_banda_atr_evento | ATOM | timeout | -0.67% | -1.47% | -0.34 |
| 2026-09-30 00:25 | c_banda_atr_evento | TAO | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 00:25 | c_banda_atr_evento | XLM | timeout | -1.12% | -1.93% | -0.44 |
| 2026-09-30 00:25 | ruptura_volumen_regimen | RAY | stop-loss | -1.53% | -2.03% | -0.46 |
| 2026-09-30 00:25 | c_banda_atr_regimen | GRT | timeout | -0.81% | -1.30% | -0.30 |

## Eventos de la última vuelta

- 2026-09-30 00:25 [estocastico_rebote] ENTRADA BTC @ 73592.6 (22.31 €, apertura)
- 2026-09-30 00:30 [macd_momentum] CIERRE ICP momentum perdido bruto -0.36% neto -0.86%
- 2026-09-30 00:30 [macd_momentum_evento] CIERRE ICP momentum perdido bruto -0.36% neto -0.86%
- 2026-09-30 00:30 [pullback_tendencia] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-30 00:30 [macd_momentum] CIERRE SHIB momentum perdido bruto -0.55% neto -1.05%
- 2026-09-30 00:30 [macd_momentum_evento] CIERRE SHIB momentum perdido bruto -0.55% neto -1.05%
- 2026-09-30 00:30 [reversion_bb] CIERRE ASTER take-profit bruto +1.50% neto +0.40%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
