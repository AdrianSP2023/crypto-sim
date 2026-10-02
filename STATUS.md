# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 03:16 UTC · vueltas 374 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.89 € (-4.15%) | 295 | 24 | 35% | -0.002% | -0.590% | -0.711% | -39.54 € |
| reversion_bb | 919.62 € (-0.50%) | 66 | 6 | 58% | +0.515% | -0.381% | -0.486% | -5.81 € |
| ruptura_volumen | 867.71 € (-6.12%) | 336 | 26 | 25% | -0.174% | -0.751% | -0.860% | -56.74 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.49 € (-3.76%) | 196 | 10 | 16% | -0.167% | -0.801% | -0.890% | -35.65 € |
| macd_momentum | 862.72 € (-6.66%) | 533 | 33 | 21% | +0.004% | -0.545% | -0.647% | -64.86 € |
| estocastico_rebote | 873.93 € (-5.44%) | 346 | 15 | 32% | -0.092% | -0.667% | -0.776% | -52.07 € |
| ruptura_estricta | 883.90 € (-4.36%) | 170 | 29 | 25% | -0.432% | -1.087% | -1.204% | -42.02 € |
| macd_sin_salida | 875.85 € (-5.24%) | 370 | 31 | 35% | -0.047% | -0.617% | -0.728% | -51.64 € |
| c_banda_atr_tope | 912.27 € (-1.29%) | 68 | 5 | 32% | +0.108% | -0.780% | -0.894% | -12.20 € |
| ruptura_volumen_tope | 903.74 € (-2.22%) | 111 | 5 | 25% | -0.080% | -0.818% | -0.933% | -20.77 € |
| c_banda_atr_regimen | 897.70 € (-2.87%) | 142 | 30 | 30% | -0.202% | -0.886% | -1.018% | -28.75 € |
| macd_momentum_regimen | 885.50 € (-4.19%) | 298 | 31 | 19% | -0.025% | -0.613% | -0.718% | -41.35 € |
| ruptura_volumen_regimen | 872.03 € (-5.65%) | 263 | 22 | 22% | -0.281% | -0.880% | -0.993% | -52.17 € |
| c_banda_atr_evento | 891.79 € (-3.51%) | 262 | 24 | 36% | +0.037% | -0.564% | -0.680% | -33.65 € |
| macd_momentum_evento | 867.50 € (-6.14%) | 486 | 33 | 19% | +0.002% | -0.552% | -0.651% | -60.10 € |
| ruptura_volumen_evento | 880.05 € (-4.78%) | 286 | 26 | 26% | -0.094% | -0.687% | -0.788% | -44.40 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 03:15 | macd_sin_salida | SOL | timeout | +1.37% | +0.87% | +0.19 |
| 2026-10-02 03:15 | macd_sin_salida | ETH | timeout | +0.53% | +0.03% | +0.01 |
| 2026-10-02 03:15 | estocastico_rebote | TRX | timeout | +0.05% | -0.45% | -0.10 |
| 2026-10-02 03:10 | macd_momentum_evento | CRV | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 03:10 | estocastico_rebote | XMR | timeout | -0.19% | -0.69% | -0.15 |
| 2026-10-02 03:10 | macd_momentum | CRV | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 03:05 | ruptura_volumen_evento | NEAR | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 03:05 | macd_momentum_evento | KAS | take-profit | +2.18% | +1.68% | +0.36 |
| 2026-10-02 03:05 | macd_momentum_evento | MON | momentum perdido | -0.66% | -1.16% | -0.25 |
| 2026-10-02 03:05 | macd_momentum_evento | DOT | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 03:05 | c_banda_atr_evento | KAS | take-profit | +2.01% | +1.51% | +0.34 |
| 2026-10-02 03:05 | c_banda_atr_evento | TON | timeout | -1.07% | -1.57% | -0.35 |
| 2026-10-02 03:05 | c_banda_atr_evento | XDC | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 03:05 | c_banda_atr_evento | DOT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 03:05 | ruptura_volumen_regimen | NEAR | take-profit | +2.50% | +2.00% | +0.44 |

## Eventos de la última vuelta

- 2026-10-02 03:15 [macd_sin_salida] CIERRE ETH timeout bruto +0.53% neto +0.03%
- 2026-10-02 03:15 [macd_sin_salida] CIERRE SOL timeout bruto +1.37% neto +0.87%
- 2026-10-02 03:15 [estocastico_rebote] CIERRE TRX timeout bruto +0.05% neto -0.45%
- 2026-10-02 03:10 [ruptura_volumen] ENTRADA ONDO @ 0.44221 (21.69 €, apertura)
- 2026-10-02 03:10 [ruptura_volumen_regimen] ENTRADA ONDO @ 0.44221 (21.80 €, apertura)
- 2026-10-02 03:10 [ruptura_volumen_evento] ENTRADA ONDO @ 0.44221 (22.00 €, apertura)
- 2026-10-02 03:10 [macd_momentum] ENTRADA VVV @ 23.619 (21.48 €, apertura)
- 2026-10-02 03:10 [macd_momentum_regimen] ENTRADA VVV @ 23.619 (22.07 €, apertura)
- 2026-10-02 03:10 [macd_momentum_evento] ENTRADA VVV @ 23.619 (21.60 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
