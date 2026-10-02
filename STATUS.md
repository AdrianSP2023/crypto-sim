# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 07:56 UTC · vueltas 384 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.72 € (-3.73%) | 333 | 20 | 39% | +0.124% | -0.454% | -0.575% | -34.48 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 862.66 € (-6.66%) | 413 | 6 | 27% | -0.112% | -0.676% | -0.784% | -62.49 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.71 € (-3.74%) | 237 | 7 | 20% | -0.036% | -0.647% | -0.733% | -34.84 € |
| macd_momentum | 854.17 € (-7.58%) | 645 | 12 | 22% | +0.046% | -0.494% | -0.596% | -70.98 € |
| estocastico_rebote | 879.39 € (-4.85%) | 387 | 40 | 36% | +0.043% | -0.524% | -0.633% | -45.99 € |
| ruptura_estricta | 882.34 € (-4.53%) | 231 | 5 | 32% | -0.185% | -0.799% | -0.913% | -41.99 € |
| macd_sin_salida | 880.20 € (-4.76%) | 432 | 20 | 40% | +0.113% | -0.447% | -0.558% | -44.02 € |
| c_banda_atr_tope | 913.21 € (-1.19%) | 76 | 5 | 37% | +0.213% | -0.634% | -0.750% | -11.08 € |
| ruptura_volumen_tope | 901.30 € (-2.48%) | 127 | 4 | 24% | -0.087% | -0.795% | -0.908% | -23.06 € |
| c_banda_atr_regimen | 902.16 € (-2.39%) | 185 | 20 | 40% | +0.131% | -0.510% | -0.640% | -21.73 € |
| macd_momentum_regimen | 877.04 € (-5.11%) | 408 | 12 | 22% | +0.041% | -0.523% | -0.626% | -48.11 € |
| ruptura_volumen_regimen | 867.34 € (-6.16%) | 336 | 6 | 24% | -0.188% | -0.766% | -0.879% | -57.81 € |
| c_banda_atr_evento | 895.64 € (-3.09%) | 300 | 20 | 40% | +0.172% | -0.416% | -0.533% | -28.56 € |
| macd_momentum_evento | 858.90 € (-7.07%) | 598 | 12 | 21% | +0.048% | -0.497% | -0.595% | -66.25 € |
| ruptura_volumen_evento | 874.93 € (-5.34%) | 363 | 6 | 28% | -0.042% | -0.614% | -0.717% | -50.22 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 07:55 | ruptura_volumen_evento | VVV | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-02 07:55 | ruptura_volumen_evento | PUMP | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:55 | ruptura_volumen_regimen | VVV | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-02 07:55 | ruptura_volumen_regimen | PUMP | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:55 | ruptura_volumen_tope | PUMP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 07:55 | estocastico_rebote | OP | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 07:55 | ruptura_volumen | VVV | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-02 07:55 | ruptura_volumen | PUMP | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:50 | ruptura_volumen_evento | MINA | take-profit | +2.56% | +2.06% | +0.45 |
| 2026-10-02 07:50 | ruptura_volumen_regimen | MINA | take-profit | +2.56% | +2.06% | +0.45 |
| 2026-10-02 07:50 | ruptura_estricta | APT | timeout | -0.01% | -0.51% | -0.11 |
| 2026-10-02 07:50 | ruptura_estricta | KAS | timeout | -1.03% | -1.53% | -0.34 |
| 2026-10-02 07:50 | rebote_extremo | QNT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-10-02 07:50 | ruptura_volumen | MINA | take-profit | +2.56% | +2.06% | +0.44 |
| 2026-10-02 07:45 | ruptura_volumen_evento | XMR | timeout | +0.00% | -0.50% | -0.11 |

## Eventos de la última vuelta

- 2026-10-02 07:50 [macd_momentum] ENTRADA XRP @ 1.35765 (21.33 €, apertura)
- 2026-10-02 07:50 [macd_momentum_regimen] ENTRADA XRP @ 1.35765 (21.90 €, apertura)
- 2026-10-02 07:50 [macd_momentum_evento] ENTRADA XRP @ 1.35765 (21.45 €, apertura)
- 2026-10-02 07:50 [pullback_tendencia] ENTRADA AVAX @ 9.83 (22.24 €, apertura)
- 2026-10-02 07:50 [macd_momentum] ENTRADA HBAR @ 0.09275 (21.33 €, apertura)
- 2026-10-02 07:50 [macd_sin_salida] ENTRADA HBAR @ 0.09275 (22.01 €, apertura)
- 2026-10-02 07:50 [macd_momentum_regimen] ENTRADA HBAR @ 0.09275 (21.90 €, apertura)
- 2026-10-02 07:50 [macd_momentum_evento] ENTRADA HBAR @ 0.09275 (21.45 €, apertura)
- 2026-10-02 07:55 [ruptura_volumen] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:55 [ruptura_volumen_tope] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:55 [ruptura_volumen_regimen] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:55 [ruptura_volumen_evento] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:50 [c_banda_atr] ENTRADA DOT @ 1.0886 (22.24 €, apertura)
- 2026-10-02 07:50 [ruptura_volumen] ENTRADA DOT @ 1.0886 (21.54 €, apertura)
- 2026-10-02 07:50 [ruptura_volumen_tope] ENTRADA DOT @ 1.0886 (22.53 €, apertura)
- 2026-10-02 07:50 [c_banda_atr_regimen] ENTRADA DOT @ 1.0886 (22.56 €, apertura)
- 2026-10-02 07:50 [ruptura_volumen_regimen] ENTRADA DOT @ 1.0886 (21.66 €, apertura)
- 2026-10-02 07:50 [c_banda_atr_evento] ENTRADA DOT @ 1.0886 (22.39 €, apertura)
- 2026-10-02 07:50 [ruptura_volumen_evento] ENTRADA DOT @ 1.0886 (21.85 €, apertura)
- 2026-10-02 07:50 [ruptura_volumen] ENTRADA CRV @ 0.33836 (21.54 €, apertura)
- 2026-10-02 07:50 [ruptura_volumen_tope] ENTRADA CRV @ 0.33836 (22.53 €, apertura)
- 2026-10-02 07:50 [ruptura_volumen_regimen] ENTRADA CRV @ 0.33836 (21.66 €, apertura)
- 2026-10-02 07:50 [ruptura_volumen_evento] ENTRADA CRV @ 0.33836 (21.85 €, apertura)
- 2026-10-02 07:50 [macd_momentum] ENTRADA USELESS @ 0.22256 (21.33 €, apertura)
- 2026-10-02 07:50 [macd_sin_salida] ENTRADA USELESS @ 0.22256 (22.01 €, apertura)
- 2026-10-02 07:50 [macd_momentum_regimen] ENTRADA USELESS @ 0.22256 (21.90 €, apertura)
- 2026-10-02 07:50 [macd_momentum_evento] ENTRADA USELESS @ 0.22256 (21.45 €, apertura)
- 2026-10-02 07:50 [c_banda_atr] ENTRADA BCH @ 279.68 (22.24 €, apertura)
- 2026-10-02 07:50 [c_banda_atr_regimen] ENTRADA BCH @ 279.68 (22.56 €, apertura)
- 2026-10-02 07:50 [c_banda_atr_evento] ENTRADA BCH @ 279.68 (22.39 €, apertura)
- 2026-10-02 07:55 [estocastico_rebote] CIERRE OP take-profit bruto +1.80% neto +1.30%
- 2026-10-02 07:50 [estocastico_rebote] ENTRADA FIL @ 0.921 (21.96 €, apertura)
- 2026-10-02 07:55 [ruptura_volumen] CIERRE VVV timeout bruto +0.91% neto +0.41%
- 2026-10-02 07:55 [ruptura_volumen_regimen] CIERRE VVV timeout bruto +0.91% neto +0.41%
- 2026-10-02 07:55 [ruptura_volumen_evento] CIERRE VVV timeout bruto +0.91% neto +0.41%
- 2026-10-02 07:50 [macd_momentum] ENTRADA SHIB @ 5.26e-06 (21.33 €, apertura)
- 2026-10-02 07:50 [macd_momentum_regimen] ENTRADA SHIB @ 5.26e-06 (21.90 €, apertura)
- 2026-10-02 07:50 [macd_momentum_evento] ENTRADA SHIB @ 5.26e-06 (21.45 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
