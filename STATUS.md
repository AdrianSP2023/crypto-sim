# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 14:37 UTC · vueltas 59 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 918.44 € (-0.63%) | 27 | 22 | 44% | +0.137% | -0.963% | -1.100% | -6.01 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 913.88 € (-1.12%) | 55 | 7 | 29% | +0.112% | -0.857% | -0.987% | -10.86 € |
| rebote_extremo | 924.38 € (+0.02%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 915.68 € (-0.93%) | 44 | 10 | 32% | +0.180% | -0.886% | -0.991% | -8.98 € |
| macd_momentum | 905.84 € (-1.99%) | 120 | 11 | 21% | +0.035% | -0.682% | -0.798% | -18.81 € |
| estocastico_rebote | 920.89 € (-0.36%) | 55 | 35 | 53% | +0.575% | -0.355% | -0.481% | -4.51 € |
| ruptura_estricta | 919.31 € (-0.53%) | 27 | 11 | 37% | +0.208% | -0.892% | -1.023% | -5.56 € |
| macd_sin_salida | 915.79 € (-0.91%) | 64 | 21 | 39% | +0.302% | -0.592% | -0.715% | -8.70 € |
| c_banda_atr_tope | 920.24 € (-0.43%) | 11 | 5 | 27% | -0.397% | -1.497% | -1.686% | -3.80 € |
| ruptura_volumen_tope | 922.14 € (-0.23%) | 14 | 5 | 21% | +0.267% | -0.833% | -0.958% | -2.69 € |
| c_banda_atr_regimen | 918.44 € (-0.63%) | 27 | 22 | 44% | +0.137% | -0.963% | -1.100% | -6.01 € |
| macd_momentum_regimen | 905.84 € (-1.99%) | 120 | 11 | 21% | +0.035% | -0.682% | -0.798% | -18.81 € |
| ruptura_volumen_regimen | 913.88 € (-1.12%) | 55 | 7 | 29% | +0.112% | -0.857% | -0.987% | -10.86 € |
| c_banda_atr_evento | 924.16 € (-0.01%) | 0 | 13 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 924.70 € (+0.05%) | 0 | 11 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen_evento | 924.15 € (-0.01%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 14:35 | ruptura_volumen_regimen | XRP | timeout | +0.95% | +0.15% | +0.04 |
| 2026-09-29 14:35 | c_banda_atr_regimen | OP | take-profit | +2.22% | +1.12% | +0.26 |
| 2026-09-29 14:35 | ruptura_volumen_tope | XRP | timeout | +0.95% | -0.15% | -0.04 |
| 2026-09-29 14:35 | macd_sin_salida | AAVE | timeout | +1.77% | +0.97% | +0.23 |
| 2026-09-29 14:35 | macd_sin_salida | ADA | timeout | -0.21% | -1.01% | -0.23 |
| 2026-09-29 14:35 | ruptura_estricta | AAVE | timeout | +1.77% | +0.67% | +0.16 |
| 2026-09-29 14:35 | estocastico_rebote | XPL | timeout | +0.11% | -0.69% | -0.16 |
| 2026-09-29 14:35 | pullback_tendencia | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:35 | ruptura_volumen | XRP | timeout | +0.95% | +0.15% | +0.04 |
| 2026-09-29 14:35 | c_banda_atr | OP | take-profit | +2.22% | +1.12% | +0.26 |
| 2026-09-29 14:30 | macd_momentum_regimen | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:30 | macd_sin_salida | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:30 | estocastico_rebote | RAY | timeout | +0.94% | +0.14% | +0.03 |
| 2026-09-29 14:30 | macd_momentum | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:25 | macd_momentum_regimen | ASTER | momentum perdido | -0.60% | -1.10% | -0.25 |

## Eventos de la última vuelta

- 2026-09-29 14:35 [ruptura_volumen] CIERRE XRP timeout bruto +0.95% neto +0.15%
- 2026-09-29 14:35 [ruptura_volumen_tope] CIERRE XRP timeout bruto +0.95% neto -0.15%
- 2026-09-29 14:35 [ruptura_volumen_regimen] CIERRE XRP timeout bruto +0.95% neto +0.15%
- 2026-09-29 14:35 [macd_sin_salida] CIERRE ADA timeout bruto -0.21% neto -1.01%
- 2026-09-29 14:30 [c_banda_atr_tope] ENTRADA LTC @ 60.3 (23.01 €, apertura)
- 2026-09-29 14:30 [c_banda_atr_evento] ENTRADA LTC @ 60.3 (23.11 €, apertura)
- 2026-09-29 14:35 [ruptura_estricta] CIERRE AAVE timeout bruto +1.77% neto +0.67%
- 2026-09-29 14:35 [macd_sin_salida] CIERRE AAVE timeout bruto +1.77% neto +0.97%
- 2026-09-29 14:30 [macd_momentum] ENTRADA TAO @ 277.255 (22.64 €, apertura)
- 2026-09-29 14:30 [macd_sin_salida] ENTRADA TAO @ 277.255 (22.89 €, apertura)
- 2026-09-29 14:30 [macd_momentum_regimen] ENTRADA TAO @ 277.255 (22.64 €, apertura)
- 2026-09-29 14:30 [macd_momentum_evento] ENTRADA TAO @ 277.255 (23.11 €, apertura)
- 2026-09-29 14:30 [macd_momentum] ENTRADA DOT @ 1.0696 (22.64 €, apertura)
- 2026-09-29 14:30 [macd_sin_salida] ENTRADA DOT @ 1.0696 (22.89 €, apertura)
- 2026-09-29 14:30 [macd_momentum_regimen] ENTRADA DOT @ 1.0696 (22.64 €, apertura)
- 2026-09-29 14:30 [macd_momentum_evento] ENTRADA DOT @ 1.0696 (23.11 €, apertura)
- 2026-09-29 14:30 [c_banda_atr] ENTRADA CRV @ 0.3544 (22.95 €, apertura)
- 2026-09-29 14:30 [ruptura_volumen] ENTRADA CRV @ 0.3544 (22.83 €, apertura)
- 2026-09-29 14:30 [macd_momentum] ENTRADA CRV @ 0.3544 (22.64 €, apertura)
- 2026-09-29 14:30 [ruptura_estricta] ENTRADA CRV @ 0.3544 (22.97 €, apertura)
- 2026-09-29 14:30 [macd_sin_salida] ENTRADA CRV @ 0.3544 (22.89 €, apertura)
- 2026-09-29 14:30 [ruptura_volumen_tope] ENTRADA CRV @ 0.3544 (23.04 €, apertura)
- 2026-09-29 14:30 [c_banda_atr_regimen] ENTRADA CRV @ 0.3544 (22.95 €, apertura)
- 2026-09-29 14:30 [macd_momentum_regimen] ENTRADA CRV @ 0.3544 (22.64 €, apertura)
- 2026-09-29 14:30 [ruptura_volumen_regimen] ENTRADA CRV @ 0.3544 (22.83 €, apertura)
- 2026-09-29 14:30 [c_banda_atr_evento] ENTRADA CRV @ 0.3544 (23.11 €, apertura)
- 2026-09-29 14:30 [macd_momentum_evento] ENTRADA CRV @ 0.3544 (23.11 €, apertura)
- 2026-09-29 14:30 [ruptura_volumen_evento] ENTRADA CRV @ 0.3544 (23.11 €, apertura)
- 2026-09-29 14:30 [c_banda_atr_evento] ENTRADA BCH @ 275.12 (23.11 €, apertura)
- 2026-09-29 14:30 [macd_momentum] ENTRADA INJ @ 6.83 (22.64 €, apertura)
- 2026-09-29 14:30 [macd_momentum_regimen] ENTRADA INJ @ 6.83 (22.64 €, apertura)
- 2026-09-29 14:30 [macd_momentum_evento] ENTRADA INJ @ 6.83 (23.11 €, apertura)
- 2026-09-29 14:30 [c_banda_atr] ENTRADA RENDER @ 1.733 (22.95 €, apertura)
- 2026-09-29 14:30 [c_banda_atr_regimen] ENTRADA RENDER @ 1.733 (22.95 €, apertura)
- 2026-09-29 14:30 [c_banda_atr_evento] ENTRADA RENDER @ 1.733 (23.11 €, apertura)
- 2026-09-29 14:35 [pullback_tendencia] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:35 [c_banda_atr] CIERRE OP take-profit bruto +2.22% neto +1.12%
- 2026-09-29 14:35 [c_banda_atr_regimen] CIERRE OP take-profit bruto +2.22% neto +1.12%
- 2026-09-29 14:30 [c_banda_atr] ENTRADA TON @ 1.37 (22.96 €, apertura)
- 2026-09-29 14:30 [c_banda_atr_regimen] ENTRADA TON @ 1.37 (22.96 €, apertura)
- 2026-09-29 14:30 [c_banda_atr_evento] ENTRADA TON @ 1.37 (23.11 €, apertura)
- 2026-09-29 14:35 [estocastico_rebote] CIERRE XPL timeout bruto +0.11% neto -0.69%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
