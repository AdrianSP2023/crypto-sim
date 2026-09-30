# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 18:47 UTC · vueltas 50 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.09 € (-1.64%) | 44 | 9 | 30% | -0.357% | -1.409% | -1.565% | -14.30 € |
| reversion_bb | 922.61 € (-0.18%) | 5 | 4 | 60% | +0.300% | -0.800% | -0.943% | -0.93 € |
| ruptura_volumen | 898.79 € (-2.75%) | 72 | 2 | 14% | -0.670% | -1.532% | -1.672% | -25.31 € |
| rebote_extremo | 924.05 € (-0.02%) | 2 | 1 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 906.94 € (-1.87%) | 52 | 3 | 15% | -0.434% | -1.436% | -1.573% | -17.14 € |
| macd_momentum | 909.91 € (-1.55%) | 71 | 3 | 30% | +0.017% | -0.850% | -0.990% | -13.91 € |
| estocastico_rebote | 906.99 € (-1.87%) | 84 | 30 | 42% | +0.099% | -0.711% | -0.847% | -13.81 € |
| ruptura_estricta | 899.66 € (-2.66%) | 44 | 2 | 9% | -1.331% | -2.418% | -2.568% | -24.50 € |
| macd_sin_salida | 905.99 € (-1.97%) | 63 | 7 | 33% | -0.294% | -1.208% | -1.348% | -17.55 € |
| c_banda_atr_tope | 922.04 € (-0.24%) | 10 | 5 | 50% | +0.251% | -0.849% | -1.019% | -1.96 € |
| ruptura_volumen_tope | 918.62 € (-0.61%) | 17 | 1 | 24% | -0.279% | -1.379% | -1.470% | -5.41 € |
| c_banda_atr_regimen | 909.13 € (-1.63%) | 41 | 4 | 27% | -0.444% | -1.544% | -1.698% | -14.59 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.36 € (-2.80%) | 71 | 1 | 13% | -0.726% | -1.594% | -1.734% | -25.94 € |
| c_banda_atr_evento | 919.30 € (-0.53%) | 11 | 9 | 27% | -0.570% | -1.670% | -1.809% | -4.25 € |
| macd_momentum_evento | 917.71 € (-0.71%) | 24 | 3 | 25% | -0.005% | -1.105% | -1.246% | -6.11 € |
| ruptura_volumen_evento | 914.60 € (-1.04%) | 22 | 2 | 9% | -0.768% | -1.868% | -1.984% | -9.49 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 18:45 | c_banda_atr_evento | DASH | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 18:45 | c_banda_atr_regimen | DASH | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-30 18:45 | c_banda_atr | DASH | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 18:40 | macd_momentum_evento | MON | momentum perdido | -0.31% | -1.41% | -0.33 |
| 2026-09-30 18:40 | ruptura_estricta | XDC | timeout | -0.76% | -1.56% | -0.35 |
| 2026-09-30 18:40 | estocastico_rebote | USELESS | stop-loss | -1.56% | -2.06% | -0.47 |
| 2026-09-30 18:40 | estocastico_rebote | WLD | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 18:40 | estocastico_rebote | ONDO | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 18:40 | estocastico_rebote | ADA | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 18:40 | macd_momentum | MON | momentum perdido | -0.31% | -0.81% | -0.18 |
| 2026-09-30 18:35 | estocastico_rebote | MINA | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 18:35 | estocastico_rebote | PEPE | timeout | -0.71% | -1.21% | -0.28 |
| 2026-09-30 18:35 | estocastico_rebote | SUI | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 18:35 | estocastico_rebote | XRP | timeout | -0.42% | -0.92% | -0.21 |
| 2026-09-30 18:35 | reversion_bb | MINA | stop-loss | -1.50% | -2.60% | -0.60 |

## Eventos de la última vuelta

- 2026-09-30 18:40 [rebote_extremo] ENTRADA ONDO @ 0.42571 (23.10 €, apertura)
- 2026-09-30 18:40 [estocastico_rebote] ENTRADA MINA @ 0.127 (22.76 €, apertura)
- 2026-09-30 18:45 [c_banda_atr] CIERRE DASH stop-loss bruto -1.50% neto -2.30%
- 2026-09-30 18:45 [c_banda_atr_regimen] CIERRE DASH stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 18:45 [c_banda_atr_evento] CIERRE DASH stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 18:40 [macd_momentum] ENTRADA XMR @ 482.14 (22.76 €, apertura)
- 2026-09-30 18:40 [macd_sin_salida] ENTRADA XMR @ 482.14 (22.67 €, apertura)
- 2026-09-30 18:40 [macd_momentum_evento] ENTRADA XMR @ 482.14 (22.95 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
