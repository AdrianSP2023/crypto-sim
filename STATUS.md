# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 14:52 UTC · vueltas 62 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 918.66 € (-0.60%) | 32 | 17 | 50% | +0.324% | -0.776% | -0.931% | -5.74 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 914.31 € (-1.07%) | 56 | 13 | 29% | +0.102% | -0.864% | -0.992% | -11.15 € |
| rebote_extremo | 924.29 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 915.05 € (-0.99%) | 49 | 9 | 33% | +0.150% | -0.871% | -0.982% | -9.83 € |
| macd_momentum | 907.37 € (-1.83%) | 123 | 21 | 23% | +0.083% | -0.629% | -0.747% | -17.79 € |
| estocastico_rebote | 920.38 € (-0.42%) | 59 | 33 | 54% | +0.616% | -0.296% | -0.429% | -4.03 € |
| ruptura_estricta | 919.33 € (-0.53%) | 28 | 13 | 36% | +0.165% | -0.935% | -1.064% | -6.04 € |
| macd_sin_salida | 917.13 € (-0.77%) | 69 | 23 | 42% | +0.396% | -0.478% | -0.610% | -7.59 € |
| c_banda_atr_tope | 920.48 € (-0.41%) | 11 | 5 | 27% | -0.397% | -1.497% | -1.686% | -3.80 € |
| ruptura_volumen_tope | 922.20 € (-0.22%) | 15 | 5 | 20% | +0.300% | -0.800% | -0.920% | -2.77 € |
| c_banda_atr_regimen | 918.66 € (-0.60%) | 32 | 17 | 50% | +0.324% | -0.776% | -0.931% | -5.74 € |
| macd_momentum_regimen | 907.37 € (-1.83%) | 123 | 21 | 23% | +0.083% | -0.629% | -0.747% | -17.79 € |
| ruptura_volumen_regimen | 914.31 € (-1.07%) | 56 | 13 | 29% | +0.102% | -0.864% | -0.992% | -11.15 € |
| c_banda_atr_evento | 924.52 € (+0.03%) | 4 | 13 | 75% | +1.114% | +0.013% | -0.247% | +0.01 € |
| macd_momentum_evento | 925.85 € (+0.17%) | 3 | 21 | 100% | +2.000% | +0.900% | +0.687% | +0.62 € |
| ruptura_volumen_evento | 924.57 € (+0.04%) | 0 | 9 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 14:50 | macd_momentum_evento | ZRO | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 14:50 | macd_momentum_evento | CRV | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 14:50 | c_banda_atr_evento | MINA | take-profit | +2.05% | +0.95% | +0.22 |
| 2026-09-29 14:50 | c_banda_atr_evento | CRV | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 14:50 | macd_momentum_regimen | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:50 | macd_momentum_regimen | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:50 | c_banda_atr_regimen | FIL | take-profit | +2.21% | +1.11% | +0.26 |
| 2026-09-29 14:50 | c_banda_atr_regimen | MINA | take-profit | +2.05% | +0.95% | +0.22 |
| 2026-09-29 14:50 | c_banda_atr_regimen | CRV | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 14:50 | macd_sin_salida | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:50 | macd_sin_salida | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:50 | ruptura_estricta | ZEC | timeout | -0.99% | -2.09% | -0.48 |
| 2026-09-29 14:50 | macd_momentum | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:50 | macd_momentum | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:50 | pullback_tendencia | POL | stop-loss | -1.50% | -2.30% | -0.53 |

## Eventos de la última vuelta

- 2026-09-29 14:50 [ruptura_estricta] CIERRE ZEC timeout bruto -0.99% neto -2.09%
- 2026-09-29 14:45 [macd_momentum] ENTRADA AVAX @ 10.249 (22.64 €, apertura)
- 2026-09-29 14:45 [macd_sin_salida] ENTRADA AVAX @ 10.249 (22.90 €, apertura)
- 2026-09-29 14:45 [macd_momentum_regimen] ENTRADA AVAX @ 10.249 (22.64 €, apertura)
- 2026-09-29 14:45 [macd_momentum_evento] ENTRADA AVAX @ 10.249 (23.11 €, apertura)
- 2026-09-29 14:45 [ruptura_volumen] ENTRADA TAO @ 280.247 (22.83 €, apertura)
- 2026-09-29 14:45 [ruptura_volumen_regimen] ENTRADA TAO @ 280.247 (22.83 €, apertura)
- 2026-09-29 14:45 [ruptura_volumen_evento] ENTRADA TAO @ 280.247 (23.11 €, apertura)
- 2026-09-29 14:50 [c_banda_atr] CIERRE CRV take-profit bruto +2.00% neto +0.90%
- 2026-09-29 14:50 [pullback_tendencia] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:50 [macd_momentum] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:50 [macd_sin_salida] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:50 [c_banda_atr_regimen] CIERRE CRV take-profit bruto +2.00% neto +0.90%
- 2026-09-29 14:50 [macd_momentum_regimen] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:50 [c_banda_atr_evento] CIERRE CRV take-profit bruto +2.00% neto +0.90%
- 2026-09-29 14:50 [macd_momentum_evento] CIERRE CRV take-profit bruto +2.00% neto +0.90%
- 2026-09-29 14:50 [macd_momentum] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:50 [macd_sin_salida] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:50 [macd_momentum_regimen] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-29 14:50 [macd_momentum_evento] CIERRE ZRO take-profit bruto +2.00% neto +0.90%
- 2026-09-29 14:50 [c_banda_atr] CIERRE MINA take-profit bruto +2.05% neto +0.95%
- 2026-09-29 14:50 [c_banda_atr_regimen] CIERRE MINA take-profit bruto +2.05% neto +0.95%
- 2026-09-29 14:50 [c_banda_atr_evento] CIERRE MINA take-profit bruto +2.05% neto +0.95%
- 2026-09-29 14:45 [ruptura_volumen] ENTRADA NIGHT @ 0.02857 (22.83 €, apertura)
- 2026-09-29 14:45 [ruptura_estricta] ENTRADA NIGHT @ 0.02857 (22.95 €, apertura)
- 2026-09-29 14:45 [ruptura_volumen_regimen] ENTRADA NIGHT @ 0.02857 (22.83 €, apertura)
- 2026-09-29 14:45 [ruptura_volumen_evento] ENTRADA NIGHT @ 0.02857 (23.11 €, apertura)
- 2026-09-29 14:50 [c_banda_atr] CIERRE FIL take-profit bruto +2.21% neto +1.11%
- 2026-09-29 14:50 [c_banda_atr_regimen] CIERRE FIL take-profit bruto +2.21% neto +1.11%
- 2026-09-29 14:50 [pullback_tendencia] CIERRE POL stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 14:45 [macd_momentum] ENTRADA BNB @ 674.68 (22.66 €, apertura)
- 2026-09-29 14:45 [macd_momentum_regimen] ENTRADA BNB @ 674.68 (22.66 €, apertura)
- 2026-09-29 14:45 [macd_momentum_evento] ENTRADA BNB @ 674.68 (23.12 €, apertura)
- 2026-09-29 14:45 [ruptura_volumen] ENTRADA ASTER @ 0.64317 (22.83 €, apertura)
- 2026-09-29 14:45 [ruptura_volumen_regimen] ENTRADA ASTER @ 0.64317 (22.83 €, apertura)
- 2026-09-29 14:45 [c_banda_atr_evento] ENTRADA ASTER @ 0.64317 (23.11 €, apertura)
- 2026-09-29 14:45 [ruptura_volumen_evento] ENTRADA ASTER @ 0.64317 (23.11 €, apertura)
- 2026-09-29 14:45 [ruptura_volumen] ENTRADA XPL @ 0.0888 (22.83 €, apertura)
- 2026-09-29 14:45 [ruptura_volumen_regimen] ENTRADA XPL @ 0.0888 (22.83 €, apertura)
- 2026-09-29 14:45 [ruptura_volumen_evento] ENTRADA XPL @ 0.0888 (23.11 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
