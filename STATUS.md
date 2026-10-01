# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 20:12 UTC · vueltas 303 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.73 € (-3.63%) | 244 | 26 | 36% | -0.032% | -0.639% | -0.762% | -35.51 € |
| reversion_bb | 917.12 € (-0.77%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 873.85 € (-5.45%) | 287 | 5 | 25% | -0.193% | -0.784% | -0.891% | -50.76 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.49 € (-3.65%) | 175 | 4 | 15% | -0.201% | -0.852% | -0.945% | -33.89 € |
| macd_momentum | 871.21 € (-5.74%) | 439 | 22 | 22% | +0.015% | -0.545% | -0.649% | -53.76 € |
| estocastico_rebote | 878.84 € (-4.91%) | 294 | 25 | 32% | -0.116% | -0.704% | -0.815% | -46.86 € |
| ruptura_estricta | 884.79 € (-4.27%) | 152 | 14 | 25% | -0.452% | -1.126% | -1.243% | -39.01 € |
| macd_sin_salida | 882.37 € (-4.53%) | 306 | 27 | 37% | -0.030% | -0.615% | -0.729% | -42.77 € |
| c_banda_atr_tope | 912.12 € (-1.31%) | 56 | 5 | 30% | +0.019% | -0.953% | -1.068% | -12.26 € |
| ruptura_volumen_tope | 908.05 € (-1.75%) | 93 | 5 | 29% | +0.019% | -0.765% | -0.878% | -16.32 € |
| c_banda_atr_regimen | 901.40 € (-2.47%) | 117 | 21 | 33% | -0.150% | -0.873% | -1.012% | -23.43 € |
| macd_momentum_regimen | 891.63 € (-3.53%) | 239 | 19 | 22% | +0.003% | -0.606% | -0.715% | -32.95 € |
| ruptura_volumen_regimen | 876.65 € (-5.15%) | 221 | 4 | 19% | -0.340% | -0.958% | -1.073% | -47.86 € |
| c_banda_atr_evento | 896.66 € (-2.98%) | 211 | 26 | 36% | +0.011% | -0.614% | -0.731% | -29.59 € |
| macd_momentum_evento | 876.04 € (-5.22%) | 392 | 22 | 20% | +0.013% | -0.554% | -0.654% | -48.94 € |
| ruptura_volumen_evento | 886.28 € (-4.11%) | 237 | 5 | 26% | -0.101% | -0.713% | -0.811% | -38.33 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 20:10 | macd_sin_salida | TRUMP | timeout | +0.77% | +0.27% | +0.06 |
| 2026-10-01 20:10 | macd_sin_salida | CRV | timeout | +0.60% | +0.10% | +0.02 |
| 2026-10-01 20:10 | macd_sin_salida | LTC | timeout | +1.46% | +0.95% | +0.21 |
| 2026-10-01 20:10 | estocastico_rebote | PEPE | timeout | +0.74% | +0.24% | +0.05 |
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

## Eventos de la última vuelta

- 2026-10-01 20:05 [macd_momentum] ENTRADA LINK @ 12.9 (21.76 €, apertura)
- 2026-10-01 20:05 [macd_momentum_regimen] ENTRADA LINK @ 12.9 (22.28 €, apertura)
- 2026-10-01 20:05 [macd_momentum_evento] ENTRADA LINK @ 12.9 (21.88 €, apertura)
- 2026-10-01 20:05 [macd_momentum] ENTRADA ADA @ 0.221311 (21.76 €, apertura)
- 2026-10-01 20:05 [macd_sin_salida] ENTRADA ADA @ 0.221311 (22.03 €, apertura)
- 2026-10-01 20:05 [macd_momentum_regimen] ENTRADA ADA @ 0.221311 (22.28 €, apertura)
- 2026-10-01 20:05 [macd_momentum_evento] ENTRADA ADA @ 0.221311 (21.88 €, apertura)
- 2026-10-01 20:05 [macd_momentum] ENTRADA AVAX @ 9.808 (21.76 €, apertura)
- 2026-10-01 20:05 [macd_momentum_regimen] ENTRADA AVAX @ 9.808 (22.28 €, apertura)
- 2026-10-01 20:05 [macd_momentum_evento] ENTRADA AVAX @ 9.808 (21.88 €, apertura)
- 2026-10-01 20:10 [macd_sin_salida] CIERRE LTC timeout bruto +1.45% neto +0.95%
- 2026-10-01 20:05 [macd_momentum] ENTRADA ONDO @ 0.44182 (21.76 €, apertura)
- 2026-10-01 20:05 [macd_sin_salida] ENTRADA ONDO @ 0.44182 (22.03 €, apertura)
- 2026-10-01 20:05 [macd_momentum_regimen] ENTRADA ONDO @ 0.44182 (22.28 €, apertura)
- 2026-10-01 20:05 [macd_momentum_evento] ENTRADA ONDO @ 0.44182 (21.88 €, apertura)
- 2026-10-01 20:10 [macd_sin_salida] CIERRE CRV timeout bruto +0.60% neto +0.10%
- 2026-10-01 20:05 [macd_momentum] ENTRADA PEPE @ 3.968e-06 (21.76 €, apertura)
- 2026-10-01 20:10 [estocastico_rebote] CIERRE PEPE timeout bruto +0.74% neto +0.24%
- 2026-10-01 20:05 [macd_sin_salida] ENTRADA PEPE @ 3.968e-06 (22.04 €, apertura)
- 2026-10-01 20:05 [macd_momentum_regimen] ENTRADA PEPE @ 3.968e-06 (22.28 €, apertura)
- 2026-10-01 20:05 [macd_momentum_evento] ENTRADA PEPE @ 3.968e-06 (21.88 €, apertura)
- 2026-10-01 20:05 [macd_momentum] ENTRADA MINA @ 0.136 (21.76 €, apertura)
- 2026-10-01 20:05 [macd_sin_salida] ENTRADA MINA @ 0.136 (22.04 €, apertura)
- 2026-10-01 20:05 [ruptura_volumen_tope] ENTRADA MINA @ 0.136 (22.70 €, apertura)
- 2026-10-01 20:05 [macd_momentum_regimen] ENTRADA MINA @ 0.136 (22.28 €, apertura)
- 2026-10-01 20:05 [macd_momentum_evento] ENTRADA MINA @ 0.136 (21.88 €, apertura)
- 2026-10-01 20:05 [c_banda_atr] ENTRADA FIL @ 0.908 (22.22 €, apertura)
- 2026-10-01 20:05 [c_banda_atr_regimen] ENTRADA FIL @ 0.908 (22.52 €, apertura)
- 2026-10-01 20:05 [c_banda_atr_evento] ENTRADA FIL @ 0.908 (22.37 €, apertura)
- 2026-10-01 20:05 [macd_momentum] ENTRADA SHIB @ 5.162e-06 (21.76 €, apertura)
- 2026-10-01 20:05 [macd_sin_salida] ENTRADA SHIB @ 5.162e-06 (22.04 €, apertura)
- 2026-10-01 20:05 [macd_momentum_regimen] ENTRADA SHIB @ 5.162e-06 (22.28 €, apertura)
- 2026-10-01 20:05 [macd_momentum_evento] ENTRADA SHIB @ 5.162e-06 (21.88 €, apertura)
- 2026-10-01 20:05 [macd_momentum] ENTRADA PENGU @ 0.008473 (21.76 €, apertura)
- 2026-10-01 20:05 [macd_sin_salida] ENTRADA PENGU @ 0.008473 (22.04 €, apertura)
- 2026-10-01 20:05 [macd_momentum_regimen] ENTRADA PENGU @ 0.008473 (22.28 €, apertura)
- 2026-10-01 20:05 [macd_momentum_evento] ENTRADA PENGU @ 0.008473 (21.88 €, apertura)
- 2026-10-01 20:05 [macd_momentum] ENTRADA TRUMP @ 1.837 (21.76 €, apertura)
- 2026-10-01 20:10 [macd_sin_salida] CIERRE TRUMP timeout bruto +0.77% neto +0.27%
- 2026-10-01 20:05 [macd_momentum_regimen] ENTRADA TRUMP @ 1.837 (22.28 €, apertura)
- 2026-10-01 20:05 [macd_momentum_evento] ENTRADA TRUMP @ 1.837 (21.88 €, apertura)
- 2026-10-01 20:05 [ruptura_estricta] ENTRADA KAS @ 0.03773 (22.13 €, apertura)
- 2026-10-01 20:05 [ruptura_volumen_regimen] ENTRADA KAS @ 0.03773 (21.91 €, apertura)
- 2026-10-01 20:05 [c_banda_atr] ENTRADA APT @ 0.6895 (22.22 €, apertura)
- 2026-10-01 20:05 [c_banda_atr_regimen] ENTRADA APT @ 0.6895 (22.52 €, apertura)
- 2026-10-01 20:05 [c_banda_atr_evento] ENTRADA APT @ 0.6895 (22.37 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
