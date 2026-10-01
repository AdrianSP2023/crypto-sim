# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 22:51 UTC · vueltas 335 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 883.42 € (-4.42%) | 260 | 25 | 35% | -0.053% | -0.653% | -0.775% | -38.57 € |
| reversion_bb | 916.16 € (-0.87%) | 51 | 17 | 49% | +0.294% | -0.718% | -0.815% | -8.44 € |
| ruptura_volumen | 871.78 € (-5.68%) | 295 | 4 | 24% | -0.201% | -0.789% | -0.897% | -52.46 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.91 € (-3.82%) | 185 | 2 | 15% | -0.200% | -0.842% | -0.932% | -35.38 € |
| macd_momentum | 863.28 € (-6.60%) | 479 | 17 | 21% | -0.007% | -0.561% | -0.665% | -60.25 € |
| estocastico_rebote | 871.58 € (-5.70%) | 324 | 13 | 30% | -0.142% | -0.722% | -0.832% | -52.76 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 872.32 € (-5.62%) | 332 | 23 | 35% | -0.087% | -0.666% | -0.779% | -50.02 € |
| c_banda_atr_tope | 910.72 € (-1.46%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.67 € (-2.01%) | 100 | 3 | 27% | -0.043% | -0.807% | -0.922% | -18.48 € |
| c_banda_atr_regimen | 896.04 € (-3.05%) | 131 | 7 | 31% | -0.214% | -0.913% | -1.049% | -27.37 € |
| macd_momentum_regimen | 885.33 € (-4.21%) | 275 | 1 | 20% | -0.029% | -0.624% | -0.731% | -38.93 € |
| ruptura_volumen_regimen | 875.03 € (-5.32%) | 228 | 2 | 19% | -0.342% | -0.956% | -1.071% | -49.23 € |
| c_banda_atr_evento | 889.30 € (-3.78%) | 227 | 25 | 35% | -0.015% | -0.631% | -0.748% | -32.67 € |
| macd_momentum_evento | 868.06 € (-6.08%) | 432 | 17 | 19% | -0.011% | -0.572% | -0.671% | -55.47 € |
| ruptura_volumen_evento | 884.18 € (-4.33%) | 245 | 4 | 25% | -0.114% | -0.721% | -0.821% | -40.05 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 22:50 | macd_sin_salida | WLD | timeout | -0.52% | -1.01% | -0.22 |
| 2026-10-01 22:50 | estocastico_rebote | LINK | timeout | -0.97% | -1.47% | -0.32 |
| 2026-10-01 22:50 | reversion_bb | USELESS | stop-loss | -1.52% | -2.02% | -0.46 |
| 2026-10-01 22:45 | ruptura_volumen_evento | BCH | timeout | +0.20% | -0.30% | -0.07 |
| 2026-10-01 22:45 | ruptura_volumen_regimen | BCH | timeout | +0.20% | -0.30% | -0.07 |
| 2026-10-01 22:45 | estocastico_rebote | XMR | timeout | +0.38% | -0.12% | -0.03 |
| 2026-10-01 22:45 | ruptura_volumen | BCH | timeout | +0.20% | -0.30% | -0.07 |
| 2026-10-01 22:40 | c_banda_atr_evento | BCH | timeout | +0.34% | -0.16% | -0.04 |
| 2026-10-01 22:40 | c_banda_atr_regimen | BCH | timeout | +0.34% | -0.16% | -0.04 |
| 2026-10-01 22:40 | estocastico_rebote | SHIB | timeout | -0.14% | -0.64% | -0.14 |
| 2026-10-01 22:40 | estocastico_rebote | LTC | timeout | +0.76% | +0.26% | +0.06 |
| 2026-10-01 22:40 | c_banda_atr | BCH | timeout | +0.34% | -0.16% | -0.04 |
| 2026-10-01 22:35 | ruptura_volumen_evento | LTC | timeout | -0.41% | -0.91% | -0.20 |
| 2026-10-01 22:35 | ruptura_volumen_regimen | LTC | timeout | -0.41% | -0.91% | -0.20 |
| 2026-10-01 22:35 | ruptura_volumen_tope | LTC | timeout | -0.41% | -0.91% | -0.21 |

## Eventos de la última vuelta

- 2026-10-01 22:50 [estocastico_rebote] CIERRE LINK timeout bruto -0.97% neto -1.47%
- 2026-10-01 22:50 [macd_sin_salida] CIERRE WLD timeout bruto -0.52% neto -1.02%
- 2026-10-01 22:50 [reversion_bb] CIERRE USELESS stop-loss bruto -1.52% neto -2.02%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
