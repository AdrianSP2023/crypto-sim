# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 09:56 UTC · vueltas 408 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.42 € (-3.66%) | 341 | 24 | 40% | +0.136% | -0.441% | -0.561% | -34.27 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 860.29 € (-6.92%) | 429 | 19 | 27% | -0.105% | -0.665% | -0.775% | -63.88 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 890.19 € (-3.68%) | 247 | 9 | 21% | -0.020% | -0.627% | -0.714% | -35.15 € |
| macd_momentum | 852.43 € (-7.77%) | 691 | 12 | 23% | +0.061% | -0.477% | -0.578% | -73.29 € |
| estocastico_rebote | 881.22 € (-4.66%) | 421 | 30 | 37% | +0.092% | -0.470% | -0.577% | -44.88 € |
| ruptura_estricta | 882.57 € (-4.51%) | 237 | 12 | 32% | -0.154% | -0.765% | -0.882% | -41.27 € |
| macd_sin_salida | 881.19 € (-4.66%) | 448 | 32 | 40% | +0.106% | -0.452% | -0.562% | -46.03 € |
| c_banda_atr_tope | 913.47 € (-1.17%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 899.96 € (-2.63%) | 133 | 0 | 23% | -0.101% | -0.800% | -0.912% | -24.29 € |
| c_banda_atr_regimen | 903.06 € (-2.29%) | 193 | 24 | 40% | +0.146% | -0.489% | -0.617% | -21.72 € |
| macd_momentum_regimen | 875.25 € (-5.30%) | 454 | 12 | 24% | +0.064% | -0.494% | -0.595% | -50.48 € |
| ruptura_volumen_regimen | 864.96 € (-6.41%) | 352 | 19 | 24% | -0.175% | -0.749% | -0.864% | -59.21 € |
| c_banda_atr_evento | 896.35 € (-3.02%) | 308 | 24 | 41% | +0.183% | -0.402% | -0.518% | -28.35 € |
| macd_momentum_evento | 857.15 € (-7.26%) | 644 | 12 | 23% | +0.063% | -0.478% | -0.576% | -68.57 € |
| ruptura_volumen_evento | 872.53 € (-5.59%) | 379 | 19 | 27% | -0.036% | -0.605% | -0.709% | -51.63 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 09:55 | ruptura_volumen_evento | POL | timeout | -0.29% | -0.80% | -0.17 |
| 2026-10-02 09:55 | ruptura_volumen_regimen | POL | timeout | -0.29% | -0.80% | -0.17 |
| 2026-10-02 09:55 | ruptura_volumen_tope | POL | timeout | -0.29% | -0.80% | -0.18 |
| 2026-10-02 09:55 | estocastico_rebote | VVV | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-02 09:55 | pullback_tendencia | VVV | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 09:55 | ruptura_volumen | POL | timeout | -0.29% | -0.80% | -0.17 |
| 2026-10-02 09:50 | ruptura_volumen_evento | CRV | timeout | +0.32% | -0.18% | -0.04 |
| 2026-10-02 09:50 | ruptura_volumen_evento | DOT | timeout | -0.47% | -0.97% | -0.21 |
| 2026-10-02 09:50 | macd_momentum_evento | ZEC | momentum perdido | -0.45% | -0.95% | -0.20 |
| 2026-10-02 09:50 | ruptura_volumen_regimen | CRV | timeout | +0.32% | -0.18% | -0.04 |
| 2026-10-02 09:50 | ruptura_volumen_regimen | DOT | timeout | -0.47% | -0.97% | -0.21 |
| 2026-10-02 09:50 | macd_momentum_regimen | ZEC | momentum perdido | -0.45% | -0.95% | -0.21 |
| 2026-10-02 09:50 | ruptura_volumen_tope | CRV | timeout | +0.32% | -0.18% | -0.04 |
| 2026-10-02 09:50 | ruptura_volumen_tope | DOT | timeout | -0.47% | -0.97% | -0.22 |
| 2026-10-02 09:50 | macd_momentum | ZEC | momentum perdido | -0.45% | -0.95% | -0.20 |

## Eventos de la última vuelta

- 2026-10-02 09:50 [pullback_tendencia] ENTRADA ETH @ 2442.23 (22.22 €, apertura)
- 2026-10-02 09:55 [ruptura_volumen] CIERRE POL timeout bruto -0.29% neto -0.79%
- 2026-10-02 09:55 [ruptura_volumen_tope] CIERRE POL timeout bruto -0.29% neto -0.79%
- 2026-10-02 09:55 [ruptura_volumen_regimen] CIERRE POL timeout bruto -0.29% neto -0.79%
- 2026-10-02 09:55 [ruptura_volumen_evento] CIERRE POL timeout bruto -0.29% neto -0.79%
- 2026-10-02 09:50 [estocastico_rebote] ENTRADA JUP @ 0.2932 (21.98 €, apertura)
- 2026-10-02 09:55 [pullback_tendencia] CIERRE VVV take-profit bruto +2.00% neto +1.50%
- 2026-10-02 09:55 [estocastico_rebote] CIERRE VVV take-profit bruto +1.80% neto +1.30%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
