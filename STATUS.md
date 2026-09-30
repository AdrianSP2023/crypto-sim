# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 14:16 UTC · vueltas 24 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 915.51 € (-0.94%) | 27 | 7 | 37% | -0.185% | -1.285% | -1.449% | -8.02 € |
| reversion_bb | 924.42 € (+0.02%) | 1 | 2 | 100% | +1.500% | +0.400% | +0.231% | +0.09 € |
| ruptura_volumen | 910.31 € (-1.51%) | 37 | 13 | 22% | -0.430% | -1.530% | -1.696% | -13.03 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 917.73 € (-0.70%) | 21 | 8 | 29% | -0.149% | -1.249% | -1.376% | -6.06 € |
| macd_momentum | 913.27 € (-1.19%) | 46 | 2 | 30% | +0.022% | -1.039% | -1.175% | -11.04 € |
| estocastico_rebote | 922.08 € (-0.23%) | 13 | 21 | 62% | +0.577% | -0.523% | -0.699% | -1.57 € |
| ruptura_estricta | 915.52 € (-0.94%) | 11 | 28 | 36% | -0.138% | -1.238% | -1.450% | -3.14 € |
| macd_sin_salida | 913.83 € (-1.13%) | 35 | 12 | 40% | -0.105% | -1.205% | -1.355% | -9.75 € |
| c_banda_atr_tope | 922.67 € (-0.17%) | 8 | 0 | 50% | +0.252% | -0.849% | -1.012% | -1.57 € |
| ruptura_volumen_tope | 922.07 € (-0.24%) | 7 | 2 | 29% | -0.161% | -1.261% | -1.367% | -2.04 € |
| c_banda_atr_regimen | 915.51 € (-0.94%) | 27 | 7 | 37% | -0.185% | -1.285% | -1.449% | -8.02 € |
| macd_momentum_regimen | 913.27 € (-1.19%) | 46 | 2 | 30% | +0.022% | -1.039% | -1.175% | -11.04 € |
| ruptura_volumen_regimen | 910.31 € (-1.51%) | 37 | 13 | 22% | -0.430% | -1.530% | -1.696% | -13.03 € |
| c_banda_atr_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 924.24 € (-0.00%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 14:15 | c_banda_atr_regimen | BCH | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 14:15 | c_banda_atr_tope | BCH | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 14:15 | ruptura_estricta | BCH | stop-loss | -2.00% | -3.10% | -0.72 |
| 2026-09-30 14:15 | estocastico_rebote | BCH | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 14:15 | c_banda_atr | BCH | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 14:00 | ruptura_volumen_regimen | MINA | stop-loss | -1.83% | -2.93% | -0.64 |
| 2026-09-30 14:00 | ruptura_volumen | MINA | stop-loss | -1.83% | -2.93% | -0.64 |
| 2026-09-30 13:55 | ruptura_volumen_regimen | XDC | stop-loss | -1.46% | -2.56% | -0.59 |
| 2026-09-30 13:55 | ruptura_volumen_tope | XDC | stop-loss | -1.46% | -2.56% | -0.59 |
| 2026-09-30 13:55 | ruptura_volumen | XDC | stop-loss | -1.46% | -2.56% | -0.59 |
| 2026-09-30 13:45 | ruptura_volumen_regimen | ASTER | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 13:45 | ruptura_volumen_regimen | RENDER | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 13:45 | ruptura_volumen_regimen | BCH | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 13:45 | ruptura_volumen_regimen | ONDO | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 13:45 | macd_momentum_regimen | TRUMP | momentum perdido | -0.33% | -1.13% | -0.26 |

## Eventos de la última vuelta

- 2026-09-30 14:10 [estocastico_rebote] ENTRADA ONDO @ 0.45067 (23.08 €, apertura)
- 2026-09-30 14:15 [c_banda_atr] CIERRE BCH stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 14:15 [estocastico_rebote] CIERRE BCH stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 14:15 [ruptura_estricta] CIERRE BCH stop-loss bruto -2.00% neto -3.10%
- 2026-09-30 14:15 [c_banda_atr_tope] CIERRE BCH stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 14:15 [c_banda_atr_regimen] CIERRE BCH stop-loss bruto -1.50% neto -2.60%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
