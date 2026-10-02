# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 06:21 UTC · vueltas 365 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.62 € (-3.64%) | 324 | 14 | 39% | +0.113% | -0.467% | -0.586% | -34.51 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 865.60 € (-6.34%) | 379 | 30 | 27% | -0.112% | -0.681% | -0.790% | -57.95 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.96 € (-3.71%) | 216 | 15 | 19% | -0.072% | -0.694% | -0.781% | -34.09 € |
| macd_momentum | 855.79 € (-7.41%) | 623 | 5 | 23% | +0.050% | -0.492% | -0.594% | -68.39 € |
| estocastico_rebote | 878.23 € (-4.98%) | 376 | 34 | 36% | +0.024% | -0.546% | -0.654% | -46.48 € |
| ruptura_estricta | 885.36 € (-4.21%) | 207 | 27 | 33% | -0.193% | -0.821% | -0.935% | -38.75 € |
| macd_sin_salida | 881.42 € (-4.63%) | 412 | 23 | 40% | +0.105% | -0.459% | -0.569% | -43.08 € |
| c_banda_atr_tope | 913.48 € (-1.16%) | 71 | 5 | 34% | +0.148% | -0.724% | -0.833% | -11.81 € |
| ruptura_volumen_tope | 902.42 € (-2.36%) | 121 | 5 | 26% | -0.062% | -0.780% | -0.893% | -21.58 € |
| c_banda_atr_regimen | 903.26 € (-2.27%) | 177 | 14 | 40% | +0.119% | -0.528% | -0.655% | -21.53 € |
| macd_momentum_regimen | 878.71 € (-4.93%) | 386 | 5 | 22% | +0.046% | -0.521% | -0.625% | -45.46 € |
| ruptura_volumen_regimen | 870.30 € (-5.84%) | 302 | 30 | 24% | -0.196% | -0.783% | -0.898% | -53.25 € |
| c_banda_atr_evento | 896.55 € (-3.00%) | 291 | 14 | 40% | +0.161% | -0.429% | -0.544% | -28.59 € |
| macd_momentum_evento | 860.53 € (-6.89%) | 576 | 5 | 22% | +0.051% | -0.495% | -0.593% | -63.65 € |
| ruptura_volumen_evento | 877.92 € (-5.01%) | 329 | 30 | 28% | -0.034% | -0.614% | -0.717% | -45.62 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 06:20 | ruptura_volumen_tope | BTC | timeout | +0.09% | -0.41% | -0.09 |
| 2026-10-02 06:20 | pullback_tendencia | OP | rotura de tendencia | -0.85% | -1.35% | -0.30 |
| 2026-10-02 06:15 | macd_momentum_evento | XMR | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 06:15 | macd_momentum_evento | LTC | momentum perdido | +0.99% | +0.49% | +0.11 |
| 2026-10-02 06:15 | c_banda_atr_evento | HYPE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 06:15 | macd_momentum_regimen | XMR | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 06:15 | macd_momentum_regimen | LTC | momentum perdido | +0.99% | +0.49% | +0.11 |
| 2026-10-02 06:15 | c_banda_atr_regimen | HYPE | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 06:15 | macd_momentum | XMR | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 06:15 | macd_momentum | LTC | momentum perdido | +0.99% | +0.49% | +0.10 |
| 2026-10-02 06:15 | c_banda_atr | HYPE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 06:05 | ruptura_volumen_evento | DOGE | timeout | +1.20% | +0.70% | +0.15 |
| 2026-10-02 06:05 | macd_momentum_evento | DASH | momentum perdido | +0.28% | -0.22% | -0.05 |
| 2026-10-02 06:05 | macd_momentum_evento | ICP | momentum perdido | -0.20% | -0.70% | -0.15 |
| 2026-10-02 06:05 | ruptura_volumen_regimen | DOGE | timeout | +1.20% | +0.70% | +0.15 |

## Eventos de la última vuelta

- 2026-10-02 06:20 [ruptura_volumen_tope] CIERRE BTC timeout bruto +0.09% neto -0.41%
- 2026-10-02 06:15 [estocastico_rebote] ENTRADA SOL @ 108.01 (21.94 €, apertura)
- 2026-10-02 06:15 [macd_momentum] ENTRADA NEAR @ 4.4764 (21.40 €, apertura)
- 2026-10-02 06:15 [macd_momentum_regimen] ENTRADA NEAR @ 4.4764 (21.97 €, apertura)
- 2026-10-02 06:15 [macd_momentum_evento] ENTRADA NEAR @ 4.4764 (21.51 €, apertura)
- 2026-10-02 06:20 [pullback_tendencia] CIERRE OP rotura de tendencia bruto -0.85% neto -1.35%
- 2026-10-02 06:15 [ruptura_volumen] ENTRADA WLFI @ 0.0501 (21.66 €, apertura)
- 2026-10-02 06:15 [ruptura_volumen_tope] ENTRADA WLFI @ 0.0501 (22.57 €, apertura)
- 2026-10-02 06:15 [ruptura_volumen_regimen] ENTRADA WLFI @ 0.0501 (21.77 €, apertura)
- 2026-10-02 06:15 [ruptura_volumen_evento] ENTRADA WLFI @ 0.0501 (21.97 €, apertura)
- 2026-10-02 06:15 [estocastico_rebote] ENTRADA APT @ 0.7295 (21.94 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
