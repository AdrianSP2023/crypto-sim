# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 12:01 UTC · vueltas 29 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 927.83 € (+0.39%) | 6 | 25 | 83% | +1.417% | +0.317% | +0.155% | +0.44 € |
| reversion_bb | 923.64 € (-0.07%) | 1 | 0 | 0% | -1.500% | -2.600% | -2.784% | -0.60 € |
| ruptura_volumen | 922.70 € (-0.17%) | 20 | 26 | 35% | +0.592% | -0.508% | -0.647% | -2.35 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 923.84 € (-0.04%) | 14 | 8 | 50% | +0.573% | -0.527% | -0.662% | -1.71 € |
| macd_momentum | 917.12 € (-0.77%) | 48 | 40 | 17% | +0.035% | -0.990% | -1.113% | -11.00 € |
| estocastico_rebote | 929.46 € (+0.57%) | 17 | 31 | 82% | +1.234% | +0.134% | -0.014% | +0.53 € |
| ruptura_estricta | 926.46 € (+0.24%) | 3 | 26 | 67% | +1.404% | +0.304% | +0.034% | +0.21 € |
| macd_sin_salida | 927.27 € (+0.33%) | 19 | 35 | 74% | +1.097% | -0.003% | -0.155% | -0.01 € |
| c_banda_atr_tope | 925.22 € (+0.11%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 924.06 € (-0.02%) | 6 | 5 | 17% | +0.212% | -0.888% | -1.018% | -1.23 € |
| c_banda_atr_regimen | 927.83 € (+0.39%) | 6 | 25 | 83% | +1.417% | +0.317% | +0.155% | +0.44 € |
| macd_momentum_regimen | 917.12 € (-0.77%) | 48 | 40 | 17% | +0.035% | -0.990% | -1.113% | -11.00 € |
| ruptura_volumen_regimen | 922.70 € (-0.17%) | 20 | 26 | 35% | +0.592% | -0.508% | -0.647% | -2.35 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 12:00 | ruptura_volumen_regimen | RAY | timeout | +1.07% | -0.03% | -0.01 |
| 2026-09-29 12:00 | ruptura_volumen_regimen | PUMP | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 12:00 | c_banda_atr_regimen | AVAX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 12:00 | macd_sin_salida | RENDER | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 12:00 | macd_sin_salida | AVAX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 12:00 | ruptura_estricta | PUMP | take-profit | +3.00% | +1.90% | +0.44 |
| 2026-09-29 12:00 | pullback_tendencia | AVAX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 12:00 | ruptura_volumen | RAY | timeout | +1.07% | -0.03% | -0.01 |
| 2026-09-29 12:00 | ruptura_volumen | PUMP | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 12:00 | c_banda_atr | AVAX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 11:55 | ruptura_volumen_regimen | DOGE | timeout | +0.01% | -1.09% | -0.25 |
| 2026-09-29 11:55 | ruptura_volumen_regimen | SUI | timeout | +1.13% | +0.03% | +0.01 |
| 2026-09-29 11:55 | ruptura_volumen_regimen | XRP | timeout | +0.18% | -0.92% | -0.21 |
| 2026-09-29 11:55 | c_banda_atr_regimen | KAS | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 11:55 | macd_sin_salida | POL | take-profit | +2.38% | +1.28% | +0.29 |

## Eventos de la última vuelta

- 2026-09-29 11:55 [ruptura_volumen] ENTRADA ETH @ 2408.61 (23.04 €, apertura)
- 2026-09-29 11:55 [ruptura_estricta] ENTRADA ETH @ 2408.61 (23.10 €, apertura)
- 2026-09-29 11:55 [ruptura_volumen_regimen] ENTRADA ETH @ 2408.61 (23.04 €, apertura)
- 2026-09-29 11:55 [ruptura_volumen] ENTRADA SOL @ 105.91 (23.04 €, apertura)
- 2026-09-29 11:55 [ruptura_estricta] ENTRADA SOL @ 105.91 (23.10 €, apertura)
- 2026-09-29 11:55 [ruptura_volumen_regimen] ENTRADA SOL @ 105.91 (23.04 €, apertura)
- 2026-09-29 12:00 [c_banda_atr] CIERRE AVAX take-profit bruto +2.00% neto +0.90%
- 2026-09-29 12:00 [pullback_tendencia] CIERRE AVAX take-profit bruto +2.00% neto +0.90%
- 2026-09-29 12:00 [macd_sin_salida] CIERRE AVAX take-profit bruto +2.00% neto +0.90%
- 2026-09-29 12:00 [c_banda_atr_regimen] CIERRE AVAX take-profit bruto +2.00% neto +0.90%
- 2026-09-29 12:00 [ruptura_volumen] CIERRE PUMP take-profit bruto +2.50% neto +1.40%
- 2026-09-29 12:00 [ruptura_estricta] CIERRE PUMP take-profit bruto +3.00% neto +1.90%
- 2026-09-29 12:00 [ruptura_volumen_regimen] CIERRE PUMP take-profit bruto +2.50% neto +1.40%
- 2026-09-29 11:55 [ruptura_volumen] ENTRADA XDC @ 0.03278 (23.05 €, apertura)
- 2026-09-29 11:55 [macd_sin_salida] ENTRADA XDC @ 0.03278 (23.10 €, apertura)
- 2026-09-29 11:55 [ruptura_volumen_regimen] ENTRADA XDC @ 0.03278 (23.05 €, apertura)
- 2026-09-29 11:55 [macd_sin_salida] ENTRADA TRX @ 0.295649 (23.10 €, apertura)
- 2026-09-29 12:00 [macd_sin_salida] CIERRE RENDER take-profit bruto +2.00% neto +0.90%
- 2026-09-29 12:00 [ruptura_volumen] CIERRE RAY timeout bruto +1.07% neto -0.03%
- 2026-09-29 12:00 [ruptura_volumen_regimen] CIERRE RAY timeout bruto +1.07% neto -0.03%
- 2026-09-29 11:55 [ruptura_volumen] ENTRADA OP @ 0.1192 (23.05 €, apertura)
- 2026-09-29 11:55 [ruptura_volumen_regimen] ENTRADA OP @ 0.1192 (23.05 €, apertura)
- 2026-09-29 11:55 [ruptura_estricta] ENTRADA PENGU @ 0.008665 (23.11 €, apertura)
- 2026-09-29 11:55 [ruptura_volumen] ENTRADA SPX @ 0.3682 (23.05 €, apertura)
- 2026-09-29 11:55 [ruptura_volumen_regimen] ENTRADA SPX @ 0.3682 (23.05 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
