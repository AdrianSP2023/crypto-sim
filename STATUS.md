# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 15:17 UTC · vueltas 67 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 913.23 € (-1.19%) | 41 | 9 | 39% | +0.038% | -1.033% | -1.175% | -9.77 € |
| reversion_bb | 922.78 € (-0.16%) | 2 | 3 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 911.66 € (-1.36%) | 65 | 4 | 29% | +0.050% | -0.851% | -0.987% | -12.73 € |
| rebote_extremo | 924.02 € (-0.02%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 911.38 € (-1.39%) | 59 | 5 | 27% | -0.009% | -0.952% | -1.060% | -12.92 € |
| macd_momentum | 899.98 € (-2.62%) | 143 | 4 | 20% | -0.054% | -0.737% | -0.852% | -24.13 € |
| estocastico_rebote | 909.89 € (-1.55%) | 73 | 21 | 44% | +0.208% | -0.637% | -0.774% | -10.72 € |
| ruptura_estricta | 916.26 € (-0.86%) | 33 | 8 | 33% | +0.044% | -1.056% | -1.179% | -8.04 € |
| macd_sin_salida | 909.81 € (-1.56%) | 79 | 14 | 37% | +0.171% | -0.659% | -0.785% | -11.96 € |
| c_banda_atr_tope | 917.86 € (-0.69%) | 14 | 3 | 21% | -0.635% | -1.735% | -1.906% | -5.60 € |
| ruptura_volumen_tope | 920.80 € (-0.37%) | 18 | 2 | 22% | +0.248% | -0.852% | -0.988% | -3.54 € |
| c_banda_atr_regimen | 913.23 € (-1.19%) | 41 | 9 | 39% | +0.038% | -1.033% | -1.175% | -9.77 € |
| macd_momentum_regimen | 899.98 € (-2.62%) | 143 | 4 | 20% | -0.054% | -0.737% | -0.852% | -24.13 € |
| ruptura_volumen_regimen | 911.66 € (-1.36%) | 65 | 4 | 29% | +0.050% | -0.851% | -0.987% | -12.73 € |
| c_banda_atr_evento | 919.28 € (-0.54%) | 12 | 6 | 33% | -0.366% | -1.466% | -1.646% | -4.06 € |
| macd_momentum_evento | 915.53 € (-0.94%) | 23 | 4 | 17% | -0.513% | -1.613% | -1.726% | -8.58 € |
| ruptura_volumen_evento | 921.68 € (-0.28%) | 7 | 3 | 29% | -0.366% | -1.466% | -1.659% | -2.37 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 15:15 | macd_momentum_evento | SPX | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 15:15 | macd_momentum_evento | OP | momentum perdido | -0.59% | -1.69% | -0.39 |
| 2026-09-29 15:15 | macd_momentum_evento | BCH | momentum perdido | -0.70% | -1.80% | -0.42 |
| 2026-09-29 15:15 | macd_momentum_evento | TAO | momentum perdido | -0.71% | -1.81% | -0.42 |
| 2026-09-29 15:15 | macd_momentum_evento | SUI | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 15:15 | macd_momentum_evento | ADA | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 15:15 | c_banda_atr_evento | ASTER | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 15:15 | c_banda_atr_evento | RENDER | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 15:15 | c_banda_atr_evento | ADA | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 15:15 | macd_momentum_regimen | SPX | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 15:15 | macd_momentum_regimen | OP | momentum perdido | -0.76% | -1.26% | -0.29 |
| 2026-09-29 15:15 | macd_momentum_regimen | BCH | momentum perdido | -0.70% | -1.21% | -0.27 |
| 2026-09-29 15:15 | macd_momentum_regimen | TAO | momentum perdido | -0.71% | -1.21% | -0.27 |
| 2026-09-29 15:15 | macd_momentum_regimen | SUI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 15:15 | macd_momentum_regimen | ADA | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-29 15:15 [pullback_tendencia] CIERRE XRP rotura de tendencia bruto -0.99% neto -1.49%
- 2026-09-29 15:15 [macd_momentum] CIERRE ADA stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:15 [macd_momentum_regimen] CIERRE ADA stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:15 [c_banda_atr_evento] CIERRE ADA stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:15 [macd_momentum_evento] CIERRE ADA stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:15 [macd_momentum] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:15 [macd_sin_salida] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:15 [macd_momentum_regimen] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:15 [macd_momentum_evento] CIERRE SUI stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:15 [macd_sin_salida] CIERRE XLM stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:10 [reversion_bb] ENTRADA AVAX @ 10.035 (23.08 €, apertura)
- 2026-09-29 15:15 [macd_momentum] CIERRE TAO momentum perdido bruto -0.71% neto -1.21%
- 2026-09-29 15:15 [macd_momentum_regimen] CIERRE TAO momentum perdido bruto -0.71% neto -1.21%
- 2026-09-29 15:15 [macd_momentum_evento] CIERRE TAO momentum perdido bruto -0.71% neto -1.81%
- 2026-09-29 15:15 [estocastico_rebote] CIERRE XDC stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:15 [c_banda_atr] CIERRE DASH stop-loss bruto -1.54% neto -2.34%
- 2026-09-29 15:15 [c_banda_atr_regimen] CIERRE DASH stop-loss bruto -1.54% neto -2.34%
- 2026-09-29 15:15 [ruptura_estricta] CIERRE ENA stop-loss bruto -2.00% neto -3.10%
- 2026-09-29 15:15 [estocastico_rebote] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:10 [reversion_bb] ENTRADA BCH @ 273.18 (23.08 €, apertura)
- 2026-09-29 15:15 [macd_momentum] CIERRE BCH momentum perdido bruto -0.71% neto -1.21%
- 2026-09-29 15:15 [macd_momentum_regimen] CIERRE BCH momentum perdido bruto -0.71% neto -1.21%
- 2026-09-29 15:15 [macd_momentum_evento] CIERRE BCH momentum perdido bruto -0.71% neto -1.81%
- 2026-09-29 15:15 [c_banda_atr] CIERRE RENDER stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 15:15 [c_banda_atr_regimen] CIERRE RENDER stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 15:15 [c_banda_atr_evento] CIERRE RENDER stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:15 [pullback_tendencia] CIERRE PEPE rotura de tendencia bruto -1.30% neto -2.10%
- 2026-09-29 15:15 [macd_momentum] CIERRE OP momentum perdido bruto -0.76% neto -1.26%
- 2026-09-29 15:15 [macd_momentum_regimen] CIERRE OP momentum perdido bruto -0.76% neto -1.26%
- 2026-09-29 15:15 [macd_momentum_evento] CIERRE OP momentum perdido bruto -0.59% neto -1.69%
- 2026-09-29 15:15 [estocastico_rebote] CIERRE GRT stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:15 [c_banda_atr_evento] CIERRE ASTER stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:15 [macd_momentum] CIERRE SPX stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:15 [macd_momentum_regimen] CIERRE SPX stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 15:15 [macd_momentum_evento] CIERRE SPX stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 15:10 [reversion_bb] ENTRADA FET @ 0.2017 (23.08 €, apertura)
- 2026-09-29 15:10 [estocastico_rebote] ENTRADA FET @ 0.2017 (22.84 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
