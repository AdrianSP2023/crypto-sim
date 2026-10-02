# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 02:21 UTC · vueltas 363 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.37 € (-3.99%) | 288 | 23 | 35% | -0.009% | -0.599% | -0.720% | -39.22 € |
| reversion_bb | 919.54 € (-0.51%) | 63 | 9 | 56% | +0.466% | -0.449% | -0.556% | -6.52 € |
| ruptura_volumen | 868.03 € (-6.08%) | 327 | 24 | 25% | -0.197% | -0.777% | -0.884% | -57.07 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.01 € (-3.81%) | 194 | 5 | 15% | -0.189% | -0.825% | -0.913% | -36.33 € |
| macd_momentum | 864.52 € (-6.46%) | 518 | 39 | 21% | +0.005% | -0.545% | -0.647% | -63.18 € |
| estocastico_rebote | 873.87 € (-5.45%) | 342 | 13 | 32% | -0.095% | -0.671% | -0.781% | -51.81 € |
| ruptura_estricta | 883.62 € (-4.40%) | 167 | 26 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 875.72 € (-5.25%) | 360 | 40 | 34% | -0.080% | -0.652% | -0.764% | -53.06 € |
| c_banda_atr_tope | 912.34 € (-1.29%) | 66 | 5 | 30% | +0.050% | -0.850% | -0.964% | -12.88 € |
| ruptura_volumen_tope | 903.75 € (-2.22%) | 110 | 5 | 25% | -0.103% | -0.843% | -0.959% | -21.22 € |
| c_banda_atr_regimen | 898.59 € (-2.77%) | 139 | 26 | 29% | -0.197% | -0.885% | -1.018% | -28.14 € |
| macd_momentum_regimen | 887.07 € (-4.02%) | 286 | 33 | 20% | -0.019% | -0.610% | -0.715% | -39.56 € |
| ruptura_volumen_regimen | 872.36 € (-5.61%) | 254 | 19 | 21% | -0.314% | -0.917% | -1.030% | -52.49 € |
| c_banda_atr_evento | 893.28 € (-3.35%) | 255 | 23 | 36% | +0.030% | -0.573% | -0.689% | -33.32 € |
| macd_momentum_evento | 869.31 € (-5.94%) | 471 | 39 | 19% | +0.003% | -0.553% | -0.652% | -58.41 € |
| ruptura_volumen_evento | 880.38 € (-4.75%) | 277 | 24 | 26% | -0.119% | -0.715% | -0.814% | -44.73 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 02:20 | ruptura_volumen_evento | RENDER | timeout | +1.06% | +0.56% | +0.12 |
| 2026-10-02 02:20 | ruptura_volumen_evento | USELESS | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 02:20 | ruptura_volumen_evento | LTC | timeout | +0.21% | -0.29% | -0.06 |
| 2026-10-02 02:20 | ruptura_volumen_evento | SOL | timeout | +0.96% | +0.46% | +0.10 |
| 2026-10-02 02:20 | c_banda_atr_evento | SPX | timeout | +0.71% | +0.21% | +0.05 |
| 2026-10-02 02:20 | ruptura_volumen_regimen | SHIB | timeout | +0.08% | -0.42% | -0.09 |
| 2026-10-02 02:20 | ruptura_volumen_regimen | RENDER | timeout | +1.06% | +0.56% | +0.12 |
| 2026-10-02 02:20 | ruptura_volumen_regimen | USELESS | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 02:20 | ruptura_volumen_regimen | LTC | timeout | +0.21% | -0.29% | -0.06 |
| 2026-10-02 02:20 | ruptura_volumen_regimen | SOL | timeout | +0.96% | +0.46% | +0.10 |
| 2026-10-02 02:20 | ruptura_volumen | RENDER | timeout | +1.06% | +0.56% | +0.12 |
| 2026-10-02 02:20 | ruptura_volumen | USELESS | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 02:20 | ruptura_volumen | LTC | timeout | +0.21% | -0.29% | -0.06 |
| 2026-10-02 02:20 | ruptura_volumen | SOL | timeout | +0.96% | +0.46% | +0.10 |
| 2026-10-02 02:20 | reversion_bb | PEPE | take-profit | +1.62% | +1.12% | +0.26 |

## Eventos de la última vuelta

- 2026-10-02 02:20 [ruptura_volumen] CIERRE SOL timeout bruto +0.96% neto +0.46%
- 2026-10-02 02:20 [ruptura_volumen_regimen] CIERRE SOL timeout bruto +0.96% neto +0.46%
- 2026-10-02 02:20 [ruptura_volumen_evento] CIERRE SOL timeout bruto +0.96% neto +0.46%
- 2026-10-02 02:15 [ruptura_volumen] ENTRADA AVAX @ 9.805 (21.67 €, apertura)
- 2026-10-02 02:15 [ruptura_estricta] ENTRADA AVAX @ 9.805 (22.06 €, apertura)
- 2026-10-02 02:15 [ruptura_volumen_regimen] ENTRADA AVAX @ 9.805 (21.78 €, apertura)
- 2026-10-02 02:15 [ruptura_volumen_evento] ENTRADA AVAX @ 9.805 (21.98 €, apertura)
- 2026-10-02 02:20 [ruptura_volumen] CIERRE LTC timeout bruto +0.21% neto -0.29%
- 2026-10-02 02:20 [ruptura_volumen_regimen] CIERRE LTC timeout bruto +0.21% neto -0.29%
- 2026-10-02 02:20 [ruptura_volumen_evento] CIERRE LTC timeout bruto +0.21% neto -0.29%
- 2026-10-02 02:15 [macd_momentum] ENTRADA ZRO @ 1.643 (21.53 €, apertura)
- 2026-10-02 02:15 [macd_momentum_regimen] ENTRADA ZRO @ 1.643 (22.12 €, apertura)
- 2026-10-02 02:15 [macd_momentum_evento] ENTRADA ZRO @ 1.643 (21.65 €, apertura)
- 2026-10-02 02:20 [ruptura_volumen] CIERRE USELESS take-profit bruto +2.50% neto +2.00%
- 2026-10-02 02:20 [ruptura_volumen_regimen] CIERRE USELESS take-profit bruto +2.50% neto +2.00%
- 2026-10-02 02:20 [ruptura_volumen_evento] CIERRE USELESS take-profit bruto +2.50% neto +2.00%
- 2026-10-02 02:20 [reversion_bb] CIERRE PEPE take-profit bruto +1.62% neto +1.12%
- 2026-10-02 02:20 [ruptura_volumen] CIERRE RENDER timeout bruto +1.06% neto +0.56%
- 2026-10-02 02:15 [ruptura_estricta] ENTRADA RENDER @ 1.72 (22.06 €, apertura)
- 2026-10-02 02:20 [ruptura_volumen_regimen] CIERRE RENDER timeout bruto +1.06% neto +0.56%
- 2026-10-02 02:20 [ruptura_volumen_evento] CIERRE RENDER timeout bruto +1.06% neto +0.56%
- 2026-10-02 02:15 [macd_momentum] ENTRADA INJ @ 6.648 (21.53 €, apertura)
- 2026-10-02 02:15 [macd_momentum_regimen] ENTRADA INJ @ 6.648 (22.12 €, apertura)
- 2026-10-02 02:15 [macd_momentum_evento] ENTRADA INJ @ 6.648 (21.65 €, apertura)
- 2026-10-02 02:20 [ruptura_volumen_regimen] CIERRE SHIB timeout bruto +0.08% neto -0.42%
- 2026-10-02 02:20 [c_banda_atr] CIERRE SPX timeout bruto +0.71% neto +0.21%
- 2026-10-02 02:20 [c_banda_atr_evento] CIERRE SPX timeout bruto +0.71% neto +0.21%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
