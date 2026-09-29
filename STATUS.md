# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 06:36 UTC · vueltas 235 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 858.29 € (-7.14%) | 154 | 27 | 21% | -0.674% | -1.774% | -1.900% | -69.17 € |
| reversion_bb | 918.89 € (-0.58%) | 42 | 0 | 62% | +0.511% | -0.589% | -0.762% | -5.35 € |
| ruptura_volumen | 869.00 € (-5.98%) | 137 | 29 | 15% | -0.428% | -1.528% | -1.652% | -56.96 € |
| rebote_extremo | 917.94 € (-0.68%) | 27 | 0 | 41% | +0.285% | -0.815% | -1.073% | -6.30 € |
| pullback_tendencia | 903.16 € (-2.28%) | 66 | 0 | 23% | -0.196% | -1.296% | -1.390% | -21.08 € |
| macd_momentum | 881.91 € (-4.58%) | 151 | 32 | 17% | -0.234% | -1.334% | -1.445% | -46.70 € |
| estocastico_rebote | 884.94 € (-4.25%) | 110 | 1 | 25% | -0.435% | -1.535% | -1.632% | -39.51 € |
| c_banda_atr_filtro | 891.41 € (-3.55%) | 72 | 26 | 11% | -1.088% | -2.188% | -2.308% | -36.03 € |
| ruptura_volumen_filtro | 893.71 € (-3.30%) | 83 | 29 | 12% | -0.602% | -1.702% | -1.827% | -32.23 € |
| macd_momentum_filtro | 902.52 € (-2.35%) | 75 | 32 | 9% | -0.428% | -1.528% | -1.631% | -26.18 € |
| pullback_tendencia_filtro | 914.62 € (-1.04%) | 30 | 0 | 17% | -0.293% | -1.393% | -1.459% | -9.62 € |
| estocastico_rebote_filtro | 914.43 € (-1.06%) | 23 | 1 | 13% | -0.795% | -1.895% | -2.002% | -10.03 € |
| ruptura_estricta | 913.07 € (-1.21%) | 25 | 18 | 16% | -1.119% | -2.219% | -2.368% | -12.76 € |
| macd_sin_salida | 909.55 € (-1.59%) | 55 | 36 | 27% | -0.437% | -1.537% | -1.660% | -19.42 € |
| c_banda_atr_tope | 922.37 € (-0.20%) | 13 | 5 | 46% | +0.130% | -0.970% | -1.146% | -2.91 € |
| ruptura_volumen_tope | 924.18 € (-0.01%) | 8 | 5 | 38% | +0.641% | -0.459% | -0.604% | -0.85 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 06:35 | ruptura_estricta | WLD | take-profit | +3.00% | +1.90% | +0.43 |
| 2026-09-29 06:35 | ruptura_volumen_filtro | WLD | take-profit | +2.50% | +1.40% | +0.31 |
| 2026-09-29 06:35 | ruptura_volumen_filtro | GRT | timeout | -0.56% | -1.66% | -0.37 |
| 2026-09-29 06:35 | ruptura_volumen | WLD | take-profit | +2.50% | +1.40% | +0.30 |
| 2026-09-29 06:35 | ruptura_volumen | GRT | timeout | -0.56% | -1.66% | -0.36 |
| 2026-09-29 06:30 | macd_momentum_filtro | KAS | momentum perdido | -0.07% | -1.17% | -0.26 |
| 2026-09-29 06:30 | ruptura_volumen_filtro | NIGHT | timeout | -0.24% | -1.34% | -0.30 |
| 2026-09-29 06:30 | macd_momentum | KAS | momentum perdido | -0.07% | -1.17% | -0.26 |
| 2026-09-29 06:30 | ruptura_volumen | NIGHT | timeout | -0.24% | -1.34% | -0.29 |
| 2026-09-29 06:25 | macd_momentum_filtro | PUMP | momentum perdido | -0.37% | -1.47% | -0.33 |
| 2026-09-29 06:25 | ruptura_volumen_filtro | AVAX | take-profit | +2.50% | +1.40% | +0.31 |
| 2026-09-29 06:25 | macd_momentum | PUMP | momentum perdido | -0.37% | -1.47% | -0.32 |
| 2026-09-29 06:25 | ruptura_volumen | AVAX | take-profit | +2.50% | +1.40% | +0.30 |
| 2026-09-29 06:20 | ruptura_estricta | CRV | take-profit | +3.00% | +1.90% | +0.43 |
| 2026-09-29 06:20 | pullback_tendencia_filtro | CRV | take-profit | +2.00% | +0.90% | +0.21 |

## Eventos de la última vuelta

- 2026-09-29 06:35 [ruptura_volumen] CIERRE GRT timeout bruto -0.56% neto -1.66%
- 2026-09-29 06:35 [ruptura_volumen_filtro] CIERRE GRT timeout bruto -0.56% neto -1.66%
- 2026-09-29 06:35 [ruptura_estricta] ENTRADA FET @ 0.2007 (22.78 €)
- 2026-09-29 06:35 [ruptura_volumen] ENTRADA ZRO @ 1.365 (21.67 €)
- 2026-09-29 06:35 [ruptura_volumen_filtro] ENTRADA ZRO @ 1.365 (22.29 €)
- 2026-09-29 06:35 [ruptura_volumen] CIERRE WLD take-profit bruto +2.50% neto +1.40%
- 2026-09-29 06:35 [ruptura_volumen_filtro] CIERRE WLD take-profit bruto +2.50% neto +1.40%
- 2026-09-29 06:35 [ruptura_estricta] CIERRE WLD take-profit bruto +3.00% neto +1.90%

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
