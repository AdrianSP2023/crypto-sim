# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 23:51 UTC · vueltas 170 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 900.28 € (-2.59%) | 77 | 25 | 29% | -0.324% | -1.163% | -1.310% | -20.56 € |
| reversion_bb | 918.03 € (-0.67%) | 18 | 12 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 901.02 € (-2.51%) | 114 | 7 | 23% | -0.133% | -0.862% | -0.988% | -22.49 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.31 € (-2.16%) | 91 | 0 | 22% | -0.169% | -0.956% | -1.077% | -19.93 € |
| macd_momentum | 883.32 € (-4.43%) | 227 | 3 | 15% | -0.178% | -0.793% | -0.904% | -40.85 € |
| estocastico_rebote | 892.50 € (-3.43%) | 162 | 9 | 33% | -0.168% | -0.830% | -0.950% | -30.73 € |
| ruptura_estricta | 908.61 € (-1.69%) | 49 | 8 | 27% | -0.286% | -1.318% | -1.451% | -14.86 € |
| macd_sin_salida | 896.20 € (-3.03%) | 131 | 14 | 27% | -0.183% | -0.883% | -1.008% | -26.42 € |
| c_banda_atr_tope | 913.01 € (-1.22%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 914.00 € (-1.11%) | 38 | 3 | 16% | -0.032% | -1.132% | -1.250% | -9.90 € |
| c_banda_atr_regimen | 902.96 € (-2.30%) | 58 | 18 | 28% | -0.411% | -1.361% | -1.501% | -18.16 € |
| macd_momentum_regimen | 887.47 € (-3.98%) | 192 | 1 | 15% | -0.201% | -0.837% | -0.949% | -36.53 € |
| ruptura_volumen_regimen | 904.21 € (-2.17%) | 94 | 6 | 22% | -0.122% | -0.900% | -1.028% | -19.39 € |
| c_banda_atr_evento | 904.31 € (-2.16%) | 45 | 25 | 22% | -0.604% | -1.597% | -1.756% | -16.51 € |
| macd_momentum_evento | 895.74 € (-3.08%) | 107 | 3 | 7% | -0.416% | -1.163% | -1.268% | -28.43 € |
| ruptura_volumen_evento | 906.56 € (-1.91%) | 55 | 7 | 13% | -0.360% | -1.340% | -1.468% | -16.93 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 23:50 | ruptura_volumen_evento | ZEC | timeout | -0.05% | -0.55% | -0.12 |
| 2026-09-29 23:50 | macd_momentum_evento | POL | momentum perdido | -0.75% | -1.25% | -0.28 |
| 2026-09-29 23:50 | macd_momentum_evento | ATOM | momentum perdido | -0.39% | -0.89% | -0.20 |
| 2026-09-29 23:50 | macd_momentum_evento | PUMP | momentum perdido | -0.67% | -1.17% | -0.27 |
| 2026-09-29 23:50 | macd_momentum_evento | BTC | momentum perdido | +0.16% | -0.34% | -0.08 |
| 2026-09-29 23:50 | macd_momentum_regimen | POL | momentum perdido | -0.75% | -1.25% | -0.28 |
| 2026-09-29 23:50 | macd_momentum_regimen | ATOM | momentum perdido | -0.39% | -0.89% | -0.20 |
| 2026-09-29 23:50 | ruptura_volumen_tope | ZEC | timeout | -0.05% | -1.15% | -0.26 |
| 2026-09-29 23:50 | ruptura_estricta | POL | timeout | -1.11% | -1.61% | -0.37 |
| 2026-09-29 23:50 | macd_momentum | POL | momentum perdido | -0.75% | -1.25% | -0.28 |
| 2026-09-29 23:50 | macd_momentum | ATOM | momentum perdido | -0.39% | -0.89% | -0.20 |
| 2026-09-29 23:50 | macd_momentum | PUMP | momentum perdido | -0.67% | -1.17% | -0.26 |
| 2026-09-29 23:50 | macd_momentum | BTC | momentum perdido | +0.16% | -0.34% | -0.08 |
| 2026-09-29 23:50 | ruptura_volumen | ZEC | timeout | -0.05% | -0.55% | -0.12 |
| 2026-09-29 23:45 | ruptura_volumen_evento | VVV | stop-loss | -1.20% | -1.70% | -0.39 |

## Eventos de la última vuelta

- 2026-09-29 23:50 [macd_momentum] CIERRE BTC momentum perdido bruto +0.16% neto -0.34%
- 2026-09-29 23:50 [macd_momentum_evento] CIERRE BTC momentum perdido bruto +0.16% neto -0.34%
- 2026-09-29 23:50 [ruptura_volumen] CIERRE ZEC timeout bruto -0.05% neto -0.55%
- 2026-09-29 23:50 [ruptura_volumen_tope] CIERRE ZEC timeout bruto -0.05% neto -1.15%
- 2026-09-29 23:50 [ruptura_volumen_evento] CIERRE ZEC timeout bruto -0.05% neto -0.55%
- 2026-09-29 23:45 [reversion_bb] ENTRADA NEAR @ 4.2874 (22.95 €, apertura)
- 2026-09-29 23:50 [macd_momentum] CIERRE PUMP momentum perdido bruto -0.67% neto -1.17%
- 2026-09-29 23:50 [macd_momentum_evento] CIERRE PUMP momentum perdido bruto -0.67% neto -1.17%
- 2026-09-29 23:45 [reversion_bb] ENTRADA ENA @ 0.2184 (22.95 €, apertura)
- 2026-09-29 23:45 [reversion_bb] ENTRADA MON @ 0.02354 (22.95 €, apertura)
- 2026-09-29 23:45 [reversion_bb] ENTRADA INJ @ 6.689 (22.95 €, apertura)
- 2026-09-29 23:50 [macd_momentum] CIERRE ATOM momentum perdido bruto -0.39% neto -0.89%
- 2026-09-29 23:50 [macd_momentum_regimen] CIERRE ATOM momentum perdido bruto -0.39% neto -0.89%
- 2026-09-29 23:50 [macd_momentum_evento] CIERRE ATOM momentum perdido bruto -0.39% neto -0.89%
- 2026-09-29 23:45 [reversion_bb] ENTRADA RENDER @ 1.679 (22.95 €, apertura)
- 2026-09-29 23:45 [reversion_bb] ENTRADA TON @ 1.304 (22.95 €, apertura)
- 2026-09-29 23:50 [macd_momentum] CIERRE POL momentum perdido bruto -0.75% neto -1.25%
- 2026-09-29 23:50 [ruptura_estricta] CIERRE POL timeout bruto -1.11% neto -1.61%
- 2026-09-29 23:50 [macd_momentum_regimen] CIERRE POL momentum perdido bruto -0.75% neto -1.25%
- 2026-09-29 23:50 [macd_momentum_evento] CIERRE POL momentum perdido bruto -0.75% neto -1.25%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
