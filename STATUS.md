# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 20:31 UTC · vueltas 71 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.78 € (-1.56%) | 49 | 29 | 27% | -0.396% | -1.423% | -1.574% | -16.06 € |
| reversion_bb | 922.74 € (-0.16%) | 7 | 5 | 57% | +0.214% | -0.886% | -1.014% | -1.44 € |
| ruptura_volumen | 899.04 € (-2.73%) | 74 | 12 | 14% | -0.665% | -1.518% | -1.656% | -25.76 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 906.35 € (-1.94%) | 58 | 3 | 16% | -0.440% | -1.395% | -1.533% | -18.56 € |
| macd_momentum | 909.55 € (-1.59%) | 79 | 11 | 27% | -0.026% | -0.856% | -0.992% | -15.57 € |
| estocastico_rebote | 907.32 € (-1.83%) | 99 | 23 | 38% | -0.027% | -0.790% | -0.925% | -18.03 € |
| ruptura_estricta | 899.46 € (-2.68%) | 46 | 5 | 11% | -1.277% | -2.350% | -2.498% | -24.89 € |
| macd_sin_salida | 906.86 € (-1.88%) | 66 | 14 | 33% | -0.296% | -1.192% | -1.330% | -18.12 € |
| c_banda_atr_tope | 921.61 € (-0.28%) | 14 | 5 | 36% | +0.100% | -1.000% | -1.153% | -3.23 € |
| ruptura_volumen_tope | 918.90 € (-0.58%) | 18 | 5 | 22% | -0.331% | -1.431% | -1.522% | -5.94 € |
| c_banda_atr_regimen | 908.97 € (-1.65%) | 43 | 2 | 26% | -0.480% | -1.573% | -1.728% | -15.58 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 919.38 € (-0.53%) | 17 | 28 | 18% | -0.577% | -1.677% | -1.812% | -6.59 € |
| macd_momentum_evento | 916.24 € (-0.87%) | 32 | 11 | 19% | -0.106% | -1.206% | -1.338% | -8.88 € |
| ruptura_volumen_evento | 914.58 € (-1.04%) | 24 | 12 | 8% | -0.746% | -1.846% | -1.960% | -10.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 20:25 | estocastico_rebote | ASTER | timeout | +0.17% | -0.33% | -0.08 |
| 2026-09-30 20:25 | estocastico_rebote | FET | take-profit | +1.99% | +1.49% | +0.34 |
| 2026-09-30 20:25 | pullback_tendencia | FET | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 20:20 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 20:20 | ruptura_estricta | MON | timeout | +1.86% | +1.06% | +0.24 |
| 2026-09-30 20:20 | estocastico_rebote | XDC | timeout | +0.53% | +0.03% | +0.01 |
| 2026-09-30 20:10 | rebote_extremo | ONDO | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 20:05 | c_banda_atr_evento | SEI | timeout | -0.82% | -1.92% | -0.44 |
| 2026-09-30 20:05 | c_banda_atr_evento | XMR | timeout | +0.17% | -0.93% | -0.21 |
| 2026-09-30 20:05 | c_banda_atr_regimen | SEI | timeout | -0.82% | -1.62% | -0.37 |
| 2026-09-30 20:05 | c_banda_atr_tope | XMR | timeout | +0.17% | -0.93% | -0.21 |
| 2026-09-30 20:05 | macd_sin_salida | ALGO | stop-loss | -1.51% | -2.01% | -0.46 |
| 2026-09-30 20:05 | c_banda_atr | SEI | timeout | -0.82% | -1.62% | -0.37 |
| 2026-09-30 20:00 | macd_momentum_evento | TON | momentum perdido | -0.22% | -1.32% | -0.30 |
| 2026-09-30 20:00 | macd_momentum_evento | XLM | momentum perdido | +0.15% | -0.95% | -0.22 |

## Eventos de la última vuelta

- 2026-09-30 20:25 [macd_momentum] ENTRADA LINK @ 12.6536 (22.72 €, apertura)
- 2026-09-30 20:25 [macd_sin_salida] ENTRADA LINK @ 12.6536 (22.65 €, apertura)
- 2026-09-30 20:25 [macd_momentum_evento] ENTRADA LINK @ 12.6536 (22.88 €, apertura)
- 2026-09-30 20:25 [c_banda_atr] ENTRADA AVAX @ 9.66 (22.70 €, apertura)
- 2026-09-30 20:25 [c_banda_atr_evento] ENTRADA AVAX @ 9.66 (22.94 €, apertura)
- 2026-09-30 20:25 [c_banda_atr] ENTRADA ZEC @ 1259.16 (22.70 €, apertura)
- 2026-09-30 20:25 [c_banda_atr_evento] ENTRADA ZEC @ 1259.16 (22.94 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen] ENTRADA HYPE @ 79.67 (22.46 €, apertura)
- 2026-09-30 20:25 [macd_momentum] ENTRADA HYPE @ 79.67 (22.72 €, apertura)
- 2026-09-30 20:25 [macd_momentum_evento] ENTRADA HYPE @ 79.67 (22.88 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen_evento] ENTRADA HYPE @ 79.67 (22.85 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen] ENTRADA LTC @ 58.84 (22.46 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen_evento] ENTRADA LTC @ 58.84 (22.85 €, apertura)
- 2026-09-30 20:25 [c_banda_atr] ENTRADA ARB @ 0.1812 (22.70 €, apertura)
- 2026-09-30 20:25 [macd_momentum] ENTRADA ARB @ 0.1812 (22.72 €, apertura)
- 2026-09-30 20:25 [macd_sin_salida] ENTRADA ARB @ 0.1812 (22.65 €, apertura)
- 2026-09-30 20:25 [c_banda_atr_evento] ENTRADA ARB @ 0.1812 (22.94 €, apertura)
- 2026-09-30 20:25 [macd_momentum_evento] ENTRADA ARB @ 0.1812 (22.88 €, apertura)
- 2026-09-30 20:25 [macd_momentum] ENTRADA ENA @ 0.2339 (22.72 €, apertura)
- 2026-09-30 20:25 [macd_sin_salida] ENTRADA ENA @ 0.2339 (22.65 €, apertura)
- 2026-09-30 20:25 [macd_momentum_evento] ENTRADA ENA @ 0.2339 (22.88 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen] ENTRADA FET @ 0.2008 (22.46 €, apertura)
- 2026-09-30 20:25 [ruptura_estricta] ENTRADA FET @ 0.2008 (22.48 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen_evento] ENTRADA FET @ 0.2008 (22.85 €, apertura)
- 2026-09-30 20:25 [c_banda_atr] ENTRADA POL @ 0.09904 (22.70 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen] ENTRADA POL @ 0.09904 (22.46 €, apertura)
- 2026-09-30 20:25 [macd_momentum] ENTRADA POL @ 0.09904 (22.72 €, apertura)
- 2026-09-30 20:25 [macd_sin_salida] ENTRADA POL @ 0.09904 (22.65 €, apertura)
- 2026-09-30 20:25 [c_banda_atr_evento] ENTRADA POL @ 0.09904 (22.94 €, apertura)
- 2026-09-30 20:25 [macd_momentum_evento] ENTRADA POL @ 0.09904 (22.88 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen_evento] ENTRADA POL @ 0.09904 (22.85 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen] ENTRADA WLD @ 0.474 (22.46 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen_evento] ENTRADA WLD @ 0.474 (22.85 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen] ENTRADA XDC @ 0.03044 (22.46 €, apertura)
- 2026-09-30 20:25 [ruptura_estricta] ENTRADA XDC @ 0.03044 (22.48 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen_evento] ENTRADA XDC @ 0.03044 (22.85 €, apertura)
- 2026-09-30 20:25 [c_banda_atr] ENTRADA VVV @ 24.314 (22.70 €, apertura)
- 2026-09-30 20:25 [c_banda_atr_evento] ENTRADA VVV @ 24.314 (22.94 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen] ENTRADA ASTER @ 0.67086 (22.46 €, apertura)
- 2026-09-30 20:25 [ruptura_volumen_evento] ENTRADA ASTER @ 0.67086 (22.85 €, apertura)
- 2026-09-30 20:25 [c_banda_atr] ENTRADA PENGU @ 0.008597 (22.70 €, apertura)
- 2026-09-30 20:25 [c_banda_atr_evento] ENTRADA PENGU @ 0.008597 (22.94 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
