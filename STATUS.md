# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 07:16 UTC · vueltas 157 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.00 € (-1.76%) | 143 | 24 | 41% | +0.176% | -0.506% | -0.625% | -16.69 € |
| reversion_bb | 921.50 € (-0.30%) | 17 | 2 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 889.88 € (-3.72%) | 193 | 11 | 24% | -0.147% | -0.783% | -0.892% | -34.43 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 901.74 € (-2.43%) | 103 | 14 | 17% | -0.210% | -0.967% | -1.077% | -22.78 € |
| macd_momentum | 891.01 € (-3.60%) | 273 | 15 | 23% | +0.058% | -0.537% | -0.643% | -33.36 € |
| estocastico_rebote | 903.13 € (-2.28%) | 177 | 32 | 40% | +0.131% | -0.517% | -0.637% | -21.05 € |
| ruptura_estricta | 900.36 € (-2.58%) | 102 | 19 | 30% | -0.285% | -1.044% | -1.171% | -24.51 € |
| macd_sin_salida | 902.69 € (-2.33%) | 180 | 34 | 43% | +0.141% | -0.504% | -0.615% | -20.87 € |
| c_banda_atr_tope | 917.19 € (-0.76%) | 30 | 5 | 30% | +0.135% | -0.965% | -1.091% | -6.68 € |
| ruptura_volumen_tope | 914.77 € (-1.02%) | 52 | 5 | 31% | +0.206% | -0.802% | -0.909% | -9.60 € |
| c_banda_atr_regimen | 912.20 € (-1.30%) | 86 | 23 | 43% | +0.193% | -0.610% | -0.749% | -12.14 € |
| macd_momentum_regimen | 900.04 € (-2.62%) | 187 | 15 | 24% | +0.071% | -0.569% | -0.677% | -24.32 € |
| ruptura_volumen_regimen | 890.73 € (-3.63%) | 166 | 11 | 22% | -0.230% | -0.887% | -1.000% | -33.57 € |
| c_banda_atr_evento | 914.04 € (-1.10%) | 110 | 24 | 44% | +0.322% | -0.418% | -0.524% | -10.65 € |
| macd_momentum_evento | 895.94 € (-3.06%) | 226 | 15 | 20% | +0.065% | -0.552% | -0.651% | -28.43 € |
| ruptura_volumen_evento | 902.54 € (-2.35%) | 143 | 11 | 26% | +0.020% | -0.664% | -0.760% | -21.75 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 07:15 | ruptura_volumen_evento | BNB | timeout | +0.20% | -0.30% | -0.07 |
| 2026-10-01 07:15 | macd_momentum_evento | ASTER | momentum perdido | +0.33% | -0.17% | -0.04 |
| 2026-10-01 07:15 | macd_momentum_evento | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 07:15 | c_banda_atr_evento | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 07:15 | c_banda_atr_evento | ZRO | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 07:15 | c_banda_atr_evento | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 07:15 | ruptura_volumen_regimen | BNB | timeout | +0.20% | -0.30% | -0.07 |
| 2026-10-01 07:15 | macd_momentum_regimen | ASTER | momentum perdido | +0.33% | -0.17% | -0.04 |
| 2026-10-01 07:15 | macd_momentum_regimen | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 07:15 | c_banda_atr_regimen | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 07:15 | c_banda_atr_regimen | ZRO | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 07:15 | c_banda_atr_regimen | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 07:15 | macd_sin_salida | XMR | timeout | +0.19% | -0.31% | -0.07 |
| 2026-10-01 07:15 | macd_sin_salida | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 07:15 | ruptura_estricta | XMR | timeout | +0.19% | -0.31% | -0.07 |

## Eventos de la última vuelta

- 2026-10-01 07:15 [c_banda_atr] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-10-01 07:15 [c_banda_atr_regimen] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-10-01 07:15 [c_banda_atr_evento] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-10-01 07:15 [ruptura_estricta] CIERRE PUMP stop-loss bruto -2.50% neto -3.00%
- 2026-10-01 07:15 [c_banda_atr] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:10 [pullback_tendencia] ENTRADA ZRO @ 1.516 (22.55 €, apertura)
- 2026-10-01 07:15 [pullback_tendencia] CIERRE ZRO rotura de tendencia bruto -0.73% neto -1.23%
- 2026-10-01 07:15 [macd_momentum] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:15 [macd_sin_salida] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:15 [c_banda_atr_regimen] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:15 [macd_momentum_regimen] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:15 [c_banda_atr_evento] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:15 [macd_momentum_evento] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:10 [macd_momentum] ENTRADA DOGE @ 0.0844631 (22.27 €, apertura)
- 2026-10-01 07:10 [macd_sin_salida] ENTRADA DOGE @ 0.0844631 (22.59 €, apertura)
- 2026-10-01 07:10 [macd_momentum_regimen] ENTRADA DOGE @ 0.0844631 (22.50 €, apertura)
- 2026-10-01 07:10 [macd_momentum_evento] ENTRADA DOGE @ 0.0844631 (22.40 €, apertura)
- 2026-10-01 07:10 [ruptura_estricta] ENTRADA DOT @ 1.1109 (22.49 €, apertura)
- 2026-10-01 07:10 [ruptura_volumen] ENTRADA FET @ 0.2162 (22.25 €, apertura)
- 2026-10-01 07:10 [ruptura_volumen_tope] ENTRADA FET @ 0.2162 (22.87 €, apertura)
- 2026-10-01 07:10 [ruptura_volumen_regimen] ENTRADA FET @ 0.2162 (22.27 €, apertura)
- 2026-10-01 07:10 [ruptura_volumen_evento] ENTRADA FET @ 0.2162 (22.56 €, apertura)
- 2026-10-01 07:15 [pullback_tendencia] CIERRE POL rotura de tendencia bruto -0.56% neto -1.06%
- 2026-10-01 07:15 [c_banda_atr] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-10-01 07:15 [c_banda_atr_regimen] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-10-01 07:15 [c_banda_atr_evento] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-10-01 07:15 [macd_momentum] CIERRE ASTER momentum perdido bruto +0.33% neto -0.17%
- 2026-10-01 07:15 [macd_momentum_regimen] CIERRE ASTER momentum perdido bruto +0.33% neto -0.17%
- 2026-10-01 07:15 [macd_momentum_evento] CIERRE ASTER momentum perdido bruto +0.33% neto -0.17%
- 2026-10-01 07:15 [ruptura_volumen] CIERRE BNB timeout bruto +0.20% neto -0.30%
- 2026-10-01 07:15 [ruptura_volumen_regimen] CIERRE BNB timeout bruto +0.20% neto -0.30%
- 2026-10-01 07:15 [ruptura_volumen_evento] CIERRE BNB timeout bruto +0.20% neto -0.30%
- 2026-10-01 07:15 [ruptura_estricta] CIERRE XMR timeout bruto +0.19% neto -0.31%
- 2026-10-01 07:15 [macd_sin_salida] CIERRE XMR timeout bruto +0.19% neto -0.31%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
