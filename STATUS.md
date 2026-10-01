# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 13:41 UTC · vueltas 231 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 894.47 € (-3.22%) | 192 | 18 | 35% | -0.035% | -0.671% | -0.797% | -29.44 € |
| reversion_bb | 918.33 € (-0.64%) | 32 | 11 | 38% | +0.087% | -1.013% | -1.110% | -7.48 € |
| ruptura_volumen | 882.39 € (-4.53%) | 228 | 6 | 23% | -0.199% | -0.813% | -0.922% | -42.05 € |
| rebote_extremo | 922.29 € (-0.21%) | 10 | 0 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 894.53 € (-3.21%) | 135 | 0 | 14% | -0.271% | -0.966% | -1.072% | -29.72 € |
| macd_momentum | 880.26 € (-4.76%) | 329 | 1 | 21% | -0.014% | -0.593% | -0.703% | -44.12 € |
| estocastico_rebote | 879.14 € (-4.88%) | 269 | 13 | 30% | -0.161% | -0.758% | -0.868% | -46.15 € |
| ruptura_estricta | 887.68 € (-3.96%) | 128 | 7 | 24% | -0.538% | -1.244% | -1.368% | -36.36 € |
| macd_sin_salida | 885.78 € (-4.16%) | 234 | 14 | 35% | -0.121% | -0.732% | -0.849% | -39.05 € |
| c_banda_atr_tope | 912.94 € (-1.22%) | 44 | 5 | 27% | -0.045% | -1.131% | -1.251% | -11.45 € |
| ruptura_volumen_tope | 910.72 € (-1.46%) | 70 | 2 | 27% | +0.038% | -0.839% | -0.954% | -13.50 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 894.03 € (-3.27%) | 205 | 1 | 22% | -0.022% | -0.649% | -0.762% | -30.34 € |
| ruptura_volumen_regimen | 884.34 € (-4.32%) | 183 | 2 | 20% | -0.324% | -0.966% | -1.081% | -40.16 € |
| c_banda_atr_evento | 900.43 € (-2.58%) | 159 | 18 | 36% | +0.022% | -0.644% | -0.763% | -23.48 € |
| macd_momentum_evento | 885.14 € (-4.23%) | 282 | 1 | 18% | -0.021% | -0.614% | -0.719% | -39.24 € |
| ruptura_volumen_evento | 894.94 € (-3.17%) | 178 | 6 | 24% | -0.078% | -0.727% | -0.824% | -29.49 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 13:40 | macd_sin_salida | RENDER | timeout | -0.12% | -0.62% | -0.14 |
| 2026-10-01 13:35 | estocastico_rebote | MON | stop-loss | -1.50% | -2.00% | -0.44 |
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

## Eventos de la última vuelta

- 2026-10-01 13:35 [c_banda_atr] ENTRADA DOT @ 1.0591 (22.37 €, apertura)
- 2026-10-01 13:35 [c_banda_atr_tope] ENTRADA DOT @ 1.0591 (22.82 €, apertura)
- 2026-10-01 13:35 [c_banda_atr_evento] ENTRADA DOT @ 1.0591 (22.52 €, apertura)
- 2026-10-01 13:35 [c_banda_atr] ENTRADA ARB @ 0.1779 (22.37 €, apertura)
- 2026-10-01 13:35 [c_banda_atr_tope] ENTRADA ARB @ 0.1779 (22.82 €, apertura)
- 2026-10-01 13:35 [c_banda_atr_evento] ENTRADA ARB @ 0.1779 (22.52 €, apertura)
- 2026-10-01 13:35 [estocastico_rebote] ENTRADA ALGO @ 0.11242 (21.95 €, apertura)
- 2026-10-01 13:40 [macd_sin_salida] CIERRE RENDER timeout bruto -0.12% neto -0.62%
- 2026-10-01 13:35 [c_banda_atr] ENTRADA OP @ 0.1148 (22.37 €, apertura)
- 2026-10-01 13:35 [c_banda_atr_evento] ENTRADA OP @ 0.1148 (22.52 €, apertura)
- 2026-10-01 13:35 [c_banda_atr] ENTRADA KSM @ 4.65 (22.37 €, apertura)
- 2026-10-01 13:35 [c_banda_atr_evento] ENTRADA KSM @ 4.65 (22.52 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
