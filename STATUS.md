# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 13:06 UTC · vueltas 406 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.18 € (-3.69%) | 371 | 23 | 40% | +0.140% | -0.430% | -0.551% | -36.33 € |
| reversion_bb | 920.22 € (-0.44%) | 74 | 2 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 857.91 € (-7.18%) | 464 | 17 | 26% | -0.104% | -0.660% | -0.769% | -68.34 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 886.63 € (-4.07%) | 274 | 11 | 21% | -0.017% | -0.614% | -0.699% | -38.12 € |
| macd_momentum | 847.48 € (-8.31%) | 759 | 22 | 24% | +0.064% | -0.471% | -0.570% | -79.16 € |
| estocastico_rebote | 878.08 € (-4.99%) | 467 | 20 | 37% | +0.101% | -0.455% | -0.562% | -48.12 € |
| ruptura_estricta | 880.80 € (-4.70%) | 255 | 13 | 32% | -0.147% | -0.751% | -0.866% | -43.51 € |
| macd_sin_salida | 877.83 € (-5.02%) | 496 | 27 | 40% | +0.122% | -0.431% | -0.540% | -48.53 € |
| c_banda_atr_tope | 913.83 € (-1.13%) | 84 | 5 | 38% | +0.258% | -0.556% | -0.676% | -10.75 € |
| ruptura_volumen_tope | 899.33 € (-2.70%) | 140 | 5 | 23% | -0.110% | -0.799% | -0.913% | -25.51 € |
| c_banda_atr_regimen | 902.72 € (-2.33%) | 223 | 23 | 42% | +0.155% | -0.462% | -0.591% | -23.67 € |
| macd_momentum_regimen | 870.17 € (-5.85%) | 522 | 22 | 24% | +0.068% | -0.482% | -0.582% | -56.51 € |
| ruptura_volumen_regimen | 862.57 € (-6.67%) | 387 | 17 | 24% | -0.168% | -0.735% | -0.849% | -63.70 € |
| c_banda_atr_evento | 894.49 € (-3.22%) | 336 | 7 | 41% | +0.185% | -0.394% | -0.509% | -30.23 € |
| macd_momentum_evento | 851.60 € (-7.86%) | 699 | 1 | 23% | +0.069% | -0.468% | -0.564% | -72.78 € |
| ruptura_volumen_evento | 867.48 € (-6.14%) | 410 | 4 | 26% | -0.056% | -0.621% | -0.723% | -57.09 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-02 13:00 | estocastico_rebote | DASH | timeout | +0.27% | -0.23% | -0.05 |
| 2026-10-02 13:00 | estocastico_rebote | ZRO | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-02 13:00 | macd_momentum | TON | momentum perdido | +0.22% | -0.28% | -0.06 |

## Eventos de la última vuelta

- 2026-10-02 13:05 [pullback_tendencia] CIERRE BTC timeout bruto +0.72% neto +0.22%
- 2026-10-02 13:05 [macd_momentum] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 13:05 [macd_sin_salida] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 13:05 [macd_momentum_regimen] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 13:05 [reversion_bb] CIERRE TAO take-profit bruto +1.50% neto +1.00%
- 2026-10-02 13:00 [ruptura_volumen] ENTRADA UNI @ 8.0908 (21.39 €, apertura)
- 2026-10-02 13:00 [ruptura_estricta] ENTRADA UNI @ 8.0908 (22.02 €, apertura)
- 2026-10-02 13:00 [ruptura_volumen_regimen] ENTRADA UNI @ 8.0908 (21.50 €, apertura)
- 2026-10-02 13:00 [ruptura_volumen] ENTRADA ZRO @ 1.679 (21.39 €, apertura)
- 2026-10-02 13:00 [ruptura_volumen_regimen] ENTRADA ZRO @ 1.679 (21.50 €, apertura)
- 2026-10-02 13:00 [macd_momentum] ENTRADA ONDO @ 0.45349 (21.13 €, apertura)
- 2026-10-02 13:00 [macd_momentum_regimen] ENTRADA ONDO @ 0.45349 (21.69 €, apertura)
- 2026-10-02 13:05 [ruptura_volumen] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%
- 2026-10-02 13:05 [ruptura_volumen_regimen] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%
- 2026-10-02 13:05 [estocastico_rebote] CIERRE RENDER timeout bruto +0.23% neto -0.27%
- 2026-10-02 13:05 [estocastico_rebote] CIERRE SHIB timeout bruto -0.49% neto -0.99%
- 2026-10-02 13:05 [estocastico_rebote] CIERRE KAS timeout bruto +0.42% neto -0.08%
- 2026-10-02 13:00 [pullback_tendencia] ENTRADA SKY @ 0.08198 (22.15 €, apertura)
- 2026-10-02 13:00 [ruptura_estricta] ENTRADA APT @ 0.742 (22.02 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
