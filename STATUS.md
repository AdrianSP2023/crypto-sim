# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 02:56 UTC · vueltas 370 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.78 € (-4.16%) | 290 | 24 | 35% | -0.008% | -0.598% | -0.718% | -39.37 € |
| reversion_bb | 919.70 € (-0.49%) | 63 | 9 | 56% | +0.466% | -0.449% | -0.556% | -6.52 € |
| ruptura_volumen | 867.26 € (-6.16%) | 335 | 19 | 25% | -0.182% | -0.760% | -0.868% | -57.18 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.40 € (-3.77%) | 195 | 11 | 15% | -0.178% | -0.813% | -0.902% | -35.98 € |
| macd_momentum | 862.68 € (-6.66%) | 529 | 30 | 20% | -0.002% | -0.552% | -0.654% | -65.17 € |
| estocastico_rebote | 873.16 € (-5.53%) | 344 | 14 | 32% | -0.092% | -0.668% | -0.776% | -51.82 € |
| ruptura_estricta | 883.29 € (-4.43%) | 169 | 27 | 25% | -0.452% | -1.108% | -1.225% | -42.57 € |
| macd_sin_salida | 875.14 € (-5.31%) | 363 | 38 | 34% | -0.069% | -0.641% | -0.753% | -52.57 € |
| c_banda_atr_tope | 912.37 € (-1.28%) | 67 | 5 | 31% | +0.080% | -0.815% | -0.929% | -12.54 € |
| ruptura_volumen_tope | 903.61 € (-2.23%) | 111 | 5 | 25% | -0.080% | -0.818% | -0.933% | -20.77 € |
| c_banda_atr_regimen | 897.15 € (-2.93%) | 140 | 28 | 29% | -0.208% | -0.895% | -1.028% | -28.64 € |
| macd_momentum_regimen | 885.17 € (-4.23%) | 296 | 26 | 19% | -0.030% | -0.618% | -0.724% | -41.43 € |
| ruptura_volumen_regimen | 871.84 € (-5.67%) | 262 | 15 | 21% | -0.291% | -0.891% | -1.004% | -52.60 € |
| c_banda_atr_evento | 891.67 € (-3.52%) | 257 | 24 | 36% | +0.031% | -0.572% | -0.687% | -33.48 € |
| macd_momentum_evento | 867.46 € (-6.14%) | 482 | 30 | 19% | -0.005% | -0.560% | -0.659% | -60.41 € |
| ruptura_volumen_evento | 879.60 € (-4.83%) | 285 | 19 | 26% | -0.104% | -0.696% | -0.797% | -44.84 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 02:55 | ruptura_volumen_evento | HYPE | timeout | +0.04% | -0.46% | -0.10 |
| 2026-10-02 02:55 | macd_momentum_evento | SHIB | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-10-02 02:55 | macd_momentum_evento | WLD | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 02:55 | ruptura_volumen_regimen | HYPE | timeout | +0.04% | -0.46% | -0.10 |
| 2026-10-02 02:55 | macd_momentum_regimen | SHIB | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-10-02 02:55 | macd_momentum_regimen | WLD | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 02:55 | macd_sin_salida | POL | timeout | +1.20% | +0.70% | +0.15 |
| 2026-10-02 02:55 | ruptura_estricta | WLFI | timeout | -0.40% | -0.90% | -0.20 |
| 2026-10-02 02:55 | macd_momentum | SHIB | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-10-02 02:55 | macd_momentum | WLD | momentum perdido | -0.07% | -0.57% | -0.12 |
| 2026-10-02 02:55 | ruptura_volumen | HYPE | timeout | +0.04% | -0.46% | -0.10 |
| 2026-10-02 02:45 | ruptura_volumen_evento | DASH | timeout | -0.26% | -0.76% | -0.17 |
| 2026-10-02 02:45 | ruptura_volumen_evento | MINA | timeout | +2.34% | +1.84% | +0.41 |
| 2026-10-02 02:45 | macd_momentum_evento | ARB | momentum perdido | -0.11% | -0.61% | -0.13 |
| 2026-10-02 02:45 | macd_momentum_evento | ETH | momentum perdido | -0.09% | -0.59% | -0.13 |

## Eventos de la última vuelta

- 2026-10-02 02:50 [ruptura_volumen] ENTRADA HBAR @ 0.09248 (21.68 €, apertura)
- 2026-10-02 02:50 [ruptura_estricta] ENTRADA HBAR @ 0.09248 (22.05 €, apertura)
- 2026-10-02 02:50 [ruptura_volumen_regimen] ENTRADA HBAR @ 0.09248 (21.79 €, apertura)
- 2026-10-02 02:50 [ruptura_volumen_evento] ENTRADA HBAR @ 0.09248 (21.99 €, apertura)
- 2026-10-02 02:55 [ruptura_volumen] CIERRE HYPE timeout bruto +0.04% neto -0.46%
- 2026-10-02 02:55 [ruptura_volumen_regimen] CIERRE HYPE timeout bruto +0.04% neto -0.46%
- 2026-10-02 02:55 [ruptura_volumen_evento] CIERRE HYPE timeout bruto +0.04% neto -0.46%
- 2026-10-02 02:50 [c_banda_atr] ENTRADA ARB @ 0.1806 (22.12 €, apertura)
- 2026-10-02 02:50 [c_banda_atr_regimen] ENTRADA ARB @ 0.1806 (22.39 €, apertura)
- 2026-10-02 02:50 [c_banda_atr_evento] ENTRADA ARB @ 0.1806 (22.27 €, apertura)
- 2026-10-02 02:55 [macd_sin_salida] CIERRE POL timeout bruto +1.20% neto +0.70%
- 2026-10-02 02:55 [macd_momentum] CIERRE WLD momentum perdido bruto -0.07% neto -0.57%
- 2026-10-02 02:55 [macd_momentum_regimen] CIERRE WLD momentum perdido bruto -0.07% neto -0.57%
- 2026-10-02 02:55 [macd_momentum_evento] CIERRE WLD momentum perdido bruto -0.07% neto -0.57%
- 2026-10-02 02:50 [c_banda_atr] ENTRADA OP @ 0.1165 (22.12 €, apertura)
- 2026-10-02 02:50 [c_banda_atr_regimen] ENTRADA OP @ 0.1165 (22.39 €, apertura)
- 2026-10-02 02:50 [macd_momentum_regimen] ENTRADA OP @ 0.1165 (22.07 €, apertura)
- 2026-10-02 02:50 [ruptura_volumen_regimen] ENTRADA OP @ 0.1165 (21.79 €, apertura)
- 2026-10-02 02:50 [c_banda_atr_evento] ENTRADA OP @ 0.1165 (22.27 €, apertura)
- 2026-10-02 02:55 [ruptura_estricta] CIERRE WLFI timeout bruto -0.40% neto -0.90%
- 2026-10-02 02:55 [macd_momentum] CIERRE SHIB momentum perdido bruto +0.04% neto -0.46%
- 2026-10-02 02:55 [macd_momentum_regimen] CIERRE SHIB momentum perdido bruto +0.04% neto -0.46%
- 2026-10-02 02:55 [macd_momentum_evento] CIERRE SHIB momentum perdido bruto +0.04% neto -0.46%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
