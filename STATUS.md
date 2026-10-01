# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 22:41 UTC · vueltas 333 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.66 € (-4.28%) | 260 | 25 | 35% | -0.053% | -0.653% | -0.775% | -38.57 € |
| reversion_bb | 917.32 € (-0.75%) | 50 | 18 | 50% | +0.330% | -0.692% | -0.789% | -7.97 € |
| ruptura_volumen | 871.90 € (-5.66%) | 294 | 4 | 24% | -0.202% | -0.791% | -0.899% | -52.40 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.04 € (-3.81%) | 185 | 2 | 15% | -0.200% | -0.842% | -0.932% | -35.38 € |
| macd_momentum | 863.99 € (-6.52%) | 479 | 16 | 21% | -0.007% | -0.561% | -0.665% | -60.25 € |
| estocastico_rebote | 872.32 € (-5.62%) | 322 | 15 | 30% | -0.141% | -0.722% | -0.831% | -52.41 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 873.38 € (-5.50%) | 331 | 24 | 35% | -0.086% | -0.665% | -0.778% | -49.80 € |
| c_banda_atr_tope | 911.00 € (-1.43%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.68 € (-2.01%) | 100 | 2 | 27% | -0.043% | -0.807% | -0.922% | -18.48 € |
| c_banda_atr_regimen | 896.36 € (-3.02%) | 131 | 7 | 31% | -0.214% | -0.913% | -1.049% | -27.37 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 275 | 1 | 20% | -0.029% | -0.624% | -0.731% | -38.93 € |
| ruptura_volumen_regimen | 875.12 € (-5.31%) | 227 | 3 | 19% | -0.344% | -0.959% | -1.074% | -49.17 € |
| c_banda_atr_evento | 890.54 € (-3.65%) | 227 | 25 | 35% | -0.015% | -0.631% | -0.748% | -32.67 € |
| macd_momentum_evento | 868.78 € (-6.00%) | 432 | 16 | 19% | -0.011% | -0.572% | -0.671% | -55.47 € |
| ruptura_volumen_evento | 884.30 € (-4.32%) | 244 | 4 | 25% | -0.115% | -0.723% | -0.823% | -39.98 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 22:40 | c_banda_atr_evento | BCH | timeout | +0.34% | -0.16% | -0.04 |
| 2026-10-01 22:40 | c_banda_atr_regimen | BCH | timeout | +0.34% | -0.16% | -0.04 |
| 2026-10-01 22:40 | estocastico_rebote | SHIB | timeout | -0.14% | -0.64% | -0.14 |
| 2026-10-01 22:40 | estocastico_rebote | LTC | timeout | +0.76% | +0.26% | +0.06 |
| 2026-10-01 22:40 | c_banda_atr | BCH | timeout | +0.34% | -0.16% | -0.04 |
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

## Eventos de la última vuelta

- 2026-10-01 22:40 [estocastico_rebote] CIERRE LTC timeout bruto +0.76% neto +0.26%
- 2026-10-01 22:40 [c_banda_atr] CIERRE BCH timeout bruto +0.34% neto -0.16%
- 2026-10-01 22:40 [c_banda_atr_regimen] CIERRE BCH timeout bruto +0.34% neto -0.16%
- 2026-10-01 22:40 [c_banda_atr_evento] CIERRE BCH timeout bruto +0.34% neto -0.16%
- 2026-10-01 22:35 [ruptura_volumen] ENTRADA WLFI @ 0.0497 (21.80 €, apertura)
- 2026-10-01 22:35 [ruptura_volumen_tope] ENTRADA WLFI @ 0.0497 (22.64 €, apertura)
- 2026-10-01 22:35 [ruptura_volumen_evento] ENTRADA WLFI @ 0.0497 (22.11 €, apertura)
- 2026-10-01 22:40 [estocastico_rebote] CIERRE SHIB timeout bruto -0.14% neto -0.64%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
