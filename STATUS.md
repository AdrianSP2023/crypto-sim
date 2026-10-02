# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 09:26 UTC · vueltas 402 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.91 € (-3.71%) | 341 | 23 | 40% | +0.136% | -0.441% | -0.561% | -34.27 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 861.27 € (-6.81%) | 422 | 23 | 27% | -0.095% | -0.657% | -0.766% | -62.08 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.93 € (-3.71%) | 242 | 9 | 21% | -0.025% | -0.634% | -0.721% | -34.83 € |
| macd_momentum | 851.96 € (-7.82%) | 685 | 9 | 23% | +0.060% | -0.478% | -0.579% | -72.79 € |
| estocastico_rebote | 880.39 € (-4.74%) | 416 | 24 | 37% | +0.088% | -0.475% | -0.582% | -44.80 € |
| ruptura_estricta | 882.24 € (-4.54%) | 237 | 8 | 32% | -0.154% | -0.765% | -0.882% | -41.27 € |
| macd_sin_salida | 880.73 € (-4.71%) | 441 | 35 | 40% | +0.110% | -0.449% | -0.560% | -45.05 € |
| c_banda_atr_tope | 913.42 € (-1.17%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 900.75 € (-2.54%) | 128 | 5 | 24% | -0.088% | -0.794% | -0.908% | -23.22 € |
| c_banda_atr_regimen | 902.54 € (-2.35%) | 193 | 23 | 40% | +0.146% | -0.489% | -0.617% | -21.72 € |
| macd_momentum_regimen | 874.77 € (-5.35%) | 448 | 9 | 23% | +0.063% | -0.495% | -0.597% | -49.97 € |
| ruptura_volumen_regimen | 865.95 € (-6.31%) | 345 | 23 | 25% | -0.165% | -0.741% | -0.855% | -57.40 € |
| c_banda_atr_evento | 895.83 € (-3.07%) | 308 | 23 | 41% | +0.183% | -0.402% | -0.518% | -28.35 € |
| macd_momentum_evento | 856.68 € (-7.31%) | 638 | 9 | 22% | +0.063% | -0.479% | -0.577% | -68.07 € |
| ruptura_volumen_evento | 873.53 € (-5.49%) | 372 | 23 | 28% | -0.023% | -0.594% | -0.698% | -49.81 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 09:25 | macd_momentum_evento | MON | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 09:25 | c_banda_atr_evento | ENA | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-10-02 09:25 | macd_momentum_regimen | MON | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 09:25 | c_banda_atr_regimen | ENA | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-10-02 09:25 | macd_sin_salida | MON | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 09:25 | estocastico_rebote | ENA | timeout | -1.36% | -1.86% | -0.41 |
| 2026-10-02 09:25 | macd_momentum | MON | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 09:25 | c_banda_atr | ENA | stop-loss | -1.63% | -2.13% | -0.47 |
| 2026-10-02 09:20 | ruptura_volumen_evento | SKY | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 09:20 | macd_momentum_evento | RENDER | momentum perdido | +0.63% | +0.13% | +0.03 |
| 2026-10-02 09:20 | macd_momentum_evento | PEPE | momentum perdido | +0.69% | +0.19% | +0.04 |
| 2026-10-02 09:20 | macd_momentum_evento | XLM | momentum perdido | +0.90% | +0.40% | +0.09 |
| 2026-10-02 09:20 | c_banda_atr_evento | FET | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 09:20 | ruptura_volumen_regimen | SKY | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 09:20 | macd_momentum_regimen | RENDER | momentum perdido | +0.63% | +0.13% | +0.03 |

## Eventos de la última vuelta

- 2026-10-02 09:20 [estocastico_rebote] ENTRADA NEAR @ 4.372 (22.00 €, apertura)
- 2026-10-02 09:20 [macd_momentum] ENTRADA ADA @ 0.227527 (21.30 €, apertura)
- 2026-10-02 09:20 [macd_momentum_regimen] ENTRADA ADA @ 0.227527 (21.87 €, apertura)
- 2026-10-02 09:20 [macd_momentum_evento] ENTRADA ADA @ 0.227527 (21.42 €, apertura)
- 2026-10-02 09:20 [estocastico_rebote] ENTRADA SUI @ 1.0515 (22.00 €, apertura)
- 2026-10-02 09:20 [macd_momentum] ENTRADA ZEC @ 1238 (21.30 €, apertura)
- 2026-10-02 09:20 [macd_momentum_regimen] ENTRADA ZEC @ 1238 (21.87 €, apertura)
- 2026-10-02 09:20 [macd_momentum_evento] ENTRADA ZEC @ 1238 (21.42 €, apertura)
- 2026-10-02 09:25 [c_banda_atr] CIERRE ENA stop-loss bruto -1.63% neto -2.13%
- 2026-10-02 09:25 [estocastico_rebote] CIERRE ENA timeout bruto -1.36% neto -1.86%
- 2026-10-02 09:25 [c_banda_atr_regimen] CIERRE ENA stop-loss bruto -1.63% neto -2.13%
- 2026-10-02 09:25 [c_banda_atr_evento] CIERRE ENA stop-loss bruto -1.63% neto -2.13%
- 2026-10-02 09:20 [estocastico_rebote] ENTRADA FET @ 0.2085 (21.99 €, apertura)
- 2026-10-02 09:20 [estocastico_rebote] ENTRADA POL @ 0.09837 (21.99 €, apertura)
- 2026-10-02 09:20 [estocastico_rebote] ENTRADA BCH @ 280.68 (21.99 €, apertura)
- 2026-10-02 09:25 [macd_momentum] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 09:25 [macd_sin_salida] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 09:25 [macd_momentum_regimen] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 09:25 [macd_momentum_evento] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 09:20 [macd_momentum] ENTRADA DASH @ 53.297 (21.29 €, apertura)
- 2026-10-02 09:20 [macd_momentum_regimen] ENTRADA DASH @ 53.297 (21.86 €, apertura)
- 2026-10-02 09:20 [macd_momentum_evento] ENTRADA DASH @ 53.297 (21.40 €, apertura)
- 2026-10-02 09:20 [estocastico_rebote] ENTRADA KSM @ 4.59 (21.99 €, apertura)
- 2026-10-02 09:20 [c_banda_atr] ENTRADA SEI @ 0.06401 (22.25 €, apertura)
- 2026-10-02 09:20 [c_banda_atr_regimen] ENTRADA SEI @ 0.06401 (22.56 €, apertura)
- 2026-10-02 09:20 [c_banda_atr_evento] ENTRADA SEI @ 0.06401 (22.40 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
