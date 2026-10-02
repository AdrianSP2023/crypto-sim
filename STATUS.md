# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 03:11 UTC · vueltas 373 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 886.12 € (-4.12%) | 295 | 24 | 35% | -0.002% | -0.590% | -0.711% | -39.54 € |
| reversion_bb | 919.70 € (-0.49%) | 66 | 6 | 58% | +0.515% | -0.381% | -0.486% | -5.81 € |
| ruptura_volumen | 867.95 € (-6.09%) | 336 | 25 | 25% | -0.174% | -0.751% | -0.860% | -56.74 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.53 € (-3.76%) | 196 | 10 | 16% | -0.167% | -0.801% | -0.890% | -35.65 € |
| macd_momentum | 862.79 € (-6.65%) | 533 | 32 | 21% | +0.004% | -0.545% | -0.647% | -64.86 € |
| estocastico_rebote | 873.96 € (-5.44%) | 345 | 16 | 32% | -0.092% | -0.668% | -0.777% | -51.97 € |
| ruptura_estricta | 883.89 € (-4.37%) | 170 | 29 | 25% | -0.432% | -1.087% | -1.204% | -42.02 € |
| macd_sin_salida | 876.07 € (-5.21%) | 368 | 33 | 35% | -0.052% | -0.623% | -0.734% | -51.84 € |
| c_banda_atr_tope | 912.37 € (-1.28%) | 68 | 5 | 32% | +0.108% | -0.780% | -0.894% | -12.20 € |
| ruptura_volumen_tope | 903.83 € (-2.21%) | 111 | 5 | 25% | -0.080% | -0.818% | -0.933% | -20.77 € |
| c_banda_atr_regimen | 897.91 € (-2.85%) | 142 | 30 | 30% | -0.202% | -0.886% | -1.018% | -28.75 € |
| macd_momentum_regimen | 885.40 € (-4.20%) | 298 | 30 | 19% | -0.025% | -0.613% | -0.718% | -41.35 € |
| ruptura_volumen_regimen | 872.16 € (-5.63%) | 263 | 21 | 22% | -0.281% | -0.880% | -0.993% | -52.17 € |
| c_banda_atr_evento | 892.02 € (-3.49%) | 262 | 24 | 36% | +0.037% | -0.564% | -0.680% | -33.65 € |
| macd_momentum_evento | 867.57 € (-6.13%) | 486 | 32 | 19% | +0.002% | -0.552% | -0.651% | -60.10 € |
| ruptura_volumen_evento | 880.30 € (-4.75%) | 286 | 25 | 26% | -0.094% | -0.687% | -0.788% | -44.40 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-02 03:05 | macd_momentum_regimen | MON | momentum perdido | -0.66% | -1.16% | -0.26 |
| 2026-10-02 03:05 | macd_momentum_regimen | DOT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 03:05 | c_banda_atr_regimen | XDC | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-10-02 03:05 [ruptura_volumen] ENTRADA BTC @ 75905 (21.69 €, apertura)
- 2026-10-02 03:05 [ruptura_estricta] ENTRADA BTC @ 75905 (22.06 €, apertura)
- 2026-10-02 03:05 [ruptura_volumen_regimen] ENTRADA BTC @ 75905 (21.80 €, apertura)
- 2026-10-02 03:05 [ruptura_volumen_evento] ENTRADA BTC @ 75905 (22.00 €, apertura)
- 2026-10-02 03:05 [ruptura_estricta] ENTRADA XRP @ 1.3379 (22.06 €, apertura)
- 2026-10-02 03:05 [estocastico_rebote] ENTRADA ZRO @ 1.619 (21.81 €, apertura)
- 2026-10-02 03:05 [ruptura_volumen] ENTRADA DOT @ 1.0693 (21.69 €, apertura)
- 2026-10-02 03:05 [ruptura_volumen_regimen] ENTRADA DOT @ 1.0693 (21.80 €, apertura)
- 2026-10-02 03:05 [ruptura_volumen_evento] ENTRADA DOT @ 1.0693 (22.00 €, apertura)
- 2026-10-02 03:10 [macd_momentum] CIERRE CRV momentum perdido bruto -0.07% neto -0.57%
- 2026-10-02 03:10 [macd_momentum_evento] CIERRE CRV momentum perdido bruto -0.07% neto -0.57%
- 2026-10-02 03:05 [macd_momentum] ENTRADA WLD @ 0.4572 (21.48 €, apertura)
- 2026-10-02 03:05 [macd_momentum_regimen] ENTRADA WLD @ 0.4572 (22.07 €, apertura)
- 2026-10-02 03:05 [macd_momentum_evento] ENTRADA WLD @ 0.4572 (21.60 €, apertura)
- 2026-10-02 03:05 [estocastico_rebote] ENTRADA USELESS @ 0.21452 (21.81 €, apertura)
- 2026-10-02 03:05 [c_banda_atr] ENTRADA JUP @ 0.29623 (22.12 €, apertura)
- 2026-10-02 03:05 [c_banda_atr_regimen] ENTRADA JUP @ 0.29623 (22.39 €, apertura)
- 2026-10-02 03:05 [c_banda_atr_evento] ENTRADA JUP @ 0.29623 (22.26 €, apertura)
- 2026-10-02 03:05 [ruptura_volumen] ENTRADA RENDER @ 1.731 (21.69 €, apertura)
- 2026-10-02 03:05 [ruptura_volumen_regimen] ENTRADA RENDER @ 1.731 (21.80 €, apertura)
- 2026-10-02 03:05 [ruptura_volumen_evento] ENTRADA RENDER @ 1.731 (22.00 €, apertura)
- 2026-10-02 03:05 [ruptura_volumen] ENTRADA KAS @ 0.03755 (21.69 €, apertura)
- 2026-10-02 03:05 [ruptura_volumen_regimen] ENTRADA KAS @ 0.03755 (21.80 €, apertura)
- 2026-10-02 03:05 [ruptura_volumen_evento] ENTRADA KAS @ 0.03755 (22.00 €, apertura)
- 2026-10-02 03:10 [estocastico_rebote] CIERRE XMR timeout bruto -0.19% neto -0.69%
- 2026-10-02 03:05 [c_banda_atr] ENTRADA SPX @ 0.394 (22.12 €, apertura)
- 2026-10-02 03:05 [macd_momentum] ENTRADA SPX @ 0.394 (21.48 €, apertura)
- 2026-10-02 03:05 [macd_momentum_regimen] ENTRADA SPX @ 0.394 (22.07 €, apertura)
- 2026-10-02 03:05 [c_banda_atr_evento] ENTRADA SPX @ 0.394 (22.26 €, apertura)
- 2026-10-02 03:05 [macd_momentum_evento] ENTRADA SPX @ 0.394 (21.60 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
