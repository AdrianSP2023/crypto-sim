# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 03:06 UTC · vueltas 184 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.15 € (-2.71%) | 104 | 21 | 28% | -0.292% | -1.043% | -1.183% | -24.86 € |
| reversion_bb | 918.50 € (-0.62%) | 29 | 6 | 48% | +0.205% | -0.895% | -0.997% | -5.98 € |
| ruptura_volumen | 895.49 € (-3.11%) | 137 | 14 | 22% | -0.207% | -0.897% | -1.028% | -28.05 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.55 € (-2.02%) | 105 | 4 | 26% | -0.039% | -0.787% | -0.914% | -18.95 € |
| macd_momentum | 882.46 € (-4.52%) | 261 | 5 | 17% | -0.100% | -0.700% | -0.812% | -41.41 € |
| estocastico_rebote | 892.73 € (-3.41%) | 182 | 17 | 35% | -0.093% | -0.737% | -0.870% | -30.66 € |
| ruptura_estricta | 904.87 € (-2.10%) | 65 | 4 | 25% | -0.348% | -1.249% | -1.393% | -18.63 € |
| macd_sin_salida | 896.11 € (-3.04%) | 152 | 18 | 30% | -0.114% | -0.786% | -0.911% | -27.30 € |
| c_banda_atr_tope | 910.56 € (-1.48%) | 35 | 5 | 17% | -0.565% | -1.665% | -1.801% | -13.39 € |
| ruptura_volumen_tope | 911.12 € (-1.42%) | 49 | 5 | 18% | -0.084% | -1.123% | -1.247% | -12.65 € |
| c_banda_atr_regimen | 901.52 € (-2.46%) | 70 | 8 | 24% | -0.493% | -1.366% | -1.501% | -21.94 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 900.44 € (-2.58%) | 106 | 10 | 20% | -0.219% | -0.965% | -1.100% | -23.40 € |
| c_banda_atr_evento | 902.22 € (-2.38%) | 72 | 21 | 24% | -0.452% | -1.319% | -1.464% | -21.80 € |
| macd_momentum_evento | 894.87 € (-3.18%) | 141 | 5 | 13% | -0.213% | -0.900% | -1.009% | -28.99 € |
| ruptura_volumen_evento | 901.00 € (-2.51%) | 78 | 14 | 14% | -0.423% | -1.261% | -1.396% | -22.53 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 03:05 | ruptura_volumen_evento | ATOM | timeout | -0.89% | -1.39% | -0.31 |
| 2026-09-30 03:05 | macd_momentum_evento | ADA | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-09-30 03:05 | ruptura_estricta | WLD | stop-loss | -2.00% | -2.50% | -0.57 |
| 2026-09-30 03:05 | estocastico_rebote | PENGU | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 03:05 | estocastico_rebote | ZRO | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 03:05 | estocastico_rebote | ZEC | timeout | -0.98% | -1.48% | -0.33 |
| 2026-09-30 03:05 | macd_momentum | ADA | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-09-30 03:05 | pullback_tendencia | SUI | rotura de tendencia | -0.36% | -0.86% | -0.20 |
| 2026-09-30 03:05 | ruptura_volumen | ATOM | timeout | -0.89% | -1.39% | -0.31 |
| 2026-09-30 03:00 | macd_momentum_evento | HBAR | momentum perdido | -0.41% | -0.91% | -0.20 |
| 2026-09-30 03:00 | c_banda_atr_evento | WLD | stop-loss | -1.52% | -2.02% | -0.46 |
| 2026-09-30 03:00 | c_banda_atr_regimen | WLD | stop-loss | -1.52% | -2.02% | -0.46 |
| 2026-09-30 03:00 | ruptura_estricta | PENGU | stop-loss | -2.00% | -2.50% | -0.57 |
| 2026-09-30 03:00 | macd_momentum | HBAR | momentum perdido | -0.41% | -0.91% | -0.20 |
| 2026-09-30 03:00 | c_banda_atr | WLD | stop-loss | -1.52% | -2.02% | -0.46 |

## Eventos de la última vuelta

- 2026-09-30 03:05 [estocastico_rebote] CIERRE ZEC timeout bruto -0.98% neto -1.48%
- 2026-09-30 03:05 [macd_momentum] CIERRE ADA momentum perdido bruto -0.17% neto -0.67%
- 2026-09-30 03:05 [macd_momentum_evento] CIERRE ADA momentum perdido bruto -0.17% neto -0.67%
- 2026-09-30 03:05 [pullback_tendencia] CIERRE SUI rotura de tendencia bruto -0.36% neto -0.86%
- 2026-09-30 03:00 [estocastico_rebote] ENTRADA PUMP @ 0.005169 (22.34 €, apertura)
- 2026-09-30 03:00 [macd_momentum] ENTRADA DOT @ 1.0664 (22.07 €, apertura)
- 2026-09-30 03:00 [macd_sin_salida] ENTRADA DOT @ 1.0664 (22.42 €, apertura)
- 2026-09-30 03:00 [macd_momentum_evento] ENTRADA DOT @ 1.0664 (22.38 €, apertura)
- 2026-09-30 03:05 [ruptura_volumen] CIERRE ATOM timeout bruto -0.89% neto -1.39%
- 2026-09-30 03:05 [ruptura_volumen_evento] CIERRE ATOM timeout bruto -0.89% neto -1.39%
- 2026-09-30 03:05 [ruptura_estricta] CIERRE WLD stop-loss bruto -2.00% neto -2.50%
- 2026-09-30 03:05 [estocastico_rebote] CIERRE ZRO take-profit bruto +1.80% neto +1.30%
- 2026-09-30 03:05 [estocastico_rebote] CIERRE PENGU stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
