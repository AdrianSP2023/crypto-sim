# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 10:06 UTC · vueltas 191 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.07 € (-2.94%) | 169 | 11 | 36% | -0.010% | -0.664% | -0.786% | -25.71 € |
| reversion_bb | 917.80 € (-0.70%) | 23 | 7 | 35% | -0.013% | -1.113% | -1.221% | -5.91 € |
| ruptura_volumen | 884.81 € (-4.27%) | 208 | 7 | 23% | -0.193% | -0.818% | -0.928% | -38.69 € |
| rebote_extremo | 923.08 € (-0.13%) | 5 | 4 | 60% | +0.548% | -0.552% | -0.686% | -0.64 € |
| pullback_tendencia | 896.85 € (-2.96%) | 124 | 0 | 15% | -0.255% | -0.968% | -1.073% | -27.39 € |
| macd_momentum | 884.84 € (-4.26%) | 297 | 3 | 22% | +0.002% | -0.586% | -0.694% | -39.45 € |
| estocastico_rebote | 881.12 € (-4.67%) | 231 | 26 | 32% | -0.155% | -0.768% | -0.883% | -40.27 € |
| ruptura_estricta | 890.64 € (-3.63%) | 121 | 3 | 26% | -0.481% | -1.199% | -1.325% | -33.21 € |
| macd_sin_salida | 888.13 € (-3.91%) | 220 | 5 | 36% | -0.092% | -0.710% | -0.824% | -35.69 € |
| c_banda_atr_tope | 913.86 € (-1.12%) | 39 | 3 | 28% | +0.022% | -1.078% | -1.194% | -9.67 € |
| ruptura_volumen_tope | 911.98 € (-1.33%) | 61 | 4 | 28% | +0.095% | -0.838% | -0.954% | -11.75 € |
| c_banda_atr_regimen | 902.68 € (-2.33%) | 108 | 1 | 34% | -0.118% | -0.859% | -1.000% | -21.32 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 903.04 € (-2.29%) | 136 | 11 | 37% | +0.063% | -0.631% | -0.744% | -19.73 € |
| macd_momentum_evento | 889.75 € (-3.73%) | 250 | 3 | 20% | -0.003% | -0.608% | -0.711% | -34.54 € |
| ruptura_volumen_evento | 897.40 € (-2.90%) | 158 | 7 | 24% | -0.055% | -0.723% | -0.820% | -26.08 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 10:05 | ruptura_volumen_evento | ALGO | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 10:05 | ruptura_volumen_evento | TRX | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 10:05 | c_banda_atr_evento | ARB | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 10:05 | ruptura_volumen_tope | ALGO | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 10:05 | ruptura_volumen_tope | TRX | timeout | -0.16% | -0.66% | -0.15 |
| 2026-10-01 10:05 | c_banda_atr_tope | ARB | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-10-01 10:05 | macd_sin_salida | TAO | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 10:05 | estocastico_rebote | ASTER | stop-loss | -1.90% | -2.40% | -0.53 |
| 2026-10-01 10:05 | estocastico_rebote | ONDO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 10:05 | estocastico_rebote | FET | stop-loss | -1.50% | -2.00% | -0.35 |
| 2026-10-01 10:05 | estocastico_rebote | ENA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 10:05 | estocastico_rebote | DOT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 10:05 | estocastico_rebote | ZEC | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 10:05 | estocastico_rebote | NEAR | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 10:05 | ruptura_volumen | ALGO | stop-loss | -1.20% | -1.70% | -0.38 |

## Eventos de la última vuelta

- 2026-10-01 10:05 [estocastico_rebote] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:05 [estocastico_rebote] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:00 [macd_momentum] ENTRADA HYPE @ 78.89 (22.12 €, apertura)
- 2026-10-01 10:00 [macd_sin_salida] ENTRADA HYPE @ 78.89 (22.22 €, apertura)
- 2026-10-01 10:00 [macd_momentum_evento] ENTRADA HYPE @ 78.89 (22.24 €, apertura)
- 2026-10-01 10:05 [macd_sin_salida] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:05 [estocastico_rebote] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:05 [c_banda_atr] CIERRE ARB stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:05 [reversion_bb] CIERRE ARB stop-loss bruto -1.50% neto -2.60%
- 2026-10-01 10:05 [c_banda_atr_tope] CIERRE ARB stop-loss bruto -1.50% neto -2.60%
- 2026-10-01 10:05 [c_banda_atr_evento] CIERRE ARB stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:05 [estocastico_rebote] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:05 [estocastico_rebote] CIERRE FET stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:05 [ruptura_volumen] CIERRE TRX timeout bruto -0.16% neto -0.66%
- 2026-10-01 10:05 [ruptura_volumen_tope] CIERRE TRX timeout bruto -0.16% neto -0.66%
- 2026-10-01 10:05 [ruptura_volumen_evento] CIERRE TRX timeout bruto -0.16% neto -0.66%
- 2026-10-01 10:05 [ruptura_volumen] CIERRE ALGO stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 10:05 [ruptura_volumen_tope] CIERRE ALGO stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 10:05 [ruptura_volumen_evento] CIERRE ALGO stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 10:05 [reversion_bb] CIERRE ONDO stop-loss bruto -1.50% neto -2.60%
- 2026-10-01 10:05 [estocastico_rebote] CIERRE ONDO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:05 [estocastico_rebote] CIERRE ASTER stop-loss bruto -1.90% neto -2.40%
- 2026-10-01 10:00 [ruptura_volumen] ENTRADA SKY @ 0.06938 (22.14 €, apertura)
- 2026-10-01 10:00 [ruptura_volumen_tope] ENTRADA SKY @ 0.06938 (22.81 €, apertura)
- 2026-10-01 10:00 [ruptura_volumen_evento] ENTRADA SKY @ 0.06938 (22.45 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
