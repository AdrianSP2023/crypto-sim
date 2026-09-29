# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 13:31 UTC · vueltas 47 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 925.18 € (+0.10%) | 11 | 24 | 91% | +1.682% | +0.582% | +0.462% | +1.48 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 918.69 € (-0.60%) | 36 | 19 | 33% | +0.325% | -0.758% | -0.896% | -6.30 € |
| rebote_extremo | 924.54 € (+0.03%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 920.30 € (-0.43%) | 28 | 12 | 39% | +0.391% | -0.709% | -0.821% | -4.59 € |
| macd_momentum | 910.29 € (-1.51%) | 92 | 11 | 21% | +0.085% | -0.699% | -0.813% | -14.81 € |
| estocastico_rebote | 926.73 € (+0.27%) | 31 | 35 | 74% | +1.056% | +0.005% | -0.129% | +0.04 € |
| ruptura_estricta | 921.47 € (-0.30%) | 20 | 14 | 35% | +0.299% | -0.801% | -0.935% | -3.70 € |
| macd_sin_salida | 919.05 € (-0.56%) | 44 | 21 | 41% | +0.466% | -0.545% | -0.668% | -5.54 € |
| c_banda_atr_tope | 924.19 € (-0.01%) | 2 | 5 | 100% | +2.000% | +0.900% | +0.708% | +0.42 € |
| ruptura_volumen_tope | 922.82 € (-0.15%) | 10 | 5 | 30% | +0.387% | -0.713% | -0.836% | -1.65 € |
| c_banda_atr_regimen | 925.18 € (+0.10%) | 11 | 24 | 91% | +1.682% | +0.582% | +0.462% | +1.48 € |
| macd_momentum_regimen | 910.29 € (-1.51%) | 92 | 11 | 21% | +0.085% | -0.699% | -0.813% | -14.81 € |
| ruptura_volumen_regimen | 918.69 € (-0.60%) | 36 | 19 | 33% | +0.325% | -0.758% | -0.896% | -6.30 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 13:30 | ruptura_volumen_regimen | ASTER | timeout | -0.36% | -1.16% | -0.27 |
| 2026-09-29 13:30 | macd_momentum_regimen | INJ | momentum perdido | -0.32% | -0.82% | -0.19 |
| 2026-09-29 13:30 | estocastico_rebote | XDC | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-29 13:30 | macd_momentum | INJ | momentum perdido | -0.32% | -0.82% | -0.19 |
| 2026-09-29 13:30 | pullback_tendencia | ENA | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 13:30 | ruptura_volumen | ASTER | timeout | -0.36% | -1.16% | -0.27 |
| 2026-09-29 13:25 | macd_momentum_regimen | TRUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 13:25 | c_banda_atr_regimen | ENA | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 13:25 | c_banda_atr_tope | ENA | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 13:25 | estocastico_rebote | ASTER | timeout | +0.63% | -0.17% | -0.04 |
| 2026-09-29 13:25 | estocastico_rebote | CRV | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-29 13:25 | macd_momentum | TRUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 13:25 | pullback_tendencia | MON | rotura de tendencia | -0.98% | -2.08% | -0.48 |
| 2026-09-29 13:25 | c_banda_atr | ENA | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 13:20 | ruptura_volumen_regimen | FET | stop-loss | -1.24% | -2.04% | -0.47 |

## Eventos de la última vuelta

- 2026-09-29 13:30 [estocastico_rebote] CIERRE XDC take-profit bruto +1.80% neto +1.00%
- 2026-09-29 13:25 [ruptura_volumen] ENTRADA ENA @ 0.2276 (22.96 €, apertura)
- 2026-09-29 13:30 [pullback_tendencia] CIERRE ENA take-profit bruto +2.00% neto +0.90%
- 2026-09-29 13:25 [ruptura_volumen_regimen] ENTRADA ENA @ 0.2276 (22.96 €, apertura)
- 2026-09-29 13:30 [macd_momentum] CIERRE INJ momentum perdido bruto -0.32% neto -0.82%
- 2026-09-29 13:30 [macd_momentum_regimen] CIERRE INJ momentum perdido bruto -0.32% neto -0.82%
- 2026-09-29 13:25 [c_banda_atr] ENTRADA FIL @ 0.951 (23.14 €, apertura)
- 2026-09-29 13:25 [c_banda_atr_regimen] ENTRADA FIL @ 0.951 (23.14 €, apertura)
- 2026-09-29 13:25 [estocastico_rebote] ENTRADA GRT @ 0.02681 (23.11 €, apertura)
- 2026-09-29 13:30 [ruptura_volumen] CIERRE ASTER timeout bruto -0.36% neto -1.16%
- 2026-09-29 13:30 [ruptura_volumen_regimen] CIERRE ASTER timeout bruto -0.36% neto -1.16%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
