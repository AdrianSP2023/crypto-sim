# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 13:56 UTC · vueltas 52 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 921.21 € (-0.33%) | 21 | 17 | 52% | +0.442% | -0.658% | -0.794% | -3.19 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 915.78 € (-0.92%) | 50 | 7 | 30% | +0.166% | -0.838% | -0.971% | -9.66 € |
| rebote_extremo | 924.58 € (+0.04%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 916.57 € (-0.83%) | 38 | 8 | 34% | +0.280% | -0.820% | -0.925% | -7.19 € |
| macd_momentum | 908.50 € (-1.70%) | 106 | 4 | 20% | +0.059% | -0.687% | -0.800% | -16.76 € |
| estocastico_rebote | 923.60 € (-0.07%) | 42 | 28 | 64% | +0.913% | -0.066% | -0.184% | -0.63 € |
| ruptura_estricta | 921.44 € (-0.30%) | 23 | 13 | 39% | +0.434% | -0.666% | -0.800% | -3.54 € |
| macd_sin_salida | 917.70 € (-0.71%) | 51 | 19 | 39% | +0.333% | -0.631% | -0.753% | -7.40 € |
| c_banda_atr_tope | 922.26 € (-0.21%) | 8 | 2 | 38% | +0.019% | -1.081% | -1.255% | -2.00 € |
| ruptura_volumen_tope | 922.61 € (-0.18%) | 13 | 4 | 23% | +0.215% | -0.885% | -1.016% | -2.66 € |
| c_banda_atr_regimen | 921.21 € (-0.33%) | 21 | 17 | 52% | +0.442% | -0.658% | -0.794% | -3.19 € |
| macd_momentum_regimen | 908.50 € (-1.70%) | 106 | 4 | 20% | +0.059% | -0.687% | -0.800% | -16.76 € |
| ruptura_volumen_regimen | 915.78 € (-0.92%) | 50 | 7 | 30% | +0.166% | -0.838% | -0.971% | -9.66 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 13:55 | ruptura_volumen_regimen | SPX | timeout | +0.08% | -0.72% | -0.17 |
| 2026-09-29 13:55 | ruptura_volumen_regimen | SOL | timeout | +1.20% | +0.40% | +0.09 |
| 2026-09-29 13:55 | ruptura_volumen_regimen | ETH | timeout | +0.07% | -0.73% | -0.17 |
| 2026-09-29 13:55 | macd_momentum_regimen | USELESS | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 13:55 | macd_momentum_regimen | XDC | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 13:55 | c_banda_atr_regimen | USELESS | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 13:55 | c_banda_atr_regimen | WLD | timeout | -0.86% | -1.96% | -0.45 |
| 2026-09-29 13:55 | c_banda_atr_regimen | PUMP | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 13:55 | c_banda_atr_tope | USELESS | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-29 13:55 | c_banda_atr_tope | PUMP | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 13:55 | macd_sin_salida | USELESS | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 13:55 | macd_sin_salida | XDC | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 13:55 | ruptura_estricta | USELESS | take-profit | +3.00% | +1.90% | +0.44 |
| 2026-09-29 13:55 | ruptura_estricta | NEAR | take-profit | +3.00% | +1.90% | +0.44 |
| 2026-09-29 13:55 | estocastico_rebote | FIL | timeout | +0.32% | -0.48% | -0.11 |

## Eventos de la última vuelta

- 2026-09-29 13:55 [ruptura_volumen] CIERRE ETH timeout bruto +0.07% neto -0.73%
- 2026-09-29 13:55 [ruptura_volumen_regimen] CIERRE ETH timeout bruto +0.07% neto -0.73%
- 2026-09-29 13:55 [ruptura_volumen] CIERRE SOL timeout bruto +1.20% neto +0.40%
- 2026-09-29 13:55 [estocastico_rebote] CIERRE SOL take-profit bruto +1.80% neto +1.00%
- 2026-09-29 13:55 [ruptura_volumen_regimen] CIERRE SOL timeout bruto +1.20% neto +0.40%
- 2026-09-29 13:50 [ruptura_volumen] ENTRADA NEAR @ 4.3546 (22.87 €, apertura)
- 2026-09-29 13:50 [macd_momentum] ENTRADA NEAR @ 4.3546 (22.69 €, apertura)
- 2026-09-29 13:55 [ruptura_estricta] CIERRE NEAR take-profit bruto +3.00% neto +1.90%
- 2026-09-29 13:50 [macd_sin_salida] ENTRADA NEAR @ 4.3546 (22.92 €, apertura)
- 2026-09-29 13:50 [ruptura_volumen_tope] ENTRADA NEAR @ 4.3546 (23.04 €, apertura)
- 2026-09-29 13:50 [macd_momentum_regimen] ENTRADA NEAR @ 4.3546 (22.69 €, apertura)
- 2026-09-29 13:50 [ruptura_volumen_regimen] ENTRADA NEAR @ 4.3546 (22.87 €, apertura)
- 2026-09-29 13:50 [estocastico_rebote] ENTRADA SUI @ 1.0223 (23.10 €, apertura)
- 2026-09-29 13:55 [c_banda_atr] CIERRE PUMP stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 13:55 [c_banda_atr_tope] CIERRE PUMP stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 13:55 [c_banda_atr_regimen] CIERRE PUMP stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 13:55 [estocastico_rebote] CIERRE HYPE timeout bruto +0.03% neto -0.77%
- 2026-09-29 13:55 [macd_momentum] CIERRE XDC stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 13:55 [macd_sin_salida] CIERRE XDC stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 13:55 [macd_momentum_regimen] CIERRE XDC stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 13:55 [estocastico_rebote] CIERRE DOGE timeout bruto +1.05% neto +0.25%
- 2026-09-29 13:50 [estocastico_rebote] ENTRADA MON @ 0.02526 (23.10 €, apertura)
- 2026-09-29 13:55 [estocastico_rebote] CIERRE BCH timeout bruto -0.11% neto -0.91%
- 2026-09-29 13:50 [estocastico_rebote] ENTRADA ATOM @ 1.5452 (23.09 €, apertura)
- 2026-09-29 13:55 [c_banda_atr] CIERRE WLD timeout bruto -0.86% neto -1.96%
- 2026-09-29 13:55 [c_banda_atr_regimen] CIERRE WLD timeout bruto -0.86% neto -1.96%
- 2026-09-29 13:55 [c_banda_atr] CIERRE USELESS take-profit bruto +2.00% neto +0.90%
- 2026-09-29 13:55 [macd_momentum] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-09-29 13:55 [ruptura_estricta] CIERRE USELESS take-profit bruto +3.00% neto +1.90%
- 2026-09-29 13:55 [macd_sin_salida] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-09-29 13:55 [c_banda_atr_tope] CIERRE USELESS take-profit bruto +2.00% neto +0.90%
- 2026-09-29 13:55 [c_banda_atr_regimen] CIERRE USELESS take-profit bruto +2.00% neto +0.90%
- 2026-09-29 13:55 [macd_momentum_regimen] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-09-29 13:55 [estocastico_rebote] CIERRE FIL timeout bruto +0.32% neto -0.48%
- 2026-09-29 13:55 [ruptura_volumen] CIERRE SPX timeout bruto +0.08% neto -0.72%
- 2026-09-29 13:55 [ruptura_volumen_regimen] CIERRE SPX timeout bruto +0.08% neto -0.72%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
