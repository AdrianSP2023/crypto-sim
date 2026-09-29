# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 08:11 UTC · vueltas 194 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 859.58 € (-7.00%) | 173 | 13 | 29% | -0.401% | -1.501% | -1.633% | -66.28 € |
| reversion_bb | 918.89 € (-0.58%) | 42 | 0 | 62% | +0.511% | -0.589% | -0.760% | -5.35 € |
| ruptura_volumen | 872.26 € (-5.62%) | 165 | 28 | 24% | -0.126% | -1.226% | -1.349% | -55.43 € |
| rebote_extremo | 917.94 € (-0.68%) | 27 | 0 | 41% | +0.285% | -0.815% | -1.082% | -6.30 € |
| pullback_tendencia | 902.76 € (-2.32%) | 66 | 4 | 23% | -0.196% | -1.296% | -1.393% | -21.08 € |
| macd_momentum | 879.31 € (-4.86%) | 194 | 11 | 26% | +0.075% | -1.025% | -1.141% | -46.14 € |
| estocastico_rebote | 885.20 € (-4.22%) | 112 | 2 | 26% | -0.395% | -1.495% | -1.595% | -39.20 € |
| c_banda_atr_filtro | 892.98 € (-3.38%) | 91 | 13 | 29% | -0.478% | -1.578% | -1.708% | -32.93 € |
| ruptura_volumen_filtro | 898.06 € (-2.83%) | 110 | 28 | 26% | -0.082% | -1.182% | -1.304% | -29.73 € |
| macd_momentum_filtro | 899.86 € (-2.64%) | 118 | 11 | 28% | +0.150% | -0.950% | -1.062% | -25.63 € |
| pullback_tendencia_filtro | 914.21 € (-1.08%) | 30 | 4 | 17% | -0.293% | -1.393% | -1.461% | -9.62 € |
| estocastico_rebote_filtro | 914.70 € (-1.03%) | 25 | 2 | 20% | -0.587% | -1.687% | -1.798% | -9.71 € |
| ruptura_estricta | 919.05 € (-0.56%) | 36 | 33 | 36% | -0.120% | -1.220% | -1.397% | -10.14 € |
| macd_sin_salida | 911.55 € (-1.37%) | 84 | 20 | 49% | +0.306% | -0.794% | -0.926% | -15.38 € |
| c_banda_atr_tope | 922.19 € (-0.22%) | 17 | 5 | 59% | +0.570% | -0.530% | -0.716% | -2.08 € |
| ruptura_volumen_tope | 923.69 € (-0.06%) | 13 | 4 | 38% | +0.774% | -0.326% | -0.490% | -0.98 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 08:10 | ruptura_volumen_tope | ZRO | stop-loss | -1.37% | -2.47% | -0.57 |
| 2026-09-29 08:10 | ruptura_estricta | USELESS | stop-loss | -2.30% | -3.40% | -0.78 |
| 2026-09-29 08:10 | macd_momentum_filtro | ICP | momentum perdido | -0.17% | -1.27% | -0.29 |
| 2026-09-29 08:10 | macd_momentum_filtro | FET | momentum perdido | +0.00% | -1.10% | -0.25 |
| 2026-09-29 08:10 | macd_momentum_filtro | JUP | momentum perdido | +1.11% | +0.01% | +0.00 |
| 2026-09-29 08:10 | macd_momentum_filtro | LTC | momentum perdido | +0.87% | -0.23% | -0.05 |
| 2026-09-29 08:10 | ruptura_volumen_filtro | OP | timeout | +0.70% | -0.40% | -0.09 |
| 2026-09-29 08:10 | ruptura_volumen_filtro | USELESS | stop-loss | -2.30% | -3.40% | -0.76 |
| 2026-09-29 08:10 | ruptura_volumen_filtro | ZEC | timeout | +1.61% | +0.51% | +0.12 |
| 2026-09-29 08:10 | macd_momentum | ICP | momentum perdido | -0.17% | -1.27% | -0.28 |
| 2026-09-29 08:10 | macd_momentum | FET | momentum perdido | +0.00% | -1.10% | -0.24 |
| 2026-09-29 08:10 | macd_momentum | JUP | momentum perdido | +1.11% | +0.01% | +0.00 |
| 2026-09-29 08:10 | macd_momentum | LTC | momentum perdido | +0.87% | -0.23% | -0.05 |
| 2026-09-29 08:10 | ruptura_volumen | OP | timeout | +0.70% | -0.40% | -0.09 |
| 2026-09-29 08:10 | ruptura_volumen | USELESS | stop-loss | -2.30% | -3.40% | -0.74 |

## Eventos de la última vuelta

- 2026-09-29 08:10 [ruptura_volumen] CIERRE ZEC timeout bruto +1.61% neto +0.51%
- 2026-09-29 08:10 [ruptura_volumen_filtro] CIERRE ZEC timeout bruto +1.61% neto +0.51%
- 2026-09-29 08:10 [pullback_tendencia] ENTRADA LTC @ 60.44 (22.58 €)
- 2026-09-29 08:10 [macd_momentum] CIERRE LTC momentum perdido bruto +0.87% neto -0.23%
- 2026-09-29 08:10 [macd_momentum_filtro] CIERRE LTC momentum perdido bruto +0.87% neto -0.23%
- 2026-09-29 08:10 [pullback_tendencia_filtro] ENTRADA LTC @ 60.44 (22.87 €)
- 2026-09-29 08:10 [ruptura_volumen] CIERRE XDC stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 08:10 [macd_momentum] ENTRADA XDC @ 0.03084 (21.97 €)
- 2026-09-29 08:10 [macd_momentum_filtro] ENTRADA XDC @ 0.03084 (22.48 €)
- 2026-09-29 08:10 [macd_sin_salida] ENTRADA XDC @ 0.03084 (22.72 €)
- 2026-09-29 08:10 [macd_momentum] CIERRE JUP momentum perdido bruto +1.11% neto +0.01%
- 2026-09-29 08:10 [macd_momentum_filtro] CIERRE JUP momentum perdido bruto +1.11% neto +0.01%
- 2026-09-29 08:10 [ruptura_volumen] CIERRE USELESS stop-loss bruto -2.30% neto -3.40%
- 2026-09-29 08:10 [ruptura_volumen_filtro] CIERRE USELESS stop-loss bruto -2.30% neto -3.40%
- 2026-09-29 08:10 [ruptura_estricta] CIERRE USELESS stop-loss bruto -2.30% neto -3.40%
- 2026-09-29 08:10 [macd_momentum] CIERRE FET momentum perdido bruto +0.00% neto -1.10%
- 2026-09-29 08:10 [macd_momentum_filtro] CIERRE FET momentum perdido bruto +0.00% neto -1.10%
- 2026-09-29 08:10 [ruptura_volumen_tope] CIERRE ZRO stop-loss bruto -1.37% neto -2.47%
- 2026-09-29 08:10 [pullback_tendencia] ENTRADA ICP @ 2.944 (22.58 €)
- 2026-09-29 08:10 [macd_momentum] CIERRE ICP momentum perdido bruto -0.17% neto -1.27%
- 2026-09-29 08:10 [macd_momentum_filtro] CIERRE ICP momentum perdido bruto -0.17% neto -1.27%
- 2026-09-29 08:10 [pullback_tendencia_filtro] ENTRADA ICP @ 2.944 (22.87 €)
- 2026-09-29 08:10 [ruptura_volumen] CIERRE OP timeout bruto +0.70% neto -0.40%
- 2026-09-29 08:10 [ruptura_volumen_filtro] CIERRE OP timeout bruto +0.70% neto -0.40%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
