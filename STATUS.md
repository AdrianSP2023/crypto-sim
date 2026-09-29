# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 12:46 UTC · vueltas 38 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 925.24 € (+0.11%) | 8 | 25 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| reversion_bb | 923.52 € (-0.08%) | 1 | 1 | 0% | -1.500% | -2.600% | -2.784% | -0.60 € |
| ruptura_volumen | 918.91 € (-0.58%) | 33 | 20 | 36% | +0.440% | -0.660% | -0.793% | -5.03 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 921.59 € (-0.29%) | 22 | 11 | 41% | +0.429% | -0.671% | -0.770% | -3.41 € |
| macd_momentum | 910.98 € (-1.44%) | 81 | 13 | 17% | +0.036% | -0.786% | -0.906% | -14.67 € |
| estocastico_rebote | 925.68 € (+0.16%) | 24 | 27 | 79% | +1.179% | +0.079% | -0.061% | +0.44 € |
| ruptura_estricta | 923.54 € (-0.08%) | 10 | 21 | 50% | +0.567% | -0.533% | -0.705% | -1.23 € |
| macd_sin_salida | 920.42 € (-0.41%) | 36 | 20 | 50% | +0.611% | -0.448% | -0.577% | -3.72 € |
| c_banda_atr_tope | 924.65 € (+0.04%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 923.06 € (-0.13%) | 9 | 5 | 33% | +0.563% | -0.537% | -0.664% | -1.12 € |
| c_banda_atr_regimen | 925.24 € (+0.11%) | 8 | 25 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| macd_momentum_regimen | 910.98 € (-1.44%) | 81 | 13 | 17% | +0.036% | -0.786% | -0.906% | -14.67 € |
| ruptura_volumen_regimen | 918.91 € (-0.58%) | 33 | 20 | 36% | +0.440% | -0.660% | -0.793% | -5.03 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 12:45 | macd_momentum_regimen | WLD | momentum perdido | -0.94% | -1.44% | -0.33 |
| 2026-09-29 12:45 | macd_momentum_regimen | RENDER | momentum perdido | -0.23% | -0.73% | -0.17 |
| 2026-09-29 12:45 | macd_sin_salida | FET | timeout | +0.10% | -0.70% | -0.16 |
| 2026-09-29 12:45 | macd_sin_salida | SEI | timeout | +0.06% | -0.74% | -0.17 |
| 2026-09-29 12:45 | macd_sin_salida | PEPE | timeout | +1.24% | +0.44% | +0.10 |
| 2026-09-29 12:45 | macd_sin_salida | ATOM | timeout | -0.11% | -0.91% | -0.21 |
| 2026-09-29 12:45 | macd_sin_salida | DASH | timeout | -0.25% | -1.05% | -0.24 |
| 2026-09-29 12:45 | macd_sin_salida | ONDO | timeout | -1.30% | -2.40% | -0.55 |
| 2026-09-29 12:45 | ruptura_estricta | FIL | timeout | +0.00% | -1.10% | -0.25 |
| 2026-09-29 12:45 | ruptura_estricta | MON | timeout | +1.26% | +0.16% | +0.04 |
| 2026-09-29 12:45 | estocastico_rebote | PEPE | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-29 12:45 | estocastico_rebote | MON | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-29 12:45 | macd_momentum | WLD | momentum perdido | -0.94% | -1.44% | -0.33 |
| 2026-09-29 12:45 | macd_momentum | RENDER | momentum perdido | -0.23% | -0.73% | -0.17 |
| 2026-09-29 12:45 | pullback_tendencia | TRX | rotura de tendencia | -0.04% | -1.14% | -0.26 |

## Eventos de la última vuelta

- 2026-09-29 12:40 [c_banda_atr] ENTRADA BTC @ 74359.3 (23.13 €, apertura)
- 2026-09-29 12:40 [macd_momentum] ENTRADA BTC @ 74359.3 (22.75 €, apertura)
- 2026-09-29 12:40 [c_banda_atr_regimen] ENTRADA BTC @ 74359.3 (23.13 €, apertura)
- 2026-09-29 12:40 [macd_momentum_regimen] ENTRADA BTC @ 74359.3 (22.75 €, apertura)
- 2026-09-29 12:40 [pullback_tendencia] ENTRADA LINK @ 13.5571 (23.04 €, apertura)
- 2026-09-29 12:45 [pullback_tendencia] CIERRE LINK rotura de tendencia bruto -0.64% neto -1.74%
- 2026-09-29 12:40 [macd_momentum] ENTRADA LINK @ 13.5571 (22.75 €, apertura)
- 2026-09-29 12:40 [macd_sin_salida] ENTRADA LINK @ 13.5571 (23.04 €, apertura)
- 2026-09-29 12:40 [macd_momentum_regimen] ENTRADA LINK @ 13.5571 (22.75 €, apertura)
- 2026-09-29 12:40 [reversion_bb] ENTRADA HBAR @ 0.10177 (23.09 €, apertura)
- 2026-09-29 12:40 [pullback_tendencia] ENTRADA NEAR @ 4.2811 (23.03 €, apertura)
- 2026-09-29 12:45 [pullback_tendencia] CIERRE LTC rotura de tendencia bruto +0.03% neto -1.07%
- 2026-09-29 12:40 [pullback_tendencia] ENTRADA AVAX @ 10.387 (23.03 €, apertura)
- 2026-09-29 12:45 [macd_sin_salida] CIERRE ONDO timeout bruto -1.30% neto -2.40%
- 2026-09-29 12:40 [ruptura_volumen] ENTRADA DOGE @ 0.0847361 (22.98 €, apertura)
- 2026-09-29 12:40 [ruptura_volumen_regimen] ENTRADA DOGE @ 0.0847361 (22.98 €, apertura)
- 2026-09-29 12:45 [macd_sin_salida] CIERRE DASH timeout bruto -0.25% neto -1.05%
- 2026-09-29 12:45 [estocastico_rebote] CIERRE MON take-profit bruto +1.80% neto +0.70%
- 2026-09-29 12:45 [ruptura_estricta] CIERRE MON timeout bruto +1.26% neto +0.16%
- 2026-09-29 12:40 [pullback_tendencia] ENTRADA TRX @ 0.295674 (23.03 €, apertura)
- 2026-09-29 12:45 [pullback_tendencia] CIERRE TRX rotura de tendencia bruto -0.04% neto -1.14%
- 2026-09-29 12:45 [macd_sin_salida] CIERRE ATOM timeout bruto -0.11% neto -0.91%
- 2026-09-29 12:45 [macd_momentum] CIERRE RENDER momentum perdido bruto -0.23% neto -0.73%
- 2026-09-29 12:45 [macd_momentum_regimen] CIERRE RENDER momentum perdido bruto -0.23% neto -0.73%
- 2026-09-29 12:45 [macd_momentum] CIERRE WLD momentum perdido bruto -0.94% neto -1.44%
- 2026-09-29 12:45 [macd_momentum_regimen] CIERRE WLD momentum perdido bruto -0.94% neto -1.44%
- 2026-09-29 12:45 [estocastico_rebote] CIERRE PEPE take-profit bruto +1.80% neto +0.70%
- 2026-09-29 12:45 [macd_sin_salida] CIERRE PEPE timeout bruto +1.24% neto +0.44%
- 2026-09-29 12:45 [macd_sin_salida] CIERRE SEI timeout bruto +0.06% neto -0.74%
- 2026-09-29 12:45 [ruptura_estricta] CIERRE FIL timeout bruto +0.00% neto -1.10%
- 2026-09-29 12:40 [macd_momentum] ENTRADA BNB @ 674.97 (22.74 €, apertura)
- 2026-09-29 12:40 [macd_momentum_regimen] ENTRADA BNB @ 674.97 (22.74 €, apertura)
- 2026-09-29 12:40 [pullback_tendencia] ENTRADA GRT @ 0.0271 (23.02 €, apertura)
- 2026-09-29 12:45 [macd_sin_salida] CIERRE FET timeout bruto +0.10% neto -0.70%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
