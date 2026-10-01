# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 01:16 UTC · vueltas 86 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.88 € (-2.20%) | 90 | 24 | 27% | -0.276% | -1.066% | -1.193% | -22.00 € |
| reversion_bb | 921.76 € (-0.27%) | 12 | 4 | 42% | +0.121% | -0.979% | -1.107% | -2.72 € |
| ruptura_volumen | 893.76 € (-3.30%) | 117 | 14 | 16% | -0.436% | -1.159% | -1.274% | -30.97 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.64 € (-2.12%) | 75 | 7 | 16% | -0.336% | -1.188% | -1.313% | -20.41 € |
| macd_momentum | 903.34 € (-2.26%) | 139 | 30 | 24% | -0.044% | -0.732% | -0.845% | -23.29 € |
| estocastico_rebote | 903.38 € (-2.26%) | 137 | 15 | 36% | +0.008% | -0.683% | -0.806% | -21.52 € |
| ruptura_estricta | 899.02 € (-2.73%) | 56 | 13 | 16% | -1.018% | -1.989% | -2.131% | -25.63 € |
| macd_sin_salida | 904.99 € (-2.08%) | 97 | 33 | 35% | -0.182% | -0.951% | -1.076% | -21.19 € |
| c_banda_atr_tope | 918.70 € (-0.60%) | 21 | 5 | 29% | -0.083% | -1.183% | -1.319% | -5.73 € |
| ruptura_volumen_tope | 915.10 € (-0.99%) | 33 | 5 | 18% | -0.115% | -1.215% | -1.296% | -9.23 € |
| c_banda_atr_regimen | 907.79 € (-1.78%) | 47 | 9 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.87 € (-1.66%) | 78 | 10 | 24% | -0.062% | -0.896% | -1.021% | -16.08 € |
| ruptura_volumen_regimen | 894.92 € (-3.17%) | 96 | 5 | 14% | -0.572% | -1.344% | -1.466% | -29.50 € |
| c_banda_atr_evento | 910.24 € (-1.52%) | 57 | 24 | 25% | -0.256% | -1.193% | -1.302% | -15.65 € |
| macd_momentum_evento | 908.34 € (-1.72%) | 92 | 30 | 17% | -0.081% | -0.868% | -0.969% | -18.31 € |
| ruptura_volumen_evento | 906.47 € (-1.92%) | 67 | 14 | 13% | -0.293% | -1.187% | -1.277% | -18.26 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 01:15 | ruptura_estricta | ZRO | timeout | -1.76% | -2.26% | -0.51 |
| 2026-10-01 01:15 | estocastico_rebote | BNB | timeout | +0.51% | +0.01% | +0.00 |
| 2026-10-01 01:15 | estocastico_rebote | KSM | timeout | +1.77% | +1.27% | +0.29 |
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

## Eventos de la última vuelta

- 2026-10-01 01:10 [pullback_tendencia] ENTRADA LINK @ 12.6883 (22.60 €, apertura)
- 2026-10-01 01:10 [macd_momentum] ENTRADA ADA @ 0.218397 (22.52 €, apertura)
- 2026-10-01 01:10 [macd_momentum_evento] ENTRADA ADA @ 0.218397 (22.65 €, apertura)
- 2026-10-01 01:10 [c_banda_atr] ENTRADA HBAR @ 0.09216 (22.56 €, apertura)
- 2026-10-01 01:10 [c_banda_atr_evento] ENTRADA HBAR @ 0.09216 (22.71 €, apertura)
- 2026-10-01 01:10 [macd_momentum] ENTRADA AAVE @ 140.94 (22.52 €, apertura)
- 2026-10-01 01:10 [macd_momentum_evento] ENTRADA AAVE @ 140.94 (22.65 €, apertura)
- 2026-10-01 01:10 [macd_momentum] ENTRADA LTC @ 59.5 (22.52 €, apertura)
- 2026-10-01 01:10 [macd_momentum_evento] ENTRADA LTC @ 59.5 (22.65 €, apertura)
- 2026-10-01 01:15 [ruptura_estricta] CIERRE ZRO timeout bruto -1.76% neto -2.26%
- 2026-10-01 01:10 [macd_momentum] ENTRADA ARB @ 0.1792 (22.52 €, apertura)
- 2026-10-01 01:10 [macd_momentum_evento] ENTRADA ARB @ 0.1792 (22.65 €, apertura)
- 2026-10-01 01:10 [ruptura_volumen] ENTRADA ICP @ 2.952 (22.33 €, apertura)
- 2026-10-01 01:10 [ruptura_volumen_evento] ENTRADA ICP @ 2.952 (22.65 €, apertura)
- 2026-10-01 01:10 [ruptura_volumen] ENTRADA BCH @ 270.82 (22.33 €, apertura)
- 2026-10-01 01:10 [ruptura_volumen_evento] ENTRADA BCH @ 270.82 (22.65 €, apertura)
- 2026-10-01 01:10 [ruptura_volumen] ENTRADA RENDER @ 1.691 (22.33 €, apertura)
- 2026-10-01 01:10 [ruptura_volumen_evento] ENTRADA RENDER @ 1.691 (22.65 €, apertura)
- 2026-10-01 01:15 [estocastico_rebote] CIERRE KSM timeout bruto +1.77% neto +1.27%
- 2026-10-01 01:15 [estocastico_rebote] CIERRE BNB timeout bruto +0.51% neto +0.01%
- 2026-10-01 01:10 [macd_momentum] ENTRADA SPX @ 0.3919 (22.52 €, apertura)
- 2026-10-01 01:10 [macd_momentum_evento] ENTRADA SPX @ 0.3919 (22.65 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
