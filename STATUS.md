# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 00:46 UTC · vueltas 344 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.78 € (-4.16%) | 272 | 22 | 34% | -0.047% | -0.643% | -0.765% | -39.74 € |
| reversion_bb | 918.23 € (-0.65%) | 53 | 16 | 51% | +0.343% | -0.650% | -0.747% | -7.94 € |
| ruptura_volumen | 870.97 € (-5.76%) | 300 | 26 | 24% | -0.201% | -0.788% | -0.896% | -53.22 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.66 € (-3.85%) | 190 | 5 | 15% | -0.201% | -0.840% | -0.929% | -36.21 € |
| macd_momentum | 863.42 € (-6.58%) | 497 | 10 | 20% | -0.008% | -0.560% | -0.663% | -62.30 € |
| estocastico_rebote | 873.55 € (-5.48%) | 334 | 13 | 31% | -0.106% | -0.684% | -0.794% | -51.54 € |
| ruptura_estricta | 882.36 € (-4.53%) | 167 | 5 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 872.45 € (-5.60%) | 350 | 15 | 34% | -0.089% | -0.664% | -0.775% | -52.49 € |
| c_banda_atr_tope | 911.78 € (-1.35%) | 62 | 5 | 31% | +0.026% | -0.900% | -1.015% | -12.81 € |
| ruptura_volumen_tope | 905.15 € (-2.07%) | 103 | 5 | 26% | -0.041% | -0.797% | -0.913% | -18.80 € |
| c_banda_atr_regimen | 896.02 € (-3.05%) | 138 | 5 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 885.44 € (-4.20%) | 278 | 3 | 19% | -0.029% | -0.623% | -0.728% | -39.27 € |
| ruptura_volumen_regimen | 874.37 € (-5.40%) | 231 | 23 | 19% | -0.342% | -0.955% | -1.069% | -49.79 € |
| c_banda_atr_evento | 891.67 € (-3.52%) | 239 | 22 | 34% | -0.011% | -0.622% | -0.738% | -33.85 € |
| macd_momentum_evento | 868.20 € (-6.06%) | 450 | 10 | 18% | -0.011% | -0.570% | -0.669% | -57.53 € |
| ruptura_volumen_evento | 883.36 € (-4.42%) | 250 | 26 | 25% | -0.115% | -0.721% | -0.821% | -40.82 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 00:45 | ruptura_volumen_evento | SKY | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 00:45 | macd_momentum_evento | POL | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-02 00:45 | macd_momentum_evento | AVAX | momentum perdido | -0.16% | -0.66% | -0.14 |
| 2026-10-02 00:45 | macd_momentum_evento | ETH | momentum perdido | +0.23% | -0.27% | -0.06 |
| 2026-10-02 00:45 | ruptura_volumen_regimen | SKY | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 00:45 | macd_momentum_regimen | ETH | momentum perdido | +0.05% | -0.45% | -0.10 |
| 2026-10-02 00:45 | macd_sin_salida | WLFI | timeout | +0.61% | +0.11% | +0.02 |
| 2026-10-02 00:45 | macd_sin_salida | AAVE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:45 | ruptura_estricta | SKY | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-02 00:45 | macd_momentum | POL | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-02 00:45 | macd_momentum | AVAX | momentum perdido | -0.16% | -0.66% | -0.14 |
| 2026-10-02 00:45 | macd_momentum | ETH | momentum perdido | +0.23% | -0.27% | -0.06 |
| 2026-10-02 00:45 | ruptura_volumen | SKY | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 00:40 | ruptura_volumen_evento | ETH | timeout | +0.04% | -0.46% | -0.10 |
| 2026-10-02 00:40 | macd_momentum_evento | WLFI | momentum perdido | +0.00% | -0.50% | -0.11 |

## Eventos de la última vuelta

- 2026-10-02 00:45 [macd_momentum] CIERRE ETH momentum perdido bruto +0.23% neto -0.27%
- 2026-10-02 00:45 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto +0.05% neto -0.45%
- 2026-10-02 00:45 [macd_momentum_evento] CIERRE ETH momentum perdido bruto +0.23% neto -0.27%
- 2026-10-02 00:45 [macd_momentum] CIERRE AVAX momentum perdido bruto -0.16% neto -0.66%
- 2026-10-02 00:45 [macd_momentum_evento] CIERRE AVAX momentum perdido bruto -0.16% neto -0.66%
- 2026-10-02 00:45 [macd_sin_salida] CIERRE AAVE take-profit bruto +2.00% neto +1.50%
- 2026-10-02 00:40 [c_banda_atr] ENTRADA TRX @ 0.297531 (22.11 €, apertura)
- 2026-10-02 00:40 [c_banda_atr_tope] ENTRADA TRX @ 0.297531 (22.79 €, apertura)
- 2026-10-02 00:40 [c_banda_atr_regimen] ENTRADA TRX @ 0.297531 (22.39 €, apertura)
- 2026-10-02 00:40 [c_banda_atr_evento] ENTRADA TRX @ 0.297531 (22.26 €, apertura)
- 2026-10-02 00:45 [macd_momentum] CIERRE POL momentum perdido bruto -0.24% neto -0.74%
- 2026-10-02 00:45 [macd_momentum_evento] CIERRE POL momentum perdido bruto -0.24% neto -0.74%
- 2026-10-02 00:45 [macd_sin_salida] CIERRE WLFI timeout bruto +0.61% neto +0.11%
- 2026-10-02 00:45 [ruptura_volumen] CIERRE SKY stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 00:45 [ruptura_estricta] CIERRE SKY stop-loss bruto -2.00% neto -2.50%
- 2026-10-02 00:45 [ruptura_volumen_regimen] CIERRE SKY stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 00:45 [ruptura_volumen_evento] CIERRE SKY stop-loss bruto -1.20% neto -1.70%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
