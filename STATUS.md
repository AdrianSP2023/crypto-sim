# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 12:57 UTC · vueltas 8 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 927.25 € (+0.33%) | 5 | 27 | 60% | +0.602% | -0.498% | -0.800% | -0.58 € |
| reversion_bb | 924.33 € (+0.01%) | 1 | 0 | 100% | +1.500% | +0.400% | +0.231% | +0.09 € |
| ruptura_volumen | 928.41 € (+0.45%) | 5 | 39 | 20% | -0.460% | -1.560% | -1.908% | -1.80 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 925.84 € (+0.17%) | 6 | 12 | 67% | +0.902% | -0.198% | -0.365% | -0.28 € |
| macd_momentum | 929.14 € (+0.53%) | 10 | 34 | 70% | +1.057% | -0.043% | -0.273% | -0.10 € |
| estocastico_rebote | 927.25 € (+0.33%) | 3 | 14 | 100% | +1.836% | +0.736% | +0.492% | +0.51 € |
| ruptura_estricta | 928.04 € (+0.41%) | 2 | 33 | 50% | +0.500% | -0.600% | -1.141% | -0.28 € |
| macd_sin_salida | 929.53 € (+0.57%) | 9 | 35 | 78% | +1.225% | +0.125% | -0.117% | +0.26 € |
| c_banda_atr_tope | 924.89 € (+0.07%) | 2 | 4 | 50% | +0.256% | -0.844% | -1.075% | -0.39 € |
| ruptura_volumen_tope | 925.48 € (+0.13%) | 0 | 5 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| c_banda_atr_regimen | 927.25 € (+0.33%) | 5 | 27 | 60% | +0.602% | -0.498% | -0.800% | -0.58 € |
| macd_momentum_regimen | 929.14 € (+0.53%) | 10 | 34 | 70% | +1.057% | -0.043% | -0.273% | -0.10 € |
| ruptura_volumen_regimen | 928.41 € (+0.45%) | 5 | 39 | 20% | -0.460% | -1.560% | -1.908% | -1.80 € |
| c_banda_atr_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 12:55 | macd_momentum_regimen | SPX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 12:55 | macd_momentum_regimen | APT | take-profit | +2.01% | +0.91% | +0.21 |
| 2026-09-30 12:55 | macd_momentum_regimen | MINA | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 12:55 | c_banda_atr_regimen | SPX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 12:55 | macd_sin_salida | SPX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 12:55 | macd_sin_salida | APT | take-profit | +2.01% | +0.91% | +0.21 |
| 2026-09-30 12:55 | macd_sin_salida | MINA | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 12:55 | macd_momentum | SPX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 12:55 | macd_momentum | APT | take-profit | +2.01% | +0.91% | +0.21 |
| 2026-09-30 12:55 | macd_momentum | MINA | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 12:55 | c_banda_atr | SPX | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 12:50 | ruptura_volumen_regimen | WLD | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 12:50 | macd_momentum_regimen | JUP | momentum perdido | -0.45% | -1.55% | -0.36 |
| 2026-09-30 12:50 | macd_momentum_regimen | NEAR | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 12:50 | c_banda_atr_regimen | NEAR | stop-loss | -1.50% | -2.60% | -0.60 |

## Eventos de la última vuelta

- 2026-09-30 12:50 [ruptura_estricta] ENTRADA SUI @ 1.0399 (23.10 €, apertura)
- 2026-09-30 12:50 [pullback_tendencia] ENTRADA TRX @ 0.299228 (23.10 €, apertura)
- 2026-09-30 12:50 [estocastico_rebote] ENTRADA TRX @ 0.299228 (23.12 €, apertura)
- 2026-09-30 12:50 [ruptura_volumen] ENTRADA BCH @ 276.47 (23.06 €, apertura)
- 2026-09-30 12:50 [ruptura_estricta] ENTRADA BCH @ 276.47 (23.10 €, apertura)
- 2026-09-30 12:50 [ruptura_volumen_regimen] ENTRADA BCH @ 276.47 (23.06 €, apertura)
- 2026-09-30 12:50 [pullback_tendencia] ENTRADA JUP @ 0.29681 (23.10 €, apertura)
- 2026-09-30 12:55 [macd_momentum] CIERRE MINA take-profit bruto +2.00% neto +0.90%
- 2026-09-30 12:55 [macd_sin_salida] CIERRE MINA take-profit bruto +2.00% neto +0.90%
- 2026-09-30 12:55 [macd_momentum_regimen] CIERRE MINA take-profit bruto +2.00% neto +0.90%
- 2026-09-30 12:55 [macd_momentum] CIERRE APT take-profit bruto +2.01% neto +0.91%
- 2026-09-30 12:55 [macd_sin_salida] CIERRE APT take-profit bruto +2.01% neto +0.91%
- 2026-09-30 12:55 [macd_momentum_regimen] CIERRE APT take-profit bruto +2.01% neto +0.91%
- 2026-09-30 12:55 [c_banda_atr] CIERRE SPX take-profit bruto +2.00% neto +0.90%
- 2026-09-30 12:55 [macd_momentum] CIERRE SPX take-profit bruto +2.00% neto +0.90%
- 2026-09-30 12:55 [macd_sin_salida] CIERRE SPX take-profit bruto +2.00% neto +0.90%
- 2026-09-30 12:55 [c_banda_atr_regimen] CIERRE SPX take-profit bruto +2.00% neto +0.90%
- 2026-09-30 12:55 [macd_momentum_regimen] CIERRE SPX take-profit bruto +2.00% neto +0.90%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
