# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 10:46 UTC · vueltas 418 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.61 € (-3.75%) | 349 | 22 | 40% | +0.140% | -0.435% | -0.555% | -34.59 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 858.20 € (-7.15%) | 445 | 12 | 26% | -0.108% | -0.667% | -0.775% | -66.34 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.92 € (-3.71%) | 253 | 10 | 21% | -0.010% | -0.614% | -0.702% | -35.30 € |
| macd_momentum | 850.51 € (-7.98%) | 705 | 22 | 23% | +0.057% | -0.480% | -0.581% | -75.14 € |
| estocastico_rebote | 880.89 € (-4.69%) | 430 | 34 | 38% | +0.112% | -0.449% | -0.555% | -43.78 € |
| ruptura_estricta | 882.26 € (-4.54%) | 239 | 16 | 32% | -0.149% | -0.760% | -0.876% | -41.31 € |
| macd_sin_salida | 880.54 € (-4.73%) | 454 | 40 | 40% | +0.106% | -0.452% | -0.562% | -46.64 € |
| c_banda_atr_tope | 913.18 € (-1.20%) | 79 | 5 | 38% | +0.232% | -0.602% | -0.716% | -10.94 € |
| ruptura_volumen_tope | 900.22 € (-2.60%) | 133 | 5 | 23% | -0.101% | -0.800% | -0.912% | -24.29 € |
| c_banda_atr_regimen | 902.12 € (-2.39%) | 202 | 21 | 42% | +0.156% | -0.474% | -0.601% | -22.02 € |
| macd_momentum_regimen | 873.28 € (-5.51%) | 468 | 22 | 24% | +0.058% | -0.497% | -0.600% | -52.38 € |
| ruptura_volumen_regimen | 862.86 € (-6.64%) | 368 | 12 | 24% | -0.177% | -0.748% | -0.860% | -61.68 € |
| c_banda_atr_evento | 895.53 € (-3.11%) | 316 | 22 | 41% | +0.187% | -0.397% | -0.512% | -28.67 € |
| macd_momentum_evento | 855.22 € (-7.47%) | 658 | 22 | 22% | +0.059% | -0.481% | -0.579% | -70.43 € |
| ruptura_volumen_evento | 870.41 € (-5.82%) | 395 | 12 | 27% | -0.043% | -0.610% | -0.712% | -54.13 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 10:45 | macd_sin_salida | POL | timeout | -0.53% | -1.03% | -0.23 |
| 2026-10-02 10:40 | ruptura_volumen_evento | ASTER | timeout | -0.75% | -1.25% | -0.27 |
| 2026-10-02 10:40 | macd_momentum_evento | ZRO | momentum perdido | -1.21% | -1.71% | -0.37 |
| 2026-10-02 10:40 | ruptura_volumen_regimen | ASTER | timeout | -0.75% | -1.25% | -0.27 |
| 2026-10-02 10:40 | macd_momentum_regimen | ZRO | momentum perdido | -1.21% | -1.71% | -0.37 |
| 2026-10-02 10:40 | estocastico_rebote | LTC | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 10:40 | macd_momentum | ZRO | momentum perdido | -1.21% | -1.71% | -0.36 |
| 2026-10-02 10:40 | pullback_tendencia | SHIB | rotura de tendencia | -0.53% | -1.03% | -0.23 |
| 2026-10-02 10:40 | pullback_tendencia | XRP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 10:40 | ruptura_volumen | ASTER | timeout | -0.75% | -1.25% | -0.27 |
| 2026-10-02 10:35 | macd_momentum_evento | CRV | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-02 10:35 | c_banda_atr_evento | TRUMP | timeout | +1.50% | +1.00% | +0.22 |
| 2026-10-02 10:35 | c_banda_atr_evento | TAO | timeout | +0.73% | +0.23% | +0.05 |
| 2026-10-02 10:35 | c_banda_atr_evento | AVAX | timeout | +1.09% | +0.59% | +0.13 |
| 2026-10-02 10:35 | macd_momentum_regimen | CRV | momentum perdido | -0.24% | -0.74% | -0.16 |

## Eventos de la última vuelta

- 2026-10-02 10:40 [macd_momentum] ENTRADA SOL @ 108.53 (21.23 €, apertura)
- 2026-10-02 10:40 [macd_momentum_regimen] ENTRADA SOL @ 108.53 (21.80 €, apertura)
- 2026-10-02 10:40 [macd_momentum_evento] ENTRADA SOL @ 108.53 (21.35 €, apertura)
- 2026-10-02 10:40 [macd_momentum] ENTRADA LINK @ 12.8497 (21.23 €, apertura)
- 2026-10-02 10:40 [macd_sin_salida] ENTRADA LINK @ 12.8497 (21.95 €, apertura)
- 2026-10-02 10:40 [macd_momentum_regimen] ENTRADA LINK @ 12.8497 (21.80 €, apertura)
- 2026-10-02 10:40 [macd_momentum_evento] ENTRADA LINK @ 12.8497 (21.35 €, apertura)
- 2026-10-02 10:40 [macd_momentum] ENTRADA SUI @ 1.0534 (21.23 €, apertura)
- 2026-10-02 10:40 [macd_momentum_regimen] ENTRADA SUI @ 1.0534 (21.80 €, apertura)
- 2026-10-02 10:40 [macd_momentum_evento] ENTRADA SUI @ 1.0534 (21.35 €, apertura)
- 2026-10-02 10:40 [macd_momentum] ENTRADA XLM @ 0.201487 (21.23 €, apertura)
- 2026-10-02 10:40 [macd_momentum_regimen] ENTRADA XLM @ 0.201487 (21.80 €, apertura)
- 2026-10-02 10:40 [macd_momentum_evento] ENTRADA XLM @ 0.201487 (21.35 €, apertura)
- 2026-10-02 10:40 [pullback_tendencia] ENTRADA TAO @ 277.898 (22.22 €, apertura)
- 2026-10-02 10:45 [macd_sin_salida] CIERRE POL timeout bruto -0.53% neto -1.03%
- 2026-10-02 10:40 [macd_momentum] ENTRADA ALGO @ 0.11656 (21.23 €, apertura)
- 2026-10-02 10:40 [macd_sin_salida] ENTRADA ALGO @ 0.11656 (21.94 €, apertura)
- 2026-10-02 10:40 [macd_momentum_regimen] ENTRADA ALGO @ 0.11656 (21.80 €, apertura)
- 2026-10-02 10:40 [macd_momentum_evento] ENTRADA ALGO @ 0.11656 (21.35 €, apertura)
- 2026-10-02 10:40 [macd_momentum] ENTRADA FIL @ 0.923 (21.23 €, apertura)
- 2026-10-02 10:40 [macd_momentum_regimen] ENTRADA FIL @ 0.923 (21.80 €, apertura)
- 2026-10-02 10:40 [macd_momentum_evento] ENTRADA FIL @ 0.923 (21.35 €, apertura)
- 2026-10-02 10:40 [macd_momentum] ENTRADA SEI @ 0.06429 (21.23 €, apertura)
- 2026-10-02 10:40 [macd_sin_salida] ENTRADA SEI @ 0.06429 (20.74 €, apertura)
- 2026-10-02 10:40 [macd_momentum_regimen] ENTRADA SEI @ 0.06429 (21.80 €, apertura)
- 2026-10-02 10:40 [macd_momentum_evento] ENTRADA SEI @ 0.06429 (21.35 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
