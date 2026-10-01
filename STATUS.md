# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 20:07 UTC · vueltas 302 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.64 € (-3.64%) | 244 | 24 | 36% | -0.032% | -0.639% | -0.762% | -35.51 € |
| reversion_bb | 917.05 € (-0.78%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 873.81 € (-5.46%) | 287 | 5 | 25% | -0.193% | -0.784% | -0.891% | -50.76 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.49 € (-3.65%) | 175 | 4 | 15% | -0.201% | -0.852% | -0.945% | -33.89 € |
| macd_momentum | 871.13 € (-5.75%) | 439 | 13 | 22% | +0.015% | -0.545% | -0.649% | -53.76 € |
| estocastico_rebote | 879.14 € (-4.88%) | 293 | 26 | 31% | -0.119% | -0.708% | -0.819% | -46.91 € |
| ruptura_estricta | 884.78 € (-4.27%) | 152 | 13 | 25% | -0.452% | -1.126% | -1.243% | -39.01 € |
| macd_sin_salida | 882.48 € (-4.52%) | 303 | 24 | 36% | -0.039% | -0.625% | -0.740% | -43.06 € |
| c_banda_atr_tope | 912.22 € (-1.30%) | 56 | 5 | 30% | +0.019% | -0.953% | -1.068% | -12.26 € |
| ruptura_volumen_tope | 907.98 € (-1.76%) | 93 | 4 | 29% | +0.019% | -0.765% | -0.878% | -16.32 € |
| c_banda_atr_regimen | 901.31 € (-2.48%) | 117 | 19 | 33% | -0.150% | -0.873% | -1.012% | -23.43 € |
| macd_momentum_regimen | 891.60 € (-3.53%) | 239 | 10 | 22% | +0.003% | -0.606% | -0.715% | -32.95 € |
| ruptura_volumen_regimen | 876.64 € (-5.15%) | 221 | 3 | 19% | -0.340% | -0.958% | -1.073% | -47.86 € |
| c_banda_atr_evento | 896.57 € (-2.99%) | 211 | 24 | 36% | +0.011% | -0.614% | -0.731% | -29.59 € |
| macd_momentum_evento | 875.96 € (-5.22%) | 392 | 13 | 20% | +0.013% | -0.554% | -0.654% | -48.94 € |
| ruptura_volumen_evento | 886.25 € (-4.11%) | 237 | 5 | 26% | -0.101% | -0.713% | -0.811% | -38.33 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 20:05 | c_banda_atr_evento | RENDER | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 20:05 | c_banda_atr_regimen | RENDER | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 20:05 | macd_sin_salida | XLM | timeout | +0.27% | -0.23% | -0.05 |
| 2026-10-01 20:05 | macd_sin_salida | SOL | timeout | +0.48% | -0.02% | -0.01 |
| 2026-10-01 20:05 | macd_sin_salida | ETH | timeout | +0.42% | -0.08% | -0.02 |
| 2026-10-01 20:05 | estocastico_rebote | BCH | timeout | +0.41% | -0.09% | -0.02 |
| 2026-10-01 20:05 | estocastico_rebote | TAO | timeout | +0.77% | +0.27% | +0.06 |
| 2026-10-01 20:05 | c_banda_atr | RENDER | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 20:00 | ruptura_volumen_evento | SKY | timeout | +1.23% | +0.73% | +0.16 |
| 2026-10-01 20:00 | ruptura_volumen_evento | TON | timeout | +0.15% | -0.35% | -0.08 |
| 2026-10-01 20:00 | ruptura_volumen_regimen | SKY | timeout | +1.23% | +0.73% | +0.16 |
| 2026-10-01 20:00 | ruptura_volumen_regimen | TON | timeout | +0.15% | -0.35% | -0.08 |
| 2026-10-01 20:00 | macd_sin_salida | TRX | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 20:00 | ruptura_volumen | SKY | timeout | +1.23% | +0.73% | +0.16 |
| 2026-10-01 20:00 | ruptura_volumen | TON | timeout | +0.15% | -0.35% | -0.08 |

## Eventos de la última vuelta

- 2026-10-01 20:05 [macd_sin_salida] CIERRE ETH timeout bruto +0.42% neto -0.08%
- 2026-10-01 20:05 [macd_sin_salida] CIERRE SOL timeout bruto +0.48% neto -0.02%
- 2026-10-01 20:00 [macd_momentum] ENTRADA SUI @ 1.0563 (21.76 €, apertura)
- 2026-10-01 20:00 [macd_sin_salida] ENTRADA SUI @ 1.0563 (22.03 €, apertura)
- 2026-10-01 20:00 [macd_momentum_regimen] ENTRADA SUI @ 1.0563 (22.28 €, apertura)
- 2026-10-01 20:00 [macd_momentum_evento] ENTRADA SUI @ 1.0563 (21.88 €, apertura)
- 2026-10-01 20:05 [macd_sin_salida] CIERRE XLM timeout bruto +0.27% neto -0.23%
- 2026-10-01 20:00 [macd_momentum] ENTRADA TAO @ 271.893 (21.76 €, apertura)
- 2026-10-01 20:05 [estocastico_rebote] CIERRE TAO timeout bruto +0.77% neto +0.27%
- 2026-10-01 20:00 [macd_sin_salida] ENTRADA TAO @ 271.893 (22.03 €, apertura)
- 2026-10-01 20:00 [macd_momentum_regimen] ENTRADA TAO @ 271.893 (22.28 €, apertura)
- 2026-10-01 20:00 [macd_momentum_evento] ENTRADA TAO @ 271.893 (21.88 €, apertura)
- 2026-10-01 20:00 [macd_momentum] ENTRADA DOT @ 1.054 (21.76 €, apertura)
- 2026-10-01 20:00 [macd_sin_salida] ENTRADA DOT @ 1.054 (22.03 €, apertura)
- 2026-10-01 20:00 [macd_momentum_regimen] ENTRADA DOT @ 1.054 (22.28 €, apertura)
- 2026-10-01 20:00 [macd_momentum_evento] ENTRADA DOT @ 1.054 (21.88 €, apertura)
- 2026-10-01 20:00 [macd_momentum] ENTRADA BCH @ 273.97 (21.76 €, apertura)
- 2026-10-01 20:05 [estocastico_rebote] CIERRE BCH timeout bruto +0.41% neto -0.09%
- 2026-10-01 20:00 [macd_sin_salida] ENTRADA BCH @ 273.97 (22.03 €, apertura)
- 2026-10-01 20:00 [macd_momentum_regimen] ENTRADA BCH @ 273.97 (22.28 €, apertura)
- 2026-10-01 20:00 [macd_momentum_evento] ENTRADA BCH @ 273.97 (21.88 €, apertura)
- 2026-10-01 20:05 [c_banda_atr] CIERRE RENDER timeout bruto +0.24% neto -0.26%
- 2026-10-01 20:05 [c_banda_atr_regimen] CIERRE RENDER timeout bruto +0.24% neto -0.26%
- 2026-10-01 20:05 [c_banda_atr_evento] CIERRE RENDER timeout bruto +0.24% neto -0.26%
- 2026-10-01 20:00 [pullback_tendencia] ENTRADA TRUMP @ 1.837 (22.26 €, apertura)
- 2026-10-01 20:00 [c_banda_atr] ENTRADA XMR @ 484.68 (22.22 €, apertura)
- 2026-10-01 20:00 [c_banda_atr_regimen] ENTRADA XMR @ 484.68 (22.52 €, apertura)
- 2026-10-01 20:00 [c_banda_atr_evento] ENTRADA XMR @ 484.68 (22.37 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
