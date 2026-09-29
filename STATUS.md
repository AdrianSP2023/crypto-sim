# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 11:57 UTC · vueltas 28 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 928.10 € (+0.42%) | 5 | 26 | 80% | +1.300% | +0.200% | +0.016% | +0.23 € |
| reversion_bb | 923.64 € (-0.07%) | 1 | 0 | 0% | -1.500% | -2.600% | -2.784% | -0.60 € |
| ruptura_volumen | 923.60 € (-0.07%) | 18 | 23 | 33% | +0.459% | -0.641% | -0.763% | -2.66 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 924.09 € (-0.02%) | 13 | 9 | 46% | +0.463% | -0.637% | -0.779% | -1.91 € |
| macd_momentum | 917.75 € (-0.70%) | 48 | 40 | 17% | +0.035% | -0.990% | -1.113% | -11.00 € |
| estocastico_rebote | 929.74 € (+0.60%) | 17 | 31 | 82% | +1.234% | +0.134% | -0.014% | +0.53 € |
| ruptura_estricta | 926.75 € (+0.27%) | 2 | 24 | 50% | +0.605% | -0.494% | -0.730% | -0.23 € |
| macd_sin_salida | 928.01 € (+0.41%) | 17 | 35 | 71% | +0.991% | -0.109% | -0.270% | -0.43 € |
| c_banda_atr_tope | 925.16 € (+0.10%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 923.97 € (-0.03%) | 6 | 5 | 17% | +0.212% | -0.888% | -1.018% | -1.23 € |
| c_banda_atr_regimen | 928.10 € (+0.42%) | 5 | 26 | 80% | +1.300% | +0.200% | +0.016% | +0.23 € |
| macd_momentum_regimen | 917.75 € (-0.70%) | 48 | 40 | 17% | +0.035% | -0.990% | -1.113% | -11.00 € |
| ruptura_volumen_regimen | 923.60 € (-0.07%) | 18 | 23 | 33% | +0.459% | -0.641% | -0.763% | -2.66 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 11:55 | ruptura_volumen_regimen | DOGE | timeout | +0.01% | -1.09% | -0.25 |
| 2026-09-29 11:55 | ruptura_volumen_regimen | SUI | timeout | +1.13% | +0.03% | +0.01 |
| 2026-09-29 11:55 | ruptura_volumen_regimen | XRP | timeout | +0.18% | -0.92% | -0.21 |
| 2026-09-29 11:55 | c_banda_atr_regimen | KAS | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 11:55 | macd_sin_salida | POL | take-profit | +2.38% | +1.28% | +0.29 |
| 2026-09-29 11:55 | macd_sin_salida | OP | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 11:55 | macd_sin_salida | ZRO | take-profit | +2.10% | +1.00% | +0.23 |
| 2026-09-29 11:55 | estocastico_rebote | KAS | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 11:55 | estocastico_rebote | PENGU | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-29 11:55 | estocastico_rebote | INJ | take-profit | +1.87% | +0.77% | +0.18 |
| 2026-09-29 11:55 | estocastico_rebote | DOT | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-29 11:55 | pullback_tendencia | FET | take-profit | +2.23% | +1.13% | +0.26 |
| 2026-09-29 11:55 | pullback_tendencia | DOT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 11:55 | pullback_tendencia | UNI | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 11:55 | ruptura_volumen | DOGE | timeout | +0.01% | -1.09% | -0.25 |

## Eventos de la última vuelta

- 2026-09-29 11:50 [ruptura_volumen] ENTRADA BTC @ 74381.7 (23.05 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen_regimen] ENTRADA BTC @ 74381.7 (23.05 €, apertura)
- 2026-09-29 11:55 [ruptura_volumen] CIERRE XRP timeout bruto +0.18% neto -0.92%
- 2026-09-29 11:55 [ruptura_volumen_regimen] CIERRE XRP timeout bruto +0.18% neto -0.92%
- 2026-09-29 11:50 [ruptura_volumen] ENTRADA HBAR @ 0.10521 (23.05 €, apertura)
- 2026-09-29 11:50 [ruptura_estricta] ENTRADA HBAR @ 0.10521 (23.10 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen_regimen] ENTRADA HBAR @ 0.10521 (23.05 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen] ENTRADA ZEC @ 1278.95 (23.05 €, apertura)
- 2026-09-29 11:50 [ruptura_estricta] ENTRADA ZEC @ 1278.95 (23.10 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen_regimen] ENTRADA ZEC @ 1278.95 (23.05 €, apertura)
- 2026-09-29 11:55 [ruptura_volumen] CIERRE SUI timeout bruto +1.13% neto +0.03%
- 2026-09-29 11:55 [ruptura_volumen_regimen] CIERRE SUI timeout bruto +1.13% neto +0.03%
- 2026-09-29 11:50 [ruptura_estricta] ENTRADA XLM @ 0.208191 (23.10 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen] ENTRADA UNI @ 8.1238 (23.05 €, apertura)
- 2026-09-29 11:55 [pullback_tendencia] CIERRE UNI take-profit bruto +2.00% neto +0.90%
- 2026-09-29 11:50 [ruptura_volumen_regimen] ENTRADA UNI @ 8.1238 (23.05 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen] ENTRADA TAO @ 280.115 (23.05 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen_regimen] ENTRADA TAO @ 280.115 (23.05 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen] ENTRADA HYPE @ 78.39 (23.05 €, apertura)
- 2026-09-29 11:50 [ruptura_estricta] ENTRADA HYPE @ 78.39 (23.10 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen_regimen] ENTRADA HYPE @ 78.39 (23.05 €, apertura)
- 2026-09-29 11:55 [ruptura_volumen] CIERRE DOGE timeout bruto +0.01% neto -1.09%
- 2026-09-29 11:55 [ruptura_volumen_regimen] CIERRE DOGE timeout bruto +0.01% neto -1.09%
- 2026-09-29 11:55 [pullback_tendencia] CIERRE DOT take-profit bruto +2.00% neto +0.90%
- 2026-09-29 11:55 [estocastico_rebote] CIERRE DOT take-profit bruto +1.80% neto +0.70%
- 2026-09-29 11:50 [ruptura_volumen] ENTRADA DASH @ 54.7 (23.04 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen_regimen] ENTRADA DASH @ 54.7 (23.04 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen] ENTRADA JUP @ 0.29408 (23.04 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen_regimen] ENTRADA JUP @ 0.29408 (23.04 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen] ENTRADA ICP @ 2.987 (23.04 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen_regimen] ENTRADA ICP @ 2.987 (23.04 €, apertura)
- 2026-09-29 11:55 [estocastico_rebote] CIERRE INJ take-profit bruto +1.87% neto +0.77%
- 2026-09-29 11:55 [macd_sin_salida] CIERRE ZRO take-profit bruto +2.10% neto +1.00%
- 2026-09-29 11:50 [c_banda_atr] ENTRADA VIRTUAL @ 0.7296 (23.13 €, apertura)
- 2026-09-29 11:50 [estocastico_rebote] ENTRADA VIRTUAL @ 0.7296 (23.13 €, apertura)
- 2026-09-29 11:50 [c_banda_atr_regimen] ENTRADA VIRTUAL @ 0.7296 (23.13 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen] ENTRADA PEPE @ 3.8e-06 (23.04 €, apertura)
- 2026-09-29 11:50 [ruptura_volumen_regimen] ENTRADA PEPE @ 3.8e-06 (23.04 €, apertura)
- 2026-09-29 11:50 [ruptura_estricta] ENTRADA USELESS @ 0.21098 (23.10 €, apertura)
- 2026-09-29 11:55 [macd_sin_salida] CIERRE OP take-profit bruto +2.00% neto +0.90%
- 2026-09-29 11:50 [ruptura_volumen] ENTRADA PENGU @ 0.008606 (23.04 €, apertura)
- 2026-09-29 11:55 [estocastico_rebote] CIERRE PENGU take-profit bruto +1.80% neto +0.70%
- 2026-09-29 11:50 [ruptura_volumen_regimen] ENTRADA PENGU @ 0.008606 (23.04 €, apertura)
- 2026-09-29 11:55 [macd_sin_salida] CIERRE POL take-profit bruto +2.38% neto +1.28%
- 2026-09-29 11:50 [macd_momentum] ENTRADA TRUMP @ 1.798 (22.83 €, apertura)
- 2026-09-29 11:50 [macd_momentum_regimen] ENTRADA TRUMP @ 1.798 (22.83 €, apertura)
- 2026-09-29 11:55 [c_banda_atr] CIERRE KAS stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 11:55 [reversion_bb] CIERRE KAS stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 11:55 [estocastico_rebote] CIERRE KAS stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 11:55 [c_banda_atr_regimen] CIERRE KAS stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 11:55 [pullback_tendencia] CIERRE FET take-profit bruto +2.23% neto +1.13%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
