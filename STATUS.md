# Simulación P1 (sin dinero real)

Config `P1-v9` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 00:26 UTC · vueltas 189 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 871.05 € (-5.76%) | 109 | 23 | 18% | -0.772% | -1.872% | -1.993% | -54.16 € |
| reversion_bb | 924.00 € (-0.03%) | 28 | 4 | 79% | +0.978% | -0.122% | -0.302% | -0.42 € |
| ruptura_volumen | 883.56 € (-4.40%) | 89 | 20 | 15% | -0.444% | -1.544% | -1.665% | -41.13 € |
| rebote_extremo | 922.00 € (-0.24%) | 10 | 0 | 50% | +0.661% | -0.439% | -0.790% | -2.24 € |
| pullback_tendencia | 904.76 € (-2.11%) | 55 | 1 | 18% | -0.333% | -1.433% | -1.530% | -19.56 € |
| macd_momentum | 892.25 € (-3.46%) | 105 | 8 | 16% | -0.227% | -1.327% | -1.437% | -32.94 € |
| estocastico_rebote | 896.40 € (-3.01%) | 81 | 4 | 28% | -0.355% | -1.455% | -1.552% | -28.12 € |
| c_banda_atr_filtro | 895.91 € (-3.07%) | 51 | 6 | 6% | -1.292% | -2.392% | -2.513% | -28.06 € |
| ruptura_volumen_filtro | 908.60 € (-1.69%) | 38 | 22 | 8% | -0.726% | -1.826% | -1.946% | -15.94 € |
| macd_momentum_filtro | 910.46 € (-1.49%) | 42 | 4 | 12% | -0.356% | -1.456% | -1.560% | -14.07 € |
| pullback_tendencia_filtro | 916.26 € (-0.86%) | 23 | 1 | 13% | -0.421% | -1.521% | -1.584% | -8.06 € |
| estocastico_rebote_filtro | 918.83 € (-0.58%) | 15 | 2 | 20% | -0.415% | -1.515% | -1.614% | -5.24 € |
| ruptura_estricta | 920.32 € (-0.42%) | 7 | 8 | 14% | -1.333% | -2.433% | -2.561% | -3.93 € |
| macd_sin_salida | 916.34 € (-0.85%) | 26 | 11 | 27% | -0.387% | -1.487% | -1.595% | -8.94 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 00:25 | pullback_tendencia_filtro | ETH | rotura de tendencia | -0.25% | -1.35% | -0.31 |
| 2026-09-29 00:25 | ruptura_volumen_filtro | XLM | stop-loss | -1.20% | -2.30% | -0.52 |
| 2026-09-29 00:25 | macd_momentum | VVV | momentum perdido | +0.03% | -1.07% | -0.24 |
| 2026-09-29 00:25 | macd_momentum | DASH | momentum perdido | +0.90% | -0.20% | -0.04 |
| 2026-09-29 00:25 | macd_momentum | ETH | momentum perdido | +0.04% | -1.06% | -0.24 |
| 2026-09-29 00:25 | pullback_tendencia | ETH | rotura de tendencia | -0.25% | -1.35% | -0.31 |
| 2026-09-29 00:25 | ruptura_volumen | XLM | stop-loss | -1.20% | -2.30% | -0.51 |
| 2026-09-29 00:20 | pullback_tendencia_filtro | BTC | rotura de tendencia | -0.10% | -1.20% | -0.27 |
| 2026-09-29 00:20 | macd_momentum | VIRTUAL | momentum perdido | +1.64% | +0.54% | +0.12 |
| 2026-09-29 00:20 | pullback_tendencia | BTC | rotura de tendencia | -0.10% | -1.20% | -0.27 |
| 2026-09-29 00:15 | estocastico_rebote | HBAR | stop-loss | -1.50% | -2.60% | -0.58 |
| 2026-09-29 00:15 | macd_momentum | LTC | momentum perdido | +0.05% | -1.05% | -0.23 |
| 2026-09-29 00:15 | ruptura_volumen | ICP | take-profit | +2.78% | +1.68% | +0.37 |
| 2026-09-29 00:10 | macd_sin_salida | W | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 00:10 | estocastico_rebote_filtro | TRX | timeout | -0.12% | -1.22% | -0.28 |

## Eventos de la última vuelta

- 2026-09-29 00:25 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto -0.25% neto -1.35%
- 2026-09-29 00:25 [macd_momentum] CIERRE ETH momentum perdido bruto +0.04% neto -1.06%
- 2026-09-29 00:25 [pullback_tendencia_filtro] CIERRE ETH rotura de tendencia bruto -0.25% neto -1.35%
- 2026-09-29 00:25 [ruptura_volumen] CIERRE XLM stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 00:25 [ruptura_volumen_filtro] CIERRE XLM stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 00:25 [macd_momentum] CIERRE DASH momentum perdido bruto +0.90% neto -0.20%
- 2026-09-29 00:25 [c_banda_atr] ENTRADA TRX @ 0.295164 (21.75 €)
- 2026-09-29 00:25 [c_banda_atr_filtro] ENTRADA TRX @ 0.295164 (22.40 €)
- 2026-09-29 00:25 [macd_momentum] CIERRE VVV momentum perdido bruto +0.03% neto -1.07%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
