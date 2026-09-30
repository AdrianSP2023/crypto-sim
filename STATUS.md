# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 17:46 UTC · vueltas 66 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.46 € (-1.49%) | 41 | 10 | 32% | -0.270% | -1.340% | -1.501% | -12.68 € |
| reversion_bb | 923.82 € (-0.05%) | 4 | 3 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 898.98 € (-2.73%) | 67 | 5 | 13% | -0.709% | -1.598% | -1.738% | -24.57 € |
| rebote_extremo | 923.90 € (-0.04%) | 2 | 0 | 50% | +0.370% | -0.731% | -0.816% | -0.34 € |
| pullback_tendencia | 907.80 € (-1.78%) | 48 | 4 | 15% | -0.448% | -1.485% | -1.610% | -16.37 € |
| macd_momentum | 911.28 € (-1.40%) | 66 | 1 | 32% | +0.045% | -0.851% | -0.999% | -12.95 € |
| estocastico_rebote | 914.40 € (-1.06%) | 74 | 12 | 47% | +0.293% | -0.560% | -0.707% | -9.62 € |
| ruptura_estricta | 900.15 € (-2.61%) | 42 | 3 | 10% | -1.325% | -2.425% | -2.569% | -23.48 € |
| macd_sin_salida | 907.08 € (-1.86%) | 60 | 4 | 33% | -0.264% | -1.199% | -1.345% | -16.61 € |
| c_banda_atr_tope | 922.26 € (-0.21%) | 10 | 5 | 50% | +0.251% | -0.849% | -1.020% | -1.96 € |
| ruptura_volumen_tope | 918.51 € (-0.62%) | 16 | 0 | 19% | -0.453% | -1.553% | -1.655% | -5.74 € |
| c_banda_atr_regimen | 910.39 € (-1.50%) | 38 | 7 | 29% | -0.357% | -1.457% | -1.613% | -12.78 € |
| macd_momentum_regimen | 911.82 € (-1.34%) | 57 | 1 | 32% | +0.014% | -0.944% | -1.091% | -12.41 € |
| ruptura_volumen_regimen | 898.80 € (-2.75%) | 67 | 5 | 13% | -0.721% | -1.610% | -1.751% | -24.75 € |
| c_banda_atr_evento | 920.74 € (-0.38%) | 8 | 11 | 38% | -0.201% | -1.301% | -1.463% | -2.41 € |
| macd_momentum_evento | 919.78 € (-0.48%) | 19 | 1 | 32% | +0.085% | -1.015% | -1.188% | -4.45 € |
| ruptura_volumen_evento | 915.49 € (-0.95%) | 17 | 5 | 6% | -0.950% | -2.050% | -2.160% | -8.05 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 17:45 | ruptura_volumen_evento | AAVE | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:45 | macd_momentum_evento | TON | momentum perdido | +0.07% | -1.02% | -0.24 |
| 2026-09-30 17:45 | macd_momentum_evento | NIGHT | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 17:45 | c_banda_atr_evento | INJ | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 17:45 | ruptura_volumen_regimen | AAVE | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 17:45 | macd_momentum_regimen | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 17:45 | c_banda_atr_regimen | INJ | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-30 17:45 | ruptura_volumen_tope | XMR | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 17:45 | macd_sin_salida | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 17:45 | estocastico_rebote | AAVE | timeout | +0.57% | +0.07% | +0.02 |
| 2026-09-30 17:45 | estocastico_rebote | ETH | timeout | +0.38% | -0.12% | -0.03 |
| 2026-09-30 17:45 | macd_momentum | TON | momentum perdido | +0.07% | -0.42% | -0.10 |
| 2026-09-30 17:45 | macd_momentum | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 17:45 | ruptura_volumen | AAVE | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 17:45 | c_banda_atr | INJ | stop-loss | -1.50% | -2.30% | -0.53 |

## Eventos de la última vuelta

- 2026-09-30 17:45 [estocastico_rebote] CIERRE ETH timeout bruto +0.38% neto -0.12%
- 2026-09-30 17:45 [ruptura_volumen] CIERRE AAVE stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:45 [estocastico_rebote] CIERRE AAVE timeout bruto +0.57% neto +0.07%
- 2026-09-30 17:45 [ruptura_volumen_regimen] CIERRE AAVE stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:45 [ruptura_volumen_evento] CIERRE AAVE stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:40 [estocastico_rebote] ENTRADA ICP @ 3.015 (22.87 €, apertura)
- 2026-09-30 17:45 [macd_momentum] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 17:45 [macd_sin_salida] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 17:45 [macd_momentum_regimen] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 17:45 [macd_momentum_evento] CIERRE NIGHT take-profit bruto +2.00% neto +0.90%
- 2026-09-30 17:45 [c_banda_atr] CIERRE INJ stop-loss bruto -1.50% neto -2.30%
- 2026-09-30 17:45 [c_banda_atr_regimen] CIERRE INJ stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:45 [c_banda_atr_evento] CIERRE INJ stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:40 [reversion_bb] ENTRADA WLFI @ 0.0492 (23.10 €, apertura)
- 2026-09-30 17:40 [estocastico_rebote] ENTRADA DASH @ 53.969 (22.87 €, apertura)
- 2026-09-30 17:45 [macd_momentum] CIERRE TON momentum perdido bruto +0.08% neto -0.42%
- 2026-09-30 17:45 [macd_momentum_evento] CIERRE TON momentum perdido bruto +0.08% neto -1.02%
- 2026-09-30 17:45 [ruptura_volumen_tope] CIERRE XMR stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:40 [estocastico_rebote] ENTRADA SPX @ 0.3868 (22.87 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
