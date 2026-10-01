# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 01:11 UTC · vueltas 85 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.57 € (-2.24%) | 90 | 23 | 27% | -0.276% | -1.066% | -1.193% | -22.00 € |
| reversion_bb | 921.76 € (-0.27%) | 12 | 4 | 42% | +0.121% | -0.979% | -1.107% | -2.72 € |
| ruptura_volumen | 893.46 € (-3.33%) | 117 | 11 | 16% | -0.436% | -1.159% | -1.274% | -30.97 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.31 € (-2.16%) | 75 | 6 | 16% | -0.336% | -1.188% | -1.313% | -20.41 € |
| macd_momentum | 902.55 € (-2.35%) | 139 | 25 | 24% | -0.044% | -0.732% | -0.845% | -23.29 € |
| estocastico_rebote | 903.59 € (-2.23%) | 135 | 17 | 36% | -0.009% | -0.702% | -0.825% | -21.81 € |
| ruptura_estricta | 898.88 € (-2.74%) | 55 | 14 | 16% | -1.004% | -1.984% | -2.128% | -25.12 € |
| macd_sin_salida | 904.32 € (-2.16%) | 97 | 33 | 35% | -0.182% | -0.951% | -1.076% | -21.19 € |
| c_banda_atr_tope | 918.83 € (-0.59%) | 21 | 5 | 29% | -0.083% | -1.183% | -1.319% | -5.73 € |
| ruptura_volumen_tope | 915.03 € (-1.00%) | 33 | 5 | 18% | -0.115% | -1.215% | -1.296% | -9.23 € |
| c_banda_atr_regimen | 907.76 € (-1.78%) | 47 | 9 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.78 € (-1.67%) | 78 | 10 | 24% | -0.062% | -0.896% | -1.021% | -16.08 € |
| ruptura_volumen_regimen | 894.72 € (-3.19%) | 96 | 5 | 14% | -0.572% | -1.344% | -1.466% | -29.50 € |
| c_banda_atr_evento | 909.93 € (-1.55%) | 57 | 23 | 25% | -0.256% | -1.193% | -1.302% | -15.65 € |
| macd_momentum_evento | 907.55 € (-1.81%) | 92 | 25 | 17% | -0.081% | -0.868% | -0.969% | -18.31 € |
| ruptura_volumen_evento | 906.17 € (-1.96%) | 67 | 11 | 13% | -0.293% | -1.187% | -1.277% | -18.26 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 01:10 | macd_momentum_evento | FET | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 01:10 | c_banda_atr_evento | FET | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 01:10 | macd_momentum | FET | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 01:10 | c_banda_atr | FET | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 01:05 | ruptura_volumen_evento | TRUMP | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-01 01:05 | ruptura_volumen_evento | FIL | timeout | +0.54% | +0.04% | +0.01 |
| 2026-10-01 01:05 | macd_momentum_evento | LINK | momentum perdido | -0.30% | -0.80% | -0.18 |
| 2026-10-01 01:05 | c_banda_atr_evento | LINK | timeout | +0.16% | -0.64% | -0.15 |
| 2026-10-01 01:05 | ruptura_volumen_regimen | TRUMP | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-01 01:05 | ruptura_volumen_regimen | FIL | timeout | +0.54% | +0.04% | +0.01 |
| 2026-10-01 01:05 | macd_momentum_regimen | LINK | momentum perdido | -0.30% | -0.80% | -0.18 |
| 2026-10-01 01:05 | macd_sin_salida | VVV | stop-loss | -1.51% | -2.01% | -0.45 |
| 2026-10-01 01:05 | macd_sin_salida | FET | take-profit | +2.40% | +1.90% | +0.43 |
| 2026-10-01 01:05 | macd_momentum | LINK | momentum perdido | -0.30% | -0.80% | -0.18 |
| 2026-10-01 01:05 | pullback_tendencia | FET | take-profit | +2.40% | +1.90% | +0.43 |

## Eventos de la última vuelta

- 2026-10-01 01:05 [c_banda_atr] ENTRADA TAO @ 266.121 (22.55 €, apertura)
- 2026-10-01 01:05 [c_banda_atr_evento] ENTRADA TAO @ 266.121 (22.71 €, apertura)
- 2026-10-01 01:10 [c_banda_atr] CIERRE FET take-profit bruto +2.00% neto +1.50%
- 2026-10-01 01:10 [macd_momentum] CIERRE FET take-profit bruto +2.00% neto +1.50%
- 2026-10-01 01:10 [c_banda_atr_evento] CIERRE FET take-profit bruto +2.00% neto +1.50%
- 2026-10-01 01:10 [macd_momentum_evento] CIERRE FET take-profit bruto +2.00% neto +1.50%
- 2026-10-01 01:05 [c_banda_atr] ENTRADA INJ @ 6.536 (22.56 €, apertura)
- 2026-10-01 01:05 [c_banda_atr_evento] ENTRADA INJ @ 6.536 (22.71 €, apertura)
- 2026-10-01 01:05 [macd_momentum] ENTRADA SHIB @ 5.07e-06 (22.52 €, apertura)
- 2026-10-01 01:05 [macd_momentum_evento] ENTRADA SHIB @ 5.07e-06 (22.65 €, apertura)
- 2026-10-01 01:05 [pullback_tendencia] ENTRADA TRUMP @ 1.821 (22.60 €, apertura)
- 2026-10-01 01:05 [macd_momentum] ENTRADA SEI @ 0.0652 (22.52 €, apertura)
- 2026-10-01 01:05 [macd_sin_salida] ENTRADA SEI @ 0.0652 (22.58 €, apertura)
- 2026-10-01 01:05 [macd_momentum_evento] ENTRADA SEI @ 0.0652 (22.65 €, apertura)
- 2026-10-01 01:05 [c_banda_atr] ENTRADA SPX @ 0.3904 (22.56 €, apertura)
- 2026-10-01 01:05 [c_banda_atr_evento] ENTRADA SPX @ 0.3904 (22.71 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
