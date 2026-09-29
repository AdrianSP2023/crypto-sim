# Simulación P1 (sin dinero real)

Config `P1-v10` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-29 06:41 UTC · vueltas 236 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 858.18 € (-7.15%) | 155 | 26 | 21% | -0.680% | -1.780% | -1.906% | -69.73 € |
| reversion_bb | 918.89 € (-0.58%) | 42 | 0 | 62% | +0.511% | -0.589% | -0.762% | -5.35 € |
| ruptura_volumen | 868.75 € (-6.00%) | 137 | 30 | 15% | -0.428% | -1.528% | -1.652% | -56.96 € |
| rebote_extremo | 917.94 € (-0.68%) | 27 | 0 | 41% | +0.285% | -0.815% | -1.073% | -6.30 € |
| pullback_tendencia | 903.16 € (-2.28%) | 66 | 0 | 23% | -0.196% | -1.296% | -1.390% | -21.08 € |
| macd_momentum | 881.88 € (-4.58%) | 151 | 32 | 17% | -0.234% | -1.334% | -1.445% | -46.70 € |
| estocastico_rebote | 884.86 € (-4.26%) | 110 | 2 | 25% | -0.435% | -1.535% | -1.632% | -39.51 € |
| c_banda_atr_filtro | 891.15 € (-3.58%) | 73 | 26 | 11% | -1.095% | -2.195% | -2.315% | -36.61 € |
| ruptura_volumen_filtro | 893.45 € (-3.33%) | 83 | 30 | 12% | -0.602% | -1.702% | -1.827% | -32.23 € |
| macd_momentum_filtro | 902.49 € (-2.35%) | 75 | 32 | 9% | -0.428% | -1.528% | -1.631% | -26.18 € |
| pullback_tendencia_filtro | 914.62 € (-1.04%) | 30 | 0 | 17% | -0.293% | -1.393% | -1.459% | -9.62 € |
| estocastico_rebote_filtro | 914.35 € (-1.07%) | 23 | 2 | 13% | -0.795% | -1.895% | -2.002% | -10.03 € |
| ruptura_estricta | 912.71 € (-1.25%) | 25 | 18 | 16% | -1.119% | -2.219% | -2.368% | -12.76 € |
| macd_sin_salida | 909.13 € (-1.64%) | 56 | 35 | 27% | -0.457% | -1.557% | -1.681% | -20.02 € |
| c_banda_atr_tope | 922.32 € (-0.21%) | 13 | 5 | 46% | +0.130% | -0.970% | -1.146% | -2.91 € |
| ruptura_volumen_tope | 923.95 € (-0.03%) | 9 | 4 | 44% | +0.848% | -0.252% | -0.387% | -0.53 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 06:40 | ruptura_volumen_tope | AVAX | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 06:40 | macd_sin_salida | PUMP | stop-loss | -1.54% | -2.64% | -0.60 |
| 2026-09-29 06:40 | c_banda_atr_filtro | PUMP | stop-loss | -1.54% | -2.64% | -0.59 |
| 2026-09-29 06:40 | c_banda_atr | PUMP | stop-loss | -1.54% | -2.64% | -0.56 |
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

## Eventos de la última vuelta

- 2026-09-29 06:40 [c_banda_atr] CIERRE PUMP stop-loss bruto -1.54% neto -2.64%
- 2026-09-29 06:40 [c_banda_atr_filtro] CIERRE PUMP stop-loss bruto -1.54% neto -2.64%
- 2026-09-29 06:40 [macd_sin_salida] CIERRE PUMP stop-loss bruto -1.54% neto -2.64%
- 2026-09-29 06:40 [ruptura_volumen] ENTRADA AVAX @ 9.583 (21.68 €)
- 2026-09-29 06:40 [ruptura_volumen_filtro] ENTRADA AVAX @ 9.583 (22.30 €)
- 2026-09-29 06:40 [ruptura_volumen_tope] CIERRE AVAX take-profit bruto +2.50% neto +1.40%
- 2026-09-29 06:40 [c_banda_atr_filtro] ENTRADA INJ @ 6.52 (22.19 €)
- 2026-09-29 06:40 [estocastico_rebote] ENTRADA CC @ 0.11629 (22.12 €)
- 2026-09-29 06:40 [estocastico_rebote_filtro] ENTRADA CC @ 0.11629 (22.86 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
