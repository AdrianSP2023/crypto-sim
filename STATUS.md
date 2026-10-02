# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 14:11 UTC · vueltas 419 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 882.43 € (-4.52%) | 383 | 20 | 39% | +0.120% | -0.448% | -0.569% | -38.98 € |
| reversion_bb | 919.72 € (-0.49%) | 74 | 2 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 853.28 € (-7.68%) | 480 | 16 | 26% | -0.096% | -0.651% | -0.761% | -69.66 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 881.23 € (-4.65%) | 297 | 2 | 19% | -0.050% | -0.639% | -0.724% | -42.91 € |
| macd_momentum | 838.90 € (-9.23%) | 799 | 5 | 23% | +0.050% | -0.483% | -0.583% | -85.20 € |
| estocastico_rebote | 873.32 € (-5.51%) | 477 | 15 | 37% | +0.100% | -0.454% | -0.560% | -49.02 € |
| ruptura_estricta | 878.63 € (-4.94%) | 258 | 18 | 32% | -0.132% | -0.734% | -0.849% | -43.05 € |
| macd_sin_salida | 869.26 € (-5.95%) | 516 | 22 | 39% | +0.106% | -0.445% | -0.553% | -51.96 € |
| c_banda_atr_tope | 912.16 € (-1.31%) | 85 | 4 | 38% | +0.237% | -0.573% | -0.693% | -11.21 € |
| ruptura_volumen_tope | 898.24 € (-2.81%) | 144 | 3 | 23% | -0.106% | -0.789% | -0.905% | -25.92 € |
| c_banda_atr_regimen | 894.76 € (-3.19%) | 236 | 19 | 40% | +0.115% | -0.495% | -0.624% | -26.81 € |
| macd_momentum_regimen | 861.36 € (-6.80%) | 562 | 5 | 23% | +0.048% | -0.499% | -0.599% | -62.72 € |
| ruptura_volumen_regimen | 857.91 € (-7.18%) | 403 | 16 | 24% | -0.156% | -0.721% | -0.836% | -65.02 € |
| c_banda_atr_evento | 893.36 € (-3.34%) | 341 | 2 | 41% | +0.184% | -0.393% | -0.508% | -30.62 € |
| macd_momentum_evento | 851.50 € (-7.87%) | 700 | 0 | 23% | +0.070% | -0.468% | -0.564% | -72.75 € |
| ruptura_volumen_evento | 867.02 € (-6.19%) | 414 | 0 | 26% | -0.052% | -0.616% | -0.719% | -57.21 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 14:10 | c_banda_atr_evento | FIL | timeout | +0.43% | -0.07% | -0.01 |
| 2026-10-02 14:10 | ruptura_volumen_regimen | ADA | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 14:10 | macd_momentum_regimen | TAO | momentum perdido | -0.25% | -0.75% | -0.16 |
| 2026-10-02 14:10 | c_banda_atr_regimen | SPX | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 14:10 | c_banda_atr_regimen | FIL | timeout | +0.43% | -0.07% | -0.01 |
| 2026-10-02 14:10 | c_banda_atr_regimen | ENA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 14:10 | c_banda_atr_regimen | TAO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 14:10 | c_banda_atr_regimen | HBAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 14:10 | c_banda_atr_regimen | AVAX | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 14:10 | ruptura_volumen_tope | DASH | timeout | -0.61% | -1.11% | -0.25 |
| 2026-10-02 14:10 | c_banda_atr_tope | SPX | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-02 14:10 | macd_sin_salida | USELESS | stop-loss | -2.03% | -2.53% | -0.55 |
| 2026-10-02 14:10 | macd_sin_salida | CRV | stop-loss | -1.68% | -2.18% | -0.48 |
| 2026-10-02 14:10 | macd_sin_salida | ENA | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 14:10 | macd_sin_salida | HBAR | stop-loss | -1.50% | -2.00% | -0.44 |

## Eventos de la última vuelta

- 2026-10-02 14:10 [macd_sin_salida] CIERRE BTC timeout bruto -0.35% neto -0.85%
- 2026-10-02 14:10 [macd_sin_salida] CIERRE XRP stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [ruptura_volumen] CIERRE ADA stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 14:10 [estocastico_rebote] CIERRE ADA stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [macd_sin_salida] CIERRE ADA stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [ruptura_volumen_regimen] CIERRE ADA stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 14:10 [pullback_tendencia] CIERRE SUI rotura de tendencia bruto -1.12% neto -1.62%
- 2026-10-02 14:10 [c_banda_atr] CIERRE AVAX stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [macd_sin_salida] CIERRE AVAX stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [c_banda_atr_regimen] CIERRE AVAX stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [c_banda_atr] CIERRE HBAR stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [macd_sin_salida] CIERRE HBAR stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [c_banda_atr_regimen] CIERRE HBAR stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [estocastico_rebote] CIERRE HYPE stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [c_banda_atr] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [macd_momentum] CIERRE TAO momentum perdido bruto -0.25% neto -0.75%
- 2026-10-02 14:10 [c_banda_atr_regimen] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [macd_momentum_regimen] CIERRE TAO momentum perdido bruto -0.25% neto -0.75%
- 2026-10-02 14:10 [c_banda_atr] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [estocastico_rebote] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [macd_sin_salida] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [c_banda_atr_regimen] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [macd_sin_salida] CIERRE CRV stop-loss bruto -1.68% neto -2.18%
- 2026-10-02 14:10 [macd_sin_salida] CIERRE USELESS stop-loss bruto -2.03% neto -2.53%
- 2026-10-02 14:10 [pullback_tendencia] CIERRE OP rotura de tendencia bruto -0.84% neto -1.34%
- 2026-10-02 14:10 [c_banda_atr] CIERRE FIL timeout bruto +0.43% neto -0.07%
- 2026-10-02 14:10 [c_banda_atr_regimen] CIERRE FIL timeout bruto +0.43% neto -0.07%
- 2026-10-02 14:10 [c_banda_atr_evento] CIERRE FIL timeout bruto +0.43% neto -0.07%
- 2026-10-02 14:10 [ruptura_volumen_tope] CIERRE DASH timeout bruto -0.61% neto -1.11%
- 2026-10-02 14:10 [c_banda_atr_tope] CIERRE SPX stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:10 [c_banda_atr_regimen] CIERRE SPX stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
