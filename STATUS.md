# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 01:16 UTC · vueltas 350 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 883.89 € (-4.37%) | 273 | 25 | 34% | -0.040% | -0.636% | -0.757% | -39.41 € |
| reversion_bb | 917.12 € (-0.77%) | 57 | 14 | 53% | +0.375% | -0.583% | -0.692% | -7.66 € |
| ruptura_volumen | 867.60 € (-6.13%) | 303 | 29 | 24% | -0.210% | -0.797% | -0.905% | -54.33 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.11 € (-3.91%) | 192 | 4 | 15% | -0.202% | -0.839% | -0.927% | -36.55 € |
| macd_momentum | 861.43 € (-6.80%) | 508 | 4 | 20% | -0.005% | -0.557% | -0.658% | -63.25 € |
| estocastico_rebote | 872.47 € (-5.60%) | 338 | 11 | 31% | -0.101% | -0.678% | -0.788% | -51.74 € |
| ruptura_estricta | 881.75 € (-4.60%) | 167 | 11 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 870.96 € (-5.77%) | 353 | 13 | 34% | -0.091% | -0.665% | -0.776% | -53.05 € |
| c_banda_atr_tope | 911.65 € (-1.36%) | 63 | 5 | 30% | +0.022% | -0.897% | -1.012% | -12.97 € |
| ruptura_volumen_tope | 904.53 € (-2.13%) | 103 | 5 | 26% | -0.041% | -0.797% | -0.913% | -18.80 € |
| c_banda_atr_regimen | 895.36 € (-3.12%) | 138 | 8 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 884.32 € (-4.32%) | 282 | 3 | 19% | -0.037% | -0.629% | -0.733% | -40.21 € |
| ruptura_volumen_regimen | 871.35 € (-5.72%) | 234 | 26 | 19% | -0.353% | -0.964% | -1.078% | -50.90 € |
| c_banda_atr_evento | 889.78 € (-3.73%) | 240 | 25 | 35% | -0.003% | -0.613% | -0.729% | -33.51 € |
| macd_momentum_evento | 866.20 € (-6.28%) | 461 | 4 | 19% | -0.009% | -0.566% | -0.664% | -58.48 € |
| ruptura_volumen_evento | 879.95 € (-4.79%) | 253 | 29 | 25% | -0.128% | -0.732% | -0.832% | -41.94 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 01:15 | ruptura_volumen_evento | ZRO | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 01:15 | macd_momentum_evento | ZEC | momentum perdido | -0.87% | -1.37% | -0.30 |
| 2026-10-02 01:15 | macd_momentum_evento | ETH | momentum perdido | -0.18% | -0.68% | -0.15 |
| 2026-10-02 01:15 | ruptura_volumen_regimen | ZRO | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 01:15 | macd_momentum_regimen | ZEC | momentum perdido | -0.87% | -1.37% | -0.30 |
| 2026-10-02 01:15 | macd_momentum_regimen | ETH | momentum perdido | -0.18% | -0.68% | -0.15 |
| 2026-10-02 01:15 | macd_sin_salida | TRUMP | timeout | -0.49% | -0.99% | -0.22 |
| 2026-10-02 01:15 | macd_sin_salida | FIL | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 01:15 | macd_sin_salida | AVAX | timeout | -0.57% | -1.07% | -0.23 |
| 2026-10-02 01:15 | macd_momentum | ZEC | momentum perdido | -0.87% | -1.37% | -0.30 |
| 2026-10-02 01:15 | macd_momentum | ETH | momentum perdido | -0.18% | -0.68% | -0.15 |
| 2026-10-02 01:15 | pullback_tendencia | BTC | rotura de tendencia | -0.09% | -0.59% | -0.13 |
| 2026-10-02 01:15 | ruptura_volumen | ZRO | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 01:10 | ruptura_volumen_evento | SUI | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 01:10 | macd_momentum_evento | PUMP | momentum perdido | -0.79% | -1.29% | -0.28 |

## Eventos de la última vuelta

- 2026-10-02 01:15 [pullback_tendencia] CIERRE BTC rotura de tendencia bruto -0.09% neto -0.59%
- 2026-10-02 01:15 [macd_momentum] CIERRE ETH momentum perdido bruto -0.18% neto -0.68%
- 2026-10-02 01:15 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto -0.18% neto -0.68%
- 2026-10-02 01:15 [macd_momentum_evento] CIERRE ETH momentum perdido bruto -0.18% neto -0.68%
- 2026-10-02 01:15 [macd_sin_salida] CIERRE AVAX timeout bruto -0.57% neto -1.07%
- 2026-10-02 01:15 [macd_momentum] CIERRE ZEC momentum perdido bruto -0.87% neto -1.37%
- 2026-10-02 01:15 [macd_momentum_regimen] CIERRE ZEC momentum perdido bruto -0.87% neto -1.37%
- 2026-10-02 01:15 [macd_momentum_evento] CIERRE ZEC momentum perdido bruto -0.87% neto -1.37%
- 2026-10-02 01:10 [reversion_bb] ENTRADA XLM @ 0.193544 (22.91 €, apertura)
- 2026-10-02 01:15 [ruptura_volumen] CIERRE ZRO stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 01:15 [ruptura_volumen_regimen] CIERRE ZRO stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 01:15 [ruptura_volumen_evento] CIERRE ZRO stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 01:10 [macd_momentum] ENTRADA ICP @ 2.934 (21.53 €, apertura)
- 2026-10-02 01:10 [ruptura_estricta] ENTRADA ICP @ 2.934 (22.06 €, apertura)
- 2026-10-02 01:10 [macd_momentum_evento] ENTRADA ICP @ 2.934 (21.64 €, apertura)
- 2026-10-02 01:10 [c_banda_atr] ENTRADA NIGHT @ 0.03447 (22.12 €, apertura)
- 2026-10-02 01:10 [c_banda_atr_evento] ENTRADA NIGHT @ 0.03447 (22.27 €, apertura)
- 2026-10-02 01:15 [macd_sin_salida] CIERRE FIL timeout bruto +0.00% neto -0.50%
- 2026-10-02 01:15 [macd_sin_salida] CIERRE TRUMP timeout bruto -0.49% neto -0.99%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
