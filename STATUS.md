# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 01:36 UTC · vueltas 354 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.27 € (-4.32%) | 274 | 25 | 34% | -0.038% | -0.634% | -0.755% | -39.43 € |
| reversion_bb | 917.39 € (-0.74%) | 57 | 15 | 53% | +0.375% | -0.583% | -0.692% | -7.66 € |
| ruptura_volumen | 867.34 € (-6.16%) | 308 | 26 | 24% | -0.225% | -0.810% | -0.917% | -56.07 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.19 € (-3.90%) | 193 | 4 | 15% | -0.201% | -0.837% | -0.925% | -36.66 € |
| macd_momentum | 861.50 € (-6.79%) | 511 | 5 | 21% | +0.001% | -0.550% | -0.652% | -62.84 € |
| estocastico_rebote | 872.30 € (-5.62%) | 339 | 15 | 32% | -0.096% | -0.673% | -0.783% | -51.46 € |
| ruptura_estricta | 882.25 € (-4.54%) | 167 | 11 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 870.86 € (-5.78%) | 356 | 14 | 34% | -0.093% | -0.667% | -0.778% | -53.60 € |
| c_banda_atr_tope | 911.47 € (-1.38%) | 64 | 4 | 30% | +0.028% | -0.884% | -1.001% | -13.00 € |
| ruptura_volumen_tope | 904.64 € (-2.12%) | 105 | 5 | 26% | -0.058% | -0.810% | -0.924% | -19.47 € |
| c_banda_atr_regimen | 896.02 € (-3.05%) | 139 | 7 | 29% | -0.197% | -0.885% | -1.018% | -28.14 € |
| macd_momentum_regimen | 884.34 € (-4.32%) | 285 | 0 | 20% | -0.026% | -0.618% | -0.723% | -39.89 € |
| ruptura_volumen_regimen | 870.58 € (-5.81%) | 239 | 21 | 19% | -0.372% | -0.981% | -1.095% | -52.84 € |
| c_banda_atr_evento | 890.15 € (-3.69%) | 241 | 25 | 34% | -0.001% | -0.611% | -0.727% | -33.53 € |
| macd_momentum_evento | 866.28 € (-6.27%) | 464 | 5 | 19% | -0.001% | -0.558% | -0.657% | -58.06 € |
| ruptura_volumen_evento | 879.68 € (-4.82%) | 258 | 26 | 24% | -0.147% | -0.749% | -0.849% | -43.71 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 01:35 | ruptura_volumen_evento | LINK | timeout | -0.70% | -1.20% | -0.27 |
| 2026-10-02 01:35 | macd_momentum_evento | LTC | momentum perdido | +0.89% | +0.39% | +0.08 |
| 2026-10-02 01:35 | macd_momentum_evento | AAVE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 01:35 | c_banda_atr_evento | WLFI | timeout | +0.40% | -0.10% | -0.02 |
| 2026-10-02 01:35 | macd_momentum_regimen | AAVE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 01:35 | c_banda_atr_regimen | AAVE | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 01:35 | ruptura_volumen_tope | LINK | timeout | -0.70% | -1.20% | -0.27 |
| 2026-10-02 01:35 | c_banda_atr_tope | WLFI | timeout | +0.40% | -0.10% | -0.02 |
| 2026-10-02 01:35 | macd_momentum | LTC | momentum perdido | +0.89% | +0.39% | +0.08 |
| 2026-10-02 01:35 | macd_momentum | AAVE | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 01:35 | ruptura_volumen | LINK | timeout | -0.70% | -1.20% | -0.26 |
| 2026-10-02 01:35 | c_banda_atr | WLFI | timeout | +0.40% | -0.10% | -0.02 |
| 2026-10-02 01:30 | macd_momentum_evento | MINA | momentum perdido | +0.52% | +0.02% | +0.00 |
| 2026-10-02 01:30 | macd_momentum_regimen | MINA | momentum perdido | +0.52% | +0.02% | +0.00 |
| 2026-10-02 01:30 | macd_sin_salida | PUMP | timeout | -0.47% | -0.96% | -0.21 |

## Eventos de la última vuelta

- 2026-10-02 01:35 [ruptura_volumen] CIERRE LINK timeout bruto -0.70% neto -1.20%
- 2026-10-02 01:35 [ruptura_volumen_tope] CIERRE LINK timeout bruto -0.70% neto -1.20%
- 2026-10-02 01:35 [ruptura_volumen_evento] CIERRE LINK timeout bruto -0.70% neto -1.20%
- 2026-10-02 01:30 [ruptura_volumen] ENTRADA AAVE @ 156.04 (21.70 €, apertura)
- 2026-10-02 01:35 [macd_momentum] CIERRE AAVE take-profit bruto +2.00% neto +1.50%
- 2026-10-02 01:30 [ruptura_volumen_tope] ENTRADA AAVE @ 156.04 (22.62 €, apertura)
- 2026-10-02 01:35 [c_banda_atr_regimen] CIERRE AAVE take-profit bruto +2.00% neto +1.50%
- 2026-10-02 01:35 [macd_momentum_regimen] CIERRE AAVE take-profit bruto +2.00% neto +1.50%
- 2026-10-02 01:35 [macd_momentum_evento] CIERRE AAVE take-profit bruto +2.00% neto +1.50%
- 2026-10-02 01:30 [ruptura_volumen_evento] ENTRADA AAVE @ 156.04 (22.01 €, apertura)
- 2026-10-02 01:35 [macd_momentum] CIERRE LTC momentum perdido bruto +0.89% neto +0.39%
- 2026-10-02 01:35 [macd_momentum_evento] CIERRE LTC momentum perdido bruto +0.89% neto +0.39%
- 2026-10-02 01:30 [c_banda_atr] ENTRADA ZRO @ 1.647 (22.12 €, apertura)
- 2026-10-02 01:30 [c_banda_atr_evento] ENTRADA ZRO @ 1.647 (22.27 €, apertura)
- 2026-10-02 01:30 [estocastico_rebote] ENTRADA ARB @ 0.1781 (21.82 €, apertura)
- 2026-10-02 01:30 [estocastico_rebote] ENTRADA WLD @ 0.451 (21.82 €, apertura)
- 2026-10-02 01:30 [macd_momentum] ENTRADA USELESS @ 0.21158 (21.54 €, apertura)
- 2026-10-02 01:30 [macd_sin_salida] ENTRADA USELESS @ 0.21158 (21.77 €, apertura)
- 2026-10-02 01:30 [macd_momentum_evento] ENTRADA USELESS @ 0.21158 (21.65 €, apertura)
- 2026-10-02 01:30 [estocastico_rebote] ENTRADA PEPE @ 3.9e-06 (21.82 €, apertura)
- 2026-10-02 01:30 [macd_momentum] ENTRADA OP @ 0.1149 (21.54 €, apertura)
- 2026-10-02 01:30 [macd_sin_salida] ENTRADA OP @ 0.1149 (21.77 €, apertura)
- 2026-10-02 01:30 [macd_momentum_evento] ENTRADA OP @ 0.1149 (21.65 €, apertura)
- 2026-10-02 01:35 [c_banda_atr] CIERRE WLFI timeout bruto +0.40% neto -0.10%
- 2026-10-02 01:35 [c_banda_atr_tope] CIERRE WLFI timeout bruto +0.40% neto -0.10%
- 2026-10-02 01:35 [c_banda_atr_evento] CIERRE WLFI timeout bruto +0.40% neto -0.10%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
