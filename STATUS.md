# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 18:41 UTC · vueltas 49 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.53 € (-1.59%) | 43 | 10 | 30% | -0.331% | -1.389% | -1.543% | -13.77 € |
| reversion_bb | 922.74 € (-0.16%) | 5 | 4 | 60% | +0.300% | -0.800% | -0.943% | -0.93 € |
| ruptura_volumen | 898.87 € (-2.74%) | 72 | 2 | 14% | -0.670% | -1.532% | -1.672% | -25.31 € |
| rebote_extremo | 923.90 € (-0.04%) | 2 | 0 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 907.33 € (-1.83%) | 52 | 3 | 15% | -0.434% | -1.436% | -1.573% | -17.14 € |
| macd_momentum | 910.20 € (-1.52%) | 71 | 2 | 30% | +0.017% | -0.850% | -0.990% | -13.91 € |
| estocastico_rebote | 907.36 € (-1.83%) | 84 | 29 | 42% | +0.099% | -0.711% | -0.847% | -13.81 € |
| ruptura_estricta | 899.88 € (-2.64%) | 44 | 2 | 9% | -1.331% | -2.418% | -2.568% | -24.50 € |
| macd_sin_salida | 906.22 € (-1.95%) | 63 | 6 | 33% | -0.294% | -1.208% | -1.348% | -17.55 € |
| c_banda_atr_tope | 921.99 € (-0.24%) | 10 | 5 | 50% | +0.251% | -0.849% | -1.019% | -1.96 € |
| ruptura_volumen_tope | 918.69 € (-0.60%) | 17 | 1 | 24% | -0.279% | -1.379% | -1.470% | -5.41 € |
| c_banda_atr_regimen | 909.69 € (-1.57%) | 40 | 5 | 28% | -0.418% | -1.518% | -1.671% | -14.00 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.37 € (-2.80%) | 71 | 1 | 13% | -0.726% | -1.594% | -1.734% | -25.94 € |
| c_banda_atr_evento | 919.82 € (-0.48%) | 10 | 10 | 30% | -0.477% | -1.577% | -1.709% | -3.64 € |
| macd_momentum_evento | 918.00 € (-0.67%) | 24 | 2 | 25% | -0.005% | -1.105% | -1.246% | -6.11 € |
| ruptura_volumen_evento | 914.68 € (-1.03%) | 22 | 2 | 9% | -0.768% | -1.868% | -1.984% | -9.49 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-30 18:30 | ruptura_volumen_evento | XMR | timeout | +0.35% | -0.75% | -0.17 |
| 2026-09-30 18:30 | ruptura_volumen_regimen | XMR | timeout | +0.35% | -0.15% | -0.03 |
| 2026-09-30 18:30 | ruptura_volumen | XMR | timeout | +0.35% | -0.15% | -0.03 |

## Eventos de la última vuelta

- 2026-09-30 18:40 [estocastico_rebote] CIERRE ADA stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 18:35 [estocastico_rebote] ENTRADA ENA @ 0.233 (22.80 €, apertura)
- 2026-09-30 18:40 [estocastico_rebote] CIERRE ONDO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 18:40 [estocastico_rebote] CIERRE WLD stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 18:40 [ruptura_estricta] CIERRE XDC timeout bruto -0.76% neto -1.56%
- 2026-09-30 18:40 [estocastico_rebote] CIERRE USELESS stop-loss bruto -1.56% neto -2.06%
- 2026-09-30 18:40 [macd_momentum] CIERRE MON momentum perdido bruto -0.31% neto -0.81%
- 2026-09-30 18:40 [macd_momentum_evento] CIERRE MON momentum perdido bruto -0.31% neto -1.41%
- 2026-09-30 18:35 [c_banda_atr] ENTRADA BNB @ 677.08 (22.76 €, apertura)
- 2026-09-30 18:35 [c_banda_atr_evento] ENTRADA BNB @ 677.08 (23.01 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
