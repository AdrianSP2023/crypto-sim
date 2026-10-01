# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 07:11 UTC · vueltas 156 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.93 € (-1.66%) | 140 | 27 | 40% | +0.162% | -0.524% | -0.641% | -16.92 € |
| reversion_bb | 921.59 € (-0.29%) | 17 | 2 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 890.57 € (-3.64%) | 192 | 11 | 24% | -0.149% | -0.785% | -0.895% | -34.36 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 902.93 € (-2.31%) | 101 | 15 | 18% | -0.202% | -0.963% | -1.074% | -22.27 € |
| macd_momentum | 892.01 € (-3.49%) | 271 | 16 | 23% | +0.063% | -0.533% | -0.639% | -32.88 € |
| estocastico_rebote | 904.23 € (-2.16%) | 177 | 32 | 40% | +0.131% | -0.517% | -0.637% | -21.05 € |
| ruptura_estricta | 901.37 € (-2.47%) | 100 | 20 | 31% | -0.267% | -1.031% | -1.157% | -23.77 € |
| macd_sin_salida | 904.20 € (-2.17%) | 178 | 35 | 43% | +0.150% | -0.497% | -0.607% | -20.35 € |
| c_banda_atr_tope | 917.55 € (-0.72%) | 30 | 5 | 30% | +0.135% | -0.965% | -1.091% | -6.68 € |
| ruptura_volumen_tope | 915.04 € (-1.00%) | 52 | 4 | 31% | +0.206% | -0.802% | -0.909% | -9.60 € |
| c_banda_atr_regimen | 913.16 € (-1.20%) | 83 | 26 | 42% | +0.170% | -0.644% | -0.780% | -12.37 € |
| macd_momentum_regimen | 901.05 € (-2.51%) | 185 | 16 | 24% | +0.078% | -0.563% | -0.672% | -23.83 € |
| ruptura_volumen_regimen | 891.42 € (-3.55%) | 165 | 11 | 22% | -0.232% | -0.890% | -1.004% | -33.50 € |
| c_banda_atr_evento | 914.97 € (-1.00%) | 107 | 27 | 43% | +0.308% | -0.439% | -0.542% | -10.88 € |
| macd_momentum_evento | 896.95 € (-2.95%) | 224 | 16 | 21% | +0.070% | -0.547% | -0.646% | -27.94 € |
| ruptura_volumen_evento | 903.24 € (-2.27%) | 142 | 11 | 26% | +0.019% | -0.667% | -0.763% | -21.69 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 07:10 | macd_momentum_evento | POL | momentum perdido | -0.21% | -0.71% | -0.16 |
| 2026-10-01 07:10 | c_banda_atr_evento | FET | take-profit | +2.12% | +1.62% | +0.37 |
| 2026-10-01 07:10 | macd_momentum_regimen | POL | momentum perdido | -0.21% | -0.71% | -0.16 |
| 2026-10-01 07:10 | c_banda_atr_regimen | FET | take-profit | +2.12% | +1.62% | +0.37 |
| 2026-10-01 07:10 | macd_sin_salida | ENA | stop-loss | -1.60% | -2.10% | -0.48 |
| 2026-10-01 07:10 | estocastico_rebote | FET | take-profit | +2.12% | +1.62% | +0.37 |
| 2026-10-01 07:10 | macd_momentum | POL | momentum perdido | -0.21% | -0.71% | -0.16 |
| 2026-10-01 07:10 | c_banda_atr | FET | take-profit | +2.12% | +1.62% | +0.37 |
| 2026-10-01 07:05 | ruptura_volumen_evento | KSM | timeout | +0.86% | +0.36% | +0.08 |
| 2026-10-01 07:05 | ruptura_volumen_evento | XDC | timeout | +0.67% | +0.17% | +0.04 |
| 2026-10-01 07:05 | macd_momentum_evento | TON | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 07:05 | ruptura_volumen_regimen | KSM | timeout | +0.86% | +0.36% | +0.08 |
| 2026-10-01 07:05 | ruptura_volumen_regimen | XDC | timeout | +0.67% | +0.17% | +0.04 |
| 2026-10-01 07:05 | macd_momentum_regimen | TON | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 07:05 | ruptura_volumen_tope | XDC | timeout | +0.67% | +0.17% | +0.04 |

## Eventos de la última vuelta

- 2026-10-01 07:05 [macd_momentum] ENTRADA AVAX @ 9.853 (22.29 €, apertura)
- 2026-10-01 07:05 [macd_sin_salida] ENTRADA AVAX @ 9.853 (22.61 €, apertura)
- 2026-10-01 07:05 [macd_momentum_regimen] ENTRADA AVAX @ 9.853 (22.51 €, apertura)
- 2026-10-01 07:05 [macd_momentum_evento] ENTRADA AVAX @ 9.853 (22.41 €, apertura)
- 2026-10-01 07:05 [macd_momentum] ENTRADA UNI @ 7.9145 (22.29 €, apertura)
- 2026-10-01 07:05 [macd_sin_salida] ENTRADA UNI @ 7.9145 (22.61 €, apertura)
- 2026-10-01 07:05 [macd_momentum_regimen] ENTRADA UNI @ 7.9145 (22.51 €, apertura)
- 2026-10-01 07:05 [macd_momentum_evento] ENTRADA UNI @ 7.9145 (22.41 €, apertura)
- 2026-10-01 07:10 [macd_sin_salida] CIERRE ENA stop-loss bruto -1.60% neto -2.10%
- 2026-10-01 07:10 [c_banda_atr] CIERRE FET take-profit bruto +2.12% neto +1.62%
- 2026-10-01 07:10 [estocastico_rebote] CIERRE FET take-profit bruto +2.12% neto +1.62%
- 2026-10-01 07:10 [c_banda_atr_regimen] CIERRE FET take-profit bruto +2.12% neto +1.62%
- 2026-10-01 07:10 [c_banda_atr_evento] CIERRE FET take-profit bruto +2.12% neto +1.62%
- 2026-10-01 07:10 [macd_momentum] CIERRE POL momentum perdido bruto -0.21% neto -0.71%
- 2026-10-01 07:10 [macd_momentum_regimen] CIERRE POL momentum perdido bruto -0.21% neto -0.71%
- 2026-10-01 07:10 [macd_momentum_evento] CIERRE POL momentum perdido bruto -0.21% neto -0.71%
- 2026-10-01 07:05 [macd_momentum] ENTRADA ONDO @ 0.451 (22.28 €, apertura)
- 2026-10-01 07:05 [macd_momentum_regimen] ENTRADA ONDO @ 0.451 (22.51 €, apertura)
- 2026-10-01 07:05 [macd_momentum_evento] ENTRADA ONDO @ 0.451 (22.41 €, apertura)
- 2026-10-01 07:05 [ruptura_volumen] ENTRADA SEI @ 0.06575 (22.25 €, apertura)
- 2026-10-01 07:05 [macd_momentum] ENTRADA SEI @ 0.06575 (22.28 €, apertura)
- 2026-10-01 07:05 [estocastico_rebote] ENTRADA SEI @ 0.06575 (22.58 €, apertura)
- 2026-10-01 07:05 [ruptura_estricta] ENTRADA SEI @ 0.06575 (22.51 €, apertura)
- 2026-10-01 07:05 [ruptura_volumen_tope] ENTRADA SEI @ 0.06575 (22.87 €, apertura)
- 2026-10-01 07:05 [macd_momentum_regimen] ENTRADA SEI @ 0.06575 (22.51 €, apertura)
- 2026-10-01 07:05 [ruptura_volumen_regimen] ENTRADA SEI @ 0.06575 (22.27 €, apertura)
- 2026-10-01 07:05 [macd_momentum_evento] ENTRADA SEI @ 0.06575 (22.41 €, apertura)
- 2026-10-01 07:05 [ruptura_volumen_evento] ENTRADA SEI @ 0.06575 (22.56 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
