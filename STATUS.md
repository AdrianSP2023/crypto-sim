# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 00:36 UTC · vueltas 342 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.70 € (-4.17%) | 272 | 21 | 34% | -0.047% | -0.643% | -0.765% | -39.74 € |
| reversion_bb | 918.55 € (-0.62%) | 53 | 16 | 51% | +0.343% | -0.650% | -0.747% | -7.94 € |
| ruptura_volumen | 872.17 € (-5.63%) | 298 | 27 | 24% | -0.198% | -0.786% | -0.894% | -52.75 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.28 € (-3.89%) | 190 | 5 | 15% | -0.201% | -0.840% | -0.929% | -36.21 € |
| macd_momentum | 863.79 € (-6.54%) | 491 | 15 | 20% | -0.007% | -0.560% | -0.663% | -61.58 € |
| estocastico_rebote | 872.90 € (-5.56%) | 334 | 13 | 31% | -0.106% | -0.684% | -0.794% | -51.54 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 5 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 872.14 € (-5.64%) | 348 | 17 | 34% | -0.097% | -0.672% | -0.783% | -52.84 € |
| c_banda_atr_tope | 911.58 € (-1.37%) | 62 | 4 | 31% | +0.026% | -0.900% | -1.015% | -12.81 € |
| ruptura_volumen_tope | 905.63 € (-2.01%) | 102 | 4 | 26% | -0.041% | -0.800% | -0.917% | -18.70 € |
| c_banda_atr_regimen | 895.84 € (-3.07%) | 138 | 4 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 885.17 € (-4.23%) | 276 | 4 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 875.28 € (-5.30%) | 230 | 23 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 891.59 € (-3.53%) | 239 | 21 | 34% | -0.011% | -0.622% | -0.738% | -33.85 € |
| macd_momentum_evento | 868.57 € (-6.02%) | 444 | 15 | 19% | -0.011% | -0.570% | -0.670% | -56.80 € |
| ruptura_volumen_evento | 884.58 € (-4.29%) | 248 | 27 | 25% | -0.112% | -0.718% | -0.819% | -40.34 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 00:35 | ruptura_volumen_evento | WLFI | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 00:35 | ruptura_volumen_tope | WLFI | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 00:35 | c_banda_atr_tope | FET | timeout | +1.52% | +1.02% | +0.23 |
| 2026-10-02 00:35 | estocastico_rebote | WLFI | timeout | +0.40% | -0.10% | -0.02 |
| 2026-10-02 00:35 | ruptura_volumen | WLFI | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 00:30 | estocastico_rebote | USELESS | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 00:30 | pullback_tendencia | PUMP | rotura de tendencia | -0.50% | -1.00% | -0.22 |
| 2026-10-02 00:25 | estocastico_rebote | ARB | timeout | +0.68% | +0.17% | +0.04 |
| 2026-10-02 00:20 | macd_momentum_evento | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:20 | c_banda_atr_evento | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:20 | macd_sin_salida | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:20 | estocastico_rebote | JUP | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 00:20 | estocastico_rebote | AVAX | timeout | +0.13% | -0.37% | -0.08 |
| 2026-10-02 00:20 | macd_momentum | SKY | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 00:20 | reversion_bb | OP | take-profit | +1.69% | +1.19% | +0.27 |

## Eventos de la última vuelta

- 2026-10-02 00:35 [c_banda_atr_tope] CIERRE FET timeout bruto +1.52% neto +1.02%
- 2026-10-02 00:30 [ruptura_volumen] ENTRADA WLD @ 0.4516 (21.79 €, apertura)
- 2026-10-02 00:30 [ruptura_volumen_regimen] ENTRADA WLD @ 0.4516 (21.87 €, apertura)
- 2026-10-02 00:30 [ruptura_volumen_evento] ENTRADA WLD @ 0.4516 (22.10 €, apertura)
- 2026-10-02 00:35 [ruptura_volumen] CIERRE WLFI timeout bruto +0.00% neto -0.50%
- 2026-10-02 00:35 [estocastico_rebote] CIERRE WLFI timeout bruto +0.40% neto -0.10%
- 2026-10-02 00:35 [ruptura_volumen_tope] CIERRE WLFI timeout bruto +0.00% neto -0.50%
- 2026-10-02 00:35 [ruptura_volumen_evento] CIERRE WLFI timeout bruto +0.00% neto -0.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
