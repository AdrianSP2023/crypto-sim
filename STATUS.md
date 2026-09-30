# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 01:01 UTC · vueltas 184 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.22 € (-2.71%) | 90 | 24 | 27% | -0.374% | -1.164% | -1.308% | -24.02 € |
| reversion_bb | 918.29 € (-0.64%) | 20 | 14 | 35% | -0.250% | -1.350% | -1.448% | -6.23 € |
| ruptura_volumen | 900.22 € (-2.60%) | 119 | 8 | 22% | -0.177% | -0.896% | -1.024% | -24.38 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.26 € (-2.05%) | 94 | 3 | 23% | -0.131% | -0.909% | -1.029% | -19.57 € |
| macd_momentum | 883.57 € (-4.40%) | 232 | 13 | 15% | -0.176% | -0.789% | -0.900% | -41.49 € |
| estocastico_rebote | 892.99 € (-3.38%) | 173 | 11 | 32% | -0.155% | -0.806% | -0.937% | -31.85 € |
| ruptura_estricta | 908.87 € (-1.66%) | 53 | 5 | 26% | -0.257% | -1.249% | -1.386% | -15.22 € |
| macd_sin_salida | 896.38 € (-3.01%) | 138 | 16 | 27% | -0.198% | -0.888% | -1.011% | -27.97 € |
| c_banda_atr_tope | 912.63 € (-1.26%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.85 € (-1.12%) | 40 | 5 | 15% | -0.097% | -1.197% | -1.319% | -11.01 € |
| c_banda_atr_regimen | 901.29 € (-2.48%) | 68 | 8 | 24% | -0.518% | -1.401% | -1.535% | -21.87 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.43 € (-2.25%) | 96 | 4 | 22% | -0.151% | -0.922% | -1.053% | -20.29 € |
| c_banda_atr_evento | 902.77 € (-2.32%) | 58 | 24 | 21% | -0.618% | -1.537% | -1.690% | -20.47 € |
| macd_momentum_evento | 896.00 € (-3.06%) | 112 | 13 | 8% | -0.401% | -1.137% | -1.244% | -29.08 € |
| ruptura_volumen_evento | 905.76 € (-2.00%) | 60 | 8 | 12% | -0.428% | -1.368% | -1.499% | -18.83 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 01:00 | c_banda_atr_evento | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:00 | estocastico_rebote | SUI | timeout | -0.56% | -1.06% | -0.24 |
| 2026-09-30 01:00 | c_banda_atr | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 00:55 | estocastico_rebote | SPX | timeout | +0.38% | -0.12% | -0.03 |
| 2026-09-30 00:50 | ruptura_volumen_evento | NEAR | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 00:50 | ruptura_estricta | BCH | timeout | -0.64% | -1.14% | -0.26 |
| 2026-09-30 00:50 | estocastico_rebote | INJ | timeout | -0.88% | -1.38% | -0.31 |
| 2026-09-30 00:50 | ruptura_volumen | NEAR | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 00:45 | c_banda_atr_evento | ASTER | take-profit | +2.14% | +1.64% | +0.37 |
| 2026-09-30 00:45 | estocastico_rebote | ASTER | take-profit | +2.14% | +1.64% | +0.37 |
| 2026-09-30 00:45 | c_banda_atr | ASTER | take-profit | +2.14% | +1.64% | +0.37 |
| 2026-09-30 00:40 | estocastico_rebote | TRX | timeout | -0.13% | -0.63% | -0.14 |
| 2026-09-30 00:40 | estocastico_rebote | ICP | timeout | +0.89% | +0.39% | +0.09 |
| 2026-09-30 00:40 | estocastico_rebote | DOT | timeout | +0.00% | -0.50% | -0.11 |
| 2026-09-30 00:35 | c_banda_atr_evento | DASH | timeout | -1.30% | -2.10% | -0.48 |

## Eventos de la última vuelta

- 2026-09-30 00:55 [pullback_tendencia] ENTRADA NEAR @ 4.3829 (22.62 €, apertura)
- 2026-09-30 01:00 [estocastico_rebote] CIERRE SUI timeout bruto -0.56% neto -1.06%
- 2026-09-30 00:55 [c_banda_atr] ENTRADA CRV @ 0.33508 (22.50 €, apertura)
- 2026-09-30 00:55 [c_banda_atr_evento] ENTRADA CRV @ 0.33508 (22.59 €, apertura)
- 2026-09-30 00:55 [reversion_bb] ENTRADA ATOM @ 1.5149 (22.95 €, apertura)
- 2026-09-30 01:00 [c_banda_atr] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:00 [c_banda_atr_evento] CIERRE ZRO take-profit bruto +2.00% neto +1.50%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
