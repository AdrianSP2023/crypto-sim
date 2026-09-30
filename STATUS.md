# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 21:11 UTC · vueltas 79 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.30 € (-1.94%) | 53 | 29 | 25% | -0.447% | -1.439% | -1.592% | -17.55 € |
| reversion_bb | 922.29 € (-0.21%) | 8 | 4 | 50% | +0.000% | -1.100% | -1.225% | -2.04 € |
| ruptura_volumen | 898.08 € (-2.83%) | 76 | 15 | 14% | -0.644% | -1.487% | -1.626% | -25.92 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 905.66 € (-2.01%) | 60 | 5 | 15% | -0.430% | -1.370% | -1.511% | -18.85 € |
| macd_momentum | 906.92 € (-1.87%) | 86 | 9 | 24% | -0.073% | -0.877% | -1.011% | -17.33 € |
| estocastico_rebote | 904.82 € (-2.10%) | 113 | 11 | 36% | -0.013% | -0.744% | -0.875% | -19.37 € |
| ruptura_estricta | 899.21 € (-2.71%) | 46 | 5 | 11% | -1.277% | -2.350% | -2.498% | -24.89 € |
| macd_sin_salida | 904.88 € (-2.09%) | 70 | 14 | 33% | -0.296% | -1.169% | -1.305% | -18.84 € |
| c_banda_atr_tope | 921.19 € (-0.33%) | 14 | 5 | 36% | +0.100% | -1.000% | -1.153% | -3.23 € |
| ruptura_volumen_tope | 917.93 € (-0.68%) | 20 | 5 | 20% | -0.282% | -1.382% | -1.478% | -6.38 € |
| c_banda_atr_regimen | 908.70 € (-1.68%) | 44 | 1 | 25% | -0.461% | -1.547% | -1.705% | -15.68 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 915.40 € (-0.96%) | 21 | 28 | 14% | -0.670% | -1.770% | -1.913% | -8.58 € |
| macd_momentum_evento | 912.63 € (-1.26%) | 39 | 9 | 15% | -0.196% | -1.296% | -1.425% | -11.61 € |
| ruptura_volumen_evento | 913.33 € (-1.18%) | 26 | 15 | 8% | -0.677% | -1.777% | -1.893% | -10.66 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 21:10 | estocastico_rebote | NIGHT | take-profit | +2.03% | +1.53% | +0.35 |
| 2026-09-30 21:05 | ruptura_volumen_evento | HBAR | timeout | +0.89% | -0.21% | -0.05 |
| 2026-09-30 21:05 | ruptura_volumen_tope | HBAR | timeout | +0.89% | -0.21% | -0.05 |
| 2026-09-30 21:05 | estocastico_rebote | KSM | timeout | +1.78% | +1.28% | +0.29 |
| 2026-09-30 21:05 | ruptura_volumen | HBAR | timeout | +0.89% | +0.39% | +0.09 |
| 2026-09-30 21:00 | c_banda_atr_evento | ENA | stop-loss | -1.54% | -2.64% | -0.61 |
| 2026-09-30 21:00 | macd_sin_salida | ENA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 21:00 | estocastico_rebote | XMR | timeout | -0.59% | -1.09% | -0.25 |
| 2026-09-30 21:00 | estocastico_rebote | VVV | timeout | -0.32% | -0.82% | -0.19 |
| 2026-09-30 21:00 | pullback_tendencia | TON | rotura de tendencia | -0.37% | -0.87% | -0.20 |
| 2026-09-30 21:00 | c_banda_atr | ENA | stop-loss | -1.54% | -2.04% | -0.46 |
| 2026-09-30 20:55 | ruptura_volumen_evento | TON | timeout | -0.59% | -1.69% | -0.39 |
| 2026-09-30 20:55 | macd_momentum_evento | TON | momentum perdido | -0.45% | -1.54% | -0.35 |
| 2026-09-30 20:55 | macd_momentum_evento | ALGO | momentum perdido | -0.90% | -2.00% | -0.46 |
| 2026-09-30 20:55 | macd_momentum_evento | XLM | momentum perdido | +0.21% | -0.89% | -0.20 |

## Eventos de la última vuelta

- 2026-09-30 21:05 [ruptura_volumen] ENTRADA ETH @ 2366.03 (22.46 €, apertura)
- 2026-09-30 21:05 [ruptura_volumen_tope] ENTRADA ETH @ 2366.03 (22.95 €, apertura)
- 2026-09-30 21:05 [ruptura_volumen_evento] ENTRADA ETH @ 2366.03 (22.84 €, apertura)
- 2026-09-30 21:05 [c_banda_atr] ENTRADA NEAR @ 4.7522 (22.67 €, apertura)
- 2026-09-30 21:05 [macd_momentum] ENTRADA NEAR @ 4.7522 (22.67 €, apertura)
- 2026-09-30 21:05 [macd_sin_salida] ENTRADA NEAR @ 4.7522 (22.64 €, apertura)
- 2026-09-30 21:05 [c_banda_atr_evento] ENTRADA NEAR @ 4.7522 (22.89 €, apertura)
- 2026-09-30 21:05 [macd_momentum_evento] ENTRADA NEAR @ 4.7522 (22.82 €, apertura)
- 2026-09-30 21:05 [c_banda_atr] ENTRADA LINK @ 12.66 (22.67 €, apertura)
- 2026-09-30 21:05 [c_banda_atr_evento] ENTRADA LINK @ 12.66 (22.89 €, apertura)
- 2026-09-30 21:05 [macd_momentum] ENTRADA WLD @ 0.4724 (22.67 €, apertura)
- 2026-09-30 21:05 [macd_sin_salida] ENTRADA WLD @ 0.4724 (22.64 €, apertura)
- 2026-09-30 21:05 [macd_momentum_evento] ENTRADA WLD @ 0.4724 (22.82 €, apertura)
- 2026-09-30 21:05 [estocastico_rebote] ENTRADA XDC @ 0.03046 (22.61 €, apertura)
- 2026-09-30 21:10 [estocastico_rebote] CIERRE NIGHT take-profit bruto +2.03% neto +1.53%
- 2026-09-30 21:05 [ruptura_volumen_tope] ENTRADA ASTER @ 0.6752 (22.95 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
