# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 22:31 UTC · vueltas 95 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.69 € (-2.22%) | 64 | 30 | 20% | -0.593% | -1.501% | -1.650% | -22.04 € |
| reversion_bb | 922.11 € (-0.23%) | 9 | 5 | 44% | -0.167% | -1.267% | -1.401% | -2.64 € |
| ruptura_volumen | 896.47 € (-3.00%) | 91 | 3 | 15% | -0.563% | -1.350% | -1.489% | -28.12 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.59 € (-2.13%) | 65 | 1 | 15% | -0.413% | -1.319% | -1.456% | -19.65 € |
| macd_momentum | 905.14 € (-2.07%) | 100 | 12 | 24% | -0.100% | -0.861% | -0.993% | -19.75 € |
| estocastico_rebote | 902.91 € (-2.31%) | 124 | 11 | 34% | -0.056% | -0.766% | -0.898% | -21.86 € |
| ruptura_estricta | 898.65 € (-2.77%) | 48 | 6 | 10% | -1.282% | -2.332% | -2.480% | -25.75 € |
| macd_sin_salida | 904.12 € (-2.18%) | 80 | 18 | 31% | -0.317% | -1.143% | -1.276% | -21.02 € |
| c_banda_atr_tope | 919.54 € (-0.51%) | 18 | 5 | 28% | -0.168% | -1.268% | -1.428% | -5.26 € |
| ruptura_volumen_tope | 917.11 € (-0.77%) | 24 | 5 | 17% | -0.322% | -1.422% | -1.541% | -7.86 € |
| c_banda_atr_regimen | 908.47 € (-1.71%) | 45 | 0 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 911.50 € (-1.38%) | 31 | 30 | 10% | -0.895% | -1.995% | -2.132% | -14.24 € |
| macd_momentum_evento | 910.29 € (-1.51%) | 53 | 12 | 15% | -0.213% | -1.200% | -1.327% | -14.60 € |
| ruptura_volumen_evento | 909.63 € (-1.58%) | 41 | 3 | 10% | -0.486% | -1.586% | -1.711% | -14.96 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 22:30 | ruptura_volumen_evento | JUP | timeout | -0.56% | -1.66% | -0.38 |
| 2026-09-30 22:30 | ruptura_volumen_evento | DOGE | timeout | -0.16% | -1.26% | -0.29 |
| 2026-09-30 22:30 | estocastico_rebote | NEAR | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 22:30 | ruptura_volumen | JUP | timeout | -0.56% | -1.06% | -0.24 |
| 2026-09-30 22:30 | ruptura_volumen | DOGE | timeout | -0.16% | -0.66% | -0.15 |
| 2026-09-30 22:25 | ruptura_volumen_evento | ASTER | timeout | +0.45% | -0.65% | -0.15 |
| 2026-09-30 22:25 | ruptura_volumen_evento | XDC | timeout | +0.13% | -0.97% | -0.22 |
| 2026-09-30 22:25 | ruptura_volumen_evento | POL | timeout | -0.38% | -1.48% | -0.34 |
| 2026-09-30 22:25 | ruptura_volumen_evento | LTC | timeout | +0.63% | -0.47% | -0.11 |
| 2026-09-30 22:25 | ruptura_volumen_evento | HYPE | timeout | +1.18% | +0.08% | +0.02 |
| 2026-09-30 22:25 | ruptura_volumen | ASTER | timeout | +0.45% | -0.05% | -0.01 |
| 2026-09-30 22:25 | ruptura_volumen | XDC | timeout | +0.13% | -0.37% | -0.08 |
| 2026-09-30 22:25 | ruptura_volumen | POL | timeout | -0.38% | -0.88% | -0.20 |
| 2026-09-30 22:25 | ruptura_volumen | LTC | timeout | +0.63% | +0.13% | +0.03 |
| 2026-09-30 22:25 | ruptura_volumen | HYPE | timeout | +1.18% | +0.68% | +0.15 |

## Eventos de la última vuelta

- 2026-09-30 22:25 [c_banda_atr] ENTRADA XRP @ 1.31488 (22.56 €, apertura)
- 2026-09-30 22:25 [c_banda_atr_evento] ENTRADA XRP @ 1.31488 (22.75 €, apertura)
- 2026-09-30 22:25 [c_banda_atr] ENTRADA ETH @ 2368.79 (22.56 €, apertura)
- 2026-09-30 22:25 [c_banda_atr_evento] ENTRADA ETH @ 2368.79 (22.75 €, apertura)
- 2026-09-30 22:30 [estocastico_rebote] CIERRE NEAR take-profit bruto +1.80% neto +1.30%
- 2026-09-30 22:25 [macd_momentum] ENTRADA ADA @ 0.216554 (22.61 €, apertura)
- 2026-09-30 22:25 [macd_sin_salida] ENTRADA ADA @ 0.216554 (22.58 €, apertura)
- 2026-09-30 22:25 [macd_momentum_evento] ENTRADA ADA @ 0.216554 (22.74 €, apertura)
- 2026-09-30 22:25 [macd_momentum] ENTRADA SUI @ 1.0247 (22.61 €, apertura)
- 2026-09-30 22:25 [macd_sin_salida] ENTRADA SUI @ 1.0247 (22.58 €, apertura)
- 2026-09-30 22:25 [macd_momentum_evento] ENTRADA SUI @ 1.0247 (22.74 €, apertura)
- 2026-09-30 22:25 [c_banda_atr] ENTRADA AAVE @ 140.57 (22.56 €, apertura)
- 2026-09-30 22:25 [macd_momentum] ENTRADA AAVE @ 140.57 (22.61 €, apertura)
- 2026-09-30 22:25 [macd_sin_salida] ENTRADA AAVE @ 140.57 (22.58 €, apertura)
- 2026-09-30 22:25 [c_banda_atr_evento] ENTRADA AAVE @ 140.57 (22.75 €, apertura)
- 2026-09-30 22:25 [macd_momentum_evento] ENTRADA AAVE @ 140.57 (22.74 €, apertura)
- 2026-09-30 22:25 [c_banda_atr] ENTRADA ZEC @ 1255.43 (22.56 €, apertura)
- 2026-09-30 22:25 [c_banda_atr_evento] ENTRADA ZEC @ 1255.43 (22.75 €, apertura)
- 2026-09-30 22:30 [ruptura_volumen] CIERRE DOGE timeout bruto -0.16% neto -0.66%
- 2026-09-30 22:30 [ruptura_volumen_evento] CIERRE DOGE timeout bruto -0.16% neto -1.26%
- 2026-09-30 22:25 [estocastico_rebote] ENTRADA FET @ 0.2005 (22.56 €, apertura)
- 2026-09-30 22:25 [c_banda_atr] ENTRADA ONDO @ 0.43994 (22.56 €, apertura)
- 2026-09-30 22:25 [macd_momentum] ENTRADA ONDO @ 0.43994 (22.61 €, apertura)
- 2026-09-30 22:25 [c_banda_atr_evento] ENTRADA ONDO @ 0.43994 (22.75 €, apertura)
- 2026-09-30 22:25 [macd_momentum_evento] ENTRADA ONDO @ 0.43994 (22.74 €, apertura)
- 2026-09-30 22:25 [c_banda_atr] ENTRADA USELESS @ 0.2124 (22.56 €, apertura)
- 2026-09-30 22:25 [c_banda_atr_evento] ENTRADA USELESS @ 0.2124 (22.75 €, apertura)
- 2026-09-30 22:30 [ruptura_volumen] CIERRE JUP timeout bruto -0.56% neto -1.06%
- 2026-09-30 22:30 [ruptura_volumen_evento] CIERRE JUP timeout bruto -0.56% neto -1.66%
- 2026-09-30 22:25 [macd_momentum] ENTRADA VVV @ 24.443 (22.61 €, apertura)
- 2026-09-30 22:25 [macd_sin_salida] ENTRADA VVV @ 24.443 (22.58 €, apertura)
- 2026-09-30 22:25 [macd_momentum_evento] ENTRADA VVV @ 24.443 (22.74 €, apertura)
- 2026-09-30 22:25 [c_banda_atr] ENTRADA APT @ 0.6755 (22.56 €, apertura)
- 2026-09-30 22:25 [c_banda_atr_evento] ENTRADA APT @ 0.6755 (22.75 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
