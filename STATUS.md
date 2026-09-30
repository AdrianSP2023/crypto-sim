# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 17:16 UTC · vueltas 60 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 914.00 € (-1.11%) | 38 | 12 | 34% | -0.170% | -1.262% | -1.425% | -11.08 € |
| reversion_bb | 923.92 € (-0.04%) | 4 | 0 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 904.12 € (-2.18%) | 54 | 17 | 17% | -0.603% | -1.586% | -1.735% | -19.71 € |
| rebote_extremo | 924.39 € (+0.02%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 911.60 € (-1.37%) | 37 | 10 | 16% | -0.441% | -1.541% | -1.668% | -13.12 € |
| macd_momentum | 912.42 € (-1.28%) | 61 | 5 | 31% | +0.056% | -0.871% | -1.012% | -12.27 € |
| estocastico_rebote | 917.64 € (-0.71%) | 66 | 11 | 52% | +0.318% | -0.559% | -0.720% | -8.59 € |
| ruptura_estricta | 901.23 € (-2.49%) | 40 | 4 | 10% | -1.291% | -2.391% | -2.538% | -22.08 € |
| macd_sin_salida | 909.30 € (-1.62%) | 54 | 9 | 35% | -0.190% | -1.174% | -1.318% | -14.65 € |
| c_banda_atr_tope | 923.86 € (-0.04%) | 9 | 5 | 56% | +0.446% | -0.654% | -0.837% | -1.36 € |
| ruptura_volumen_tope | 920.60 € (-0.39%) | 11 | 5 | 27% | -0.187% | -1.287% | -1.378% | -3.27 € |
| c_banda_atr_regimen | 912.83 € (-1.23%) | 36 | 8 | 31% | -0.290% | -1.390% | -1.546% | -11.56 € |
| macd_momentum_regimen | 912.71 € (-1.25%) | 53 | 4 | 30% | +0.026% | -0.966% | -1.106% | -11.83 € |
| ruptura_volumen_regimen | 903.97 € (-2.19%) | 55 | 16 | 16% | -0.613% | -1.588% | -1.737% | -20.10 € |
| c_banda_atr_evento | 925.31 € (+0.12%) | 4 | 14 | 75% | +1.125% | +0.025% | -0.192% | +0.02 € |
| macd_momentum_evento | 921.63 € (-0.28%) | 14 | 5 | 36% | +0.151% | -0.949% | -1.097% | -3.07 € |
| ruptura_volumen_evento | 922.54 € (-0.18%) | 4 | 17 | 25% | -0.300% | -1.400% | -1.537% | -1.29 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 17:10 | macd_momentum_evento | ENA | momentum perdido | +0.29% | -0.81% | -0.19 |
| 2026-09-30 17:10 | macd_momentum_regimen | ENA | momentum perdido | +0.29% | -0.21% | -0.05 |
| 2026-09-30 17:10 | estocastico_rebote | APT | take-profit | +1.85% | +1.05% | +0.24 |
| 2026-09-30 17:10 | macd_momentum | ENA | momentum perdido | +0.29% | -0.21% | -0.05 |
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

## Eventos de la última vuelta

- 2026-09-30 17:10 [pullback_tendencia] ENTRADA NEAR @ 4.7556 (22.78 €, apertura)
- 2026-09-30 17:10 [pullback_tendencia] ENTRADA ICP @ 3.08 (22.78 €, apertura)
- 2026-09-30 17:10 [ruptura_volumen] ENTRADA JUP @ 0.29425 (22.61 €, apertura)
- 2026-09-30 17:10 [ruptura_volumen_regimen] ENTRADA JUP @ 0.29425 (22.60 €, apertura)
- 2026-09-30 17:10 [ruptura_volumen_evento] ENTRADA JUP @ 0.29425 (23.07 €, apertura)
- 2026-09-30 17:10 [pullback_tendencia] ENTRADA SPX @ 0.394 (22.78 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
