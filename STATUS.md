# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 13:46 UTC · vueltas 232 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 894.48 € (-3.22%) | 192 | 24 | 35% | -0.035% | -0.671% | -0.797% | -29.44 € |
| reversion_bb | 918.47 € (-0.62%) | 32 | 11 | 38% | +0.087% | -1.013% | -1.110% | -7.48 € |
| ruptura_volumen | 882.22 € (-4.55%) | 228 | 9 | 23% | -0.199% | -0.813% | -0.922% | -42.05 € |
| rebote_extremo | 922.29 € (-0.21%) | 10 | 0 | 50% | +0.254% | -0.846% | -1.015% | -1.95 € |
| pullback_tendencia | 894.53 € (-3.21%) | 135 | 0 | 14% | -0.271% | -0.966% | -1.072% | -29.72 € |
| macd_momentum | 880.18 € (-4.77%) | 329 | 12 | 21% | -0.014% | -0.593% | -0.703% | -44.12 € |
| estocastico_rebote | 878.88 € (-4.91%) | 269 | 15 | 30% | -0.161% | -0.758% | -0.868% | -46.15 € |
| ruptura_estricta | 887.20 € (-4.01%) | 130 | 5 | 24% | -0.535% | -1.238% | -1.361% | -36.74 € |
| macd_sin_salida | 885.21 € (-4.22%) | 238 | 17 | 35% | -0.114% | -0.724% | -0.839% | -39.24 € |
| c_banda_atr_tope | 912.96 € (-1.22%) | 44 | 5 | 27% | -0.045% | -1.131% | -1.251% | -11.45 € |
| ruptura_volumen_tope | 910.55 € (-1.48%) | 70 | 5 | 27% | +0.038% | -0.839% | -0.954% | -13.50 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 894.03 € (-3.27%) | 205 | 1 | 22% | -0.022% | -0.649% | -0.762% | -30.34 € |
| ruptura_volumen_regimen | 884.29 € (-4.32%) | 183 | 2 | 20% | -0.324% | -0.966% | -1.081% | -40.16 € |
| c_banda_atr_evento | 900.43 € (-2.58%) | 159 | 24 | 36% | +0.022% | -0.644% | -0.763% | -23.48 € |
| macd_momentum_evento | 885.06 € (-4.24%) | 282 | 12 | 18% | -0.021% | -0.614% | -0.719% | -39.24 € |
| ruptura_volumen_evento | 894.78 € (-3.19%) | 178 | 9 | 24% | -0.078% | -0.727% | -0.824% | -29.49 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 13:45 | macd_sin_salida | BCH | timeout | +0.08% | -0.42% | -0.09 |
| 2026-10-01 13:45 | macd_sin_salida | LINK | timeout | +0.69% | +0.19% | +0.04 |
| 2026-10-01 13:45 | macd_sin_salida | ETH | timeout | +0.18% | -0.32% | -0.07 |
| 2026-10-01 13:45 | macd_sin_salida | XRP | timeout | +0.18% | -0.32% | -0.07 |
| 2026-10-01 13:45 | ruptura_estricta | BNB | timeout | -0.06% | -0.56% | -0.12 |
| 2026-10-01 13:45 | ruptura_estricta | HYPE | timeout | -0.68% | -1.18% | -0.26 |
| 2026-10-01 13:40 | macd_sin_salida | RENDER | timeout | -0.12% | -0.62% | -0.14 |
| 2026-10-01 13:35 | estocastico_rebote | MON | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 13:30 | c_banda_atr_evento | ONDO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 13:30 | estocastico_rebote | VVV | timeout | +0.21% | -0.28% | -0.06 |
| 2026-10-01 13:30 | reversion_bb | OP | timeout | -0.70% | -1.80% | -0.41 |
| 2026-10-01 13:30 | c_banda_atr | ONDO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 13:25 | macd_momentum_evento | XDC | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 13:25 | ruptura_volumen_tope | XDC | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 13:25 | macd_sin_salida | TON | timeout | +0.00% | -0.50% | -0.11 |

## Eventos de la última vuelta

- 2026-10-01 13:40 [c_banda_atr] ENTRADA BTC @ 74217.5 (22.37 €, apertura)
- 2026-10-01 13:40 [c_banda_atr_evento] ENTRADA BTC @ 74217.5 (22.52 €, apertura)
- 2026-10-01 13:40 [c_banda_atr] ENTRADA XRP @ 1.31793 (22.37 €, apertura)
- 2026-10-01 13:45 [macd_sin_salida] CIERRE XRP timeout bruto +0.18% neto -0.32%
- 2026-10-01 13:40 [c_banda_atr_evento] ENTRADA XRP @ 1.31793 (22.52 €, apertura)
- 2026-10-01 13:45 [macd_sin_salida] CIERRE ETH timeout bruto +0.18% neto -0.32%
- 2026-10-01 13:40 [macd_momentum] ENTRADA SOL @ 104.2 (22.00 €, apertura)
- 2026-10-01 13:40 [macd_sin_salida] ENTRADA SOL @ 104.2 (22.13 €, apertura)
- 2026-10-01 13:40 [macd_momentum_evento] ENTRADA SOL @ 104.2 (22.13 €, apertura)
- 2026-10-01 13:45 [macd_sin_salida] CIERRE LINK timeout bruto +0.69% neto +0.19%
- 2026-10-01 13:40 [c_banda_atr] ENTRADA ADA @ 0.219163 (22.37 €, apertura)
- 2026-10-01 13:40 [c_banda_atr_evento] ENTRADA ADA @ 0.219163 (22.52 €, apertura)
- 2026-10-01 13:40 [macd_momentum] ENTRADA AVAX @ 9.74 (22.00 €, apertura)
- 2026-10-01 13:40 [macd_sin_salida] ENTRADA AVAX @ 9.74 (22.13 €, apertura)
- 2026-10-01 13:40 [macd_momentum_evento] ENTRADA AVAX @ 9.74 (22.13 €, apertura)
- 2026-10-01 13:40 [ruptura_volumen] ENTRADA HBAR @ 0.09341 (22.05 €, apertura)
- 2026-10-01 13:40 [ruptura_volumen_tope] ENTRADA HBAR @ 0.09341 (22.77 €, apertura)
- 2026-10-01 13:40 [ruptura_volumen_evento] ENTRADA HBAR @ 0.09341 (22.37 €, apertura)
- 2026-10-01 13:45 [ruptura_estricta] CIERRE HYPE timeout bruto -0.68% neto -1.18%
- 2026-10-01 13:40 [c_banda_atr] ENTRADA TAO @ 268.376 (22.37 €, apertura)
- 2026-10-01 13:40 [c_banda_atr_evento] ENTRADA TAO @ 268.376 (22.52 €, apertura)
- 2026-10-01 13:40 [macd_momentum] ENTRADA UNI @ 7.9947 (22.00 €, apertura)
- 2026-10-01 13:40 [macd_momentum_evento] ENTRADA UNI @ 7.9947 (22.13 €, apertura)
- 2026-10-01 13:40 [ruptura_volumen] ENTRADA ARB @ 0.1785 (22.05 €, apertura)
- 2026-10-01 13:40 [macd_momentum] ENTRADA ARB @ 0.1785 (22.00 €, apertura)
- 2026-10-01 13:40 [macd_sin_salida] ENTRADA ARB @ 0.1785 (22.13 €, apertura)
- 2026-10-01 13:40 [ruptura_volumen_tope] ENTRADA ARB @ 0.1785 (22.77 €, apertura)
- 2026-10-01 13:40 [macd_momentum_evento] ENTRADA ARB @ 0.1785 (22.13 €, apertura)
- 2026-10-01 13:40 [ruptura_volumen_evento] ENTRADA ARB @ 0.1785 (22.37 €, apertura)
- 2026-10-01 13:40 [macd_momentum] ENTRADA ICP @ 2.928 (22.00 €, apertura)
- 2026-10-01 13:40 [macd_sin_salida] ENTRADA ICP @ 2.928 (22.13 €, apertura)
- 2026-10-01 13:40 [macd_momentum_evento] ENTRADA ICP @ 2.928 (22.13 €, apertura)
- 2026-10-01 13:40 [estocastico_rebote] ENTRADA XDC @ 0.03095 (21.95 €, apertura)
- 2026-10-01 13:40 [estocastico_rebote] ENTRADA NIGHT @ 0.03511 (21.95 €, apertura)
- 2026-10-01 13:45 [macd_sin_salida] CIERRE BCH timeout bruto +0.08% neto -0.42%
- 2026-10-01 13:40 [macd_momentum] ENTRADA OP @ 0.1149 (22.00 €, apertura)
- 2026-10-01 13:40 [macd_momentum_evento] ENTRADA OP @ 0.1149 (22.13 €, apertura)
- 2026-10-01 13:40 [macd_momentum] ENTRADA KSM @ 4.61 (22.00 €, apertura)
- 2026-10-01 13:40 [macd_momentum_evento] ENTRADA KSM @ 4.61 (22.13 €, apertura)
- 2026-10-01 13:40 [macd_momentum] ENTRADA TRUMP @ 1.834 (22.00 €, apertura)
- 2026-10-01 13:40 [macd_sin_salida] ENTRADA TRUMP @ 1.834 (22.13 €, apertura)
- 2026-10-01 13:40 [macd_momentum_evento] ENTRADA TRUMP @ 1.834 (22.13 €, apertura)
- 2026-10-01 13:40 [c_banda_atr] ENTRADA BNB @ 681.97 (22.37 €, apertura)
- 2026-10-01 13:45 [ruptura_estricta] CIERRE BNB timeout bruto -0.06% neto -0.56%
- 2026-10-01 13:40 [c_banda_atr_evento] ENTRADA BNB @ 681.97 (22.52 €, apertura)
- 2026-10-01 13:40 [macd_momentum] ENTRADA TON @ 1.334 (22.00 €, apertura)
- 2026-10-01 13:40 [macd_sin_salida] ENTRADA TON @ 1.334 (22.13 €, apertura)
- 2026-10-01 13:40 [macd_momentum_evento] ENTRADA TON @ 1.334 (22.13 €, apertura)
- 2026-10-01 13:40 [c_banda_atr] ENTRADA SKY @ 0.06984 (22.37 €, apertura)
- 2026-10-01 13:40 [c_banda_atr_evento] ENTRADA SKY @ 0.06984 (22.52 €, apertura)
- 2026-10-01 13:40 [ruptura_volumen] ENTRADA SEI @ 0.0648 (22.05 €, apertura)
- 2026-10-01 13:40 [macd_momentum] ENTRADA SEI @ 0.0648 (22.00 €, apertura)
- 2026-10-01 13:40 [ruptura_volumen_tope] ENTRADA SEI @ 0.0648 (22.77 €, apertura)
- 2026-10-01 13:40 [macd_momentum_evento] ENTRADA SEI @ 0.0648 (22.13 €, apertura)
- 2026-10-01 13:40 [ruptura_volumen_evento] ENTRADA SEI @ 0.0648 (22.37 €, apertura)
- 2026-10-01 13:40 [macd_momentum] ENTRADA APT @ 0.6826 (22.00 €, apertura)
- 2026-10-01 13:40 [macd_sin_salida] ENTRADA APT @ 0.6826 (22.13 €, apertura)
- 2026-10-01 13:40 [macd_momentum_evento] ENTRADA APT @ 0.6826 (22.13 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
