# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 17:11 UTC · vueltas 59 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 914.13 € (-1.09%) | 38 | 12 | 34% | -0.170% | -1.262% | -1.425% | -11.08 € |
| reversion_bb | 923.92 € (-0.04%) | 4 | 0 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 904.57 € (-2.13%) | 54 | 16 | 17% | -0.603% | -1.586% | -1.735% | -19.71 € |
| rebote_extremo | 924.40 € (+0.02%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 912.14 € (-1.31%) | 37 | 7 | 16% | -0.441% | -1.541% | -1.668% | -13.12 € |
| macd_momentum | 912.55 € (-1.27%) | 61 | 5 | 31% | +0.056% | -0.871% | -1.012% | -12.27 € |
| estocastico_rebote | 917.81 € (-0.70%) | 66 | 11 | 52% | +0.318% | -0.559% | -0.720% | -8.59 € |
| ruptura_estricta | 901.29 € (-2.48%) | 40 | 4 | 10% | -1.291% | -2.391% | -2.538% | -22.08 € |
| macd_sin_salida | 909.58 € (-1.59%) | 54 | 9 | 35% | -0.190% | -1.174% | -1.318% | -14.65 € |
| c_banda_atr_tope | 923.90 € (-0.04%) | 9 | 5 | 56% | +0.446% | -0.654% | -0.837% | -1.36 € |
| ruptura_volumen_tope | 920.70 € (-0.38%) | 11 | 5 | 27% | -0.187% | -1.287% | -1.378% | -3.27 € |
| c_banda_atr_regimen | 912.92 € (-1.22%) | 36 | 8 | 31% | -0.290% | -1.390% | -1.546% | -11.56 € |
| macd_momentum_regimen | 912.84 € (-1.23%) | 53 | 4 | 30% | +0.026% | -0.966% | -1.106% | -11.83 € |
| ruptura_volumen_regimen | 904.43 € (-2.14%) | 55 | 15 | 16% | -0.613% | -1.588% | -1.737% | -20.10 € |
| c_banda_atr_evento | 925.48 € (+0.13%) | 4 | 14 | 75% | +1.125% | +0.025% | -0.192% | +0.02 € |
| macd_momentum_evento | 921.75 € (-0.27%) | 14 | 5 | 36% | +0.151% | -0.949% | -1.097% | -3.07 € |
| ruptura_volumen_evento | 923.00 € (-0.13%) | 4 | 16 | 25% | -0.300% | -1.400% | -1.537% | -1.29 € |
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

- 2026-09-30 17:05 [macd_momentum] ENTRADA QNT @ 268.39 (22.80 €, apertura)
- 2026-09-30 17:05 [macd_sin_salida] ENTRADA QNT @ 268.39 (22.74 €, apertura)
- 2026-09-30 17:05 [macd_momentum_regimen] ENTRADA QNT @ 268.39 (22.81 €, apertura)
- 2026-09-30 17:05 [macd_momentum_evento] ENTRADA QNT @ 268.39 (23.03 €, apertura)
- 2026-09-30 17:05 [ruptura_volumen] ENTRADA HYPE @ 79.77 (22.61 €, apertura)
- 2026-09-30 17:05 [ruptura_volumen_regimen] ENTRADA HYPE @ 79.77 (22.60 €, apertura)
- 2026-09-30 17:05 [ruptura_volumen_evento] ENTRADA HYPE @ 79.77 (23.07 €, apertura)
- 2026-09-30 17:05 [pullback_tendencia] ENTRADA LTC @ 59.31 (22.78 €, apertura)
- 2026-09-30 17:10 [macd_momentum] CIERRE ENA momentum perdido bruto +0.29% neto -0.21%
- 2026-09-30 17:10 [macd_momentum_regimen] CIERRE ENA momentum perdido bruto +0.29% neto -0.21%
- 2026-09-30 17:10 [macd_momentum_evento] CIERRE ENA momentum perdido bruto +0.29% neto -0.81%
- 2026-09-30 17:05 [pullback_tendencia] ENTRADA USELESS @ 0.2187 (22.78 €, apertura)
- 2026-09-30 17:05 [pullback_tendencia] ENTRADA KSM @ 4.61 (22.78 €, apertura)
- 2026-09-30 17:10 [estocastico_rebote] CIERRE APT take-profit bruto +1.85% neto +1.05%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
