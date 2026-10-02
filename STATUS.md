# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 14:31 UTC · vueltas 423 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 882.12 € (-4.56%) | 386 | 19 | 39% | +0.108% | -0.459% | -0.580% | -40.28 € |
| reversion_bb | 919.88 € (-0.47%) | 74 | 3 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 852.92 € (-7.72%) | 487 | 11 | 26% | -0.097% | -0.651% | -0.760% | -70.62 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 880.98 € (-4.68%) | 297 | 6 | 19% | -0.050% | -0.639% | -0.724% | -42.91 € |
| macd_momentum | 838.43 € (-9.28%) | 803 | 2 | 23% | +0.049% | -0.483% | -0.583% | -85.66 € |
| estocastico_rebote | 872.43 € (-5.61%) | 480 | 32 | 37% | +0.090% | -0.464% | -0.570% | -50.37 € |
| ruptura_estricta | 877.83 € (-5.02%) | 262 | 15 | 32% | -0.138% | -0.738% | -0.854% | -43.95 € |
| macd_sin_salida | 868.56 € (-6.02%) | 519 | 20 | 39% | +0.099% | -0.451% | -0.559% | -52.96 € |
| c_banda_atr_tope | 912.11 € (-1.31%) | 86 | 5 | 37% | +0.219% | -0.588% | -0.706% | -11.62 € |
| ruptura_volumen_tope | 898.30 € (-2.81%) | 148 | 1 | 23% | -0.090% | -0.769% | -0.884% | -25.95 € |
| c_banda_atr_regimen | 894.47 € (-3.22%) | 239 | 18 | 39% | +0.096% | -0.514% | -0.641% | -28.13 € |
| macd_momentum_regimen | 860.88 € (-6.86%) | 566 | 2 | 23% | +0.047% | -0.499% | -0.599% | -63.18 € |
| ruptura_volumen_regimen | 857.55 € (-7.22%) | 410 | 11 | 24% | -0.156% | -0.720% | -0.834% | -65.99 € |
| c_banda_atr_evento | 893.21 € (-3.36%) | 342 | 4 | 41% | +0.180% | -0.397% | -0.512% | -31.03 € |
| macd_momentum_evento | 851.42 € (-7.88%) | 700 | 1 | 23% | +0.070% | -0.468% | -0.564% | -72.75 € |
| ruptura_volumen_evento | 867.45 € (-6.14%) | 415 | 1 | 27% | -0.046% | -0.610% | -0.713% | -56.78 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 14:30 | c_banda_atr_evento | XLM | timeout | -1.30% | -1.80% | -0.40 |
| 2026-10-02 14:30 | ruptura_volumen_regimen | DOGE | stop-loss | -1.20% | -1.70% | -0.36 |
| 2026-10-02 14:30 | c_banda_atr_regimen | XLM | timeout | -1.30% | -1.80% | -0.41 |
| 2026-10-02 14:30 | c_banda_atr_regimen | ETH | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 14:30 | c_banda_atr_tope | XLM | timeout | -1.30% | -1.80% | -0.41 |
| 2026-10-02 14:30 | macd_sin_salida | TAO | timeout | -0.68% | -1.18% | -0.26 |
| 2026-10-02 14:30 | ruptura_estricta | ZRO | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-02 14:30 | ruptura_volumen | DOGE | stop-loss | -1.20% | -1.70% | -0.36 |
| 2026-10-02 14:30 | c_banda_atr | XLM | timeout | -1.30% | -1.80% | -0.40 |
| 2026-10-02 14:30 | c_banda_atr | ETH | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 14:25 | ruptura_volumen_evento | ZRO | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 14:25 | ruptura_volumen_regimen | ZRO | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 14:25 | macd_momentum_regimen | LTC | momentum perdido | +0.18% | -0.32% | -0.07 |
| 2026-10-02 14:25 | ruptura_volumen_tope | ZRO | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-02 14:25 | ruptura_estricta | BCH | timeout | -0.97% | -1.47% | -0.32 |

## Eventos de la última vuelta

- 2026-10-02 14:25 [estocastico_rebote] ENTRADA BTC @ 76737.1 (21.85 €, apertura)
- 2026-10-02 14:30 [c_banda_atr] CIERRE ETH stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:30 [c_banda_atr_regimen] CIERRE ETH stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:25 [estocastico_rebote] ENTRADA SOL @ 108.34 (21.85 €, apertura)
- 2026-10-02 14:25 [estocastico_rebote] ENTRADA SUI @ 1.0562 (21.85 €, apertura)
- 2026-10-02 14:25 [estocastico_rebote] ENTRADA ZEC @ 1234.61 (21.85 €, apertura)
- 2026-10-02 14:30 [c_banda_atr] CIERRE XLM timeout bruto -1.30% neto -1.80%
- 2026-10-02 14:30 [c_banda_atr_tope] CIERRE XLM timeout bruto -1.30% neto -1.80%
- 2026-10-02 14:30 [c_banda_atr_regimen] CIERRE XLM timeout bruto -1.30% neto -1.80%
- 2026-10-02 14:30 [c_banda_atr_evento] CIERRE XLM timeout bruto -1.30% neto -1.80%
- 2026-10-02 14:25 [estocastico_rebote] ENTRADA TAO @ 276.28 (21.85 €, apertura)
- 2026-10-02 14:30 [macd_sin_salida] CIERRE TAO timeout bruto -0.68% neto -1.18%
- 2026-10-02 14:30 [ruptura_estricta] CIERRE ZRO stop-loss bruto -2.00% neto -2.50%
- 2026-10-02 14:30 [ruptura_volumen] CIERRE DOGE stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 14:30 [ruptura_volumen_regimen] CIERRE DOGE stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 14:25 [c_banda_atr] ENTRADA POL @ 0.09956 (22.10 €, apertura)
- 2026-10-02 14:25 [c_banda_atr_tope] ENTRADA POL @ 0.09956 (22.82 €, apertura)
- 2026-10-02 14:25 [c_banda_atr_regimen] ENTRADA POL @ 0.09956 (22.40 €, apertura)
- 2026-10-02 14:25 [c_banda_atr_evento] ENTRADA POL @ 0.09956 (22.33 €, apertura)
- 2026-10-02 14:25 [estocastico_rebote] ENTRADA NIGHT @ 0.04226 (21.85 €, apertura)
- 2026-10-02 14:25 [estocastico_rebote] ENTRADA RENDER @ 1.767 (21.85 €, apertura)
- 2026-10-02 14:25 [c_banda_atr_tope] ENTRADA WLFI @ 0.0503 (22.82 €, apertura)
- 2026-10-02 14:25 [c_banda_atr_evento] ENTRADA WLFI @ 0.0503 (22.33 €, apertura)
- 2026-10-02 14:25 [estocastico_rebote] ENTRADA PENGU @ 0.008738 (21.85 €, apertura)
- 2026-10-02 14:25 [c_banda_atr] ENTRADA XMR @ 484.77 (22.10 €, apertura)
- 2026-10-02 14:25 [ruptura_volumen] ENTRADA XMR @ 484.77 (21.34 €, apertura)
- 2026-10-02 14:25 [ruptura_volumen_tope] ENTRADA XMR @ 484.77 (22.46 €, apertura)
- 2026-10-02 14:25 [c_banda_atr_regimen] ENTRADA XMR @ 484.77 (22.40 €, apertura)
- 2026-10-02 14:25 [ruptura_volumen_regimen] ENTRADA XMR @ 484.77 (21.46 €, apertura)
- 2026-10-02 14:25 [c_banda_atr_evento] ENTRADA XMR @ 484.77 (22.33 €, apertura)
- 2026-10-02 14:25 [ruptura_volumen_evento] ENTRADA XMR @ 484.77 (21.69 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
