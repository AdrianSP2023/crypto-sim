# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 00:26 UTC · vueltas 340 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 886.09 € (-4.13%) | 272 | 21 | 34% | -0.047% | -0.643% | -0.765% | -39.74 € |
| reversion_bb | 918.83 € (-0.58%) | 53 | 16 | 51% | +0.343% | -0.650% | -0.747% | -7.94 € |
| ruptura_volumen | 872.76 € (-5.57%) | 297 | 21 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.53 € (-3.86%) | 189 | 6 | 15% | -0.199% | -0.839% | -0.928% | -35.99 € |
| macd_momentum | 864.25 € (-6.49%) | 491 | 14 | 20% | -0.007% | -0.560% | -0.663% | -61.58 € |
| estocastico_rebote | 873.50 € (-5.49%) | 332 | 15 | 31% | -0.113% | -0.692% | -0.801% | -51.80 € |
| ruptura_estricta | 883.09 € (-4.45%) | 166 | 5 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 872.58 € (-5.59%) | 348 | 16 | 34% | -0.097% | -0.672% | -0.783% | -52.84 € |
| c_banda_atr_tope | 911.84 € (-1.34%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.95 € (-1.98%) | 101 | 5 | 27% | -0.042% | -0.803% | -0.919% | -18.58 € |
| c_banda_atr_regimen | 895.82 € (-3.07%) | 138 | 3 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 885.36 € (-4.21%) | 276 | 3 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 875.56 € (-5.27%) | 230 | 16 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 891.98 € (-3.49%) | 239 | 21 | 34% | -0.011% | -0.622% | -0.738% | -33.85 € |
| macd_momentum_evento | 869.04 € (-5.97%) | 444 | 14 | 19% | -0.011% | -0.570% | -0.670% | -56.80 € |
| ruptura_volumen_evento | 885.17 € (-4.23%) | 247 | 21 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 00:25 | estocastico_rebote | ARB | timeout | +0.68% | +0.17% | +0.04 |
| 2026-10-02 00:20 | macd_momentum_evento | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:20 | c_banda_atr_evento | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:20 | macd_sin_salida | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:20 | estocastico_rebote | JUP | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 00:20 | estocastico_rebote | AVAX | timeout | +0.13% | -0.37% | -0.08 |
| 2026-10-02 00:20 | macd_momentum | SKY | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 00:20 | reversion_bb | OP | take-profit | +1.69% | +1.19% | +0.27 |
| 2026-10-02 00:20 | c_banda_atr | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:15 | estocastico_rebote | FET | take-profit | +2.08% | +1.58% | +0.34 |
| 2026-10-02 00:10 | c_banda_atr_evento | DASH | timeout | -0.87% | -1.37% | -0.31 |
| 2026-10-02 00:10 | pullback_tendencia | AAVE | rotura de tendencia | +0.18% | -0.32% | -0.07 |
| 2026-10-02 00:10 | c_banda_atr | DASH | timeout | -0.87% | -1.37% | -0.30 |
| 2026-10-02 00:05 | macd_momentum_evento | PUMP | momentum perdido | -0.10% | -0.60% | -0.13 |
| 2026-10-02 00:05 | c_banda_atr_evento | APT | timeout | -0.86% | -1.36% | -0.30 |

## Eventos de la última vuelta

- 2026-10-02 00:20 [ruptura_volumen] ENTRADA SOL @ 105.56 (21.79 €, apertura)
- 2026-10-02 00:20 [ruptura_estricta] ENTRADA SOL @ 105.56 (22.07 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen_regimen] ENTRADA SOL @ 105.56 (21.87 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen_evento] ENTRADA SOL @ 105.56 (22.10 €, apertura)
- 2026-10-02 00:20 [estocastico_rebote] ENTRADA AAVE @ 153.24 (21.81 €, apertura)
- 2026-10-02 00:20 [macd_momentum] ENTRADA ZEC @ 1190.41 (21.57 €, apertura)
- 2026-10-02 00:20 [macd_sin_salida] ENTRADA ZEC @ 1190.41 (21.79 €, apertura)
- 2026-10-02 00:20 [macd_momentum_regimen] ENTRADA ZEC @ 1190.41 (22.13 €, apertura)
- 2026-10-02 00:20 [macd_momentum_evento] ENTRADA ZEC @ 1190.41 (21.69 €, apertura)
- 2026-10-02 00:20 [estocastico_rebote] ENTRADA PUMP @ 0.005178 (21.81 €, apertura)
- 2026-10-02 00:20 [c_banda_atr] ENTRADA XLM @ 0.195284 (22.11 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen] ENTRADA XLM @ 0.195284 (21.79 €, apertura)
- 2026-10-02 00:20 [c_banda_atr_regimen] ENTRADA XLM @ 0.195284 (22.39 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen_regimen] ENTRADA XLM @ 0.195284 (21.87 €, apertura)
- 2026-10-02 00:20 [c_banda_atr_evento] ENTRADA XLM @ 0.195284 (22.26 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen_evento] ENTRADA XLM @ 0.195284 (22.10 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen] ENTRADA LTC @ 61.16 (21.79 €, apertura)
- 2026-10-02 00:20 [ruptura_estricta] ENTRADA LTC @ 61.16 (22.07 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen_regimen] ENTRADA LTC @ 61.16 (21.87 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen_evento] ENTRADA LTC @ 61.16 (22.10 €, apertura)
- 2026-10-02 00:25 [estocastico_rebote] CIERRE ARB timeout bruto +0.67% neto +0.17%
- 2026-10-02 00:20 [ruptura_estricta] ENTRADA FET @ 0.207 (22.07 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen] ENTRADA USELESS @ 0.2119 (21.79 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen_regimen] ENTRADA USELESS @ 0.2119 (21.87 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen_evento] ENTRADA USELESS @ 0.2119 (22.10 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen] ENTRADA RENDER @ 1.702 (21.79 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen_regimen] ENTRADA RENDER @ 1.702 (21.87 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen_evento] ENTRADA RENDER @ 1.702 (22.10 €, apertura)
- 2026-10-02 00:20 [pullback_tendencia] ENTRADA MINA @ 0.1356 (22.21 €, apertura)
- 2026-10-02 00:20 [c_banda_atr_regimen] ENTRADA VVV @ 23.329 (22.39 €, apertura)
- 2026-10-02 00:20 [ruptura_volumen_regimen] ENTRADA SHIB @ 5.155e-06 (21.87 €, apertura)
- 2026-10-02 00:20 [estocastico_rebote] ENTRADA TON @ 1.398 (21.81 €, apertura)
- 2026-10-02 00:20 [ruptura_estricta] ENTRADA SKY @ 0.0763 (22.07 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
