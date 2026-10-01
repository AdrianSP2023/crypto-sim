# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 14:51 UTC · vueltas 245 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.26 € (-3.57%) | 202 | 16 | 34% | -0.062% | -0.691% | -0.817% | -31.86 € |
| reversion_bb | 916.67 € (-0.82%) | 33 | 10 | 39% | +0.133% | -0.967% | -1.063% | -7.36 € |
| ruptura_volumen | 879.03 € (-4.89%) | 238 | 5 | 23% | -0.220% | -0.830% | -0.937% | -44.72 € |
| rebote_extremo | 921.88 € (-0.26%) | 10 | 1 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 893.27 € (-3.35%) | 141 | 1 | 13% | -0.279% | -0.967% | -1.069% | -31.03 € |
| macd_momentum | 876.43 € (-5.17%) | 342 | 17 | 20% | -0.023% | -0.600% | -0.710% | -46.32 € |
| estocastico_rebote | 877.51 € (-5.06%) | 272 | 13 | 30% | -0.164% | -0.759% | -0.872% | -46.75 € |
| ruptura_estricta | 885.21 € (-4.22%) | 136 | 2 | 23% | -0.551% | -1.245% | -1.367% | -38.60 € |
| macd_sin_salida | 881.10 € (-4.67%) | 250 | 15 | 34% | -0.135% | -0.740% | -0.856% | -42.06 € |
| c_banda_atr_tope | 912.06 € (-1.32%) | 48 | 4 | 27% | -0.027% | -1.077% | -1.191% | -11.88 € |
| ruptura_volumen_tope | 908.23 € (-1.73%) | 76 | 3 | 25% | -0.052% | -0.899% | -1.014% | -15.67 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 897.19 € (-2.93%) | 169 | 16 | 35% | -0.014% | -0.670% | -0.789% | -25.91 € |
| macd_momentum_evento | 881.29 € (-4.65%) | 295 | 17 | 18% | -0.032% | -0.621% | -0.727% | -41.46 € |
| ruptura_volumen_evento | 891.53 € (-3.54%) | 188 | 5 | 23% | -0.112% | -0.752% | -0.849% | -32.19 € |
| rebote_desplome | 924.91 € (+0.07%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.91 € (+0.07%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 14:50 | ruptura_volumen_evento | USELESS | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 14:50 | c_banda_atr_evento | ASTER | timeout | -0.45% | -0.95% | -0.21 |
| 2026-10-01 14:50 | c_banda_atr_evento | DOT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 14:50 | ruptura_volumen_tope | USELESS | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 14:50 | c_banda_atr_tope | DOT | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 14:50 | macd_sin_salida | ZEC | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 14:50 | ruptura_estricta | PEPE | timeout | -0.26% | -0.76% | -0.17 |
| 2026-10-01 14:50 | ruptura_estricta | DOGE | timeout | -0.43% | -0.93% | -0.21 |
| 2026-10-01 14:50 | pullback_tendencia | PEPE | rotura de tendencia | -1.03% | -1.53% | -0.34 |
| 2026-10-01 14:50 | pullback_tendencia | LINK | rotura de tendencia | -0.27% | -0.77% | -0.17 |
| 2026-10-01 14:50 | pullback_tendencia | ETH | rotura de tendencia | -0.27% | -0.77% | -0.17 |
| 2026-10-01 14:50 | ruptura_volumen | USELESS | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-01 14:50 | c_banda_atr | ASTER | timeout | -0.45% | -0.95% | -0.21 |
| 2026-10-01 14:50 | c_banda_atr | DOT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 14:45 | ruptura_volumen_evento | UNI | stop-loss | -1.30% | -1.80% | -0.40 |

## Eventos de la última vuelta

- 2026-10-01 14:45 [pullback_tendencia] ENTRADA ETH @ 2389.08 (22.35 €, apertura)
- 2026-10-01 14:50 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto -0.27% neto -0.77%
- 2026-10-01 14:50 [pullback_tendencia] CIERRE LINK rotura de tendencia bruto -0.27% neto -0.77%
- 2026-10-01 14:50 [macd_sin_salida] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:50 [ruptura_estricta] CIERRE DOGE timeout bruto -0.43% neto -0.93%
- 2026-10-01 14:50 [c_banda_atr] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:50 [c_banda_atr_tope] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:50 [c_banda_atr_evento] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 14:45 [c_banda_atr] ENTRADA XDC @ 0.03117 (22.31 €, apertura)
- 2026-10-01 14:45 [c_banda_atr_tope] ENTRADA XDC @ 0.03117 (22.81 €, apertura)
- 2026-10-01 14:45 [c_banda_atr_evento] ENTRADA XDC @ 0.03117 (22.46 €, apertura)
- 2026-10-01 14:50 [ruptura_volumen] CIERRE USELESS stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 14:50 [ruptura_volumen_tope] CIERRE USELESS stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 14:50 [ruptura_volumen_evento] CIERRE USELESS stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 14:50 [pullback_tendencia] CIERRE PEPE rotura de tendencia bruto -1.03% neto -1.53%
- 2026-10-01 14:50 [ruptura_estricta] CIERRE PEPE timeout bruto -0.26% neto -0.76%
- 2026-10-01 14:50 [c_banda_atr] CIERRE ASTER timeout bruto -0.45% neto -0.95%
- 2026-10-01 14:50 [c_banda_atr_evento] CIERRE ASTER timeout bruto -0.45% neto -0.95%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
