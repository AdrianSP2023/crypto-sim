# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 06:41 UTC · vueltas 150 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.28 € (-1.84%) | 139 | 19 | 40% | +0.148% | -0.540% | -0.656% | -17.29 € |
| reversion_bb | 921.53 € (-0.29%) | 17 | 2 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 890.93 € (-3.60%) | 182 | 19 | 24% | -0.152% | -0.795% | -0.902% | -33.02 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 902.50 € (-2.35%) | 98 | 17 | 17% | -0.220% | -0.990% | -1.101% | -22.20 € |
| macd_momentum | 892.63 € (-3.42%) | 264 | 10 | 24% | +0.072% | -0.527% | -0.631% | -31.67 € |
| estocastico_rebote | 902.31 € (-2.37%) | 175 | 23 | 39% | +0.110% | -0.539% | -0.660% | -21.71 € |
| ruptura_estricta | 901.13 € (-2.50%) | 91 | 28 | 31% | -0.321% | -1.111% | -1.242% | -23.31 € |
| macd_sin_salida | 904.12 € (-2.18%) | 176 | 27 | 44% | +0.165% | -0.483% | -0.593% | -19.58 € |
| c_banda_atr_tope | 917.38 € (-0.74%) | 30 | 5 | 30% | +0.135% | -0.965% | -1.091% | -6.68 € |
| ruptura_volumen_tope | 915.17 € (-0.98%) | 50 | 3 | 30% | +0.225% | -0.803% | -0.901% | -9.25 € |
| c_banda_atr_regimen | 911.49 € (-1.38%) | 82 | 18 | 41% | +0.146% | -0.672% | -0.808% | -12.74 € |
| macd_momentum_regimen | 901.68 € (-2.44%) | 178 | 10 | 25% | +0.092% | -0.555% | -0.663% | -22.61 € |
| ruptura_volumen_regimen | 891.70 € (-3.52%) | 156 | 18 | 21% | -0.237% | -0.904% | -1.014% | -32.21 € |
| c_banda_atr_evento | 913.32 € (-1.18%) | 106 | 19 | 42% | +0.291% | -0.458% | -0.562% | -11.25 € |
| macd_momentum_evento | 897.58 € (-2.88%) | 217 | 10 | 21% | +0.081% | -0.540% | -0.637% | -26.73 € |
| ruptura_volumen_evento | 903.61 € (-2.23%) | 132 | 19 | 26% | +0.028% | -0.672% | -0.763% | -20.33 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 06:40 | macd_momentum_evento | BNB | momentum perdido | +0.19% | -0.31% | -0.07 |
| 2026-10-01 06:40 | macd_momentum_evento | PENGU | momentum perdido | -0.08% | -0.58% | -0.13 |
| 2026-10-01 06:40 | macd_momentum_regimen | BNB | momentum perdido | +0.19% | -0.31% | -0.07 |
| 2026-10-01 06:40 | macd_momentum_regimen | PENGU | momentum perdido | -0.08% | -0.58% | -0.13 |
| 2026-10-01 06:40 | macd_sin_salida | ETH | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-01 06:40 | ruptura_estricta | PEPE | timeout | +0.86% | +0.36% | +0.08 |
| 2026-10-01 06:40 | ruptura_estricta | TAO | timeout | +0.88% | +0.38% | +0.09 |
| 2026-10-01 06:40 | macd_momentum | BNB | momentum perdido | +0.19% | -0.31% | -0.07 |
| 2026-10-01 06:40 | macd_momentum | PENGU | momentum perdido | -0.08% | -0.58% | -0.13 |
| 2026-10-01 06:40 | pullback_tendencia | ARB | rotura de tendencia | -0.33% | -0.83% | -0.19 |
| 2026-10-01 06:40 | pullback_tendencia | LINK | rotura de tendencia | -0.22% | -0.72% | -0.16 |
| 2026-10-01 06:35 | macd_momentum_evento | ALGO | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-10-01 06:35 | macd_momentum_evento | AAVE | momentum perdido | +0.01% | -0.49% | -0.11 |
| 2026-10-01 06:35 | c_banda_atr_evento | TON | timeout | +0.83% | +0.33% | +0.07 |
| 2026-10-01 06:35 | c_banda_atr_evento | ICP | timeout | -1.07% | -1.57% | -0.35 |

## Eventos de la última vuelta

- 2026-10-01 06:40 [macd_sin_salida] CIERRE ETH timeout bruto +0.91% neto +0.41%
- 2026-10-01 06:35 [pullback_tendencia] ENTRADA SOL @ 105.32 (22.56 €, apertura)
- 2026-10-01 06:35 [c_banda_atr] ENTRADA QNT @ 258.99 (22.67 €, apertura)
- 2026-10-01 06:35 [c_banda_atr_regimen] ENTRADA QNT @ 258.99 (22.79 €, apertura)
- 2026-10-01 06:35 [c_banda_atr_evento] ENTRADA QNT @ 258.99 (22.82 €, apertura)
- 2026-10-01 06:35 [pullback_tendencia] ENTRADA NEAR @ 4.8439 (22.56 €, apertura)
- 2026-10-01 06:40 [pullback_tendencia] CIERRE LINK rotura de tendencia bruto -0.22% neto -0.72%
- 2026-10-01 06:35 [ruptura_volumen] ENTRADA PUMP @ 0.005281 (22.28 €, apertura)
- 2026-10-01 06:35 [ruptura_estricta] ENTRADA PUMP @ 0.005281 (22.52 €, apertura)
- 2026-10-01 06:35 [ruptura_volumen_tope] ENTRADA PUMP @ 0.005281 (22.87 €, apertura)
- 2026-10-01 06:35 [ruptura_volumen_regimen] ENTRADA PUMP @ 0.005281 (22.30 €, apertura)
- 2026-10-01 06:35 [ruptura_volumen_evento] ENTRADA PUMP @ 0.005281 (22.60 €, apertura)
- 2026-10-01 06:40 [ruptura_estricta] CIERRE TAO timeout bruto +0.88% neto +0.38%
- 2026-10-01 06:40 [pullback_tendencia] CIERRE ARB rotura de tendencia bruto -0.33% neto -0.83%
- 2026-10-01 06:35 [macd_momentum] ENTRADA ONDO @ 0.45101 (22.32 €, apertura)
- 2026-10-01 06:35 [macd_sin_salida] ENTRADA ONDO @ 0.45101 (22.62 €, apertura)
- 2026-10-01 06:35 [macd_momentum_regimen] ENTRADA ONDO @ 0.45101 (22.55 €, apertura)
- 2026-10-01 06:35 [macd_momentum_evento] ENTRADA ONDO @ 0.45101 (22.44 €, apertura)
- 2026-10-01 06:40 [ruptura_estricta] CIERRE PEPE timeout bruto +0.86% neto +0.36%
- 2026-10-01 06:40 [macd_momentum] CIERRE PENGU momentum perdido bruto -0.08% neto -0.58%
- 2026-10-01 06:40 [macd_momentum_regimen] CIERRE PENGU momentum perdido bruto -0.08% neto -0.58%
- 2026-10-01 06:40 [macd_momentum_evento] CIERRE PENGU momentum perdido bruto -0.08% neto -0.58%
- 2026-10-01 06:40 [macd_momentum] CIERRE BNB momentum perdido bruto +0.19% neto -0.31%
- 2026-10-01 06:40 [macd_momentum_regimen] CIERRE BNB momentum perdido bruto +0.19% neto -0.31%
- 2026-10-01 06:40 [macd_momentum_evento] CIERRE BNB momentum perdido bruto +0.19% neto -0.31%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
