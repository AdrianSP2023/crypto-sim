# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 11:26 UTC · vueltas 426 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.60 € (-3.75%) | 352 | 23 | 41% | +0.152% | -0.422% | -0.542% | -33.86 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 856.58 € (-7.32%) | 447 | 11 | 26% | -0.112% | -0.670% | -0.778% | -66.90 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.40 € (-3.77%) | 256 | 13 | 21% | -0.008% | -0.611% | -0.698% | -35.52 € |
| macd_momentum | 849.09 € (-8.13%) | 721 | 19 | 23% | +0.058% | -0.478% | -0.579% | -76.51 € |
| estocastico_rebote | 880.24 € (-4.76%) | 434 | 34 | 38% | +0.125% | -0.436% | -0.543% | -42.94 € |
| ruptura_estricta | 880.44 € (-4.74%) | 245 | 10 | 31% | -0.174% | -0.782% | -0.897% | -43.52 € |
| macd_sin_salida | 876.51 € (-5.16%) | 476 | 26 | 39% | +0.111% | -0.444% | -0.552% | -47.97 € |
| c_banda_atr_tope | 913.19 € (-1.20%) | 80 | 5 | 39% | +0.254% | -0.576% | -0.690% | -10.59 € |
| ruptura_volumen_tope | 899.17 € (-2.71%) | 134 | 5 | 23% | -0.110% | -0.807% | -0.920% | -24.67 € |
| c_banda_atr_regimen | 902.12 € (-2.39%) | 205 | 23 | 42% | +0.177% | -0.451% | -0.579% | -21.29 € |
| macd_momentum_regimen | 871.83 € (-5.67%) | 484 | 19 | 23% | +0.060% | -0.494% | -0.596% | -53.79 € |
| ruptura_volumen_regimen | 861.23 € (-6.82%) | 370 | 11 | 24% | -0.180% | -0.751% | -0.863% | -62.25 € |
| c_banda_atr_evento | 895.52 € (-3.11%) | 319 | 23 | 42% | +0.200% | -0.383% | -0.499% | -27.94 € |
| macd_momentum_evento | 853.79 € (-7.62%) | 674 | 19 | 22% | +0.060% | -0.479% | -0.577% | -71.81 € |
| ruptura_volumen_evento | 868.77 € (-6.00%) | 397 | 11 | 27% | -0.047% | -0.613% | -0.716% | -54.70 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 11:25 | macd_momentum_evento | TRUMP | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 11:25 | macd_momentum_evento | USELESS | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 11:25 | c_banda_atr_evento | USELESS | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 11:25 | macd_momentum_regimen | TRUMP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 11:25 | macd_momentum_regimen | USELESS | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 11:25 | c_banda_atr_regimen | USELESS | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 11:25 | estocastico_rebote | SKY | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-02 11:25 | estocastico_rebote | USELESS | take-profit | +2.01% | +1.51% | +0.33 |
| 2026-10-02 11:25 | macd_momentum | TRUMP | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 11:25 | macd_momentum | USELESS | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 11:25 | c_banda_atr | USELESS | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 11:20 | macd_momentum_evento | FIL | momentum perdido | -0.43% | -0.93% | -0.20 |
| 2026-10-02 11:20 | macd_momentum_regimen | FIL | momentum perdido | -0.43% | -0.93% | -0.20 |
| 2026-10-02 11:20 | macd_sin_salida | LTC | timeout | -0.85% | -1.35% | -0.30 |
| 2026-10-02 11:20 | ruptura_estricta | POL | timeout | -1.31% | -1.81% | -0.40 |

## Eventos de la última vuelta

- 2026-10-02 11:20 [macd_momentum] ENTRADA AAVE @ 165.39 (21.18 €, apertura)
- 2026-10-02 11:20 [macd_sin_salida] ENTRADA AAVE @ 165.39 (21.91 €, apertura)
- 2026-10-02 11:20 [macd_momentum_regimen] ENTRADA AAVE @ 165.39 (21.74 €, apertura)
- 2026-10-02 11:20 [macd_momentum_evento] ENTRADA AAVE @ 165.39 (21.29 €, apertura)
- 2026-10-02 11:20 [pullback_tendencia] ENTRADA DOGE @ 0.0861859 (22.22 €, apertura)
- 2026-10-02 11:25 [c_banda_atr] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:25 [macd_momentum] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:25 [estocastico_rebote] CIERRE USELESS take-profit bruto +2.01% neto +1.51%
- 2026-10-02 11:25 [c_banda_atr_regimen] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:25 [macd_momentum_regimen] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:25 [c_banda_atr_evento] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:25 [macd_momentum_evento] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:20 [pullback_tendencia] ENTRADA BCH @ 281.67 (22.22 €, apertura)
- 2026-10-02 11:20 [macd_momentum] ENTRADA PENGU @ 0.008838 (21.19 €, apertura)
- 2026-10-02 11:20 [macd_sin_salida] ENTRADA PENGU @ 0.008838 (21.91 €, apertura)
- 2026-10-02 11:20 [macd_momentum_regimen] ENTRADA PENGU @ 0.008838 (21.75 €, apertura)
- 2026-10-02 11:20 [macd_momentum_evento] ENTRADA PENGU @ 0.008838 (21.30 €, apertura)
- 2026-10-02 11:25 [macd_momentum] CIERRE TRUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:25 [macd_momentum_regimen] CIERRE TRUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:25 [macd_momentum_evento] CIERRE TRUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:20 [c_banda_atr] ENTRADA SKY @ 0.08104 (22.26 €, apertura)
- 2026-10-02 11:25 [estocastico_rebote] CIERRE SKY take-profit bruto +1.80% neto +1.30%
- 2026-10-02 11:20 [c_banda_atr_regimen] ENTRADA SKY @ 0.08104 (22.57 €, apertura)
- 2026-10-02 11:20 [c_banda_atr_evento] ENTRADA SKY @ 0.08104 (22.41 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
