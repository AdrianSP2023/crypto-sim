# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 00:11 UTC · vueltas 174 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.87 € (-2.64%) | 80 | 24 | 28% | -0.370% | -1.196% | -1.344% | -21.95 € |
| reversion_bb | 918.55 € (-0.62%) | 18 | 13 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 900.79 € (-2.54%) | 115 | 8 | 23% | -0.136% | -0.863% | -0.989% | -22.71 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.83 € (-2.10%) | 92 | 1 | 23% | -0.140% | -0.923% | -1.043% | -19.46 € |
| macd_momentum | 883.06 € (-4.46%) | 230 | 2 | 15% | -0.174% | -0.787% | -0.899% | -41.07 € |
| estocastico_rebote | 892.49 € (-3.44%) | 163 | 13 | 33% | -0.168% | -0.828% | -0.948% | -30.88 € |
| ruptura_estricta | 908.39 € (-1.72%) | 50 | 7 | 26% | -0.297% | -1.319% | -1.455% | -15.17 € |
| macd_sin_salida | 896.09 € (-3.05%) | 135 | 11 | 27% | -0.186% | -0.879% | -1.004% | -27.12 € |
| c_banda_atr_tope | 912.91 € (-1.23%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.95 € (-1.11%) | 38 | 5 | 16% | -0.032% | -1.132% | -1.250% | -9.90 € |
| c_banda_atr_regimen | 902.58 € (-2.34%) | 60 | 16 | 27% | -0.450% | -1.385% | -1.523% | -19.09 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 904.12 € (-2.18%) | 94 | 6 | 22% | -0.122% | -0.900% | -1.028% | -19.39 € |
| c_banda_atr_evento | 903.83 € (-2.21%) | 48 | 24 | 21% | -0.662% | -1.631% | -1.792% | -17.98 € |
| macd_momentum_evento | 895.48 € (-3.11%) | 110 | 2 | 8% | -0.400% | -1.140% | -1.248% | -28.65 € |
| ruptura_volumen_evento | 906.34 € (-1.94%) | 56 | 8 | 12% | -0.362% | -1.333% | -1.460% | -17.16 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 00:10 | c_banda_atr_evento | LTC | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 00:10 | c_banda_atr_regimen | LTC | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 00:10 | macd_sin_salida | SHIB | timeout | +0.02% | -0.48% | -0.11 |
| 2026-09-30 00:10 | pullback_tendencia | QNT | take-profit | +2.59% | +2.09% | +0.47 |
| 2026-09-30 00:10 | c_banda_atr | LTC | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 00:05 | ruptura_volumen_evento | PEPE | timeout | -0.48% | -0.98% | -0.22 |
| 2026-09-30 00:05 | macd_momentum_evento | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 00:05 | macd_sin_salida | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 00:05 | macd_sin_salida | LINK | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 00:05 | estocastico_rebote | ASTER | timeout | -0.14% | -0.64% | -0.14 |
| 2026-09-30 00:05 | macd_momentum | QNT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 00:05 | ruptura_volumen | PEPE | timeout | -0.48% | -0.98% | -0.22 |
| 2026-09-30 00:00 | macd_momentum_evento | XPL | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-09-30 00:00 | c_banda_atr_evento | XPL | stop-loss | -1.63% | -2.13% | -0.49 |
| 2026-09-30 00:00 | c_banda_atr_evento | NIGHT | stop-loss | -1.50% | -2.00% | -0.46 |

## Eventos de la última vuelta

- 2026-09-30 00:05 [ruptura_volumen] ENTRADA QNT @ 243.06 (22.54 €, apertura)
- 2026-09-30 00:10 [pullback_tendencia] CIERRE QNT take-profit bruto +2.59% neto +2.09%
- 2026-09-30 00:05 [ruptura_volumen_tope] ENTRADA QNT @ 243.06 (22.86 €, apertura)
- 2026-09-30 00:05 [ruptura_volumen_evento] ENTRADA QNT @ 243.06 (22.68 €, apertura)
- 2026-09-30 00:05 [estocastico_rebote] ENTRADA ZEC @ 1256.37 (22.33 €, apertura)
- 2026-09-30 00:10 [c_banda_atr] CIERRE LTC stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:10 [c_banda_atr_regimen] CIERRE LTC stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:10 [c_banda_atr_evento] CIERRE LTC stop-loss bruto -1.50% neto -2.30%
- 2026-09-30 00:05 [estocastico_rebote] ENTRADA PUMP @ 0.005212 (22.33 €, apertura)
- 2026-09-30 00:05 [ruptura_volumen] ENTRADA XDC @ 0.02947 (22.54 €, apertura)
- 2026-09-30 00:05 [ruptura_volumen_tope] ENTRADA XDC @ 0.02947 (22.86 €, apertura)
- 2026-09-30 00:05 [ruptura_volumen_evento] ENTRADA XDC @ 0.02947 (22.68 €, apertura)
- 2026-09-30 00:05 [c_banda_atr] ENTRADA SHIB @ 5.088e-06 (22.56 €, apertura)
- 2026-09-30 00:10 [macd_sin_salida] CIERRE SHIB timeout bruto +0.02% neto -0.48%
- 2026-09-30 00:05 [c_banda_atr_evento] ENTRADA SHIB @ 5.088e-06 (22.66 €, apertura)
- 2026-09-30 00:05 [macd_momentum] ENTRADA PENGU @ 0.00882 (22.08 €, apertura)
- 2026-09-30 00:05 [macd_momentum_evento] ENTRADA PENGU @ 0.00882 (22.39 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
