# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 18:36 UTC · vueltas 48 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.88 € (-1.55%) | 43 | 9 | 30% | -0.331% | -1.389% | -1.543% | -13.77 € |
| reversion_bb | 922.97 € (-0.14%) | 5 | 4 | 60% | +0.300% | -0.800% | -0.943% | -0.93 € |
| ruptura_volumen | 899.10 € (-2.72%) | 72 | 2 | 14% | -0.670% | -1.532% | -1.672% | -25.31 € |
| rebote_extremo | 923.90 € (-0.04%) | 2 | 0 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 907.62 € (-1.80%) | 52 | 3 | 15% | -0.434% | -1.436% | -1.573% | -17.14 € |
| macd_momentum | 910.59 € (-1.48%) | 70 | 3 | 30% | +0.022% | -0.851% | -0.991% | -13.73 € |
| estocastico_rebote | 909.90 € (-1.55%) | 80 | 32 | 44% | +0.180% | -0.646% | -0.783% | -11.97 € |
| ruptura_estricta | 900.36 € (-2.58%) | 43 | 3 | 9% | -1.345% | -2.438% | -2.588% | -24.15 € |
| macd_sin_salida | 906.53 € (-1.92%) | 63 | 6 | 33% | -0.294% | -1.208% | -1.348% | -17.55 € |
| c_banda_atr_tope | 922.19 € (-0.22%) | 10 | 5 | 50% | +0.251% | -0.849% | -1.019% | -1.96 € |
| ruptura_volumen_tope | 918.81 € (-0.59%) | 17 | 1 | 24% | -0.279% | -1.379% | -1.470% | -5.41 € |
| c_banda_atr_regimen | 909.79 € (-1.56%) | 40 | 5 | 28% | -0.418% | -1.518% | -1.671% | -14.00 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.50 € (-2.79%) | 71 | 1 | 13% | -0.726% | -1.594% | -1.734% | -25.94 € |
| c_banda_atr_evento | 920.17 € (-0.44%) | 10 | 9 | 30% | -0.477% | -1.577% | -1.709% | -3.64 € |
| macd_momentum_evento | 918.53 € (-0.62%) | 23 | 3 | 26% | +0.009% | -1.091% | -1.236% | -5.79 € |
| ruptura_volumen_evento | 914.92 € (-1.01%) | 22 | 2 | 9% | -0.768% | -1.868% | -1.984% | -9.49 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 18:35 | estocastico_rebote | MINA | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 18:35 | estocastico_rebote | PEPE | timeout | -0.71% | -1.21% | -0.28 |
| 2026-09-30 18:35 | estocastico_rebote | SUI | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 18:35 | estocastico_rebote | XRP | timeout | -0.42% | -0.92% | -0.21 |
| 2026-09-30 18:35 | reversion_bb | MINA | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 18:30 | ruptura_volumen_evento | XMR | timeout | +0.35% | -0.75% | -0.17 |
| 2026-09-30 18:30 | ruptura_volumen_regimen | XMR | timeout | +0.35% | -0.15% | -0.03 |
| 2026-09-30 18:30 | ruptura_volumen | XMR | timeout | +0.35% | -0.15% | -0.03 |
| 2026-09-30 18:25 | macd_momentum_evento | TON | momentum perdido | -0.30% | -1.40% | -0.32 |
| 2026-09-30 18:25 | macd_momentum_evento | XDC | momentum perdido | -0.56% | -1.66% | -0.38 |
| 2026-09-30 18:25 | macd_momentum_regimen | XDC | momentum perdido | -0.56% | -1.06% | -0.24 |
| 2026-09-30 18:25 | macd_momentum | TON | momentum perdido | -0.30% | -0.80% | -0.18 |
| 2026-09-30 18:25 | macd_momentum | XDC | momentum perdido | -0.56% | -1.06% | -0.24 |
| 2026-09-30 18:10 | macd_sin_salida | VVV | stop-loss | -2.31% | -2.81% | -0.64 |
| 2026-09-30 18:10 | estocastico_rebote | ENA | stop-loss | -1.65% | -2.15% | -0.49 |

## Eventos de la última vuelta

- 2026-09-30 18:35 [estocastico_rebote] CIERRE XRP timeout bruto -0.42% neto -0.92%
- 2026-09-30 18:30 [macd_momentum] ENTRADA NEAR @ 4.8059 (22.76 €, apertura)
- 2026-09-30 18:30 [macd_sin_salida] ENTRADA NEAR @ 4.8059 (22.67 €, apertura)
- 2026-09-30 18:30 [macd_momentum_evento] ENTRADA NEAR @ 4.8059 (22.96 €, apertura)
- 2026-09-30 18:35 [estocastico_rebote] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 18:30 [ruptura_volumen] ENTRADA ALGO @ 0.11108 (22.47 €, apertura)
- 2026-09-30 18:30 [ruptura_volumen_tope] ENTRADA ALGO @ 0.11108 (22.97 €, apertura)
- 2026-09-30 18:30 [ruptura_volumen_evento] ENTRADA ALGO @ 0.11108 (22.87 €, apertura)
- 2026-09-30 18:35 [estocastico_rebote] CIERRE PEPE timeout bruto -0.71% neto -1.21%
- 2026-09-30 18:35 [reversion_bb] CIERRE MINA stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 18:35 [estocastico_rebote] CIERRE MINA stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
