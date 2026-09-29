# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 11:26 UTC · vueltas 22 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 923.74 € (-0.05%) | 1 | 12 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| reversion_bb | 924.22 € (-0.00%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen | 921.16 € (-0.33%) | 6 | 12 | 17% | -0.602% | -1.702% | -1.846% | -2.36 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 921.04 € (-0.35%) | 7 | 12 | 0% | -0.887% | -1.987% | -2.128% | -3.21 € |
| macd_momentum | 912.06 € (-1.32%) | 42 | 7 | 7% | -0.192% | -1.277% | -1.401% | -12.39 € |
| estocastico_rebote | 924.97 € (+0.08%) | 3 | 37 | 67% | +0.701% | -0.399% | -0.587% | -0.28 € |
| ruptura_estricta | 922.25 € (-0.21%) | 2 | 12 | 50% | +0.605% | -0.494% | -0.730% | -0.23 € |
| macd_sin_salida | 919.94 € (-0.46%) | 9 | 34 | 44% | +0.040% | -1.060% | -1.269% | -2.20 € |
| c_banda_atr_tope | 923.83 € (-0.04%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 922.87 € (-0.15%) | 2 | 5 | 0% | -1.238% | -2.338% | -2.482% | -1.08 € |
| c_banda_atr_regimen | 923.74 € (-0.05%) | 1 | 12 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| macd_momentum_regimen | 912.06 € (-1.32%) | 42 | 7 | 7% | -0.192% | -1.277% | -1.401% | -12.39 € |
| ruptura_volumen_regimen | 921.16 € (-0.33%) | 6 | 12 | 17% | -0.602% | -1.702% | -1.846% | -2.36 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 11:25 | macd_momentum_regimen | XDC | momentum perdido | +0.25% | -0.55% | -0.13 |
| 2026-09-29 11:25 | macd_momentum_regimen | PUMP | take-profit | +2.00% | +1.20% | +0.27 |
| 2026-09-29 11:25 | macd_sin_salida | PUMP | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 11:25 | macd_momentum | XDC | momentum perdido | +0.25% | -0.55% | -0.13 |
| 2026-09-29 11:25 | macd_momentum | PUMP | take-profit | +2.00% | +1.20% | +0.27 |
| 2026-09-29 11:20 | macd_sin_salida | VVV | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 11:20 | ruptura_estricta | NIGHT | take-profit | +3.21% | +2.11% | +0.49 |
| 2026-09-29 11:20 | pullback_tendencia | VIRTUAL | rotura de tendencia | -0.21% | -1.31% | -0.30 |
| 2026-09-29 11:15 | ruptura_volumen_regimen | NIGHT | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 11:15 | ruptura_volumen_regimen | JUP | stop-loss | -1.24% | -2.34% | -0.54 |
| 2026-09-29 11:15 | ruptura_volumen_regimen | ONDO | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 11:15 | estocastico_rebote | PUMP | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-29 11:15 | ruptura_volumen | NIGHT | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 11:15 | ruptura_volumen | JUP | stop-loss | -1.24% | -2.34% | -0.54 |
| 2026-09-29 11:15 | ruptura_volumen | ONDO | stop-loss | -1.20% | -2.30% | -0.53 |

## Eventos de la última vuelta

- 2026-09-29 11:20 [macd_momentum] ENTRADA XLM @ 0.203909 (22.79 €, apertura)
- 2026-09-29 11:20 [macd_momentum_regimen] ENTRADA XLM @ 0.203909 (22.79 €, apertura)
- 2026-09-29 11:20 [pullback_tendencia] ENTRADA AAVE @ 147.34 (23.03 €, apertura)
- 2026-09-29 11:25 [macd_momentum] CIERRE PUMP take-profit bruto +2.00% neto +1.20%
- 2026-09-29 11:25 [macd_sin_salida] CIERRE PUMP take-profit bruto +2.00% neto +0.90%
- 2026-09-29 11:25 [macd_momentum_regimen] CIERRE PUMP take-profit bruto +2.00% neto +1.20%
- 2026-09-29 11:20 [macd_momentum] ENTRADA ARB @ 0.1852 (22.80 €, apertura)
- 2026-09-29 11:20 [macd_momentum_regimen] ENTRADA ARB @ 0.1852 (22.80 €, apertura)
- 2026-09-29 11:25 [macd_momentum] CIERRE XDC momentum perdido bruto +0.25% neto -0.55%
- 2026-09-29 11:25 [macd_momentum_regimen] CIERRE XDC momentum perdido bruto +0.25% neto -0.55%
- 2026-09-29 11:20 [c_banda_atr] ENTRADA ZRO @ 1.384 (23.11 €, apertura)
- 2026-09-29 11:20 [estocastico_rebote] ENTRADA ZRO @ 1.384 (23.10 €, apertura)
- 2026-09-29 11:20 [c_banda_atr_regimen] ENTRADA ZRO @ 1.384 (23.11 €, apertura)
- 2026-09-29 11:20 [c_banda_atr] ENTRADA OP @ 0.1169 (23.11 €, apertura)
- 2026-09-29 11:20 [c_banda_atr_regimen] ENTRADA OP @ 0.1169 (23.11 €, apertura)
- 2026-09-29 11:20 [macd_momentum] ENTRADA POL @ 0.10208 (22.80 €, apertura)
- 2026-09-29 11:20 [macd_momentum_regimen] ENTRADA POL @ 0.10208 (22.80 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
