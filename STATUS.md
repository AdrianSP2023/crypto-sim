# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 16:11 UTC · vueltas 261 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.08 € (-3.70%) | 216 | 21 | 33% | -0.085% | -0.706% | -0.830% | -34.72 € |
| reversion_bb | 916.38 € (-0.85%) | 38 | 9 | 39% | +0.067% | -1.033% | -1.133% | -9.04 € |
| ruptura_volumen | 879.36 € (-4.86%) | 241 | 10 | 23% | -0.219% | -0.827% | -0.935% | -45.15 € |
| rebote_extremo | 922.10 € (-0.23%) | 12 | 1 | 50% | +0.217% | -0.883% | -1.057% | -2.45 € |
| pullback_tendencia | 892.95 € (-3.39%) | 145 | 6 | 13% | -0.284% | -0.966% | -1.067% | -31.87 € |
| macd_momentum | 875.10 € (-5.32%) | 366 | 21 | 20% | -0.037% | -0.608% | -0.716% | -50.13 € |
| estocastico_rebote | 878.76 € (-4.92%) | 279 | 8 | 30% | -0.147% | -0.741% | -0.853% | -46.76 € |
| ruptura_estricta | 885.81 € (-4.16%) | 137 | 7 | 23% | -0.562% | -1.254% | -1.376% | -39.15 € |
| macd_sin_salida | 883.16 € (-4.44%) | 260 | 23 | 34% | -0.114% | -0.715% | -0.831% | -42.25 € |
| c_banda_atr_tope | 912.50 € (-1.27%) | 50 | 5 | 28% | -0.015% | -1.043% | -1.156% | -11.99 € |
| ruptura_volumen_tope | 907.87 € (-1.77%) | 80 | 5 | 25% | -0.069% | -0.899% | -1.014% | -16.50 € |
| c_banda_atr_regimen | 902.03 € (-2.40%) | 110 | 2 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.84 € (-3.29%) | 206 | 1 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.50 € (-4.41%) | 185 | 3 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 896.00 € (-3.05%) | 183 | 21 | 34% | -0.044% | -0.689% | -0.807% | -28.79 € |
| macd_momentum_evento | 879.95 € (-4.79%) | 319 | 21 | 18% | -0.046% | -0.629% | -0.733% | -45.29 € |
| ruptura_volumen_evento | 891.87 € (-3.50%) | 191 | 10 | 24% | -0.112% | -0.751% | -0.847% | -32.63 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 16:10 | estocastico_rebote | HYPE | timeout | -1.25% | -1.75% | -0.39 |
| 2026-10-01 16:10 | estocastico_rebote | ETH | timeout | +0.32% | -0.18% | -0.04 |
| 2026-10-01 16:05 | rebote_desplome_mercado | NIGHT | take-profit | +8.00% | +6.90% | +1.59 |
| 2026-10-01 16:05 | rebote_desplome | NIGHT | take-profit | +8.00% | +6.90% | +1.59 |
| 2026-10-01 16:05 | macd_momentum_evento | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 16:05 | macd_momentum_evento | UNI | momentum perdido | -0.00% | -0.50% | -0.11 |
| 2026-10-01 16:05 | c_banda_atr_evento | XMR | timeout | +0.09% | -0.41% | -0.09 |
| 2026-10-01 16:05 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 16:05 | macd_sin_salida | USELESS | take-profit | +2.16% | +1.66% | +0.37 |
| 2026-10-01 16:05 | macd_momentum | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 16:05 | macd_momentum | UNI | momentum perdido | -0.00% | -0.50% | -0.11 |
| 2026-10-01 16:05 | c_banda_atr | XMR | timeout | +0.09% | -0.41% | -0.09 |
| 2026-10-01 16:00 | macd_sin_salida | PEPE | take-profit | +2.06% | +1.56% | +0.34 |
| 2026-10-01 16:00 | rebote_extremo | PUMP | take-profit | +2.07% | +0.97% | +0.22 |
| 2026-10-01 15:55 | ruptura_volumen_evento | SKY | take-profit | +2.50% | +2.00% | +0.45 |

## Eventos de la última vuelta

- 2026-10-01 16:10 [estocastico_rebote] CIERRE ETH timeout bruto +0.32% neto -0.18%
- 2026-10-01 16:05 [macd_momentum] ENTRADA LINK @ 12.7637 (21.85 €, apertura)
- 2026-10-01 16:05 [macd_momentum_regimen] ENTRADA LINK @ 12.7637 (22.35 €, apertura)
- 2026-10-01 16:05 [macd_momentum_evento] ENTRADA LINK @ 12.7637 (21.97 €, apertura)
- 2026-10-01 16:10 [estocastico_rebote] CIERRE HYPE timeout bruto -1.25% neto -1.75%
- 2026-10-01 16:05 [c_banda_atr] ENTRADA JUP @ 0.28356 (22.24 €, apertura)
- 2026-10-01 16:05 [c_banda_atr_regimen] ENTRADA JUP @ 0.28356 (22.55 €, apertura)
- 2026-10-01 16:05 [c_banda_atr_evento] ENTRADA JUP @ 0.28356 (22.39 €, apertura)
- 2026-10-01 16:05 [c_banda_atr] ENTRADA RENDER @ 1.699 (22.24 €, apertura)
- 2026-10-01 16:05 [c_banda_atr_regimen] ENTRADA RENDER @ 1.699 (22.55 €, apertura)
- 2026-10-01 16:05 [c_banda_atr_evento] ENTRADA RENDER @ 1.699 (22.39 €, apertura)
- 2026-10-01 16:05 [ruptura_volumen] ENTRADA VVV @ 24.657 (21.98 €, apertura)
- 2026-10-01 16:05 [ruptura_volumen_regimen] ENTRADA VVV @ 24.657 (22.09 €, apertura)
- 2026-10-01 16:05 [ruptura_volumen_evento] ENTRADA VVV @ 24.657 (22.29 €, apertura)
- 2026-10-01 16:05 [ruptura_volumen] ENTRADA SHIB @ 5.122e-06 (21.98 €, apertura)
- 2026-10-01 16:05 [ruptura_estricta] ENTRADA SHIB @ 5.122e-06 (22.13 €, apertura)
- 2026-10-01 16:05 [ruptura_volumen_regimen] ENTRADA SHIB @ 5.122e-06 (22.09 €, apertura)
- 2026-10-01 16:05 [ruptura_volumen_evento] ENTRADA SHIB @ 5.122e-06 (22.29 €, apertura)
- 2026-10-01 16:05 [ruptura_volumen] ENTRADA KSM @ 4.61 (21.98 €, apertura)
- 2026-10-01 16:05 [ruptura_volumen_regimen] ENTRADA KSM @ 4.61 (22.09 €, apertura)
- 2026-10-01 16:05 [ruptura_volumen_evento] ENTRADA KSM @ 4.61 (22.29 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
