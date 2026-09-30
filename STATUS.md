# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 23:46 UTC · vueltas 110 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 904.97 € (-2.09%) | 74 | 28 | 28% | -0.344% | -1.197% | -1.338% | -20.34 € |
| reversion_bb | 921.94 € (-0.25%) | 10 | 5 | 40% | -0.070% | -1.170% | -1.296% | -2.71 € |
| ruptura_volumen | 895.58 € (-3.10%) | 95 | 25 | 17% | -0.481% | -1.256% | -1.391% | -27.32 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.61 € (-2.12%) | 66 | 6 | 15% | -0.407% | -1.307% | -1.444% | -19.77 € |
| macd_momentum | 903.18 € (-2.28%) | 121 | 15 | 25% | -0.068% | -0.784% | -0.906% | -21.74 € |
| estocastico_rebote | 903.14 € (-2.28%) | 127 | 10 | 35% | -0.037% | -0.743% | -0.875% | -21.70 € |
| ruptura_estricta | 898.53 € (-2.78%) | 52 | 9 | 13% | -1.113% | -2.121% | -2.268% | -25.38 € |
| macd_sin_salida | 904.12 € (-2.18%) | 88 | 28 | 33% | -0.217% | -1.013% | -1.141% | -20.50 € |
| c_banda_atr_tope | 919.34 € (-0.53%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.258% | -5.10 € |
| ruptura_volumen_tope | 916.01 € (-0.89%) | 28 | 5 | 18% | -0.171% | -1.271% | -1.380% | -8.20 € |
| c_banda_atr_regimen | 907.59 € (-1.80%) | 46 | 8 | 24% | -0.467% | -1.535% | -1.694% | -16.25 € |
| macd_momentum_regimen | 909.53 € (-1.59%) | 69 | 7 | 28% | -0.037% | -0.915% | -1.046% | -14.55 € |
| ruptura_volumen_regimen | 897.05 € (-2.94%) | 74 | 23 | 14% | -0.676% | -1.529% | -1.667% | -25.94 € |
| c_banda_atr_evento | 912.17 € (-1.31%) | 41 | 28 | 27% | -0.372% | -1.391% | -1.517% | -13.14 € |
| macd_momentum_evento | 908.25 € (-1.73%) | 74 | 15 | 19% | -0.130% | -0.982% | -1.094% | -16.67 € |
| ruptura_volumen_evento | 908.46 € (-1.71%) | 45 | 25 | 13% | -0.319% | -1.392% | -1.511% | -14.42 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 23:45 | macd_momentum_evento | SPX | momentum perdido | +0.83% | +0.33% | +0.07 |
| 2026-09-30 23:45 | macd_momentum_evento | TRUMP | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-09-30 23:45 | macd_momentum_evento | SHIB | momentum perdido | -0.33% | -0.83% | -0.19 |
| 2026-09-30 23:45 | macd_momentum_evento | JUP | momentum perdido | +0.64% | +0.14% | +0.03 |
| 2026-09-30 23:45 | c_banda_atr_evento | OP | timeout | -0.09% | -0.89% | -0.20 |
| 2026-09-30 23:45 | macd_momentum_regimen | TRUMP | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-09-30 23:45 | macd_momentum_regimen | SHIB | momentum perdido | -0.33% | -0.83% | -0.19 |
| 2026-09-30 23:45 | c_banda_atr_regimen | USELESS | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-09-30 23:45 | macd_momentum | SPX | momentum perdido | +0.83% | +0.33% | +0.07 |
| 2026-09-30 23:45 | macd_momentum | TRUMP | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-09-30 23:45 | macd_momentum | SHIB | momentum perdido | -0.33% | -0.83% | -0.19 |
| 2026-09-30 23:45 | macd_momentum | JUP | momentum perdido | +0.64% | +0.14% | +0.03 |
| 2026-09-30 23:45 | c_banda_atr | OP | timeout | -0.09% | -0.59% | -0.13 |
| 2026-09-30 23:40 | macd_momentum_evento | ONDO | momentum perdido | +0.61% | +0.11% | +0.03 |
| 2026-09-30 23:40 | macd_momentum_evento | ARB | momentum perdido | -0.33% | -0.83% | -0.19 |

## Eventos de la última vuelta

- 2026-09-30 23:40 [estocastico_rebote] ENTRADA PUMP @ 0.005229 (22.56 €, apertura)
- 2026-09-30 23:45 [c_banda_atr_regimen] CIERRE USELESS stop-loss bruto -1.63% neto -2.13%
- 2026-09-30 23:45 [macd_momentum] CIERRE JUP momentum perdido bruto +0.64% neto +0.14%
- 2026-09-30 23:45 [macd_momentum_evento] CIERRE JUP momentum perdido bruto +0.64% neto +0.14%
- 2026-09-30 23:40 [ruptura_volumen] ENTRADA MON @ 0.02763 (22.42 €, apertura)
- 2026-09-30 23:40 [ruptura_estricta] ENTRADA MON @ 0.02763 (22.47 €, apertura)
- 2026-09-30 23:40 [ruptura_volumen_tope] ENTRADA MON @ 0.02763 (22.90 €, apertura)
- 2026-09-30 23:40 [ruptura_volumen_regimen] ENTRADA MON @ 0.02763 (22.46 €, apertura)
- 2026-09-30 23:40 [ruptura_volumen_evento] ENTRADA MON @ 0.02763 (22.75 €, apertura)
- 2026-09-30 23:45 [c_banda_atr] CIERRE OP timeout bruto -0.09% neto -0.59%
- 2026-09-30 23:45 [c_banda_atr_evento] CIERRE OP timeout bruto -0.09% neto -0.89%
- 2026-09-30 23:45 [macd_momentum] CIERRE SHIB momentum perdido bruto -0.33% neto -0.83%
- 2026-09-30 23:45 [macd_momentum_regimen] CIERRE SHIB momentum perdido bruto -0.33% neto -0.83%
- 2026-09-30 23:45 [macd_momentum_evento] CIERRE SHIB momentum perdido bruto -0.33% neto -0.83%
- 2026-09-30 23:45 [macd_momentum] CIERRE TRUMP momentum perdido bruto -0.17% neto -0.67%
- 2026-09-30 23:45 [macd_momentum_regimen] CIERRE TRUMP momentum perdido bruto -0.17% neto -0.67%
- 2026-09-30 23:45 [macd_momentum_evento] CIERRE TRUMP momentum perdido bruto -0.17% neto -0.67%
- 2026-09-30 23:45 [macd_momentum] CIERRE SPX momentum perdido bruto +0.83% neto +0.33%
- 2026-09-30 23:45 [macd_momentum_evento] CIERRE SPX momentum perdido bruto +0.83% neto +0.33%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
