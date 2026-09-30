# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 00:26 UTC · vueltas 177 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.57 € (-2.89%) | 87 | 18 | 25% | -0.419% | -1.219% | -1.363% | -24.32 € |
| reversion_bb | 917.37 € (-0.74%) | 19 | 14 | 32% | -0.342% | -1.442% | -1.543% | -6.32 € |
| ruptura_volumen | 899.95 € (-2.63%) | 118 | 5 | 22% | -0.168% | -0.889% | -1.018% | -23.99 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.42 € (-2.14%) | 93 | 2 | 23% | -0.154% | -0.935% | -1.055% | -19.91 € |
| macd_momentum | 882.80 € (-4.48%) | 230 | 4 | 15% | -0.174% | -0.787% | -0.899% | -41.07 € |
| estocastico_rebote | 891.61 € (-3.53%) | 165 | 12 | 32% | -0.184% | -0.843% | -0.962% | -31.77 € |
| ruptura_estricta | 908.00 € (-1.76%) | 51 | 6 | 25% | -0.313% | -1.325% | -1.459% | -15.53 € |
| macd_sin_salida | 894.94 € (-3.17%) | 138 | 8 | 27% | -0.198% | -0.888% | -1.011% | -27.97 € |
| c_banda_atr_tope | 912.55 € (-1.27%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.22 € (-1.19%) | 40 | 3 | 15% | -0.097% | -1.197% | -1.319% | -11.01 € |
| c_banda_atr_regimen | 900.64 € (-2.55%) | 67 | 9 | 24% | -0.506% | -1.395% | -1.529% | -21.46 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.37 € (-2.26%) | 96 | 4 | 22% | -0.151% | -0.922% | -1.053% | -20.29 € |
| c_banda_atr_evento | 901.18 € (-2.50%) | 55 | 18 | 18% | -0.704% | -1.640% | -1.793% | -20.70 € |
| macd_momentum_evento | 895.21 € (-3.14%) | 110 | 4 | 8% | -0.400% | -1.140% | -1.248% | -28.65 € |
| ruptura_volumen_evento | 905.49 € (-2.03%) | 59 | 5 | 12% | -0.415% | -1.362% | -1.495% | -18.45 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 00:25 | ruptura_volumen_evento | RAY | stop-loss | -1.53% | -2.03% | -0.46 |
| 2026-09-30 00:25 | c_banda_atr_evento | GRT | timeout | -0.81% | -1.60% | -0.37 |
| 2026-09-30 00:25 | c_banda_atr_evento | TRUMP | timeout | -0.83% | -1.63% | -0.37 |
| 2026-09-30 00:25 | c_banda_atr_evento | PEPE | timeout | -0.32% | -1.12% | -0.26 |
| 2026-09-30 00:25 | c_banda_atr_evento | ATOM | timeout | -0.67% | -1.47% | -0.34 |
| 2026-09-30 00:25 | c_banda_atr_evento | TAO | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 00:25 | c_banda_atr_evento | XLM | timeout | -1.12% | -1.93% | -0.44 |
| 2026-09-30 00:25 | ruptura_volumen_regimen | RAY | stop-loss | -1.53% | -2.03% | -0.46 |
| 2026-09-30 00:25 | c_banda_atr_regimen | GRT | timeout | -0.81% | -1.30% | -0.30 |
| 2026-09-30 00:25 | c_banda_atr_regimen | TRUMP | timeout | -0.83% | -1.33% | -0.30 |
| 2026-09-30 00:25 | c_banda_atr_regimen | PEPE | timeout | -0.32% | -0.82% | -0.19 |
| 2026-09-30 00:25 | c_banda_atr_regimen | ATOM | timeout | -0.67% | -1.17% | -0.27 |
| 2026-09-30 00:25 | c_banda_atr_regimen | TAO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 00:25 | c_banda_atr_regimen | XLM | timeout | -1.12% | -1.62% | -0.37 |
| 2026-09-30 00:25 | macd_sin_salida | PUMP | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-30 00:20 [pullback_tendencia] ENTRADA QNT @ 241.94 (22.62 €, apertura)
- 2026-09-30 00:25 [pullback_tendencia] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [c_banda_atr] CIERRE XLM timeout bruto -1.13% neto -1.63%
- 2026-09-30 00:25 [c_banda_atr_regimen] CIERRE XLM timeout bruto -1.13% neto -1.63%
- 2026-09-30 00:25 [c_banda_atr_evento] CIERRE XLM timeout bruto -1.13% neto -1.93%
- 2026-09-30 00:20 [reversion_bb] ENTRADA AAVE @ 143.46 (22.95 €, apertura)
- 2026-09-30 00:25 [estocastico_rebote] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [estocastico_rebote] CIERRE PUMP stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [macd_sin_salida] CIERRE PUMP stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [c_banda_atr] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [c_banda_atr_regimen] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [c_banda_atr_evento] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:25 [c_banda_atr] CIERRE ATOM timeout bruto -0.66% neto -1.16%
- 2026-09-30 00:25 [c_banda_atr_regimen] CIERRE ATOM timeout bruto -0.66% neto -1.16%
- 2026-09-30 00:25 [c_banda_atr_evento] CIERRE ATOM timeout bruto -0.66% neto -1.46%
- 2026-09-30 00:25 [c_banda_atr] CIERRE PEPE timeout bruto -0.32% neto -0.82%
- 2026-09-30 00:25 [c_banda_atr_regimen] CIERRE PEPE timeout bruto -0.32% neto -0.82%
- 2026-09-30 00:25 [c_banda_atr_evento] CIERRE PEPE timeout bruto -0.32% neto -1.12%
- 2026-09-30 00:25 [ruptura_volumen] CIERRE RAY stop-loss bruto -1.53% neto -2.03%
- 2026-09-30 00:20 [pullback_tendencia] ENTRADA RAY @ 1.671 (22.61 €, apertura)
- 2026-09-30 00:25 [ruptura_volumen_regimen] CIERRE RAY stop-loss bruto -1.53% neto -2.03%
- 2026-09-30 00:25 [ruptura_volumen_evento] CIERRE RAY stop-loss bruto -1.53% neto -2.03%
- 2026-09-30 00:25 [c_banda_atr] CIERRE TRUMP timeout bruto -0.83% neto -1.33%
- 2026-09-30 00:25 [c_banda_atr_regimen] CIERRE TRUMP timeout bruto -0.83% neto -1.33%
- 2026-09-30 00:25 [c_banda_atr_evento] CIERRE TRUMP timeout bruto -0.83% neto -1.63%
- 2026-09-30 00:25 [c_banda_atr] CIERRE GRT timeout bruto -0.81% neto -1.31%
- 2026-09-30 00:25 [c_banda_atr_regimen] CIERRE GRT timeout bruto -0.81% neto -1.31%
- 2026-09-30 00:25 [c_banda_atr_evento] CIERRE GRT timeout bruto -0.81% neto -1.61%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
