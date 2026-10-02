# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 09:06 UTC · vueltas 398 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.92 € (-3.71%) | 339 | 24 | 40% | +0.146% | -0.431% | -0.551% | -33.36 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 860.86 € (-6.86%) | 420 | 24 | 27% | -0.098% | -0.660% | -0.770% | -62.14 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.45 € (-3.76%) | 241 | 6 | 20% | -0.033% | -0.642% | -0.729% | -35.16 € |
| macd_momentum | 854.00 € (-7.60%) | 662 | 28 | 23% | +0.053% | -0.487% | -0.588% | -71.67 € |
| estocastico_rebote | 880.44 € (-4.74%) | 413 | 17 | 38% | +0.093% | -0.470% | -0.577% | -44.06 € |
| ruptura_estricta | 881.74 € (-4.60%) | 237 | 8 | 32% | -0.154% | -0.765% | -0.882% | -41.27 € |
| macd_sin_salida | 879.81 € (-4.81%) | 440 | 36 | 40% | +0.114% | -0.445% | -0.556% | -44.61 € |
| c_banda_atr_tope | 913.03 € (-1.21%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 900.71 € (-2.55%) | 128 | 5 | 24% | -0.088% | -0.794% | -0.908% | -23.22 € |
| c_banda_atr_regimen | 902.55 € (-2.35%) | 191 | 24 | 41% | +0.164% | -0.472% | -0.600% | -20.78 € |
| macd_momentum_regimen | 876.87 € (-5.13%) | 425 | 28 | 22% | +0.052% | -0.509% | -0.614% | -48.82 € |
| ruptura_volumen_regimen | 865.53 € (-6.35%) | 343 | 24 | 24% | -0.170% | -0.746% | -0.860% | -57.47 € |
| c_banda_atr_evento | 895.85 € (-3.07%) | 306 | 24 | 41% | +0.195% | -0.391% | -0.507% | -27.43 € |
| macd_momentum_evento | 858.73 € (-7.09%) | 615 | 28 | 22% | +0.055% | -0.488% | -0.587% | -66.94 € |
| ruptura_volumen_evento | 873.11 € (-5.53%) | 370 | 24 | 28% | -0.027% | -0.598% | -0.702% | -49.87 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 09:05 | ruptura_volumen_evento | ENA | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 09:05 | macd_momentum_evento | WLFI | momentum perdido | -0.20% | -0.70% | -0.15 |
| 2026-10-02 09:05 | macd_momentum_evento | DOT | momentum perdido | -0.54% | -1.04% | -0.22 |
| 2026-10-02 09:05 | ruptura_volumen_regimen | ENA | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 09:05 | macd_momentum_regimen | WLFI | momentum perdido | -0.20% | -0.70% | -0.15 |
| 2026-10-02 09:05 | macd_momentum_regimen | DOT | momentum perdido | -0.54% | -1.04% | -0.23 |
| 2026-10-02 09:05 | macd_sin_salida | ENA | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 09:05 | estocastico_rebote | USELESS | timeout | +0.47% | -0.03% | -0.01 |
| 2026-10-02 09:05 | estocastico_rebote | AVAX | timeout | -0.13% | -0.63% | -0.14 |
| 2026-10-02 09:05 | macd_momentum | WLFI | momentum perdido | -0.20% | -0.70% | -0.15 |
| 2026-10-02 09:05 | macd_momentum | DOT | momentum perdido | -0.54% | -1.04% | -0.22 |
| 2026-10-02 09:05 | pullback_tendencia | ZEC | rotura de tendencia | -0.35% | -0.85% | -0.19 |
| 2026-10-02 09:05 | pullback_tendencia | AVAX | rotura de tendencia | +0.00% | -0.50% | -0.11 |
| 2026-10-02 09:05 | ruptura_volumen | ENA | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 09:00 | macd_momentum_evento | XMR | momentum perdido | -0.38% | -0.88% | -0.19 |

## Eventos de la última vuelta

- 2026-10-02 09:05 [pullback_tendencia] CIERRE AVAX rotura de tendencia bruto +0.00% neto -0.50%
- 2026-10-02 09:05 [estocastico_rebote] CIERRE AVAX timeout bruto -0.13% neto -0.63%
- 2026-10-02 09:05 [pullback_tendencia] CIERRE ZEC rotura de tendencia bruto -0.35% neto -0.85%
- 2026-10-02 09:05 [macd_momentum] CIERRE DOT momentum perdido bruto -0.54% neto -1.04%
- 2026-10-02 09:05 [macd_momentum_regimen] CIERRE DOT momentum perdido bruto -0.54% neto -1.04%
- 2026-10-02 09:05 [macd_momentum_evento] CIERRE DOT momentum perdido bruto -0.54% neto -1.04%
- 2026-10-02 09:05 [ruptura_volumen] CIERRE ENA stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 09:05 [macd_sin_salida] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 09:05 [ruptura_volumen_regimen] CIERRE ENA stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 09:05 [ruptura_volumen_evento] CIERRE ENA stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 09:05 [estocastico_rebote] CIERRE USELESS timeout bruto +0.48% neto -0.02%
- 2026-10-02 09:05 [macd_momentum] CIERRE WLFI momentum perdido bruto -0.20% neto -0.70%
- 2026-10-02 09:05 [macd_momentum_regimen] CIERRE WLFI momentum perdido bruto -0.20% neto -0.70%
- 2026-10-02 09:05 [macd_momentum_evento] CIERRE WLFI momentum perdido bruto -0.20% neto -0.70%
- 2026-10-02 09:00 [ruptura_estricta] ENTRADA SKY @ 0.0768 (22.07 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
