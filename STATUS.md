# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 23:21 UTC · vueltas 105 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 905.89 € (-1.99%) | 70 | 31 | 26% | -0.419% | -1.292% | -1.435% | -20.77 € |
| reversion_bb | 921.94 € (-0.25%) | 10 | 4 | 40% | -0.070% | -1.170% | -1.296% | -2.71 € |
| ruptura_volumen | 895.79 € (-3.08%) | 94 | 21 | 16% | -0.513% | -1.290% | -1.426% | -27.77 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.58 € (-2.13%) | 66 | 2 | 15% | -0.407% | -1.307% | -1.444% | -19.77 € |
| macd_momentum | 905.09 € (-2.07%) | 108 | 26 | 23% | -0.104% | -0.846% | -0.975% | -20.95 € |
| estocastico_rebote | 903.34 € (-2.26%) | 127 | 8 | 35% | -0.037% | -0.743% | -0.875% | -21.70 € |
| ruptura_estricta | 898.50 € (-2.78%) | 50 | 10 | 12% | -1.227% | -2.255% | -2.403% | -25.93 € |
| macd_sin_salida | 905.13 € (-2.07%) | 83 | 32 | 33% | -0.256% | -1.071% | -1.202% | -20.44 € |
| c_banda_atr_tope | 919.60 € (-0.50%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.258% | -5.10 € |
| ruptura_volumen_tope | 915.99 € (-0.89%) | 27 | 5 | 19% | -0.185% | -1.285% | -1.398% | -8.00 € |
| c_banda_atr_regimen | 908.40 € (-1.71%) | 45 | 6 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 910.83 € (-1.45%) | 62 | 13 | 29% | -0.036% | -0.957% | -1.095% | -13.68 € |
| ruptura_volumen_regimen | 897.25 € (-2.92%) | 73 | 21 | 12% | -0.720% | -1.577% | -1.716% | -26.39 € |
| c_banda_atr_evento | 913.37 € (-1.18%) | 37 | 31 | 22% | -0.517% | -1.560% | -1.687% | -13.30 € |
| macd_momentum_evento | 910.17 € (-1.52%) | 61 | 26 | 15% | -0.207% | -1.135% | -1.256% | -15.88 € |
| ruptura_volumen_evento | 908.67 € (-1.68%) | 44 | 21 | 11% | -0.383% | -1.469% | -1.589% | -14.88 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 23:20 | macd_momentum_evento | INJ | momentum perdido | -0.52% | -1.02% | -0.23 |
| 2026-09-30 23:20 | macd_momentum_evento | PUMP | momentum perdido | -0.89% | -1.39% | -0.32 |
| 2026-09-30 23:20 | macd_momentum_regimen | PUMP | momentum perdido | -0.89% | -1.39% | -0.32 |
| 2026-09-30 23:20 | macd_sin_salida | UNI | timeout | +0.06% | -0.44% | -0.10 |
| 2026-09-30 23:20 | macd_momentum | INJ | momentum perdido | -0.52% | -1.02% | -0.23 |
| 2026-09-30 23:20 | macd_momentum | PUMP | momentum perdido | -0.89% | -1.39% | -0.32 |
| 2026-09-30 23:20 | reversion_bb | ASTER | timeout | +0.80% | -0.30% | -0.07 |
| 2026-09-30 23:15 | macd_momentum_evento | SEI | momentum perdido | +0.17% | -0.33% | -0.07 |
| 2026-09-30 23:15 | macd_momentum_evento | TON | momentum perdido | -1.04% | -1.54% | -0.35 |
| 2026-09-30 23:15 | macd_momentum_evento | VVV | momentum perdido | -0.46% | -0.96% | -0.22 |
| 2026-09-30 23:15 | macd_momentum_evento | CRV | momentum perdido | -0.59% | -1.09% | -0.25 |
| 2026-09-30 23:15 | c_banda_atr_evento | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 23:15 | macd_momentum_regimen | TON | momentum perdido | -1.04% | -1.54% | -0.35 |
| 2026-09-30 23:15 | macd_momentum | SEI | momentum perdido | +0.17% | -0.33% | -0.07 |
| 2026-09-30 23:15 | macd_momentum | TON | momentum perdido | -1.04% | -1.54% | -0.35 |

## Eventos de la última vuelta

- 2026-09-30 23:20 [macd_momentum] CIERRE PUMP momentum perdido bruto -0.89% neto -1.39%
- 2026-09-30 23:20 [macd_momentum_regimen] CIERRE PUMP momentum perdido bruto -0.89% neto -1.39%
- 2026-09-30 23:20 [macd_momentum_evento] CIERRE PUMP momentum perdido bruto -0.89% neto -1.39%
- 2026-09-30 23:20 [macd_sin_salida] CIERRE UNI timeout bruto +0.06% neto -0.44%
- 2026-09-30 23:20 [macd_momentum] CIERRE INJ momentum perdido bruto -0.52% neto -1.02%
- 2026-09-30 23:20 [macd_momentum_evento] CIERRE INJ momentum perdido bruto -0.52% neto -1.02%
- 2026-09-30 23:20 [reversion_bb] CIERRE ASTER timeout bruto +0.80% neto -0.30%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
