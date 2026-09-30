# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 21:21 UTC · vueltas 81 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 905.47 € (-2.03%) | 53 | 29 | 25% | -0.447% | -1.439% | -1.592% | -17.55 € |
| reversion_bb | 922.26 € (-0.21%) | 8 | 4 | 50% | +0.000% | -1.100% | -1.225% | -2.04 € |
| ruptura_volumen | 897.49 € (-2.89%) | 77 | 14 | 14% | -0.652% | -1.491% | -1.629% | -26.32 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 905.31 € (-2.05%) | 61 | 4 | 15% | -0.429% | -1.362% | -1.501% | -19.05 € |
| macd_momentum | 906.53 € (-1.92%) | 89 | 8 | 25% | -0.062% | -0.855% | -0.988% | -17.49 € |
| estocastico_rebote | 904.56 € (-2.13%) | 114 | 10 | 36% | -0.010% | -0.739% | -0.870% | -19.40 € |
| ruptura_estricta | 898.93 € (-2.74%) | 46 | 5 | 11% | -1.277% | -2.350% | -2.498% | -24.89 € |
| macd_sin_salida | 904.82 € (-2.10%) | 70 | 16 | 33% | -0.296% | -1.169% | -1.305% | -18.84 € |
| c_banda_atr_tope | 920.97 € (-0.35%) | 14 | 5 | 36% | +0.100% | -1.000% | -1.153% | -3.23 € |
| ruptura_volumen_tope | 917.93 € (-0.68%) | 20 | 5 | 20% | -0.282% | -1.382% | -1.478% | -6.38 € |
| c_banda_atr_regimen | 908.60 € (-1.69%) | 44 | 1 | 25% | -0.461% | -1.547% | -1.705% | -15.68 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 914.56 € (-1.05%) | 21 | 28 | 14% | -0.670% | -1.770% | -1.913% | -8.58 € |
| macd_momentum_evento | 912.03 € (-1.32%) | 42 | 8 | 17% | -0.163% | -1.242% | -1.369% | -11.99 € |
| ruptura_volumen_evento | 912.59 € (-1.26%) | 27 | 14 | 7% | -0.700% | -1.800% | -1.915% | -11.21 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 21:20 | ruptura_volumen_evento | FET | stop-loss | -1.29% | -2.40% | -0.55 |
| 2026-09-30 21:20 | macd_momentum_evento | WLD | momentum perdido | -0.19% | -0.99% | -0.23 |
| 2026-09-30 21:20 | macd_momentum_evento | CRV | momentum perdido | +0.90% | +0.10% | +0.02 |
| 2026-09-30 21:20 | macd_momentum_evento | FET | momentum perdido | +0.05% | -0.75% | -0.17 |
| 2026-09-30 21:20 | estocastico_rebote | PUMP | timeout | +0.35% | -0.15% | -0.04 |
| 2026-09-30 21:20 | macd_momentum | WLD | momentum perdido | -0.19% | -0.69% | -0.16 |
| 2026-09-30 21:20 | macd_momentum | CRV | momentum perdido | +0.90% | +0.40% | +0.09 |
| 2026-09-30 21:20 | macd_momentum | FET | momentum perdido | +0.05% | -0.45% | -0.10 |
| 2026-09-30 21:20 | ruptura_volumen | FET | stop-loss | -1.29% | -1.79% | -0.40 |
| 2026-09-30 21:15 | pullback_tendencia | XLM | rotura de tendencia | -0.35% | -0.85% | -0.19 |
| 2026-09-30 21:10 | estocastico_rebote | NIGHT | take-profit | +2.03% | +1.53% | +0.35 |
| 2026-09-30 21:05 | ruptura_volumen_evento | HBAR | timeout | +0.89% | -0.21% | -0.05 |
| 2026-09-30 21:05 | ruptura_volumen_tope | HBAR | timeout | +0.89% | -0.21% | -0.05 |
| 2026-09-30 21:05 | estocastico_rebote | KSM | timeout | +1.78% | +1.28% | +0.29 |
| 2026-09-30 21:05 | ruptura_volumen | HBAR | timeout | +0.89% | +0.39% | +0.09 |

## Eventos de la última vuelta

- 2026-09-30 21:20 [estocastico_rebote] CIERRE PUMP timeout bruto +0.35% neto -0.15%
- 2026-09-30 21:20 [ruptura_volumen] CIERRE FET stop-loss bruto -1.29% neto -1.79%
- 2026-09-30 21:20 [macd_momentum] CIERRE FET momentum perdido bruto +0.05% neto -0.45%
- 2026-09-30 21:20 [macd_momentum_evento] CIERRE FET momentum perdido bruto +0.05% neto -0.75%
- 2026-09-30 21:20 [ruptura_volumen_evento] CIERRE FET stop-loss bruto -1.29% neto -2.39%
- 2026-09-30 21:20 [macd_momentum] CIERRE CRV momentum perdido bruto +0.90% neto +0.40%
- 2026-09-30 21:20 [macd_momentum_evento] CIERRE CRV momentum perdido bruto +0.90% neto +0.10%
- 2026-09-30 21:20 [macd_momentum] CIERRE WLD momentum perdido bruto -0.19% neto -0.69%
- 2026-09-30 21:20 [macd_momentum_evento] CIERRE WLD momentum perdido bruto -0.19% neto -0.99%
- 2026-09-30 21:15 [macd_momentum] ENTRADA MON @ 0.026 (22.67 €, apertura)
- 2026-09-30 21:15 [macd_sin_salida] ENTRADA MON @ 0.026 (22.64 €, apertura)
- 2026-09-30 21:15 [macd_momentum_evento] ENTRADA MON @ 0.026 (22.81 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
