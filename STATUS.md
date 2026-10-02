# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 04:01 UTC · vueltas 383 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.11 € (-4.23%) | 296 | 26 | 35% | +0.004% | -0.585% | -0.705% | -39.31 € |
| reversion_bb | 919.41 € (-0.52%) | 70 | 3 | 60% | +0.530% | -0.343% | -0.445% | -5.55 € |
| ruptura_volumen | 866.21 € (-6.28%) | 341 | 25 | 25% | -0.173% | -0.750% | -0.858% | -57.46 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.57 € (-3.75%) | 199 | 13 | 16% | -0.160% | -0.793% | -0.881% | -35.81 € |
| macd_momentum | 858.42 € (-7.12%) | 561 | 11 | 21% | +0.011% | -0.536% | -0.637% | -67.04 € |
| estocastico_rebote | 873.23 € (-5.52%) | 351 | 22 | 32% | -0.078% | -0.653% | -0.762% | -51.71 € |
| ruptura_estricta | 881.95 € (-4.58%) | 180 | 20 | 27% | -0.377% | -1.023% | -1.140% | -41.90 € |
| macd_sin_salida | 875.27 € (-5.30%) | 373 | 32 | 35% | -0.049% | -0.619% | -0.729% | -52.17 € |
| c_banda_atr_tope | 912.33 € (-1.29%) | 68 | 5 | 32% | +0.108% | -0.780% | -0.894% | -12.20 € |
| ruptura_volumen_tope | 902.94 € (-2.30%) | 114 | 4 | 25% | -0.076% | -0.807% | -0.922% | -21.05 € |
| c_banda_atr_regimen | 897.47 € (-2.90%) | 142 | 33 | 30% | -0.202% | -0.886% | -1.018% | -28.75 € |
| macd_momentum_regimen | 881.40 € (-4.64%) | 324 | 11 | 19% | -0.021% | -0.602% | -0.705% | -44.08 € |
| ruptura_volumen_regimen | 870.88 € (-5.77%) | 266 | 23 | 21% | -0.287% | -0.885% | -0.997% | -53.01 € |
| c_banda_atr_evento | 891.00 € (-3.60%) | 263 | 26 | 36% | +0.043% | -0.558% | -0.673% | -33.42 € |
| macd_momentum_evento | 863.17 € (-6.61%) | 514 | 11 | 19% | +0.009% | -0.542% | -0.640% | -62.30 € |
| ruptura_volumen_evento | 878.53 € (-4.95%) | 291 | 25 | 26% | -0.096% | -0.686% | -0.787% | -45.12 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-02 03:55 | macd_momentum_regimen | AAVE | momentum perdido | -1.03% | -1.53% | -0.34 |
| 2026-10-02 03:55 | ruptura_volumen_tope | ETH | timeout | +0.01% | -0.48% | -0.11 |
| 2026-10-02 03:55 | macd_sin_salida | MON | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 03:55 | macd_sin_salida | TAO | timeout | +0.80% | +0.30% | +0.06 |
| 2026-10-02 03:55 | ruptura_estricta | HYPE | timeout | +0.59% | +0.09% | +0.02 |

## Eventos de la última vuelta

- 2026-10-02 03:55 [macd_momentum] ENTRADA SOL @ 107.46 (21.43 €, apertura)
- 2026-10-02 03:55 [macd_sin_salida] ENTRADA SOL @ 107.46 (21.80 €, apertura)
- 2026-10-02 03:55 [macd_momentum_regimen] ENTRADA SOL @ 107.46 (22.00 €, apertura)
- 2026-10-02 03:55 [macd_momentum_evento] ENTRADA SOL @ 107.46 (21.55 €, apertura)
- 2026-10-02 04:00 [estocastico_rebote] CIERRE AVAX timeout bruto +0.27% neto -0.23%
- 2026-10-02 04:00 [estocastico_rebote] CIERRE PUMP take-profit bruto +1.80% neto +1.30%
- 2026-10-02 03:55 [c_banda_atr] ENTRADA HYPE @ 78.97 (22.12 €, apertura)
- 2026-10-02 03:55 [c_banda_atr_regimen] ENTRADA HYPE @ 78.97 (22.39 €, apertura)
- 2026-10-02 03:55 [c_banda_atr_evento] ENTRADA HYPE @ 78.97 (22.27 €, apertura)
- 2026-10-02 04:00 [ruptura_estricta] CIERRE INJ timeout bruto -0.06% neto -0.56%
- 2026-10-02 03:55 [estocastico_rebote] ENTRADA TRUMP @ 1.836 (21.81 €, apertura)
- 2026-10-02 04:00 [estocastico_rebote] CIERRE SKY timeout bruto +0.23% neto -0.27%
- 2026-10-02 03:55 [pullback_tendencia] ENTRADA APT @ 0.7101 (22.21 €, apertura)
- 2026-10-02 03:55 [pullback_tendencia] ENTRADA SPX @ 0.3928 (22.21 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
