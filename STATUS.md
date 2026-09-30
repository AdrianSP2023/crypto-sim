# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 23:31 UTC · vueltas 107 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.08 € (-1.96%) | 71 | 31 | 27% | -0.390% | -1.258% | -1.400% | -20.51 € |
| reversion_bb | 921.98 € (-0.24%) | 10 | 4 | 40% | -0.070% | -1.170% | -1.296% | -2.71 € |
| ruptura_volumen | 895.81 € (-3.08%) | 95 | 24 | 17% | -0.481% | -1.256% | -1.391% | -27.32 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.44 € (-2.14%) | 66 | 5 | 15% | -0.407% | -1.307% | -1.444% | -19.77 € |
| macd_momentum | 905.11 € (-2.07%) | 110 | 25 | 24% | -0.084% | -0.822% | -0.950% | -20.72 € |
| estocastico_rebote | 903.28 € (-2.27%) | 127 | 8 | 35% | -0.037% | -0.743% | -0.875% | -21.70 € |
| ruptura_estricta | 898.34 € (-2.80%) | 51 | 9 | 12% | -1.194% | -2.211% | -2.360% | -25.94 € |
| macd_sin_salida | 904.51 € (-2.14%) | 88 | 28 | 33% | -0.217% | -1.013% | -1.141% | -20.50 € |
| c_banda_atr_tope | 919.49 € (-0.51%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.258% | -5.10 € |
| ruptura_volumen_tope | 916.07 € (-0.88%) | 27 | 5 | 19% | -0.185% | -1.285% | -1.398% | -8.00 € |
| c_banda_atr_regimen | 908.25 € (-1.73%) | 45 | 9 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 910.78 € (-1.46%) | 63 | 13 | 30% | -0.004% | -0.918% | -1.055% | -13.33 € |
| ruptura_volumen_regimen | 897.24 € (-2.92%) | 74 | 22 | 14% | -0.676% | -1.529% | -1.667% | -25.94 € |
| c_banda_atr_evento | 913.50 € (-1.16%) | 38 | 31 | 24% | -0.461% | -1.498% | -1.623% | -13.11 € |
| macd_momentum_evento | 910.19 € (-1.52%) | 63 | 25 | 16% | -0.169% | -1.083% | -1.204% | -15.65 € |
| ruptura_volumen_evento | 908.69 € (-1.68%) | 45 | 24 | 13% | -0.319% | -1.392% | -1.511% | -14.42 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 23:30 | macd_momentum_evento | FET | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-09-30 23:30 | macd_sin_salida | ALGO | timeout | -0.43% | -0.93% | -0.21 |
| 2026-09-30 23:30 | macd_momentum | FET | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-09-30 23:25 | ruptura_volumen_evento | MON | take-profit | +2.50% | +2.00% | +0.46 |
| 2026-09-30 23:25 | macd_momentum_evento | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 23:25 | c_banda_atr_evento | ASTER | timeout | +1.62% | +0.82% | +0.19 |
| 2026-09-30 23:25 | ruptura_volumen_regimen | MON | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 23:25 | macd_momentum_regimen | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 23:25 | macd_sin_salida | TON | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 23:25 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 23:25 | macd_sin_salida | POL | timeout | +1.75% | +1.25% | +0.28 |
| 2026-09-30 23:25 | macd_sin_salida | LINK | timeout | +0.40% | -0.10% | -0.02 |
| 2026-09-30 23:25 | ruptura_estricta | XDC | timeout | +0.46% | -0.04% | -0.01 |
| 2026-09-30 23:25 | macd_momentum | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 23:25 | ruptura_volumen | MON | take-profit | +2.50% | +2.00% | +0.45 |

## Eventos de la última vuelta

- 2026-09-30 23:25 [macd_momentum_regimen] ENTRADA ETH @ 2373.74 (22.77 €, apertura)
- 2026-09-30 23:25 [pullback_tendencia] ENTRADA NEAR @ 4.7397 (22.61 €, apertura)
- 2026-09-30 23:25 [ruptura_volumen] ENTRADA AVAX @ 9.704 (22.42 €, apertura)
- 2026-09-30 23:25 [ruptura_volumen_regimen] ENTRADA AVAX @ 9.704 (22.46 €, apertura)
- 2026-09-30 23:25 [ruptura_volumen_evento] ENTRADA AVAX @ 9.704 (22.75 €, apertura)
- 2026-09-30 23:25 [pullback_tendencia] ENTRADA ZRO @ 1.545 (22.61 €, apertura)
- 2026-09-30 23:25 [c_banda_atr] ENTRADA DOGE @ 0.0835384 (22.59 €, apertura)
- 2026-09-30 23:25 [c_banda_atr_regimen] ENTRADA DOGE @ 0.0835384 (22.71 €, apertura)
- 2026-09-30 23:25 [c_banda_atr_evento] ENTRADA DOGE @ 0.0835384 (22.78 €, apertura)
- 2026-09-30 23:30 [macd_momentum] CIERRE FET momentum perdido bruto +0.00% neto -0.50%
- 2026-09-30 23:30 [macd_momentum_evento] CIERRE FET momentum perdido bruto +0.00% neto -0.50%
- 2026-09-30 23:30 [macd_sin_salida] CIERRE ALGO timeout bruto -0.43% neto -0.93%
- 2026-09-30 23:25 [c_banda_atr_regimen] ENTRADA USELESS @ 0.21373 (22.71 €, apertura)
- 2026-09-30 23:25 [ruptura_volumen] ENTRADA JUP @ 0.2925 (22.42 €, apertura)
- 2026-09-30 23:25 [ruptura_volumen_regimen] ENTRADA JUP @ 0.2925 (22.46 €, apertura)
- 2026-09-30 23:25 [ruptura_volumen_evento] ENTRADA JUP @ 0.2925 (22.75 €, apertura)
- 2026-09-30 23:25 [c_banda_atr_regimen] ENTRADA SHIB @ 5.096e-06 (22.71 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
