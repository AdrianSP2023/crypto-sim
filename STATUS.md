# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 13:31 UTC · vueltas 229 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 892.99 € (-3.38%) | 192 | 14 | 35% | -0.035% | -0.671% | -0.797% | -29.44 € |
| reversion_bb | 916.74 € (-0.81%) | 32 | 11 | 38% | +0.087% | -1.013% | -1.110% | -7.48 € |
| ruptura_volumen | 881.63 € (-4.61%) | 228 | 6 | 23% | -0.199% | -0.813% | -0.922% | -42.05 € |
| rebote_extremo | 922.29 € (-0.21%) | 10 | 0 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 894.53 € (-3.21%) | 135 | 0 | 14% | -0.271% | -0.966% | -1.072% | -29.72 € |
| macd_momentum | 880.26 € (-4.76%) | 329 | 1 | 21% | -0.014% | -0.593% | -0.703% | -44.12 € |
| estocastico_rebote | 877.68 € (-5.04%) | 268 | 13 | 30% | -0.156% | -0.753% | -0.864% | -45.71 € |
| ruptura_estricta | 886.66 € (-4.07%) | 128 | 7 | 24% | -0.538% | -1.244% | -1.368% | -36.36 € |
| macd_sin_salida | 883.70 € (-4.39%) | 233 | 15 | 35% | -0.121% | -0.733% | -0.849% | -38.91 € |
| c_banda_atr_tope | 912.48 € (-1.27%) | 44 | 3 | 27% | -0.045% | -1.131% | -1.251% | -11.45 € |
| ruptura_volumen_tope | 910.40 € (-1.50%) | 70 | 2 | 27% | +0.038% | -0.839% | -0.954% | -13.50 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 894.03 € (-3.27%) | 205 | 1 | 22% | -0.022% | -0.649% | -0.762% | -30.34 € |
| ruptura_volumen_regimen | 884.17 € (-4.34%) | 183 | 2 | 20% | -0.324% | -0.966% | -1.081% | -40.16 € |
| c_banda_atr_evento | 898.93 € (-2.74%) | 159 | 14 | 36% | +0.022% | -0.644% | -0.763% | -23.48 € |
| macd_momentum_evento | 885.14 € (-4.23%) | 282 | 1 | 18% | -0.021% | -0.614% | -0.719% | -39.24 € |
| ruptura_volumen_evento | 894.17 € (-3.25%) | 178 | 6 | 24% | -0.078% | -0.727% | -0.824% | -29.49 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 13:30 | c_banda_atr_evento | ONDO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 13:30 | estocastico_rebote | VVV | timeout | +0.21% | -0.28% | -0.06 |
| 2026-10-01 13:30 | reversion_bb | OP | timeout | -0.70% | -1.80% | -0.41 |
| 2026-10-01 13:30 | c_banda_atr | ONDO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 13:25 | macd_momentum_evento | XDC | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 13:25 | ruptura_volumen_tope | XDC | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 13:25 | macd_sin_salida | TON | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-01 13:25 | macd_sin_salida | XDC | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 13:25 | estocastico_rebote | AVAX | timeout | -0.29% | -0.79% | -0.17 |
| 2026-10-01 13:25 | macd_momentum | XDC | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 13:25 | reversion_bb | APT | timeout | -0.54% | -1.64% | -0.38 |
| 2026-10-01 13:25 | reversion_bb | LINK | timeout | +0.09% | -1.01% | -0.23 |
| 2026-10-01 13:25 | reversion_bb | XRP | timeout | -0.32% | -1.42% | -0.33 |
| 2026-10-01 13:20 | ruptura_volumen_evento | KSM | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 13:20 | ruptura_volumen_regimen | KAS | stop-loss | -1.33% | -1.83% | -0.41 |

## Eventos de la última vuelta

- 2026-10-01 13:30 [c_banda_atr] CIERRE ONDO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 13:30 [c_banda_atr_evento] CIERRE ONDO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 13:25 [estocastico_rebote] ENTRADA PEPE @ 3.869e-06 (21.96 €, apertura)
- 2026-10-01 13:25 [estocastico_rebote] ENTRADA INJ @ 6.634 (21.96 €, apertura)
- 2026-10-01 13:30 [reversion_bb] CIERRE OP timeout bruto -0.70% neto -1.80%
- 2026-10-01 13:30 [estocastico_rebote] CIERRE VVV timeout bruto +0.21% neto -0.29%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
