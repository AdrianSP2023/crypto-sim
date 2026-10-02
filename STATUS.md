# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 13:11 UTC · vueltas 407 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.31 € (-3.78%) | 371 | 23 | 40% | +0.140% | -0.430% | -0.551% | -36.33 € |
| reversion_bb | 920.11 € (-0.45%) | 74 | 2 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 857.02 € (-7.27%) | 464 | 20 | 26% | -0.104% | -0.660% | -0.769% | -68.34 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 886.38 € (-4.10%) | 274 | 12 | 21% | -0.017% | -0.614% | -0.699% | -38.12 € |
| macd_momentum | 846.45 € (-8.42%) | 759 | 30 | 24% | +0.064% | -0.471% | -0.570% | -79.16 € |
| estocastico_rebote | 877.45 € (-5.06%) | 467 | 21 | 37% | +0.101% | -0.455% | -0.562% | -48.12 € |
| ruptura_estricta | 880.47 € (-4.74%) | 255 | 14 | 32% | -0.147% | -0.751% | -0.866% | -43.51 € |
| macd_sin_salida | 876.64 € (-5.15%) | 498 | 29 | 40% | +0.122% | -0.431% | -0.540% | -48.69 € |
| c_banda_atr_tope | 913.60 € (-1.15%) | 84 | 5 | 38% | +0.258% | -0.556% | -0.676% | -10.75 € |
| ruptura_volumen_tope | 899.13 € (-2.72%) | 141 | 5 | 23% | -0.113% | -0.800% | -0.913% | -25.74 € |
| c_banda_atr_regimen | 901.84 € (-2.42%) | 223 | 23 | 42% | +0.155% | -0.462% | -0.591% | -23.67 € |
| macd_momentum_regimen | 869.12 € (-5.96%) | 522 | 30 | 24% | +0.068% | -0.482% | -0.582% | -56.51 € |
| ruptura_volumen_regimen | 861.67 € (-6.77%) | 387 | 20 | 24% | -0.168% | -0.735% | -0.849% | -63.70 € |
| c_banda_atr_evento | 894.44 € (-3.22%) | 336 | 7 | 41% | +0.185% | -0.394% | -0.509% | -30.23 € |
| macd_momentum_evento | 851.60 € (-7.86%) | 699 | 1 | 23% | +0.069% | -0.468% | -0.564% | -72.78 € |
| ruptura_volumen_evento | 867.47 € (-6.14%) | 410 | 4 | 26% | -0.056% | -0.621% | -0.723% | -57.09 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 13:10 | ruptura_volumen_tope | HYPE | timeout | -0.50% | -1.00% | -0.23 |
| 2026-10-02 13:10 | macd_sin_salida | FIL | timeout | +0.65% | +0.15% | +0.03 |
| 2026-10-02 13:10 | macd_sin_salida | CRV | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-02 13:05 | ruptura_volumen_regimen | NIGHT | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 13:05 | macd_momentum_regimen | PUMP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 13:05 | macd_sin_salida | PUMP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 13:05 | estocastico_rebote | KAS | timeout | +0.42% | -0.08% | -0.02 |
| 2026-10-02 13:05 | estocastico_rebote | SHIB | timeout | -0.49% | -0.99% | -0.22 |
| 2026-10-02 13:05 | estocastico_rebote | RENDER | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-02 13:05 | macd_momentum | PUMP | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 13:05 | pullback_tendencia | BTC | timeout | +0.72% | +0.22% | +0.05 |
| 2026-10-02 13:05 | ruptura_volumen | NIGHT | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 13:05 | reversion_bb | TAO | take-profit | +1.50% | +1.00% | +0.23 |
| 2026-10-02 13:00 | macd_momentum_regimen | TON | momentum perdido | +0.22% | -0.28% | -0.06 |
| 2026-10-02 13:00 | macd_sin_salida | ONDO | timeout | +0.82% | +0.33% | +0.07 |

## Eventos de la última vuelta

- 2026-10-02 13:05 [macd_momentum] ENTRADA BTC @ 77201.1 (21.13 €, apertura)
- 2026-10-02 13:05 [macd_momentum_regimen] ENTRADA BTC @ 77201.1 (21.69 €, apertura)
- 2026-10-02 13:05 [pullback_tendencia] ENTRADA ETH @ 2451.22 (22.15 €, apertura)
- 2026-10-02 13:05 [macd_momentum] ENTRADA ETH @ 2451.22 (21.13 €, apertura)
- 2026-10-02 13:05 [macd_momentum_regimen] ENTRADA ETH @ 2451.22 (21.69 €, apertura)
- 2026-10-02 13:05 [macd_momentum] ENTRADA LINK @ 12.8315 (21.13 €, apertura)
- 2026-10-02 13:05 [macd_momentum_regimen] ENTRADA LINK @ 12.8315 (21.69 €, apertura)
- 2026-10-02 13:05 [ruptura_estricta] ENTRADA SUI @ 1.0701 (22.02 €, apertura)
- 2026-10-02 13:05 [macd_momentum] ENTRADA ZEC @ 1235.32 (21.13 €, apertura)
- 2026-10-02 13:05 [macd_sin_salida] ENTRADA ZEC @ 1235.32 (21.89 €, apertura)
- 2026-10-02 13:05 [macd_momentum_regimen] ENTRADA ZEC @ 1235.32 (21.69 €, apertura)
- 2026-10-02 13:05 [ruptura_volumen] ENTRADA PUMP @ 0.005344 (21.40 €, apertura)
- 2026-10-02 13:05 [ruptura_volumen_regimen] ENTRADA PUMP @ 0.005344 (21.51 €, apertura)
- 2026-10-02 13:10 [ruptura_volumen_tope] CIERRE HYPE timeout bruto -0.50% neto -1.00%
- 2026-10-02 13:05 [ruptura_volumen] ENTRADA TAO @ 278.382 (21.40 €, apertura)
- 2026-10-02 13:05 [ruptura_volumen_tope] ENTRADA TAO @ 278.382 (22.46 €, apertura)
- 2026-10-02 13:05 [ruptura_volumen_regimen] ENTRADA TAO @ 278.382 (21.51 €, apertura)
- 2026-10-02 13:05 [macd_momentum] ENTRADA DOT @ 1.0897 (21.13 €, apertura)
- 2026-10-02 13:05 [macd_sin_salida] ENTRADA DOT @ 1.0897 (21.89 €, apertura)
- 2026-10-02 13:05 [macd_momentum_regimen] ENTRADA DOT @ 1.0897 (21.69 €, apertura)
- 2026-10-02 13:05 [estocastico_rebote] ENTRADA ALGO @ 0.11555 (21.90 €, apertura)
- 2026-10-02 13:10 [macd_sin_salida] CIERRE CRV timeout bruto -0.36% neto -0.86%
- 2026-10-02 13:05 [macd_momentum] ENTRADA BCH @ 281.2 (21.13 €, apertura)
- 2026-10-02 13:05 [macd_sin_salida] ENTRADA BCH @ 281.2 (21.89 €, apertura)
- 2026-10-02 13:05 [macd_momentum_regimen] ENTRADA BCH @ 281.2 (21.69 €, apertura)
- 2026-10-02 13:10 [macd_sin_salida] CIERRE FIL timeout bruto +0.65% neto +0.15%
- 2026-10-02 13:05 [ruptura_volumen] ENTRADA KSM @ 4.62 (21.40 €, apertura)
- 2026-10-02 13:05 [ruptura_volumen_regimen] ENTRADA KSM @ 4.62 (21.51 €, apertura)
- 2026-10-02 13:05 [macd_momentum] ENTRADA BNB @ 693.92 (21.13 €, apertura)
- 2026-10-02 13:05 [macd_sin_salida] ENTRADA BNB @ 693.92 (21.89 €, apertura)
- 2026-10-02 13:05 [macd_momentum_regimen] ENTRADA BNB @ 693.92 (21.69 €, apertura)
- 2026-10-02 13:05 [macd_momentum] ENTRADA TON @ 1.382 (21.13 €, apertura)
- 2026-10-02 13:05 [macd_momentum_regimen] ENTRADA TON @ 1.382 (21.69 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
