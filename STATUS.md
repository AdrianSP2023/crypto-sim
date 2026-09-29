# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 07:56 UTC · vueltas 191 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 860.45 € (-6.90%) | 172 | 14 | 29% | -0.416% | -1.516% | -1.648% | -66.51 € |
| reversion_bb | 918.89 € (-0.58%) | 42 | 0 | 62% | +0.511% | -0.589% | -0.760% | -5.35 € |
| ruptura_volumen | 876.05 € (-5.21%) | 157 | 34 | 23% | -0.146% | -1.246% | -1.369% | -53.97 € |
| rebote_extremo | 917.94 € (-0.68%) | 27 | 0 | 41% | +0.285% | -0.815% | -1.082% | -6.30 € |
| pullback_tendencia | 903.21 € (-2.28%) | 66 | 1 | 23% | -0.196% | -1.296% | -1.393% | -21.08 € |
| macd_momentum | 883.03 € (-4.46%) | 183 | 21 | 26% | +0.055% | -1.045% | -1.161% | -44.45 € |
| estocastico_rebote | 885.06 € (-4.24%) | 111 | 3 | 25% | -0.415% | -1.515% | -1.614% | -39.35 € |
| c_banda_atr_filtro | 893.89 € (-3.28%) | 90 | 14 | 28% | -0.508% | -1.608% | -1.737% | -33.17 € |
| ruptura_volumen_filtro | 901.13 € (-2.50%) | 102 | 35 | 25% | -0.145% | -1.245% | -1.368% | -29.05 € |
| macd_momentum_filtro | 903.66 € (-2.23%) | 107 | 21 | 27% | +0.124% | -0.976% | -1.089% | -23.89 € |
| pullback_tendencia_filtro | 914.66 € (-1.04%) | 30 | 1 | 17% | -0.293% | -1.393% | -1.461% | -9.62 € |
| estocastico_rebote_filtro | 914.55 € (-1.05%) | 24 | 3 | 17% | -0.686% | -1.787% | -1.894% | -9.87 € |
| ruptura_estricta | 921.27 € (-0.32%) | 34 | 35 | 38% | -0.001% | -1.101% | -1.278% | -8.65 € |
| macd_sin_salida | 913.00 € (-1.22%) | 82 | 21 | 49% | +0.281% | -0.819% | -0.952% | -15.50 € |
| c_banda_atr_tope | 922.54 € (-0.18%) | 17 | 5 | 59% | +0.570% | -0.530% | -0.716% | -2.08 € |
| ruptura_volumen_tope | 924.42 € (+0.02%) | 12 | 5 | 42% | +0.952% | -0.148% | -0.319% | -0.41 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 07:55 | macd_sin_salida | RENDER | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 07:55 | macd_sin_salida | ETH | timeout | +1.77% | +0.67% | +0.15 |
| 2026-09-29 07:55 | ruptura_estricta | AVAX | take-profit | +3.00% | +1.90% | +0.43 |
| 2026-09-29 07:55 | macd_momentum_filtro | RENDER | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 07:55 | ruptura_volumen_filtro | PEPE | timeout | +1.84% | +0.74% | +0.17 |
| 2026-09-29 07:55 | ruptura_volumen_filtro | AVAX | take-profit | +2.50% | +1.40% | +0.31 |
| 2026-09-29 07:55 | ruptura_volumen_filtro | XRP | timeout | +1.10% | +0.01% | +0.00 |
| 2026-09-29 07:55 | macd_momentum | RENDER | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 07:55 | ruptura_volumen | PEPE | timeout | +1.84% | +0.74% | +0.16 |
| 2026-09-29 07:55 | ruptura_volumen | AVAX | take-profit | +2.50% | +1.40% | +0.30 |
| 2026-09-29 07:55 | ruptura_volumen | XRP | timeout | +1.10% | +0.01% | +0.00 |
| 2026-09-29 07:50 | macd_sin_salida | ATOM | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 07:50 | macd_sin_salida | W | stop-loss | -1.56% | -2.66% | -0.60 |
| 2026-09-29 07:50 | macd_momentum_filtro | ATOM | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 07:50 | macd_momentum_filtro | BTC | momentum perdido | -0.08% | -1.18% | -0.26 |

## Eventos de la última vuelta

- 2026-09-29 07:55 [macd_sin_salida] CIERRE ETH timeout bruto +1.77% neto +0.67%
- 2026-09-29 07:55 [ruptura_volumen] CIERRE XRP timeout bruto +1.11% neto +0.01%
- 2026-09-29 07:55 [ruptura_volumen_filtro] CIERRE XRP timeout bruto +1.11% neto +0.01%
- 2026-09-29 07:55 [ruptura_estricta] ENTRADA TAO @ 277 (22.88 €)
- 2026-09-29 07:55 [ruptura_volumen] CIERRE AVAX take-profit bruto +2.50% neto +1.40%
- 2026-09-29 07:55 [ruptura_volumen_filtro] CIERRE AVAX take-profit bruto +2.50% neto +1.40%
- 2026-09-29 07:55 [ruptura_estricta] CIERRE AVAX take-profit bruto +3.00% neto +1.90%
- 2026-09-29 07:55 [estocastico_rebote] ENTRADA XDC @ 0.03053 (22.12 €)
- 2026-09-29 07:55 [estocastico_rebote_filtro] ENTRADA XDC @ 0.03053 (22.86 €)
- 2026-09-29 07:55 [ruptura_volumen] CIERRE PEPE timeout bruto +1.84% neto +0.74%
- 2026-09-29 07:55 [ruptura_volumen_filtro] CIERRE PEPE timeout bruto +1.84% neto +0.74%
- 2026-09-29 07:55 [macd_momentum] CIERRE RENDER take-profit bruto +2.00% neto +0.90%
- 2026-09-29 07:55 [macd_momentum_filtro] CIERRE RENDER take-profit bruto +2.00% neto +0.90%
- 2026-09-29 07:55 [macd_sin_salida] CIERRE RENDER take-profit bruto +2.00% neto +0.90%
- 2026-09-29 07:55 [ruptura_estricta] ENTRADA SKY @ 0.07198 (22.89 €)
- 2026-09-29 07:55 [estocastico_rebote] ENTRADA VIRTUAL @ 0.7196 (22.12 €)
- 2026-09-29 07:55 [estocastico_rebote_filtro] ENTRADA VIRTUAL @ 0.7196 (22.86 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
