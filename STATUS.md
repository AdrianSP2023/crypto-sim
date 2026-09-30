# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 20:41 UTC · vueltas 73 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.92 € (-1.77%) | 51 | 28 | 25% | -0.442% | -1.447% | -1.599% | -16.99 € |
| reversion_bb | 922.54 € (-0.18%) | 7 | 5 | 57% | +0.214% | -0.886% | -1.014% | -1.44 € |
| ruptura_volumen | 898.44 € (-2.79%) | 74 | 14 | 14% | -0.665% | -1.518% | -1.656% | -25.76 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 905.95 € (-1.98%) | 59 | 3 | 15% | -0.431% | -1.378% | -1.517% | -18.66 € |
| macd_momentum | 908.39 € (-1.71%) | 79 | 13 | 27% | -0.026% | -0.856% | -0.992% | -15.57 € |
| estocastico_rebote | 906.19 € (-1.95%) | 101 | 22 | 38% | -0.043% | -0.802% | -0.935% | -18.66 € |
| ruptura_estricta | 899.24 € (-2.71%) | 46 | 5 | 11% | -1.277% | -2.350% | -2.498% | -24.89 € |
| macd_sin_salida | 905.80 € (-2.00%) | 67 | 14 | 33% | -0.287% | -1.177% | -1.316% | -18.17 € |
| c_banda_atr_tope | 921.19 € (-0.33%) | 14 | 5 | 36% | +0.100% | -1.000% | -1.153% | -3.23 € |
| ruptura_volumen_tope | 918.73 € (-0.60%) | 18 | 5 | 22% | -0.331% | -1.431% | -1.522% | -5.94 € |
| c_banda_atr_regimen | 908.81 € (-1.67%) | 43 | 2 | 26% | -0.480% | -1.573% | -1.728% | -15.58 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 917.23 € (-0.76%) | 19 | 27 | 16% | -0.679% | -1.779% | -1.917% | -7.80 € |
| macd_momentum_evento | 915.08 € (-0.99%) | 32 | 13 | 19% | -0.106% | -1.206% | -1.338% | -8.88 € |
| ruptura_volumen_evento | 913.97 € (-1.11%) | 24 | 14 | 8% | -0.746% | -1.846% | -1.960% | -10.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 20:40 | pullback_tendencia | XDC | rotura de tendencia | +0.10% | -0.40% | -0.09 |
| 2026-09-30 20:35 | c_banda_atr_evento | USELESS | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 20:35 | c_banda_atr_evento | ICP | stop-loss | -1.59% | -2.69% | -0.62 |
| 2026-09-30 20:35 | macd_sin_salida | XDC | timeout | +0.30% | -0.20% | -0.05 |
| 2026-09-30 20:35 | estocastico_rebote | TRUMP | timeout | -0.06% | -0.56% | -0.13 |
| 2026-09-30 20:35 | estocastico_rebote | ICP | stop-loss | -1.66% | -2.16% | -0.49 |
| 2026-09-30 20:35 | c_banda_atr | USELESS | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 20:35 | c_banda_atr | ICP | stop-loss | -1.59% | -2.09% | -0.47 |
| 2026-09-30 20:25 | estocastico_rebote | ASTER | timeout | +0.17% | -0.33% | -0.08 |
| 2026-09-30 20:25 | estocastico_rebote | FET | take-profit | +1.99% | +1.49% | +0.34 |
| 2026-09-30 20:25 | pullback_tendencia | FET | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 20:20 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 20:20 | ruptura_estricta | MON | timeout | +1.86% | +1.06% | +0.24 |
| 2026-09-30 20:20 | estocastico_rebote | XDC | timeout | +0.53% | +0.03% | +0.01 |
| 2026-09-30 20:10 | rebote_extremo | ONDO | take-profit | +2.00% | +0.90% | +0.21 |

## Eventos de la última vuelta

- 2026-09-30 20:35 [pullback_tendencia] ENTRADA XDC @ 0.0302 (22.64 €, apertura)
- 2026-09-30 20:40 [pullback_tendencia] CIERRE XDC rotura de tendencia bruto +0.10% neto -0.40%
- 2026-09-30 20:35 [macd_momentum] ENTRADA TON @ 1.349 (22.72 €, apertura)
- 2026-09-30 20:35 [macd_momentum_evento] ENTRADA TON @ 1.349 (22.88 €, apertura)
- 2026-09-30 20:35 [c_banda_atr] ENTRADA SEI @ 0.06466 (22.68 €, apertura)
- 2026-09-30 20:35 [c_banda_atr_evento] ENTRADA SEI @ 0.06466 (22.91 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
