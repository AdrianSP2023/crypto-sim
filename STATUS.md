# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 16:31 UTC · vueltas 51 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 915.82 € (-0.91%) | 32 | 11 | 38% | -0.172% | -1.272% | -1.442% | -9.41 € |
| reversion_bb | 923.92 € (-0.04%) | 4 | 0 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 905.17 € (-2.06%) | 51 | 5 | 16% | -0.638% | -1.650% | -1.798% | -19.38 € |
| rebote_extremo | 924.38 € (+0.01%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 912.50 € (-1.27%) | 33 | 2 | 18% | -0.461% | -1.561% | -1.697% | -11.86 € |
| macd_momentum | 912.64 € (-1.25%) | 57 | 6 | 33% | +0.094% | -0.863% | -1.008% | -11.37 € |
| estocastico_rebote | 918.38 € (-0.63%) | 59 | 16 | 49% | +0.217% | -0.670% | -0.837% | -9.18 € |
| ruptura_estricta | 902.33 € (-2.37%) | 39 | 3 | 10% | -1.273% | -2.373% | -2.522% | -21.38 € |
| macd_sin_salida | 909.26 € (-1.62%) | 54 | 7 | 35% | -0.190% | -1.174% | -1.318% | -14.65 € |
| c_banda_atr_tope | 923.64 € (-0.07%) | 9 | 5 | 56% | +0.446% | -0.654% | -0.837% | -1.36 € |
| ruptura_volumen_tope | 921.50 € (-0.30%) | 9 | 5 | 22% | -0.373% | -1.473% | -1.564% | -3.06 € |
| c_banda_atr_regimen | 914.76 € (-1.03%) | 30 | 7 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| macd_momentum_regimen | 912.56 € (-1.26%) | 51 | 3 | 31% | +0.041% | -0.971% | -1.110% | -11.44 € |
| ruptura_volumen_regimen | 904.90 € (-2.09%) | 52 | 4 | 15% | -0.649% | -1.651% | -1.798% | -19.76 € |
| c_banda_atr_evento | 925.98 € (+0.19%) | 2 | 9 | 100% | +2.000% | +0.900% | +0.614% | +0.42 € |
| macd_momentum_evento | 922.40 € (-0.20%) | 10 | 6 | 50% | +0.405% | -0.695% | -0.868% | -1.61 € |
| ruptura_volumen_evento | 924.03 € (-0.02%) | 1 | 5 | 0% | -1.200% | -2.300% | -2.340% | -0.53 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 16:30 | macd_momentum_evento | NEAR | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:30 | macd_momentum_regimen | NEAR | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 16:30 | macd_sin_salida | NEAR | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 16:30 | ruptura_estricta | XMR | timeout | -0.17% | -1.27% | -0.29 |
| 2026-09-30 16:30 | macd_momentum | NEAR | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 16:30 | reversion_bb | CRV | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-09-30 16:25 | estocastico_rebote | NIGHT | take-profit | +1.80% | +1.30% | +0.30 |
| 2026-09-30 16:20 | macd_sin_salida | TRX | timeout | -0.43% | -1.24% | -0.29 |
| 2026-09-30 16:15 | ruptura_volumen_evento | MON | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 16:15 | ruptura_volumen_regimen | MON | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 16:15 | estocastico_rebote | ENA | take-profit | +1.80% | +1.30% | +0.30 |
| 2026-09-30 16:15 | ruptura_volumen | MON | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 16:10 | macd_momentum_evento | SPX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:10 | macd_momentum_evento | MON | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:10 | c_banda_atr_evento | SPX | take-profit | +2.00% | +0.90% | +0.21 |

## Eventos de la última vuelta

- 2026-09-30 16:25 [pullback_tendencia] ENTRADA QNT @ 264.92 (22.81 €, apertura)
- 2026-09-30 16:30 [macd_momentum] CIERRE NEAR take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:30 [macd_sin_salida] CIERRE NEAR take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:30 [macd_momentum_regimen] CIERRE NEAR take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:30 [macd_momentum_evento] CIERRE NEAR take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:30 [reversion_bb] CIERRE CRV take-profit bruto +1.50% neto +0.40%
- 2026-09-30 16:30 [ruptura_estricta] CIERRE XMR timeout bruto -0.17% neto -1.27%
- 2026-09-30 16:25 [ruptura_estricta] ENTRADA SPX @ 0.3987 (22.57 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
