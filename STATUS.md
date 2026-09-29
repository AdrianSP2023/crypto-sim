# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 11:46 UTC · vueltas 26 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 926.71 € (+0.27%) | 3 | 27 | 100% | +2.000% | +0.900% | +0.736% | +0.62 € |
| reversion_bb | 924.35 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen | 923.49 € (-0.08%) | 10 | 14 | 20% | +0.013% | -1.087% | -1.222% | -2.51 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 924.30 € (+0.01%) | 8 | 14 | 12% | -0.526% | -1.626% | -1.761% | -3.00 € |
| macd_momentum | 914.97 € (-1.00%) | 44 | 40 | 9% | -0.144% | -1.210% | -1.332% | -12.30 € |
| estocastico_rebote | 930.06 € (+0.63%) | 7 | 40 | 86% | +1.358% | +0.258% | +0.110% | +0.42 € |
| ruptura_estricta | 924.89 € (+0.07%) | 2 | 17 | 50% | +0.605% | -0.494% | -0.730% | -0.23 € |
| macd_sin_salida | 926.07 € (+0.20%) | 10 | 40 | 50% | +0.236% | -0.864% | -1.057% | -2.00 € |
| c_banda_atr_tope | 924.50 € (+0.03%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 923.21 € (-0.11%) | 6 | 5 | 17% | +0.212% | -0.888% | -1.018% | -1.23 € |
| c_banda_atr_regimen | 926.71 € (+0.27%) | 3 | 27 | 100% | +2.000% | +0.900% | +0.736% | +0.62 € |
| macd_momentum_regimen | 914.97 € (-1.00%) | 44 | 40 | 9% | -0.144% | -1.210% | -1.332% | -12.30 € |
| ruptura_volumen_regimen | 923.49 € (-0.08%) | 10 | 14 | 20% | +0.013% | -1.087% | -1.222% | -2.51 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 11:45 | ruptura_volumen_regimen | FIL | timeout | +0.53% | -0.57% | -0.13 |
| 2026-09-29 11:45 | ruptura_volumen_regimen | MON | timeout | -0.20% | -1.30% | -0.30 |
| 2026-09-29 11:45 | macd_momentum_regimen | ARB | take-profit | +2.05% | +1.55% | +0.35 |
| 2026-09-29 11:45 | c_banda_atr_regimen | XLM | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 11:45 | ruptura_volumen_tope | FIL | timeout | +0.53% | -0.57% | -0.13 |
| 2026-09-29 11:45 | ruptura_volumen_tope | MON | timeout | -0.20% | -1.30% | -0.30 |
| 2026-09-29 11:45 | macd_momentum | ARB | take-profit | +2.05% | +1.55% | +0.35 |
| 2026-09-29 11:45 | ruptura_volumen | FIL | timeout | +0.53% | -0.57% | -0.13 |
| 2026-09-29 11:45 | ruptura_volumen | MON | timeout | -0.20% | -1.30% | -0.30 |
| 2026-09-29 11:45 | c_banda_atr | XLM | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 11:40 | ruptura_volumen_regimen | FET | timeout | +0.92% | -0.18% | -0.04 |
| 2026-09-29 11:40 | ruptura_volumen_regimen | ARB | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 11:40 | ruptura_volumen_tope | FET | timeout | +0.92% | -0.18% | -0.04 |
| 2026-09-29 11:40 | ruptura_volumen_tope | ARB | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 11:40 | estocastico_rebote | POL | take-profit | +2.00% | +0.90% | +0.21 |

## Eventos de la última vuelta

- 2026-09-29 11:40 [macd_momentum] ENTRADA SOL @ 105.52 (22.79 €, apertura)
- 2026-09-29 11:40 [macd_momentum_regimen] ENTRADA SOL @ 105.52 (22.79 €, apertura)
- 2026-09-29 11:40 [ruptura_estricta] ENTRADA NEAR @ 4.2757 (23.10 €, apertura)
- 2026-09-29 11:40 [ruptura_volumen_tope] ENTRADA NEAR @ 4.2757 (23.09 €, apertura)
- 2026-09-29 11:45 [c_banda_atr] CIERRE XLM take-profit bruto +2.00% neto +0.90%
- 2026-09-29 11:45 [c_banda_atr_regimen] CIERRE XLM take-profit bruto +2.00% neto +0.90%
- 2026-09-29 11:40 [macd_momentum] ENTRADA AVAX @ 10.338 (22.79 €, apertura)
- 2026-09-29 11:40 [macd_momentum_regimen] ENTRADA AVAX @ 10.338 (22.79 €, apertura)
- 2026-09-29 11:45 [macd_momentum] CIERRE ARB take-profit bruto +2.05% neto +1.55%
- 2026-09-29 11:45 [macd_momentum_regimen] CIERRE ARB take-profit bruto +2.05% neto +1.55%
- 2026-09-29 11:40 [macd_momentum] ENTRADA DOGE @ 0.0841602 (22.80 €, apertura)
- 2026-09-29 11:40 [macd_momentum_regimen] ENTRADA DOGE @ 0.0841602 (22.80 €, apertura)
- 2026-09-29 11:40 [macd_momentum] ENTRADA DOT @ 1.074 (22.80 €, apertura)
- 2026-09-29 11:40 [macd_momentum_regimen] ENTRADA DOT @ 1.074 (22.80 €, apertura)
- 2026-09-29 11:40 [macd_momentum] ENTRADA JUP @ 0.29213 (22.80 €, apertura)
- 2026-09-29 11:40 [macd_momentum_regimen] ENTRADA JUP @ 0.29213 (22.80 €, apertura)
- 2026-09-29 11:45 [ruptura_volumen] CIERRE MON timeout bruto -0.20% neto -1.30%
- 2026-09-29 11:45 [ruptura_volumen_tope] CIERRE MON timeout bruto -0.20% neto -1.30%
- 2026-09-29 11:45 [ruptura_volumen_regimen] CIERRE MON timeout bruto -0.20% neto -1.30%
- 2026-09-29 11:40 [macd_momentum] ENTRADA BCH @ 275.7 (22.80 €, apertura)
- 2026-09-29 11:40 [macd_momentum_regimen] ENTRADA BCH @ 275.7 (22.80 €, apertura)
- 2026-09-29 11:40 [macd_momentum] ENTRADA INJ @ 6.742 (22.80 €, apertura)
- 2026-09-29 11:40 [macd_momentum_regimen] ENTRADA INJ @ 6.742 (22.80 €, apertura)
- 2026-09-29 11:40 [ruptura_estricta] ENTRADA ATOM @ 1.572 (23.10 €, apertura)
- 2026-09-29 11:40 [ruptura_volumen_tope] ENTRADA ATOM @ 1.572 (23.08 €, apertura)
- 2026-09-29 11:40 [macd_momentum] ENTRADA PEPE @ 3.779e-06 (22.80 €, apertura)
- 2026-09-29 11:40 [macd_momentum_regimen] ENTRADA PEPE @ 3.779e-06 (22.80 €, apertura)
- 2026-09-29 11:45 [ruptura_volumen] CIERRE FIL timeout bruto +0.53% neto -0.57%
- 2026-09-29 11:45 [ruptura_volumen_tope] CIERRE FIL timeout bruto +0.53% neto -0.57%
- 2026-09-29 11:45 [ruptura_volumen_regimen] CIERRE FIL timeout bruto +0.53% neto -0.57%
- 2026-09-29 11:40 [macd_momentum] ENTRADA PENGU @ 0.008507 (22.80 €, apertura)
- 2026-09-29 11:40 [macd_momentum_regimen] ENTRADA PENGU @ 0.008507 (22.80 €, apertura)
- 2026-09-29 11:40 [c_banda_atr] ENTRADA TRUMP @ 1.786 (23.12 €, apertura)
- 2026-09-29 11:40 [c_banda_atr_regimen] ENTRADA TRUMP @ 1.786 (23.12 €, apertura)
- 2026-09-29 11:40 [ruptura_volumen] ENTRADA XPL @ 0.0889 (23.04 €, apertura)
- 2026-09-29 11:40 [ruptura_volumen_tope] ENTRADA XPL @ 0.0889 (23.08 €, apertura)
- 2026-09-29 11:40 [ruptura_volumen_regimen] ENTRADA XPL @ 0.0889 (23.04 €, apertura)
- 2026-09-29 11:40 [c_banda_atr] ENTRADA KAS @ 0.04075 (23.12 €, apertura)
- 2026-09-29 11:40 [c_banda_atr_regimen] ENTRADA KAS @ 0.04075 (23.12 €, apertura)
- 2026-09-29 11:40 [macd_momentum] ENTRADA FET @ 0.2095 (22.80 €, apertura)
- 2026-09-29 11:40 [macd_momentum_regimen] ENTRADA FET @ 0.2095 (22.80 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
