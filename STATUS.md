# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 11:31 UTC · vueltas 387 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.58 € (-3.75%) | 353 | 22 | 41% | +0.158% | -0.416% | -0.535% | -33.47 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 856.60 € (-7.32%) | 447 | 15 | 26% | -0.112% | -0.670% | -0.776% | -66.90 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.39 € (-3.77%) | 256 | 13 | 21% | -0.008% | -0.611% | -0.696% | -35.52 € |
| macd_momentum | 848.63 € (-8.18%) | 724 | 16 | 23% | +0.060% | -0.476% | -0.575% | -76.51 € |
| estocastico_rebote | 879.63 € (-4.83%) | 434 | 34 | 38% | +0.125% | -0.436% | -0.542% | -42.94 € |
| ruptura_estricta | 880.30 € (-4.75%) | 245 | 11 | 31% | -0.174% | -0.782% | -0.896% | -43.52 € |
| macd_sin_salida | 876.13 € (-5.21%) | 478 | 24 | 39% | +0.113% | -0.441% | -0.549% | -47.89 € |
| c_banda_atr_tope | 913.23 € (-1.19%) | 80 | 5 | 39% | +0.254% | -0.576% | -0.690% | -10.59 € |
| ruptura_volumen_tope | 899.09 € (-2.72%) | 134 | 5 | 23% | -0.110% | -0.807% | -0.919% | -24.67 € |
| c_banda_atr_regimen | 902.09 € (-2.40%) | 206 | 22 | 43% | +0.186% | -0.440% | -0.567% | -20.90 € |
| macd_momentum_regimen | 871.35 € (-5.72%) | 487 | 16 | 23% | +0.062% | -0.491% | -0.591% | -53.79 € |
| ruptura_volumen_regimen | 861.25 € (-6.82%) | 370 | 15 | 24% | -0.180% | -0.751% | -0.861% | -62.25 € |
| c_banda_atr_evento | 895.50 € (-3.11%) | 320 | 22 | 42% | +0.207% | -0.376% | -0.491% | -27.55 € |
| macd_momentum_evento | 853.33 € (-7.67%) | 677 | 16 | 22% | +0.062% | -0.477% | -0.573% | -71.81 € |
| ruptura_volumen_evento | 868.79 € (-6.00%) | 397 | 15 | 27% | -0.047% | -0.613% | -0.714% | -54.70 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 11:30 | macd_momentum_evento | AAVE | momentum perdido | -0.56% | -1.06% | -0.23 |
| 2026-10-02 11:30 | macd_momentum_evento | QNT | take-profit | +2.23% | +1.73% | +0.37 |
| 2026-10-02 11:30 | macd_momentum_evento | ETH | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-02 11:30 | c_banda_atr_evento | QNT | take-profit | +2.23% | +1.73% | +0.39 |
| 2026-10-02 11:30 | macd_momentum_regimen | AAVE | momentum perdido | -0.56% | -1.06% | -0.23 |
| 2026-10-02 11:30 | macd_momentum_regimen | QNT | take-profit | +2.23% | +1.73% | +0.38 |
| 2026-10-02 11:30 | macd_momentum_regimen | ETH | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-02 11:30 | c_banda_atr_regimen | QNT | take-profit | +2.23% | +1.73% | +0.39 |
| 2026-10-02 11:30 | macd_sin_salida | UNI | timeout | -0.86% | -1.36% | -0.30 |
| 2026-10-02 11:30 | macd_sin_salida | QNT | take-profit | +2.23% | +1.73% | +0.38 |
| 2026-10-02 11:30 | macd_momentum | AAVE | momentum perdido | -0.56% | -1.06% | -0.23 |
| 2026-10-02 11:30 | macd_momentum | QNT | take-profit | +2.23% | +1.73% | +0.37 |
| 2026-10-02 11:30 | macd_momentum | ETH | momentum perdido | -0.15% | -0.65% | -0.14 |
| 2026-10-02 11:30 | c_banda_atr | QNT | take-profit | +2.23% | +1.73% | +0.39 |
| 2026-10-02 11:25 | macd_momentum_evento | TRUMP | take-profit | +2.00% | +1.50% | +0.32 |

## Eventos de la última vuelta

- 2026-10-02 11:30 [macd_momentum] CIERRE ETH momentum perdido bruto -0.15% neto -0.65%
- 2026-10-02 11:30 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto -0.15% neto -0.65%
- 2026-10-02 11:30 [macd_momentum_evento] CIERRE ETH momentum perdido bruto -0.15% neto -0.65%
- 2026-10-02 11:30 [c_banda_atr] CIERRE QNT take-profit bruto +2.23% neto +1.73%
- 2026-10-02 11:30 [macd_momentum] CIERRE QNT take-profit bruto +2.23% neto +1.73%
- 2026-10-02 11:30 [macd_sin_salida] CIERRE QNT take-profit bruto +2.23% neto +1.73%
- 2026-10-02 11:30 [c_banda_atr_regimen] CIERRE QNT take-profit bruto +2.23% neto +1.73%
- 2026-10-02 11:30 [macd_momentum_regimen] CIERRE QNT take-profit bruto +2.23% neto +1.73%
- 2026-10-02 11:30 [c_banda_atr_evento] CIERRE QNT take-profit bruto +2.23% neto +1.73%
- 2026-10-02 11:30 [macd_momentum_evento] CIERRE QNT take-profit bruto +2.23% neto +1.73%
- 2026-10-02 11:30 [macd_momentum] CIERRE AAVE momentum perdido bruto -0.56% neto -1.06%
- 2026-10-02 11:30 [macd_momentum_regimen] CIERRE AAVE momentum perdido bruto -0.56% neto -1.06%
- 2026-10-02 11:30 [macd_momentum_evento] CIERRE AAVE momentum perdido bruto -0.56% neto -1.06%
- 2026-10-02 11:30 [macd_sin_salida] CIERRE UNI timeout bruto -0.86% neto -1.36%
- 2026-10-02 11:25 [ruptura_volumen] ENTRADA USELESS @ 0.22909 (21.43 €, apertura)
- 2026-10-02 11:25 [ruptura_volumen_regimen] ENTRADA USELESS @ 0.22909 (21.55 €, apertura)
- 2026-10-02 11:25 [ruptura_volumen_evento] ENTRADA USELESS @ 0.22909 (21.74 €, apertura)
- 2026-10-02 11:25 [ruptura_volumen] ENTRADA BCH @ 282.21 (21.43 €, apertura)
- 2026-10-02 11:25 [ruptura_estricta] ENTRADA BCH @ 282.21 (22.02 €, apertura)
- 2026-10-02 11:25 [ruptura_volumen_regimen] ENTRADA BCH @ 282.21 (21.55 €, apertura)
- 2026-10-02 11:25 [ruptura_volumen_evento] ENTRADA BCH @ 282.21 (21.74 €, apertura)
- 2026-10-02 11:25 [ruptura_volumen] ENTRADA WLFI @ 0.05 (21.43 €, apertura)
- 2026-10-02 11:25 [ruptura_volumen_regimen] ENTRADA WLFI @ 0.05 (21.55 €, apertura)
- 2026-10-02 11:25 [ruptura_volumen_evento] ENTRADA WLFI @ 0.05 (21.74 €, apertura)
- 2026-10-02 11:25 [ruptura_volumen] ENTRADA TRUMP @ 1.908 (21.43 €, apertura)
- 2026-10-02 11:25 [ruptura_volumen_regimen] ENTRADA TRUMP @ 1.908 (21.55 €, apertura)
- 2026-10-02 11:25 [ruptura_volumen_evento] ENTRADA TRUMP @ 1.908 (21.74 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
