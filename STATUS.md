# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 12:16 UTC · vueltas 32 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 926.24 € (+0.22%) | 8 | 23 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| reversion_bb | 923.64 € (-0.07%) | 1 | 0 | 0% | -1.500% | -2.600% | -2.784% | -0.60 € |
| ruptura_volumen | 921.35 € (-0.31%) | 24 | 24 | 42% | +0.756% | -0.344% | -0.494% | -1.91 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 923.29 € (-0.10%) | 16 | 8 | 50% | +0.583% | -0.517% | -0.639% | -1.92 € |
| macd_momentum | 914.98 € (-1.00%) | 54 | 35 | 22% | +0.174% | -0.798% | -0.915% | -9.99 € |
| estocastico_rebote | 928.02 € (+0.41%) | 18 | 31 | 83% | +1.265% | +0.165% | +0.021% | +0.69 € |
| ruptura_estricta | 926.08 € (+0.20%) | 4 | 26 | 50% | +0.553% | -0.547% | -0.818% | -0.51 € |
| macd_sin_salida | 924.92 € (+0.07%) | 21 | 34 | 71% | +1.016% | -0.084% | -0.233% | -0.41 € |
| c_banda_atr_tope | 924.57 € (+0.04%) | 1 | 5 | 100% | +2.000% | +0.900% | +0.604% | +0.21 € |
| ruptura_volumen_tope | 923.84 € (-0.04%) | 6 | 5 | 17% | +0.212% | -0.888% | -1.018% | -1.23 € |
| c_banda_atr_regimen | 926.24 € (+0.22%) | 8 | 23 | 88% | +1.562% | +0.462% | +0.326% | +0.85 € |
| macd_momentum_regimen | 914.98 € (-1.00%) | 54 | 35 | 22% | +0.174% | -0.798% | -0.915% | -9.99 € |
| ruptura_volumen_regimen | 921.35 € (-0.31%) | 24 | 24 | 42% | +0.756% | -0.344% | -0.494% | -1.91 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 12:15 | ruptura_volumen_regimen | POL | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 12:15 | macd_momentum_regimen | ASTER | momentum perdido | +0.27% | -0.53% | -0.12 |
| 2026-09-29 12:15 | macd_momentum_regimen | SUI | momentum perdido | -0.54% | -1.04% | -0.24 |
| 2026-09-29 12:15 | ruptura_estricta | NIGHT | stop-loss | -2.00% | -3.10% | -0.72 |
| 2026-09-29 12:15 | macd_momentum | ASTER | momentum perdido | +0.27% | -0.53% | -0.12 |
| 2026-09-29 12:15 | macd_momentum | SUI | momentum perdido | -0.54% | -1.04% | -0.24 |
| 2026-09-29 12:15 | ruptura_volumen | POL | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 12:10 | ruptura_volumen_regimen | USELESS | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 12:10 | macd_sin_salida | MINA | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 12:10 | ruptura_volumen | USELESS | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 12:05 | ruptura_volumen_regimen | PENGU | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-29 12:05 | ruptura_volumen_regimen | ICP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 12:05 | macd_momentum_regimen | PENGU | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 12:05 | macd_momentum_regimen | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 12:05 | macd_momentum_regimen | AVAX | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-09-29 12:15 [macd_momentum] CIERRE SUI momentum perdido bruto -0.54% neto -1.04%
- 2026-09-29 12:15 [macd_momentum_regimen] CIERRE SUI momentum perdido bruto -0.54% neto -1.04%
- 2026-09-29 12:10 [pullback_tendencia] ENTRADA DOT @ 1.0729 (23.06 €, apertura)
- 2026-09-29 12:10 [estocastico_rebote] ENTRADA MINA @ 0.1335 (23.12 €, apertura)
- 2026-09-29 12:15 [ruptura_estricta] CIERRE NIGHT stop-loss bruto -2.00% neto -3.10%
- 2026-09-29 12:15 [ruptura_volumen] CIERRE POL take-profit bruto +2.50% neto +1.40%
- 2026-09-29 12:15 [ruptura_volumen_regimen] CIERRE POL take-profit bruto +2.50% neto +1.40%
- 2026-09-29 12:15 [macd_momentum] CIERRE ASTER momentum perdido bruto +0.27% neto -0.53%
- 2026-09-29 12:15 [macd_momentum_regimen] CIERRE ASTER momentum perdido bruto +0.27% neto -0.53%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
