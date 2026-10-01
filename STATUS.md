# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 07:01 UTC · vueltas 154 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.36 € (-1.72%) | 139 | 27 | 40% | +0.148% | -0.540% | -0.656% | -17.29 € |
| reversion_bb | 921.59 € (-0.29%) | 17 | 2 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 890.55 € (-3.65%) | 190 | 12 | 24% | -0.159% | -0.796% | -0.901% | -34.48 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 902.72 € (-2.33%) | 101 | 15 | 18% | -0.202% | -0.963% | -1.074% | -22.27 € |
| macd_momentum | 891.70 € (-3.52%) | 269 | 11 | 23% | +0.064% | -0.533% | -0.637% | -32.61 € |
| estocastico_rebote | 903.46 € (-2.25%) | 176 | 32 | 39% | +0.119% | -0.529% | -0.649% | -21.42 € |
| ruptura_estricta | 901.26 € (-2.49%) | 99 | 20 | 31% | -0.274% | -1.041% | -1.165% | -23.74 € |
| macd_sin_salida | 903.77 € (-2.21%) | 177 | 32 | 44% | +0.160% | -0.488% | -0.598% | -19.87 € |
| c_banda_atr_tope | 917.52 € (-0.73%) | 30 | 5 | 30% | +0.135% | -0.965% | -1.091% | -6.68 € |
| ruptura_volumen_tope | 914.92 € (-1.01%) | 51 | 3 | 29% | +0.197% | -0.821% | -0.919% | -9.64 € |
| c_banda_atr_regimen | 912.55 € (-1.26%) | 82 | 26 | 41% | +0.146% | -0.672% | -0.808% | -12.74 € |
| macd_momentum_regimen | 900.75 € (-2.54%) | 183 | 11 | 25% | +0.080% | -0.563% | -0.670% | -23.56 € |
| ruptura_volumen_regimen | 891.40 € (-3.55%) | 163 | 12 | 21% | -0.244% | -0.904% | -1.013% | -33.62 € |
| c_banda_atr_evento | 914.40 € (-1.06%) | 106 | 27 | 42% | +0.291% | -0.458% | -0.562% | -11.25 € |
| macd_momentum_evento | 896.64 € (-2.99%) | 222 | 11 | 21% | +0.072% | -0.547% | -0.644% | -27.67 € |
| ruptura_volumen_evento | 903.22 € (-2.27%) | 140 | 12 | 25% | +0.008% | -0.680% | -0.770% | -21.80 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 07:00 | ruptura_estricta | KAS | timeout | -0.97% | -1.47% | -0.33 |
| 2026-10-01 07:00 | ruptura_estricta | ETH | timeout | +0.82% | +0.33% | +0.07 |
| 2026-10-01 06:55 | macd_momentum_evento | TRUMP | momentum perdido | -0.42% | -0.92% | -0.21 |
| 2026-10-01 06:55 | macd_momentum_evento | ZEC | momentum perdido | -0.37% | -0.87% | -0.19 |
| 2026-10-01 06:55 | macd_momentum_regimen | TRUMP | momentum perdido | -0.42% | -0.92% | -0.21 |
| 2026-10-01 06:55 | macd_momentum_regimen | ZEC | momentum perdido | -0.37% | -0.87% | -0.20 |
| 2026-10-01 06:55 | macd_sin_salida | KAS | timeout | -0.77% | -1.27% | -0.29 |
| 2026-10-01 06:55 | ruptura_estricta | DASH | timeout | +0.10% | -0.40% | -0.09 |
| 2026-10-01 06:55 | ruptura_estricta | SHIB | timeout | +0.20% | -0.30% | -0.07 |
| 2026-10-01 06:55 | ruptura_estricta | SOL | timeout | +0.77% | +0.27% | +0.06 |
| 2026-10-01 06:55 | ruptura_estricta | XRP | timeout | +0.48% | -0.02% | -0.00 |
| 2026-10-01 06:55 | estocastico_rebote | ZRO | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 06:55 | macd_momentum | TRUMP | momentum perdido | -0.42% | -0.92% | -0.20 |
| 2026-10-01 06:55 | macd_momentum | ZEC | momentum perdido | -0.37% | -0.87% | -0.19 |
| 2026-10-01 06:50 | ruptura_volumen_evento | BCH | timeout | -0.18% | -0.68% | -0.15 |

## Eventos de la última vuelta

- 2026-10-01 06:55 [estocastico_rebote] ENTRADA BTC @ 74381.9 (22.57 €, apertura)
- 2026-10-01 07:00 [ruptura_estricta] CIERRE ETH timeout bruto +0.83% neto +0.33%
- 2026-10-01 06:55 [estocastico_rebote] ENTRADA SOL @ 105.4 (22.57 €, apertura)
- 2026-10-01 06:55 [c_banda_atr] ENTRADA AVAX @ 9.833 (22.67 €, apertura)
- 2026-10-01 06:55 [c_banda_atr_regimen] ENTRADA AVAX @ 9.833 (22.79 €, apertura)
- 2026-10-01 06:55 [c_banda_atr_evento] ENTRADA AVAX @ 9.833 (22.82 €, apertura)
- 2026-10-01 06:55 [c_banda_atr] ENTRADA XLM @ 0.201149 (22.67 €, apertura)
- 2026-10-01 06:55 [c_banda_atr_regimen] ENTRADA XLM @ 0.201149 (22.79 €, apertura)
- 2026-10-01 06:55 [c_banda_atr_evento] ENTRADA XLM @ 0.201149 (22.82 €, apertura)
- 2026-10-01 06:55 [macd_momentum] ENTRADA TAO @ 274.58 (22.29 €, apertura)
- 2026-10-01 06:55 [macd_momentum_regimen] ENTRADA TAO @ 274.58 (22.52 €, apertura)
- 2026-10-01 06:55 [macd_momentum_evento] ENTRADA TAO @ 274.58 (22.41 €, apertura)
- 2026-10-01 06:55 [c_banda_atr] ENTRADA ZRO @ 1.529 (22.67 €, apertura)
- 2026-10-01 06:55 [macd_momentum] ENTRADA ZRO @ 1.529 (22.29 €, apertura)
- 2026-10-01 06:55 [macd_sin_salida] ENTRADA ZRO @ 1.529 (22.61 €, apertura)
- 2026-10-01 06:55 [c_banda_atr_regimen] ENTRADA ZRO @ 1.529 (22.79 €, apertura)
- 2026-10-01 06:55 [macd_momentum_regimen] ENTRADA ZRO @ 1.529 (22.52 €, apertura)
- 2026-10-01 06:55 [c_banda_atr_evento] ENTRADA ZRO @ 1.529 (22.82 €, apertura)
- 2026-10-01 06:55 [macd_momentum_evento] ENTRADA ZRO @ 1.529 (22.41 €, apertura)
- 2026-10-01 06:55 [c_banda_atr] ENTRADA DOT @ 1.1038 (22.67 €, apertura)
- 2026-10-01 06:55 [ruptura_volumen] ENTRADA DOT @ 1.1038 (22.24 €, apertura)
- 2026-10-01 06:55 [ruptura_volumen_tope] ENTRADA DOT @ 1.1038 (22.87 €, apertura)
- 2026-10-01 06:55 [c_banda_atr_regimen] ENTRADA DOT @ 1.1038 (22.79 €, apertura)
- 2026-10-01 06:55 [ruptura_volumen_regimen] ENTRADA DOT @ 1.1038 (22.27 €, apertura)
- 2026-10-01 06:55 [c_banda_atr_evento] ENTRADA DOT @ 1.1038 (22.82 €, apertura)
- 2026-10-01 06:55 [ruptura_volumen_evento] ENTRADA DOT @ 1.1038 (22.56 €, apertura)
- 2026-10-01 06:55 [estocastico_rebote] ENTRADA ARB @ 0.1824 (22.57 €, apertura)
- 2026-10-01 06:55 [estocastico_rebote] ENTRADA BCH @ 272.96 (22.57 €, apertura)
- 2026-10-01 06:55 [estocastico_rebote] ENTRADA MON @ 0.03018 (22.57 €, apertura)
- 2026-10-01 06:55 [c_banda_atr] ENTRADA VVV @ 24.811 (22.67 €, apertura)
- 2026-10-01 06:55 [c_banda_atr_regimen] ENTRADA VVV @ 24.811 (22.79 €, apertura)
- 2026-10-01 06:55 [c_banda_atr_evento] ENTRADA VVV @ 24.811 (22.82 €, apertura)
- 2026-10-01 07:00 [ruptura_estricta] CIERRE KAS timeout bruto -0.97% neto -1.47%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
