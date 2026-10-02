# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 04:06 UTC · vueltas 384 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.71 € (-4.17%) | 296 | 27 | 35% | +0.004% | -0.585% | -0.705% | -39.31 € |
| reversion_bb | 919.57 € (-0.51%) | 70 | 3 | 60% | +0.530% | -0.343% | -0.445% | -5.55 € |
| ruptura_volumen | 866.81 € (-6.21%) | 341 | 25 | 25% | -0.173% | -0.750% | -0.858% | -57.46 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.65 € (-3.74%) | 199 | 14 | 16% | -0.160% | -0.793% | -0.881% | -35.81 € |
| macd_momentum | 858.61 € (-7.10%) | 562 | 11 | 21% | +0.011% | -0.535% | -0.637% | -67.13 € |
| estocastico_rebote | 873.59 € (-5.48%) | 351 | 22 | 32% | -0.078% | -0.653% | -0.762% | -51.71 € |
| ruptura_estricta | 882.59 € (-4.51%) | 180 | 21 | 27% | -0.377% | -1.023% | -1.140% | -41.90 € |
| macd_sin_salida | 876.10 € (-5.21%) | 374 | 31 | 35% | -0.043% | -0.613% | -0.723% | -51.85 € |
| c_banda_atr_tope | 912.37 € (-1.28%) | 68 | 5 | 32% | +0.108% | -0.780% | -0.894% | -12.20 € |
| ruptura_volumen_tope | 903.24 € (-2.27%) | 114 | 5 | 25% | -0.076% | -0.807% | -0.922% | -21.05 € |
| c_banda_atr_regimen | 898.34 € (-2.80%) | 143 | 33 | 30% | -0.186% | -0.869% | -1.001% | -28.41 € |
| macd_momentum_regimen | 881.60 € (-4.61%) | 325 | 11 | 19% | -0.021% | -0.601% | -0.705% | -44.17 € |
| ruptura_volumen_regimen | 871.33 € (-5.72%) | 266 | 23 | 21% | -0.287% | -0.885% | -0.997% | -53.01 € |
| c_banda_atr_evento | 891.60 € (-3.53%) | 263 | 27 | 36% | +0.043% | -0.558% | -0.673% | -33.42 € |
| macd_momentum_evento | 863.37 € (-6.59%) | 515 | 11 | 19% | +0.009% | -0.542% | -0.640% | -62.39 € |
| ruptura_volumen_evento | 879.15 € (-4.88%) | 291 | 25 | 26% | -0.096% | -0.686% | -0.787% | -45.12 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 04:05 | macd_momentum_evento | SPX | momentum perdido | +0.08% | -0.42% | -0.09 |
| 2026-10-02 04:05 | macd_momentum_regimen | SPX | momentum perdido | +0.08% | -0.42% | -0.09 |
| 2026-10-02 04:05 | c_banda_atr_regimen | FET | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 04:05 | macd_sin_salida | FET | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 04:05 | macd_momentum | SPX | momentum perdido | +0.08% | -0.42% | -0.09 |
| 2026-10-02 04:00 | ruptura_estricta | INJ | timeout | -0.06% | -0.56% | -0.12 |
| 2026-10-02 04:00 | estocastico_rebote | SKY | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-02 04:00 | estocastico_rebote | PUMP | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 04:00 | estocastico_rebote | AVAX | timeout | +0.27% | -0.23% | -0.05 |
| 2026-10-02 03:55 | ruptura_volumen_evento | ZEC | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 03:55 | ruptura_volumen_evento | ETH | timeout | +0.01% | -0.48% | -0.11 |
| 2026-10-02 03:55 | macd_momentum_evento | AAVE | momentum perdido | -1.03% | -1.53% | -0.33 |
| 2026-10-02 03:55 | c_banda_atr_evento | VVV | timeout | +1.57% | +1.07% | +0.24 |
| 2026-10-02 03:55 | ruptura_volumen_regimen | ZEC | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 03:55 | ruptura_volumen_regimen | ETH | timeout | +0.01% | -0.48% | -0.11 |

## Eventos de la última vuelta

- 2026-10-02 04:00 [macd_momentum] ENTRADA AAVE @ 156.69 (21.43 €, apertura)
- 2026-10-02 04:00 [macd_momentum_regimen] ENTRADA AAVE @ 156.69 (22.00 €, apertura)
- 2026-10-02 04:00 [macd_momentum_evento] ENTRADA AAVE @ 156.69 (21.55 €, apertura)
- 2026-10-02 04:00 [pullback_tendencia] ENTRADA LTC @ 61.15 (22.21 €, apertura)
- 2026-10-02 04:05 [macd_sin_salida] CIERRE FET take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:05 [c_banda_atr_regimen] CIERRE FET take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:00 [c_banda_atr] ENTRADA PENGU @ 0.00852 (22.12 €, apertura)
- 2026-10-02 04:00 [c_banda_atr_regimen] ENTRADA PENGU @ 0.00852 (22.40 €, apertura)
- 2026-10-02 04:00 [c_banda_atr_evento] ENTRADA PENGU @ 0.00852 (22.27 €, apertura)
- 2026-10-02 04:00 [ruptura_estricta] ENTRADA TON @ 1.399 (22.06 €, apertura)
- 2026-10-02 04:00 [ruptura_volumen_tope] ENTRADA TON @ 1.399 (22.58 €, apertura)
- 2026-10-02 04:05 [macd_momentum] CIERRE SPX momentum perdido bruto +0.08% neto -0.42%
- 2026-10-02 04:05 [macd_momentum_regimen] CIERRE SPX momentum perdido bruto +0.08% neto -0.42%
- 2026-10-02 04:05 [macd_momentum_evento] CIERRE SPX momentum perdido bruto +0.08% neto -0.42%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
