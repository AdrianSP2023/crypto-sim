# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 02:01 UTC · vueltas 359 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 886.17 € (-4.12%) | 276 | 31 | 34% | -0.034% | -0.628% | -0.750% | -39.38 € |
| reversion_bb | 918.30 € (-0.64%) | 59 | 13 | 53% | +0.386% | -0.556% | -0.664% | -7.57 € |
| ruptura_volumen | 867.95 € (-6.09%) | 314 | 24 | 24% | -0.230% | -0.813% | -0.920% | -57.36 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.58 € (-3.86%) | 193 | 6 | 15% | -0.201% | -0.837% | -0.925% | -36.66 € |
| macd_momentum | 861.07 € (-6.84%) | 516 | 18 | 21% | -0.003% | -0.553% | -0.655% | -63.83 € |
| estocastico_rebote | 873.30 € (-5.51%) | 339 | 16 | 32% | -0.096% | -0.673% | -0.783% | -51.46 € |
| ruptura_estricta | 882.85 € (-4.48%) | 167 | 15 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 872.13 € (-5.64%) | 357 | 26 | 34% | -0.097% | -0.670% | -0.782% | -54.04 € |
| c_banda_atr_tope | 911.79 € (-1.35%) | 65 | 5 | 29% | +0.034% | -0.872% | -0.988% | -13.02 € |
| ruptura_volumen_tope | 903.59 € (-2.23%) | 109 | 5 | 25% | -0.093% | -0.835% | -0.948% | -20.84 € |
| c_banda_atr_regimen | 896.43 € (-3.01%) | 139 | 20 | 29% | -0.197% | -0.885% | -1.018% | -28.14 € |
| macd_momentum_regimen | 884.44 € (-4.31%) | 285 | 11 | 20% | -0.026% | -0.618% | -0.723% | -39.89 € |
| ruptura_volumen_regimen | 872.06 € (-5.65%) | 240 | 21 | 19% | -0.376% | -0.984% | -1.098% | -53.22 € |
| c_banda_atr_evento | 892.07 € (-3.48%) | 243 | 31 | 35% | +0.004% | -0.605% | -0.722% | -33.49 € |
| macd_momentum_evento | 865.84 € (-6.32%) | 469 | 18 | 19% | -0.006% | -0.562% | -0.660% | -59.06 € |
| ruptura_volumen_evento | 880.30 € (-4.75%) | 264 | 24 | 24% | -0.155% | -0.755% | -0.853% | -45.02 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 02:00 | ruptura_volumen_evento | ASTER | stop-loss | -1.21% | -1.71% | -0.38 |
| 2026-10-02 02:00 | ruptura_volumen_evento | JUP | timeout | +1.26% | +0.76% | +0.17 |
| 2026-10-02 02:00 | c_banda_atr_evento | NIGHT | take-profit | +2.70% | +2.20% | +0.49 |
| 2026-10-02 02:00 | ruptura_volumen_regimen | ASTER | stop-loss | -1.21% | -1.71% | -0.37 |
| 2026-10-02 02:00 | ruptura_volumen_tope | ASTER | stop-loss | -1.21% | -1.71% | -0.39 |
| 2026-10-02 02:00 | c_banda_atr_tope | LTC | timeout | +0.39% | -0.11% | -0.02 |
| 2026-10-02 02:00 | ruptura_volumen | ASTER | stop-loss | -1.21% | -1.71% | -0.37 |
| 2026-10-02 02:00 | ruptura_volumen | JUP | timeout | +1.26% | +0.76% | +0.17 |
| 2026-10-02 02:00 | c_banda_atr | NIGHT | take-profit | +2.70% | +2.20% | +0.49 |
| 2026-10-02 01:55 | ruptura_volumen_evento | SHIB | timeout | -0.15% | -0.66% | -0.14 |
| 2026-10-02 01:55 | ruptura_volumen | SHIB | timeout | -0.15% | -0.66% | -0.14 |
| 2026-10-02 01:55 | reversion_bb | SOL | take-profit | +1.50% | +1.00% | +0.23 |
| 2026-10-02 01:50 | ruptura_volumen_evento | AVAX | timeout | -0.98% | -1.48% | -0.33 |
| 2026-10-02 01:50 | macd_momentum_evento | ICP | momentum perdido | -0.31% | -0.81% | -0.17 |
| 2026-10-02 01:50 | ruptura_volumen_tope | AVAX | timeout | -0.98% | -1.48% | -0.34 |

## Eventos de la última vuelta

- 2026-10-02 01:55 [c_banda_atr] ENTRADA BTC @ 75486.6 (22.11 €, apertura)
- 2026-10-02 01:55 [macd_momentum] ENTRADA BTC @ 75486.6 (21.51 €, apertura)
- 2026-10-02 01:55 [macd_sin_salida] ENTRADA BTC @ 75486.6 (21.76 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_regimen] ENTRADA BTC @ 75486.6 (22.40 €, apertura)
- 2026-10-02 01:55 [macd_momentum_regimen] ENTRADA BTC @ 75486.6 (22.11 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_evento] ENTRADA BTC @ 75486.6 (22.26 €, apertura)
- 2026-10-02 01:55 [macd_momentum_evento] ENTRADA BTC @ 75486.6 (21.63 €, apertura)
- 2026-10-02 01:55 [c_banda_atr] ENTRADA XRP @ 1.32927 (22.11 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_regimen] ENTRADA XRP @ 1.32927 (22.40 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_evento] ENTRADA XRP @ 1.32927 (22.26 €, apertura)
- 2026-10-02 01:55 [ruptura_volumen] ENTRADA ETH @ 2413.57 (21.68 €, apertura)
- 2026-10-02 01:55 [macd_momentum] ENTRADA ETH @ 2413.57 (21.51 €, apertura)
- 2026-10-02 01:55 [ruptura_estricta] ENTRADA ETH @ 2413.57 (22.06 €, apertura)
- 2026-10-02 01:55 [ruptura_volumen_tope] ENTRADA ETH @ 2413.57 (22.59 €, apertura)
- 2026-10-02 01:55 [macd_momentum_regimen] ENTRADA ETH @ 2413.57 (22.11 €, apertura)
- 2026-10-02 01:55 [ruptura_volumen_regimen] ENTRADA ETH @ 2413.57 (21.78 €, apertura)
- 2026-10-02 01:55 [macd_momentum_evento] ENTRADA ETH @ 2413.57 (21.63 €, apertura)
- 2026-10-02 01:55 [ruptura_volumen_evento] ENTRADA ETH @ 2413.57 (21.99 €, apertura)
- 2026-10-02 01:55 [macd_momentum] ENTRADA SOL @ 106.25 (21.51 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_regimen] ENTRADA SOL @ 106.25 (22.40 €, apertura)
- 2026-10-02 01:55 [macd_momentum_regimen] ENTRADA SOL @ 106.25 (22.11 €, apertura)
- 2026-10-02 01:55 [macd_momentum_evento] ENTRADA SOL @ 106.25 (21.63 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_regimen] ENTRADA ADA @ 0.218799 (22.40 €, apertura)
- 2026-10-02 01:55 [c_banda_atr] ENTRADA SUI @ 1.0531 (22.11 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_regimen] ENTRADA SUI @ 1.0531 (22.40 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_evento] ENTRADA SUI @ 1.0531 (22.26 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_regimen] ENTRADA ZEC @ 1185.81 (22.40 €, apertura)
- 2026-10-02 01:55 [macd_momentum] ENTRADA XLM @ 0.194877 (21.51 €, apertura)
- 2026-10-02 01:55 [macd_sin_salida] ENTRADA XLM @ 0.194877 (21.76 €, apertura)
- 2026-10-02 01:55 [macd_momentum_regimen] ENTRADA XLM @ 0.194877 (22.11 €, apertura)
- 2026-10-02 01:55 [macd_momentum_evento] ENTRADA XLM @ 0.194877 (21.63 €, apertura)
- 2026-10-02 01:55 [c_banda_atr] ENTRADA TAO @ 270.703 (22.11 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_regimen] ENTRADA TAO @ 270.703 (22.40 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_evento] ENTRADA TAO @ 270.703 (22.26 €, apertura)
- 2026-10-02 01:55 [c_banda_atr] ENTRADA UNI @ 7.981 (22.11 €, apertura)
- 2026-10-02 01:55 [macd_momentum] ENTRADA UNI @ 7.981 (21.51 €, apertura)
- 2026-10-02 01:55 [macd_sin_salida] ENTRADA UNI @ 7.981 (21.76 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_regimen] ENTRADA UNI @ 7.981 (22.40 €, apertura)
- 2026-10-02 01:55 [macd_momentum_regimen] ENTRADA UNI @ 7.981 (22.11 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_evento] ENTRADA UNI @ 7.981 (22.26 €, apertura)
- 2026-10-02 01:55 [macd_momentum_evento] ENTRADA UNI @ 7.981 (21.63 €, apertura)
- 2026-10-02 02:00 [c_banda_atr_tope] CIERRE LTC timeout bruto +0.39% neto -0.11%
- 2026-10-02 01:55 [macd_momentum] ENTRADA DOT @ 1.0486 (21.51 €, apertura)
- 2026-10-02 01:55 [macd_sin_salida] ENTRADA DOT @ 1.0486 (21.76 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_tope] ENTRADA DOT @ 1.0486 (22.78 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_regimen] ENTRADA DOT @ 1.0486 (22.40 €, apertura)
- 2026-10-02 01:55 [macd_momentum_regimen] ENTRADA DOT @ 1.0486 (22.11 €, apertura)
- 2026-10-02 01:55 [macd_momentum_evento] ENTRADA DOT @ 1.0486 (21.63 €, apertura)
- 2026-10-02 01:55 [macd_momentum] ENTRADA ARB @ 0.1798 (21.51 €, apertura)
- 2026-10-02 01:55 [macd_sin_salida] ENTRADA ARB @ 0.1798 (21.76 €, apertura)
- 2026-10-02 01:55 [macd_momentum_regimen] ENTRADA ARB @ 0.1798 (22.11 €, apertura)
- 2026-10-02 01:55 [macd_momentum_evento] ENTRADA ARB @ 0.1798 (21.63 €, apertura)
- 2026-10-02 01:55 [macd_momentum] ENTRADA FET @ 0.2087 (21.51 €, apertura)
- 2026-10-02 01:55 [macd_sin_salida] ENTRADA FET @ 0.2087 (21.76 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_regimen] ENTRADA FET @ 0.2087 (22.40 €, apertura)
- 2026-10-02 01:55 [macd_momentum_regimen] ENTRADA FET @ 0.2087 (22.11 €, apertura)
- 2026-10-02 01:55 [macd_momentum_evento] ENTRADA FET @ 0.2087 (21.63 €, apertura)
- 2026-10-02 01:55 [macd_momentum] ENTRADA ALGO @ 0.10981 (21.51 €, apertura)
- 2026-10-02 01:55 [macd_sin_salida] ENTRADA ALGO @ 0.10981 (21.76 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_regimen] ENTRADA ALGO @ 0.10981 (22.40 €, apertura)
- 2026-10-02 01:55 [macd_momentum_regimen] ENTRADA ALGO @ 0.10981 (22.11 €, apertura)
- 2026-10-02 01:55 [macd_momentum_evento] ENTRADA ALGO @ 0.10981 (21.63 €, apertura)
- 2026-10-02 02:00 [c_banda_atr] CIERRE NIGHT take-profit bruto +2.70% neto +2.20%
- 2026-10-02 02:00 [c_banda_atr_evento] CIERRE NIGHT take-profit bruto +2.70% neto +2.20%
- 2026-10-02 01:55 [c_banda_atr] ENTRADA USELESS @ 0.21551 (22.12 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_regimen] ENTRADA USELESS @ 0.21551 (22.40 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_evento] ENTRADA USELESS @ 0.21551 (22.27 €, apertura)
- 2026-10-02 02:00 [ruptura_volumen] CIERRE JUP timeout bruto +1.26% neto +0.76%
- 2026-10-02 02:00 [ruptura_volumen_evento] CIERRE JUP timeout bruto +1.26% neto +0.76%
- 2026-10-02 02:00 [ruptura_volumen] CIERRE ASTER stop-loss bruto -1.21% neto -1.71%
- 2026-10-02 02:00 [ruptura_volumen_tope] CIERRE ASTER stop-loss bruto -1.21% neto -1.71%
- 2026-10-02 02:00 [ruptura_volumen_regimen] CIERRE ASTER stop-loss bruto -1.21% neto -1.71%
- 2026-10-02 02:00 [ruptura_volumen_evento] CIERRE ASTER stop-loss bruto -1.21% neto -1.71%
- 2026-10-02 01:55 [macd_momentum] ENTRADA BNB @ 686.81 (21.51 €, apertura)
- 2026-10-02 01:55 [macd_momentum_regimen] ENTRADA BNB @ 686.81 (22.11 €, apertura)
- 2026-10-02 01:55 [macd_momentum_evento] ENTRADA BNB @ 686.81 (21.63 €, apertura)
- 2026-10-02 01:55 [macd_momentum] ENTRADA APT @ 0.6981 (21.51 €, apertura)
- 2026-10-02 01:55 [macd_sin_salida] ENTRADA APT @ 0.6981 (21.76 €, apertura)
- 2026-10-02 01:55 [ruptura_volumen_tope] ENTRADA APT @ 0.6981 (22.59 €, apertura)
- 2026-10-02 01:55 [macd_momentum_regimen] ENTRADA APT @ 0.6981 (22.11 €, apertura)
- 2026-10-02 01:55 [macd_momentum_evento] ENTRADA APT @ 0.6981 (21.63 €, apertura)
- 2026-10-02 01:55 [estocastico_rebote] ENTRADA SPX @ 0.3919 (21.82 €, apertura)
- 2026-10-02 01:55 [c_banda_atr_regimen] ENTRADA SPX @ 0.3919 (22.40 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
