# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 13:01 UTC · vueltas 41 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 924.66 € (+0.05%) | 8 | 25 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 918.27 € (-0.65%) | 34 | 20 | 35% | +0.392% | -0.708% | -0.839% | -5.56 € |
| rebote_extremo | 924.35 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 920.71 € (-0.38%) | 24 | 11 | 42% | +0.446% | -0.654% | -0.769% | -3.63 € |
| macd_momentum | 910.32 € (-1.51%) | 86 | 9 | 17% | +0.035% | -0.769% | -0.885% | -15.22 € |
| estocastico_rebote | 925.17 € (+0.10%) | 25 | 27 | 80% | +1.204% | +0.104% | -0.035% | +0.60 € |
| ruptura_estricta | 921.18 € (-0.33%) | 17 | 16 | 35% | +0.334% | -0.766% | -0.899% | -3.01 € |
| macd_sin_salida | 918.77 € (-0.59%) | 42 | 15 | 43% | +0.523% | -0.499% | -0.613% | -4.84 € |
| c_banda_atr_tope | 924.47 € (+0.02%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 922.63 € (-0.17%) | 10 | 5 | 30% | +0.387% | -0.713% | -0.836% | -1.65 € |
| c_banda_atr_regimen | 924.66 € (+0.05%) | 8 | 25 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| macd_momentum_regimen | 910.32 € (-1.51%) | 86 | 9 | 17% | +0.035% | -0.769% | -0.885% | -15.22 € |
| ruptura_volumen_regimen | 918.27 € (-0.65%) | 34 | 20 | 35% | +0.392% | -0.708% | -0.839% | -5.56 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 13:00 | macd_momentum_regimen | BNB | momentum perdido | -0.05% | -0.55% | -0.12 |
| 2026-09-29 13:00 | macd_momentum_regimen | TRX | momentum perdido | -0.11% | -0.61% | -0.14 |
| 2026-09-29 13:00 | ruptura_estricta | ONDO | timeout | -1.60% | -2.70% | -0.62 |
| 2026-09-29 13:00 | macd_momentum | BNB | momentum perdido | -0.05% | -0.55% | -0.12 |
| 2026-09-29 13:00 | macd_momentum | TRX | momentum perdido | -0.11% | -0.61% | -0.14 |
| 2026-09-29 12:55 | macd_momentum_regimen | AAVE | momentum perdido | +0.57% | +0.07% | +0.01 |
| 2026-09-29 12:55 | macd_sin_salida | SPX | timeout | +0.22% | -0.58% | -0.13 |
| 2026-09-29 12:55 | macd_sin_salida | BNB | timeout | -0.10% | -0.90% | -0.21 |
| 2026-09-29 12:55 | macd_sin_salida | HYPE | timeout | -0.43% | -1.24% | -0.28 |
| 2026-09-29 12:55 | ruptura_estricta | DOGE | timeout | +0.21% | -0.89% | -0.20 |
| 2026-09-29 12:55 | ruptura_estricta | SUI | timeout | +0.54% | -0.56% | -0.13 |
| 2026-09-29 12:55 | ruptura_estricta | XRP | timeout | +2.55% | +1.45% | +0.34 |
| 2026-09-29 12:55 | estocastico_rebote | TRUMP | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-29 12:55 | macd_momentum | AAVE | momentum perdido | +0.57% | +0.07% | +0.01 |
| 2026-09-29 12:55 | pullback_tendencia | NIGHT | take-profit | +2.00% | +0.90% | +0.21 |

## Eventos de la última vuelta

- 2026-09-29 13:00 [ruptura_estricta] CIERRE ONDO timeout bruto -1.60% neto -2.70%
- 2026-09-29 13:00 [macd_momentum] CIERRE TRX momentum perdido bruto -0.11% neto -0.61%
- 2026-09-29 13:00 [macd_momentum_regimen] CIERRE TRX momentum perdido bruto -0.11% neto -0.61%
- 2026-09-29 13:00 [macd_momentum] CIERRE BNB momentum perdido bruto -0.05% neto -0.55%
- 2026-09-29 13:00 [macd_momentum_regimen] CIERRE BNB momentum perdido bruto -0.05% neto -0.55%
- 2026-09-29 12:55 [ruptura_volumen] ENTRADA TRUMP @ 1.819 (22.97 €, apertura)
- 2026-09-29 12:55 [ruptura_estricta] ENTRADA TRUMP @ 1.819 (23.03 €, apertura)
- 2026-09-29 12:55 [ruptura_volumen_regimen] ENTRADA TRUMP @ 1.819 (22.97 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
