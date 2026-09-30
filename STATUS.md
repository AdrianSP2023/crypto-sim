# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 22:16 UTC · vueltas 92 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 900.71 € (-2.55%) | 64 | 18 | 20% | -0.593% | -1.501% | -1.650% | -22.04 € |
| reversion_bb | 921.47 € (-0.30%) | 9 | 5 | 44% | -0.167% | -1.267% | -1.401% | -2.64 € |
| ruptura_volumen | 896.49 € (-3.00%) | 84 | 10 | 14% | -0.625% | -1.436% | -1.580% | -27.62 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.61 € (-2.12%) | 65 | 1 | 15% | -0.413% | -1.319% | -1.456% | -19.65 € |
| macd_momentum | 904.70 € (-2.11%) | 100 | 3 | 24% | -0.100% | -0.861% | -0.993% | -19.75 € |
| estocastico_rebote | 901.48 € (-2.46%) | 123 | 7 | 33% | -0.071% | -0.783% | -0.916% | -22.15 € |
| ruptura_estricta | 897.80 € (-2.86%) | 48 | 5 | 10% | -1.282% | -2.332% | -2.480% | -25.75 € |
| macd_sin_salida | 902.43 € (-2.36%) | 80 | 11 | 31% | -0.317% | -1.143% | -1.276% | -21.02 € |
| c_banda_atr_tope | 918.92 € (-0.58%) | 18 | 3 | 28% | -0.168% | -1.268% | -1.428% | -5.26 € |
| ruptura_volumen_tope | 916.58 € (-0.83%) | 24 | 4 | 17% | -0.322% | -1.422% | -1.541% | -7.86 € |
| c_banda_atr_regimen | 908.47 € (-1.71%) | 45 | 0 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 908.49 € (-1.70%) | 31 | 18 | 10% | -0.895% | -1.995% | -2.132% | -14.24 € |
| macd_momentum_evento | 909.85 € (-1.56%) | 53 | 3 | 15% | -0.213% | -1.200% | -1.327% | -14.60 € |
| ruptura_volumen_evento | 910.62 € (-1.47%) | 34 | 10 | 9% | -0.623% | -1.723% | -1.859% | -13.49 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 22:15 | macd_momentum_evento | HYPE | momentum perdido | +0.68% | -0.12% | -0.03 |
| 2026-09-30 22:15 | macd_momentum_evento | LINK | momentum perdido | -0.39% | -1.19% | -0.27 |
| 2026-09-30 22:15 | macd_momentum | HYPE | momentum perdido | +0.68% | +0.18% | +0.04 |
| 2026-09-30 22:15 | macd_momentum | LINK | momentum perdido | -0.39% | -0.89% | -0.20 |
| 2026-09-30 22:10 | ruptura_volumen_evento | KSM | stop-loss | -1.32% | -2.42% | -0.55 |
| 2026-09-30 22:10 | ruptura_volumen_evento | MON | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 22:10 | c_banda_atr_evento | DASH | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 22:10 | c_banda_atr_evento | RENDER | stop-loss | -1.76% | -2.87% | -0.66 |
| 2026-09-30 22:10 | c_banda_atr_evento | WLD | stop-loss | -1.57% | -2.67% | -0.61 |
| 2026-09-30 22:10 | c_banda_atr_tope | WLD | stop-loss | -1.57% | -2.67% | -0.61 |
| 2026-09-30 22:10 | c_banda_atr_tope | FET | stop-loss | -1.60% | -2.70% | -0.62 |
| 2026-09-30 22:10 | macd_sin_salida | WLD | stop-loss | -1.72% | -2.21% | -0.50 |
| 2026-09-30 22:10 | macd_sin_salida | FET | timeout | -0.61% | -1.11% | -0.25 |
| 2026-09-30 22:10 | ruptura_estricta | FET | stop-loss | -2.00% | -2.50% | -0.56 |
| 2026-09-30 22:10 | estocastico_rebote | FET | stop-loss | -1.60% | -2.10% | -0.47 |

## Eventos de la última vuelta

- 2026-09-30 22:15 [macd_momentum] CIERRE LINK momentum perdido bruto -0.39% neto -0.89%
- 2026-09-30 22:15 [macd_momentum_evento] CIERRE LINK momentum perdido bruto -0.39% neto -1.19%
- 2026-09-30 22:10 [estocastico_rebote] ENTRADA HBAR @ 0.093 (22.55 €, apertura)
- 2026-09-30 22:10 [pullback_tendencia] ENTRADA PUMP @ 0.005206 (22.61 €, apertura)
- 2026-09-30 22:15 [macd_momentum] CIERRE HYPE momentum perdido bruto +0.68% neto +0.18%
- 2026-09-30 22:15 [macd_momentum_evento] CIERRE HYPE momentum perdido bruto +0.68% neto -0.12%
- 2026-09-30 22:10 [reversion_bb] ENTRADA KAS @ 0.038 (23.04 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
