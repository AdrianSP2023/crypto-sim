# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 17:31 UTC · vueltas 277 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.53 € (-3.54%) | 225 | 24 | 33% | -0.096% | -0.712% | -0.836% | -36.45 € |
| reversion_bb | 916.90 € (-0.79%) | 44 | 4 | 48% | +0.266% | -0.800% | -0.897% | -8.11 € |
| ruptura_volumen | 879.38 € (-4.85%) | 255 | 16 | 24% | -0.203% | -0.805% | -0.914% | -46.46 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 893.32 € (-3.35%) | 156 | 5 | 14% | -0.239% | -0.908% | -1.005% | -32.22 € |
| macd_momentum | 874.93 € (-5.34%) | 391 | 35 | 20% | -0.032% | -0.599% | -0.706% | -52.66 € |
| estocastico_rebote | 877.76 € (-5.03%) | 286 | 7 | 31% | -0.137% | -0.729% | -0.840% | -47.14 € |
| ruptura_estricta | 886.87 € (-4.04%) | 140 | 15 | 23% | -0.546% | -1.235% | -1.356% | -39.39 € |
| macd_sin_salida | 884.74 € (-4.27%) | 274 | 34 | 34% | -0.111% | -0.706% | -0.821% | -43.96 € |
| c_banda_atr_tope | 912.12 € (-1.31%) | 52 | 5 | 27% | -0.078% | -1.085% | -1.200% | -12.96 € |
| ruptura_volumen_tope | 909.13 € (-1.63%) | 87 | 5 | 29% | +0.028% | -0.775% | -0.891% | -15.48 € |
| c_banda_atr_regimen | 902.55 € (-2.35%) | 110 | 11 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.46 € (-3.33%) | 208 | 18 | 22% | -0.023% | -0.648% | -0.761% | -30.74 € |
| ruptura_volumen_regimen | 882.67 € (-4.50%) | 190 | 13 | 19% | -0.347% | -0.985% | -1.101% | -42.43 € |
| c_banda_atr_evento | 897.46 € (-2.90%) | 192 | 24 | 34% | -0.059% | -0.697% | -0.815% | -30.53 € |
| macd_momentum_evento | 879.78 € (-4.81%) | 344 | 35 | 18% | -0.040% | -0.617% | -0.720% | -47.83 € |
| ruptura_volumen_evento | 891.89 € (-3.50%) | 205 | 16 | 25% | -0.100% | -0.729% | -0.827% | -33.96 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 17:30 | ruptura_volumen_evento | XMR | timeout | +2.17% | +1.67% | +0.37 |
| 2026-10-01 17:30 | ruptura_volumen_evento | MON | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 17:30 | macd_momentum_evento | USELESS | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 17:30 | c_banda_atr_evento | USELESS | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 17:30 | ruptura_volumen_tope | XMR | timeout | +2.17% | +1.67% | +0.38 |
| 2026-10-01 17:30 | ruptura_volumen_tope | MON | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 17:30 | macd_sin_salida | USELESS | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 17:30 | ruptura_estricta | TAO | timeout | +0.10% | -0.40% | -0.09 |
| 2026-10-01 17:30 | macd_momentum | USELESS | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 17:30 | ruptura_volumen | XMR | timeout | +2.17% | +1.67% | +0.37 |
| 2026-10-01 17:30 | ruptura_volumen | MON | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-01 17:30 | reversion_bb | RENDER | take-profit | +1.50% | +0.70% | +0.16 |
| 2026-10-01 17:30 | reversion_bb | ZEC | take-profit | +1.50% | +0.70% | +0.16 |
| 2026-10-01 17:30 | c_banda_atr | USELESS | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 17:25 | c_banda_atr_evento | SUI | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-10-01 17:25 [macd_momentum] ENTRADA LINK @ 12.7497 (21.78 €, apertura)
- 2026-10-01 17:25 [macd_momentum_regimen] ENTRADA LINK @ 12.7497 (22.34 €, apertura)
- 2026-10-01 17:25 [macd_momentum_evento] ENTRADA LINK @ 12.7497 (21.90 €, apertura)
- 2026-10-01 17:25 [c_banda_atr] ENTRADA AAVE @ 149.72 (22.19 €, apertura)
- 2026-10-01 17:25 [c_banda_atr_regimen] ENTRADA AAVE @ 149.72 (22.55 €, apertura)
- 2026-10-01 17:25 [c_banda_atr_evento] ENTRADA AAVE @ 149.72 (22.33 €, apertura)
- 2026-10-01 17:30 [reversion_bb] CIERRE ZEC take-profit bruto +1.50% neto +0.70%
- 2026-10-01 17:25 [macd_momentum] ENTRADA PUMP @ 0.004999 (21.78 €, apertura)
- 2026-10-01 17:25 [macd_sin_salida] ENTRADA PUMP @ 0.004999 (22.00 €, apertura)
- 2026-10-01 17:25 [macd_momentum_regimen] ENTRADA PUMP @ 0.004999 (22.34 €, apertura)
- 2026-10-01 17:25 [macd_momentum_evento] ENTRADA PUMP @ 0.004999 (21.90 €, apertura)
- 2026-10-01 17:30 [ruptura_estricta] CIERRE TAO timeout bruto +0.10% neto -0.40%
- 2026-10-01 17:25 [macd_momentum] ENTRADA UNI @ 8.1023 (21.78 €, apertura)
- 2026-10-01 17:25 [macd_momentum_regimen] ENTRADA UNI @ 8.1023 (22.34 €, apertura)
- 2026-10-01 17:25 [macd_momentum_evento] ENTRADA UNI @ 8.1023 (21.90 €, apertura)
- 2026-10-01 17:25 [macd_momentum] ENTRADA ZRO @ 1.574 (21.78 €, apertura)
- 2026-10-01 17:25 [macd_sin_salida] ENTRADA ZRO @ 1.574 (22.00 €, apertura)
- 2026-10-01 17:25 [macd_momentum_regimen] ENTRADA ZRO @ 1.574 (22.34 €, apertura)
- 2026-10-01 17:25 [macd_momentum_evento] ENTRADA ZRO @ 1.574 (21.90 €, apertura)
- 2026-10-01 17:30 [c_banda_atr] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:30 [macd_momentum] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:30 [macd_sin_salida] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:30 [c_banda_atr_evento] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:30 [macd_momentum_evento] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-01 17:25 [macd_momentum] ENTRADA BCH @ 274.14 (21.79 €, apertura)
- 2026-10-01 17:25 [macd_momentum_regimen] ENTRADA BCH @ 274.14 (22.34 €, apertura)
- 2026-10-01 17:25 [macd_momentum_evento] ENTRADA BCH @ 274.14 (21.91 €, apertura)
- 2026-10-01 17:30 [ruptura_volumen] CIERRE MON take-profit bruto +2.50% neto +2.00%
- 2026-10-01 17:30 [ruptura_volumen_tope] CIERRE MON take-profit bruto +2.50% neto +2.00%
- 2026-10-01 17:30 [ruptura_volumen_evento] CIERRE MON take-profit bruto +2.50% neto +2.00%
- 2026-10-01 17:30 [reversion_bb] CIERRE RENDER take-profit bruto +1.50% neto +0.70%
- 2026-10-01 17:25 [ruptura_volumen] ENTRADA WLFI @ 0.0493 (21.94 €, apertura)
- 2026-10-01 17:25 [ruptura_volumen_tope] ENTRADA WLFI @ 0.0493 (22.71 €, apertura)
- 2026-10-01 17:25 [ruptura_volumen_regimen] ENTRADA WLFI @ 0.0493 (22.05 €, apertura)
- 2026-10-01 17:25 [ruptura_volumen_evento] ENTRADA WLFI @ 0.0493 (22.25 €, apertura)
- 2026-10-01 17:25 [ruptura_volumen] ENTRADA TRUMP @ 1.841 (21.94 €, apertura)
- 2026-10-01 17:25 [ruptura_volumen_regimen] ENTRADA TRUMP @ 1.841 (22.05 €, apertura)
- 2026-10-01 17:25 [ruptura_volumen_evento] ENTRADA TRUMP @ 1.841 (22.25 €, apertura)
- 2026-10-01 17:30 [ruptura_volumen] CIERRE XMR timeout bruto +2.17% neto +1.67%
- 2026-10-01 17:30 [ruptura_volumen_tope] CIERRE XMR timeout bruto +2.17% neto +1.67%
- 2026-10-01 17:30 [ruptura_volumen_evento] CIERRE XMR timeout bruto +2.17% neto +1.67%
- 2026-10-01 17:25 [ruptura_volumen] ENTRADA SPX @ 0.3906 (21.94 €, apertura)
- 2026-10-01 17:25 [ruptura_estricta] ENTRADA SPX @ 0.3906 (22.12 €, apertura)
- 2026-10-01 17:25 [ruptura_volumen_tope] ENTRADA SPX @ 0.3906 (22.72 €, apertura)
- 2026-10-01 17:25 [ruptura_volumen_regimen] ENTRADA SPX @ 0.3906 (22.05 €, apertura)
- 2026-10-01 17:25 [ruptura_volumen_evento] ENTRADA SPX @ 0.3906 (22.26 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
