# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 14:26 UTC · vueltas 422 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 883.58 € (-4.40%) | 384 | 19 | 39% | +0.116% | -0.452% | -0.573% | -39.43 € |
| reversion_bb | 920.07 € (-0.45%) | 74 | 3 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 853.74 € (-7.63%) | 486 | 11 | 26% | -0.095% | -0.648% | -0.758% | -70.26 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 881.52 € (-4.62%) | 297 | 6 | 19% | -0.050% | -0.639% | -0.724% | -42.91 € |
| macd_momentum | 838.55 € (-9.27%) | 803 | 2 | 23% | +0.049% | -0.483% | -0.583% | -85.66 € |
| estocastico_rebote | 874.92 € (-5.34%) | 480 | 24 | 37% | +0.090% | -0.464% | -0.570% | -50.37 € |
| ruptura_estricta | 879.14 € (-4.88%) | 261 | 16 | 32% | -0.131% | -0.732% | -0.847% | -43.39 € |
| macd_sin_salida | 870.18 € (-5.85%) | 518 | 21 | 39% | +0.101% | -0.450% | -0.558% | -52.71 € |
| c_banda_atr_tope | 912.58 € (-1.26%) | 85 | 4 | 38% | +0.237% | -0.573% | -0.693% | -11.21 € |
| ruptura_volumen_tope | 898.30 € (-2.81%) | 148 | 0 | 23% | -0.090% | -0.769% | -0.884% | -25.95 € |
| c_banda_atr_regimen | 895.84 € (-3.07%) | 237 | 18 | 40% | +0.108% | -0.502% | -0.631% | -27.27 € |
| macd_momentum_regimen | 861.00 € (-6.84%) | 566 | 2 | 23% | +0.047% | -0.499% | -0.599% | -63.18 € |
| ruptura_volumen_regimen | 858.38 € (-7.13%) | 409 | 11 | 24% | -0.154% | -0.718% | -0.832% | -65.63 € |
| c_banda_atr_evento | 893.52 € (-3.32%) | 341 | 2 | 41% | +0.184% | -0.393% | -0.508% | -30.62 € |
| macd_momentum_evento | 851.52 € (-7.87%) | 700 | 1 | 23% | +0.070% | -0.468% | -0.564% | -72.75 € |
| ruptura_volumen_evento | 867.45 € (-6.14%) | 415 | 0 | 27% | -0.046% | -0.610% | -0.713% | -56.78 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 14:25 | ruptura_volumen_evento | ZRO | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 14:25 | ruptura_volumen_regimen | ZRO | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 14:25 | macd_momentum_regimen | LTC | momentum perdido | +0.18% | -0.32% | -0.07 |
| 2026-10-02 14:25 | ruptura_volumen_tope | ZRO | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-02 14:25 | ruptura_estricta | BCH | timeout | -0.97% | -1.47% | -0.32 |
| 2026-10-02 14:25 | macd_momentum | LTC | momentum perdido | +0.18% | -0.32% | -0.07 |
| 2026-10-02 14:25 | ruptura_volumen | ZRO | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 14:20 | ruptura_volumen_regimen | BTC | timeout | -0.50% | -1.00% | -0.21 |
| 2026-10-02 14:20 | macd_momentum_regimen | FIL | momentum perdido | +1.30% | +0.80% | +0.17 |
| 2026-10-02 14:20 | macd_momentum_regimen | AAVE | momentum perdido | -0.87% | -1.37% | -0.30 |
| 2026-10-02 14:20 | ruptura_estricta | TRUMP | stop-loss | -2.10% | -2.60% | -0.57 |
| 2026-10-02 14:20 | estocastico_rebote | TRUMP | stop-loss | -1.55% | -2.05% | -0.45 |
| 2026-10-02 14:20 | macd_momentum | FIL | momentum perdido | +1.30% | +0.80% | +0.17 |
| 2026-10-02 14:20 | macd_momentum | AAVE | momentum perdido | -0.87% | -1.37% | -0.29 |
| 2026-10-02 14:20 | ruptura_volumen | BTC | timeout | -0.50% | -1.00% | -0.21 |

## Eventos de la última vuelta

- 2026-10-02 14:20 [pullback_tendencia] ENTRADA QNT @ 221.17 (22.03 €, apertura)
- 2026-10-02 14:25 [macd_momentum] CIERRE LTC momentum perdido bruto +0.18% neto -0.32%
- 2026-10-02 14:25 [macd_momentum_regimen] CIERRE LTC momentum perdido bruto +0.18% neto -0.32%
- 2026-10-02 14:25 [ruptura_volumen] CIERRE ZRO take-profit bruto +2.50% neto +2.00%
- 2026-10-02 14:20 [ruptura_estricta] ENTRADA ZRO @ 1.773 (22.03 €, apertura)
- 2026-10-02 14:25 [ruptura_volumen_tope] CIERRE ZRO take-profit bruto +2.50% neto +2.00%
- 2026-10-02 14:25 [ruptura_volumen_regimen] CIERRE ZRO take-profit bruto +2.50% neto +2.00%
- 2026-10-02 14:25 [ruptura_volumen_evento] CIERRE ZRO take-profit bruto +2.50% neto +2.00%
- 2026-10-02 14:20 [estocastico_rebote] ENTRADA ARB @ 0.1822 (21.85 €, apertura)
- 2026-10-02 14:20 [pullback_tendencia] ENTRADA WLD @ 0.51 (22.03 €, apertura)
- 2026-10-02 14:25 [ruptura_estricta] CIERRE BCH timeout bruto -0.97% neto -1.47%
- 2026-10-02 14:20 [pullback_tendencia] ENTRADA SKY @ 0.08317 (22.03 €, apertura)
- 2026-10-02 14:20 [macd_momentum] ENTRADA SKY @ 0.08317 (20.96 €, apertura)
- 2026-10-02 14:20 [macd_sin_salida] ENTRADA SKY @ 0.08317 (21.79 €, apertura)
- 2026-10-02 14:20 [macd_momentum_regimen] ENTRADA SKY @ 0.08317 (21.53 €, apertura)
- 2026-10-02 14:20 [macd_momentum_evento] ENTRADA SKY @ 0.08317 (21.29 €, apertura)
- 2026-10-02 14:20 [estocastico_rebote] ENTRADA SPX @ 0.3966 (21.85 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
