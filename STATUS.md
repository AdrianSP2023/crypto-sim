# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 02:46 UTC · vueltas 368 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.64 € (-4.18%) | 290 | 22 | 35% | -0.008% | -0.598% | -0.718% | -39.37 € |
| reversion_bb | 919.05 € (-0.56%) | 63 | 9 | 56% | +0.466% | -0.449% | -0.556% | -6.52 € |
| ruptura_volumen | 866.57 € (-6.24%) | 334 | 19 | 25% | -0.182% | -0.760% | -0.869% | -57.08 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.89 € (-3.82%) | 195 | 9 | 15% | -0.178% | -0.813% | -0.902% | -35.98 € |
| macd_momentum | 861.36 € (-6.80%) | 527 | 32 | 20% | -0.002% | -0.552% | -0.654% | -64.95 € |
| estocastico_rebote | 872.63 € (-5.58%) | 344 | 14 | 32% | -0.092% | -0.668% | -0.776% | -51.82 € |
| ruptura_estricta | 882.20 € (-4.55%) | 168 | 27 | 25% | -0.452% | -1.109% | -1.225% | -42.37 € |
| macd_sin_salida | 873.34 € (-5.51%) | 362 | 39 | 34% | -0.072% | -0.644% | -0.757% | -52.72 € |
| c_banda_atr_tope | 912.07 € (-1.32%) | 67 | 5 | 31% | +0.080% | -0.815% | -0.929% | -12.54 € |
| ruptura_volumen_tope | 903.36 € (-2.26%) | 111 | 4 | 25% | -0.080% | -0.818% | -0.933% | -20.77 € |
| c_banda_atr_regimen | 896.62 € (-2.99%) | 140 | 26 | 29% | -0.208% | -0.895% | -1.028% | -28.64 € |
| macd_momentum_regimen | 884.27 € (-4.32%) | 294 | 27 | 19% | -0.030% | -0.619% | -0.724% | -41.20 € |
| ruptura_volumen_regimen | 871.41 € (-5.72%) | 261 | 14 | 21% | -0.293% | -0.893% | -1.006% | -52.50 € |
| c_banda_atr_evento | 891.53 € (-3.54%) | 257 | 22 | 36% | +0.031% | -0.572% | -0.687% | -33.48 € |
| macd_momentum_evento | 866.14 € (-6.29%) | 480 | 32 | 19% | -0.005% | -0.560% | -0.659% | -60.19 € |
| ruptura_volumen_evento | 878.90 € (-4.91%) | 284 | 19 | 26% | -0.104% | -0.697% | -0.798% | -44.73 € |
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

- 2026-10-02 02:45 [macd_momentum] CIERRE ETH momentum perdido bruto -0.09% neto -0.59%
- 2026-10-02 02:45 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto -0.09% neto -0.59%
- 2026-10-02 02:45 [macd_momentum_evento] CIERRE ETH momentum perdido bruto -0.09% neto -0.59%
- 2026-10-02 02:45 [c_banda_atr] CIERRE ZRO stop-loss bruto -1.70% neto -2.20%
- 2026-10-02 02:45 [c_banda_atr_regimen] CIERRE ZRO stop-loss bruto -1.70% neto -2.20%
- 2026-10-02 02:45 [c_banda_atr_evento] CIERRE ZRO stop-loss bruto -1.70% neto -2.20%
- 2026-10-02 02:45 [macd_momentum] CIERRE ARB momentum perdido bruto -0.11% neto -0.61%
- 2026-10-02 02:45 [macd_momentum_regimen] CIERRE ARB momentum perdido bruto -0.11% neto -0.61%
- 2026-10-02 02:45 [macd_momentum_evento] CIERRE ARB momentum perdido bruto -0.11% neto -0.61%
- 2026-10-02 02:45 [c_banda_atr] CIERRE FET take-profit bruto +2.00% neto +1.50%
- 2026-10-02 02:45 [c_banda_atr_tope] CIERRE FET take-profit bruto +2.00% neto +1.50%
- 2026-10-02 02:45 [c_banda_atr_evento] CIERRE FET take-profit bruto +2.00% neto +1.50%
- 2026-10-02 02:45 [ruptura_volumen] CIERRE MINA timeout bruto +2.34% neto +1.84%
- 2026-10-02 02:45 [ruptura_volumen_regimen] CIERRE MINA timeout bruto +2.34% neto +1.84%
- 2026-10-02 02:45 [ruptura_volumen_evento] CIERRE MINA timeout bruto +2.34% neto +1.84%
- 2026-10-02 02:40 [c_banda_atr] ENTRADA WLFI @ 0.0496 (22.12 €, apertura)
- 2026-10-02 02:40 [estocastico_rebote] ENTRADA WLFI @ 0.0496 (21.81 €, apertura)
- 2026-10-02 02:40 [c_banda_atr_tope] ENTRADA WLFI @ 0.0496 (22.79 €, apertura)
- 2026-10-02 02:40 [c_banda_atr_regimen] ENTRADA WLFI @ 0.0496 (22.39 €, apertura)
- 2026-10-02 02:40 [c_banda_atr_evento] ENTRADA WLFI @ 0.0496 (22.27 €, apertura)
- 2026-10-02 02:45 [ruptura_volumen] CIERRE DASH timeout bruto -0.26% neto -0.76%
- 2026-10-02 02:45 [ruptura_volumen_regimen] CIERRE DASH timeout bruto -0.26% neto -0.76%
- 2026-10-02 02:45 [ruptura_volumen_evento] CIERRE DASH timeout bruto -0.26% neto -0.76%
- 2026-10-02 02:40 [macd_momentum] ENTRADA KSM @ 4.54 (21.48 €, apertura)
- 2026-10-02 02:40 [macd_sin_salida] ENTRADA KSM @ 4.54 (21.79 €, apertura)
- 2026-10-02 02:40 [macd_momentum_regimen] ENTRADA KSM @ 4.54 (22.08 €, apertura)
- 2026-10-02 02:40 [macd_momentum_evento] ENTRADA KSM @ 4.54 (21.60 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
