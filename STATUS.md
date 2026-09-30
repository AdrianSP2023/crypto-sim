# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 00:36 UTC · vueltas 179 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.52 € (-2.67%) | 88 | 18 | 25% | -0.429% | -1.226% | -1.370% | -24.73 € |
| reversion_bb | 918.14 € (-0.66%) | 20 | 13 | 35% | -0.250% | -1.350% | -1.448% | -6.23 € |
| ruptura_volumen | 900.42 € (-2.58%) | 118 | 6 | 22% | -0.168% | -0.889% | -1.018% | -23.99 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.67 € (-2.12%) | 94 | 1 | 23% | -0.131% | -0.909% | -1.029% | -19.57 € |
| macd_momentum | 883.12 € (-4.45%) | 232 | 3 | 15% | -0.176% | -0.789% | -0.900% | -41.49 € |
| estocastico_rebote | 893.26 € (-3.35%) | 166 | 15 | 33% | -0.172% | -0.830% | -0.949% | -31.48 € |
| ruptura_estricta | 908.80 € (-1.67%) | 52 | 5 | 27% | -0.249% | -1.251% | -1.388% | -14.96 € |
| macd_sin_salida | 895.94 € (-3.06%) | 138 | 9 | 27% | -0.198% | -0.888% | -1.011% | -27.97 € |
| c_banda_atr_tope | 912.67 € (-1.25%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.50 € (-1.16%) | 40 | 4 | 15% | -0.097% | -1.197% | -1.319% | -11.01 € |
| c_banda_atr_regimen | 901.40 € (-2.47%) | 68 | 8 | 24% | -0.518% | -1.401% | -1.535% | -21.87 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.60 € (-2.23%) | 96 | 4 | 22% | -0.151% | -0.922% | -1.053% | -20.29 € |
| c_banda_atr_evento | 903.07 € (-2.29%) | 56 | 18 | 18% | -0.714% | -1.648% | -1.800% | -21.18 € |
| macd_momentum_evento | 895.53 € (-3.11%) | 112 | 3 | 8% | -0.401% | -1.137% | -1.244% | -29.08 € |
| ruptura_volumen_evento | 905.96 € (-1.98%) | 59 | 6 | 12% | -0.415% | -1.362% | -1.495% | -18.45 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 00:35 | c_banda_atr_evento | DASH | timeout | -1.30% | -2.10% | -0.48 |
| 2026-09-30 00:35 | c_banda_atr_regimen | DASH | timeout | -1.30% | -1.80% | -0.41 |
| 2026-09-30 00:35 | ruptura_estricta | ZRO | take-profit | +3.00% | +2.50% | +0.57 |
| 2026-09-30 00:35 | estocastico_rebote | NEAR | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 00:35 | c_banda_atr | DASH | timeout | -1.30% | -1.80% | -0.41 |
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

## Eventos de la última vuelta

- 2026-09-30 00:35 [estocastico_rebote] CIERRE NEAR take-profit bruto +1.80% neto +1.30%
- 2026-09-30 00:30 [estocastico_rebote] ENTRADA AVAX @ 10.062 (22.32 €, apertura)
- 2026-09-30 00:30 [estocastico_rebote] ENTRADA PUMP @ 0.005092 (22.32 €, apertura)
- 2026-09-30 00:35 [c_banda_atr] CIERRE DASH timeout bruto -1.30% neto -1.80%
- 2026-09-30 00:35 [c_banda_atr_regimen] CIERRE DASH timeout bruto -1.30% neto -1.80%
- 2026-09-30 00:35 [c_banda_atr_evento] CIERRE DASH timeout bruto -1.30% neto -2.10%
- 2026-09-30 00:30 [c_banda_atr] ENTRADA ZRO @ 1.5 (22.49 €, apertura)
- 2026-09-30 00:35 [ruptura_estricta] CIERRE ZRO take-profit bruto +3.00% neto +2.50%
- 2026-09-30 00:30 [c_banda_atr_evento] ENTRADA ZRO @ 1.5 (22.58 €, apertura)
- 2026-09-30 00:30 [estocastico_rebote] ENTRADA USELESS @ 0.21415 (22.32 €, apertura)
- 2026-09-30 00:30 [ruptura_volumen] ENTRADA SEI @ 0.06515 (22.51 €, apertura)
- 2026-09-30 00:30 [macd_momentum] ENTRADA SEI @ 0.06515 (22.07 €, apertura)
- 2026-09-30 00:30 [macd_sin_salida] ENTRADA SEI @ 0.06515 (22.41 €, apertura)
- 2026-09-30 00:30 [ruptura_volumen_tope] ENTRADA SEI @ 0.06515 (22.83 €, apertura)
- 2026-09-30 00:30 [macd_momentum_evento] ENTRADA SEI @ 0.06515 (22.38 €, apertura)
- 2026-09-30 00:30 [ruptura_volumen_evento] ENTRADA SEI @ 0.06515 (22.64 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
