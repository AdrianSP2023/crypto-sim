# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 12:51 UTC · vueltas 39 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 923.98 € (-0.03%) | 8 | 25 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 917.96 € (-0.68%) | 34 | 19 | 35% | +0.392% | -0.708% | -0.839% | -5.56 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 920.55 € (-0.40%) | 23 | 11 | 39% | +0.379% | -0.721% | -0.825% | -3.83 € |
| macd_momentum | 910.18 € (-1.52%) | 83 | 11 | 17% | +0.031% | -0.783% | -0.902% | -14.98 € |
| estocastico_rebote | 924.52 € (+0.03%) | 24 | 27 | 79% | +1.179% | +0.079% | -0.061% | +0.44 € |
| ruptura_estricta | 921.51 € (-0.30%) | 13 | 19 | 38% | +0.306% | -0.794% | -0.950% | -2.38 € |
| macd_sin_salida | 918.96 € (-0.57%) | 39 | 17 | 46% | +0.571% | -0.467% | -0.588% | -4.21 € |
| c_banda_atr_tope | 924.25 € (+0.00%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 922.45 € (-0.19%) | 10 | 5 | 30% | +0.387% | -0.713% | -0.836% | -1.65 € |
| c_banda_atr_regimen | 923.98 € (-0.03%) | 8 | 25 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| macd_momentum_regimen | 910.18 € (-1.52%) | 83 | 11 | 17% | +0.031% | -0.783% | -0.902% | -14.98 € |
| ruptura_volumen_regimen | 917.96 € (-0.68%) | 34 | 19 | 35% | +0.392% | -0.708% | -0.839% | -5.56 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 12:50 | ruptura_volumen_regimen | AVAX | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 12:50 | macd_momentum_regimen | INJ | momentum perdido | +0.37% | -0.13% | -0.03 |
| 2026-09-29 12:50 | macd_momentum_regimen | LINK | momentum perdido | -0.72% | -1.22% | -0.28 |
| 2026-09-29 12:50 | ruptura_volumen_tope | ATOM | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 12:50 | macd_sin_salida | ASTER | timeout | -0.01% | -0.81% | -0.19 |
| 2026-09-29 12:50 | macd_sin_salida | LTC | timeout | -0.21% | -1.01% | -0.23 |
| 2026-09-29 12:50 | macd_sin_salida | ETH | timeout | +0.51% | -0.29% | -0.07 |
| 2026-09-29 12:50 | ruptura_estricta | TRUMP | timeout | +0.06% | -1.04% | -0.24 |
| 2026-09-29 12:50 | ruptura_estricta | OP | timeout | -0.26% | -1.36% | -0.31 |
| 2026-09-29 12:50 | ruptura_estricta | JUP | timeout | -1.49% | -2.59% | -0.60 |
| 2026-09-29 12:50 | macd_momentum | INJ | momentum perdido | +0.37% | -0.13% | -0.03 |
| 2026-09-29 12:50 | macd_momentum | LINK | momentum perdido | -0.72% | -1.22% | -0.28 |
| 2026-09-29 12:50 | pullback_tendencia | GRT | rotura de tendencia | -0.74% | -1.84% | -0.42 |
| 2026-09-29 12:50 | ruptura_volumen | AVAX | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 12:50 | reversion_bb | HBAR | stop-loss | -1.50% | -2.60% | -0.60 |

## Eventos de la última vuelta

- 2026-09-29 12:50 [macd_momentum] CIERRE LINK momentum perdido bruto -0.72% neto -1.22%
- 2026-09-29 12:50 [macd_momentum_regimen] CIERRE LINK momentum perdido bruto -0.72% neto -1.22%
- 2026-09-29 12:50 [macd_sin_salida] CIERRE ETH timeout bruto +0.51% neto -0.29%
- 2026-09-29 12:50 [reversion_bb] CIERRE HBAR stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 12:50 [macd_sin_salida] CIERRE LTC timeout bruto -0.21% neto -1.01%
- 2026-09-29 12:45 [pullback_tendencia] ENTRADA XLM @ 0.206044 (23.02 €, apertura)
- 2026-09-29 12:50 [ruptura_volumen] CIERRE AVAX stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 12:50 [ruptura_volumen_regimen] CIERRE AVAX stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 12:50 [ruptura_estricta] CIERRE JUP timeout bruto -1.49% neto -2.59%
- 2026-09-29 12:50 [macd_momentum] CIERRE INJ momentum perdido bruto +0.37% neto -0.13%
- 2026-09-29 12:50 [macd_momentum_regimen] CIERRE INJ momentum perdido bruto +0.37% neto -0.13%
- 2026-09-29 12:50 [ruptura_volumen_tope] CIERRE ATOM stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 12:45 [ruptura_estricta] ENTRADA PEPE @ 3.823e-06 (23.06 €, apertura)
- 2026-09-29 12:45 [ruptura_volumen_tope] ENTRADA PEPE @ 3.823e-06 (23.06 €, apertura)
- 2026-09-29 12:50 [ruptura_estricta] CIERRE OP timeout bruto -0.26% neto -1.36%
- 2026-09-29 12:50 [ruptura_estricta] CIERRE TRUMP timeout bruto +0.06% neto -1.04%
- 2026-09-29 12:50 [pullback_tendencia] CIERRE GRT rotura de tendencia bruto -0.74% neto -1.84%
- 2026-09-29 12:50 [macd_sin_salida] CIERRE ASTER timeout bruto -0.01% neto -0.81%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
