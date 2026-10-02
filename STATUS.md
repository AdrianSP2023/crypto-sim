# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 13:26 UTC · vueltas 410 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.54 € (-3.86%) | 372 | 23 | 40% | +0.141% | -0.430% | -0.551% | -36.38 € |
| reversion_bb | 920.13 € (-0.44%) | 74 | 2 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 857.48 € (-7.22%) | 468 | 18 | 26% | -0.097% | -0.652% | -0.762% | -68.16 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 885.67 € (-4.17%) | 276 | 13 | 21% | -0.019% | -0.614% | -0.700% | -38.43 € |
| macd_momentum | 845.90 € (-8.48%) | 765 | 27 | 24% | +0.064% | -0.470% | -0.569% | -79.63 € |
| estocastico_rebote | 877.28 € (-5.08%) | 468 | 20 | 37% | +0.105% | -0.451% | -0.557% | -47.77 € |
| ruptura_estricta | 880.75 € (-4.71%) | 256 | 15 | 32% | -0.147% | -0.750% | -0.864% | -43.61 € |
| macd_sin_salida | 876.32 € (-5.19%) | 499 | 31 | 40% | +0.122% | -0.431% | -0.540% | -48.78 € |
| c_banda_atr_tope | 913.34 € (-1.18%) | 84 | 5 | 38% | +0.258% | -0.556% | -0.676% | -10.75 € |
| ruptura_volumen_tope | 899.45 € (-2.68%) | 142 | 5 | 23% | -0.095% | -0.780% | -0.894% | -25.29 € |
| c_banda_atr_regimen | 901.07 € (-2.51%) | 224 | 23 | 42% | +0.156% | -0.461% | -0.590% | -23.73 € |
| macd_momentum_regimen | 868.55 € (-6.03%) | 528 | 27 | 24% | +0.068% | -0.481% | -0.581% | -56.99 € |
| ruptura_volumen_regimen | 862.14 € (-6.72%) | 391 | 18 | 24% | -0.159% | -0.725% | -0.839% | -63.51 € |
| c_banda_atr_evento | 894.18 € (-3.25%) | 337 | 6 | 41% | +0.185% | -0.393% | -0.508% | -30.29 € |
| macd_momentum_evento | 851.60 € (-7.86%) | 699 | 1 | 23% | +0.069% | -0.468% | -0.564% | -72.78 € |
| ruptura_volumen_evento | 867.11 € (-6.18%) | 413 | 1 | 26% | -0.055% | -0.619% | -0.722% | -57.34 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 13:25 | ruptura_volumen_evento | WLFI | timeout | +0.40% | -0.10% | -0.02 |
| 2026-10-02 13:25 | ruptura_volumen_evento | BCH | timeout | -0.39% | -0.89% | -0.19 |
| 2026-10-02 13:25 | ruptura_volumen_regimen | WLFI | timeout | +0.40% | -0.10% | -0.02 |
| 2026-10-02 13:25 | ruptura_volumen_regimen | MON | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 13:25 | ruptura_volumen_regimen | BCH | timeout | -0.39% | -0.89% | -0.19 |
| 2026-10-02 13:25 | macd_momentum_regimen | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 13:25 | macd_momentum_regimen | XRP | momentum perdido | +0.01% | -0.49% | -0.11 |
| 2026-10-02 13:25 | ruptura_volumen_tope | MON | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-02 13:25 | macd_sin_salida | TRX | timeout | +0.07% | -0.43% | -0.10 |
| 2026-10-02 13:25 | ruptura_estricta | TRX | timeout | +0.07% | -0.43% | -0.10 |
| 2026-10-02 13:25 | macd_momentum | MON | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 13:25 | macd_momentum | XRP | momentum perdido | +0.01% | -0.49% | -0.10 |
| 2026-10-02 13:25 | ruptura_volumen | WLFI | timeout | +0.40% | -0.10% | -0.02 |
| 2026-10-02 13:25 | ruptura_volumen | MON | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 13:25 | ruptura_volumen | BCH | timeout | -0.39% | -0.89% | -0.19 |

## Eventos de la última vuelta

- 2026-10-02 13:25 [macd_momentum] CIERRE XRP momentum perdido bruto +0.01% neto -0.49%
- 2026-10-02 13:25 [macd_momentum_regimen] CIERRE XRP momentum perdido bruto +0.01% neto -0.49%
- 2026-10-02 13:20 [macd_momentum] ENTRADA HYPE @ 81.11 (21.11 €, apertura)
- 2026-10-02 13:20 [macd_sin_salida] ENTRADA HYPE @ 81.11 (21.89 €, apertura)
- 2026-10-02 13:20 [macd_momentum_regimen] ENTRADA HYPE @ 81.11 (21.67 €, apertura)
- 2026-10-02 13:20 [macd_momentum] ENTRADA LTC @ 62.3 (21.11 €, apertura)
- 2026-10-02 13:20 [macd_sin_salida] ENTRADA LTC @ 62.3 (21.89 €, apertura)
- 2026-10-02 13:20 [macd_momentum_regimen] ENTRADA LTC @ 62.3 (21.67 €, apertura)
- 2026-10-02 13:20 [ruptura_estricta] ENTRADA ZRO @ 1.688 (22.02 €, apertura)
- 2026-10-02 13:25 [ruptura_estricta] CIERRE TRX timeout bruto +0.07% neto -0.43%
- 2026-10-02 13:25 [macd_sin_salida] CIERRE TRX timeout bruto +0.07% neto -0.43%
- 2026-10-02 13:25 [ruptura_volumen] CIERRE BCH timeout bruto -0.39% neto -0.89%
- 2026-10-02 13:20 [pullback_tendencia] ENTRADA BCH @ 281.1 (22.15 €, apertura)
- 2026-10-02 13:25 [ruptura_volumen_regimen] CIERRE BCH timeout bruto -0.39% neto -0.89%
- 2026-10-02 13:25 [ruptura_volumen_evento] CIERRE BCH timeout bruto -0.39% neto -0.89%
- 2026-10-02 13:25 [ruptura_volumen] CIERRE MON take-profit bruto +2.50% neto +2.00%
- 2026-10-02 13:25 [macd_momentum] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-10-02 13:25 [ruptura_volumen_tope] CIERRE MON take-profit bruto +2.50% neto +2.00%
- 2026-10-02 13:25 [macd_momentum_regimen] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-10-02 13:25 [ruptura_volumen_regimen] CIERRE MON take-profit bruto +2.50% neto +2.00%
- 2026-10-02 13:25 [ruptura_volumen] CIERRE WLFI timeout bruto +0.40% neto -0.10%
- 2026-10-02 13:25 [ruptura_volumen_regimen] CIERRE WLFI timeout bruto +0.40% neto -0.10%
- 2026-10-02 13:25 [ruptura_volumen_evento] CIERRE WLFI timeout bruto +0.40% neto -0.10%
- 2026-10-02 13:20 [ruptura_volumen] ENTRADA TON @ 1.388 (21.40 €, apertura)
- 2026-10-02 13:20 [ruptura_volumen_tope] ENTRADA TON @ 1.388 (22.47 €, apertura)
- 2026-10-02 13:20 [ruptura_volumen_regimen] ENTRADA TON @ 1.388 (21.52 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
