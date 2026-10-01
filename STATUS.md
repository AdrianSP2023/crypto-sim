# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 06:16 UTC · vueltas 145 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.20 € (-1.74%) | 135 | 20 | 40% | +0.164% | -0.529% | -0.647% | -16.49 € |
| reversion_bb | 921.59 € (-0.29%) | 17 | 2 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 891.71 € (-3.52%) | 180 | 20 | 24% | -0.160% | -0.805% | -0.913% | -33.06 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.03 € (-2.30%) | 95 | 15 | 17% | -0.242% | -1.020% | -1.134% | -22.18 € |
| macd_momentum | 893.69 € (-3.31%) | 256 | 13 | 25% | +0.078% | -0.524% | -0.629% | -30.58 € |
| estocastico_rebote | 902.77 € (-2.32%) | 173 | 18 | 39% | +0.102% | -0.549% | -0.669% | -21.86 € |
| ruptura_estricta | 902.90 € (-2.31%) | 87 | 30 | 29% | -0.359% | -1.162% | -1.295% | -23.31 € |
| macd_sin_salida | 905.78 € (-2.00%) | 169 | 28 | 44% | +0.187% | -0.468% | -0.580% | -18.23 € |
| c_banda_atr_tope | 917.43 € (-0.74%) | 30 | 5 | 30% | +0.135% | -0.965% | -1.091% | -6.68 € |
| ruptura_volumen_tope | 915.29 € (-0.97%) | 47 | 5 | 26% | +0.141% | -0.921% | -1.019% | -9.96 € |
| c_banda_atr_regimen | 912.40 € (-1.28%) | 79 | 18 | 42% | +0.174% | -0.656% | -0.794% | -12.00 € |
| macd_momentum_regimen | 902.75 € (-2.33%) | 170 | 13 | 26% | +0.101% | -0.552% | -0.661% | -21.51 € |
| ruptura_volumen_regimen | 892.43 € (-3.44%) | 154 | 19 | 21% | -0.248% | -0.917% | -1.028% | -32.25 € |
| c_banda_atr_evento | 914.25 € (-1.08%) | 102 | 20 | 43% | +0.317% | -0.442% | -0.546% | -10.44 € |
| macd_momentum_evento | 898.64 € (-2.77%) | 209 | 13 | 22% | +0.089% | -0.537% | -0.635% | -25.63 € |
| ruptura_volumen_evento | 904.39 € (-2.15%) | 130 | 20 | 25% | +0.019% | -0.684% | -0.775% | -20.37 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 06:15 | ruptura_volumen_evento | XMR | timeout | +0.19% | -0.31% | -0.07 |
| 2026-10-01 06:15 | ruptura_volumen_evento | ZEC | timeout | +0.48% | -0.01% | -0.00 |
| 2026-10-01 06:15 | ruptura_volumen_regimen | XMR | timeout | +0.19% | -0.31% | -0.07 |
| 2026-10-01 06:15 | ruptura_volumen_regimen | ZEC | timeout | +0.48% | -0.01% | -0.00 |
| 2026-10-01 06:15 | ruptura_volumen | XMR | timeout | +0.19% | -0.31% | -0.07 |
| 2026-10-01 06:15 | ruptura_volumen | ZEC | timeout | +0.48% | -0.01% | -0.00 |
| 2026-10-01 06:10 | ruptura_volumen_evento | PUMP | timeout | +1.13% | +0.63% | +0.14 |
| 2026-10-01 06:10 | macd_momentum_evento | SOL | momentum perdido | +1.02% | +0.52% | +0.12 |
| 2026-10-01 06:10 | macd_momentum_evento | ETH | momentum perdido | +0.92% | +0.42% | +0.09 |
| 2026-10-01 06:10 | c_banda_atr_evento | SOL | timeout | +0.99% | +0.49% | +0.11 |
| 2026-10-01 06:10 | c_banda_atr_evento | BTC | timeout | +0.81% | +0.31% | +0.07 |
| 2026-10-01 06:10 | ruptura_volumen_regimen | PUMP | timeout | +1.13% | +0.63% | +0.14 |
| 2026-10-01 06:10 | macd_momentum_regimen | SOL | momentum perdido | +1.02% | +0.52% | +0.12 |
| 2026-10-01 06:10 | macd_momentum_regimen | ETH | momentum perdido | +0.92% | +0.42% | +0.09 |
| 2026-10-01 06:10 | ruptura_estricta | SKY | timeout | +1.36% | +0.86% | +0.19 |

## Eventos de la última vuelta

- 2026-10-01 06:10 [pullback_tendencia] ENTRADA SUI @ 1.0352 (22.55 €, apertura)
- 2026-10-01 06:15 [ruptura_volumen] CIERRE ZEC timeout bruto +0.49% neto -0.01%
- 2026-10-01 06:15 [ruptura_volumen_regimen] CIERRE ZEC timeout bruto +0.49% neto -0.01%
- 2026-10-01 06:15 [ruptura_volumen_evento] CIERRE ZEC timeout bruto +0.49% neto -0.01%
- 2026-10-01 06:10 [macd_momentum] ENTRADA ENA @ 0.2438 (22.34 €, apertura)
- 2026-10-01 06:10 [macd_sin_salida] ENTRADA ENA @ 0.2438 (22.65 €, apertura)
- 2026-10-01 06:10 [macd_momentum_regimen] ENTRADA ENA @ 0.2438 (22.57 €, apertura)
- 2026-10-01 06:10 [macd_momentum_evento] ENTRADA ENA @ 0.2438 (22.47 €, apertura)
- 2026-10-01 06:15 [ruptura_volumen] CIERRE XMR timeout bruto +0.19% neto -0.31%
- 2026-10-01 06:15 [ruptura_volumen_regimen] CIERRE XMR timeout bruto +0.19% neto -0.31%
- 2026-10-01 06:15 [ruptura_volumen_evento] CIERRE XMR timeout bruto +0.19% neto -0.31%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
