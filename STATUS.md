# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 22:36 UTC · vueltas 332 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.76 € (-4.27%) | 259 | 26 | 35% | -0.054% | -0.655% | -0.777% | -38.54 € |
| reversion_bb | 917.37 € (-0.74%) | 50 | 18 | 50% | +0.330% | -0.692% | -0.789% | -7.97 € |
| ruptura_volumen | 871.86 € (-5.67%) | 294 | 3 | 24% | -0.202% | -0.791% | -0.899% | -52.40 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.97 € (-3.82%) | 185 | 2 | 15% | -0.200% | -0.842% | -0.932% | -35.38 € |
| macd_momentum | 863.73 € (-6.55%) | 479 | 16 | 21% | -0.007% | -0.561% | -0.665% | -60.25 € |
| estocastico_rebote | 872.18 € (-5.63%) | 320 | 17 | 30% | -0.143% | -0.725% | -0.835% | -52.32 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 873.08 € (-5.54%) | 331 | 24 | 35% | -0.086% | -0.665% | -0.778% | -49.80 € |
| c_banda_atr_tope | 910.93 € (-1.44%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.68 € (-2.01%) | 100 | 1 | 27% | -0.043% | -0.807% | -0.922% | -18.48 € |
| c_banda_atr_regimen | 896.48 € (-3.00%) | 130 | 8 | 31% | -0.218% | -0.919% | -1.055% | -27.34 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 275 | 1 | 20% | -0.029% | -0.624% | -0.731% | -38.93 € |
| ruptura_volumen_regimen | 875.08 € (-5.32%) | 227 | 3 | 19% | -0.344% | -0.959% | -1.074% | -49.17 € |
| c_banda_atr_evento | 890.65 € (-3.63%) | 226 | 26 | 35% | -0.017% | -0.634% | -0.750% | -32.64 € |
| macd_momentum_evento | 868.52 € (-6.03%) | 432 | 16 | 19% | -0.011% | -0.572% | -0.671% | -55.47 € |
| ruptura_volumen_evento | 884.26 € (-4.33%) | 244 | 3 | 25% | -0.115% | -0.723% | -0.823% | -39.98 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 22:35 | ruptura_volumen_evento | LTC | timeout | -0.41% | -0.91% | -0.20 |
| 2026-10-01 22:35 | ruptura_volumen_regimen | LTC | timeout | -0.41% | -0.91% | -0.20 |
| 2026-10-01 22:35 | ruptura_volumen_tope | LTC | timeout | -0.41% | -0.91% | -0.21 |
| 2026-10-01 22:35 | ruptura_volumen | LTC | timeout | -0.41% | -0.91% | -0.20 |
| 2026-10-01 22:30 | macd_momentum_evento | XMR | momentum perdido | +0.06% | -0.44% | -0.10 |
| 2026-10-01 22:30 | macd_momentum_regimen | XMR | momentum perdido | +0.06% | -0.44% | -0.10 |
| 2026-10-01 22:30 | estocastico_rebote | PUMP | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-01 22:30 | macd_momentum | XMR | momentum perdido | +0.06% | -0.44% | -0.10 |
| 2026-10-01 22:20 | ruptura_volumen_evento | ICP | timeout | -0.58% | -1.08% | -0.24 |
| 2026-10-01 22:20 | ruptura_volumen_regimen | ICP | timeout | -0.58% | -1.08% | -0.24 |
| 2026-10-01 22:20 | ruptura_volumen_tope | ICP | timeout | -0.58% | -1.08% | -0.25 |
| 2026-10-01 22:20 | estocastico_rebote | VVV | timeout | +0.30% | -0.20% | -0.04 |
| 2026-10-01 22:20 | ruptura_volumen | ICP | timeout | -0.58% | -1.08% | -0.24 |
| 2026-10-01 22:15 | estocastico_rebote | UNI | timeout | -0.21% | -0.71% | -0.16 |
| 2026-10-01 22:10 | macd_momentum_evento | SKY | momentum perdido | -0.13% | -0.63% | -0.14 |

## Eventos de la última vuelta

- 2026-10-01 22:30 [macd_momentum] ENTRADA PUMP @ 0.00516 (21.60 €, apertura)
- 2026-10-01 22:30 [macd_sin_salida] ENTRADA PUMP @ 0.00516 (21.86 €, apertura)
- 2026-10-01 22:30 [macd_momentum_evento] ENTRADA PUMP @ 0.00516 (21.72 €, apertura)
- 2026-10-01 22:35 [ruptura_volumen] CIERRE LTC timeout bruto -0.41% neto -0.91%
- 2026-10-01 22:35 [ruptura_volumen_tope] CIERRE LTC timeout bruto -0.41% neto -0.91%
- 2026-10-01 22:35 [ruptura_volumen_regimen] CIERRE LTC timeout bruto -0.41% neto -0.91%
- 2026-10-01 22:35 [ruptura_volumen_evento] CIERRE LTC timeout bruto -0.41% neto -0.91%
- 2026-10-01 22:30 [macd_momentum] ENTRADA WLD @ 0.444 (21.60 €, apertura)
- 2026-10-01 22:30 [macd_momentum_evento] ENTRADA WLD @ 0.444 (21.72 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
