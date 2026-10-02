# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 07:51 UTC · vueltas 383 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.24 € (-3.79%) | 333 | 18 | 39% | +0.124% | -0.454% | -0.575% | -34.48 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 862.75 € (-6.65%) | 411 | 6 | 27% | -0.112% | -0.676% | -0.784% | -62.21 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.38 € (-3.77%) | 237 | 6 | 20% | -0.036% | -0.647% | -0.733% | -34.84 € |
| macd_momentum | 853.68 € (-7.63%) | 645 | 8 | 22% | +0.046% | -0.494% | -0.596% | -70.98 € |
| estocastico_rebote | 878.62 € (-4.94%) | 386 | 40 | 36% | +0.038% | -0.529% | -0.637% | -46.27 € |
| ruptura_estricta | 882.68 € (-4.50%) | 231 | 5 | 32% | -0.185% | -0.799% | -0.913% | -41.99 € |
| macd_sin_salida | 879.68 € (-4.82%) | 432 | 18 | 40% | +0.113% | -0.447% | -0.558% | -44.02 € |
| c_banda_atr_tope | 913.09 € (-1.21%) | 76 | 5 | 37% | +0.213% | -0.634% | -0.750% | -11.08 € |
| ruptura_volumen_tope | 901.41 € (-2.47%) | 126 | 3 | 25% | -0.078% | -0.787% | -0.901% | -22.68 € |
| c_banda_atr_regimen | 901.70 € (-2.44%) | 185 | 18 | 40% | +0.131% | -0.510% | -0.640% | -21.73 € |
| macd_momentum_regimen | 876.54 € (-5.16%) | 408 | 8 | 22% | +0.041% | -0.523% | -0.626% | -48.11 € |
| ruptura_volumen_regimen | 867.44 € (-6.15%) | 334 | 6 | 24% | -0.189% | -0.767% | -0.880% | -57.53 € |
| c_banda_atr_evento | 895.16 € (-3.15%) | 300 | 18 | 40% | +0.172% | -0.416% | -0.533% | -28.56 € |
| macd_momentum_evento | 858.41 € (-7.12%) | 598 | 8 | 21% | +0.048% | -0.497% | -0.595% | -66.25 € |
| ruptura_volumen_evento | 875.03 € (-5.32%) | 361 | 6 | 27% | -0.041% | -0.614% | -0.717% | -49.94 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 07:50 | ruptura_volumen_evento | MINA | take-profit | +2.56% | +2.06% | +0.45 |
| 2026-10-02 07:50 | ruptura_volumen_regimen | MINA | take-profit | +2.56% | +2.06% | +0.45 |
| 2026-10-02 07:50 | ruptura_estricta | APT | timeout | -0.01% | -0.51% | -0.11 |
| 2026-10-02 07:50 | ruptura_estricta | KAS | timeout | -1.03% | -1.53% | -0.34 |
| 2026-10-02 07:50 | rebote_extremo | QNT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-10-02 07:50 | ruptura_volumen | MINA | take-profit | +2.56% | +2.06% | +0.44 |
| 2026-10-02 07:45 | ruptura_volumen_evento | XMR | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 07:45 | ruptura_volumen_regimen | XMR | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 07:45 | ruptura_volumen_tope | XMR | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 07:45 | ruptura_volumen | XMR | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 07:40 | ruptura_volumen_evento | MON | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:40 | ruptura_volumen_regimen | MON | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:40 | ruptura_volumen_tope | MON | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 07:40 | pullback_tendencia | ADA | rotura de tendencia | -0.65% | -1.15% | -0.26 |
| 2026-10-02 07:40 | ruptura_volumen | MON | stop-loss | -1.20% | -1.70% | -0.37 |

## Eventos de la última vuelta

- 2026-10-02 07:50 [rebote_extremo] CIERRE QNT take-profit bruto +2.00% neto +0.90%
- 2026-10-02 07:45 [macd_momentum] ENTRADA FET @ 0.2102 (21.33 €, apertura)
- 2026-10-02 07:45 [macd_momentum_regimen] ENTRADA FET @ 0.2102 (21.90 €, apertura)
- 2026-10-02 07:45 [macd_momentum_evento] ENTRADA FET @ 0.2102 (21.45 €, apertura)
- 2026-10-02 07:45 [macd_momentum] ENTRADA POL @ 0.098 (21.33 €, apertura)
- 2026-10-02 07:45 [macd_sin_salida] ENTRADA POL @ 0.098 (22.01 €, apertura)
- 2026-10-02 07:45 [macd_momentum_regimen] ENTRADA POL @ 0.098 (21.90 €, apertura)
- 2026-10-02 07:45 [macd_momentum_evento] ENTRADA POL @ 0.098 (21.45 €, apertura)
- 2026-10-02 07:45 [macd_momentum] ENTRADA CRV @ 0.33768 (21.33 €, apertura)
- 2026-10-02 07:45 [macd_momentum_regimen] ENTRADA CRV @ 0.33768 (21.90 €, apertura)
- 2026-10-02 07:45 [macd_momentum_evento] ENTRADA CRV @ 0.33768 (21.45 €, apertura)
- 2026-10-02 07:45 [c_banda_atr] ENTRADA USELESS @ 0.22359 (22.24 €, apertura)
- 2026-10-02 07:45 [c_banda_atr_regimen] ENTRADA USELESS @ 0.22359 (22.56 €, apertura)
- 2026-10-02 07:45 [c_banda_atr_evento] ENTRADA USELESS @ 0.22359 (22.39 €, apertura)
- 2026-10-02 07:45 [ruptura_volumen] ENTRADA OP @ 0.1185 (21.54 €, apertura)
- 2026-10-02 07:45 [ruptura_volumen_tope] ENTRADA OP @ 0.1185 (22.54 €, apertura)
- 2026-10-02 07:45 [ruptura_volumen_regimen] ENTRADA OP @ 0.1185 (21.66 €, apertura)
- 2026-10-02 07:45 [ruptura_volumen_evento] ENTRADA OP @ 0.1185 (21.85 €, apertura)
- 2026-10-02 07:50 [ruptura_volumen] CIERRE MINA take-profit bruto +2.56% neto +2.06%
- 2026-10-02 07:50 [ruptura_volumen_regimen] CIERRE MINA take-profit bruto +2.56% neto +2.06%
- 2026-10-02 07:50 [ruptura_volumen_evento] CIERRE MINA take-profit bruto +2.56% neto +2.06%
- 2026-10-02 07:45 [macd_momentum] ENTRADA WLFI @ 0.0499 (21.33 €, apertura)
- 2026-10-02 07:45 [macd_momentum_regimen] ENTRADA WLFI @ 0.0499 (21.90 €, apertura)
- 2026-10-02 07:45 [macd_momentum_evento] ENTRADA WLFI @ 0.0499 (21.45 €, apertura)
- 2026-10-02 07:50 [ruptura_estricta] CIERRE KAS timeout bruto -1.03% neto -1.53%
- 2026-10-02 07:50 [ruptura_estricta] CIERRE APT timeout bruto -0.01% neto -0.51%
- 2026-10-02 07:45 [c_banda_atr] ENTRADA SPX @ 0.4006 (22.24 €, apertura)
- 2026-10-02 07:45 [c_banda_atr_evento] ENTRADA SPX @ 0.4006 (22.39 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
