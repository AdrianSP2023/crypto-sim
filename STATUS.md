# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 02:16 UTC · vueltas 98 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.39 € (-2.36%) | 93 | 28 | 27% | -0.278% | -1.058% | -1.185% | -22.57 € |
| reversion_bb | 921.29 € (-0.32%) | 13 | 3 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 892.25 € (-3.46%) | 126 | 16 | 16% | -0.431% | -1.138% | -1.251% | -32.72 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.55 € (-2.24%) | 81 | 3 | 16% | -0.317% | -1.143% | -1.266% | -21.21 € |
| macd_momentum | 897.84 € (-2.86%) | 170 | 7 | 21% | -0.036% | -0.690% | -0.800% | -26.79 € |
| estocastico_rebote | 902.18 € (-2.39%) | 140 | 18 | 36% | -0.001% | -0.688% | -0.810% | -22.14 € |
| ruptura_estricta | 897.67 € (-2.87%) | 61 | 15 | 15% | -0.937% | -1.870% | -2.008% | -26.23 € |
| macd_sin_salida | 901.61 € (-2.45%) | 118 | 18 | 34% | -0.105% | -0.826% | -0.942% | -22.39 € |
| c_banda_atr_tope | 917.53 € (-0.73%) | 23 | 5 | 26% | -0.149% | -1.249% | -1.380% | -6.62 € |
| ruptura_volumen_tope | 915.52 € (-0.94%) | 33 | 5 | 18% | -0.115% | -1.215% | -1.296% | -9.23 € |
| c_banda_atr_regimen | 906.86 € (-1.88%) | 48 | 13 | 23% | -0.511% | -1.555% | -1.710% | -17.17 € |
| macd_momentum_regimen | 905.65 € (-2.01%) | 92 | 2 | 21% | -0.098% | -0.882% | -1.000% | -18.63 € |
| ruptura_volumen_regimen | 892.72 € (-3.41%) | 103 | 11 | 14% | -0.568% | -1.322% | -1.441% | -31.10 € |
| c_banda_atr_evento | 908.67 € (-1.68%) | 60 | 28 | 25% | -0.260% | -1.180% | -1.289% | -16.29 € |
| macd_momentum_evento | 902.82 € (-2.32%) | 123 | 7 | 15% | -0.061% | -0.776% | -0.875% | -21.82 € |
| ruptura_volumen_evento | 904.94 € (-2.09%) | 76 | 16 | 13% | -0.302% | -1.149% | -1.237% | -20.03 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 02:15 | macd_momentum_evento | KAS | take-profit | +2.19% | +1.69% | +0.38 |
| 2026-10-01 02:15 | macd_sin_salida | KAS | take-profit | +2.19% | +1.69% | +0.38 |
| 2026-10-01 02:15 | macd_momentum | KAS | take-profit | +2.19% | +1.69% | +0.38 |
| 2026-10-01 02:10 | macd_momentum_evento | CRV | momentum perdido | +0.33% | -0.17% | -0.04 |
| 2026-10-01 02:10 | macd_momentum | CRV | momentum perdido | +0.33% | -0.17% | -0.04 |
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

## Eventos de la última vuelta

- 2026-10-01 02:10 [c_banda_atr] ENTRADA BTC @ 73792.4 (22.54 €, apertura)
- 2026-10-01 02:10 [c_banda_atr_evento] ENTRADA BTC @ 73792.4 (22.70 €, apertura)
- 2026-10-01 02:10 [ruptura_volumen] ENTRADA ETH @ 2377.56 (22.29 €, apertura)
- 2026-10-01 02:10 [ruptura_volumen_evento] ENTRADA ETH @ 2377.56 (22.61 €, apertura)
- 2026-10-01 02:10 [c_banda_atr] ENTRADA SOL @ 104.4 (22.54 €, apertura)
- 2026-10-01 02:10 [c_banda_atr_evento] ENTRADA SOL @ 104.4 (22.70 €, apertura)
- 2026-10-01 02:10 [estocastico_rebote] ENTRADA SUI @ 1.0407 (22.55 €, apertura)
- 2026-10-01 02:10 [macd_momentum] ENTRADA XLM @ 0.201782 (22.43 €, apertura)
- 2026-10-01 02:10 [macd_sin_salida] ENTRADA XLM @ 0.201782 (22.54 €, apertura)
- 2026-10-01 02:10 [macd_momentum_evento] ENTRADA XLM @ 0.201782 (22.55 €, apertura)
- 2026-10-01 02:10 [macd_momentum] ENTRADA DOGE @ 0.083808 (22.43 €, apertura)
- 2026-10-01 02:10 [macd_sin_salida] ENTRADA DOGE @ 0.083808 (22.54 €, apertura)
- 2026-10-01 02:10 [macd_momentum_evento] ENTRADA DOGE @ 0.083808 (22.55 €, apertura)
- 2026-10-01 02:10 [estocastico_rebote] ENTRADA FET @ 0.2049 (22.55 €, apertura)
- 2026-10-01 02:10 [estocastico_rebote] ENTRADA WLD @ 0.4758 (22.55 €, apertura)
- 2026-10-01 02:15 [macd_momentum] CIERRE KAS take-profit bruto +2.19% neto +1.69%
- 2026-10-01 02:15 [macd_sin_salida] CIERRE KAS take-profit bruto +2.19% neto +1.69%
- 2026-10-01 02:15 [macd_momentum_evento] CIERRE KAS take-profit bruto +2.19% neto +1.69%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
