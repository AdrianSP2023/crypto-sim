# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 22:36 UTC · vueltas 155 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 905.23 € (-2.06%) | 68 | 19 | 31% | -0.213% | -1.096% | -1.242% | -17.16 € |
| reversion_bb | 917.67 € (-0.71%) | 18 | 3 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 902.82 € (-2.32%) | 107 | 5 | 23% | -0.127% | -0.871% | -1.000% | -21.36 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.02 € (-2.08%) | 85 | 3 | 22% | -0.181% | -0.988% | -1.111% | -19.25 € |
| macd_momentum | 890.62 € (-3.64%) | 193 | 13 | 17% | -0.112% | -0.747% | -0.864% | -32.85 € |
| estocastico_rebote | 892.08 € (-3.48%) | 156 | 14 | 31% | -0.219% | -0.886% | -1.007% | -31.59 € |
| ruptura_estricta | 909.15 € (-1.63%) | 47 | 6 | 28% | -0.283% | -1.338% | -1.473% | -14.47 € |
| macd_sin_salida | 900.14 € (-2.61%) | 104 | 34 | 32% | -0.095% | -0.846% | -0.978% | -20.17 € |
| c_banda_atr_tope | 912.83 € (-1.23%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 914.76 € (-1.03%) | 34 | 3 | 15% | -0.070% | -1.170% | -1.287% | -9.16 € |
| c_banda_atr_regimen | 907.54 € (-1.81%) | 53 | 9 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.80 € (-3.29%) | 173 | 0 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 905.94 € (-1.98%) | 89 | 3 | 24% | -0.089% | -0.882% | -1.011% | -18.01 € |
| c_banda_atr_evento | 909.56 € (-1.59%) | 36 | 19 | 25% | -0.463% | -1.547% | -1.706% | -12.82 € |
| macd_momentum_evento | 903.14 € (-2.28%) | 73 | 13 | 10% | -0.351% | -1.213% | -1.331% | -20.32 € |
| ruptura_volumen_evento | 908.44 € (-1.71%) | 48 | 5 | 12% | -0.381% | -1.424% | -1.557% | -15.73 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 22:35 | ruptura_volumen_evento | SPX | timeout | -0.05% | -0.85% | -0.20 |
| 2026-09-29 22:35 | ruptura_volumen_evento | XLM | timeout | -0.21% | -1.01% | -0.23 |
| 2026-09-29 22:35 | macd_momentum_evento | POL | momentum perdido | -0.50% | -1.00% | -0.23 |
| 2026-09-29 22:35 | macd_momentum_evento | ARB | momentum perdido | -0.55% | -1.05% | -0.24 |
| 2026-09-29 22:35 | c_banda_atr_evento | HBAR | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-29 22:35 | ruptura_volumen_regimen | SPX | timeout | -0.05% | -0.55% | -0.13 |
| 2026-09-29 22:35 | ruptura_volumen_regimen | XLM | timeout | -0.21% | -0.71% | -0.16 |
| 2026-09-29 22:35 | ruptura_volumen_tope | SPX | timeout | -0.05% | -1.15% | -0.27 |
| 2026-09-29 22:35 | ruptura_estricta | FET | stop-loss | -2.03% | -2.53% | -0.58 |
| 2026-09-29 22:35 | macd_momentum | POL | momentum perdido | -0.50% | -1.00% | -0.22 |
| 2026-09-29 22:35 | macd_momentum | ARB | momentum perdido | -0.55% | -1.05% | -0.23 |
| 2026-09-29 22:35 | pullback_tendencia | PENGU | rotura de tendencia | +0.00% | -0.50% | -0.11 |
| 2026-09-29 22:35 | ruptura_volumen | SPX | timeout | -0.05% | -0.55% | -0.13 |
| 2026-09-29 22:35 | ruptura_volumen | XLM | timeout | -0.21% | -0.71% | -0.16 |
| 2026-09-29 22:35 | c_banda_atr | HBAR | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-29 22:35 [c_banda_atr] CIERRE HBAR stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 22:35 [c_banda_atr_evento] CIERRE HBAR stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 22:35 [ruptura_volumen] CIERRE XLM timeout bruto -0.21% neto -0.71%
- 2026-09-29 22:35 [ruptura_volumen_regimen] CIERRE XLM timeout bruto -0.21% neto -0.71%
- 2026-09-29 22:35 [ruptura_volumen_evento] CIERRE XLM timeout bruto -0.21% neto -1.01%
- 2026-09-29 22:30 [pullback_tendencia] ENTRADA PUMP @ 0.00515 (22.63 €, apertura)
- 2026-09-29 22:35 [macd_momentum] CIERRE ARB momentum perdido bruto -0.55% neto -1.05%
- 2026-09-29 22:35 [macd_momentum_evento] CIERRE ARB momentum perdido bruto -0.55% neto -1.05%
- 2026-09-29 22:30 [pullback_tendencia] ENTRADA PENGU @ 0.008741 (22.63 €, apertura)
- 2026-09-29 22:35 [pullback_tendencia] CIERRE PENGU rotura de tendencia bruto +0.00% neto -0.50%
- 2026-09-29 22:35 [macd_momentum] CIERRE POL momentum perdido bruto -0.50% neto -1.00%
- 2026-09-29 22:35 [macd_momentum_evento] CIERRE POL momentum perdido bruto -0.50% neto -1.00%
- 2026-09-29 22:35 [ruptura_volumen] CIERRE SPX timeout bruto -0.05% neto -0.55%
- 2026-09-29 22:35 [ruptura_volumen_tope] CIERRE SPX timeout bruto -0.05% neto -1.15%
- 2026-09-29 22:35 [ruptura_volumen_regimen] CIERRE SPX timeout bruto -0.05% neto -0.55%
- 2026-09-29 22:35 [ruptura_volumen_evento] CIERRE SPX timeout bruto -0.05% neto -0.85%
- 2026-09-29 22:35 [ruptura_estricta] CIERRE FET stop-loss bruto -2.03% neto -2.53%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
