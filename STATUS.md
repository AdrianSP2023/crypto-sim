# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 03:11 UTC · vueltas 185 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.90 € (-2.85%) | 110 | 15 | 27% | -0.264% | -1.002% | -1.138% | -25.26 € |
| reversion_bb | 918.33 € (-0.64%) | 29 | 6 | 48% | +0.205% | -0.895% | -0.997% | -5.98 € |
| ruptura_volumen | 894.85 € (-3.18%) | 139 | 12 | 22% | -0.207% | -0.895% | -1.025% | -28.38 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.19 € (-2.06%) | 105 | 4 | 26% | -0.039% | -0.787% | -0.914% | -18.95 € |
| macd_momentum | 882.04 € (-4.57%) | 264 | 3 | 17% | -0.106% | -0.705% | -0.817% | -42.19 € |
| estocastico_rebote | 892.84 € (-3.40%) | 182 | 17 | 35% | -0.093% | -0.737% | -0.870% | -30.66 € |
| ruptura_estricta | 904.63 € (-2.12%) | 65 | 4 | 25% | -0.348% | -1.249% | -1.393% | -18.63 € |
| macd_sin_salida | 895.79 € (-3.08%) | 152 | 19 | 30% | -0.114% | -0.786% | -0.911% | -27.30 € |
| c_banda_atr_tope | 910.25 € (-1.51%) | 36 | 4 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.74 € (-1.46%) | 50 | 4 | 18% | -0.106% | -1.134% | -1.258% | -13.03 € |
| c_banda_atr_regimen | 900.66 € (-2.55%) | 76 | 2 | 22% | -0.477% | -1.320% | -1.449% | -23.02 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 900.31 € (-2.59%) | 106 | 10 | 20% | -0.219% | -0.965% | -1.100% | -23.40 € |
| c_banda_atr_evento | 900.96 € (-2.52%) | 78 | 15 | 23% | -0.402% | -1.240% | -1.379% | -22.20 € |
| macd_momentum_evento | 894.44 € (-3.22%) | 144 | 3 | 13% | -0.223% | -0.906% | -1.014% | -29.79 € |
| ruptura_volumen_evento | 900.36 € (-2.58%) | 80 | 12 | 14% | -0.418% | -1.248% | -1.381% | -22.86 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 03:10 | ruptura_volumen_evento | TRUMP | timeout | -0.17% | -0.67% | -0.15 |
| 2026-09-30 03:10 | ruptura_volumen_evento | TAO | timeout | -0.28% | -0.79% | -0.18 |
| 2026-09-30 03:10 | macd_momentum_evento | FIL | momentum perdido | -0.53% | -1.03% | -0.23 |
| 2026-09-30 03:10 | macd_momentum_evento | ENA | momentum perdido | -1.40% | -1.90% | -0.43 |
| 2026-09-30 03:10 | macd_momentum_evento | DOT | momentum perdido | -0.11% | -0.61% | -0.14 |
| 2026-09-30 03:10 | c_banda_atr_evento | SEI | timeout | -0.72% | -1.22% | -0.28 |
| 2026-09-30 03:10 | c_banda_atr_evento | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 03:10 | c_banda_atr_evento | RENDER | timeout | +0.47% | -0.03% | -0.01 |
| 2026-09-30 03:10 | c_banda_atr_evento | DOT | timeout | +0.36% | -0.14% | -0.03 |
| 2026-09-30 03:10 | c_banda_atr_evento | DOGE | timeout | -0.85% | -1.35% | -0.31 |
| 2026-09-30 03:10 | c_banda_atr_evento | SUI | timeout | +0.00% | -0.50% | -0.11 |
| 2026-09-30 03:10 | c_banda_atr_regimen | SEI | timeout | -0.72% | -1.22% | -0.28 |
| 2026-09-30 03:10 | c_banda_atr_regimen | RENDER | timeout | +0.47% | -0.03% | -0.01 |
| 2026-09-30 03:10 | c_banda_atr_regimen | BCH | timeout | -0.99% | -1.49% | -0.34 |
| 2026-09-30 03:10 | c_banda_atr_regimen | DOT | timeout | +0.36% | -0.14% | -0.03 |

## Eventos de la última vuelta

- 2026-09-30 03:10 [c_banda_atr] CIERRE SUI timeout bruto +0.00% neto -0.50%
- 2026-09-30 03:10 [c_banda_atr_regimen] CIERRE SUI timeout bruto +0.00% neto -0.50%
- 2026-09-30 03:10 [c_banda_atr_evento] CIERRE SUI timeout bruto +0.00% neto -0.50%
- 2026-09-30 03:10 [ruptura_volumen] CIERRE TAO timeout bruto -0.28% neto -0.78%
- 2026-09-30 03:10 [ruptura_volumen_evento] CIERRE TAO timeout bruto -0.28% neto -0.78%
- 2026-09-30 03:10 [c_banda_atr] CIERRE DOGE timeout bruto -0.85% neto -1.35%
- 2026-09-30 03:10 [c_banda_atr_regimen] CIERRE DOGE timeout bruto -0.85% neto -1.35%
- 2026-09-30 03:10 [c_banda_atr_evento] CIERRE DOGE timeout bruto -0.85% neto -1.35%
- 2026-09-30 03:10 [c_banda_atr] CIERRE DOT timeout bruto +0.36% neto -0.14%
- 2026-09-30 03:10 [macd_momentum] CIERRE DOT momentum perdido bruto -0.11% neto -0.61%
- 2026-09-30 03:10 [c_banda_atr_regimen] CIERRE DOT timeout bruto +0.36% neto -0.14%
- 2026-09-30 03:10 [c_banda_atr_evento] CIERRE DOT timeout bruto +0.36% neto -0.14%
- 2026-09-30 03:10 [macd_momentum_evento] CIERRE DOT momentum perdido bruto -0.11% neto -0.61%
- 2026-09-30 03:10 [macd_momentum] CIERRE ENA momentum perdido bruto -1.40% neto -1.90%
- 2026-09-30 03:10 [ruptura_volumen_tope] CIERRE ENA stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 03:10 [macd_momentum_evento] CIERRE ENA momentum perdido bruto -1.40% neto -1.90%
- 2026-09-30 03:10 [c_banda_atr_regimen] CIERRE BCH timeout bruto -0.99% neto -1.49%
- 2026-09-30 03:10 [c_banda_atr] CIERRE RENDER timeout bruto +0.47% neto -0.03%
- 2026-09-30 03:10 [c_banda_atr_regimen] CIERRE RENDER timeout bruto +0.47% neto -0.03%
- 2026-09-30 03:10 [c_banda_atr_evento] CIERRE RENDER timeout bruto +0.47% neto -0.03%
- 2026-09-30 03:10 [c_banda_atr] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-30 03:05 [macd_momentum] ENTRADA ZRO @ 1.575 (22.06 €, apertura)
- 2026-09-30 03:05 [macd_sin_salida] ENTRADA ZRO @ 1.575 (22.42 €, apertura)
- 2026-09-30 03:10 [c_banda_atr_tope] CIERRE ZRO take-profit bruto +2.00% neto +0.90%
- 2026-09-30 03:10 [c_banda_atr_evento] CIERRE ZRO take-profit bruto +2.00% neto +1.50%
- 2026-09-30 03:05 [macd_momentum_evento] ENTRADA ZRO @ 1.575 (22.37 €, apertura)
- 2026-09-30 03:10 [c_banda_atr] CIERRE SEI timeout bruto -0.72% neto -1.22%
- 2026-09-30 03:10 [c_banda_atr_regimen] CIERRE SEI timeout bruto -0.72% neto -1.22%
- 2026-09-30 03:10 [c_banda_atr_evento] CIERRE SEI timeout bruto -0.72% neto -1.22%
- 2026-09-30 03:10 [macd_momentum] CIERRE FIL momentum perdido bruto -0.53% neto -1.03%
- 2026-09-30 03:10 [macd_momentum_evento] CIERRE FIL momentum perdido bruto -0.53% neto -1.03%
- 2026-09-30 03:10 [ruptura_volumen] CIERRE TRUMP timeout bruto -0.16% neto -0.66%
- 2026-09-30 03:10 [ruptura_volumen_evento] CIERRE TRUMP timeout bruto -0.16% neto -0.66%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
