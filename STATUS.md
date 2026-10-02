# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 03:26 UTC · vueltas 376 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.75 € (-4.27%) | 295 | 24 | 35% | -0.002% | -0.590% | -0.711% | -39.54 € |
| reversion_bb | 919.42 € (-0.52%) | 66 | 6 | 58% | +0.515% | -0.381% | -0.486% | -5.81 € |
| ruptura_volumen | 866.36 € (-6.26%) | 336 | 28 | 25% | -0.174% | -0.751% | -0.860% | -56.74 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.92 € (-3.82%) | 198 | 9 | 16% | -0.171% | -0.804% | -0.893% | -36.15 € |
| macd_momentum | 860.73 € (-6.87%) | 538 | 29 | 21% | +0.004% | -0.544% | -0.646% | -65.40 € |
| estocastico_rebote | 873.43 € (-5.50%) | 347 | 14 | 32% | -0.091% | -0.667% | -0.776% | -52.18 € |
| ruptura_estricta | 882.04 € (-4.57%) | 173 | 26 | 26% | -0.408% | -1.061% | -1.176% | -41.73 € |
| macd_sin_salida | 874.41 € (-5.39%) | 371 | 31 | 35% | -0.047% | -0.617% | -0.728% | -51.80 € |
| c_banda_atr_tope | 912.17 € (-1.31%) | 68 | 5 | 32% | +0.108% | -0.780% | -0.894% | -12.20 € |
| ruptura_volumen_tope | 903.32 € (-2.26%) | 111 | 5 | 25% | -0.080% | -0.818% | -0.933% | -20.77 € |
| c_banda_atr_regimen | 896.46 € (-3.01%) | 142 | 30 | 30% | -0.202% | -0.886% | -1.018% | -28.75 € |
| macd_momentum_regimen | 883.67 € (-4.39%) | 302 | 28 | 19% | -0.028% | -0.614% | -0.719% | -41.99 € |
| ruptura_volumen_regimen | 870.88 € (-5.77%) | 263 | 24 | 22% | -0.281% | -0.880% | -0.993% | -52.17 € |
| c_banda_atr_evento | 890.64 € (-3.64%) | 262 | 24 | 36% | +0.037% | -0.564% | -0.680% | -33.65 € |
| macd_momentum_evento | 865.50 € (-6.36%) | 491 | 29 | 19% | +0.002% | -0.552% | -0.650% | -60.64 € |
| ruptura_volumen_evento | 878.69 € (-4.93%) | 286 | 28 | 26% | -0.094% | -0.687% | -0.788% | -44.40 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 03:25 | macd_momentum_evento | WLD | momentum perdido | -0.72% | -1.22% | -0.26 |
| 2026-10-02 03:25 | macd_momentum_evento | POL | momentum perdido | +0.87% | +0.37% | +0.08 |
| 2026-10-02 03:25 | macd_momentum_evento | SOL | momentum perdido | +0.37% | -0.13% | -0.03 |
| 2026-10-02 03:25 | macd_momentum_evento | ETH | momentum perdido | -0.22% | -0.72% | -0.16 |
| 2026-10-02 03:25 | macd_momentum_regimen | WLD | momentum perdido | -0.72% | -1.22% | -0.27 |
| 2026-10-02 03:25 | macd_momentum_regimen | SOL | momentum perdido | +0.37% | -0.13% | -0.03 |
| 2026-10-02 03:25 | macd_momentum_regimen | ETH | momentum perdido | -0.22% | -0.72% | -0.16 |
| 2026-10-02 03:25 | macd_momentum | WLD | momentum perdido | -0.72% | -1.22% | -0.26 |
| 2026-10-02 03:25 | macd_momentum | POL | momentum perdido | +0.87% | +0.37% | +0.08 |
| 2026-10-02 03:25 | macd_momentum | SOL | momentum perdido | +0.37% | -0.13% | -0.03 |
| 2026-10-02 03:25 | macd_momentum | ETH | momentum perdido | -0.22% | -0.72% | -0.15 |
| 2026-10-02 03:25 | pullback_tendencia | AAVE | rotura de tendencia | -0.90% | -1.40% | -0.31 |
| 2026-10-02 03:20 | macd_momentum_evento | SUI | momentum perdido | -0.30% | -0.80% | -0.17 |
| 2026-10-02 03:20 | macd_momentum_regimen | SUI | momentum perdido | -0.30% | -0.80% | -0.18 |
| 2026-10-02 03:20 | macd_sin_salida | ZEC | timeout | -0.23% | -0.73% | -0.16 |

## Eventos de la última vuelta

- 2026-10-02 03:25 [macd_momentum] CIERRE ETH momentum perdido bruto -0.22% neto -0.72%
- 2026-10-02 03:25 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto -0.22% neto -0.72%
- 2026-10-02 03:25 [macd_momentum_evento] CIERRE ETH momentum perdido bruto -0.22% neto -0.72%
- 2026-10-02 03:25 [macd_momentum] CIERRE SOL momentum perdido bruto +0.37% neto -0.13%
- 2026-10-02 03:25 [macd_momentum_regimen] CIERRE SOL momentum perdido bruto +0.37% neto -0.13%
- 2026-10-02 03:25 [macd_momentum_evento] CIERRE SOL momentum perdido bruto +0.37% neto -0.13%
- 2026-10-02 03:25 [pullback_tendencia] CIERRE AAVE rotura de tendencia bruto -0.90% neto -1.40%
- 2026-10-02 03:25 [macd_momentum] CIERRE POL momentum perdido bruto +0.87% neto +0.37%
- 2026-10-02 03:25 [macd_momentum_evento] CIERRE POL momentum perdido bruto +0.87% neto +0.37%
- 2026-10-02 03:25 [macd_momentum] CIERRE WLD momentum perdido bruto -0.72% neto -1.22%
- 2026-10-02 03:25 [macd_momentum_regimen] CIERRE WLD momentum perdido bruto -0.72% neto -1.22%
- 2026-10-02 03:25 [macd_momentum_evento] CIERRE WLD momentum perdido bruto -0.72% neto -1.22%
- 2026-10-02 03:20 [macd_momentum] ENTRADA USELESS @ 0.21594 (21.47 €, apertura)
- 2026-10-02 03:20 [macd_sin_salida] ENTRADA USELESS @ 0.21594 (21.81 €, apertura)
- 2026-10-02 03:20 [macd_momentum_regimen] ENTRADA USELESS @ 0.21594 (22.06 €, apertura)
- 2026-10-02 03:20 [macd_momentum_evento] ENTRADA USELESS @ 0.21594 (21.59 €, apertura)
- 2026-10-02 03:20 [ruptura_volumen] ENTRADA BNB @ 687.64 (21.69 €, apertura)
- 2026-10-02 03:20 [ruptura_volumen_regimen] ENTRADA BNB @ 687.64 (21.80 €, apertura)
- 2026-10-02 03:20 [ruptura_volumen_evento] ENTRADA BNB @ 687.64 (22.00 €, apertura)
- 2026-10-02 03:20 [ruptura_volumen] ENTRADA TON @ 1.401 (21.69 €, apertura)
- 2026-10-02 03:20 [ruptura_volumen_regimen] ENTRADA TON @ 1.401 (21.80 €, apertura)
- 2026-10-02 03:20 [ruptura_volumen_evento] ENTRADA TON @ 1.401 (22.00 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
