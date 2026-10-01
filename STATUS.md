# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 01:06 UTC · vueltas 84 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.29 € (-2.27%) | 89 | 21 | 26% | -0.301% | -1.095% | -1.222% | -22.34 € |
| reversion_bb | 921.72 € (-0.27%) | 12 | 4 | 42% | +0.121% | -0.979% | -1.107% | -2.72 € |
| ruptura_volumen | 893.28 € (-3.35%) | 117 | 11 | 16% | -0.436% | -1.159% | -1.274% | -30.97 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.16 € (-2.17%) | 75 | 5 | 16% | -0.336% | -1.188% | -1.313% | -20.41 € |
| macd_momentum | 902.03 € (-2.40%) | 138 | 24 | 23% | -0.059% | -0.748% | -0.861% | -23.63 € |
| estocastico_rebote | 903.06 € (-2.29%) | 135 | 17 | 36% | -0.009% | -0.702% | -0.825% | -21.81 € |
| ruptura_estricta | 898.57 € (-2.78%) | 55 | 14 | 16% | -1.004% | -1.984% | -2.128% | -25.12 € |
| macd_sin_salida | 903.59 € (-2.23%) | 97 | 32 | 35% | -0.182% | -0.951% | -1.076% | -21.19 € |
| c_banda_atr_tope | 918.84 € (-0.58%) | 21 | 5 | 29% | -0.083% | -1.183% | -1.319% | -5.73 € |
| ruptura_volumen_tope | 915.03 € (-1.00%) | 33 | 5 | 18% | -0.115% | -1.215% | -1.296% | -9.23 € |
| c_banda_atr_regimen | 907.74 € (-1.79%) | 47 | 9 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.49 € (-1.70%) | 78 | 10 | 24% | -0.062% | -0.896% | -1.021% | -16.08 € |
| ruptura_volumen_regimen | 894.61 € (-3.21%) | 96 | 5 | 14% | -0.572% | -1.344% | -1.466% | -29.50 € |
| c_banda_atr_evento | 909.64 € (-1.58%) | 56 | 21 | 23% | -0.296% | -1.241% | -1.349% | -15.99 € |
| macd_momentum_evento | 907.03 € (-1.86%) | 91 | 24 | 16% | -0.104% | -0.894% | -0.995% | -18.65 € |
| ruptura_volumen_evento | 905.99 € (-1.97%) | 67 | 11 | 13% | -0.293% | -1.187% | -1.277% | -18.26 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-01 01:05 | ruptura_volumen | TRUMP | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-01 01:05 | ruptura_volumen | FIL | timeout | +0.54% | +0.04% | +0.01 |
| 2026-10-01 01:05 | c_banda_atr | LINK | timeout | +0.16% | -0.34% | -0.08 |
| 2026-10-01 01:00 | macd_momentum_evento | ARB | momentum perdido | -0.06% | -0.56% | -0.13 |

## Eventos de la última vuelta

- 2026-10-01 01:00 [macd_momentum] ENTRADA ETH @ 2368.31 (22.52 €, apertura)
- 2026-10-01 01:00 [macd_momentum_regimen] ENTRADA ETH @ 2368.31 (22.71 €, apertura)
- 2026-10-01 01:00 [macd_momentum_evento] ENTRADA ETH @ 2368.31 (22.64 €, apertura)
- 2026-10-01 01:05 [c_banda_atr] CIERRE LINK timeout bruto +0.16% neto -0.34%
- 2026-10-01 01:05 [macd_momentum] CIERRE LINK momentum perdido bruto -0.30% neto -0.80%
- 2026-10-01 01:05 [macd_momentum_regimen] CIERRE LINK momentum perdido bruto -0.30% neto -0.80%
- 2026-10-01 01:05 [c_banda_atr_evento] CIERRE LINK timeout bruto +0.16% neto -0.64%
- 2026-10-01 01:05 [macd_momentum_evento] CIERRE LINK momentum perdido bruto -0.30% neto -0.80%
- 2026-10-01 01:00 [macd_momentum] ENTRADA DOGE @ 0.0834117 (22.52 €, apertura)
- 2026-10-01 01:00 [macd_momentum_regimen] ENTRADA DOGE @ 0.0834117 (22.70 €, apertura)
- 2026-10-01 01:00 [macd_momentum_evento] ENTRADA DOGE @ 0.0834117 (22.64 €, apertura)
- 2026-10-01 01:05 [pullback_tendencia] CIERRE FET take-profit bruto +2.40% neto +1.90%
- 2026-10-01 01:05 [macd_sin_salida] CIERRE FET take-profit bruto +2.40% neto +1.90%
- 2026-10-01 01:05 [ruptura_volumen] CIERRE FIL timeout bruto +0.54% neto +0.04%
- 2026-10-01 01:05 [ruptura_volumen_regimen] CIERRE FIL timeout bruto +0.54% neto +0.04%
- 2026-10-01 01:05 [ruptura_volumen_evento] CIERRE FIL timeout bruto +0.54% neto +0.04%
- 2026-10-01 01:05 [macd_sin_salida] CIERRE VVV stop-loss bruto -1.51% neto -2.01%
- 2026-10-01 01:05 [ruptura_volumen] CIERRE TRUMP timeout bruto +0.00% neto -0.50%
- 2026-10-01 01:05 [ruptura_volumen_regimen] CIERRE TRUMP timeout bruto +0.00% neto -0.50%
- 2026-10-01 01:05 [ruptura_volumen_evento] CIERRE TRUMP timeout bruto +0.00% neto -0.50%
- 2026-10-01 01:00 [macd_momentum] ENTRADA BNB @ 679.43 (22.52 €, apertura)
- 2026-10-01 01:00 [macd_momentum_regimen] ENTRADA BNB @ 679.43 (22.70 €, apertura)
- 2026-10-01 01:00 [macd_momentum_evento] ENTRADA BNB @ 679.43 (22.64 €, apertura)
- 2026-10-01 01:00 [ruptura_volumen] ENTRADA XMR @ 481.1 (22.33 €, apertura)
- 2026-10-01 01:00 [ruptura_estricta] ENTRADA XMR @ 481.1 (22.48 €, apertura)
- 2026-10-01 01:00 [ruptura_volumen_tope] ENTRADA XMR @ 481.1 (22.88 €, apertura)
- 2026-10-01 01:00 [ruptura_volumen_regimen] ENTRADA XMR @ 481.1 (22.37 €, apertura)
- 2026-10-01 01:00 [ruptura_volumen_evento] ENTRADA XMR @ 481.1 (22.65 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
