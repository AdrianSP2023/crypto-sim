# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 11:11 UTC · vueltas 423 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.38 € (-3.77%) | 351 | 22 | 41% | +0.147% | -0.427% | -0.547% | -34.19 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 857.20 € (-7.25%) | 447 | 10 | 26% | -0.112% | -0.670% | -0.778% | -66.90 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.51 € (-3.76%) | 256 | 11 | 21% | -0.008% | -0.611% | -0.698% | -35.52 € |
| macd_momentum | 849.23 € (-8.12%) | 716 | 19 | 23% | +0.054% | -0.482% | -0.583% | -76.63 € |
| estocastico_rebote | 879.65 € (-4.82%) | 432 | 34 | 38% | +0.116% | -0.444% | -0.551% | -43.55 € |
| ruptura_estricta | 880.96 € (-4.68%) | 243 | 12 | 32% | -0.168% | -0.777% | -0.892% | -42.90 € |
| macd_sin_salida | 876.92 € (-5.12%) | 475 | 23 | 39% | +0.113% | -0.442% | -0.550% | -47.67 € |
| c_banda_atr_tope | 913.33 € (-1.18%) | 80 | 4 | 39% | +0.254% | -0.576% | -0.690% | -10.59 € |
| ruptura_volumen_tope | 899.46 € (-2.68%) | 134 | 4 | 23% | -0.110% | -0.807% | -0.920% | -24.67 € |
| c_banda_atr_regimen | 901.90 € (-2.42%) | 204 | 22 | 42% | +0.168% | -0.460% | -0.588% | -21.62 € |
| macd_momentum_regimen | 871.97 € (-5.66%) | 479 | 19 | 23% | +0.054% | -0.501% | -0.602% | -53.91 € |
| ruptura_volumen_regimen | 861.85 € (-6.75%) | 370 | 10 | 24% | -0.180% | -0.751% | -0.863% | -62.25 € |
| c_banda_atr_evento | 895.30 € (-3.13%) | 318 | 22 | 42% | +0.195% | -0.388% | -0.505% | -28.27 € |
| macd_momentum_evento | 853.94 € (-7.61%) | 669 | 19 | 22% | +0.056% | -0.484% | -0.581% | -71.93 € |
| ruptura_volumen_evento | 869.39 € (-5.93%) | 397 | 10 | 27% | -0.047% | -0.613% | -0.716% | -54.70 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 11:10 | macd_momentum_evento | SEI | momentum perdido | -0.39% | -0.89% | -0.19 |
| 2026-10-02 11:10 | c_banda_atr_evento | PUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 11:10 | macd_momentum_regimen | SEI | momentum perdido | -0.39% | -0.89% | -0.19 |
| 2026-10-02 11:10 | c_banda_atr_regimen | PUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 11:10 | c_banda_atr_tope | PUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 11:10 | ruptura_estricta | CRV | timeout | -0.72% | -1.22% | -0.27 |
| 2026-10-02 11:10 | estocastico_rebote | PUMP | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-02 11:10 | macd_momentum | SEI | momentum perdido | -0.39% | -0.89% | -0.19 |
| 2026-10-02 11:10 | c_banda_atr | PUMP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 11:05 | macd_momentum_evento | BCH | momentum perdido | +0.09% | -0.41% | -0.09 |
| 2026-10-02 11:05 | macd_momentum_evento | XRP | momentum perdido | -0.17% | -0.67% | -0.14 |
| 2026-10-02 11:05 | macd_momentum_regimen | BCH | momentum perdido | +0.09% | -0.41% | -0.09 |
| 2026-10-02 11:05 | macd_momentum_regimen | XRP | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-10-02 11:05 | macd_sin_salida | BNB | timeout | +0.16% | -0.34% | -0.07 |
| 2026-10-02 11:05 | macd_sin_salida | PENGU | timeout | -0.21% | -0.71% | -0.16 |

## Eventos de la última vuelta

- 2026-10-02 11:05 [c_banda_atr] ENTRADA QNT @ 210.69 (22.24 €, apertura)
- 2026-10-02 11:05 [macd_momentum] ENTRADA QNT @ 210.69 (21.20 €, apertura)
- 2026-10-02 11:05 [macd_sin_salida] ENTRADA QNT @ 210.69 (21.91 €, apertura)
- 2026-10-02 11:05 [c_banda_atr_regimen] ENTRADA QNT @ 210.69 (22.56 €, apertura)
- 2026-10-02 11:05 [macd_momentum_regimen] ENTRADA QNT @ 210.69 (21.76 €, apertura)
- 2026-10-02 11:05 [c_banda_atr_evento] ENTRADA QNT @ 210.69 (22.39 €, apertura)
- 2026-10-02 11:05 [macd_momentum_evento] ENTRADA QNT @ 210.69 (21.31 €, apertura)
- 2026-10-02 11:05 [pullback_tendencia] ENTRADA AAVE @ 164.83 (22.22 €, apertura)
- 2026-10-02 11:10 [c_banda_atr] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:10 [estocastico_rebote] CIERRE PUMP take-profit bruto +1.80% neto +1.30%
- 2026-10-02 11:10 [c_banda_atr_tope] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:10 [c_banda_atr_regimen] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:10 [c_banda_atr_evento] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:05 [pullback_tendencia] ENTRADA DOT @ 1.0871 (22.22 €, apertura)
- 2026-10-02 11:10 [ruptura_estricta] CIERRE CRV timeout bruto -0.72% neto -1.22%
- 2026-10-02 11:10 [macd_momentum] CIERRE SEI momentum perdido bruto -0.39% neto -0.89%
- 2026-10-02 11:10 [macd_momentum_regimen] CIERRE SEI momentum perdido bruto -0.39% neto -0.89%
- 2026-10-02 11:10 [macd_momentum_evento] CIERRE SEI momentum perdido bruto -0.39% neto -0.89%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
