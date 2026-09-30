# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 17:21 UTC · vueltas 61 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 912.75 € (-1.24%) | 39 | 11 | 33% | -0.204% | -1.288% | -1.449% | -11.61 € |
| reversion_bb | 923.92 € (-0.04%) | 4 | 0 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 902.63 € (-2.34%) | 55 | 16 | 16% | -0.613% | -1.588% | -1.737% | -20.10 € |
| rebote_extremo | 924.33 € (+0.01%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 910.86 € (-1.45%) | 39 | 8 | 18% | -0.376% | -1.476% | -1.603% | -13.25 € |
| macd_momentum | 912.04 € (-1.32%) | 61 | 5 | 31% | +0.056% | -0.871% | -1.012% | -12.27 € |
| estocastico_rebote | 916.98 € (-0.79%) | 66 | 11 | 52% | +0.318% | -0.559% | -0.720% | -8.59 € |
| ruptura_estricta | 900.56 € (-2.56%) | 42 | 2 | 10% | -1.325% | -2.425% | -2.569% | -23.48 € |
| macd_sin_salida | 908.50 € (-1.70%) | 55 | 8 | 35% | -0.214% | -1.189% | -1.331% | -15.11 € |
| c_banda_atr_tope | 923.03 € (-0.13%) | 10 | 4 | 50% | +0.251% | -0.849% | -1.020% | -1.96 € |
| ruptura_volumen_tope | 920.27 € (-0.43%) | 11 | 5 | 27% | -0.187% | -1.287% | -1.378% | -3.27 € |
| c_banda_atr_regimen | 912.33 € (-1.29%) | 36 | 8 | 31% | -0.290% | -1.390% | -1.546% | -11.56 € |
| macd_momentum_regimen | 912.33 € (-1.29%) | 53 | 4 | 30% | +0.026% | -0.966% | -1.106% | -11.83 € |
| ruptura_volumen_regimen | 902.40 € (-2.36%) | 56 | 15 | 16% | -0.624% | -1.590% | -1.739% | -20.49 € |
| c_banda_atr_evento | 923.84 € (-0.04%) | 5 | 13 | 60% | +0.600% | -0.500% | -0.688% | -0.58 € |
| macd_momentum_evento | 921.24 € (-0.32%) | 14 | 5 | 36% | +0.151% | -0.949% | -1.097% | -3.07 € |
| ruptura_volumen_evento | 920.88 € (-0.36%) | 5 | 16 | 20% | -0.480% | -1.580% | -1.719% | -1.82 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 17:20 | ruptura_volumen_evento | ZEC | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:20 | c_banda_atr_evento | ASTER | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 17:20 | ruptura_volumen_regimen | ZEC | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 17:20 | c_banda_atr_tope | ASTER | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 17:20 | macd_sin_salida | ASTER | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 17:20 | ruptura_estricta | SPX | stop-loss | -2.00% | -3.10% | -0.70 |
| 2026-09-30 17:20 | ruptura_estricta | NEAR | stop-loss | -2.00% | -3.10% | -0.70 |
| 2026-09-30 17:20 | pullback_tendencia | MON | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-30 17:20 | pullback_tendencia | LTC | rotura de tendencia | -0.35% | -1.45% | -0.33 |
| 2026-09-30 17:20 | ruptura_volumen | ZEC | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 17:20 | c_banda_atr | ASTER | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 17:10 | macd_momentum_evento | ENA | momentum perdido | +0.29% | -0.81% | -0.19 |
| 2026-09-30 17:10 | macd_momentum_regimen | ENA | momentum perdido | +0.29% | -0.21% | -0.05 |
| 2026-09-30 17:10 | estocastico_rebote | APT | take-profit | +1.85% | +1.05% | +0.24 |
| 2026-09-30 17:10 | macd_momentum | ENA | momentum perdido | +0.29% | -0.21% | -0.05 |

## Eventos de la última vuelta

- 2026-09-30 17:20 [ruptura_estricta] CIERRE NEAR stop-loss bruto -2.00% neto -3.10%
- 2026-09-30 17:20 [ruptura_volumen] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:20 [ruptura_volumen_regimen] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:20 [ruptura_volumen_evento] CIERRE ZEC stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:20 [pullback_tendencia] CIERRE LTC rotura de tendencia bruto -0.35% neto -1.45%
- 2026-09-30 17:20 [pullback_tendencia] CIERRE MON take-profit bruto +2.00% neto +0.90%
- 2026-09-30 17:20 [c_banda_atr] CIERRE ASTER stop-loss bruto -1.50% neto -2.30%
- 2026-09-30 17:20 [macd_sin_salida] CIERRE ASTER stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:20 [c_banda_atr_tope] CIERRE ASTER stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:20 [c_banda_atr_evento] CIERRE ASTER stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:20 [ruptura_estricta] CIERRE SPX stop-loss bruto -2.00% neto -3.10%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
