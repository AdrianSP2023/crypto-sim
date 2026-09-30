# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 15:26 UTC · vueltas 38 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 913.55 € (-1.16%) | 30 | 7 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| reversion_bb | 923.58 € (-0.07%) | 2 | 2 | 50% | +0.000% | -1.100% | -1.219% | -0.51 € |
| ruptura_volumen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| rebote_extremo | 924.08 € (-0.02%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 912.74 € (-1.24%) | 32 | 1 | 19% | -0.461% | -1.561% | -1.699% | -11.51 € |
| macd_momentum | 911.32 € (-1.40%) | 50 | 5 | 28% | -0.043% | -1.065% | -1.203% | -12.29 € |
| estocastico_rebote | 911.32 € (-1.40%) | 35 | 33 | 31% | -0.397% | -1.411% | -1.596% | -11.39 € |
| ruptura_estricta | 904.06 € (-2.18%) | 32 | 7 | 12% | -1.372% | -2.472% | -2.634% | -18.27 € |
| macd_sin_salida | 908.61 € (-1.69%) | 42 | 12 | 33% | -0.343% | -1.422% | -1.569% | -13.79 € |
| c_banda_atr_tope | 922.61 € (-0.18%) | 8 | 3 | 50% | +0.252% | -0.849% | -1.012% | -1.57 € |
| ruptura_volumen_tope | 921.18 € (-0.33%) | 9 | 0 | 22% | -0.373% | -1.473% | -1.564% | -3.06 € |
| c_banda_atr_regimen | 913.61 € (-1.15%) | 30 | 4 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| macd_momentum_regimen | 912.12 € (-1.31%) | 49 | 0 | 29% | -0.039% | -1.072% | -1.211% | -12.12 € |
| ruptura_volumen_regimen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| c_banda_atr_evento | 924.18 € (-0.01%) | 0 | 3 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 922.03 € (-0.24%) | 3 | 5 | 0% | -1.160% | -2.260% | -2.405% | -1.57 € |
| ruptura_volumen_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 15:25 | macd_momentum_evento | SPX | momentum perdido | -0.23% | -1.33% | -0.31 |
| 2026-09-30 15:25 | estocastico_rebote | XMR | timeout | -0.57% | -1.37% | -0.32 |
| 2026-09-30 15:25 | macd_momentum | SPX | momentum perdido | -0.23% | -0.73% | -0.17 |
| 2026-09-30 15:25 | pullback_tendencia | HBAR | rotura de tendencia | -0.04% | -1.14% | -0.26 |
| 2026-09-30 15:20 | estocastico_rebote | NIGHT | stop-loss | -1.61% | -2.42% | -0.56 |
| 2026-09-30 15:20 | estocastico_rebote | WLD | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 15:20 | estocastico_rebote | ENA | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 15:20 | estocastico_rebote | HYPE | timeout | -0.55% | -1.35% | -0.31 |
| 2026-09-30 15:15 | estocastico_rebote | TON | take-profit | +1.99% | +1.49% | +0.34 |
| 2026-09-30 15:15 | estocastico_rebote | ICP | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-30 15:05 | estocastico_rebote | QNT | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-30 14:55 | macd_momentum_evento | NIGHT | stop-loss | -1.75% | -2.85% | -0.66 |
| 2026-09-30 14:55 | macd_momentum_regimen | NIGHT | stop-loss | -1.75% | -2.25% | -0.51 |
| 2026-09-30 14:55 | macd_sin_salida | NIGHT | stop-loss | -1.75% | -2.55% | -0.58 |
| 2026-09-30 14:55 | macd_momentum | NIGHT | stop-loss | -1.75% | -2.25% | -0.51 |

## Eventos de la última vuelta

- 2026-09-30 15:20 [pullback_tendencia] ENTRADA HBAR @ 0.09488 (22.82 €, apertura)
- 2026-09-30 15:25 [pullback_tendencia] CIERRE HBAR rotura de tendencia bruto -0.04% neto -1.14%
- 2026-09-30 15:20 [pullback_tendencia] ENTRADA ASTER @ 0.68044 (22.82 €, apertura)
- 2026-09-30 15:25 [estocastico_rebote] CIERRE XMR timeout bruto -0.57% neto -1.37%
- 2026-09-30 15:25 [macd_momentum] CIERRE SPX momentum perdido bruto -0.23% neto -0.73%
- 2026-09-30 15:25 [macd_momentum_evento] CIERRE SPX momentum perdido bruto -0.23% neto -1.33%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
