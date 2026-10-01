# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 03:01 UTC · vueltas 107 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.63 € (-2.23%) | 104 | 26 | 29% | -0.202% | -0.953% | -1.076% | -22.73 € |
| reversion_bb | 921.36 € (-0.31%) | 13 | 5 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 892.13 € (-3.47%) | 136 | 13 | 18% | -0.380% | -1.072% | -1.188% | -33.25 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.33 € (-2.26%) | 82 | 4 | 16% | -0.314% | -1.136% | -1.257% | -21.34 € |
| macd_momentum | 898.00 € (-2.84%) | 180 | 20 | 21% | -0.048% | -0.693% | -0.801% | -28.44 € |
| estocastico_rebote | 903.23 € (-2.27%) | 148 | 19 | 37% | +0.029% | -0.647% | -0.771% | -22.03 € |
| ruptura_estricta | 899.28 € (-2.70%) | 63 | 18 | 17% | -0.812% | -1.731% | -1.871% | -25.10 € |
| macd_sin_salida | 903.68 € (-2.22%) | 121 | 31 | 35% | -0.068% | -0.784% | -0.900% | -21.78 € |
| c_banda_atr_tope | 917.51 € (-0.73%) | 25 | 4 | 24% | -0.111% | -1.211% | -1.337% | -6.98 € |
| ruptura_volumen_tope | 914.99 € (-1.00%) | 40 | 3 | 22% | +0.071% | -1.029% | -1.128% | -9.48 € |
| c_banda_atr_regimen | 908.24 € (-1.73%) | 53 | 19 | 26% | -0.396% | -1.389% | -1.541% | -16.93 € |
| macd_momentum_regimen | 906.33 € (-1.94%) | 97 | 17 | 21% | -0.087% | -0.856% | -0.974% | -19.07 € |
| ruptura_volumen_regimen | 892.92 € (-3.39%) | 109 | 13 | 14% | -0.545% | -1.284% | -1.405% | -31.96 € |
| c_banda_atr_evento | 909.65 € (-1.58%) | 71 | 26 | 28% | -0.152% | -1.024% | -1.131% | -16.72 € |
| macd_momentum_evento | 902.98 € (-2.30%) | 133 | 20 | 15% | -0.074% | -0.773% | -0.871% | -23.48 € |
| ruptura_volumen_evento | 904.82 € (-2.10%) | 86 | 13 | 17% | -0.237% | -1.044% | -1.140% | -20.57 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 03:00 | ruptura_volumen_evento | XMR | timeout | -0.02% | -0.52% | -0.12 |
| 2026-10-01 03:00 | c_banda_atr_evento | SPX | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 03:00 | c_banda_atr_evento | XMR | timeout | +0.83% | +0.33% | +0.07 |
| 2026-10-01 03:00 | ruptura_volumen_regimen | XMR | timeout | -0.02% | -0.52% | -0.12 |
| 2026-10-01 03:00 | c_banda_atr_regimen | XMR | timeout | +0.83% | +0.33% | +0.07 |
| 2026-10-01 03:00 | ruptura_volumen_tope | XMR | timeout | -0.02% | -1.12% | -0.26 |
| 2026-10-01 03:00 | c_banda_atr_tope | XMR | timeout | +0.83% | -0.27% | -0.06 |
| 2026-10-01 03:00 | ruptura_estricta | TRUMP | take-profit | +3.00% | +2.50% | +0.56 |
| 2026-10-01 03:00 | estocastico_rebote | SPX | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 03:00 | estocastico_rebote | SEI | timeout | -0.56% | -1.05% | -0.24 |
| 2026-10-01 03:00 | ruptura_volumen | XMR | timeout | -0.02% | -0.52% | -0.12 |
| 2026-10-01 03:00 | c_banda_atr | SPX | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 03:00 | c_banda_atr | XMR | timeout | +0.83% | +0.33% | +0.07 |
| 2026-10-01 02:55 | macd_momentum_evento | XDC | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 02:55 | ruptura_volumen_tope | TRUMP | take-profit | +2.50% | +1.40% | +0.32 |

## Eventos de la última vuelta

- 2026-10-01 02:55 [macd_momentum] ENTRADA LTC @ 59.37 (22.39 €, apertura)
- 2026-10-01 02:55 [macd_momentum_regimen] ENTRADA LTC @ 59.37 (22.63 €, apertura)
- 2026-10-01 02:55 [macd_momentum_evento] ENTRADA LTC @ 59.37 (22.52 €, apertura)
- 2026-10-01 02:55 [macd_momentum] ENTRADA RENDER @ 1.694 (22.39 €, apertura)
- 2026-10-01 02:55 [macd_momentum_regimen] ENTRADA RENDER @ 1.694 (22.63 €, apertura)
- 2026-10-01 02:55 [macd_momentum_evento] ENTRADA RENDER @ 1.694 (22.52 €, apertura)
- 2026-10-01 02:55 [c_banda_atr_regimen] ENTRADA OP @ 0.1138 (22.68 €, apertura)
- 2026-10-01 02:55 [ruptura_volumen] ENTRADA TRUMP @ 1.953 (22.28 €, apertura)
- 2026-10-01 03:00 [ruptura_estricta] CIERRE TRUMP take-profit bruto +3.00% neto +2.50%
- 2026-10-01 02:55 [ruptura_volumen_regimen] ENTRADA TRUMP @ 1.953 (22.31 €, apertura)
- 2026-10-01 02:55 [ruptura_volumen_evento] ENTRADA TRUMP @ 1.953 (22.59 €, apertura)
- 2026-10-01 03:00 [c_banda_atr] CIERRE XMR timeout bruto +0.83% neto +0.33%
- 2026-10-01 03:00 [ruptura_volumen] CIERRE XMR timeout bruto -0.02% neto -0.52%
- 2026-10-01 03:00 [c_banda_atr_tope] CIERRE XMR timeout bruto +0.83% neto -0.27%
- 2026-10-01 03:00 [ruptura_volumen_tope] CIERRE XMR timeout bruto -0.02% neto -1.12%
- 2026-10-01 03:00 [c_banda_atr_regimen] CIERRE XMR timeout bruto +0.83% neto +0.33%
- 2026-10-01 03:00 [ruptura_volumen_regimen] CIERRE XMR timeout bruto -0.02% neto -0.52%
- 2026-10-01 03:00 [c_banda_atr_evento] CIERRE XMR timeout bruto +0.83% neto +0.33%
- 2026-10-01 03:00 [ruptura_volumen_evento] CIERRE XMR timeout bruto -0.02% neto -0.52%
- 2026-10-01 03:00 [estocastico_rebote] CIERRE SEI timeout bruto -0.55% neto -1.05%
- 2026-10-01 03:00 [c_banda_atr] CIERRE SPX take-profit bruto +2.00% neto +1.50%
- 2026-10-01 03:00 [estocastico_rebote] CIERRE SPX take-profit bruto +1.80% neto +1.30%
- 2026-10-01 03:00 [c_banda_atr_evento] CIERRE SPX take-profit bruto +2.00% neto +1.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
