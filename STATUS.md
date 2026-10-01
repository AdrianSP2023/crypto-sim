# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 00:31 UTC · vueltas 77 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.13 € (-2.39%) | 84 | 22 | 26% | -0.320% | -1.131% | -1.260% | -21.79 € |
| reversion_bb | 921.78 € (-0.27%) | 11 | 4 | 45% | +0.111% | -0.989% | -1.119% | -2.52 € |
| ruptura_volumen | 894.47 € (-3.22%) | 100 | 22 | 17% | -0.468% | -1.229% | -1.352% | -28.12 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.73 € (-2.22%) | 74 | 2 | 15% | -0.373% | -1.229% | -1.355% | -20.84 € |
| macd_momentum | 901.30 € (-2.48%) | 135 | 6 | 24% | -0.056% | -0.750% | -0.864% | -23.17 € |
| estocastico_rebote | 902.50 € (-2.35%) | 132 | 14 | 34% | -0.043% | -0.740% | -0.863% | -22.47 € |
| ruptura_estricta | 898.15 € (-2.82%) | 53 | 9 | 15% | -1.035% | -2.034% | -2.177% | -24.82 € |
| macd_sin_salida | 902.62 € (-2.34%) | 90 | 29 | 33% | -0.220% | -1.010% | -1.138% | -20.91 € |
| c_banda_atr_tope | 919.09 € (-0.56%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.248% | -5.10 € |
| ruptura_volumen_tope | 915.57 € (-0.94%) | 31 | 4 | 19% | -0.082% | -1.182% | -1.267% | -8.44 € |
| c_banda_atr_regimen | 906.94 € (-1.87%) | 47 | 7 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.47 € (-1.71%) | 76 | 0 | 25% | -0.058% | -0.902% | -1.028% | -15.78 € |
| ruptura_volumen_regimen | 896.15 € (-3.04%) | 77 | 20 | 14% | -0.651% | -1.490% | -1.625% | -26.29 € |
| c_banda_atr_evento | 908.75 € (-1.68%) | 51 | 22 | 24% | -0.327% | -1.292% | -1.401% | -15.16 € |
| macd_momentum_evento | 906.29 € (-1.94%) | 88 | 6 | 17% | -0.102% | -0.902% | -1.004% | -18.18 € |
| ruptura_volumen_evento | 907.20 € (-1.84%) | 50 | 22 | 14% | -0.309% | -1.337% | -1.433% | -15.37 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 00:30 | ruptura_volumen_evento | INJ | timeout | -0.53% | -1.33% | -0.30 |
| 2026-10-01 00:30 | ruptura_volumen_evento | CRV | timeout | -0.48% | -1.28% | -0.29 |
| 2026-10-01 00:30 | ruptura_volumen_tope | CRV | timeout | -0.48% | -1.58% | -0.36 |
| 2026-10-01 00:30 | estocastico_rebote | XLM | timeout | -0.20% | -0.70% | -0.16 |
| 2026-10-01 00:30 | ruptura_volumen | INJ | timeout | -0.53% | -1.03% | -0.23 |
| 2026-10-01 00:30 | ruptura_volumen | CRV | timeout | -0.48% | -0.98% | -0.22 |
| 2026-10-01 00:30 | reversion_bb | KAS | take-profit | +1.92% | +0.82% | +0.19 |
| 2026-10-01 00:25 | ruptura_volumen_evento | MON | take-profit | +2.50% | +2.00% | +0.46 |
| 2026-10-01 00:25 | c_banda_atr_evento | VVV | timeout | +0.05% | -0.75% | -0.17 |
| 2026-10-01 00:25 | c_banda_atr_evento | POL | timeout | +0.46% | -0.34% | -0.08 |
| 2026-10-01 00:25 | c_banda_atr_evento | AVAX | timeout | -0.46% | -1.25% | -0.29 |
| 2026-10-01 00:25 | ruptura_volumen_regimen | MON | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 00:25 | ruptura_volumen_tope | MON | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-10-01 00:25 | ruptura_estricta | MON | take-profit | +3.00% | +2.50% | +0.56 |
| 2026-10-01 00:25 | estocastico_rebote | NIGHT | take-profit | +1.80% | +1.30% | +0.29 |

## Eventos de la última vuelta

- 2026-10-01 00:25 [estocastico_rebote] ENTRADA NEAR @ 4.6839 (22.55 €, apertura)
- 2026-10-01 00:30 [estocastico_rebote] CIERRE XLM timeout bruto -0.20% neto -0.70%
- 2026-10-01 00:25 [estocastico_rebote] ENTRADA ZRO @ 1.514 (22.54 €, apertura)
- 2026-10-01 00:25 [estocastico_rebote] ENTRADA ENA @ 0.2335 (22.54 €, apertura)
- 2026-10-01 00:30 [ruptura_volumen] CIERRE CRV timeout bruto -0.48% neto -0.98%
- 2026-10-01 00:30 [ruptura_volumen_tope] CIERRE CRV timeout bruto -0.48% neto -1.58%
- 2026-10-01 00:30 [ruptura_volumen_evento] CIERRE CRV timeout bruto -0.48% neto -1.28%
- 2026-10-01 00:25 [macd_momentum] ENTRADA WLD @ 0.474 (22.53 €, apertura)
- 2026-10-01 00:25 [macd_momentum_evento] ENTRADA WLD @ 0.474 (22.65 €, apertura)
- 2026-10-01 00:25 [macd_momentum] ENTRADA NIGHT @ 0.03505 (22.53 €, apertura)
- 2026-10-01 00:25 [macd_sin_salida] ENTRADA NIGHT @ 0.03505 (22.58 €, apertura)
- 2026-10-01 00:25 [macd_momentum_evento] ENTRADA NIGHT @ 0.03505 (22.65 €, apertura)
- 2026-10-01 00:30 [ruptura_volumen] CIERRE INJ timeout bruto -0.53% neto -1.03%
- 2026-10-01 00:30 [ruptura_volumen_evento] CIERRE INJ timeout bruto -0.53% neto -1.33%
- 2026-10-01 00:25 [c_banda_atr] ENTRADA OP @ 0.1145 (22.56 €, apertura)
- 2026-10-01 00:25 [c_banda_atr_evento] ENTRADA OP @ 0.1145 (22.73 €, apertura)
- 2026-10-01 00:25 [ruptura_volumen] ENTRADA MINA @ 0.129 (22.40 €, apertura)
- 2026-10-01 00:25 [ruptura_estricta] ENTRADA MINA @ 0.129 (22.49 €, apertura)
- 2026-10-01 00:25 [ruptura_volumen_tope] ENTRADA MINA @ 0.129 (22.89 €, apertura)
- 2026-10-01 00:25 [ruptura_volumen_evento] ENTRADA MINA @ 0.129 (22.72 €, apertura)
- 2026-10-01 00:30 [reversion_bb] CIERRE KAS take-profit bruto +1.92% neto +0.82%
- 2026-10-01 00:25 [ruptura_volumen] ENTRADA APT @ 0.6849 (22.40 €, apertura)
- 2026-10-01 00:25 [ruptura_volumen_tope] ENTRADA APT @ 0.6849 (22.89 €, apertura)
- 2026-10-01 00:25 [ruptura_volumen_evento] ENTRADA APT @ 0.6849 (22.72 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
