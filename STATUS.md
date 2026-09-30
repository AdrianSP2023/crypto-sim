# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 05:41 UTC · vueltas 215 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.41 € (-2.69%) | 123 | 30 | 28% | -0.253% | -0.965% | -1.100% | -27.17 € |
| reversion_bb | 918.36 € (-0.64%) | 32 | 7 | 50% | +0.236% | -0.864% | -0.973% | -6.38 € |
| ruptura_volumen | 893.06 € (-3.37%) | 155 | 18 | 19% | -0.261% | -0.929% | -1.055% | -32.79 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.08 € (-2.07%) | 112 | 4 | 26% | -0.024% | -0.757% | -0.883% | -19.44 € |
| macd_momentum | 880.13 € (-4.77%) | 292 | 23 | 17% | -0.100% | -0.690% | -0.801% | -45.53 € |
| estocastico_rebote | 891.67 € (-3.52%) | 200 | 13 | 36% | -0.094% | -0.725% | -0.857% | -33.09 € |
| ruptura_estricta | 904.68 € (-2.12%) | 70 | 5 | 23% | -0.383% | -1.256% | -1.396% | -20.15 € |
| macd_sin_salida | 894.94 € (-3.17%) | 175 | 29 | 29% | -0.143% | -0.793% | -0.918% | -31.61 € |
| c_banda_atr_tope | 911.54 € (-1.37%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.11 € (-1.53%) | 56 | 5 | 16% | -0.186% | -1.158% | -1.275% | -14.88 € |
| c_banda_atr_regimen | 900.86 € (-2.53%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 898.84 € (-2.75%) | 116 | 0 | 18% | -0.234% | -0.959% | -1.087% | -25.40 € |
| c_banda_atr_evento | 902.48 € (-2.35%) | 91 | 30 | 24% | -0.366% | -1.156% | -1.293% | -24.11 € |
| macd_momentum_evento | 892.51 € (-3.43%) | 172 | 23 | 13% | -0.194% | -0.847% | -0.956% | -33.18 € |
| ruptura_volumen_evento | 898.56 € (-2.78%) | 96 | 18 | 11% | -0.470% | -1.245% | -1.370% | -27.29 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 05:40 | macd_momentum_evento | ASTER | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 05:40 | c_banda_atr_evento | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 05:40 | macd_sin_salida | ASTER | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 05:40 | estocastico_rebote | SEI | take-profit | +1.88% | +1.38% | +0.31 |
| 2026-09-30 05:40 | estocastico_rebote | RENDER | timeout | +0.58% | +0.09% | +0.02 |
| 2026-09-30 05:40 | estocastico_rebote | INJ | timeout | +0.81% | +0.31% | +0.07 |
| 2026-09-30 05:40 | macd_momentum | ASTER | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 05:40 | c_banda_atr | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 05:35 | estocastico_rebote | DOT | timeout | +0.95% | +0.45% | +0.10 |
| 2026-09-30 05:30 | macd_momentum_evento | KAS | momentum perdido | +0.81% | +0.31% | +0.07 |
| 2026-09-30 05:30 | macd_momentum_evento | SHIB | momentum perdido | -0.02% | -0.52% | -0.12 |
| 2026-09-30 05:30 | ruptura_estricta | SPX | stop-loss | -2.04% | -2.54% | -0.57 |
| 2026-09-30 05:30 | estocastico_rebote | TRUMP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 05:30 | macd_momentum | KAS | momentum perdido | +0.81% | +0.31% | +0.07 |
| 2026-09-30 05:30 | macd_momentum | SHIB | momentum perdido | -0.02% | -0.52% | -0.11 |

## Eventos de la última vuelta

- 2026-09-30 05:35 [ruptura_volumen] ENTRADA XRP @ 1.32616 (22.29 €, apertura)
- 2026-09-30 05:35 [ruptura_volumen_evento] ENTRADA XRP @ 1.32616 (22.42 €, apertura)
- 2026-09-30 05:35 [macd_momentum] ENTRADA ETH @ 2360.52 (21.96 €, apertura)
- 2026-09-30 05:35 [macd_sin_salida] ENTRADA ETH @ 2360.52 (22.31 €, apertura)
- 2026-09-30 05:35 [macd_momentum_evento] ENTRADA ETH @ 2360.52 (22.27 €, apertura)
- 2026-09-30 05:35 [macd_momentum] ENTRADA SOL @ 105.25 (21.96 €, apertura)
- 2026-09-30 05:35 [macd_momentum_evento] ENTRADA SOL @ 105.25 (22.27 €, apertura)
- 2026-09-30 05:35 [macd_momentum] ENTRADA NEAR @ 4.3869 (21.96 €, apertura)
- 2026-09-30 05:35 [macd_sin_salida] ENTRADA NEAR @ 4.3869 (22.31 €, apertura)
- 2026-09-30 05:35 [macd_momentum_evento] ENTRADA NEAR @ 4.3869 (22.27 €, apertura)
- 2026-09-30 05:35 [c_banda_atr] ENTRADA ADA @ 0.216636 (22.44 €, apertura)
- 2026-09-30 05:35 [macd_momentum] ENTRADA ADA @ 0.216636 (21.96 €, apertura)
- 2026-09-30 05:35 [c_banda_atr_evento] ENTRADA ADA @ 0.216636 (22.51 €, apertura)
- 2026-09-30 05:35 [macd_momentum_evento] ENTRADA ADA @ 0.216636 (22.27 €, apertura)
- 2026-09-30 05:35 [c_banda_atr] ENTRADA SUI @ 1.0238 (22.44 €, apertura)
- 2026-09-30 05:35 [macd_momentum] ENTRADA SUI @ 1.0238 (21.96 €, apertura)
- 2026-09-30 05:35 [c_banda_atr_evento] ENTRADA SUI @ 1.0238 (22.51 €, apertura)
- 2026-09-30 05:35 [macd_momentum_evento] ENTRADA SUI @ 1.0238 (22.27 €, apertura)
- 2026-09-30 05:35 [ruptura_volumen] ENTRADA XLM @ 0.196861 (22.29 €, apertura)
- 2026-09-30 05:35 [macd_momentum] ENTRADA XLM @ 0.196861 (21.96 €, apertura)
- 2026-09-30 05:35 [macd_sin_salida] ENTRADA XLM @ 0.196861 (22.31 €, apertura)
- 2026-09-30 05:35 [macd_momentum_evento] ENTRADA XLM @ 0.196861 (22.27 €, apertura)
- 2026-09-30 05:35 [ruptura_volumen_evento] ENTRADA XLM @ 0.196861 (22.42 €, apertura)
- 2026-09-30 05:35 [macd_momentum] ENTRADA AVAX @ 9.953 (21.96 €, apertura)
- 2026-09-30 05:35 [macd_sin_salida] ENTRADA AVAX @ 9.953 (22.31 €, apertura)
- 2026-09-30 05:35 [macd_momentum_evento] ENTRADA AVAX @ 9.953 (22.27 €, apertura)
- 2026-09-30 05:35 [macd_momentum] ENTRADA UNI @ 7.8096 (21.96 €, apertura)
- 2026-09-30 05:35 [macd_sin_salida] ENTRADA UNI @ 7.8096 (22.31 €, apertura)
- 2026-09-30 05:35 [macd_momentum_evento] ENTRADA UNI @ 7.8096 (22.27 €, apertura)
- 2026-09-30 05:35 [c_banda_atr] ENTRADA ALGO @ 0.11031 (22.44 €, apertura)
- 2026-09-30 05:35 [c_banda_atr_evento] ENTRADA ALGO @ 0.11031 (22.51 €, apertura)
- 2026-09-30 05:35 [macd_momentum] ENTRADA DOT @ 1.0678 (21.96 €, apertura)
- 2026-09-30 05:35 [macd_momentum_evento] ENTRADA DOT @ 1.0678 (22.27 €, apertura)
- 2026-09-30 05:35 [macd_momentum] ENTRADA ENA @ 0.2178 (21.96 €, apertura)
- 2026-09-30 05:35 [macd_sin_salida] ENTRADA ENA @ 0.2178 (22.31 €, apertura)
- 2026-09-30 05:35 [macd_momentum_evento] ENTRADA ENA @ 0.2178 (22.27 €, apertura)
- 2026-09-30 05:35 [ruptura_volumen] ENTRADA MON @ 0.02375 (22.29 €, apertura)
- 2026-09-30 05:35 [ruptura_volumen_evento] ENTRADA MON @ 0.02375 (22.42 €, apertura)
- 2026-09-30 05:40 [estocastico_rebote] CIERRE INJ timeout bruto +0.81% neto +0.31%
- 2026-09-30 05:35 [c_banda_atr] ENTRADA ATOM @ 1.517 (22.44 €, apertura)
- 2026-09-30 05:35 [c_banda_atr_evento] ENTRADA ATOM @ 1.517 (22.51 €, apertura)
- 2026-09-30 05:40 [estocastico_rebote] CIERRE RENDER timeout bruto +0.59% neto +0.09%
- 2026-09-30 05:40 [c_banda_atr] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 05:40 [c_banda_atr_evento] CIERRE ZRO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 05:40 [estocastico_rebote] CIERRE SEI take-profit bruto +1.88% neto +1.38%
- 2026-09-30 05:35 [c_banda_atr] ENTRADA OP @ 0.1151 (22.43 €, apertura)
- 2026-09-30 05:35 [macd_momentum] ENTRADA OP @ 0.1151 (21.96 €, apertura)
- 2026-09-30 05:35 [c_banda_atr_evento] ENTRADA OP @ 0.1151 (22.50 €, apertura)
- 2026-09-30 05:35 [macd_momentum_evento] ENTRADA OP @ 0.1151 (22.27 €, apertura)
- 2026-09-30 05:35 [macd_momentum] ENTRADA SHIB @ 5.121e-06 (21.96 €, apertura)
- 2026-09-30 05:35 [macd_momentum_evento] ENTRADA SHIB @ 5.121e-06 (22.27 €, apertura)
- 2026-09-30 05:35 [macd_sin_salida] ENTRADA BNB @ 673.98 (22.31 €, apertura)
- 2026-09-30 05:35 [c_banda_atr] ENTRADA GRT @ 0.02553 (22.43 €, apertura)
- 2026-09-30 05:35 [c_banda_atr_evento] ENTRADA GRT @ 0.02553 (22.50 €, apertura)
- 2026-09-30 05:40 [macd_momentum] CIERRE ASTER take-profit bruto +2.00% neto +1.50%
- 2026-09-30 05:40 [macd_sin_salida] CIERRE ASTER take-profit bruto +2.00% neto +1.50%
- 2026-09-30 05:40 [macd_momentum_evento] CIERRE ASTER take-profit bruto +2.00% neto +1.50%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
