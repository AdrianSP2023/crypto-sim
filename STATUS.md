# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 02:06 UTC · vueltas 96 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 900.88 € (-2.53%) | 93 | 26 | 27% | -0.278% | -1.058% | -1.185% | -22.57 € |
| reversion_bb | 921.21 € (-0.33%) | 13 | 3 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 891.24 € (-3.57%) | 126 | 15 | 16% | -0.431% | -1.138% | -1.251% | -32.72 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.34 € (-2.26%) | 81 | 3 | 16% | -0.317% | -1.143% | -1.266% | -21.21 € |
| macd_momentum | 897.72 € (-2.87%) | 168 | 6 | 21% | -0.052% | -0.707% | -0.817% | -27.13 € |
| estocastico_rebote | 901.32 € (-2.48%) | 140 | 15 | 36% | -0.001% | -0.688% | -0.810% | -22.14 € |
| ruptura_estricta | 896.69 € (-2.98%) | 61 | 15 | 15% | -0.937% | -1.870% | -2.008% | -26.23 € |
| macd_sin_salida | 900.85 € (-2.53%) | 117 | 17 | 33% | -0.125% | -0.848% | -0.963% | -22.77 € |
| c_banda_atr_tope | 917.53 € (-0.73%) | 23 | 4 | 26% | -0.149% | -1.249% | -1.380% | -6.62 € |
| ruptura_volumen_tope | 915.22 € (-0.98%) | 33 | 5 | 18% | -0.115% | -1.215% | -1.296% | -9.23 € |
| c_banda_atr_regimen | 906.31 € (-1.94%) | 48 | 13 | 23% | -0.511% | -1.555% | -1.710% | -17.17 € |
| macd_momentum_regimen | 905.62 € (-2.01%) | 92 | 2 | 21% | -0.098% | -0.882% | -1.000% | -18.63 € |
| ruptura_volumen_regimen | 891.97 € (-3.49%) | 103 | 11 | 14% | -0.568% | -1.322% | -1.441% | -31.10 € |
| c_banda_atr_evento | 907.15 € (-1.85%) | 60 | 26 | 25% | -0.260% | -1.180% | -1.289% | -16.29 € |
| macd_momentum_evento | 902.69 € (-2.33%) | 121 | 6 | 15% | -0.083% | -0.801% | -0.900% | -22.17 € |
| ruptura_volumen_evento | 903.92 € (-2.20%) | 76 | 15 | 13% | -0.302% | -1.149% | -1.237% | -20.03 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 02:05 | macd_momentum_evento | RENDER | momentum perdido | -0.06% | -0.56% | -0.13 |
| 2026-10-01 02:05 | macd_momentum_evento | ADA | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-10-01 02:05 | macd_momentum_regimen | RENDER | momentum perdido | -0.06% | -0.56% | -0.13 |
| 2026-10-01 02:05 | c_banda_atr_tope | DASH | timeout | -0.18% | -1.28% | -0.29 |
| 2026-10-01 02:05 | ruptura_estricta | FIL | timeout | +0.33% | -0.17% | -0.04 |
| 2026-10-01 02:05 | ruptura_estricta | ADA | timeout | -0.62% | -1.12% | -0.25 |
| 2026-10-01 02:05 | estocastico_rebote | PUMP | stop-loss | -1.53% | -2.04% | -0.46 |
| 2026-10-01 02:05 | macd_momentum | RENDER | momentum perdido | -0.06% | -0.56% | -0.13 |
| 2026-10-01 02:05 | macd_momentum | ADA | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-10-01 02:00 | macd_momentum_evento | SHIB | momentum perdido | -0.10% | -0.60% | -0.14 |
| 2026-10-01 02:00 | macd_momentum_evento | PEPE | momentum perdido | +0.05% | -0.45% | -0.10 |
| 2026-10-01 02:00 | macd_momentum_evento | DOGE | momentum perdido | +0.18% | -0.32% | -0.07 |
| 2026-10-01 02:00 | macd_momentum_regimen | PEPE | momentum perdido | +0.05% | -0.45% | -0.10 |
| 2026-10-01 02:00 | macd_momentum_regimen | DOGE | momentum perdido | +0.18% | -0.32% | -0.07 |
| 2026-10-01 02:00 | macd_momentum | SHIB | momentum perdido | -0.10% | -0.60% | -0.14 |

## Eventos de la última vuelta

- 2026-10-01 02:05 [macd_momentum] CIERRE ADA momentum perdido bruto -0.27% neto -0.77%
- 2026-10-01 02:05 [ruptura_estricta] CIERRE ADA timeout bruto -0.62% neto -1.12%
- 2026-10-01 02:05 [macd_momentum_evento] CIERRE ADA momentum perdido bruto -0.27% neto -0.77%
- 2026-10-01 02:05 [estocastico_rebote] CIERRE PUMP stop-loss bruto -1.54% neto -2.04%
- 2026-10-01 02:00 [estocastico_rebote] ENTRADA LTC @ 59.2 (22.55 €, apertura)
- 2026-10-01 02:05 [macd_momentum] CIERRE RENDER momentum perdido bruto -0.06% neto -0.56%
- 2026-10-01 02:05 [macd_momentum_regimen] CIERRE RENDER momentum perdido bruto -0.06% neto -0.56%
- 2026-10-01 02:05 [macd_momentum_evento] CIERRE RENDER momentum perdido bruto -0.06% neto -0.56%
- 2026-10-01 02:05 [ruptura_estricta] CIERRE FIL timeout bruto +0.33% neto -0.17%
- 2026-10-01 02:05 [c_banda_atr_tope] CIERRE DASH timeout bruto -0.18% neto -1.28%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
