# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 03:21 UTC · vueltas 375 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.18 € (-4.23%) | 295 | 24 | 35% | -0.002% | -0.590% | -0.711% | -39.54 € |
| reversion_bb | 919.40 € (-0.52%) | 66 | 6 | 58% | +0.515% | -0.381% | -0.486% | -5.81 € |
| ruptura_volumen | 867.00 € (-6.19%) | 336 | 26 | 25% | -0.174% | -0.751% | -0.860% | -56.74 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.24 € (-3.79%) | 197 | 10 | 16% | -0.167% | -0.801% | -0.890% | -35.84 € |
| macd_momentum | 861.83 € (-6.75%) | 534 | 32 | 21% | +0.004% | -0.545% | -0.647% | -65.03 € |
| estocastico_rebote | 873.68 € (-5.47%) | 347 | 14 | 32% | -0.091% | -0.667% | -0.776% | -52.18 € |
| ruptura_estricta | 882.82 € (-4.48%) | 173 | 26 | 26% | -0.408% | -1.061% | -1.176% | -41.73 € |
| macd_sin_salida | 874.94 € (-5.33%) | 371 | 30 | 35% | -0.047% | -0.617% | -0.728% | -51.80 € |
| c_banda_atr_tope | 912.22 € (-1.30%) | 68 | 5 | 32% | +0.108% | -0.780% | -0.894% | -12.20 € |
| ruptura_volumen_tope | 903.45 € (-2.25%) | 111 | 5 | 25% | -0.080% | -0.818% | -0.933% | -20.77 € |
| c_banda_atr_regimen | 896.90 € (-2.96%) | 142 | 30 | 30% | -0.202% | -0.886% | -1.018% | -28.75 € |
| macd_momentum_regimen | 884.62 € (-4.29%) | 299 | 30 | 19% | -0.026% | -0.613% | -0.718% | -41.53 € |
| ruptura_volumen_regimen | 871.38 € (-5.72%) | 263 | 22 | 22% | -0.281% | -0.880% | -0.993% | -52.17 € |
| c_banda_atr_evento | 891.08 € (-3.59%) | 262 | 24 | 36% | +0.037% | -0.564% | -0.680% | -33.65 € |
| macd_momentum_evento | 866.61 € (-6.24%) | 487 | 32 | 19% | +0.001% | -0.553% | -0.652% | -60.27 € |
| ruptura_volumen_evento | 879.34 € (-4.86%) | 286 | 26 | 26% | -0.094% | -0.687% | -0.788% | -44.40 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 03:20 | macd_momentum_evento | SUI | momentum perdido | -0.30% | -0.80% | -0.17 |
| 2026-10-02 03:20 | macd_momentum_regimen | SUI | momentum perdido | -0.30% | -0.80% | -0.18 |
| 2026-10-02 03:20 | macd_sin_salida | ZEC | timeout | -0.23% | -0.73% | -0.16 |
| 2026-10-02 03:20 | ruptura_estricta | FET | timeout | +1.98% | +1.48% | +0.33 |
| 2026-10-02 03:20 | ruptura_estricta | LTC | timeout | -0.21% | -0.71% | -0.16 |
| 2026-10-02 03:20 | ruptura_estricta | SOL | timeout | +1.01% | +0.51% | +0.11 |
| 2026-10-02 03:20 | estocastico_rebote | TON | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 03:20 | macd_momentum | SUI | momentum perdido | -0.30% | -0.80% | -0.17 |
| 2026-10-02 03:20 | pullback_tendencia | LTC | rotura de tendencia | -0.34% | -0.84% | -0.19 |
| 2026-10-02 03:15 | macd_sin_salida | SOL | timeout | +1.37% | +0.87% | +0.19 |
| 2026-10-02 03:15 | macd_sin_salida | ETH | timeout | +0.53% | +0.03% | +0.01 |
| 2026-10-02 03:15 | estocastico_rebote | TRX | timeout | +0.05% | -0.45% | -0.10 |
| 2026-10-02 03:10 | macd_momentum_evento | CRV | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 03:10 | estocastico_rebote | XMR | timeout | -0.19% | -0.69% | -0.15 |
| 2026-10-02 03:10 | macd_momentum | CRV | momentum perdido | -0.07% | -0.57% | -0.12 |

## Eventos de la última vuelta

- 2026-10-02 03:20 [ruptura_estricta] CIERRE SOL timeout bruto +1.01% neto +0.51%
- 2026-10-02 03:20 [macd_momentum] CIERRE SUI momentum perdido bruto -0.30% neto -0.80%
- 2026-10-02 03:20 [macd_momentum_regimen] CIERRE SUI momentum perdido bruto -0.30% neto -0.80%
- 2026-10-02 03:20 [macd_momentum_evento] CIERRE SUI momentum perdido bruto -0.30% neto -0.80%
- 2026-10-02 03:20 [macd_sin_salida] CIERRE ZEC timeout bruto -0.23% neto -0.73%
- 2026-10-02 03:20 [pullback_tendencia] CIERRE LTC rotura de tendencia bruto -0.34% neto -0.84%
- 2026-10-02 03:20 [ruptura_estricta] CIERRE LTC timeout bruto -0.21% neto -0.71%
- 2026-10-02 03:20 [ruptura_estricta] CIERRE FET timeout bruto +1.98% neto +1.48%
- 2026-10-02 03:15 [pullback_tendencia] ENTRADA SHIB @ 5.158e-06 (22.21 €, apertura)
- 2026-10-02 03:20 [estocastico_rebote] CIERRE TON timeout bruto +0.00% neto -0.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
