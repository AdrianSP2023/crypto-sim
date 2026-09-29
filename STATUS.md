# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 13:51 UTC · vueltas 51 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 920.47 € (-0.41%) | 18 | 20 | 56% | +0.536% | -0.564% | -0.674% | -2.35 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 915.06 € (-0.99%) | 47 | 9 | 30% | +0.148% | -0.869% | -1.008% | -9.42 € |
| rebote_extremo | 924.45 € (+0.02%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 916.28 € (-0.86%) | 38 | 8 | 34% | +0.280% | -0.820% | -0.925% | -7.19 € |
| macd_momentum | 908.12 € (-1.74%) | 104 | 5 | 19% | +0.055% | -0.696% | -0.806% | -16.64 € |
| estocastico_rebote | 922.02 € (-0.24%) | 37 | 30 | 68% | +0.953% | -0.050% | -0.175% | -0.42 € |
| ruptura_estricta | 920.28 € (-0.43%) | 21 | 15 | 33% | +0.190% | -0.910% | -1.043% | -4.42 € |
| macd_sin_salida | 915.88 € (-0.90%) | 49 | 20 | 39% | +0.337% | -0.647% | -0.765% | -7.28 € |
| c_banda_atr_tope | 922.59 € (-0.18%) | 6 | 4 | 33% | -0.058% | -1.158% | -1.299% | -1.61 € |
| ruptura_volumen_tope | 921.83 € (-0.26%) | 13 | 3 | 23% | +0.215% | -0.885% | -1.016% | -2.66 € |
| c_banda_atr_regimen | 920.47 € (-0.41%) | 18 | 20 | 56% | +0.536% | -0.564% | -0.674% | -2.35 € |
| macd_momentum_regimen | 908.12 € (-1.74%) | 104 | 5 | 19% | +0.055% | -0.696% | -0.806% | -16.64 € |
| ruptura_volumen_regimen | 915.06 € (-0.99%) | 47 | 9 | 30% | +0.148% | -0.869% | -1.008% | -9.42 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 13:50 | ruptura_volumen_regimen | PEPE | timeout | +0.95% | +0.15% | +0.03 |
| 2026-09-29 13:50 | ruptura_volumen_regimen | HYPE | timeout | -0.82% | -1.62% | -0.37 |
| 2026-09-29 13:50 | ruptura_volumen_regimen | ZEC | timeout | -0.36% | -1.16% | -0.27 |
| 2026-09-29 13:50 | ruptura_volumen_regimen | BTC | timeout | -0.30% | -1.10% | -0.25 |
| 2026-09-29 13:50 | macd_momentum_regimen | ZRO | momentum perdido | -0.62% | -1.12% | -0.25 |
| 2026-09-29 13:50 | estocastico_rebote | NEAR | take-profit | +1.80% | +1.30% | +0.30 |
| 2026-09-29 13:50 | macd_momentum | ZRO | momentum perdido | -0.62% | -1.12% | -0.25 |
| 2026-09-29 13:50 | pullback_tendencia | USELESS | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 13:50 | pullback_tendencia | ETH | rotura de tendencia | +0.37% | -0.73% | -0.17 |
| 2026-09-29 13:50 | ruptura_volumen | PEPE | timeout | +0.95% | +0.15% | +0.03 |
| 2026-09-29 13:50 | ruptura_volumen | HYPE | timeout | -0.82% | -1.62% | -0.37 |
| 2026-09-29 13:50 | ruptura_volumen | ZEC | timeout | -0.36% | -1.16% | -0.27 |
| 2026-09-29 13:50 | ruptura_volumen | BTC | timeout | -0.30% | -1.10% | -0.25 |
| 2026-09-29 13:45 | ruptura_volumen_regimen | RENDER | timeout | -0.46% | -1.26% | -0.29 |
| 2026-09-29 13:45 | estocastico_rebote | ADA | timeout | +0.50% | -0.30% | -0.07 |

## Eventos de la última vuelta

- 2026-09-29 13:50 [ruptura_volumen] CIERRE BTC timeout bruto -0.30% neto -1.10%
- 2026-09-29 13:50 [ruptura_volumen_regimen] CIERRE BTC timeout bruto -0.30% neto -1.10%
- 2026-09-29 13:50 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto +0.37% neto -0.73%
- 2026-09-29 13:45 [pullback_tendencia] ENTRADA QNT @ 226.26 (22.92 €, apertura)
- 2026-09-29 13:50 [ruptura_volumen] CIERRE ZEC timeout bruto -0.36% neto -1.16%
- 2026-09-29 13:50 [ruptura_volumen_regimen] CIERRE ZEC timeout bruto -0.36% neto -1.16%
- 2026-09-29 13:50 [estocastico_rebote] CIERRE NEAR take-profit bruto +1.80% neto +1.30%
- 2026-09-29 13:50 [ruptura_volumen] CIERRE HYPE timeout bruto -0.82% neto -1.62%
- 2026-09-29 13:50 [ruptura_volumen_regimen] CIERRE HYPE timeout bruto -0.82% neto -1.62%
- 2026-09-29 13:50 [macd_momentum] CIERRE ZRO momentum perdido bruto -0.62% neto -1.12%
- 2026-09-29 13:50 [macd_momentum_regimen] CIERRE ZRO momentum perdido bruto -0.62% neto -1.12%
- 2026-09-29 13:50 [ruptura_volumen] CIERRE PEPE timeout bruto +0.95% neto +0.15%
- 2026-09-29 13:50 [ruptura_volumen_regimen] CIERRE PEPE timeout bruto +0.95% neto +0.15%
- 2026-09-29 13:50 [pullback_tendencia] CIERRE USELESS take-profit bruto +2.00% neto +0.90%
- 2026-09-29 13:45 [macd_momentum] ENTRADA USELESS @ 0.21262 (22.69 €, apertura)
- 2026-09-29 13:45 [macd_sin_salida] ENTRADA USELESS @ 0.21262 (22.92 €, apertura)
- 2026-09-29 13:45 [macd_momentum_regimen] ENTRADA USELESS @ 0.21262 (22.69 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
