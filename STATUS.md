# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 03:16 UTC · vueltas 186 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.56 € (-2.89%) | 111 | 15 | 27% | -0.276% | -1.011% | -1.147% | -25.71 € |
| reversion_bb | 918.23 € (-0.65%) | 29 | 6 | 48% | +0.205% | -0.895% | -0.997% | -5.98 € |
| ruptura_volumen | 894.47 € (-3.22%) | 140 | 11 | 21% | -0.214% | -0.901% | -1.030% | -28.76 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.65 € (-2.01%) | 106 | 3 | 26% | -0.020% | -0.766% | -0.895% | -18.61 € |
| macd_momentum | 881.96 € (-4.57%) | 264 | 4 | 17% | -0.106% | -0.705% | -0.817% | -42.19 € |
| estocastico_rebote | 892.32 € (-3.45%) | 183 | 17 | 34% | -0.101% | -0.744% | -0.877% | -31.12 € |
| ruptura_estricta | 904.64 € (-2.12%) | 65 | 4 | 25% | -0.348% | -1.249% | -1.393% | -18.63 € |
| macd_sin_salida | 895.52 € (-3.11%) | 152 | 19 | 30% | -0.114% | -0.786% | -0.911% | -27.30 € |
| c_banda_atr_tope | 910.23 € (-1.52%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.73 € (-1.46%) | 50 | 4 | 18% | -0.106% | -1.134% | -1.258% | -13.03 € |
| c_banda_atr_regimen | 900.55 € (-2.56%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 899.91 € (-2.63%) | 107 | 9 | 20% | -0.228% | -0.972% | -1.106% | -23.78 € |
| c_banda_atr_evento | 900.62 € (-2.56%) | 79 | 15 | 23% | -0.415% | -1.250% | -1.388% | -22.65 € |
| macd_momentum_evento | 894.36 € (-3.23%) | 144 | 4 | 13% | -0.223% | -0.906% | -1.014% | -29.79 € |
| ruptura_volumen_evento | 899.98 € (-2.63%) | 81 | 11 | 14% | -0.427% | -1.253% | -1.386% | -23.24 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 03:15 | ruptura_volumen_evento | ENA | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 03:15 | c_banda_atr_evento | POL | timeout | -1.49% | -1.99% | -0.45 |
| 2026-09-30 03:15 | ruptura_volumen_regimen | ENA | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 03:15 | c_banda_atr_regimen | POL | timeout | -1.49% | -1.99% | -0.45 |
| 2026-09-30 03:15 | estocastico_rebote | USELESS | stop-loss | -1.55% | -2.05% | -0.46 |
| 2026-09-30 03:15 | pullback_tendencia | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 03:15 | ruptura_volumen | ENA | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 03:15 | c_banda_atr | POL | timeout | -1.49% | -1.99% | -0.45 |
| 2026-09-30 03:10 | ruptura_volumen_evento | TRUMP | timeout | -0.17% | -0.67% | -0.15 |
| 2026-09-30 03:10 | ruptura_volumen_evento | TAO | timeout | -0.28% | -0.79% | -0.18 |
| 2026-09-30 03:10 | macd_momentum_evento | FIL | momentum perdido | -0.53% | -1.03% | -0.23 |
| 2026-09-30 03:10 | macd_momentum_evento | ENA | momentum perdido | -1.40% | -1.90% | -0.43 |
| 2026-09-30 03:10 | macd_momentum_evento | DOT | momentum perdido | -0.11% | -0.61% | -0.14 |
| 2026-09-30 03:10 | c_banda_atr_evento | SEI | timeout | -0.72% | -1.22% | -0.28 |
| 2026-09-30 03:10 | c_banda_atr_evento | ZRO | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-09-30 03:15 [pullback_tendencia] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 03:10 [macd_momentum] ENTRADA HBAR @ 0.09139 (22.05 €, apertura)
- 2026-09-30 03:10 [macd_momentum_evento] ENTRADA HBAR @ 0.09139 (22.36 €, apertura)
- 2026-09-30 03:15 [ruptura_volumen] CIERRE ENA stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 03:15 [ruptura_volumen_regimen] CIERRE ENA stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 03:15 [ruptura_volumen_evento] CIERRE ENA stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 03:15 [estocastico_rebote] CIERRE USELESS stop-loss bruto -1.55% neto -2.05%
- 2026-09-30 03:10 [estocastico_rebote] ENTRADA PENGU @ 0.008772 (22.33 €, apertura)
- 2026-09-30 03:15 [c_banda_atr] CIERRE POL timeout bruto -1.49% neto -1.99%
- 2026-09-30 03:15 [c_banda_atr_regimen] CIERRE POL timeout bruto -1.49% neto -1.99%
- 2026-09-30 03:15 [c_banda_atr_evento] CIERRE POL timeout bruto -1.49% neto -1.99%
- 2026-09-30 03:10 [c_banda_atr] ENTRADA ASTER @ 0.66047 (22.46 €, apertura)
- 2026-09-30 03:10 [c_banda_atr_tope] ENTRADA ASTER @ 0.66047 (22.78 €, apertura)
- 2026-09-30 03:10 [c_banda_atr_evento] ENTRADA ASTER @ 0.66047 (22.54 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
