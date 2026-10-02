# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 11:16 UTC · vueltas 424 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.29 € (-3.78%) | 351 | 22 | 41% | +0.147% | -0.427% | -0.547% | -34.19 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 857.10 € (-7.26%) | 447 | 10 | 26% | -0.112% | -0.670% | -0.778% | -66.90 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.53 € (-3.76%) | 256 | 11 | 21% | -0.008% | -0.611% | -0.698% | -35.52 € |
| macd_momentum | 849.01 € (-8.14%) | 718 | 18 | 23% | +0.053% | -0.483% | -0.584% | -76.95 € |
| estocastico_rebote | 879.92 € (-4.79%) | 432 | 36 | 38% | +0.116% | -0.444% | -0.551% | -43.55 € |
| ruptura_estricta | 880.73 € (-4.71%) | 243 | 12 | 32% | -0.168% | -0.777% | -0.892% | -42.90 € |
| macd_sin_salida | 877.00 € (-5.11%) | 475 | 24 | 39% | +0.113% | -0.442% | -0.550% | -47.67 € |
| c_banda_atr_tope | 913.28 € (-1.19%) | 80 | 5 | 39% | +0.254% | -0.576% | -0.690% | -10.59 € |
| ruptura_volumen_tope | 899.58 € (-2.67%) | 134 | 5 | 23% | -0.110% | -0.807% | -0.920% | -24.67 € |
| c_banda_atr_regimen | 901.80 € (-2.43%) | 204 | 22 | 42% | +0.168% | -0.460% | -0.588% | -21.62 € |
| macd_momentum_regimen | 871.74 € (-5.68%) | 481 | 18 | 23% | +0.052% | -0.502% | -0.603% | -54.24 € |
| ruptura_volumen_regimen | 861.75 € (-6.76%) | 370 | 10 | 24% | -0.180% | -0.751% | -0.863% | -62.25 € |
| c_banda_atr_evento | 895.21 € (-3.14%) | 318 | 22 | 42% | +0.195% | -0.388% | -0.505% | -28.27 € |
| macd_momentum_evento | 853.71 € (-7.63%) | 671 | 18 | 22% | +0.055% | -0.484% | -0.582% | -72.25 € |
| ruptura_volumen_evento | 869.30 € (-5.94%) | 397 | 10 | 27% | -0.047% | -0.613% | -0.716% | -54.70 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 11:15 | macd_momentum_evento | KAS | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-02 11:15 | macd_momentum_evento | DASH | momentum perdido | -0.28% | -0.79% | -0.17 |
| 2026-10-02 11:15 | macd_momentum_regimen | KAS | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-02 11:15 | macd_momentum_regimen | DASH | momentum perdido | -0.28% | -0.79% | -0.17 |
| 2026-10-02 11:15 | macd_momentum | KAS | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-02 11:15 | macd_momentum | DASH | momentum perdido | -0.28% | -0.79% | -0.17 |
| 2026-10-02 11:10 | macd_momentum_evento | SEI | momentum perdido | -0.39% | -0.89% | -0.19 |
| 2026-10-02 11:10 | c_banda_atr_evento | PUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 11:10 | macd_momentum_regimen | SEI | momentum perdido | -0.39% | -0.89% | -0.19 |
| 2026-10-02 11:10 | c_banda_atr_regimen | PUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 11:10 | c_banda_atr_tope | PUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 11:10 | ruptura_estricta | CRV | timeout | -0.72% | -1.22% | -0.27 |
| 2026-10-02 11:10 | estocastico_rebote | PUMP | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-02 11:10 | macd_momentum | SEI | momentum perdido | -0.39% | -0.89% | -0.19 |
| 2026-10-02 11:10 | c_banda_atr | PUMP | take-profit | +2.00% | +1.50% | +0.33 |

## Eventos de la última vuelta

- 2026-10-02 11:10 [macd_momentum] ENTRADA BTC @ 76986 (21.19 €, apertura)
- 2026-10-02 11:10 [macd_sin_salida] ENTRADA BTC @ 76986 (21.91 €, apertura)
- 2026-10-02 11:10 [macd_momentum_regimen] ENTRADA BTC @ 76986 (21.76 €, apertura)
- 2026-10-02 11:10 [macd_momentum_evento] ENTRADA BTC @ 76986 (21.31 €, apertura)
- 2026-10-02 11:10 [estocastico_rebote] ENTRADA ZEC @ 1238.55 (22.02 €, apertura)
- 2026-10-02 11:10 [ruptura_volumen_tope] ENTRADA HYPE @ 81.3 (22.49 €, apertura)
- 2026-10-02 11:15 [macd_momentum] CIERRE DASH momentum perdido bruto -0.28% neto -0.78%
- 2026-10-02 11:15 [macd_momentum_regimen] CIERRE DASH momentum perdido bruto -0.28% neto -0.78%
- 2026-10-02 11:15 [macd_momentum_evento] CIERRE DASH momentum perdido bruto -0.28% neto -0.78%
- 2026-10-02 11:15 [macd_momentum] CIERRE KAS momentum perdido bruto -0.24% neto -0.74%
- 2026-10-02 11:15 [macd_momentum_regimen] CIERRE KAS momentum perdido bruto -0.24% neto -0.74%
- 2026-10-02 11:15 [macd_momentum_evento] CIERRE KAS momentum perdido bruto -0.24% neto -0.74%
- 2026-10-02 11:10 [estocastico_rebote] ENTRADA SKY @ 0.07963 (22.02 €, apertura)
- 2026-10-02 11:10 [c_banda_atr_tope] ENTRADA SPX @ 0.4022 (22.84 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
