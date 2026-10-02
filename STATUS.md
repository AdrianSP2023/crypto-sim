# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 10:51 UTC · vueltas 419 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.55 € (-3.75%) | 350 | 22 | 41% | +0.142% | -0.433% | -0.553% | -34.53 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 857.28 € (-7.24%) | 447 | 10 | 26% | -0.112% | -0.670% | -0.778% | -66.90 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.78 € (-3.73%) | 253 | 10 | 21% | -0.010% | -0.614% | -0.702% | -35.30 € |
| macd_momentum | 850.20 € (-8.01%) | 706 | 24 | 23% | +0.058% | -0.479% | -0.580% | -75.15 € |
| estocastico_rebote | 880.49 € (-4.73%) | 431 | 34 | 38% | +0.112% | -0.448% | -0.555% | -43.84 € |
| ruptura_estricta | 881.54 € (-4.62%) | 239 | 16 | 32% | -0.149% | -0.760% | -0.876% | -41.31 € |
| macd_sin_salida | 879.92 € (-4.79%) | 456 | 38 | 40% | +0.109% | -0.448% | -0.559% | -46.46 € |
| c_banda_atr_tope | 913.16 € (-1.20%) | 79 | 5 | 38% | +0.232% | -0.602% | -0.716% | -10.94 € |
| ruptura_volumen_tope | 899.57 € (-2.67%) | 134 | 4 | 23% | -0.110% | -0.807% | -0.920% | -24.67 € |
| c_banda_atr_regimen | 902.07 € (-2.40%) | 203 | 22 | 42% | +0.159% | -0.470% | -0.598% | -21.96 € |
| macd_momentum_regimen | 872.96 € (-5.55%) | 469 | 24 | 23% | +0.059% | -0.497% | -0.599% | -52.39 € |
| ruptura_volumen_regimen | 861.94 € (-6.74%) | 370 | 10 | 24% | -0.180% | -0.751% | -0.863% | -62.25 € |
| c_banda_atr_evento | 895.47 € (-3.11%) | 317 | 22 | 42% | +0.189% | -0.394% | -0.510% | -28.61 € |
| macd_momentum_evento | 854.91 € (-7.50%) | 659 | 24 | 22% | +0.060% | -0.480% | -0.579% | -70.44 € |
| ruptura_volumen_evento | 869.48 € (-5.92%) | 397 | 10 | 27% | -0.047% | -0.613% | -0.716% | -54.70 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 10:50 | ruptura_volumen_evento | SKY | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 10:50 | ruptura_volumen_evento | KAS | timeout | -0.42% | -0.92% | -0.20 |
| 2026-10-02 10:50 | macd_momentum_evento | VVV | momentum perdido | +0.44% | -0.06% | -0.01 |
| 2026-10-02 10:50 | c_banda_atr_evento | XDC | timeout | +0.77% | +0.27% | +0.06 |
| 2026-10-02 10:50 | ruptura_volumen_regimen | SKY | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 10:50 | ruptura_volumen_regimen | KAS | timeout | -0.42% | -0.92% | -0.20 |
| 2026-10-02 10:50 | macd_momentum_regimen | VVV | momentum perdido | +0.44% | -0.06% | -0.01 |
| 2026-10-02 10:50 | c_banda_atr_regimen | XDC | timeout | +0.77% | +0.27% | +0.06 |
| 2026-10-02 10:50 | ruptura_volumen_tope | SKY | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 10:50 | macd_sin_salida | USELESS | timeout | +0.17% | -0.33% | -0.07 |
| 2026-10-02 10:50 | macd_sin_salida | HBAR | timeout | +1.66% | +1.16% | +0.26 |
| 2026-10-02 10:50 | estocastico_rebote | FIL | timeout | +0.22% | -0.28% | -0.06 |
| 2026-10-02 10:50 | macd_momentum | VVV | momentum perdido | +0.44% | -0.06% | -0.01 |
| 2026-10-02 10:50 | ruptura_volumen | SKY | stop-loss | -1.20% | -1.70% | -0.36 |
| 2026-10-02 10:50 | ruptura_volumen | KAS | timeout | -0.42% | -0.92% | -0.20 |

## Eventos de la última vuelta

- 2026-10-02 10:45 [macd_momentum] ENTRADA ADA @ 0.228753 (21.23 €, apertura)
- 2026-10-02 10:45 [macd_momentum_regimen] ENTRADA ADA @ 0.228753 (21.80 €, apertura)
- 2026-10-02 10:45 [macd_momentum_evento] ENTRADA ADA @ 0.228753 (21.35 €, apertura)
- 2026-10-02 10:50 [macd_sin_salida] CIERRE HBAR timeout bruto +1.66% neto +1.16%
- 2026-10-02 10:45 [macd_momentum] ENTRADA DOT @ 1.0854 (21.23 €, apertura)
- 2026-10-02 10:45 [macd_momentum_regimen] ENTRADA DOT @ 1.0854 (21.80 €, apertura)
- 2026-10-02 10:45 [macd_momentum_evento] ENTRADA DOT @ 1.0854 (21.35 €, apertura)
- 2026-10-02 10:50 [c_banda_atr] CIERRE XDC timeout bruto +0.76% neto +0.26%
- 2026-10-02 10:50 [c_banda_atr_regimen] CIERRE XDC timeout bruto +0.76% neto +0.26%
- 2026-10-02 10:50 [c_banda_atr_evento] CIERRE XDC timeout bruto +0.76% neto +0.26%
- 2026-10-02 10:45 [macd_momentum] ENTRADA USELESS @ 0.22293 (21.23 €, apertura)
- 2026-10-02 10:50 [macd_sin_salida] CIERRE USELESS timeout bruto +0.17% neto -0.33%
- 2026-10-02 10:45 [macd_momentum_regimen] ENTRADA USELESS @ 0.22293 (21.80 €, apertura)
- 2026-10-02 10:45 [macd_momentum_evento] ENTRADA USELESS @ 0.22293 (21.35 €, apertura)
- 2026-10-02 10:45 [c_banda_atr] ENTRADA OP @ 0.118 (22.24 €, apertura)
- 2026-10-02 10:45 [c_banda_atr_regimen] ENTRADA OP @ 0.118 (22.56 €, apertura)
- 2026-10-02 10:45 [c_banda_atr_evento] ENTRADA OP @ 0.118 (22.39 €, apertura)
- 2026-10-02 10:50 [estocastico_rebote] CIERRE FIL timeout bruto +0.22% neto -0.28%
- 2026-10-02 10:50 [macd_momentum] CIERRE VVV momentum perdido bruto +0.44% neto -0.06%
- 2026-10-02 10:50 [macd_momentum_regimen] CIERRE VVV momentum perdido bruto +0.44% neto -0.06%
- 2026-10-02 10:50 [macd_momentum_evento] CIERRE VVV momentum perdido bruto +0.44% neto -0.06%
- 2026-10-02 10:45 [estocastico_rebote] ENTRADA ASTER @ 0.6675 (22.01 €, apertura)
- 2026-10-02 10:50 [ruptura_volumen] CIERRE KAS timeout bruto -0.42% neto -0.92%
- 2026-10-02 10:50 [ruptura_volumen_regimen] CIERRE KAS timeout bruto -0.42% neto -0.92%
- 2026-10-02 10:50 [ruptura_volumen_evento] CIERRE KAS timeout bruto -0.42% neto -0.92%
- 2026-10-02 10:50 [ruptura_volumen] CIERRE SKY stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 10:50 [ruptura_volumen_tope] CIERRE SKY stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 10:50 [ruptura_volumen_regimen] CIERRE SKY stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 10:50 [ruptura_volumen_evento] CIERRE SKY stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 10:45 [c_banda_atr_regimen] ENTRADA SPX @ 0.4018 (22.56 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
