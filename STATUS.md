# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 20:02 UTC · vueltas 301 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.76 € (-3.73%) | 243 | 24 | 36% | -0.033% | -0.641% | -0.763% | -35.45 € |
| reversion_bb | 917.00 € (-0.78%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 873.52 € (-5.49%) | 287 | 5 | 25% | -0.193% | -0.784% | -0.891% | -50.76 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.48 € (-3.65%) | 175 | 3 | 15% | -0.201% | -0.852% | -0.945% | -33.89 € |
| macd_momentum | 870.75 € (-5.79%) | 439 | 9 | 22% | +0.015% | -0.545% | -0.649% | -53.76 € |
| estocastico_rebote | 878.25 € (-4.98%) | 291 | 28 | 31% | -0.123% | -0.713% | -0.825% | -46.95 € |
| ruptura_estricta | 884.31 € (-4.32%) | 152 | 13 | 25% | -0.452% | -1.126% | -1.243% | -39.01 € |
| macd_sin_salida | 881.95 € (-4.58%) | 300 | 23 | 36% | -0.044% | -0.631% | -0.746% | -42.99 € |
| c_banda_atr_tope | 911.89 € (-1.34%) | 56 | 5 | 30% | +0.019% | -0.953% | -1.068% | -12.26 € |
| ruptura_volumen_tope | 907.82 € (-1.78%) | 93 | 4 | 29% | +0.019% | -0.765% | -0.878% | -16.32 € |
| c_banda_atr_regimen | 900.54 € (-2.56%) | 116 | 19 | 34% | -0.153% | -0.878% | -1.018% | -23.37 € |
| macd_momentum_regimen | 891.27 € (-3.57%) | 239 | 6 | 22% | +0.003% | -0.606% | -0.715% | -32.95 € |
| ruptura_volumen_regimen | 876.43 € (-5.17%) | 221 | 3 | 19% | -0.340% | -0.958% | -1.073% | -47.86 € |
| c_banda_atr_evento | 895.68 € (-3.09%) | 210 | 24 | 37% | +0.010% | -0.616% | -0.732% | -29.53 € |
| macd_momentum_evento | 875.58 € (-5.27%) | 392 | 9 | 20% | +0.013% | -0.554% | -0.654% | -48.94 € |
| ruptura_volumen_evento | 885.95 € (-4.14%) | 237 | 5 | 26% | -0.101% | -0.713% | -0.811% | -38.33 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 20:00 | ruptura_volumen_evento | SKY | timeout | +1.23% | +0.73% | +0.16 |
| 2026-10-01 20:00 | ruptura_volumen_evento | TON | timeout | +0.15% | -0.35% | -0.08 |
| 2026-10-01 20:00 | ruptura_volumen_regimen | SKY | timeout | +1.23% | +0.73% | +0.16 |
| 2026-10-01 20:00 | ruptura_volumen_regimen | TON | timeout | +0.15% | -0.35% | -0.08 |
| 2026-10-01 20:00 | macd_sin_salida | TRX | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 20:00 | ruptura_volumen | SKY | timeout | +1.23% | +0.73% | +0.16 |
| 2026-10-01 20:00 | ruptura_volumen | TON | timeout | +0.15% | -0.35% | -0.08 |
| 2026-10-01 19:55 | ruptura_volumen_evento | JUP | timeout | +0.93% | +0.43% | +0.10 |
| 2026-10-01 19:55 | ruptura_volumen_regimen | JUP | timeout | +0.93% | +0.43% | +0.09 |
| 2026-10-01 19:55 | estocastico_rebote | PUMP | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-01 19:55 | ruptura_volumen | JUP | timeout | +0.93% | +0.43% | +0.09 |
| 2026-10-01 19:50 | c_banda_atr_tope | BTC | timeout | +0.31% | -0.19% | -0.04 |
| 2026-10-01 19:45 | ruptura_volumen_evento | BCH | timeout | -0.93% | -1.43% | -0.32 |
| 2026-10-01 19:45 | ruptura_volumen_evento | XRP | timeout | -0.61% | -1.11% | -0.25 |
| 2026-10-01 19:45 | ruptura_volumen_regimen | BCH | timeout | -0.93% | -1.43% | -0.32 |

## Eventos de la última vuelta

- 2026-10-01 19:55 [macd_momentum] ENTRADA AAVE @ 150.28 (21.76 €, apertura)
- 2026-10-01 19:55 [macd_momentum_regimen] ENTRADA AAVE @ 150.28 (22.28 €, apertura)
- 2026-10-01 19:55 [macd_momentum_evento] ENTRADA AAVE @ 150.28 (21.88 €, apertura)
- 2026-10-01 19:55 [ruptura_volumen] ENTRADA PUMP @ 0.00523 (21.83 €, apertura)
- 2026-10-01 19:55 [macd_momentum] ENTRADA PUMP @ 0.00523 (21.76 €, apertura)
- 2026-10-01 19:55 [macd_sin_salida] ENTRADA PUMP @ 0.00523 (22.03 €, apertura)
- 2026-10-01 19:55 [ruptura_volumen_tope] ENTRADA PUMP @ 0.00523 (22.70 €, apertura)
- 2026-10-01 19:55 [macd_momentum_regimen] ENTRADA PUMP @ 0.00523 (22.28 €, apertura)
- 2026-10-01 19:55 [ruptura_volumen_regimen] ENTRADA PUMP @ 0.00523 (21.91 €, apertura)
- 2026-10-01 19:55 [macd_momentum_evento] ENTRADA PUMP @ 0.00523 (21.88 €, apertura)
- 2026-10-01 19:55 [ruptura_volumen_evento] ENTRADA PUMP @ 0.00523 (22.15 €, apertura)
- 2026-10-01 19:55 [c_banda_atr] ENTRADA XLM @ 0.195533 (22.22 €, apertura)
- 2026-10-01 19:55 [c_banda_atr_evento] ENTRADA XLM @ 0.195533 (22.37 €, apertura)
- 2026-10-01 19:55 [c_banda_atr] ENTRADA TAO @ 270.084 (22.22 €, apertura)
- 2026-10-01 19:55 [c_banda_atr_regimen] ENTRADA TAO @ 270.084 (22.52 €, apertura)
- 2026-10-01 19:55 [c_banda_atr_evento] ENTRADA TAO @ 270.084 (22.37 €, apertura)
- 2026-10-01 19:55 [macd_momentum] ENTRADA UNI @ 8.0848 (21.76 €, apertura)
- 2026-10-01 19:55 [macd_sin_salida] ENTRADA UNI @ 8.0848 (22.03 €, apertura)
- 2026-10-01 19:55 [macd_momentum_regimen] ENTRADA UNI @ 8.0848 (22.28 €, apertura)
- 2026-10-01 19:55 [macd_momentum_evento] ENTRADA UNI @ 8.0848 (21.88 €, apertura)
- 2026-10-01 19:55 [macd_momentum] ENTRADA LTC @ 60.61 (21.76 €, apertura)
- 2026-10-01 19:55 [macd_momentum_regimen] ENTRADA LTC @ 60.61 (22.28 €, apertura)
- 2026-10-01 19:55 [macd_momentum_evento] ENTRADA LTC @ 60.61 (21.88 €, apertura)
- 2026-10-01 19:55 [macd_momentum] ENTRADA ARB @ 0.178 (21.76 €, apertura)
- 2026-10-01 19:55 [macd_sin_salida] ENTRADA ARB @ 0.178 (22.03 €, apertura)
- 2026-10-01 19:55 [macd_momentum_regimen] ENTRADA ARB @ 0.178 (22.28 €, apertura)
- 2026-10-01 19:55 [macd_momentum_evento] ENTRADA ARB @ 0.178 (21.88 €, apertura)
- 2026-10-01 19:55 [c_banda_atr] ENTRADA FET @ 0.2041 (22.22 €, apertura)
- 2026-10-01 19:55 [c_banda_atr_regimen] ENTRADA FET @ 0.2041 (22.52 €, apertura)
- 2026-10-01 19:55 [c_banda_atr_evento] ENTRADA FET @ 0.2041 (22.37 €, apertura)
- 2026-10-01 20:00 [macd_sin_salida] CIERRE TRX timeout bruto +0.23% neto -0.27%
- 2026-10-01 19:55 [c_banda_atr] ENTRADA USELESS @ 0.21489 (22.22 €, apertura)
- 2026-10-01 19:55 [c_banda_atr_regimen] ENTRADA USELESS @ 0.21489 (22.52 €, apertura)
- 2026-10-01 19:55 [c_banda_atr_evento] ENTRADA USELESS @ 0.21489 (22.37 €, apertura)
- 2026-10-01 19:55 [c_banda_atr] ENTRADA TRUMP @ 1.833 (22.22 €, apertura)
- 2026-10-01 19:55 [c_banda_atr_regimen] ENTRADA TRUMP @ 1.833 (22.52 €, apertura)
- 2026-10-01 19:55 [c_banda_atr_evento] ENTRADA TRUMP @ 1.833 (22.37 €, apertura)
- 2026-10-01 20:00 [ruptura_volumen] CIERRE TON timeout bruto +0.15% neto -0.35%
- 2026-10-01 20:00 [ruptura_volumen_regimen] CIERRE TON timeout bruto +0.15% neto -0.35%
- 2026-10-01 20:00 [ruptura_volumen_evento] CIERRE TON timeout bruto +0.15% neto -0.35%
- 2026-10-01 20:00 [ruptura_volumen] CIERRE SKY timeout bruto +1.23% neto +0.73%
- 2026-10-01 20:00 [ruptura_volumen_regimen] CIERRE SKY timeout bruto +1.23% neto +0.73%
- 2026-10-01 20:00 [ruptura_volumen_evento] CIERRE SKY timeout bruto +1.23% neto +0.73%
- 2026-10-01 19:55 [macd_momentum] ENTRADA SPX @ 0.3899 (21.76 €, apertura)
- 2026-10-01 19:55 [macd_momentum_regimen] ENTRADA SPX @ 0.3899 (22.28 €, apertura)
- 2026-10-01 19:55 [macd_momentum_evento] ENTRADA SPX @ 0.3899 (21.88 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
