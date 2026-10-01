# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 11:21 UTC · vueltas 206 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 895.70 € (-3.09%) | 175 | 18 | 34% | -0.061% | -0.710% | -0.832% | -28.41 € |
| reversion_bb | 918.86 € (-0.58%) | 25 | 8 | 40% | +0.108% | -0.992% | -1.096% | -5.72 € |
| ruptura_volumen | 884.57 € (-4.29%) | 211 | 10 | 23% | -0.201% | -0.825% | -0.935% | -39.54 € |
| rebote_extremo | 922.08 € (-0.23%) | 9 | 0 | 44% | +0.060% | -1.040% | -1.178% | -2.16 € |
| pullback_tendencia | 896.90 € (-2.96%) | 124 | 4 | 15% | -0.255% | -0.968% | -1.073% | -27.39 € |
| macd_momentum | 883.39 € (-4.42%) | 301 | 17 | 22% | -0.003% | -0.590% | -0.699% | -40.26 € |
| estocastico_rebote | 879.84 € (-4.80%) | 256 | 10 | 30% | -0.166% | -0.768% | -0.879% | -44.57 € |
| ruptura_estricta | 890.03 € (-3.70%) | 122 | 6 | 25% | -0.486% | -1.202% | -1.328% | -33.55 € |
| macd_sin_salida | 887.32 € (-3.99%) | 222 | 18 | 36% | -0.094% | -0.711% | -0.826% | -36.06 € |
| c_banda_atr_tope | 913.28 € (-1.19%) | 41 | 5 | 27% | -0.052% | -1.152% | -1.266% | -10.86 € |
| ruptura_volumen_tope | 911.99 € (-1.33%) | 63 | 5 | 29% | +0.074% | -0.845% | -0.961% | -12.23 € |
| c_banda_atr_regimen | 902.48 € (-2.35%) | 109 | 0 | 34% | -0.130% | -0.870% | -1.010% | -21.77 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 901.66 € (-2.44%) | 142 | 18 | 35% | -0.003% | -0.689% | -0.803% | -22.44 € |
| macd_momentum_evento | 888.29 € (-3.89%) | 254 | 17 | 19% | -0.009% | -0.613% | -0.717% | -35.36 € |
| ruptura_volumen_evento | 897.15 € (-2.93%) | 161 | 10 | 24% | -0.069% | -0.733% | -0.831% | -26.94 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 11:20 | macd_momentum_evento | VVV | momentum perdido | -0.93% | -1.43% | -0.32 |
| 2026-10-01 11:20 | macd_sin_salida | LTC | timeout | +0.37% | -0.13% | -0.03 |
| 2026-10-01 11:20 | estocastico_rebote | SEI | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-01 11:20 | macd_momentum | VVV | momentum perdido | -0.93% | -1.43% | -0.32 |
| 2026-10-01 11:05 | c_banda_atr_evento | MON | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 11:05 | c_banda_atr | MON | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 11:00 | estocastico_rebote | FET | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 11:00 | reversion_bb | SUI | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-10-01 10:55 | estocastico_rebote | TRUMP | timeout | +0.77% | +0.27% | +0.06 |
| 2026-10-01 10:50 | ruptura_volumen_evento | UNI | timeout | +0.56% | +0.06% | +0.01 |
| 2026-10-01 10:50 | ruptura_volumen_tope | UNI | timeout | +0.56% | +0.06% | +0.01 |
| 2026-10-01 10:50 | ruptura_volumen | UNI | timeout | +0.56% | +0.06% | +0.01 |
| 2026-10-01 10:45 | estocastico_rebote | XDC | timeout | -0.86% | -1.36% | -0.30 |
| 2026-10-01 10:45 | rebote_extremo | TRUMP | timeout | +1.11% | +0.01% | +0.00 |
| 2026-10-01 10:40 | estocastico_rebote | APT | timeout | -0.89% | -1.39% | -0.31 |

## Eventos de la última vuelta

- 2026-10-01 11:20 [macd_sin_salida] CIERRE LTC timeout bruto +0.37% neto -0.13%
- 2026-10-01 11:15 [ruptura_volumen] ENTRADA XDC @ 0.03133 (22.12 €, apertura)
- 2026-10-01 11:15 [ruptura_volumen_evento] ENTRADA XDC @ 0.03133 (22.43 €, apertura)
- 2026-10-01 11:20 [macd_momentum] CIERRE VVV momentum perdido bruto -0.93% neto -1.43%
- 2026-10-01 11:20 [macd_momentum_evento] CIERRE VVV momentum perdido bruto -0.93% neto -1.43%
- 2026-10-01 11:20 [estocastico_rebote] CIERRE SEI timeout bruto -0.36% neto -0.86%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
