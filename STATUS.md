# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 11:21 UTC · vueltas 425 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.43 € (-3.77%) | 351 | 23 | 41% | +0.147% | -0.427% | -0.547% | -34.19 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 856.74 € (-7.30%) | 447 | 11 | 26% | -0.112% | -0.670% | -0.778% | -66.90 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.56 € (-3.75%) | 256 | 11 | 21% | -0.008% | -0.611% | -0.698% | -35.52 € |
| macd_momentum | 849.17 € (-8.12%) | 719 | 19 | 23% | +0.053% | -0.484% | -0.584% | -77.15 € |
| estocastico_rebote | 880.19 € (-4.77%) | 432 | 36 | 38% | +0.116% | -0.444% | -0.551% | -43.55 € |
| ruptura_estricta | 880.49 € (-4.73%) | 245 | 10 | 31% | -0.174% | -0.782% | -0.897% | -43.52 € |
| macd_sin_salida | 876.60 € (-5.15%) | 476 | 24 | 39% | +0.111% | -0.444% | -0.552% | -47.97 € |
| c_banda_atr_tope | 913.26 € (-1.19%) | 80 | 5 | 39% | +0.254% | -0.576% | -0.690% | -10.59 € |
| ruptura_volumen_tope | 899.19 € (-2.71%) | 134 | 5 | 23% | -0.110% | -0.807% | -0.920% | -24.67 € |
| c_banda_atr_regimen | 901.94 € (-2.41%) | 204 | 23 | 42% | +0.168% | -0.460% | -0.588% | -21.62 € |
| macd_momentum_regimen | 871.90 € (-5.66%) | 482 | 19 | 23% | +0.051% | -0.503% | -0.604% | -54.45 € |
| ruptura_volumen_regimen | 861.39 € (-6.80%) | 370 | 11 | 24% | -0.180% | -0.751% | -0.863% | -62.25 € |
| c_banda_atr_evento | 895.35 € (-3.13%) | 318 | 23 | 42% | +0.195% | -0.388% | -0.505% | -28.27 € |
| macd_momentum_evento | 853.87 € (-7.61%) | 672 | 19 | 22% | +0.054% | -0.485% | -0.583% | -72.45 € |
| ruptura_volumen_evento | 868.93 € (-5.98%) | 397 | 11 | 27% | -0.047% | -0.613% | -0.716% | -54.70 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 11:20 | macd_momentum_evento | FIL | momentum perdido | -0.43% | -0.93% | -0.20 |
| 2026-10-02 11:20 | macd_momentum_regimen | FIL | momentum perdido | -0.43% | -0.93% | -0.20 |
| 2026-10-02 11:20 | macd_sin_salida | LTC | timeout | -0.85% | -1.35% | -0.30 |
| 2026-10-02 11:20 | ruptura_estricta | POL | timeout | -1.31% | -1.81% | -0.40 |
| 2026-10-02 11:20 | ruptura_estricta | ETH | timeout | -0.51% | -1.01% | -0.22 |
| 2026-10-02 11:20 | macd_momentum | FIL | momentum perdido | -0.43% | -0.93% | -0.20 |
| 2026-10-02 11:15 | macd_momentum_evento | KAS | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-02 11:15 | macd_momentum_evento | DASH | momentum perdido | -0.28% | -0.79% | -0.17 |
| 2026-10-02 11:15 | macd_momentum_regimen | KAS | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-02 11:15 | macd_momentum_regimen | DASH | momentum perdido | -0.28% | -0.79% | -0.17 |
| 2026-10-02 11:15 | macd_momentum | KAS | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-02 11:15 | macd_momentum | DASH | momentum perdido | -0.28% | -0.79% | -0.17 |
| 2026-10-02 11:10 | macd_momentum_evento | SEI | momentum perdido | -0.39% | -0.89% | -0.19 |
| 2026-10-02 11:10 | c_banda_atr_evento | PUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 11:10 | macd_momentum_regimen | SEI | momentum perdido | -0.39% | -0.89% | -0.19 |

## Eventos de la última vuelta

- 2026-10-02 11:15 [macd_momentum] ENTRADA ETH @ 2447.24 (21.18 €, apertura)
- 2026-10-02 11:20 [ruptura_estricta] CIERRE ETH timeout bruto -0.51% neto -1.01%
- 2026-10-02 11:15 [macd_sin_salida] ENTRADA ETH @ 2447.24 (21.91 €, apertura)
- 2026-10-02 11:15 [macd_momentum_regimen] ENTRADA ETH @ 2447.24 (21.75 €, apertura)
- 2026-10-02 11:15 [macd_momentum_evento] ENTRADA ETH @ 2447.24 (21.30 €, apertura)
- 2026-10-02 11:15 [c_banda_atr] ENTRADA AAVE @ 165.54 (22.25 €, apertura)
- 2026-10-02 11:15 [c_banda_atr_regimen] ENTRADA AAVE @ 165.54 (22.57 €, apertura)
- 2026-10-02 11:15 [c_banda_atr_evento] ENTRADA AAVE @ 165.54 (22.40 €, apertura)
- 2026-10-02 11:20 [macd_sin_salida] CIERRE LTC timeout bruto -0.85% neto -1.35%
- 2026-10-02 11:20 [ruptura_estricta] CIERRE POL timeout bruto -1.31% neto -1.81%
- 2026-10-02 11:15 [macd_momentum] ENTRADA ALGO @ 0.11668 (21.18 €, apertura)
- 2026-10-02 11:15 [macd_momentum_regimen] ENTRADA ALGO @ 0.11668 (21.75 €, apertura)
- 2026-10-02 11:15 [macd_momentum_evento] ENTRADA ALGO @ 0.11668 (21.30 €, apertura)
- 2026-10-02 11:20 [macd_momentum] CIERRE FIL momentum perdido bruto -0.43% neto -0.93%
- 2026-10-02 11:20 [macd_momentum_regimen] CIERRE FIL momentum perdido bruto -0.43% neto -0.93%
- 2026-10-02 11:20 [macd_momentum_evento] CIERRE FIL momentum perdido bruto -0.43% neto -0.93%
- 2026-10-02 11:15 [ruptura_volumen] ENTRADA BNB @ 692 (21.43 €, apertura)
- 2026-10-02 11:15 [ruptura_volumen_regimen] ENTRADA BNB @ 692 (21.55 €, apertura)
- 2026-10-02 11:15 [ruptura_volumen_evento] ENTRADA BNB @ 692 (21.74 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
