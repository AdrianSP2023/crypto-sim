# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 10:56 UTC · vueltas 420 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.91 € (-3.82%) | 350 | 22 | 41% | +0.142% | -0.433% | -0.553% | -34.53 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 857.06 € (-7.27%) | 447 | 10 | 26% | -0.112% | -0.670% | -0.778% | -66.90 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.63 € (-3.74%) | 254 | 9 | 21% | -0.012% | -0.616% | -0.703% | -35.52 € |
| macd_momentum | 849.18 € (-8.12%) | 709 | 24 | 23% | +0.057% | -0.480% | -0.581% | -75.58 € |
| estocastico_rebote | 879.27 € (-4.87%) | 431 | 35 | 38% | +0.112% | -0.448% | -0.555% | -43.84 € |
| ruptura_estricta | 880.84 € (-4.70%) | 241 | 14 | 32% | -0.161% | -0.771% | -0.887% | -42.23 € |
| macd_sin_salida | 877.90 € (-5.01%) | 463 | 33 | 40% | +0.114% | -0.442% | -0.552% | -46.51 € |
| c_banda_atr_tope | 913.09 € (-1.21%) | 79 | 5 | 38% | +0.232% | -0.602% | -0.716% | -10.94 € |
| ruptura_volumen_tope | 899.51 € (-2.68%) | 134 | 4 | 23% | -0.110% | -0.807% | -0.920% | -24.67 € |
| c_banda_atr_regimen | 901.42 € (-2.47%) | 203 | 22 | 42% | +0.159% | -0.470% | -0.598% | -21.96 € |
| macd_momentum_regimen | 871.92 € (-5.66%) | 472 | 24 | 23% | +0.058% | -0.498% | -0.600% | -52.84 € |
| ruptura_volumen_regimen | 861.71 € (-6.77%) | 370 | 10 | 24% | -0.180% | -0.751% | -0.863% | -62.25 € |
| c_banda_atr_evento | 894.83 € (-3.18%) | 317 | 22 | 42% | +0.189% | -0.394% | -0.510% | -28.61 € |
| macd_momentum_evento | 853.89 € (-7.61%) | 662 | 24 | 22% | +0.059% | -0.481% | -0.579% | -70.88 € |
| ruptura_volumen_evento | 869.25 € (-5.95%) | 397 | 10 | 27% | -0.047% | -0.613% | -0.716% | -54.70 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 10:55 | macd_momentum_evento | SUI | momentum perdido | -0.47% | -0.97% | -0.21 |
| 2026-10-02 10:55 | macd_momentum_evento | ADA | momentum perdido | -0.19% | -0.69% | -0.15 |
| 2026-10-02 10:55 | macd_momentum_evento | BTC | momentum perdido | +0.12% | -0.38% | -0.08 |
| 2026-10-02 10:55 | macd_momentum_regimen | SUI | momentum perdido | -0.47% | -0.97% | -0.21 |
| 2026-10-02 10:55 | macd_momentum_regimen | ADA | momentum perdido | -0.19% | -0.69% | -0.15 |
| 2026-10-02 10:55 | macd_momentum_regimen | BTC | momentum perdido | +0.12% | -0.38% | -0.08 |
| 2026-10-02 10:55 | macd_sin_salida | SPX | timeout | -0.32% | -0.82% | -0.18 |
| 2026-10-02 10:55 | macd_sin_salida | TRUMP | timeout | +1.45% | +0.94% | +0.21 |
| 2026-10-02 10:55 | macd_sin_salida | DOT | timeout | -0.51% | -1.01% | -0.22 |
| 2026-10-02 10:55 | macd_sin_salida | DOGE | timeout | +0.47% | -0.03% | -0.01 |
| 2026-10-02 10:55 | macd_sin_salida | TAO | timeout | +0.36% | -0.14% | -0.03 |
| 2026-10-02 10:55 | macd_sin_salida | XLM | timeout | +1.21% | +0.71% | +0.16 |
| 2026-10-02 10:55 | macd_sin_salida | ETH | timeout | +0.61% | +0.12% | +0.03 |
| 2026-10-02 10:55 | ruptura_estricta | SKY | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-02 10:55 | ruptura_estricta | OP | timeout | -1.17% | -1.67% | -0.37 |

## Eventos de la última vuelta

- 2026-10-02 10:55 [macd_momentum] CIERRE BTC momentum perdido bruto +0.12% neto -0.38%
- 2026-10-02 10:55 [macd_momentum_regimen] CIERRE BTC momentum perdido bruto +0.12% neto -0.38%
- 2026-10-02 10:55 [macd_momentum_evento] CIERRE BTC momentum perdido bruto +0.12% neto -0.38%
- 2026-10-02 10:55 [macd_sin_salida] CIERRE ETH timeout bruto +0.61% neto +0.11%
- 2026-10-02 10:55 [macd_momentum] CIERRE ADA momentum perdido bruto -0.19% neto -0.69%
- 2026-10-02 10:55 [macd_momentum_regimen] CIERRE ADA momentum perdido bruto -0.19% neto -0.69%
- 2026-10-02 10:55 [macd_momentum_evento] CIERRE ADA momentum perdido bruto -0.19% neto -0.69%
- 2026-10-02 10:55 [macd_momentum] CIERRE SUI momentum perdido bruto -0.47% neto -0.97%
- 2026-10-02 10:55 [macd_momentum_regimen] CIERRE SUI momentum perdido bruto -0.47% neto -0.97%
- 2026-10-02 10:55 [macd_momentum_evento] CIERRE SUI momentum perdido bruto -0.47% neto -0.97%
- 2026-10-02 10:55 [macd_sin_salida] CIERRE XLM timeout bruto +1.21% neto +0.71%
- 2026-10-02 10:55 [pullback_tendencia] CIERRE TAO rotura de tendencia bruto -0.48% neto -0.98%
- 2026-10-02 10:55 [macd_sin_salida] CIERRE TAO timeout bruto +0.36% neto -0.14%
- 2026-10-02 10:50 [estocastico_rebote] ENTRADA ZRO @ 1.645 (22.01 €, apertura)
- 2026-10-02 10:55 [macd_sin_salida] CIERRE DOGE timeout bruto +0.47% neto -0.03%
- 2026-10-02 10:55 [macd_sin_salida] CIERRE DOT timeout bruto -0.51% neto -1.01%
- 2026-10-02 10:50 [macd_momentum] ENTRADA OP @ 0.1179 (21.22 €, apertura)
- 2026-10-02 10:55 [ruptura_estricta] CIERRE OP timeout bruto -1.17% neto -1.67%
- 2026-10-02 10:50 [macd_sin_salida] ENTRADA OP @ 0.1179 (21.94 €, apertura)
- 2026-10-02 10:50 [macd_momentum_regimen] ENTRADA OP @ 0.1179 (21.78 €, apertura)
- 2026-10-02 10:50 [macd_momentum_evento] ENTRADA OP @ 0.1179 (21.33 €, apertura)
- 2026-10-02 10:50 [macd_momentum] ENTRADA WLFI @ 0.0499 (21.22 €, apertura)
- 2026-10-02 10:50 [macd_sin_salida] ENTRADA WLFI @ 0.0499 (21.94 €, apertura)
- 2026-10-02 10:50 [macd_momentum_regimen] ENTRADA WLFI @ 0.0499 (21.78 €, apertura)
- 2026-10-02 10:50 [macd_momentum_evento] ENTRADA WLFI @ 0.0499 (21.33 €, apertura)
- 2026-10-02 10:55 [macd_sin_salida] CIERRE TRUMP timeout bruto +1.45% neto +0.95%
- 2026-10-02 10:55 [ruptura_estricta] CIERRE SKY stop-loss bruto -2.00% neto -2.50%
- 2026-10-02 10:50 [macd_momentum] ENTRADA SPX @ 0.4004 (21.22 €, apertura)
- 2026-10-02 10:55 [macd_sin_salida] CIERRE SPX timeout bruto -0.32% neto -0.82%
- 2026-10-02 10:50 [macd_momentum_regimen] ENTRADA SPX @ 0.4004 (21.78 €, apertura)
- 2026-10-02 10:50 [macd_momentum_evento] ENTRADA SPX @ 0.4004 (21.33 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
