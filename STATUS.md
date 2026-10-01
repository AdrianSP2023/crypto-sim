# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 02:21 UTC · vueltas 99 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 901.09 € (-2.50%) | 94 | 28 | 27% | -0.278% | -1.055% | -1.181% | -22.75 € |
| reversion_bb | 921.29 € (-0.32%) | 13 | 3 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 891.73 € (-3.52%) | 127 | 15 | 16% | -0.437% | -1.143% | -1.256% | -33.11 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.49 € (-2.24%) | 81 | 3 | 16% | -0.317% | -1.143% | -1.266% | -21.21 € |
| macd_momentum | 897.54 € (-2.89%) | 170 | 9 | 21% | -0.036% | -0.690% | -0.800% | -26.79 € |
| estocastico_rebote | 901.54 € (-2.46%) | 141 | 19 | 36% | -0.012% | -0.697% | -0.819% | -22.59 € |
| ruptura_estricta | 897.57 € (-2.89%) | 61 | 15 | 15% | -0.937% | -1.870% | -2.008% | -26.23 € |
| macd_sin_salida | 901.16 € (-2.50%) | 118 | 19 | 34% | -0.105% | -0.826% | -0.942% | -22.39 € |
| c_banda_atr_tope | 917.53 € (-0.73%) | 23 | 5 | 26% | -0.149% | -1.249% | -1.380% | -6.62 € |
| ruptura_volumen_tope | 915.50 € (-0.95%) | 33 | 5 | 18% | -0.115% | -1.215% | -1.296% | -9.23 € |
| c_banda_atr_regimen | 906.55 € (-1.91%) | 48 | 13 | 23% | -0.511% | -1.555% | -1.710% | -17.17 € |
| macd_momentum_regimen | 905.61 € (-2.02%) | 92 | 2 | 21% | -0.098% | -0.882% | -1.000% | -18.63 € |
| ruptura_volumen_regimen | 892.30 € (-3.46%) | 104 | 10 | 13% | -0.575% | -1.326% | -1.446% | -31.50 € |
| c_banda_atr_evento | 907.29 € (-1.83%) | 61 | 28 | 25% | -0.261% | -1.179% | -1.286% | -16.54 € |
| macd_momentum_evento | 902.51 € (-2.35%) | 123 | 9 | 15% | -0.061% | -0.776% | -0.875% | -21.82 € |
| ruptura_volumen_evento | 904.41 € (-2.15%) | 77 | 15 | 13% | -0.315% | -1.157% | -1.247% | -20.43 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 02:20 | ruptura_volumen_evento | FIL | stop-loss | -1.28% | -1.78% | -0.40 |
| 2026-10-01 02:20 | c_banda_atr_evento | ALGO | timeout | -0.27% | -1.07% | -0.24 |
| 2026-10-01 02:20 | ruptura_volumen_regimen | FIL | stop-loss | -1.28% | -1.78% | -0.40 |
| 2026-10-01 02:20 | estocastico_rebote | HYPE | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 02:20 | ruptura_volumen | FIL | stop-loss | -1.28% | -1.78% | -0.40 |
| 2026-10-01 02:20 | c_banda_atr | ALGO | timeout | -0.27% | -0.77% | -0.17 |
| 2026-10-01 02:15 | macd_momentum_evento | KAS | take-profit | +2.19% | +1.69% | +0.38 |
| 2026-10-01 02:15 | macd_sin_salida | KAS | take-profit | +2.19% | +1.69% | +0.38 |
| 2026-10-01 02:15 | macd_momentum | KAS | take-profit | +2.19% | +1.69% | +0.38 |
| 2026-10-01 02:10 | macd_momentum_evento | CRV | momentum perdido | +0.33% | -0.17% | -0.04 |
| 2026-10-01 02:10 | macd_momentum | CRV | momentum perdido | +0.33% | -0.17% | -0.04 |
| 2026-10-01 02:05 | macd_momentum_evento | RENDER | momentum perdido | -0.06% | -0.56% | -0.13 |
| 2026-10-01 02:05 | macd_momentum_evento | ADA | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-10-01 02:05 | macd_momentum_regimen | RENDER | momentum perdido | -0.06% | -0.56% | -0.13 |
| 2026-10-01 02:05 | c_banda_atr_tope | DASH | timeout | -0.18% | -1.28% | -0.29 |

## Eventos de la última vuelta

- 2026-10-01 02:20 [estocastico_rebote] CIERRE HYPE stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 02:15 [macd_momentum] ENTRADA TAO @ 265.818 (22.44 €, apertura)
- 2026-10-01 02:15 [macd_sin_salida] ENTRADA TAO @ 265.818 (22.55 €, apertura)
- 2026-10-01 02:15 [macd_momentum_evento] ENTRADA TAO @ 265.818 (22.56 €, apertura)
- 2026-10-01 02:20 [c_banda_atr] CIERRE ALGO timeout bruto -0.27% neto -0.77%
- 2026-10-01 02:20 [c_banda_atr_evento] CIERRE ALGO timeout bruto -0.27% neto -1.07%
- 2026-10-01 02:15 [estocastico_rebote] ENTRADA ONDO @ 0.44558 (22.54 €, apertura)
- 2026-10-01 02:15 [macd_momentum] ENTRADA CRV @ 0.35091 (22.44 €, apertura)
- 2026-10-01 02:15 [macd_momentum_evento] ENTRADA CRV @ 0.35091 (22.56 €, apertura)
- 2026-10-01 02:15 [c_banda_atr] ENTRADA PEPE @ 3.791e-06 (22.54 €, apertura)
- 2026-10-01 02:15 [c_banda_atr_evento] ENTRADA PEPE @ 3.791e-06 (22.69 €, apertura)
- 2026-10-01 02:20 [ruptura_volumen] CIERRE FIL stop-loss bruto -1.28% neto -1.78%
- 2026-10-01 02:20 [ruptura_volumen_regimen] CIERRE FIL stop-loss bruto -1.28% neto -1.78%
- 2026-10-01 02:20 [ruptura_volumen_evento] CIERRE FIL stop-loss bruto -1.28% neto -1.78%
- 2026-10-01 02:15 [estocastico_rebote] ENTRADA TRUMP @ 1.817 (22.54 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
