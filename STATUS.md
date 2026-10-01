# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 23:06 UTC · vueltas 338 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.42 € (-4.31%) | 260 | 26 | 35% | -0.053% | -0.653% | -0.775% | -38.57 € |
| reversion_bb | 917.02 € (-0.78%) | 51 | 17 | 49% | +0.294% | -0.718% | -0.815% | -8.44 € |
| ruptura_volumen | 871.61 € (-5.69%) | 297 | 2 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.09 € (-3.80%) | 185 | 5 | 15% | -0.200% | -0.842% | -0.932% | -35.38 € |
| macd_momentum | 863.79 € (-6.54%) | 481 | 15 | 21% | -0.007% | -0.561% | -0.664% | -60.46 € |
| estocastico_rebote | 871.85 € (-5.67%) | 325 | 12 | 30% | -0.135% | -0.716% | -0.825% | -52.45 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 872.60 € (-5.59%) | 336 | 19 | 35% | -0.092% | -0.670% | -0.783% | -50.89 € |
| c_banda_atr_tope | 911.07 € (-1.43%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.78 € (-2.00%) | 100 | 3 | 27% | -0.043% | -0.807% | -0.922% | -18.48 € |
| c_banda_atr_regimen | 896.39 € (-3.01%) | 131 | 7 | 31% | -0.214% | -0.913% | -1.049% | -27.37 € |
| macd_momentum_regimen | 885.23 € (-4.22%) | 276 | 0 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 874.82 € (-5.35%) | 230 | 0 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 890.31 € (-3.67%) | 227 | 26 | 35% | -0.015% | -0.631% | -0.748% | -32.67 € |
| macd_momentum_evento | 868.57 € (-6.02%) | 434 | 15 | 19% | -0.011% | -0.572% | -0.671% | -55.68 € |
| ruptura_volumen_evento | 884.01 € (-4.35%) | 247 | 2 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 23:05 | ruptura_volumen_evento | SKY | timeout | -0.47% | -0.97% | -0.21 |
| 2026-10-01 23:05 | macd_momentum_evento | BNB | momentum perdido | +0.15% | -0.35% | -0.08 |
| 2026-10-01 23:05 | ruptura_volumen_regimen | SKY | timeout | -0.47% | -0.97% | -0.21 |
| 2026-10-01 23:05 | macd_momentum_regimen | BNB | momentum perdido | +0.15% | -0.35% | -0.08 |
| 2026-10-01 23:05 | macd_sin_salida | SHIB | timeout | -1.06% | -1.56% | -0.34 |
| 2026-10-01 23:05 | macd_momentum | BNB | momentum perdido | +0.15% | -0.35% | -0.08 |
| 2026-10-01 23:05 | ruptura_volumen | SKY | timeout | -0.47% | -0.97% | -0.21 |
| 2026-10-01 23:00 | macd_sin_salida | BCH | timeout | +0.47% | -0.03% | -0.01 |
| 2026-10-01 22:55 | ruptura_volumen_evento | TON | timeout | +0.65% | +0.15% | +0.03 |
| 2026-10-01 22:55 | macd_momentum_evento | SPX | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-10-01 22:55 | ruptura_volumen_regimen | TON | timeout | +0.65% | +0.15% | +0.03 |
| 2026-10-01 22:55 | macd_sin_salida | ARB | timeout | -0.84% | -1.34% | -0.30 |
| 2026-10-01 22:55 | macd_sin_salida | UNI | timeout | -0.53% | -1.03% | -0.23 |
| 2026-10-01 22:55 | estocastico_rebote | MINA | take-profit | +1.89% | +1.39% | +0.30 |
| 2026-10-01 22:55 | macd_momentum | SPX | momentum perdido | -0.13% | -0.63% | -0.14 |

## Eventos de la última vuelta

- 2026-10-01 23:00 [c_banda_atr] ENTRADA ZEC @ 1186.41 (22.14 €, apertura)
- 2026-10-01 23:00 [c_banda_atr_evento] ENTRADA ZEC @ 1186.41 (22.29 €, apertura)
- 2026-10-01 23:05 [macd_sin_salida] CIERRE SHIB timeout bruto -1.07% neto -1.57%
- 2026-10-01 23:05 [macd_momentum] CIERRE BNB momentum perdido bruto +0.15% neto -0.35%
- 2026-10-01 23:05 [macd_momentum_regimen] CIERRE BNB momentum perdido bruto +0.15% neto -0.35%
- 2026-10-01 23:05 [macd_momentum_evento] CIERRE BNB momentum perdido bruto +0.15% neto -0.35%
- 2026-10-01 23:05 [ruptura_volumen] CIERRE SKY timeout bruto -0.47% neto -0.97%
- 2026-10-01 23:05 [ruptura_volumen_regimen] CIERRE SKY timeout bruto -0.47% neto -0.97%
- 2026-10-01 23:05 [ruptura_volumen_evento] CIERRE SKY timeout bruto -0.47% neto -0.97%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
