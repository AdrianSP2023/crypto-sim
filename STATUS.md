# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 07:51 UTC · vueltas 190 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 860.28 € (-6.92%) | 172 | 14 | 29% | -0.416% | -1.516% | -1.648% | -66.51 € |
| reversion_bb | 918.89 € (-0.58%) | 42 | 0 | 62% | +0.511% | -0.589% | -0.760% | -5.35 € |
| ruptura_volumen | 876.36 € (-5.18%) | 154 | 37 | 21% | -0.184% | -1.284% | -1.409% | -54.43 € |
| rebote_extremo | 917.94 € (-0.68%) | 27 | 0 | 41% | +0.285% | -0.815% | -1.082% | -6.30 € |
| pullback_tendencia | 902.98 € (-2.30%) | 66 | 1 | 23% | -0.196% | -1.296% | -1.393% | -21.08 € |
| macd_momentum | 883.35 € (-4.42%) | 182 | 22 | 25% | +0.044% | -1.055% | -1.171% | -44.65 € |
| estocastico_rebote | 885.06 € (-4.24%) | 111 | 1 | 25% | -0.415% | -1.515% | -1.614% | -39.35 € |
| c_banda_atr_filtro | 893.72 € (-3.30%) | 90 | 14 | 28% | -0.508% | -1.608% | -1.737% | -33.17 € |
| ruptura_volumen_filtro | 901.29 € (-2.48%) | 99 | 38 | 22% | -0.205% | -1.305% | -1.430% | -29.53 € |
| macd_momentum_filtro | 903.99 € (-2.19%) | 106 | 22 | 26% | +0.106% | -0.994% | -1.106% | -24.09 € |
| pullback_tendencia_filtro | 914.44 € (-1.06%) | 30 | 1 | 17% | -0.293% | -1.393% | -1.461% | -9.62 € |
| estocastico_rebote_filtro | 914.55 € (-1.05%) | 24 | 1 | 17% | -0.686% | -1.787% | -1.894% | -9.87 € |
| ruptura_estricta | 921.61 € (-0.28%) | 33 | 34 | 36% | -0.092% | -1.192% | -1.373% | -9.09 € |
| macd_sin_salida | 913.30 € (-1.18%) | 80 | 23 | 48% | +0.241% | -0.859% | -0.993% | -15.85 € |
| c_banda_atr_tope | 922.32 € (-0.21%) | 17 | 5 | 59% | +0.570% | -0.530% | -0.716% | -2.08 € |
| ruptura_volumen_tope | 924.40 € (+0.02%) | 12 | 5 | 42% | +0.952% | -0.148% | -0.319% | -0.41 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 07:50 | macd_sin_salida | ATOM | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 07:50 | macd_sin_salida | W | stop-loss | -1.56% | -2.66% | -0.60 |
| 2026-09-29 07:50 | macd_momentum_filtro | ATOM | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 07:50 | macd_momentum_filtro | BTC | momentum perdido | -0.08% | -1.18% | -0.26 |
| 2026-09-29 07:50 | ruptura_volumen_filtro | FIL | timeout | +1.53% | +0.43% | +0.10 |
| 2026-09-29 07:50 | ruptura_volumen_filtro | BTC | timeout | +0.85% | -0.25% | -0.06 |
| 2026-09-29 07:50 | macd_momentum | ATOM | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 07:50 | macd_momentum | BTC | momentum perdido | -0.08% | -1.18% | -0.26 |
| 2026-09-29 07:50 | ruptura_volumen | FIL | timeout | +1.53% | +0.43% | +0.09 |
| 2026-09-29 07:50 | ruptura_volumen | BTC | timeout | +0.85% | -0.25% | -0.05 |
| 2026-09-29 07:45 | macd_sin_salida | VVV | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 07:45 | macd_sin_salida | ICP | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 07:45 | macd_sin_salida | PEPE | take-profit | +2.01% | +0.91% | +0.20 |
| 2026-09-29 07:45 | macd_momentum_filtro | VVV | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-29 07:45 | macd_momentum_filtro | PEPE | take-profit | +2.01% | +0.91% | +0.20 |

## Eventos de la última vuelta

- 2026-09-29 07:50 [ruptura_volumen] CIERRE BTC timeout bruto +0.85% neto -0.25%
- 2026-09-29 07:50 [macd_momentum] CIERRE BTC momentum perdido bruto -0.08% neto -1.18%
- 2026-09-29 07:50 [ruptura_volumen_filtro] CIERRE BTC timeout bruto +0.85% neto -0.25%
- 2026-09-29 07:50 [macd_momentum_filtro] CIERRE BTC momentum perdido bruto -0.08% neto -1.18%
- 2026-09-29 07:50 [macd_momentum] ENTRADA XPL @ 0.0892 (21.99 €)
- 2026-09-29 07:50 [macd_momentum_filtro] ENTRADA XPL @ 0.0892 (22.50 €)
- 2026-09-29 07:50 [macd_sin_salida] CIERRE W stop-loss bruto -1.56% neto -2.66%
- 2026-09-29 07:50 [macd_momentum] CIERRE ATOM take-profit bruto +2.00% neto +0.90%
- 2026-09-29 07:50 [macd_momentum_filtro] CIERRE ATOM take-profit bruto +2.00% neto +0.90%
- 2026-09-29 07:50 [macd_sin_salida] CIERRE ATOM take-profit bruto +2.00% neto +0.90%
- 2026-09-29 07:50 [ruptura_volumen] CIERRE FIL timeout bruto +1.53% neto +0.43%
- 2026-09-29 07:50 [ruptura_volumen_filtro] CIERRE FIL timeout bruto +1.53% neto +0.43%
- 2026-09-29 07:50 [ruptura_volumen] ENTRADA ICP @ 3 (21.75 €)
- 2026-09-29 07:50 [ruptura_volumen_filtro] ENTRADA ICP @ 3 (22.37 €)
- 2026-09-29 07:50 [ruptura_estricta] ENTRADA ICP @ 3 (22.88 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
