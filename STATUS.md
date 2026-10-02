# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 02:51 UTC · vueltas 369 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.94 € (-4.14%) | 290 | 22 | 35% | -0.008% | -0.598% | -0.718% | -39.37 € |
| reversion_bb | 919.46 € (-0.52%) | 63 | 9 | 56% | +0.466% | -0.449% | -0.556% | -6.52 € |
| ruptura_volumen | 867.11 € (-6.18%) | 334 | 19 | 25% | -0.182% | -0.760% | -0.869% | -57.08 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.41 € (-3.77%) | 195 | 11 | 15% | -0.178% | -0.813% | -0.902% | -35.98 € |
| macd_momentum | 862.49 € (-6.68%) | 527 | 32 | 20% | -0.002% | -0.552% | -0.654% | -64.95 € |
| estocastico_rebote | 872.87 € (-5.56%) | 344 | 14 | 32% | -0.092% | -0.668% | -0.776% | -51.82 € |
| ruptura_estricta | 882.90 € (-4.47%) | 168 | 27 | 25% | -0.452% | -1.109% | -1.225% | -42.37 € |
| macd_sin_salida | 874.66 € (-5.36%) | 362 | 39 | 34% | -0.072% | -0.644% | -0.757% | -52.72 € |
| c_banda_atr_tope | 912.25 € (-1.30%) | 67 | 5 | 31% | +0.080% | -0.815% | -0.929% | -12.54 € |
| ruptura_volumen_tope | 903.63 € (-2.23%) | 111 | 5 | 25% | -0.080% | -0.818% | -0.933% | -20.77 € |
| c_banda_atr_regimen | 897.08 € (-2.94%) | 140 | 26 | 29% | -0.208% | -0.895% | -1.028% | -28.64 € |
| macd_momentum_regimen | 885.09 € (-4.24%) | 294 | 27 | 19% | -0.030% | -0.619% | -0.724% | -41.20 € |
| ruptura_volumen_regimen | 871.71 € (-5.68%) | 261 | 14 | 21% | -0.293% | -0.893% | -1.006% | -52.50 € |
| c_banda_atr_evento | 891.83 € (-3.51%) | 257 | 22 | 36% | +0.031% | -0.572% | -0.687% | -33.48 € |
| macd_momentum_evento | 867.27 € (-6.16%) | 480 | 32 | 19% | -0.005% | -0.560% | -0.659% | -60.19 € |
| ruptura_volumen_evento | 879.45 € (-4.85%) | 284 | 19 | 26% | -0.104% | -0.697% | -0.798% | -44.73 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 02:45 | ruptura_volumen_evento | DASH | timeout | -0.26% | -0.76% | -0.17 |
| 2026-10-02 02:45 | ruptura_volumen_evento | MINA | timeout | +2.34% | +1.84% | +0.41 |
| 2026-10-02 02:45 | macd_momentum_evento | ARB | momentum perdido | -0.11% | -0.61% | -0.13 |
| 2026-10-02 02:45 | macd_momentum_evento | ETH | momentum perdido | -0.09% | -0.59% | -0.13 |
| 2026-10-02 02:45 | c_banda_atr_evento | FET | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 02:45 | c_banda_atr_evento | ZRO | stop-loss | -1.70% | -2.20% | -0.49 |
| 2026-10-02 02:45 | ruptura_volumen_regimen | DASH | timeout | -0.26% | -0.76% | -0.17 |
| 2026-10-02 02:45 | ruptura_volumen_regimen | MINA | timeout | +2.34% | +1.84% | +0.40 |
| 2026-10-02 02:45 | macd_momentum_regimen | ARB | momentum perdido | -0.11% | -0.61% | -0.14 |
| 2026-10-02 02:45 | macd_momentum_regimen | ETH | momentum perdido | -0.09% | -0.59% | -0.13 |
| 2026-10-02 02:45 | c_banda_atr_regimen | ZRO | stop-loss | -1.70% | -2.20% | -0.49 |
| 2026-10-02 02:45 | c_banda_atr_tope | FET | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 02:45 | macd_momentum | ARB | momentum perdido | -0.11% | -0.61% | -0.13 |
| 2026-10-02 02:45 | macd_momentum | ETH | momentum perdido | -0.09% | -0.59% | -0.13 |
| 2026-10-02 02:45 | ruptura_volumen | DASH | timeout | -0.26% | -0.76% | -0.17 |

## Eventos de la última vuelta

- 2026-10-02 02:45 [pullback_tendencia] ENTRADA HYPE @ 78.49 (22.21 €, apertura)
- 2026-10-02 02:45 [ruptura_volumen_tope] ENTRADA ALGO @ 0.11152 (22.59 €, apertura)
- 2026-10-02 02:45 [pullback_tendencia] ENTRADA BNB @ 687.29 (22.21 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
