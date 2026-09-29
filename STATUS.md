# Simulación P1 (sin dinero real)

Config `P1-v9` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 01:06 UTC · vueltas 169 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 868.05 € (-6.08%) | 116 | 21 | 20% | -0.701% | -1.801% | -1.922% | -55.21 € |
| reversion_bb | 923.88 € (-0.04%) | 28 | 5 | 79% | +0.978% | -0.122% | -0.304% | -0.42 € |
| ruptura_volumen | 879.82 € (-4.81%) | 97 | 18 | 14% | -0.448% | -1.548% | -1.663% | -43.93 € |
| rebote_extremo | 922.00 € (-0.24%) | 10 | 0 | 50% | +0.661% | -0.439% | -0.795% | -2.24 € |
| pullback_tendencia | 903.70 € (-2.22%) | 58 | 2 | 17% | -0.344% | -1.444% | -1.536% | -20.68 € |
| macd_momentum | 887.55 € (-3.97%) | 119 | 2 | 15% | -0.220% | -1.320% | -1.429% | -36.91 € |
| estocastico_rebote | 895.18 € (-3.14%) | 82 | 10 | 28% | -0.351% | -1.451% | -1.547% | -28.37 € |
| c_banda_atr_filtro | 894.20 € (-3.25%) | 53 | 11 | 6% | -1.286% | -2.386% | -2.503% | -29.06 € |
| ruptura_volumen_filtro | 904.70 € (-2.11%) | 46 | 20 | 9% | -0.703% | -1.803% | -1.917% | -19.02 € |
| macd_momentum_filtro | 906.47 € (-1.92%) | 53 | 1 | 9% | -0.378% | -1.478% | -1.580% | -17.98 € |
| pullback_tendencia_filtro | 915.16 € (-0.98%) | 26 | 1 | 12% | -0.436% | -1.536% | -1.593% | -9.20 € |
| estocastico_rebote_filtro | 918.11 € (-0.66%) | 15 | 6 | 20% | -0.415% | -1.515% | -1.614% | -5.24 € |
| ruptura_estricta | 919.30 € (-0.53%) | 8 | 11 | 12% | -1.418% | -2.518% | -2.637% | -4.65 € |
| macd_sin_salida | 915.38 € (-0.96%) | 26 | 17 | 27% | -0.387% | -1.487% | -1.595% | -8.94 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 01:05 | macd_momentum_filtro | KAS | momentum perdido | -0.15% | -1.25% | -0.28 |
| 2026-09-29 01:05 | macd_momentum_filtro | PEPE | momentum perdido | -0.97% | -2.07% | -0.47 |
| 2026-09-29 01:05 | ruptura_volumen_filtro | W | stop-loss | -1.31% | -2.41% | -0.55 |
| 2026-09-29 01:05 | ruptura_volumen_filtro | LINK | stop-loss | -1.23% | -2.33% | -0.53 |
| 2026-09-29 01:05 | c_banda_atr_filtro | LTC | timeout | -0.77% | -1.87% | -0.42 |
| 2026-09-29 01:05 | estocastico_rebote | BTC | timeout | +0.01% | -1.09% | -0.25 |
| 2026-09-29 01:05 | macd_momentum | KAS | momentum perdido | -0.15% | -1.25% | -0.28 |
| 2026-09-29 01:05 | macd_momentum | PEPE | momentum perdido | -0.97% | -2.07% | -0.46 |
| 2026-09-29 01:05 | ruptura_volumen | W | stop-loss | -1.31% | -2.41% | -0.53 |
| 2026-09-29 01:05 | ruptura_volumen | LINK | stop-loss | -1.23% | -2.33% | -0.52 |
| 2026-09-29 01:05 | c_banda_atr | LTC | timeout | -0.77% | -1.87% | -0.41 |
| 2026-09-29 01:00 | pullback_tendencia_filtro | XLM | rotura de tendencia | -1.08% | -2.18% | -0.50 |
| 2026-09-29 01:00 | macd_momentum_filtro | EIGEN | momentum perdido | -0.67% | -1.77% | -0.40 |
| 2026-09-29 01:00 | macd_momentum_filtro | ARB | momentum perdido | -1.18% | -2.28% | -0.52 |
| 2026-09-29 01:00 | ruptura_volumen_filtro | VVV | timeout | -0.30% | -1.41% | -0.32 |

## Eventos de la última vuelta

- 2026-09-29 01:05 [estocastico_rebote] CIERRE BTC timeout bruto +0.01% neto -1.09%
- 2026-09-29 01:05 [ruptura_volumen] CIERRE LINK stop-loss bruto -1.23% neto -2.33%
- 2026-09-29 01:05 [ruptura_volumen_filtro] CIERRE LINK stop-loss bruto -1.23% neto -2.33%
- 2026-09-29 01:05 [c_banda_atr] CIERRE LTC timeout bruto -0.77% neto -1.87%
- 2026-09-29 01:05 [c_banda_atr_filtro] CIERRE LTC timeout bruto -0.77% neto -1.87%
- 2026-09-29 01:05 [estocastico_rebote] ENTRADA AAVE @ 131.43 (22.40 €)
- 2026-09-29 01:05 [macd_momentum] CIERRE PEPE momentum perdido bruto -0.97% neto -2.07%
- 2026-09-29 01:05 [macd_momentum_filtro] CIERRE PEPE momentum perdido bruto -0.97% neto -2.07%
- 2026-09-29 01:05 [ruptura_volumen] CIERRE W stop-loss bruto -1.31% neto -2.41%
- 2026-09-29 01:05 [ruptura_volumen_filtro] CIERRE W stop-loss bruto -1.31% neto -2.41%
- 2026-09-29 01:05 [estocastico_rebote] ENTRADA CRV @ 0.3303 (22.40 €)
- 2026-09-29 01:05 [macd_momentum] CIERRE KAS momentum perdido bruto -0.15% neto -1.25%
- 2026-09-29 01:05 [macd_momentum_filtro] CIERRE KAS momentum perdido bruto -0.15% neto -1.25%
- 2026-09-29 01:05 [macd_momentum] ENTRADA CC @ 0.11676 (22.18 €)
- 2026-09-29 01:05 [ruptura_estricta] ENTRADA CC @ 0.11676 (22.99 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
