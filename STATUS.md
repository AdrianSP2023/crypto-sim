# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 18:32 UTC · vueltas 106 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.96 € (-1.55%) | 55 | 7 | 33% | -0.213% | -1.188% | -1.326% | -15.06 € |
| reversion_bb | 918.79 € (-0.59%) | 13 | 5 | 23% | -0.806% | -1.906% | -2.012% | -5.72 € |
| ruptura_volumen | 909.54 € (-1.59%) | 70 | 7 | 27% | -0.044% | -0.917% | -1.054% | -14.76 € |
| rebote_extremo | 922.67 € (-0.17%) | 5 | 2 | 40% | -0.324% | -1.424% | -1.593% | -1.64 € |
| pullback_tendencia | 907.83 € (-1.78%) | 70 | 1 | 24% | -0.161% | -1.034% | -1.149% | -16.61 € |
| macd_momentum | 897.75 € (-2.87%) | 152 | 3 | 19% | -0.104% | -0.775% | -0.894% | -26.94 € |
| estocastico_rebote | 895.15 € (-3.15%) | 129 | 20 | 29% | -0.331% | -1.033% | -1.153% | -30.48 € |
| ruptura_estricta | 911.41 € (-1.39%) | 42 | 0 | 29% | -0.226% | -1.326% | -1.452% | -12.83 € |
| macd_sin_salida | 904.52 € (-2.13%) | 97 | 4 | 30% | -0.145% | -0.914% | -1.041% | -20.33 € |
| c_banda_atr_tope | 916.10 € (-0.88%) | 22 | 5 | 23% | -0.661% | -1.761% | -1.924% | -8.93 € |
| ruptura_volumen_tope | 919.12 € (-0.55%) | 21 | 5 | 19% | +0.041% | -1.059% | -1.189% | -5.13 € |
| c_banda_atr_regimen | 909.84 € (-1.56%) | 50 | 0 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| c_banda_atr_evento | 915.97 € (-0.90%) | 23 | 7 | 26% | -0.607% | -1.707% | -1.858% | -9.06 € |
| macd_momentum_evento | 912.02 € (-1.32%) | 32 | 3 | 12% | -0.618% | -1.718% | -1.847% | -12.68 € |
| ruptura_volumen_evento | 919.71 € (-0.49%) | 11 | 7 | 18% | -0.704% | -1.804% | -2.004% | -4.58 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 18:30 | estocastico_rebote | PENGU | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-29 18:30 | estocastico_rebote | DOGE | timeout | +0.40% | -0.10% | -0.02 |
| 2026-09-29 18:30 | estocastico_rebote | SUI | timeout | +0.30% | -0.20% | -0.05 |
| 2026-09-29 18:30 | estocastico_rebote | ZEC | timeout | +1.06% | +0.56% | +0.13 |
| 2026-09-29 18:30 | estocastico_rebote | ETH | timeout | +0.26% | -0.24% | -0.05 |
| 2026-09-29 18:30 | pullback_tendencia | NIGHT | rotura de tendencia | -1.09% | -1.59% | -0.36 |
| 2026-09-29 18:25 | estocastico_rebote | UNI | timeout | +1.29% | +0.79% | +0.18 |
| 2026-09-29 18:25 | estocastico_rebote | NEAR | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-29 18:20 | reversion_bb | VVV | take-profit | +1.83% | +0.73% | +0.17 |
| 2026-09-29 18:05 | estocastico_rebote | USELESS | take-profit | +2.21% | +1.71% | +0.38 |
| 2026-09-29 18:05 | rebote_extremo | ZEC | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 17:55 | c_banda_atr_evento | BNB | stop-loss | -1.51% | -2.61% | -0.60 |
| 2026-09-29 17:55 | c_banda_atr_evento | HYPE | stop-loss | -1.55% | -2.65% | -0.61 |
| 2026-09-29 17:55 | c_banda_atr_tope | HYPE | stop-loss | -1.55% | -2.65% | -0.61 |
| 2026-09-29 17:55 | estocastico_rebote | OP | stop-loss | -1.81% | -2.31% | -0.52 |

## Eventos de la última vuelta

- 2026-09-29 18:30 [estocastico_rebote] CIERRE ETH timeout bruto +0.26% neto -0.24%
- 2026-09-29 18:30 [estocastico_rebote] CIERRE ZEC timeout bruto +1.06% neto +0.56%
- 2026-09-29 18:25 [ruptura_volumen] ENTRADA NEAR @ 4.4024 (22.74 €, apertura)
- 2026-09-29 18:25 [macd_momentum] ENTRADA NEAR @ 4.4024 (22.43 €, apertura)
- 2026-09-29 18:25 [macd_sin_salida] ENTRADA NEAR @ 4.4024 (22.60 €, apertura)
- 2026-09-29 18:25 [ruptura_volumen_tope] ENTRADA NEAR @ 4.4024 (22.98 €, apertura)
- 2026-09-29 18:25 [macd_momentum_evento] ENTRADA NEAR @ 4.4024 (22.79 €, apertura)
- 2026-09-29 18:25 [ruptura_volumen_evento] ENTRADA NEAR @ 4.4024 (22.99 €, apertura)
- 2026-09-29 18:30 [estocastico_rebote] CIERRE SUI timeout bruto +0.30% neto -0.20%
- 2026-09-29 18:30 [estocastico_rebote] CIERRE DOGE timeout bruto +0.40% neto -0.10%
- 2026-09-29 18:25 [ruptura_volumen] ENTRADA DASH @ 54.024 (22.74 €, apertura)
- 2026-09-29 18:25 [ruptura_volumen_evento] ENTRADA DASH @ 54.024 (22.99 €, apertura)
- 2026-09-29 18:25 [c_banda_atr] ENTRADA WLD @ 0.4337 (22.73 €, apertura)
- 2026-09-29 18:25 [c_banda_atr_evento] ENTRADA WLD @ 0.4337 (22.88 €, apertura)
- 2026-09-29 18:25 [ruptura_volumen] ENTRADA SEI @ 0.0645 (22.74 €, apertura)
- 2026-09-29 18:25 [ruptura_volumen_evento] ENTRADA SEI @ 0.0645 (22.99 €, apertura)
- 2026-09-29 18:30 [pullback_tendencia] CIERRE NIGHT rotura de tendencia bruto -1.09% neto -1.59%
- 2026-09-29 18:30 [estocastico_rebote] CIERRE PENGU take-profit bruto +1.80% neto +1.30%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
