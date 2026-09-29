# Simulación P1 (sin dinero real)

Config `P1-v9` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 01:01 UTC · vueltas 168 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 867.94 € (-6.09%) | 115 | 22 | 20% | -0.700% | -1.800% | -1.922% | -54.80 € |
| reversion_bb | 923.80 € (-0.05%) | 28 | 5 | 79% | +0.978% | -0.122% | -0.304% | -0.42 € |
| ruptura_volumen | 879.84 € (-4.80%) | 95 | 20 | 15% | -0.430% | -1.530% | -1.646% | -42.88 € |
| rebote_extremo | 922.00 € (-0.24%) | 10 | 0 | 50% | +0.661% | -0.439% | -0.795% | -2.24 € |
| pullback_tendencia | 903.66 € (-2.23%) | 58 | 2 | 17% | -0.344% | -1.444% | -1.536% | -20.68 € |
| macd_momentum | 888.04 € (-3.92%) | 117 | 3 | 15% | -0.214% | -1.314% | -1.422% | -36.17 € |
| estocastico_rebote | 895.35 € (-3.13%) | 81 | 9 | 28% | -0.355% | -1.455% | -1.552% | -28.12 € |
| c_banda_atr_filtro | 894.15 € (-3.26%) | 52 | 12 | 6% | -1.296% | -2.396% | -2.515% | -28.64 € |
| ruptura_volumen_filtro | 904.49 € (-2.14%) | 44 | 22 | 9% | -0.677% | -1.777% | -1.891% | -17.94 € |
| macd_momentum_filtro | 906.98 € (-1.87%) | 51 | 3 | 10% | -0.370% | -1.470% | -1.572% | -17.22 € |
| pullback_tendencia_filtro | 915.14 € (-0.98%) | 26 | 1 | 12% | -0.436% | -1.536% | -1.593% | -9.20 € |
| estocastico_rebote_filtro | 918.01 € (-0.67%) | 15 | 6 | 20% | -0.415% | -1.515% | -1.614% | -5.24 € |
| ruptura_estricta | 919.21 € (-0.54%) | 8 | 10 | 12% | -1.418% | -2.518% | -2.637% | -4.65 € |
| macd_sin_salida | 914.43 € (-1.06%) | 26 | 17 | 27% | -0.387% | -1.487% | -1.595% | -8.94 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 01:00 | pullback_tendencia_filtro | XLM | rotura de tendencia | -1.08% | -2.18% | -0.50 |
| 2026-09-29 01:00 | macd_momentum_filtro | EIGEN | momentum perdido | -0.67% | -1.77% | -0.40 |
| 2026-09-29 01:00 | macd_momentum_filtro | ARB | momentum perdido | -1.18% | -2.28% | -0.52 |
| 2026-09-29 01:00 | ruptura_volumen_filtro | VVV | timeout | -0.30% | -1.41% | -0.32 |
| 2026-09-29 01:00 | ruptura_volumen_filtro | JUP | stop-loss | -1.20% | -2.30% | -0.52 |
| 2026-09-29 01:00 | ruptura_volumen_filtro | DASH | timeout | -0.74% | -1.84% | -0.42 |
| 2026-09-29 01:00 | macd_momentum | EIGEN | momentum perdido | -0.67% | -1.77% | -0.40 |
| 2026-09-29 01:00 | macd_momentum | ARB | momentum perdido | -1.18% | -2.28% | -0.51 |
| 2026-09-29 01:00 | pullback_tendencia | XLM | rotura de tendencia | -1.08% | -2.18% | -0.49 |
| 2026-09-29 01:00 | ruptura_volumen | VVV | timeout | -0.30% | -1.41% | -0.31 |
| 2026-09-29 01:00 | ruptura_volumen | JUP | stop-loss | -1.20% | -2.30% | -0.51 |
| 2026-09-29 00:55 | ruptura_estricta | XLM | stop-loss | -2.02% | -3.12% | -0.72 |
| 2026-09-29 00:55 | macd_momentum_filtro | CC | momentum perdido | +0.37% | -0.73% | -0.17 |
| 2026-09-29 00:55 | macd_momentum_filtro | OP | momentum perdido | -0.85% | -1.95% | -0.44 |
| 2026-09-29 00:55 | macd_momentum_filtro | ALGO | momentum perdido | +0.62% | -0.47% | -0.11 |

## Eventos de la última vuelta

- 2026-09-29 01:00 [macd_momentum] CIERRE ARB momentum perdido bruto -1.18% neto -2.28%
- 2026-09-29 01:00 [macd_momentum_filtro] CIERRE ARB momentum perdido bruto -1.18% neto -2.28%
- 2026-09-29 01:00 [pullback_tendencia] ENTRADA AVAX @ 9.411 (22.60 €)
- 2026-09-29 01:00 [pullback_tendencia] CIERRE XLM rotura de tendencia bruto -1.08% neto -2.18%
- 2026-09-29 01:00 [pullback_tendencia_filtro] CIERRE XLM rotura de tendencia bruto -1.08% neto -2.18%
- 2026-09-29 01:00 [ruptura_volumen_filtro] CIERRE DASH timeout bruto -0.74% neto -1.84%
- 2026-09-29 01:00 [ruptura_volumen] CIERRE JUP stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 01:00 [ruptura_volumen_filtro] CIERRE JUP stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 01:00 [reversion_bb] ENTRADA FET @ 0.1983 (23.10 €)
- 2026-09-29 01:00 [ruptura_volumen] CIERRE VVV timeout bruto -0.31% neto -1.41%
- 2026-09-29 01:00 [ruptura_volumen_filtro] CIERRE VVV timeout bruto -0.31% neto -1.41%
- 2026-09-29 01:00 [macd_momentum] CIERRE EIGEN momentum perdido bruto -0.67% neto -1.77%
- 2026-09-29 01:00 [macd_momentum_filtro] CIERRE EIGEN momentum perdido bruto -0.67% neto -1.77%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
