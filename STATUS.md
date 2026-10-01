# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 00:41 UTC · vueltas 79 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 901.87 € (-2.42%) | 85 | 23 | 26% | -0.312% | -1.119% | -1.248% | -21.83 € |
| reversion_bb | 921.62 € (-0.28%) | 11 | 4 | 45% | +0.111% | -0.989% | -1.119% | -2.52 € |
| ruptura_volumen | 893.83 € (-3.29%) | 109 | 15 | 16% | -0.471% | -1.211% | -1.329% | -30.16 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.91 € (-2.20%) | 74 | 4 | 15% | -0.373% | -1.229% | -1.355% | -20.84 € |
| macd_momentum | 901.52 € (-2.46%) | 135 | 11 | 24% | -0.056% | -0.750% | -0.864% | -23.17 € |
| estocastico_rebote | 902.18 € (-2.39%) | 133 | 16 | 35% | -0.037% | -0.733% | -0.856% | -22.42 € |
| ruptura_estricta | 898.29 € (-2.81%) | 53 | 12 | 15% | -1.035% | -2.034% | -2.177% | -24.82 € |
| macd_sin_salida | 902.33 € (-2.37%) | 92 | 31 | 34% | -0.204% | -0.987% | -1.115% | -20.88 € |
| c_banda_atr_tope | 918.72 € (-0.60%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.248% | -5.10 € |
| ruptura_volumen_tope | 915.39 € (-0.96%) | 32 | 4 | 19% | -0.117% | -1.217% | -1.299% | -8.97 € |
| c_banda_atr_regimen | 906.84 € (-1.88%) | 47 | 7 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.47 € (-1.71%) | 76 | 0 | 25% | -0.058% | -0.902% | -1.028% | -15.78 € |
| ruptura_volumen_regimen | 895.28 € (-3.13%) | 87 | 10 | 13% | -0.633% | -1.433% | -1.561% | -28.54 € |
| c_banda_atr_evento | 908.42 € (-1.71%) | 52 | 23 | 23% | -0.314% | -1.276% | -1.386% | -15.27 € |
| macd_momentum_evento | 906.52 € (-1.92%) | 88 | 11 | 17% | -0.102% | -0.902% | -1.004% | -18.18 € |
| ruptura_volumen_evento | 906.54 € (-1.91%) | 59 | 15 | 12% | -0.340% | -1.287% | -1.378% | -17.44 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 00:40 | ruptura_volumen_evento | DASH | timeout | -0.91% | -1.41% | -0.32 |
| 2026-10-01 00:40 | ruptura_volumen_evento | ENA | timeout | +0.30% | -0.20% | -0.05 |
| 2026-10-01 00:40 | ruptura_volumen_evento | SOL | timeout | -0.38% | -0.88% | -0.20 |
| 2026-10-01 00:40 | ruptura_volumen_regimen | DASH | timeout | -0.91% | -1.41% | -0.32 |
| 2026-10-01 00:40 | ruptura_volumen_regimen | ENA | timeout | +0.30% | -0.20% | -0.04 |
| 2026-10-01 00:40 | ruptura_volumen_regimen | SOL | timeout | -0.38% | -0.88% | -0.20 |
| 2026-10-01 00:40 | ruptura_volumen_tope | ADA | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-10-01 00:40 | macd_sin_salida | SEI | timeout | -0.28% | -0.78% | -0.18 |
| 2026-10-01 00:40 | macd_sin_salida | ONDO | timeout | +1.37% | +0.87% | +0.20 |
| 2026-10-01 00:40 | estocastico_rebote | KAS | timeout | +0.73% | +0.23% | +0.05 |
| 2026-10-01 00:40 | ruptura_volumen | DASH | timeout | -0.91% | -1.41% | -0.32 |
| 2026-10-01 00:40 | ruptura_volumen | ENA | timeout | +0.30% | -0.20% | -0.04 |
| 2026-10-01 00:40 | ruptura_volumen | SOL | timeout | -0.38% | -0.88% | -0.20 |
| 2026-10-01 00:35 | ruptura_volumen_evento | VVV | timeout | -0.85% | -1.35% | -0.31 |
| 2026-10-01 00:35 | ruptura_volumen_evento | PEPE | timeout | -0.76% | -1.26% | -0.29 |

## Eventos de la última vuelta

- 2026-10-01 00:40 [ruptura_volumen] CIERRE SOL timeout bruto -0.38% neto -0.88%
- 2026-10-01 00:40 [ruptura_volumen_regimen] CIERRE SOL timeout bruto -0.38% neto -0.88%
- 2026-10-01 00:40 [ruptura_volumen_evento] CIERRE SOL timeout bruto -0.38% neto -0.88%
- 2026-10-01 00:40 [ruptura_volumen_tope] CIERRE ADA stop-loss bruto -1.20% neto -2.30%
- 2026-10-01 00:35 [estocastico_rebote] ENTRADA PUMP @ 0.005145 (22.54 €, apertura)
- 2026-10-01 00:40 [ruptura_volumen] CIERRE ENA timeout bruto +0.30% neto -0.20%
- 2026-10-01 00:35 [pullback_tendencia] ENTRADA ENA @ 0.2342 (22.59 €, apertura)
- 2026-10-01 00:40 [ruptura_volumen_regimen] CIERRE ENA timeout bruto +0.30% neto -0.20%
- 2026-10-01 00:40 [ruptura_volumen_evento] CIERRE ENA timeout bruto +0.30% neto -0.20%
- 2026-10-01 00:40 [macd_sin_salida] CIERRE ONDO timeout bruto +1.37% neto +0.87%
- 2026-10-01 00:35 [macd_momentum] ENTRADA CRV @ 0.34814 (22.53 €, apertura)
- 2026-10-01 00:35 [macd_sin_salida] ENTRADA CRV @ 0.34814 (22.59 €, apertura)
- 2026-10-01 00:35 [macd_momentum_evento] ENTRADA CRV @ 0.34814 (22.65 €, apertura)
- 2026-10-01 00:35 [macd_momentum] ENTRADA XDC @ 0.03074 (22.53 €, apertura)
- 2026-10-01 00:35 [macd_sin_salida] ENTRADA XDC @ 0.03074 (22.59 €, apertura)
- 2026-10-01 00:35 [macd_momentum_evento] ENTRADA XDC @ 0.03074 (22.65 €, apertura)
- 2026-10-01 00:35 [pullback_tendencia] ENTRADA NIGHT @ 0.03491 (22.59 €, apertura)
- 2026-10-01 00:35 [c_banda_atr] ENTRADA FIL @ 0.922 (22.56 €, apertura)
- 2026-10-01 00:35 [c_banda_atr_evento] ENTRADA FIL @ 0.922 (22.72 €, apertura)
- 2026-10-01 00:40 [ruptura_volumen] CIERRE DASH timeout bruto -0.91% neto -1.41%
- 2026-10-01 00:40 [ruptura_volumen_regimen] CIERRE DASH timeout bruto -0.91% neto -1.41%
- 2026-10-01 00:40 [ruptura_volumen_evento] CIERRE DASH timeout bruto -0.91% neto -1.41%
- 2026-10-01 00:35 [macd_momentum] ENTRADA TRUMP @ 1.82 (22.53 €, apertura)
- 2026-10-01 00:35 [macd_momentum_evento] ENTRADA TRUMP @ 1.82 (22.65 €, apertura)
- 2026-10-01 00:40 [estocastico_rebote] CIERRE KAS timeout bruto +0.73% neto +0.23%
- 2026-10-01 00:35 [macd_momentum] ENTRADA SKY @ 0.06875 (22.53 €, apertura)
- 2026-10-01 00:35 [macd_sin_salida] ENTRADA SKY @ 0.06875 (22.59 €, apertura)
- 2026-10-01 00:35 [macd_momentum_evento] ENTRADA SKY @ 0.06875 (22.65 €, apertura)
- 2026-10-01 00:40 [macd_sin_salida] CIERRE SEI timeout bruto -0.28% neto -0.78%
- 2026-10-01 00:35 [ruptura_estricta] ENTRADA APT @ 0.6878 (22.49 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
