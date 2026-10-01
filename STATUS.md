# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 00:36 UTC · vueltas 78 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 901.79 € (-2.43%) | 85 | 22 | 26% | -0.312% | -1.119% | -1.248% | -21.83 € |
| reversion_bb | 921.79 € (-0.27%) | 11 | 4 | 45% | +0.111% | -0.989% | -1.119% | -2.52 € |
| ruptura_volumen | 893.89 € (-3.28%) | 106 | 18 | 16% | -0.475% | -1.222% | -1.342% | -29.61 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.67 € (-2.23%) | 74 | 2 | 15% | -0.373% | -1.229% | -1.355% | -20.84 € |
| macd_momentum | 901.32 € (-2.48%) | 135 | 7 | 24% | -0.056% | -0.750% | -0.864% | -23.17 € |
| estocastico_rebote | 902.48 € (-2.35%) | 132 | 16 | 34% | -0.043% | -0.740% | -0.863% | -22.47 € |
| ruptura_estricta | 898.24 € (-2.81%) | 53 | 11 | 15% | -1.035% | -2.034% | -2.177% | -24.82 € |
| macd_sin_salida | 902.17 € (-2.39%) | 90 | 30 | 33% | -0.220% | -1.010% | -1.138% | -20.91 € |
| c_banda_atr_tope | 918.89 € (-0.58%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.248% | -5.10 € |
| ruptura_volumen_tope | 915.71 € (-0.92%) | 31 | 5 | 19% | -0.082% | -1.182% | -1.267% | -8.44 € |
| c_banda_atr_regimen | 906.84 € (-1.88%) | 47 | 7 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.47 € (-1.71%) | 76 | 0 | 25% | -0.058% | -0.902% | -1.028% | -15.78 € |
| ruptura_volumen_regimen | 895.30 € (-3.13%) | 84 | 13 | 13% | -0.644% | -1.455% | -1.585% | -27.98 € |
| c_banda_atr_evento | 908.34 € (-1.72%) | 52 | 22 | 23% | -0.314% | -1.276% | -1.386% | -15.27 € |
| macd_momentum_evento | 906.31 € (-1.94%) | 88 | 7 | 17% | -0.102% | -0.902% | -1.004% | -18.18 € |
| ruptura_volumen_evento | 906.61 € (-1.91%) | 56 | 18 | 12% | -0.340% | -1.311% | -1.405% | -16.87 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 00:35 | ruptura_volumen_evento | VVV | timeout | -0.85% | -1.35% | -0.31 |
| 2026-10-01 00:35 | ruptura_volumen_evento | PEPE | timeout | -0.76% | -1.26% | -0.29 |
| 2026-10-01 00:35 | ruptura_volumen_evento | WLD | timeout | -0.29% | -0.79% | -0.18 |
| 2026-10-01 00:35 | ruptura_volumen_evento | FET | timeout | +0.05% | -0.45% | -0.10 |
| 2026-10-01 00:35 | ruptura_volumen_evento | AVAX | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 00:35 | ruptura_volumen_evento | ADA | timeout | -0.56% | -1.06% | -0.24 |
| 2026-10-01 00:35 | c_banda_atr_evento | SEI | timeout | +0.33% | -0.47% | -0.11 |
| 2026-10-01 00:35 | ruptura_volumen_regimen | VVV | timeout | -0.85% | -1.35% | -0.30 |
| 2026-10-01 00:35 | ruptura_volumen_regimen | PEPE | timeout | -0.76% | -1.26% | -0.28 |
| 2026-10-01 00:35 | ruptura_volumen_regimen | WLD | timeout | -0.29% | -0.79% | -0.18 |
| 2026-10-01 00:35 | ruptura_volumen_regimen | CRV | timeout | -0.40% | -0.90% | -0.20 |
| 2026-10-01 00:35 | ruptura_volumen_regimen | FET | timeout | +0.05% | -0.45% | -0.10 |
| 2026-10-01 00:35 | ruptura_volumen_regimen | AVAX | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 00:35 | ruptura_volumen_regimen | ADA | timeout | -0.56% | -1.06% | -0.24 |
| 2026-10-01 00:35 | ruptura_volumen | VVV | timeout | -0.85% | -1.35% | -0.30 |

## Eventos de la última vuelta

- 2026-10-01 00:35 [ruptura_volumen] CIERRE ADA timeout bruto -0.56% neto -1.06%
- 2026-10-01 00:35 [ruptura_volumen_regimen] CIERRE ADA timeout bruto -0.56% neto -1.06%
- 2026-10-01 00:35 [ruptura_volumen_evento] CIERRE ADA timeout bruto -0.56% neto -1.06%
- 2026-10-01 00:35 [ruptura_volumen] CIERRE AVAX stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 00:35 [ruptura_volumen_regimen] CIERRE AVAX stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 00:35 [ruptura_volumen_evento] CIERRE AVAX stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 00:35 [ruptura_volumen] CIERRE FET timeout bruto +0.05% neto -0.45%
- 2026-10-01 00:35 [ruptura_volumen_regimen] CIERRE FET timeout bruto +0.05% neto -0.45%
- 2026-10-01 00:35 [ruptura_volumen_evento] CIERRE FET timeout bruto +0.05% neto -0.45%
- 2026-10-01 00:30 [c_banda_atr] ENTRADA CRV @ 0.34895 (22.56 €, apertura)
- 2026-10-01 00:35 [ruptura_volumen_regimen] CIERRE CRV timeout bruto -0.40% neto -0.90%
- 2026-10-01 00:30 [c_banda_atr_evento] ENTRADA CRV @ 0.34895 (22.73 €, apertura)
- 2026-10-01 00:35 [ruptura_volumen] CIERRE WLD timeout bruto -0.29% neto -0.79%
- 2026-10-01 00:35 [ruptura_volumen_regimen] CIERRE WLD timeout bruto -0.29% neto -0.79%
- 2026-10-01 00:35 [ruptura_volumen_evento] CIERRE WLD timeout bruto -0.29% neto -0.79%
- 2026-10-01 00:30 [ruptura_volumen] ENTRADA XDC @ 0.03067 (22.38 €, apertura)
- 2026-10-01 00:30 [estocastico_rebote] ENTRADA XDC @ 0.03067 (22.54 €, apertura)
- 2026-10-01 00:30 [ruptura_estricta] ENTRADA XDC @ 0.03067 (22.49 €, apertura)
- 2026-10-01 00:30 [ruptura_volumen_tope] ENTRADA XDC @ 0.03067 (22.89 €, apertura)
- 2026-10-01 00:30 [ruptura_volumen_evento] ENTRADA XDC @ 0.03067 (22.70 €, apertura)
- 2026-10-01 00:30 [estocastico_rebote] ENTRADA JUP @ 0.29061 (22.54 €, apertura)
- 2026-10-01 00:35 [ruptura_volumen] CIERRE PEPE timeout bruto -0.76% neto -1.26%
- 2026-10-01 00:35 [ruptura_volumen_regimen] CIERRE PEPE timeout bruto -0.76% neto -1.26%
- 2026-10-01 00:35 [ruptura_volumen_evento] CIERRE PEPE timeout bruto -0.76% neto -1.26%
- 2026-10-01 00:30 [macd_momentum] ENTRADA OP @ 0.1145 (22.53 €, apertura)
- 2026-10-01 00:30 [macd_sin_salida] ENTRADA OP @ 0.1145 (22.58 €, apertura)
- 2026-10-01 00:30 [macd_momentum_evento] ENTRADA OP @ 0.1145 (22.65 €, apertura)
- 2026-10-01 00:35 [ruptura_volumen] CIERRE VVV timeout bruto -0.85% neto -1.35%
- 2026-10-01 00:35 [ruptura_volumen_regimen] CIERRE VVV timeout bruto -0.85% neto -1.35%
- 2026-10-01 00:35 [ruptura_volumen_evento] CIERRE VVV timeout bruto -0.85% neto -1.35%
- 2026-10-01 00:30 [ruptura_volumen] ENTRADA KAS @ 0.03866 (22.37 €, apertura)
- 2026-10-01 00:30 [ruptura_estricta] ENTRADA KAS @ 0.03866 (22.49 €, apertura)
- 2026-10-01 00:30 [ruptura_volumen_evento] ENTRADA KAS @ 0.03866 (22.68 €, apertura)
- 2026-10-01 00:35 [c_banda_atr] CIERRE SEI timeout bruto +0.32% neto -0.18%
- 2026-10-01 00:35 [c_banda_atr_evento] CIERRE SEI timeout bruto +0.32% neto -0.48%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
