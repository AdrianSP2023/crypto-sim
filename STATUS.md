# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 06:26 UTC · vueltas 147 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.05 € (-1.75%) | 136 | 19 | 40% | +0.152% | -0.540% | -0.657% | -16.94 € |
| reversion_bb | 921.56 € (-0.29%) | 17 | 2 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 891.81 € (-3.51%) | 180 | 20 | 24% | -0.160% | -0.805% | -0.913% | -33.06 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.27 € (-2.27%) | 96 | 17 | 18% | -0.219% | -0.994% | -1.107% | -21.85 € |
| macd_momentum | 893.68 € (-3.31%) | 258 | 12 | 24% | +0.074% | -0.527% | -0.632% | -30.98 € |
| estocastico_rebote | 903.27 € (-2.27%) | 175 | 20 | 39% | +0.110% | -0.539% | -0.660% | -21.71 € |
| ruptura_estricta | 902.74 € (-2.33%) | 88 | 29 | 28% | -0.377% | -1.177% | -1.310% | -23.87 € |
| macd_sin_salida | 905.63 € (-2.01%) | 171 | 28 | 44% | +0.166% | -0.487% | -0.598% | -19.17 € |
| c_banda_atr_tope | 917.47 € (-0.73%) | 30 | 5 | 30% | +0.135% | -0.965% | -1.091% | -6.68 € |
| ruptura_volumen_tope | 915.62 € (-0.93%) | 48 | 4 | 27% | +0.193% | -0.857% | -0.957% | -9.47 € |
| c_banda_atr_regimen | 912.22 € (-1.30%) | 80 | 17 | 41% | +0.153% | -0.673% | -0.810% | -12.45 € |
| macd_momentum_regimen | 902.74 € (-2.33%) | 172 | 12 | 26% | +0.096% | -0.556% | -0.665% | -21.91 € |
| ruptura_volumen_regimen | 892.54 € (-3.43%) | 154 | 19 | 21% | -0.248% | -0.917% | -1.028% | -32.25 € |
| c_banda_atr_evento | 914.09 € (-1.10%) | 103 | 19 | 43% | +0.300% | -0.457% | -0.560% | -10.89 € |
| macd_momentum_evento | 898.63 € (-2.77%) | 211 | 12 | 22% | +0.084% | -0.541% | -0.638% | -26.03 € |
| ruptura_volumen_evento | 904.50 € (-2.14%) | 130 | 20 | 25% | +0.019% | -0.684% | -0.775% | -20.37 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 06:25 | macd_momentum_evento | SPX | momentum perdido | -0.07% | -0.57% | -0.13 |
| 2026-10-01 06:25 | macd_momentum_evento | ARB | momentum perdido | -0.71% | -1.21% | -0.27 |
| 2026-10-01 06:25 | macd_momentum_regimen | SPX | momentum perdido | -0.07% | -0.57% | -0.13 |
| 2026-10-01 06:25 | macd_momentum_regimen | ARB | momentum perdido | -0.71% | -1.21% | -0.27 |
| 2026-10-01 06:25 | ruptura_volumen_tope | USELESS | take-profit | +2.64% | +2.14% | +0.49 |
| 2026-10-01 06:25 | macd_sin_salida | CRV | stop-loss | -1.64% | -2.14% | -0.48 |
| 2026-10-01 06:25 | estocastico_rebote | NIGHT | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 06:25 | macd_momentum | SPX | momentum perdido | -0.07% | -0.57% | -0.13 |
| 2026-10-01 06:25 | macd_momentum | ARB | momentum perdido | -0.71% | -1.21% | -0.27 |
| 2026-10-01 06:20 | c_banda_atr_evento | ZRO | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 06:20 | c_banda_atr_regimen | ZRO | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 06:20 | macd_sin_salida | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 06:20 | ruptura_estricta | ZRO | stop-loss | -2.00% | -2.50% | -0.56 |
| 2026-10-01 06:20 | estocastico_rebote | TRX | timeout | -0.14% | -0.64% | -0.14 |
| 2026-10-01 06:20 | pullback_tendencia | ENA | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-10-01 06:20 [estocastico_rebote] ENTRADA ZRO @ 1.503 (22.56 €, apertura)
- 2026-10-01 06:20 [macd_momentum] ENTRADA DOT @ 1.0992 (22.34 €, apertura)
- 2026-10-01 06:20 [macd_sin_salida] ENTRADA DOT @ 1.0992 (22.64 €, apertura)
- 2026-10-01 06:20 [macd_momentum_regimen] ENTRADA DOT @ 1.0992 (22.57 €, apertura)
- 2026-10-01 06:20 [macd_momentum_evento] ENTRADA DOT @ 1.0992 (22.47 €, apertura)
- 2026-10-01 06:25 [macd_momentum] CIERRE ARB momentum perdido bruto -0.71% neto -1.21%
- 2026-10-01 06:25 [macd_momentum_regimen] CIERRE ARB momentum perdido bruto -0.71% neto -1.21%
- 2026-10-01 06:25 [macd_momentum_evento] CIERRE ARB momentum perdido bruto -0.71% neto -1.21%
- 2026-10-01 06:25 [macd_sin_salida] CIERRE CRV stop-loss bruto -1.64% neto -2.14%
- 2026-10-01 06:25 [estocastico_rebote] CIERRE NIGHT take-profit bruto +1.80% neto +1.30%
- 2026-10-01 06:25 [ruptura_volumen_tope] CIERRE USELESS take-profit bruto +2.64% neto +2.14%
- 2026-10-01 06:25 [macd_momentum] CIERRE SPX momentum perdido bruto -0.07% neto -0.57%
- 2026-10-01 06:25 [macd_momentum_regimen] CIERRE SPX momentum perdido bruto -0.07% neto -0.57%
- 2026-10-01 06:25 [macd_momentum_evento] CIERRE SPX momentum perdido bruto -0.07% neto -0.57%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
