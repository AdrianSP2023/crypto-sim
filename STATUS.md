# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 09:21 UTC · vueltas 401 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.54 € (-3.65%) | 340 | 23 | 40% | +0.141% | -0.436% | -0.556% | -33.80 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 861.60 € (-6.78%) | 422 | 23 | 27% | -0.095% | -0.657% | -0.766% | -62.08 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.91 € (-3.71%) | 242 | 9 | 21% | -0.025% | -0.634% | -0.721% | -34.83 € |
| macd_momentum | 852.43 € (-7.77%) | 684 | 7 | 23% | +0.063% | -0.476% | -0.577% | -72.37 € |
| estocastico_rebote | 880.84 € (-4.70%) | 415 | 19 | 37% | +0.091% | -0.472% | -0.579% | -44.40 € |
| ruptura_estricta | 882.31 € (-4.54%) | 237 | 8 | 32% | -0.154% | -0.765% | -0.882% | -41.27 € |
| macd_sin_salida | 881.54 € (-4.62%) | 440 | 36 | 40% | +0.114% | -0.445% | -0.556% | -44.61 € |
| c_banda_atr_tope | 913.45 € (-1.17%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 900.79 € (-2.54%) | 128 | 5 | 24% | -0.088% | -0.794% | -0.908% | -23.22 € |
| c_banda_atr_regimen | 903.18 € (-2.28%) | 192 | 23 | 41% | +0.156% | -0.480% | -0.608% | -21.24 € |
| macd_momentum_regimen | 875.26 € (-5.30%) | 447 | 7 | 23% | +0.067% | -0.492% | -0.594% | -49.54 € |
| ruptura_volumen_regimen | 866.27 € (-6.27%) | 345 | 23 | 25% | -0.165% | -0.741% | -0.855% | -57.40 € |
| c_banda_atr_evento | 896.47 € (-3.00%) | 307 | 23 | 41% | +0.189% | -0.397% | -0.512% | -27.88 € |
| macd_momentum_evento | 857.16 € (-7.26%) | 637 | 7 | 22% | +0.065% | -0.476% | -0.575% | -67.64 € |
| ruptura_volumen_evento | 873.86 € (-5.45%) | 372 | 23 | 28% | -0.023% | -0.594% | -0.698% | -49.81 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 09:20 | ruptura_volumen_evento | SKY | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 09:20 | macd_momentum_evento | RENDER | momentum perdido | +0.63% | +0.13% | +0.03 |
| 2026-10-02 09:20 | macd_momentum_evento | PEPE | momentum perdido | +0.69% | +0.19% | +0.04 |
| 2026-10-02 09:20 | macd_momentum_evento | XLM | momentum perdido | +0.90% | +0.40% | +0.09 |
| 2026-10-02 09:20 | c_banda_atr_evento | FET | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 09:20 | ruptura_volumen_regimen | SKY | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 09:20 | macd_momentum_regimen | RENDER | momentum perdido | +0.63% | +0.13% | +0.03 |
| 2026-10-02 09:20 | macd_momentum_regimen | PEPE | momentum perdido | +0.69% | +0.19% | +0.04 |
| 2026-10-02 09:20 | macd_momentum_regimen | XLM | momentum perdido | +0.90% | +0.40% | +0.09 |
| 2026-10-02 09:20 | c_banda_atr_regimen | FET | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 09:20 | macd_momentum | RENDER | momentum perdido | +0.63% | +0.13% | +0.03 |
| 2026-10-02 09:20 | macd_momentum | PEPE | momentum perdido | +0.69% | +0.19% | +0.04 |
| 2026-10-02 09:20 | macd_momentum | XLM | momentum perdido | +0.90% | +0.40% | +0.09 |
| 2026-10-02 09:20 | pullback_tendencia | NIGHT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 09:20 | ruptura_volumen | SKY | stop-loss | -1.20% | -1.70% | -0.37 |

## Eventos de la última vuelta

- 2026-10-02 09:20 [macd_momentum] CIERRE XLM momentum perdido bruto +0.90% neto +0.40%
- 2026-10-02 09:20 [macd_momentum_regimen] CIERRE XLM momentum perdido bruto +0.90% neto +0.40%
- 2026-10-02 09:20 [macd_momentum_evento] CIERRE XLM momentum perdido bruto +0.90% neto +0.40%
- 2026-10-02 09:15 [estocastico_rebote] ENTRADA ICP @ 2.928 (22.00 €, apertura)
- 2026-10-02 09:20 [c_banda_atr] CIERRE FET stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 09:20 [c_banda_atr_regimen] CIERRE FET stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 09:20 [c_banda_atr_evento] CIERRE FET stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 09:15 [estocastico_rebote] ENTRADA ALGO @ 0.11631 (22.00 €, apertura)
- 2026-10-02 09:20 [pullback_tendencia] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 09:20 [macd_momentum] CIERRE PEPE momentum perdido bruto +0.69% neto +0.19%
- 2026-10-02 09:20 [macd_momentum_regimen] CIERRE PEPE momentum perdido bruto +0.69% neto +0.19%
- 2026-10-02 09:20 [macd_momentum_evento] CIERRE PEPE momentum perdido bruto +0.69% neto +0.19%
- 2026-10-02 09:20 [macd_momentum] CIERRE RENDER momentum perdido bruto +0.63% neto +0.13%
- 2026-10-02 09:20 [macd_momentum_regimen] CIERRE RENDER momentum perdido bruto +0.63% neto +0.13%
- 2026-10-02 09:20 [macd_momentum_evento] CIERRE RENDER momentum perdido bruto +0.63% neto +0.13%
- 2026-10-02 09:15 [pullback_tendencia] ENTRADA INJ @ 6.726 (22.24 €, apertura)
- 2026-10-02 09:15 [estocastico_rebote] ENTRADA OP @ 0.1185 (22.00 €, apertura)
- 2026-10-02 09:15 [macd_momentum] ENTRADA TRUMP @ 1.877 (21.30 €, apertura)
- 2026-10-02 09:15 [macd_momentum_regimen] ENTRADA TRUMP @ 1.877 (21.87 €, apertura)
- 2026-10-02 09:15 [macd_momentum_evento] ENTRADA TRUMP @ 1.877 (21.42 €, apertura)
- 2026-10-02 09:15 [ruptura_volumen] ENTRADA SKY @ 0.0789 (21.56 €, apertura)
- 2026-10-02 09:20 [ruptura_volumen] CIERRE SKY stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 09:15 [ruptura_volumen_regimen] ENTRADA SKY @ 0.0789 (21.68 €, apertura)
- 2026-10-02 09:20 [ruptura_volumen_regimen] CIERRE SKY stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 09:15 [ruptura_volumen_evento] ENTRADA SKY @ 0.0789 (21.87 €, apertura)
- 2026-10-02 09:20 [ruptura_volumen_evento] CIERRE SKY stop-loss bruto -1.20% neto -1.70%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
