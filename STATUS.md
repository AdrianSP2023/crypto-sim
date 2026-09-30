# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 15:06 UTC · vueltas 34 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 913.95 € (-1.11%) | 30 | 7 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| reversion_bb | 923.78 € (-0.05%) | 2 | 2 | 50% | +0.000% | -1.100% | -1.219% | -0.51 € |
| ruptura_volumen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| rebote_extremo | 924.22 € (-0.00%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 913.00 € (-1.22%) | 31 | 0 | 19% | -0.474% | -1.574% | -1.716% | -11.25 € |
| macd_momentum | 912.12 € (-1.31%) | 49 | 1 | 29% | -0.039% | -1.072% | -1.211% | -12.12 € |
| estocastico_rebote | 917.13 € (-0.77%) | 28 | 39 | 32% | -0.427% | -1.516% | -1.694% | -9.79 € |
| ruptura_estricta | 904.42 € (-2.14%) | 32 | 7 | 12% | -1.372% | -2.472% | -2.634% | -18.27 € |
| macd_sin_salida | 909.52 € (-1.59%) | 42 | 7 | 33% | -0.343% | -1.422% | -1.569% | -13.79 € |
| c_banda_atr_tope | 922.84 € (-0.15%) | 8 | 3 | 50% | +0.252% | -0.849% | -1.012% | -1.57 € |
| ruptura_volumen_tope | 921.18 € (-0.33%) | 9 | 0 | 22% | -0.373% | -1.473% | -1.564% | -3.06 € |
| c_banda_atr_regimen | 913.79 € (-1.13%) | 30 | 4 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| macd_momentum_regimen | 912.12 € (-1.31%) | 49 | 0 | 29% | -0.039% | -1.072% | -1.211% | -12.12 € |
| ruptura_volumen_regimen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| c_banda_atr_evento | 924.41 € (+0.02%) | 0 | 3 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 922.98 € (-0.14%) | 2 | 1 | 0% | -1.623% | -2.723% | -2.894% | -1.26 € |
| ruptura_volumen_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 15:05 | estocastico_rebote | QNT | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-30 14:55 | macd_momentum_evento | NIGHT | stop-loss | -1.75% | -2.85% | -0.66 |
| 2026-09-30 14:55 | macd_momentum_regimen | NIGHT | stop-loss | -1.75% | -2.25% | -0.51 |
| 2026-09-30 14:55 | macd_sin_salida | NIGHT | stop-loss | -1.75% | -2.55% | -0.58 |
| 2026-09-30 14:55 | macd_momentum | NIGHT | stop-loss | -1.75% | -2.25% | -0.51 |
| 2026-09-30 14:55 | pullback_tendencia | NIGHT | stop-loss | -1.75% | -2.85% | -0.65 |
| 2026-09-30 14:45 | estocastico_rebote | ZRO | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-30 14:40 | ruptura_volumen_regimen | MON | stop-loss | -1.20% | -2.00% | -0.46 |
| 2026-09-30 14:40 | ruptura_volumen | MON | stop-loss | -1.20% | -2.00% | -0.46 |
| 2026-09-30 14:35 | ruptura_volumen_regimen | XMR | stop-loss | -1.20% | -2.00% | -0.46 |
| 2026-09-30 14:35 | ruptura_volumen_regimen | TRUMP | stop-loss | -1.20% | -2.00% | -0.46 |
| 2026-09-30 14:35 | ruptura_volumen_regimen | BTC | timeout | -1.03% | -1.83% | -0.42 |
| 2026-09-30 14:35 | ruptura_volumen_tope | BTC | timeout | -1.03% | -2.13% | -0.49 |
| 2026-09-30 14:35 | macd_sin_salida | TRUMP | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 14:35 | ruptura_estricta | LTC | stop-loss | -2.00% | -3.10% | -0.72 |

## Eventos de la última vuelta

- 2026-09-30 15:05 [estocastico_rebote] CIERRE QNT take-profit bruto +1.80% neto +1.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
