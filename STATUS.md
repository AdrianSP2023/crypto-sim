# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 17:06 UTC · vueltas 58 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 913.97 € (-1.11%) | 38 | 12 | 34% | -0.170% | -1.262% | -1.425% | -11.08 € |
| reversion_bb | 923.92 € (-0.04%) | 4 | 0 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 904.22 € (-2.17%) | 54 | 15 | 17% | -0.603% | -1.586% | -1.735% | -19.71 € |
| rebote_extremo | 924.40 € (+0.02%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 911.65 € (-1.36%) | 37 | 4 | 16% | -0.441% | -1.541% | -1.668% | -13.12 € |
| macd_momentum | 912.43 € (-1.28%) | 60 | 5 | 32% | +0.052% | -0.883% | -1.024% | -12.22 € |
| estocastico_rebote | 917.73 € (-0.70%) | 65 | 12 | 51% | +0.295% | -0.584% | -0.745% | -8.83 € |
| ruptura_estricta | 901.17 € (-2.50%) | 40 | 4 | 10% | -1.291% | -2.391% | -2.538% | -22.08 € |
| macd_sin_salida | 909.31 € (-1.62%) | 54 | 8 | 35% | -0.190% | -1.174% | -1.318% | -14.65 € |
| c_banda_atr_tope | 923.74 € (-0.05%) | 9 | 5 | 56% | +0.446% | -0.654% | -0.837% | -1.36 € |
| ruptura_volumen_tope | 920.69 € (-0.38%) | 11 | 5 | 27% | -0.187% | -1.287% | -1.378% | -3.27 € |
| c_banda_atr_regimen | 912.92 € (-1.23%) | 36 | 8 | 31% | -0.290% | -1.390% | -1.546% | -11.56 € |
| macd_momentum_regimen | 912.71 € (-1.25%) | 52 | 4 | 31% | +0.021% | -0.981% | -1.122% | -11.78 € |
| ruptura_volumen_regimen | 904.08 € (-2.18%) | 55 | 14 | 16% | -0.613% | -1.588% | -1.737% | -20.10 € |
| c_banda_atr_evento | 925.34 € (+0.12%) | 4 | 14 | 75% | +1.125% | +0.025% | -0.192% | +0.02 € |
| macd_momentum_evento | 921.77 € (-0.27%) | 13 | 5 | 38% | +0.140% | -0.960% | -1.113% | -2.88 € |
| ruptura_volumen_evento | 922.64 € (-0.17%) | 4 | 15 | 25% | -0.300% | -1.400% | -1.537% | -1.29 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 17:05 | ruptura_volumen_evento | KSM | stop-loss | -1.30% | -2.40% | -0.55 |
| 2026-09-30 17:05 | ruptura_volumen_evento | NEAR | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:05 | c_banda_atr_evento | USELESS | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 17:05 | ruptura_volumen_regimen | KSM | stop-loss | -1.30% | -1.80% | -0.41 |
| 2026-09-30 17:05 | ruptura_volumen_regimen | NEAR | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 17:05 | c_banda_atr_regimen | USELESS | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-30 17:05 | ruptura_volumen_tope | NEAR | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:05 | pullback_tendencia | HBAR | rotura de tendencia | -0.69% | -1.79% | -0.41 |
| 2026-09-30 17:05 | ruptura_volumen | KSM | stop-loss | -1.30% | -1.80% | -0.41 |
| 2026-09-30 17:05 | ruptura_volumen | NEAR | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 17:05 | c_banda_atr | USELESS | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 16:55 | estocastico_rebote | BNB | timeout | +0.17% | -0.63% | -0.14 |
| 2026-09-30 16:55 | estocastico_rebote | ASTER | timeout | -1.05% | -1.85% | -0.43 |
| 2026-09-30 16:55 | pullback_tendencia | XDC | rotura de tendencia | -0.36% | -1.46% | -0.33 |
| 2026-09-30 16:50 | c_banda_atr_evento | ONDO | take-profit | +2.00% | +0.90% | +0.21 |

## Eventos de la última vuelta

- 2026-09-30 17:05 [ruptura_volumen] CIERRE NEAR stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:05 [ruptura_volumen_tope] CIERRE NEAR stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:05 [ruptura_volumen_regimen] CIERRE NEAR stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:05 [ruptura_volumen_evento] CIERRE NEAR stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:05 [pullback_tendencia] CIERRE HBAR rotura de tendencia bruto -0.69% neto -1.79%
- 2026-09-30 17:00 [estocastico_rebote] ENTRADA TRX @ 0.297989 (22.89 €, apertura)
- 2026-09-30 17:05 [c_banda_atr] CIERRE USELESS stop-loss bruto -1.50% neto -2.30%
- 2026-09-30 17:05 [c_banda_atr_regimen] CIERRE USELESS stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:05 [c_banda_atr_evento] CIERRE USELESS stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:05 [ruptura_volumen] CIERRE KSM stop-loss bruto -1.30% neto -1.80%
- 2026-09-30 17:05 [ruptura_volumen_regimen] CIERRE KSM stop-loss bruto -1.30% neto -1.80%
- 2026-09-30 17:05 [ruptura_volumen_evento] CIERRE KSM stop-loss bruto -1.30% neto -2.40%
- 2026-09-30 17:00 [ruptura_volumen_tope] ENTRADA XMR @ 483.32 (23.02 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
