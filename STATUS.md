# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 01:11 UTC · vueltas 349 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.24 € (-4.33%) | 273 | 24 | 34% | -0.040% | -0.636% | -0.757% | -39.41 € |
| reversion_bb | 917.22 € (-0.76%) | 57 | 13 | 53% | +0.375% | -0.583% | -0.692% | -7.66 € |
| ruptura_volumen | 868.63 € (-6.02%) | 302 | 30 | 24% | -0.207% | -0.794% | -0.902% | -53.96 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.43 € (-3.88%) | 191 | 5 | 15% | -0.202% | -0.840% | -0.929% | -36.42 € |
| macd_momentum | 861.98 € (-6.74%) | 506 | 5 | 20% | -0.003% | -0.555% | -0.657% | -62.80 € |
| estocastico_rebote | 872.84 € (-5.56%) | 338 | 11 | 31% | -0.101% | -0.678% | -0.788% | -51.74 € |
| ruptura_estricta | 882.20 € (-4.55%) | 167 | 10 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 872.04 € (-5.65%) | 350 | 16 | 34% | -0.089% | -0.664% | -0.775% | -52.49 € |
| c_banda_atr_tope | 911.75 € (-1.35%) | 63 | 5 | 30% | +0.022% | -0.897% | -1.012% | -12.97 € |
| ruptura_volumen_tope | 904.82 € (-2.10%) | 103 | 5 | 26% | -0.041% | -0.797% | -0.913% | -18.80 € |
| c_banda_atr_regimen | 895.43 € (-3.12%) | 138 | 8 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 884.83 € (-4.26%) | 280 | 5 | 19% | -0.033% | -0.626% | -0.731% | -39.76 € |
| ruptura_volumen_regimen | 872.25 € (-5.63%) | 233 | 27 | 19% | -0.349% | -0.961% | -1.075% | -50.53 € |
| c_banda_atr_evento | 890.13 € (-3.69%) | 240 | 24 | 35% | -0.003% | -0.613% | -0.729% | -33.51 € |
| macd_momentum_evento | 866.76 € (-6.22%) | 459 | 5 | 19% | -0.007% | -0.564% | -0.662% | -58.03 € |
| ruptura_volumen_evento | 880.99 € (-4.68%) | 252 | 30 | 25% | -0.124% | -0.729% | -0.828% | -41.57 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 01:10 | ruptura_volumen_evento | SUI | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 01:10 | macd_momentum_evento | PUMP | momentum perdido | -0.79% | -1.29% | -0.28 |
| 2026-10-02 01:10 | ruptura_volumen_regimen | SUI | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 01:10 | macd_momentum_regimen | PUMP | momentum perdido | -0.79% | -1.29% | -0.28 |
| 2026-10-02 01:10 | c_banda_atr_tope | DASH | timeout | -0.21% | -0.71% | -0.16 |
| 2026-10-02 01:10 | macd_momentum | PUMP | momentum perdido | -0.79% | -1.29% | -0.28 |
| 2026-10-02 01:10 | ruptura_volumen | SUI | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 01:10 | reversion_bb | SEI | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-02 01:05 | ruptura_volumen_evento | AAVE | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 01:05 | macd_momentum_evento | SPX | momentum perdido | +0.31% | -0.19% | -0.04 |
| 2026-10-02 01:05 | macd_momentum_evento | TAO | momentum perdido | -0.42% | -0.92% | -0.20 |
| 2026-10-02 01:05 | macd_momentum_evento | SUI | momentum perdido | -0.09% | -0.59% | -0.13 |
| 2026-10-02 01:05 | macd_momentum_evento | SOL | timeout | +0.61% | +0.11% | +0.02 |
| 2026-10-02 01:05 | ruptura_volumen_regimen | AAVE | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 01:05 | macd_momentum_regimen | TAO | momentum perdido | -0.42% | -0.92% | -0.20 |

## Eventos de la última vuelta

- 2026-10-02 01:10 [ruptura_volumen] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 01:10 [ruptura_volumen_regimen] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 01:10 [ruptura_volumen_evento] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 01:10 [macd_momentum] CIERRE PUMP momentum perdido bruto -0.79% neto -1.29%
- 2026-10-02 01:10 [macd_momentum_regimen] CIERRE PUMP momentum perdido bruto -0.79% neto -1.29%
- 2026-10-02 01:10 [macd_momentum_evento] CIERRE PUMP momentum perdido bruto -0.79% neto -1.29%
- 2026-10-02 01:05 [reversion_bb] ENTRADA UNI @ 7.943 (22.93 €, apertura)
- 2026-10-02 01:05 [c_banda_atr] ENTRADA ICP @ 2.932 (22.12 €, apertura)
- 2026-10-02 01:05 [c_banda_atr_regimen] ENTRADA ICP @ 2.932 (22.39 €, apertura)
- 2026-10-02 01:05 [c_banda_atr_evento] ENTRADA ICP @ 2.932 (22.27 €, apertura)
- 2026-10-02 01:10 [c_banda_atr_tope] CIERRE DASH timeout bruto -0.21% neto -0.71%
- 2026-10-02 01:05 [c_banda_atr] ENTRADA BNB @ 685.98 (22.12 €, apertura)
- 2026-10-02 01:05 [c_banda_atr_tope] ENTRADA BNB @ 685.98 (22.78 €, apertura)
- 2026-10-02 01:05 [c_banda_atr_regimen] ENTRADA BNB @ 685.98 (22.39 €, apertura)
- 2026-10-02 01:05 [c_banda_atr_evento] ENTRADA BNB @ 685.98 (22.27 €, apertura)
- 2026-10-02 01:10 [reversion_bb] CIERRE SEI stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
