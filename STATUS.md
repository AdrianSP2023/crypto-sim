# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 04:36 UTC · vueltas 126 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.16 € (-1.96%) | 116 | 25 | 33% | -0.056% | -0.781% | -0.902% | -20.81 € |
| reversion_bb | 921.79 € (-0.27%) | 14 | 4 | 36% | +0.190% | -0.910% | -1.026% | -2.94 € |
| ruptura_volumen | 890.80 € (-3.62%) | 151 | 27 | 20% | -0.304% | -0.977% | -1.087% | -33.64 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 902.93 € (-2.31%) | 87 | 8 | 16% | -0.297% | -1.101% | -1.219% | -21.92 € |
| macd_momentum | 895.40 € (-3.12%) | 214 | 21 | 21% | -0.012% | -0.634% | -0.742% | -30.91 € |
| estocastico_rebote | 902.97 € (-2.30%) | 155 | 16 | 37% | +0.057% | -0.611% | -0.732% | -21.80 € |
| ruptura_estricta | 900.47 € (-2.57%) | 77 | 24 | 23% | -0.542% | -1.385% | -1.517% | -24.56 € |
| macd_sin_salida | 905.50 € (-2.03%) | 140 | 33 | 39% | +0.043% | -0.643% | -0.758% | -20.71 € |
| c_banda_atr_tope | 918.16 € (-0.66%) | 27 | 5 | 30% | +0.046% | -1.054% | -1.177% | -6.56 € |
| ruptura_volumen_tope | 913.93 € (-1.12%) | 44 | 5 | 23% | +0.064% | -1.022% | -1.120% | -10.35 € |
| c_banda_atr_regimen | 911.07 € (-1.42%) | 59 | 24 | 31% | -0.206% | -1.148% | -1.293% | -15.61 € |
| macd_momentum_regimen | 904.48 € (-2.14%) | 128 | 21 | 20% | -0.041% | -0.745% | -0.859% | -21.85 € |
| ruptura_volumen_regimen | 891.52 € (-3.54%) | 124 | 28 | 15% | -0.453% | -1.164% | -1.279% | -32.92 € |
| c_banda_atr_evento | 912.19 € (-1.30%) | 83 | 25 | 34% | +0.045% | -0.773% | -0.879% | -14.79 € |
| macd_momentum_evento | 900.36 € (-2.58%) | 167 | 21 | 16% | -0.023% | -0.681% | -0.781% | -25.96 € |
| ruptura_volumen_evento | 903.48 € (-2.25%) | 101 | 27 | 20% | -0.144% | -0.906% | -0.996% | -20.96 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 04:35 | ruptura_volumen_evento | SPX | timeout | +0.43% | -0.07% | -0.02 |
| 2026-10-01 04:35 | ruptura_volumen_evento | AVAX | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-01 04:35 | ruptura_volumen_evento | LINK | timeout | +0.26% | -0.24% | -0.05 |
| 2026-10-01 04:35 | macd_momentum_evento | DOGE | momentum perdido | +0.28% | -0.22% | -0.05 |
| 2026-10-01 04:35 | c_banda_atr_evento | FIL | timeout | +0.76% | +0.26% | +0.06 |
| 2026-10-01 04:35 | ruptura_volumen_regimen | SPX | timeout | +0.43% | -0.07% | -0.02 |
| 2026-10-01 04:35 | ruptura_volumen_regimen | ICP | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-01 04:35 | ruptura_volumen_regimen | AVAX | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-01 04:35 | ruptura_volumen_regimen | LINK | timeout | +0.26% | -0.24% | -0.05 |
| 2026-10-01 04:35 | macd_momentum_regimen | DOGE | momentum perdido | +0.28% | -0.22% | -0.05 |
| 2026-10-01 04:35 | ruptura_volumen_tope | ICP | timeout | +0.00% | -0.80% | -0.18 |
| 2026-10-01 04:35 | ruptura_volumen_tope | AVAX | timeout | +0.91% | +0.10% | +0.02 |
| 2026-10-01 04:35 | ruptura_volumen_tope | LINK | timeout | +0.26% | -0.84% | -0.19 |
| 2026-10-01 04:35 | macd_sin_salida | UNI | timeout | +0.47% | -0.03% | -0.01 |
| 2026-10-01 04:35 | macd_momentum | DOGE | momentum perdido | +0.28% | -0.22% | -0.05 |

## Eventos de la última vuelta

- 2026-10-01 04:35 [ruptura_volumen] CIERRE LINK timeout bruto +0.26% neto -0.24%
- 2026-10-01 04:35 [ruptura_volumen_tope] CIERRE LINK timeout bruto +0.26% neto -0.84%
- 2026-10-01 04:35 [ruptura_volumen_regimen] CIERRE LINK timeout bruto +0.26% neto -0.24%
- 2026-10-01 04:35 [ruptura_volumen_evento] CIERRE LINK timeout bruto +0.26% neto -0.24%
- 2026-10-01 04:30 [ruptura_volumen] ENTRADA ADA @ 0.221799 (22.26 €, apertura)
- 2026-10-01 04:30 [ruptura_volumen_tope] ENTRADA ADA @ 0.221799 (22.85 €, apertura)
- 2026-10-01 04:30 [ruptura_volumen_regimen] ENTRADA ADA @ 0.221799 (22.28 €, apertura)
- 2026-10-01 04:30 [ruptura_volumen_evento] ENTRADA ADA @ 0.221799 (22.58 €, apertura)
- 2026-10-01 04:35 [ruptura_volumen] CIERRE AVAX timeout bruto +0.90% neto +0.40%
- 2026-10-01 04:35 [ruptura_volumen_tope] CIERRE AVAX timeout bruto +0.90% neto +0.10%
- 2026-10-01 04:35 [ruptura_volumen_regimen] CIERRE AVAX timeout bruto +0.90% neto +0.40%
- 2026-10-01 04:35 [ruptura_volumen_evento] CIERRE AVAX timeout bruto +0.90% neto +0.40%
- 2026-10-01 04:30 [ruptura_estricta] ENTRADA ZEC @ 1264.36 (22.49 €, apertura)
- 2026-10-01 04:30 [ruptura_volumen_tope] ENTRADA ZEC @ 1264.36 (22.85 €, apertura)
- 2026-10-01 04:30 [ruptura_volumen] ENTRADA UNI @ 7.8962 (22.27 €, apertura)
- 2026-10-01 04:30 [ruptura_estricta] ENTRADA UNI @ 7.8962 (22.49 €, apertura)
- 2026-10-01 04:35 [macd_sin_salida] CIERRE UNI timeout bruto +0.47% neto -0.03%
- 2026-10-01 04:30 [ruptura_volumen_regimen] ENTRADA UNI @ 7.8962 (22.29 €, apertura)
- 2026-10-01 04:30 [ruptura_volumen_evento] ENTRADA UNI @ 7.8962 (22.58 €, apertura)
- 2026-10-01 04:35 [macd_momentum] CIERRE DOGE momentum perdido bruto +0.28% neto -0.22%
- 2026-10-01 04:35 [macd_momentum_regimen] CIERRE DOGE momentum perdido bruto +0.28% neto -0.22%
- 2026-10-01 04:35 [macd_momentum_evento] CIERRE DOGE momentum perdido bruto +0.28% neto -0.22%
- 2026-10-01 04:35 [ruptura_volumen_tope] CIERRE ICP timeout bruto +0.00% neto -0.80%
- 2026-10-01 04:35 [ruptura_volumen_regimen] CIERRE ICP timeout bruto +0.00% neto -0.50%
- 2026-10-01 04:30 [c_banda_atr] ENTRADA FET @ 0.2067 (22.58 €, apertura)
- 2026-10-01 04:30 [ruptura_volumen_tope] ENTRADA FET @ 0.2067 (22.85 €, apertura)
- 2026-10-01 04:30 [c_banda_atr_regimen] ENTRADA FET @ 0.2067 (22.72 €, apertura)
- 2026-10-01 04:30 [c_banda_atr_evento] ENTRADA FET @ 0.2067 (22.73 €, apertura)
- 2026-10-01 04:30 [macd_momentum] ENTRADA ONDO @ 0.44978 (22.33 €, apertura)
- 2026-10-01 04:30 [macd_momentum_regimen] ENTRADA ONDO @ 0.44978 (22.56 €, apertura)
- 2026-10-01 04:30 [macd_momentum_evento] ENTRADA ONDO @ 0.44978 (22.46 €, apertura)
- 2026-10-01 04:30 [c_banda_atr] ENTRADA BCH @ 271.67 (22.58 €, apertura)
- 2026-10-01 04:30 [c_banda_atr_evento] ENTRADA BCH @ 271.67 (22.73 €, apertura)
- 2026-10-01 04:30 [c_banda_atr] ENTRADA OP @ 0.1155 (22.58 €, apertura)
- 2026-10-01 04:30 [macd_momentum] ENTRADA OP @ 0.1155 (22.33 €, apertura)
- 2026-10-01 04:30 [macd_sin_salida] ENTRADA OP @ 0.1155 (22.59 €, apertura)
- 2026-10-01 04:30 [macd_momentum_regimen] ENTRADA OP @ 0.1155 (22.56 €, apertura)
- 2026-10-01 04:30 [c_banda_atr_evento] ENTRADA OP @ 0.1155 (22.73 €, apertura)
- 2026-10-01 04:30 [macd_momentum_evento] ENTRADA OP @ 0.1155 (22.46 €, apertura)
- 2026-10-01 04:35 [c_banda_atr] CIERRE FIL timeout bruto +0.76% neto +0.26%
- 2026-10-01 04:35 [c_banda_atr_evento] CIERRE FIL timeout bruto +0.76% neto +0.26%
- 2026-10-01 04:30 [ruptura_estricta] ENTRADA TON @ 1.341 (22.49 €, apertura)
- 2026-10-01 04:35 [ruptura_volumen] CIERRE SPX timeout bruto +0.43% neto -0.07%
- 2026-10-01 04:35 [ruptura_volumen_regimen] CIERRE SPX timeout bruto +0.43% neto -0.07%
- 2026-10-01 04:35 [ruptura_volumen_evento] CIERRE SPX timeout bruto +0.43% neto -0.07%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
