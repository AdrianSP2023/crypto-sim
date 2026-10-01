# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 00:56 UTC · vueltas 82 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.91 € (-2.31%) | 88 | 22 | 26% | -0.307% | -1.103% | -1.232% | -22.27 € |
| reversion_bb | 921.59 € (-0.29%) | 12 | 4 | 42% | +0.121% | -0.979% | -1.107% | -2.72 € |
| ruptura_volumen | 893.57 € (-3.32%) | 115 | 12 | 16% | -0.448% | -1.175% | -1.291% | -30.87 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.50 € (-2.14%) | 74 | 5 | 15% | -0.373% | -1.229% | -1.355% | -20.84 € |
| macd_momentum | 902.42 € (-2.36%) | 136 | 22 | 24% | -0.057% | -0.749% | -0.863% | -23.32 € |
| estocastico_rebote | 902.73 € (-2.33%) | 135 | 17 | 36% | -0.009% | -0.702% | -0.825% | -21.81 € |
| ruptura_estricta | 898.83 € (-2.75%) | 55 | 13 | 16% | -1.004% | -1.984% | -2.128% | -25.12 € |
| macd_sin_salida | 903.58 € (-2.23%) | 95 | 34 | 35% | -0.195% | -0.970% | -1.096% | -21.17 € |
| c_banda_atr_tope | 918.57 € (-0.61%) | 21 | 5 | 29% | -0.083% | -1.183% | -1.319% | -5.73 € |
| ruptura_volumen_tope | 915.50 € (-0.95%) | 32 | 5 | 19% | -0.117% | -1.217% | -1.299% | -8.97 € |
| c_banda_atr_regimen | 907.24 € (-1.84%) | 47 | 9 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.55 € (-1.70%) | 76 | 8 | 25% | -0.058% | -0.902% | -1.028% | -15.78 € |
| ruptura_volumen_regimen | 894.75 € (-3.19%) | 94 | 6 | 13% | -0.590% | -1.367% | -1.490% | -29.39 € |
| c_banda_atr_evento | 909.34 € (-1.61%) | 55 | 22 | 24% | -0.305% | -1.252% | -1.362% | -15.85 € |
| macd_momentum_evento | 907.42 € (-1.82%) | 89 | 22 | 17% | -0.103% | -0.899% | -1.000% | -18.34 € |
| ruptura_volumen_evento | 906.29 € (-1.94%) | 65 | 12 | 12% | -0.310% | -1.216% | -1.306% | -18.15 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 00:55 | ruptura_volumen_evento | BCH | timeout | -0.06% | -0.56% | -0.13 |
| 2026-10-01 00:55 | macd_momentum_evento | LTC | momentum perdido | -0.18% | -0.69% | -0.15 |
| 2026-10-01 00:55 | c_banda_atr_evento | HYPE | stop-loss | -1.60% | -2.40% | -0.55 |
| 2026-10-01 00:55 | ruptura_volumen_regimen | BCH | timeout | -0.06% | -0.56% | -0.13 |
| 2026-10-01 00:55 | c_banda_atr_tope | HYPE | stop-loss | -1.60% | -2.70% | -0.62 |
| 2026-10-01 00:55 | macd_sin_salida | HYPE | stop-loss | -1.60% | -2.10% | -0.47 |
| 2026-10-01 00:55 | macd_momentum | LTC | momentum perdido | -0.18% | -0.69% | -0.15 |
| 2026-10-01 00:55 | ruptura_volumen | BCH | timeout | -0.06% | -0.56% | -0.13 |
| 2026-10-01 00:55 | c_banda_atr | HYPE | stop-loss | -1.60% | -2.10% | -0.47 |
| 2026-10-01 00:50 | ruptura_volumen_evento | SPX | timeout | -0.43% | -0.94% | -0.21 |
| 2026-10-01 00:50 | ruptura_volumen_evento | ONDO | timeout | +1.20% | +0.70% | +0.16 |
| 2026-10-01 00:50 | ruptura_volumen_evento | AAVE | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 00:50 | ruptura_volumen_regimen | SPX | timeout | -0.43% | -0.94% | -0.21 |
| 2026-10-01 00:50 | ruptura_volumen_regimen | ONDO | timeout | +1.20% | +0.70% | +0.16 |
| 2026-10-01 00:50 | ruptura_volumen_regimen | AAVE | timeout | -0.16% | -0.66% | -0.15 |

## Eventos de la última vuelta

- 2026-10-01 00:50 [ruptura_volumen] ENTRADA SUI @ 1.0381 (22.34 €, apertura)
- 2026-10-01 00:50 [ruptura_volumen_regimen] ENTRADA SUI @ 1.0381 (22.37 €, apertura)
- 2026-10-01 00:50 [ruptura_volumen_evento] ENTRADA SUI @ 1.0381 (22.66 €, apertura)
- 2026-10-01 00:55 [c_banda_atr] CIERRE HYPE stop-loss bruto -1.60% neto -2.10%
- 2026-10-01 00:55 [macd_sin_salida] CIERRE HYPE stop-loss bruto -1.60% neto -2.10%
- 2026-10-01 00:55 [c_banda_atr_tope] CIERRE HYPE stop-loss bruto -1.60% neto -2.70%
- 2026-10-01 00:55 [c_banda_atr_evento] CIERRE HYPE stop-loss bruto -1.60% neto -2.40%
- 2026-10-01 00:50 [macd_momentum] ENTRADA XLM @ 0.20015 (22.53 €, apertura)
- 2026-10-01 00:50 [macd_momentum_regimen] ENTRADA XLM @ 0.20015 (22.71 €, apertura)
- 2026-10-01 00:50 [macd_momentum_evento] ENTRADA XLM @ 0.20015 (22.65 €, apertura)
- 2026-10-01 00:55 [macd_momentum] CIERRE LTC momentum perdido bruto -0.19% neto -0.69%
- 2026-10-01 00:55 [macd_momentum_evento] CIERRE LTC momentum perdido bruto -0.19% neto -0.69%
- 2026-10-01 00:50 [macd_momentum] ENTRADA ARB @ 0.1786 (22.52 €, apertura)
- 2026-10-01 00:50 [macd_momentum_regimen] ENTRADA ARB @ 0.1786 (22.71 €, apertura)
- 2026-10-01 00:50 [macd_momentum_evento] ENTRADA ARB @ 0.1786 (22.65 €, apertura)
- 2026-10-01 00:50 [ruptura_volumen] ENTRADA FET @ 0.2044 (22.34 €, apertura)
- 2026-10-01 00:50 [ruptura_estricta] ENTRADA FET @ 0.2044 (22.48 €, apertura)
- 2026-10-01 00:50 [ruptura_volumen_regimen] ENTRADA FET @ 0.2044 (22.37 €, apertura)
- 2026-10-01 00:50 [ruptura_volumen_evento] ENTRADA FET @ 0.2044 (22.66 €, apertura)
- 2026-10-01 00:50 [ruptura_estricta] ENTRADA ONDO @ 0.44677 (22.48 €, apertura)
- 2026-10-01 00:55 [ruptura_volumen] CIERRE BCH timeout bruto -0.06% neto -0.56%
- 2026-10-01 00:55 [ruptura_volumen_regimen] CIERRE BCH timeout bruto -0.06% neto -0.56%
- 2026-10-01 00:55 [ruptura_volumen_evento] CIERRE BCH timeout bruto -0.06% neto -0.56%
- 2026-10-01 00:50 [ruptura_volumen] ENTRADA OP @ 0.1152 (22.33 €, apertura)
- 2026-10-01 00:50 [ruptura_volumen_regimen] ENTRADA OP @ 0.1152 (22.37 €, apertura)
- 2026-10-01 00:50 [ruptura_volumen_evento] ENTRADA OP @ 0.1152 (22.65 €, apertura)
- 2026-10-01 00:50 [c_banda_atr_tope] ENTRADA KSM @ 4.6 (22.96 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
