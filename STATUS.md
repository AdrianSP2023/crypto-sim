# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 00:41 UTC · vueltas 343 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.46 € (-4.20%) | 272 | 21 | 34% | -0.047% | -0.643% | -0.765% | -39.74 € |
| reversion_bb | 918.10 € (-0.66%) | 53 | 16 | 51% | +0.343% | -0.650% | -0.747% | -7.94 € |
| ruptura_volumen | 871.39 € (-5.72%) | 299 | 27 | 24% | -0.197% | -0.784% | -0.893% | -52.85 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.26 € (-3.89%) | 190 | 5 | 15% | -0.201% | -0.840% | -0.929% | -36.21 € |
| macd_momentum | 863.28 € (-6.60%) | 494 | 13 | 20% | -0.007% | -0.560% | -0.663% | -61.94 € |
| estocastico_rebote | 872.80 € (-5.57%) | 334 | 13 | 31% | -0.106% | -0.684% | -0.794% | -51.54 € |
| ruptura_estricta | 882.65 € (-4.50%) | 166 | 6 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 871.82 € (-5.67%) | 348 | 17 | 34% | -0.097% | -0.672% | -0.783% | -52.84 € |
| c_banda_atr_tope | 911.61 € (-1.37%) | 62 | 4 | 31% | +0.026% | -0.900% | -1.015% | -12.81 € |
| ruptura_volumen_tope | 905.39 € (-2.04%) | 103 | 5 | 26% | -0.041% | -0.797% | -0.913% | -18.80 € |
| c_banda_atr_regimen | 895.83 € (-3.07%) | 138 | 4 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 885.04 € (-4.24%) | 277 | 4 | 19% | -0.029% | -0.623% | -0.729% | -39.17 € |
| ruptura_volumen_regimen | 874.69 € (-5.36%) | 230 | 24 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 891.35 € (-3.56%) | 239 | 21 | 34% | -0.011% | -0.622% | -0.738% | -33.85 € |
| macd_momentum_evento | 868.07 € (-6.08%) | 447 | 13 | 19% | -0.011% | -0.570% | -0.670% | -57.17 € |
| ruptura_volumen_evento | 883.78 € (-4.38%) | 249 | 27 | 25% | -0.111% | -0.717% | -0.817% | -40.44 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 00:40 | ruptura_volumen_evento | ETH | timeout | +0.04% | -0.46% | -0.10 |
| 2026-10-02 00:40 | macd_momentum_evento | WLFI | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 00:40 | macd_momentum_evento | ZEC | momentum perdido | -0.23% | -0.72% | -0.16 |
| 2026-10-02 00:40 | macd_momentum_evento | BTC | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-10-02 00:40 | macd_momentum_regimen | ZEC | momentum perdido | -0.23% | -0.72% | -0.16 |
| 2026-10-02 00:40 | ruptura_volumen_tope | ETH | timeout | +0.04% | -0.46% | -0.10 |
| 2026-10-02 00:40 | macd_momentum | WLFI | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 00:40 | macd_momentum | ZEC | momentum perdido | -0.23% | -0.72% | -0.16 |
| 2026-10-02 00:40 | macd_momentum | BTC | momentum perdido | +0.04% | -0.46% | -0.10 |
| 2026-10-02 00:40 | ruptura_volumen | ETH | timeout | +0.04% | -0.46% | -0.10 |
| 2026-10-02 00:35 | ruptura_volumen_evento | WLFI | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 00:35 | ruptura_volumen_tope | WLFI | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 00:35 | c_banda_atr_tope | FET | timeout | +1.52% | +1.02% | +0.23 |
| 2026-10-02 00:35 | estocastico_rebote | WLFI | timeout | +0.40% | -0.10% | -0.02 |
| 2026-10-02 00:35 | ruptura_volumen | WLFI | timeout | +0.00% | -0.50% | -0.11 |

## Eventos de la última vuelta

- 2026-10-02 00:40 [macd_momentum] CIERRE BTC momentum perdido bruto +0.04% neto -0.46%
- 2026-10-02 00:40 [macd_momentum_evento] CIERRE BTC momentum perdido bruto +0.04% neto -0.46%
- 2026-10-02 00:40 [ruptura_volumen] CIERRE ETH timeout bruto +0.04% neto -0.46%
- 2026-10-02 00:40 [ruptura_volumen_tope] CIERRE ETH timeout bruto +0.04% neto -0.46%
- 2026-10-02 00:40 [ruptura_volumen_evento] CIERRE ETH timeout bruto +0.04% neto -0.46%
- 2026-10-02 00:35 [macd_momentum] ENTRADA AAVE @ 153.8 (21.56 €, apertura)
- 2026-10-02 00:35 [macd_momentum_regimen] ENTRADA AAVE @ 153.8 (22.13 €, apertura)
- 2026-10-02 00:35 [macd_momentum_evento] ENTRADA AAVE @ 153.8 (21.68 €, apertura)
- 2026-10-02 00:40 [macd_momentum] CIERRE ZEC momentum perdido bruto -0.22% neto -0.72%
- 2026-10-02 00:40 [macd_momentum_regimen] CIERRE ZEC momentum perdido bruto -0.22% neto -0.72%
- 2026-10-02 00:40 [macd_momentum_evento] CIERRE ZEC momentum perdido bruto -0.22% neto -0.72%
- 2026-10-02 00:35 [ruptura_volumen_tope] ENTRADA FET @ 0.2076 (22.64 €, apertura)
- 2026-10-02 00:35 [ruptura_volumen] ENTRADA ASTER @ 0.66483 (21.78 €, apertura)
- 2026-10-02 00:35 [ruptura_estricta] ENTRADA ASTER @ 0.66483 (22.07 €, apertura)
- 2026-10-02 00:35 [ruptura_volumen_tope] ENTRADA ASTER @ 0.66483 (22.64 €, apertura)
- 2026-10-02 00:35 [ruptura_volumen_regimen] ENTRADA ASTER @ 0.66483 (21.87 €, apertura)
- 2026-10-02 00:35 [ruptura_volumen_evento] ENTRADA ASTER @ 0.66483 (22.09 €, apertura)
- 2026-10-02 00:40 [macd_momentum] CIERRE WLFI momentum perdido bruto +0.00% neto -0.50%
- 2026-10-02 00:40 [macd_momentum_evento] CIERRE WLFI momentum perdido bruto +0.00% neto -0.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
