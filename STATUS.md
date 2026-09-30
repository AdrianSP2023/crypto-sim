# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 01:11 UTC · vueltas 186 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.89 € (-2.31%) | 90 | 27 | 27% | -0.374% | -1.164% | -1.308% | -24.02 € |
| reversion_bb | 919.64 € (-0.50%) | 23 | 11 | 43% | +0.007% | -1.093% | -1.192% | -5.80 € |
| ruptura_volumen | 900.34 € (-2.59%) | 122 | 9 | 22% | -0.164% | -0.878% | -1.004% | -24.50 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.29 € (-2.05%) | 94 | 4 | 23% | -0.131% | -0.909% | -1.029% | -19.57 € |
| macd_momentum | 885.79 € (-4.16%) | 234 | 20 | 16% | -0.157% | -0.769% | -0.880% | -40.79 € |
| estocastico_rebote | 894.19 € (-3.25%) | 174 | 10 | 33% | -0.144% | -0.794% | -0.924% | -31.56 € |
| ruptura_estricta | 909.42 € (-1.60%) | 53 | 7 | 26% | -0.257% | -1.249% | -1.386% | -15.22 € |
| macd_sin_salida | 898.17 € (-2.82%) | 145 | 17 | 28% | -0.164% | -0.844% | -0.967% | -27.95 € |
| c_banda_atr_tope | 912.74 € (-1.24%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.53 € (-1.16%) | 42 | 5 | 17% | -0.071% | -1.171% | -1.288% | -11.31 € |
| c_banda_atr_regimen | 902.50 € (-2.35%) | 68 | 8 | 24% | -0.518% | -1.401% | -1.535% | -21.87 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.53 € (-2.24%) | 98 | 2 | 21% | -0.150% | -0.917% | -1.045% | -20.58 € |
| c_banda_atr_evento | 906.46 € (-1.92%) | 58 | 27 | 21% | -0.618% | -1.537% | -1.690% | -20.47 € |
| macd_momentum_evento | 898.24 € (-2.81%) | 114 | 20 | 10% | -0.358% | -1.089% | -1.197% | -28.37 € |
| ruptura_volumen_evento | 905.88 € (-1.99%) | 63 | 9 | 13% | -0.392% | -1.311% | -1.438% | -18.96 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 01:10 | ruptura_volumen_evento | SHIB | timeout | +0.06% | -0.44% | -0.10 |
| 2026-09-30 01:10 | ruptura_volumen_evento | BTC | timeout | -0.35% | -0.85% | -0.19 |
| 2026-09-30 01:10 | macd_momentum_evento | ASTER | take-profit | +2.18% | +1.68% | +0.38 |
| 2026-09-30 01:10 | macd_momentum_evento | USELESS | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:10 | ruptura_volumen_regimen | SHIB | timeout | +0.06% | -0.44% | -0.10 |
| 2026-09-30 01:10 | ruptura_volumen_regimen | BTC | timeout | -0.35% | -0.85% | -0.19 |
| 2026-09-30 01:10 | ruptura_volumen_tope | BTC | timeout | -0.35% | -1.45% | -0.33 |
| 2026-09-30 01:10 | macd_sin_salida | BNB | timeout | +0.20% | -0.30% | -0.07 |
| 2026-09-30 01:10 | macd_sin_salida | PENGU | timeout | +1.41% | +0.91% | +0.20 |
| 2026-09-30 01:10 | macd_sin_salida | USELESS | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:10 | macd_momentum | ASTER | take-profit | +2.18% | +1.68% | +0.37 |
| 2026-09-30 01:10 | macd_momentum | USELESS | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 01:10 | ruptura_volumen | SHIB | timeout | +0.06% | -0.44% | -0.10 |
| 2026-09-30 01:10 | ruptura_volumen | BTC | timeout | -0.35% | -0.85% | -0.19 |
| 2026-09-30 01:10 | reversion_bb | INJ | take-profit | +2.12% | +1.02% | +0.23 |

## Eventos de la última vuelta

- 2026-09-30 01:10 [ruptura_volumen] CIERRE BTC timeout bruto -0.35% neto -0.85%
- 2026-09-30 01:10 [ruptura_volumen_tope] CIERRE BTC timeout bruto -0.35% neto -1.45%
- 2026-09-30 01:10 [ruptura_volumen_regimen] CIERRE BTC timeout bruto -0.35% neto -0.85%
- 2026-09-30 01:10 [ruptura_volumen_evento] CIERRE BTC timeout bruto -0.35% neto -0.85%
- 2026-09-30 01:05 [macd_momentum] ENTRADA SUI @ 1.0196 (22.07 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA SUI @ 1.0196 (22.40 €, apertura)
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA SUI @ 1.0196 (22.38 €, apertura)
- 2026-09-30 01:05 [macd_momentum] ENTRADA AVAX @ 10.087 (22.07 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA AVAX @ 10.087 (22.40 €, apertura)
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA AVAX @ 10.087 (22.38 €, apertura)
- 2026-09-30 01:05 [macd_momentum] ENTRADA PUMP @ 0.005187 (22.07 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA PUMP @ 0.005187 (22.40 €, apertura)
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA PUMP @ 0.005187 (22.38 €, apertura)
- 2026-09-30 01:10 [reversion_bb] CIERRE ALGO take-profit bruto +1.50% neto +0.40%
- 2026-09-30 01:05 [ruptura_volumen] ENTRADA ALGO @ 0.11196 (22.50 €, apertura)
- 2026-09-30 01:05 [ruptura_estricta] ENTRADA ALGO @ 0.11196 (22.73 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen_tope] ENTRADA ALGO @ 0.11196 (22.82 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen_evento] ENTRADA ALGO @ 0.11196 (22.63 €, apertura)
- 2026-09-30 01:05 [c_banda_atr] ENTRADA TAO @ 266.461 (22.51 €, apertura)
- 2026-09-30 01:05 [c_banda_atr_evento] ENTRADA TAO @ 266.461 (22.59 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen] ENTRADA ICP @ 3.077 (22.50 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen_tope] ENTRADA ICP @ 3.077 (22.82 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen_evento] ENTRADA ICP @ 3.077 (22.63 €, apertura)
- 2026-09-30 01:10 [reversion_bb] CIERRE INJ take-profit bruto +2.12% neto +1.02%
- 2026-09-30 01:05 [c_banda_atr] ENTRADA ATOM @ 1.5302 (22.51 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen] ENTRADA ATOM @ 1.5302 (22.50 €, apertura)
- 2026-09-30 01:05 [macd_momentum] ENTRADA ATOM @ 1.5302 (22.07 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA ATOM @ 1.5302 (22.40 €, apertura)
- 2026-09-30 01:05 [c_banda_atr_evento] ENTRADA ATOM @ 1.5302 (22.59 €, apertura)
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA ATOM @ 1.5302 (22.38 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen_evento] ENTRADA ATOM @ 1.5302 (22.63 €, apertura)
- 2026-09-30 01:05 [macd_momentum] ENTRADA PEPE @ 3.767e-06 (22.07 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA PEPE @ 3.767e-06 (22.40 €, apertura)
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA PEPE @ 3.767e-06 (22.38 €, apertura)
- 2026-09-30 01:05 [ruptura_volumen] ENTRADA USELESS @ 0.21587 (22.50 €, apertura)
- 2026-09-30 01:10 [macd_momentum] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:05 [ruptura_estricta] ENTRADA USELESS @ 0.21587 (22.73 €, apertura)
- 2026-09-30 01:10 [macd_sin_salida] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:10 [macd_momentum_evento] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:05 [ruptura_volumen_evento] ENTRADA USELESS @ 0.21587 (22.63 €, apertura)
- 2026-09-30 01:05 [macd_momentum] ENTRADA RAY @ 1.69 (22.08 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA RAY @ 1.69 (22.40 €, apertura)
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA RAY @ 1.69 (22.39 €, apertura)
- 2026-09-30 01:10 [ruptura_volumen] CIERRE SHIB timeout bruto +0.06% neto -0.44%
- 2026-09-30 01:05 [macd_momentum] ENTRADA SHIB @ 5.102e-06 (22.08 €, apertura)
- 2026-09-30 01:05 [macd_sin_salida] ENTRADA SHIB @ 5.102e-06 (22.40 €, apertura)
- 2026-09-30 01:10 [ruptura_volumen_regimen] CIERRE SHIB timeout bruto +0.06% neto -0.44%
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA SHIB @ 5.102e-06 (22.39 €, apertura)
- 2026-09-30 01:10 [ruptura_volumen_evento] CIERRE SHIB timeout bruto +0.06% neto -0.44%
- 2026-09-30 01:10 [macd_sin_salida] CIERRE PENGU timeout bruto +1.41% neto +0.91%
- 2026-09-30 01:05 [macd_momentum] ENTRADA BNB @ 670.3 (22.08 €, apertura)
- 2026-09-30 01:10 [macd_sin_salida] CIERRE BNB timeout bruto +0.20% neto -0.30%
- 2026-09-30 01:05 [macd_momentum_evento] ENTRADA BNB @ 670.3 (22.39 €, apertura)
- 2026-09-30 01:10 [macd_momentum] CIERRE ASTER take-profit bruto +2.18% neto +1.68%
- 2026-09-30 01:10 [macd_momentum_evento] CIERRE ASTER take-profit bruto +2.18% neto +1.68%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
