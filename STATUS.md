# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 04:51 UTC · vueltas 393 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 892.94 € (-3.39%) | 317 | 18 | 39% | +0.114% | -0.469% | -0.588% | -33.88 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.382% | -4.66 € |
| ruptura_volumen | 873.59 € (-5.48%) | 358 | 38 | 25% | -0.147% | -0.719% | -0.827% | -57.86 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 892.70 € (-3.41%) | 208 | 9 | 19% | -0.088% | -0.715% | -0.802% | -33.79 € |
| macd_momentum | 864.95 € (-6.42%) | 581 | 37 | 23% | +0.054% | -0.491% | -0.592% | -63.77 € |
| estocastico_rebote | 879.73 € (-4.82%) | 370 | 12 | 35% | +0.011% | -0.559% | -0.668% | -46.84 € |
| ruptura_estricta | 892.46 € (-3.44%) | 188 | 34 | 30% | -0.258% | -0.899% | -1.015% | -38.52 € |
| macd_sin_salida | 885.27 € (-4.22%) | 401 | 25 | 40% | +0.092% | -0.474% | -0.583% | -43.27 € |
| c_banda_atr_tope | 913.06 € (-1.21%) | 70 | 5 | 33% | +0.134% | -0.743% | -0.854% | -11.95 € |
| ruptura_volumen_tope | 904.11 € (-2.18%) | 117 | 5 | 26% | -0.045% | -0.771% | -0.885% | -20.64 € |
| c_banda_atr_regimen | 905.43 € (-2.04%) | 170 | 17 | 39% | +0.120% | -0.534% | -0.661% | -20.90 € |
| macd_momentum_regimen | 888.11 € (-3.91%) | 344 | 37 | 22% | +0.054% | -0.522% | -0.625% | -40.71 € |
| ruptura_volumen_regimen | 878.33 € (-4.97%) | 281 | 38 | 22% | -0.247% | -0.840% | -0.952% | -53.15 € |
| c_banda_atr_evento | 898.88 € (-2.74%) | 284 | 18 | 40% | +0.163% | -0.430% | -0.545% | -27.95 € |
| macd_momentum_evento | 869.74 € (-5.90%) | 534 | 37 | 21% | +0.056% | -0.493% | -0.591% | -59.00 € |
| ruptura_volumen_evento | 886.02 € (-4.14%) | 308 | 38 | 26% | -0.069% | -0.654% | -0.755% | -45.52 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 04:50 | ruptura_volumen_evento | HBAR | timeout | +0.95% | +0.45% | +0.10 |
| 2026-10-02 04:50 | macd_momentum_evento | UNI | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 04:50 | macd_momentum_evento | SOL | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 04:50 | c_banda_atr_evento | APT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 04:50 | c_banda_atr_evento | INJ | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 04:50 | c_banda_atr_evento | JUP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 04:50 | c_banda_atr_evento | SUI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 04:50 | ruptura_volumen_regimen | HBAR | timeout | +0.95% | +0.45% | +0.10 |
| 2026-10-02 04:50 | macd_momentum_regimen | UNI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 04:50 | macd_momentum_regimen | SOL | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 04:50 | c_banda_atr_regimen | APT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 04:50 | c_banda_atr_regimen | INJ | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 04:50 | c_banda_atr_regimen | JUP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 04:50 | c_banda_atr_regimen | SUI | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 04:50 | macd_sin_salida | SHIB | take-profit | +2.00% | +1.50% | +0.33 |

## Eventos de la última vuelta

- 2026-10-02 04:50 [macd_momentum] CIERRE SOL take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [macd_sin_salida] CIERRE SOL take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [macd_momentum_regimen] CIERRE SOL take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [macd_momentum_evento] CIERRE SOL take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:45 [ruptura_volumen] ENTRADA NEAR @ 4.4848 (21.66 €, apertura)
- 2026-10-02 04:45 [ruptura_volumen_regimen] ENTRADA NEAR @ 4.4848 (21.77 €, apertura)
- 2026-10-02 04:45 [ruptura_volumen_evento] ENTRADA NEAR @ 4.4848 (21.97 €, apertura)
- 2026-10-02 04:50 [c_banda_atr] CIERRE SUI take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [c_banda_atr_regimen] CIERRE SUI take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [c_banda_atr_evento] CIERRE SUI take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [ruptura_volumen] CIERRE HBAR timeout bruto +0.95% neto +0.45%
- 2026-10-02 04:50 [ruptura_volumen_regimen] CIERRE HBAR timeout bruto +0.95% neto +0.45%
- 2026-10-02 04:50 [ruptura_volumen_evento] CIERRE HBAR timeout bruto +0.95% neto +0.45%
- 2026-10-02 04:50 [macd_sin_salida] CIERRE XLM take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [macd_momentum] CIERRE UNI take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [macd_momentum_regimen] CIERRE UNI take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [macd_momentum_evento] CIERRE UNI take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [ruptura_estricta] CIERRE ARB take-profit bruto +3.00% neto +2.50%
- 2026-10-02 04:50 [c_banda_atr] CIERRE JUP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [estocastico_rebote] CIERRE JUP take-profit bruto +1.80% neto +1.30%
- 2026-10-02 04:50 [c_banda_atr_regimen] CIERRE JUP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [c_banda_atr_evento] CIERRE JUP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [ruptura_estricta] CIERRE PEPE take-profit bruto +3.00% neto +2.50%
- 2026-10-02 04:50 [pullback_tendencia] CIERRE RENDER take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [c_banda_atr] CIERRE INJ take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [estocastico_rebote] CIERRE INJ take-profit bruto +1.96% neto +1.46%
- 2026-10-02 04:50 [c_banda_atr_regimen] CIERRE INJ take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [c_banda_atr_evento] CIERRE INJ take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [pullback_tendencia] CIERRE SHIB take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [macd_sin_salida] CIERRE SHIB take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [c_banda_atr] CIERRE APT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [pullback_tendencia] CIERRE APT take-profit bruto +2.03% neto +1.53%
- 2026-10-02 04:50 [estocastico_rebote] CIERRE APT take-profit bruto +1.80% neto +1.30%
- 2026-10-02 04:50 [c_banda_atr_regimen] CIERRE APT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 04:50 [c_banda_atr_evento] CIERRE APT take-profit bruto +2.00% neto +1.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
