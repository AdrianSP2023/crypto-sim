# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 05:21 UTC · vueltas 135 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.01 € (-1.76%) | 125 | 26 | 35% | +0.047% | -0.662% | -0.780% | -19.05 € |
| reversion_bb | 921.63 € (-0.28%) | 17 | 2 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 892.95 € (-3.39%) | 158 | 32 | 22% | -0.265% | -0.930% | -1.040% | -33.52 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.00 € (-2.30%) | 90 | 11 | 17% | -0.270% | -1.063% | -1.180% | -21.90 € |
| macd_momentum | 896.32 € (-3.02%) | 226 | 27 | 22% | +0.021% | -0.595% | -0.703% | -30.62 € |
| estocastico_rebote | 903.25 € (-2.27%) | 164 | 17 | 39% | +0.095% | -0.564% | -0.684% | -21.30 € |
| ruptura_estricta | 902.54 € (-2.35%) | 78 | 32 | 24% | -0.523% | -1.362% | -1.494% | -24.46 € |
| macd_sin_salida | 907.24 € (-1.84%) | 149 | 35 | 40% | +0.090% | -0.585% | -0.698% | -20.07 € |
| c_banda_atr_tope | 917.83 € (-0.69%) | 29 | 5 | 31% | +0.111% | -0.989% | -1.117% | -6.61 € |
| ruptura_volumen_tope | 914.66 € (-1.04%) | 46 | 5 | 24% | +0.090% | -0.984% | -1.081% | -10.42 € |
| c_banda_atr_regimen | 911.91 € (-1.33%) | 70 | 24 | 34% | -0.040% | -0.913% | -1.051% | -14.73 € |
| macd_momentum_regimen | 905.41 € (-2.04%) | 140 | 27 | 23% | +0.014% | -0.672% | -0.786% | -21.56 € |
| ruptura_volumen_regimen | 893.80 € (-3.29%) | 131 | 32 | 17% | -0.398% | -1.097% | -1.212% | -32.80 € |
| c_banda_atr_evento | 914.06 € (-1.10%) | 92 | 26 | 37% | +0.174% | -0.613% | -0.716% | -13.02 € |
| macd_momentum_evento | 901.28 € (-2.48%) | 179 | 27 | 18% | +0.019% | -0.629% | -0.729% | -25.67 € |
| ruptura_volumen_evento | 905.66 € (-2.01%) | 108 | 32 | 22% | -0.098% | -0.842% | -0.934% | -20.84 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 05:20 | c_banda_atr_evento | JUP | timeout | -0.26% | -0.76% | -0.17 |
| 2026-10-01 05:20 | c_banda_atr_evento | FET | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 05:20 | c_banda_atr_regimen | JUP | timeout | -0.26% | -0.76% | -0.17 |
| 2026-10-01 05:20 | c_banda_atr_regimen | CRV | stop-loss | -1.57% | -2.08% | -0.47 |
| 2026-10-01 05:20 | c_banda_atr_regimen | FET | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 05:20 | estocastico_rebote | BNB | timeout | +0.48% | -0.02% | -0.01 |
| 2026-10-01 05:20 | estocastico_rebote | QNT | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 05:20 | c_banda_atr | JUP | timeout | -0.26% | -0.76% | -0.17 |
| 2026-10-01 05:20 | c_banda_atr | FET | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 05:15 | macd_momentum_evento | DASH | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-10-01 05:15 | macd_momentum_regimen | DASH | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-10-01 05:15 | estocastico_rebote | MON | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 05:15 | estocastico_rebote | ONDO | timeout | +1.23% | +0.73% | +0.17 |
| 2026-10-01 05:15 | macd_momentum | DASH | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-10-01 05:15 | reversion_bb | VVV | take-profit | +1.50% | +0.40% | +0.09 |

## Eventos de la última vuelta

- 2026-10-01 05:20 [estocastico_rebote] CIERRE QNT take-profit bruto +1.80% neto +1.30%
- 2026-10-01 05:15 [ruptura_estricta] ENTRADA ZRO @ 1.536 (22.49 €, apertura)
- 2026-10-01 05:20 [c_banda_atr] CIERRE FET take-profit bruto +2.00% neto +1.50%
- 2026-10-01 05:20 [c_banda_atr_regimen] CIERRE FET take-profit bruto +2.00% neto +1.50%
- 2026-10-01 05:20 [c_banda_atr_evento] CIERRE FET take-profit bruto +2.00% neto +1.50%
- 2026-10-01 05:15 [c_banda_atr] ENTRADA TRX @ 0.29831 (22.63 €, apertura)
- 2026-10-01 05:15 [c_banda_atr_evento] ENTRADA TRX @ 0.29831 (22.78 €, apertura)
- 2026-10-01 05:20 [c_banda_atr_regimen] CIERRE CRV stop-loss bruto -1.57% neto -2.07%
- 2026-10-01 05:20 [c_banda_atr] CIERRE JUP timeout bruto -0.26% neto -0.76%
- 2026-10-01 05:20 [c_banda_atr_regimen] CIERRE JUP timeout bruto -0.26% neto -0.76%
- 2026-10-01 05:20 [c_banda_atr_evento] CIERRE JUP timeout bruto -0.26% neto -0.76%
- 2026-10-01 05:15 [macd_momentum] ENTRADA RENDER @ 1.714 (22.34 €, apertura)
- 2026-10-01 05:15 [macd_sin_salida] ENTRADA RENDER @ 1.714 (22.60 €, apertura)
- 2026-10-01 05:15 [macd_momentum_regimen] ENTRADA RENDER @ 1.714 (22.57 €, apertura)
- 2026-10-01 05:15 [macd_momentum_evento] ENTRADA RENDER @ 1.714 (22.46 €, apertura)
- 2026-10-01 05:15 [estocastico_rebote] ENTRADA SHIB @ 5.129e-06 (22.57 €, apertura)
- 2026-10-01 05:15 [ruptura_volumen] ENTRADA BNB @ 680.05 (22.27 €, apertura)
- 2026-10-01 05:20 [estocastico_rebote] CIERRE BNB timeout bruto +0.48% neto -0.02%
- 2026-10-01 05:15 [ruptura_estricta] ENTRADA BNB @ 680.05 (22.49 €, apertura)
- 2026-10-01 05:15 [ruptura_volumen_regimen] ENTRADA BNB @ 680.05 (22.29 €, apertura)
- 2026-10-01 05:15 [ruptura_volumen_evento] ENTRADA BNB @ 680.05 (22.58 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
