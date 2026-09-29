# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 08:56 UTC · vueltas 203 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 858.61 € (-7.10%) | 176 | 17 | 31% | -0.360% | -1.460% | -1.591% | -65.70 € |
| reversion_bb | 918.89 € (-0.58%) | 42 | 0 | 62% | +0.511% | -0.589% | -0.760% | -5.35 € |
| ruptura_volumen | 868.76 € (-6.00%) | 178 | 22 | 26% | -0.051% | -1.151% | -1.273% | -55.98 € |
| rebote_extremo | 917.94 € (-0.68%) | 27 | 0 | 41% | +0.285% | -0.815% | -1.082% | -6.30 € |
| pullback_tendencia | 901.95 € (-2.41%) | 70 | 14 | 23% | -0.191% | -1.291% | -1.388% | -22.17 € |
| macd_momentum | 874.82 € (-5.35%) | 211 | 6 | 25% | +0.064% | -1.036% | -1.153% | -50.47 € |
| estocastico_rebote | 884.70 € (-4.28%) | 112 | 9 | 26% | -0.395% | -1.495% | -1.595% | -39.20 € |
| c_banda_atr_filtro | 891.98 € (-3.49%) | 94 | 17 | 31% | -0.399% | -1.499% | -1.626% | -32.33 € |
| ruptura_volumen_filtro | 894.46 € (-3.22%) | 123 | 22 | 29% | +0.022% | -1.078% | -1.198% | -30.30 € |
| macd_momentum_filtro | 895.26 € (-3.14%) | 135 | 6 | 25% | +0.123% | -0.977% | -1.091% | -30.05 € |
| pullback_tendencia_filtro | 913.39 € (-1.17%) | 34 | 14 | 18% | -0.271% | -1.371% | -1.442% | -10.72 € |
| estocastico_rebote_filtro | 914.18 € (-1.09%) | 25 | 9 | 20% | -0.587% | -1.687% | -1.798% | -9.71 € |
| ruptura_estricta | 917.32 € (-0.75%) | 42 | 31 | 43% | +0.165% | -0.935% | -1.100% | -9.08 € |
| macd_sin_salida | 911.13 € (-1.42%) | 94 | 17 | 53% | +0.444% | -0.656% | -0.785% | -14.23 € |
| c_banda_atr_tope | 922.46 € (-0.19%) | 17 | 5 | 59% | +0.570% | -0.530% | -0.716% | -2.08 € |
| ruptura_volumen_tope | 923.05 € (-0.13%) | 15 | 5 | 40% | +0.789% | -0.311% | -0.463% | -1.08 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 08:55 | ruptura_estricta | ETH | timeout | +1.28% | +0.18% | +0.04 |
| 2026-09-29 08:55 | pullback_tendencia_filtro | LTC | rotura de tendencia | -0.43% | -1.53% | -0.35 |
| 2026-09-29 08:55 | pullback_tendencia_filtro | XRP | rotura de tendencia | -0.40% | -1.50% | -0.34 |
| 2026-09-29 08:55 | ruptura_volumen_filtro | LTC | timeout | -0.20% | -1.30% | -0.29 |
| 2026-09-29 08:55 | pullback_tendencia | LTC | rotura de tendencia | -0.43% | -1.53% | -0.34 |
| 2026-09-29 08:55 | pullback_tendencia | XRP | rotura de tendencia | -0.40% | -1.50% | -0.34 |
| 2026-09-29 08:55 | ruptura_volumen | LTC | timeout | -0.20% | -1.30% | -0.28 |
| 2026-09-29 08:50 | macd_sin_salida | PUMP | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 08:50 | macd_sin_salida | BTC | timeout | +0.70% | -0.40% | -0.09 |
| 2026-09-29 08:50 | ruptura_estricta | BTC | timeout | +0.70% | -0.40% | -0.09 |
| 2026-09-29 08:50 | macd_momentum_filtro | FET | momentum perdido | -0.44% | -1.54% | -0.35 |
| 2026-09-29 08:50 | macd_momentum_filtro | NEAR | momentum perdido | -0.19% | -1.29% | -0.29 |
| 2026-09-29 08:50 | ruptura_volumen_filtro | XPL | stop-loss | -1.23% | -2.33% | -0.52 |
| 2026-09-29 08:50 | macd_momentum | FET | momentum perdido | -0.44% | -1.54% | -0.34 |
| 2026-09-29 08:50 | macd_momentum | NEAR | momentum perdido | -0.19% | -1.29% | -0.28 |

## Eventos de la última vuelta

- 2026-09-29 08:55 [ruptura_estricta] CIERRE ETH timeout bruto +1.28% neto +0.18%
- 2026-09-29 08:55 [pullback_tendencia] CIERRE XRP rotura de tendencia bruto -0.40% neto -1.50%
- 2026-09-29 08:55 [pullback_tendencia_filtro] CIERRE XRP rotura de tendencia bruto -0.40% neto -1.50%
- 2026-09-29 08:55 [ruptura_volumen] CIERRE LTC timeout bruto -0.20% neto -1.30%
- 2026-09-29 08:55 [pullback_tendencia] CIERRE LTC rotura de tendencia bruto -0.43% neto -1.53%
- 2026-09-29 08:55 [ruptura_volumen_filtro] CIERRE LTC timeout bruto -0.20% neto -1.30%
- 2026-09-29 08:55 [pullback_tendencia_filtro] CIERRE LTC rotura de tendencia bruto -0.43% neto -1.53%
- 2026-09-29 08:55 [estocastico_rebote] ENTRADA BCH @ 274.07 (22.13 €)
- 2026-09-29 08:55 [estocastico_rebote_filtro] ENTRADA BCH @ 274.07 (22.86 €)
- 2026-09-29 08:55 [estocastico_rebote] ENTRADA MON @ 0.02487 (22.13 €)
- 2026-09-29 08:55 [estocastico_rebote_filtro] ENTRADA MON @ 0.02487 (22.86 €)
- 2026-09-29 08:55 [estocastico_rebote] ENTRADA VVV @ 24.686 (22.13 €)
- 2026-09-29 08:55 [estocastico_rebote_filtro] ENTRADA VVV @ 24.686 (22.86 €)
- 2026-09-29 08:55 [c_banda_atr] ENTRADA KAS @ 0.04138 (21.46 €)
- 2026-09-29 08:55 [c_banda_atr_filtro] ENTRADA KAS @ 0.04138 (22.30 €)
- 2026-09-29 08:55 [macd_momentum] ENTRADA WLFI @ 0.0505 (21.84 €)
- 2026-09-29 08:55 [macd_momentum_filtro] ENTRADA WLFI @ 0.0505 (22.36 €)
- 2026-09-29 08:55 [macd_sin_salida] ENTRADA WLFI @ 0.0505 (22.75 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
