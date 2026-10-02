# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 09:46 UTC · vueltas 406 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.14 € (-3.80%) | 341 | 24 | 40% | +0.136% | -0.441% | -0.561% | -34.27 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 859.89 € (-6.96%) | 426 | 22 | 27% | -0.104% | -0.665% | -0.775% | -63.46 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.39 € (-3.77%) | 246 | 9 | 20% | -0.028% | -0.635% | -0.722% | -35.48 € |
| macd_momentum | 851.64 € (-7.85%) | 690 | 11 | 23% | +0.061% | -0.476% | -0.577% | -73.09 € |
| estocastico_rebote | 878.82 € (-4.91%) | 420 | 24 | 37% | +0.088% | -0.474% | -0.581% | -45.17 € |
| ruptura_estricta | 881.98 € (-4.57%) | 237 | 12 | 32% | -0.154% | -0.765% | -0.882% | -41.27 € |
| macd_sin_salida | 879.19 € (-4.87%) | 448 | 32 | 40% | +0.106% | -0.452% | -0.562% | -46.03 € |
| c_banda_atr_tope | 913.31 € (-1.18%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 900.16 € (-2.61%) | 130 | 3 | 24% | -0.100% | -0.803% | -0.917% | -23.85 € |
| c_banda_atr_regimen | 901.76 € (-2.43%) | 193 | 24 | 40% | +0.146% | -0.489% | -0.617% | -21.72 € |
| macd_momentum_regimen | 874.45 € (-5.39%) | 453 | 11 | 24% | +0.065% | -0.493% | -0.595% | -50.27 € |
| ruptura_volumen_regimen | 864.55 € (-6.46%) | 349 | 22 | 24% | -0.176% | -0.750% | -0.865% | -58.79 € |
| c_banda_atr_evento | 895.06 € (-3.16%) | 308 | 24 | 41% | +0.183% | -0.402% | -0.518% | -28.35 € |
| macd_momentum_evento | 856.36 € (-7.34%) | 643 | 11 | 23% | +0.064% | -0.477% | -0.575% | -68.37 € |
| ruptura_volumen_evento | 872.12 € (-5.64%) | 376 | 22 | 28% | -0.035% | -0.605% | -0.709% | -51.21 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 09:45 | ruptura_volumen_evento | OP | timeout | -0.51% | -1.01% | -0.22 |
| 2026-10-02 09:45 | ruptura_volumen_evento | USELESS | stop-loss | -1.36% | -1.86% | -0.41 |
| 2026-10-02 09:45 | macd_momentum_evento | ADA | momentum perdido | -0.23% | -0.73% | -0.16 |
| 2026-10-02 09:45 | ruptura_volumen_regimen | OP | timeout | -0.51% | -1.01% | -0.22 |
| 2026-10-02 09:45 | ruptura_volumen_regimen | USELESS | stop-loss | -1.36% | -1.86% | -0.40 |
| 2026-10-02 09:45 | macd_momentum_regimen | ADA | momentum perdido | -0.23% | -0.73% | -0.16 |
| 2026-10-02 09:45 | ruptura_volumen_tope | OP | timeout | -0.51% | -1.01% | -0.23 |
| 2026-10-02 09:45 | macd_sin_salida | ASTER | timeout | +0.08% | -0.42% | -0.09 |
| 2026-10-02 09:45 | macd_sin_salida | SUI | timeout | -0.45% | -0.94% | -0.21 |
| 2026-10-02 09:45 | estocastico_rebote | DASH | timeout | -0.05% | -0.55% | -0.12 |
| 2026-10-02 09:45 | estocastico_rebote | ASTER | timeout | +0.08% | -0.42% | -0.09 |
| 2026-10-02 09:45 | macd_momentum | ADA | momentum perdido | -0.23% | -0.73% | -0.16 |
| 2026-10-02 09:45 | pullback_tendencia | OP | rotura de tendencia | +0.43% | -0.07% | -0.02 |
| 2026-10-02 09:45 | pullback_tendencia | INJ | rotura de tendencia | -0.55% | -1.05% | -0.23 |
| 2026-10-02 09:45 | ruptura_volumen | OP | timeout | -0.51% | -1.01% | -0.22 |

## Eventos de la última vuelta

- 2026-10-02 09:40 [pullback_tendencia] ENTRADA SOL @ 108.32 (22.23 €, apertura)
- 2026-10-02 09:45 [macd_momentum] CIERRE ADA momentum perdido bruto -0.23% neto -0.73%
- 2026-10-02 09:45 [macd_momentum_regimen] CIERRE ADA momentum perdido bruto -0.23% neto -0.73%
- 2026-10-02 09:45 [macd_momentum_evento] CIERRE ADA momentum perdido bruto -0.23% neto -0.73%
- 2026-10-02 09:45 [macd_sin_salida] CIERRE SUI timeout bruto -0.45% neto -0.95%
- 2026-10-02 09:40 [macd_momentum] ENTRADA XDC @ 0.02999 (21.28 €, apertura)
- 2026-10-02 09:40 [macd_sin_salida] ENTRADA XDC @ 0.02999 (21.96 €, apertura)
- 2026-10-02 09:40 [macd_momentum_regimen] ENTRADA XDC @ 0.02999 (21.85 €, apertura)
- 2026-10-02 09:40 [macd_momentum_evento] ENTRADA XDC @ 0.02999 (21.40 €, apertura)
- 2026-10-02 09:45 [ruptura_volumen] CIERRE USELESS stop-loss bruto -1.36% neto -1.86%
- 2026-10-02 09:45 [ruptura_volumen_regimen] CIERRE USELESS stop-loss bruto -1.36% neto -1.86%
- 2026-10-02 09:45 [ruptura_volumen_evento] CIERRE USELESS stop-loss bruto -1.36% neto -1.86%
- 2026-10-02 09:45 [pullback_tendencia] CIERRE INJ rotura de tendencia bruto -0.55% neto -1.05%
- 2026-10-02 09:45 [ruptura_volumen] CIERRE OP timeout bruto -0.51% neto -1.01%
- 2026-10-02 09:45 [pullback_tendencia] CIERRE OP rotura de tendencia bruto +0.43% neto -0.07%
- 2026-10-02 09:45 [ruptura_volumen_tope] CIERRE OP timeout bruto -0.51% neto -1.01%
- 2026-10-02 09:45 [ruptura_volumen_regimen] CIERRE OP timeout bruto -0.51% neto -1.01%
- 2026-10-02 09:45 [ruptura_volumen_evento] CIERRE OP timeout bruto -0.51% neto -1.01%
- 2026-10-02 09:45 [estocastico_rebote] CIERRE ASTER timeout bruto +0.08% neto -0.42%
- 2026-10-02 09:45 [macd_sin_salida] CIERRE ASTER timeout bruto +0.08% neto -0.42%
- 2026-10-02 09:45 [estocastico_rebote] CIERRE DASH timeout bruto -0.05% neto -0.55%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
