# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 06:21 UTC · vueltas 146 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.83 € (-1.78%) | 136 | 19 | 40% | +0.152% | -0.540% | -0.657% | -16.94 € |
| reversion_bb | 921.58 € (-0.29%) | 17 | 2 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 891.43 € (-3.55%) | 180 | 20 | 24% | -0.160% | -0.805% | -0.913% | -33.06 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 902.96 € (-2.30%) | 96 | 17 | 18% | -0.219% | -0.994% | -1.107% | -21.85 € |
| macd_momentum | 893.77 € (-3.30%) | 256 | 13 | 25% | +0.078% | -0.524% | -0.629% | -30.58 € |
| estocastico_rebote | 902.83 € (-2.32%) | 174 | 20 | 39% | +0.100% | -0.550% | -0.669% | -22.00 € |
| ruptura_estricta | 902.21 € (-2.38%) | 88 | 29 | 28% | -0.377% | -1.177% | -1.310% | -23.87 € |
| macd_sin_salida | 905.40 € (-2.04%) | 170 | 28 | 44% | +0.177% | -0.477% | -0.589% | -18.69 € |
| c_banda_atr_tope | 917.36 € (-0.74%) | 30 | 5 | 30% | +0.135% | -0.965% | -1.091% | -6.68 € |
| ruptura_volumen_tope | 915.46 € (-0.95%) | 47 | 5 | 26% | +0.141% | -0.921% | -1.019% | -9.96 € |
| c_banda_atr_regimen | 911.99 € (-1.33%) | 80 | 17 | 41% | +0.153% | -0.673% | -0.810% | -12.45 € |
| macd_momentum_regimen | 902.83 € (-2.32%) | 170 | 13 | 26% | +0.101% | -0.552% | -0.661% | -21.51 € |
| ruptura_volumen_regimen | 892.18 € (-3.47%) | 154 | 19 | 21% | -0.248% | -0.917% | -1.028% | -32.25 € |
| c_banda_atr_evento | 913.87 € (-1.12%) | 103 | 19 | 43% | +0.300% | -0.457% | -0.560% | -10.89 € |
| macd_momentum_evento | 898.72 € (-2.76%) | 209 | 13 | 22% | +0.089% | -0.537% | -0.635% | -25.63 € |
| ruptura_volumen_evento | 904.11 € (-2.18%) | 130 | 20 | 25% | +0.019% | -0.684% | -0.775% | -20.37 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 06:20 | c_banda_atr_evento | ZRO | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 06:20 | c_banda_atr_regimen | ZRO | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 06:20 | macd_sin_salida | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 06:20 | ruptura_estricta | ZRO | stop-loss | -2.00% | -2.50% | -0.56 |
| 2026-10-01 06:20 | estocastico_rebote | TRX | timeout | -0.14% | -0.64% | -0.14 |
| 2026-10-01 06:20 | pullback_tendencia | ENA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 06:20 | c_banda_atr | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 06:15 | ruptura_volumen_evento | XMR | timeout | +0.19% | -0.31% | -0.07 |
| 2026-10-01 06:15 | ruptura_volumen_evento | ZEC | timeout | +0.48% | -0.01% | -0.00 |
| 2026-10-01 06:15 | ruptura_volumen_regimen | XMR | timeout | +0.19% | -0.31% | -0.07 |
| 2026-10-01 06:15 | ruptura_volumen_regimen | ZEC | timeout | +0.48% | -0.01% | -0.00 |
| 2026-10-01 06:15 | ruptura_volumen | XMR | timeout | +0.19% | -0.31% | -0.07 |
| 2026-10-01 06:15 | ruptura_volumen | ZEC | timeout | +0.48% | -0.01% | -0.00 |
| 2026-10-01 06:10 | ruptura_volumen_evento | PUMP | timeout | +1.13% | +0.63% | +0.14 |
| 2026-10-01 06:10 | macd_momentum_evento | SOL | momentum perdido | +1.02% | +0.52% | +0.12 |

## Eventos de la última vuelta

- 2026-10-01 06:15 [pullback_tendencia] ENTRADA ADA @ 0.22337 (22.55 €, apertura)
- 2026-10-01 06:15 [estocastico_rebote] ENTRADA HBAR @ 0.09361 (22.56 €, apertura)
- 2026-10-01 06:15 [pullback_tendencia] ENTRADA UNI @ 7.8963 (22.55 €, apertura)
- 2026-10-01 06:20 [c_banda_atr] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 06:20 [ruptura_estricta] CIERRE ZRO stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 06:20 [macd_sin_salida] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 06:20 [c_banda_atr_regimen] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 06:20 [c_banda_atr_evento] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 06:15 [estocastico_rebote] ENTRADA DOGE @ 0.0846257 (22.56 €, apertura)
- 2026-10-01 06:20 [pullback_tendencia] CIERRE ENA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 06:15 [pullback_tendencia] ENTRADA FET @ 0.21 (22.56 €, apertura)
- 2026-10-01 06:20 [estocastico_rebote] CIERRE TRX timeout bruto -0.14% neto -0.64%
- 2026-10-01 06:15 [estocastico_rebote] ENTRADA NIGHT @ 0.03555 (22.56 €, apertura)
- 2026-10-01 06:15 [macd_sin_salida] ENTRADA SHIB @ 5.143e-06 (22.64 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
