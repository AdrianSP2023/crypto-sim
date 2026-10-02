# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 02:16 UTC · vueltas 362 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.32 € (-3.99%) | 287 | 24 | 35% | -0.011% | -0.602% | -0.723% | -39.26 € |
| reversion_bb | 919.67 € (-0.49%) | 62 | 10 | 55% | +0.447% | -0.474% | -0.582% | -6.78 € |
| ruptura_volumen | 868.36 € (-6.05%) | 323 | 27 | 24% | -0.214% | -0.795% | -0.903% | -57.66 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.96 € (-3.82%) | 194 | 5 | 15% | -0.189% | -0.825% | -0.913% | -36.33 € |
| macd_momentum | 864.36 € (-6.48%) | 518 | 37 | 21% | +0.005% | -0.545% | -0.647% | -63.18 € |
| estocastico_rebote | 873.91 € (-5.45%) | 342 | 13 | 32% | -0.095% | -0.671% | -0.781% | -51.81 € |
| ruptura_estricta | 883.43 € (-4.42%) | 167 | 24 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 875.44 € (-5.28%) | 360 | 40 | 34% | -0.080% | -0.652% | -0.764% | -53.06 € |
| c_banda_atr_tope | 912.08 € (-1.32%) | 66 | 5 | 30% | +0.050% | -0.850% | -0.964% | -12.88 € |
| ruptura_volumen_tope | 903.70 € (-2.22%) | 110 | 5 | 25% | -0.103% | -0.843% | -0.959% | -21.22 € |
| c_banda_atr_regimen | 898.38 € (-2.80%) | 139 | 26 | 29% | -0.197% | -0.885% | -1.018% | -28.14 € |
| macd_momentum_regimen | 886.81 € (-4.05%) | 286 | 31 | 20% | -0.019% | -0.610% | -0.715% | -39.56 € |
| ruptura_volumen_regimen | 872.76 € (-5.57%) | 249 | 23 | 20% | -0.340% | -0.945% | -1.058% | -53.00 € |
| c_banda_atr_evento | 893.22 € (-3.36%) | 254 | 24 | 35% | +0.027% | -0.577% | -0.692% | -33.37 € |
| macd_momentum_evento | 869.15 € (-5.96%) | 471 | 37 | 19% | +0.003% | -0.553% | -0.652% | -58.41 € |
| ruptura_volumen_evento | 880.72 € (-4.71%) | 273 | 27 | 25% | -0.138% | -0.735% | -0.835% | -45.33 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 02:15 | ruptura_volumen_evento | APT | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 02:15 | ruptura_volumen_evento | INJ | timeout | +0.85% | +0.35% | +0.08 |
| 2026-10-02 02:15 | ruptura_volumen_evento | NIGHT | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 02:15 | ruptura_volumen_evento | XDC | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-02 02:15 | ruptura_volumen_evento | FET | timeout | +1.55% | +1.05% | +0.23 |
| 2026-10-02 02:15 | ruptura_volumen_evento | QNT | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 02:15 | macd_momentum_evento | APT | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 02:15 | ruptura_volumen_regimen | APT | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 02:15 | ruptura_volumen_regimen | INJ | timeout | +0.85% | +0.35% | +0.08 |
| 2026-10-02 02:15 | ruptura_volumen_regimen | XDC | timeout | -0.36% | -0.86% | -0.19 |
| 2026-10-02 02:15 | ruptura_volumen_regimen | FET | timeout | +1.55% | +1.05% | +0.23 |
| 2026-10-02 02:15 | ruptura_volumen_regimen | QNT | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 02:15 | macd_momentum_regimen | APT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 02:15 | ruptura_volumen_tope | NIGHT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 02:15 | macd_sin_salida | APT | take-profit | +2.00% | +1.50% | +0.33 |

## Eventos de la última vuelta

- 2026-10-02 02:10 [ruptura_volumen] ENTRADA XRP @ 1.33574 (21.67 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_regimen] ENTRADA XRP @ 1.33574 (21.78 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_evento] ENTRADA XRP @ 1.33574 (21.98 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen] ENTRADA QNT @ 231.9 (21.67 €, apertura)
- 2026-10-02 02:15 [ruptura_volumen] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 02:10 [ruptura_estricta] ENTRADA QNT @ 231.9 (22.06 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_regimen] ENTRADA QNT @ 231.9 (21.78 €, apertura)
- 2026-10-02 02:15 [ruptura_volumen_regimen] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 02:10 [ruptura_volumen_evento] ENTRADA QNT @ 231.9 (21.98 €, apertura)
- 2026-10-02 02:15 [ruptura_volumen_evento] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 02:10 [ruptura_volumen] ENTRADA ZEC @ 1194.13 (21.66 €, apertura)
- 2026-10-02 02:10 [ruptura_estricta] ENTRADA ZEC @ 1194.13 (22.06 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_regimen] ENTRADA ZEC @ 1194.13 (21.77 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_evento] ENTRADA ZEC @ 1194.13 (21.97 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen] ENTRADA TAO @ 272.671 (21.66 €, apertura)
- 2026-10-02 02:10 [ruptura_estricta] ENTRADA TAO @ 272.671 (22.06 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_regimen] ENTRADA TAO @ 272.671 (21.77 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_evento] ENTRADA TAO @ 272.671 (21.97 €, apertura)
- 2026-10-02 02:10 [c_banda_atr] ENTRADA ZRO @ 1.651 (22.12 €, apertura)
- 2026-10-02 02:10 [c_banda_atr_regimen] ENTRADA ZRO @ 1.651 (22.40 €, apertura)
- 2026-10-02 02:10 [c_banda_atr_evento] ENTRADA ZRO @ 1.651 (22.27 €, apertura)
- 2026-10-02 02:15 [ruptura_volumen] CIERRE FET timeout bruto +1.55% neto +1.05%
- 2026-10-02 02:15 [ruptura_volumen_regimen] CIERRE FET timeout bruto +1.55% neto +1.05%
- 2026-10-02 02:15 [ruptura_volumen_evento] CIERRE FET timeout bruto +1.55% neto +1.05%
- 2026-10-02 02:10 [ruptura_volumen] ENTRADA POL @ 0.09664 (21.67 €, apertura)
- 2026-10-02 02:10 [ruptura_estricta] ENTRADA POL @ 0.09664 (22.06 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_regimen] ENTRADA POL @ 0.09664 (21.77 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_evento] ENTRADA POL @ 0.09664 (21.97 €, apertura)
- 2026-10-02 02:10 [macd_momentum] ENTRADA ONDO @ 0.44069 (21.52 €, apertura)
- 2026-10-02 02:10 [macd_sin_salida] ENTRADA ONDO @ 0.44069 (21.77 €, apertura)
- 2026-10-02 02:10 [macd_momentum_regimen] ENTRADA ONDO @ 0.44069 (22.11 €, apertura)
- 2026-10-02 02:10 [macd_momentum_evento] ENTRADA ONDO @ 0.44069 (21.64 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen] ENTRADA WLD @ 0.4555 (21.67 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_regimen] ENTRADA WLD @ 0.4555 (21.77 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_evento] ENTRADA WLD @ 0.4555 (21.97 €, apertura)
- 2026-10-02 02:15 [ruptura_volumen] CIERRE XDC timeout bruto -0.36% neto -0.86%
- 2026-10-02 02:15 [ruptura_volumen_regimen] CIERRE XDC timeout bruto -0.36% neto -0.86%
- 2026-10-02 02:15 [ruptura_volumen_evento] CIERRE XDC timeout bruto -0.36% neto -0.86%
- 2026-10-02 02:15 [ruptura_volumen] CIERRE NIGHT stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 02:15 [ruptura_volumen_tope] CIERRE NIGHT stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 02:15 [ruptura_volumen_evento] CIERRE NIGHT stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 02:10 [ruptura_volumen] ENTRADA JUP @ 0.29653 (21.65 €, apertura)
- 2026-10-02 02:10 [macd_momentum] ENTRADA JUP @ 0.29653 (21.52 €, apertura)
- 2026-10-02 02:10 [macd_sin_salida] ENTRADA JUP @ 0.29653 (21.77 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_tope] ENTRADA JUP @ 0.29653 (22.58 €, apertura)
- 2026-10-02 02:10 [macd_momentum_regimen] ENTRADA JUP @ 0.29653 (22.11 €, apertura)
- 2026-10-02 02:10 [macd_momentum_evento] ENTRADA JUP @ 0.29653 (21.64 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_evento] ENTRADA JUP @ 0.29653 (21.96 €, apertura)
- 2026-10-02 02:15 [ruptura_volumen] CIERRE INJ timeout bruto +0.85% neto +0.35%
- 2026-10-02 02:15 [ruptura_volumen_regimen] CIERRE INJ timeout bruto +0.85% neto +0.35%
- 2026-10-02 02:15 [ruptura_volumen_evento] CIERRE INJ timeout bruto +0.85% neto +0.35%
- 2026-10-02 02:10 [ruptura_volumen] ENTRADA FIL @ 0.908 (21.65 €, apertura)
- 2026-10-02 02:10 [macd_momentum] ENTRADA FIL @ 0.908 (21.52 €, apertura)
- 2026-10-02 02:10 [macd_sin_salida] ENTRADA FIL @ 0.908 (21.77 €, apertura)
- 2026-10-02 02:10 [macd_momentum_regimen] ENTRADA FIL @ 0.908 (22.11 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_regimen] ENTRADA FIL @ 0.908 (21.77 €, apertura)
- 2026-10-02 02:10 [macd_momentum_evento] ENTRADA FIL @ 0.908 (21.64 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_evento] ENTRADA FIL @ 0.908 (21.96 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen] ENTRADA SHIB @ 5.159e-06 (21.65 €, apertura)
- 2026-10-02 02:10 [ruptura_estricta] ENTRADA SHIB @ 5.159e-06 (22.06 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_evento] ENTRADA SHIB @ 5.159e-06 (21.96 €, apertura)
- 2026-10-02 02:15 [reversion_bb] CIERRE PENGU take-profit bruto +1.94% neto +1.44%
- 2026-10-02 02:10 [macd_momentum] ENTRADA TON @ 1.394 (21.52 €, apertura)
- 2026-10-02 02:10 [macd_sin_salida] ENTRADA TON @ 1.394 (21.77 €, apertura)
- 2026-10-02 02:10 [c_banda_atr_regimen] ENTRADA TON @ 1.394 (22.40 €, apertura)
- 2026-10-02 02:10 [macd_momentum_regimen] ENTRADA TON @ 1.394 (22.11 €, apertura)
- 2026-10-02 02:10 [macd_momentum_evento] ENTRADA TON @ 1.394 (21.64 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen] ENTRADA SEI @ 0.06314 (21.65 €, apertura)
- 2026-10-02 02:10 [ruptura_estricta] ENTRADA SEI @ 0.06314 (22.06 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_regimen] ENTRADA SEI @ 0.06314 (21.77 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_evento] ENTRADA SEI @ 0.06314 (21.96 €, apertura)
- 2026-10-02 02:15 [ruptura_volumen] CIERRE APT take-profit bruto +2.50% neto +2.00%
- 2026-10-02 02:15 [macd_momentum] CIERRE APT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 02:15 [macd_sin_salida] CIERRE APT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 02:15 [macd_momentum_regimen] CIERRE APT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 02:15 [ruptura_volumen_regimen] CIERRE APT take-profit bruto +2.50% neto +2.00%
- 2026-10-02 02:15 [macd_momentum_evento] CIERRE APT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 02:15 [ruptura_volumen_evento] CIERRE APT take-profit bruto +2.50% neto +2.00%
- 2026-10-02 02:10 [ruptura_volumen] ENTRADA SPX @ 0.3945 (21.66 €, apertura)
- 2026-10-02 02:10 [macd_momentum] ENTRADA SPX @ 0.3945 (21.53 €, apertura)
- 2026-10-02 02:10 [ruptura_estricta] ENTRADA SPX @ 0.3945 (22.06 €, apertura)
- 2026-10-02 02:10 [macd_sin_salida] ENTRADA SPX @ 0.3945 (21.78 €, apertura)
- 2026-10-02 02:10 [macd_momentum_regimen] ENTRADA SPX @ 0.3945 (22.12 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_regimen] ENTRADA SPX @ 0.3945 (21.78 €, apertura)
- 2026-10-02 02:10 [macd_momentum_evento] ENTRADA SPX @ 0.3945 (21.65 €, apertura)
- 2026-10-02 02:10 [ruptura_volumen_evento] ENTRADA SPX @ 0.3945 (21.97 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
