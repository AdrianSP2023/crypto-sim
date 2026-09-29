# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 22:21 UTC · vueltas 152 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.74 € (-1.89%) | 66 | 20 | 32% | -0.188% | -1.084% | -1.228% | -16.47 € |
| reversion_bb | 917.75 € (-0.70%) | 18 | 3 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 903.63 € (-2.23%) | 105 | 7 | 24% | -0.127% | -0.876% | -1.005% | -21.07 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.89 € (-1.99%) | 82 | 3 | 23% | -0.173% | -0.991% | -1.114% | -18.64 € |
| macd_momentum | 892.48 € (-3.44%) | 187 | 17 | 18% | -0.102% | -0.742% | -0.858% | -31.64 € |
| estocastico_rebote | 892.84 € (-3.40%) | 156 | 13 | 31% | -0.219% | -0.886% | -1.007% | -31.59 € |
| ruptura_estricta | 910.00 € (-1.54%) | 46 | 7 | 28% | -0.245% | -1.313% | -1.447% | -13.90 € |
| macd_sin_salida | 902.54 € (-2.35%) | 104 | 32 | 32% | -0.095% | -0.846% | -0.978% | -20.17 € |
| c_banda_atr_tope | 913.09 € (-1.21%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 915.49 € (-0.95%) | 33 | 4 | 15% | -0.071% | -1.171% | -1.287% | -8.90 € |
| c_banda_atr_regimen | 908.05 € (-1.75%) | 53 | 9 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.80 € (-3.29%) | 173 | 0 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 906.70 € (-1.90%) | 86 | 6 | 24% | -0.091% | -0.894% | -1.026% | -17.65 € |
| c_banda_atr_evento | 911.22 € (-1.41%) | 34 | 20 | 26% | -0.431% | -1.531% | -1.689% | -11.99 € |
| macd_momentum_evento | 905.03 € (-2.08%) | 67 | 17 | 10% | -0.346% | -1.240% | -1.356% | -19.09 € |
| ruptura_volumen_evento | 909.40 € (-1.61%) | 46 | 7 | 13% | -0.392% | -1.446% | -1.579% | -15.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 22:20 | ruptura_volumen_evento | BNB | timeout | +0.19% | -0.61% | -0.14 |
| 2026-09-29 22:20 | ruptura_volumen_tope | BNB | timeout | +0.19% | -0.91% | -0.21 |
| 2026-09-29 22:20 | estocastico_rebote | USELESS | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-29 22:20 | pullback_tendencia | FIL | rotura de tendencia | -0.10% | -0.60% | -0.14 |
| 2026-09-29 22:20 | ruptura_volumen | BNB | timeout | +0.19% | -0.31% | -0.07 |
| 2026-09-29 22:15 | ruptura_volumen_evento | AVAX | timeout | +0.56% | -0.24% | -0.06 |
| 2026-09-29 22:15 | ruptura_volumen_tope | AVAX | timeout | +0.56% | -0.55% | -0.12 |
| 2026-09-29 22:15 | ruptura_volumen | AVAX | timeout | +0.56% | +0.06% | +0.01 |
| 2026-09-29 22:10 | c_banda_atr_evento | CRV | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 22:10 | c_banda_atr_tope | CRV | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 22:10 | c_banda_atr | CRV | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 22:05 | c_banda_atr_evento | ARB | timeout | +0.06% | -1.04% | -0.24 |
| 2026-09-29 22:05 | c_banda_atr_evento | UNI | timeout | +0.49% | -0.61% | -0.14 |
| 2026-09-29 22:05 | c_banda_atr_tope | ARB | timeout | +0.06% | -1.04% | -0.24 |
| 2026-09-29 22:05 | c_banda_atr_tope | UNI | timeout | +0.49% | -0.61% | -0.14 |

## Eventos de la última vuelta

- 2026-09-29 22:15 [ruptura_estricta] ENTRADA XLM @ 0.197894 (22.76 €, apertura)
- 2026-09-29 22:15 [ruptura_volumen_tope] ENTRADA XLM @ 0.197894 (22.89 €, apertura)
- 2026-09-29 22:15 [c_banda_atr] ENTRADA ARB @ 0.1829 (22.69 €, apertura)
- 2026-09-29 22:15 [macd_momentum] ENTRADA ARB @ 0.1829 (22.32 €, apertura)
- 2026-09-29 22:15 [c_banda_atr_evento] ENTRADA ARB @ 0.1829 (22.81 €, apertura)
- 2026-09-29 22:15 [macd_momentum_evento] ENTRADA ARB @ 0.1829 (22.63 €, apertura)
- 2026-09-29 22:15 [pullback_tendencia] ENTRADA ICP @ 3.05 (22.64 €, apertura)
- 2026-09-29 22:15 [macd_momentum] ENTRADA VVV @ 23.991 (22.32 €, apertura)
- 2026-09-29 22:15 [macd_momentum_evento] ENTRADA VVV @ 23.991 (22.63 €, apertura)
- 2026-09-29 22:15 [c_banda_atr] ENTRADA VIRTUAL @ 0.6886 (22.69 €, apertura)
- 2026-09-29 22:15 [c_banda_atr_evento] ENTRADA VIRTUAL @ 0.6886 (22.81 €, apertura)
- 2026-09-29 22:20 [estocastico_rebote] CIERRE USELESS take-profit bruto +1.80% neto +1.30%
- 2026-09-29 22:15 [pullback_tendencia] ENTRADA FIL @ 0.951 (22.64 €, apertura)
- 2026-09-29 22:20 [pullback_tendencia] CIERRE FIL rotura de tendencia bruto -0.11% neto -0.61%
- 2026-09-29 22:20 [ruptura_volumen] CIERRE BNB timeout bruto +0.19% neto -0.31%
- 2026-09-29 22:20 [ruptura_volumen_tope] CIERRE BNB timeout bruto +0.19% neto -0.91%
- 2026-09-29 22:20 [ruptura_volumen_evento] CIERRE BNB timeout bruto +0.19% neto -0.61%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
