# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 12:51 UTC · vueltas 7 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 925.04 € (+0.09%) | 4 | 28 | 50% | +0.253% | -0.847% | -1.134% | -0.78 € |
| reversion_bb | 924.33 € (+0.01%) | 1 | 0 | 100% | +1.500% | +0.400% | +0.231% | +0.09 € |
| ruptura_volumen | 925.60 € (+0.15%) | 5 | 38 | 20% | -0.460% | -1.560% | -1.908% | -1.80 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 925.34 € (+0.12%) | 6 | 10 | 67% | +0.902% | -0.198% | -0.365% | -0.28 € |
| macd_momentum | 926.10 € (+0.20%) | 7 | 37 | 57% | +0.651% | -0.449% | -0.603% | -0.73 € |
| estocastico_rebote | 926.32 € (+0.22%) | 3 | 13 | 100% | +1.836% | +0.736% | +0.492% | +0.51 € |
| ruptura_estricta | 925.52 € (+0.14%) | 2 | 31 | 50% | +0.500% | -0.600% | -1.141% | -0.28 € |
| macd_sin_salida | 926.35 € (+0.23%) | 6 | 38 | 67% | +0.835% | -0.265% | -0.423% | -0.37 € |
| c_banda_atr_tope | 924.44 € (+0.02%) | 2 | 4 | 50% | +0.256% | -0.844% | -1.075% | -0.39 € |
| ruptura_volumen_tope | 925.28 € (+0.11%) | 0 | 5 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| c_banda_atr_regimen | 925.04 € (+0.09%) | 4 | 28 | 50% | +0.253% | -0.847% | -1.134% | -0.78 € |
| macd_momentum_regimen | 926.10 € (+0.20%) | 7 | 37 | 57% | +0.651% | -0.449% | -0.603% | -0.73 € |
| ruptura_volumen_regimen | 925.60 € (+0.15%) | 5 | 38 | 20% | -0.460% | -1.560% | -1.908% | -1.80 € |
| c_banda_atr_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 12:50 | ruptura_volumen_regimen | WLD | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 12:50 | macd_momentum_regimen | JUP | momentum perdido | -0.45% | -1.55% | -0.36 |
| 2026-09-30 12:50 | macd_momentum_regimen | NEAR | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 12:50 | c_banda_atr_regimen | NEAR | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 12:50 | c_banda_atr_tope | NEAR | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 12:50 | macd_sin_salida | NEAR | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 12:50 | macd_momentum | JUP | momentum perdido | -0.45% | -1.55% | -0.36 |
| 2026-09-30 12:50 | macd_momentum | NEAR | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 12:50 | pullback_tendencia | CRV | rotura de tendencia | -1.09% | -2.19% | -0.51 |
| 2026-09-30 12:50 | ruptura_volumen | WLD | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 12:50 | c_banda_atr | NEAR | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 12:45 | ruptura_volumen_regimen | USELESS | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 12:45 | ruptura_volumen_regimen | AAVE | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 12:45 | ruptura_volumen_regimen | NEAR | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 12:45 | macd_momentum_regimen | VVV | take-profit | +2.00% | +0.90% | +0.21 |

## Eventos de la última vuelta

- 2026-09-30 12:50 [c_banda_atr] CIERRE NEAR stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 12:50 [macd_momentum] CIERRE NEAR stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 12:50 [macd_sin_salida] CIERRE NEAR stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 12:50 [c_banda_atr_tope] CIERRE NEAR stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 12:50 [c_banda_atr_regimen] CIERRE NEAR stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 12:50 [macd_momentum_regimen] CIERRE NEAR stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 12:45 [ruptura_volumen] ENTRADA LTC @ 59.8 (23.07 €, apertura)
- 2026-09-30 12:45 [macd_momentum] ENTRADA LTC @ 59.8 (23.10 €, apertura)
- 2026-09-30 12:45 [ruptura_estricta] ENTRADA LTC @ 59.8 (23.10 €, apertura)
- 2026-09-30 12:45 [macd_sin_salida] ENTRADA LTC @ 59.8 (23.10 €, apertura)
- 2026-09-30 12:45 [macd_momentum_regimen] ENTRADA LTC @ 59.8 (23.10 €, apertura)
- 2026-09-30 12:45 [ruptura_volumen_regimen] ENTRADA LTC @ 59.8 (23.07 €, apertura)
- 2026-09-30 12:50 [pullback_tendencia] CIERRE CRV rotura de tendencia bruto -1.09% neto -2.19%
- 2026-09-30 12:50 [ruptura_volumen] CIERRE WLD stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 12:50 [ruptura_volumen_regimen] CIERRE WLD stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 12:45 [macd_momentum] ENTRADA BCH @ 275.86 (23.10 €, apertura)
- 2026-09-30 12:45 [macd_sin_salida] ENTRADA BCH @ 275.86 (23.10 €, apertura)
- 2026-09-30 12:45 [macd_momentum_regimen] ENTRADA BCH @ 275.86 (23.10 €, apertura)
- 2026-09-30 12:50 [macd_momentum] CIERRE JUP momentum perdido bruto -0.45% neto -1.55%
- 2026-09-30 12:50 [macd_momentum_regimen] CIERRE JUP momentum perdido bruto -0.45% neto -1.55%
- 2026-09-30 12:45 [ruptura_volumen] ENTRADA MON @ 0.02451 (23.06 €, apertura)
- 2026-09-30 12:45 [ruptura_volumen_regimen] ENTRADA MON @ 0.02451 (23.06 €, apertura)
- 2026-09-30 12:45 [ruptura_estricta] ENTRADA RENDER @ 1.739 (23.10 €, apertura)
- 2026-09-30 12:45 [ruptura_volumen] ENTRADA FIL @ 0.954 (23.06 €, apertura)
- 2026-09-30 12:45 [ruptura_volumen_regimen] ENTRADA FIL @ 0.954 (23.06 €, apertura)
- 2026-09-30 12:45 [ruptura_volumen] ENTRADA VVV @ 24.622 (23.06 €, apertura)
- 2026-09-30 12:45 [ruptura_estricta] ENTRADA VVV @ 24.622 (23.10 €, apertura)
- 2026-09-30 12:45 [ruptura_volumen_regimen] ENTRADA VVV @ 24.622 (23.06 €, apertura)
- 2026-09-30 12:45 [ruptura_volumen] ENTRADA WLFI @ 0.05 (23.06 €, apertura)
- 2026-09-30 12:45 [ruptura_estricta] ENTRADA WLFI @ 0.05 (23.10 €, apertura)
- 2026-09-30 12:45 [ruptura_volumen_regimen] ENTRADA WLFI @ 0.05 (23.06 €, apertura)
- 2026-09-30 12:45 [macd_momentum] ENTRADA PENGU @ 0.00903 (23.09 €, apertura)
- 2026-09-30 12:45 [macd_sin_salida] ENTRADA PENGU @ 0.00903 (23.10 €, apertura)
- 2026-09-30 12:45 [macd_momentum_regimen] ENTRADA PENGU @ 0.00903 (23.09 €, apertura)
- 2026-09-30 12:45 [macd_momentum] ENTRADA KAS @ 0.03869 (23.09 €, apertura)
- 2026-09-30 12:45 [macd_sin_salida] ENTRADA KAS @ 0.03869 (23.10 €, apertura)
- 2026-09-30 12:45 [macd_momentum_regimen] ENTRADA KAS @ 0.03869 (23.09 €, apertura)
- 2026-09-30 12:45 [ruptura_estricta] ENTRADA SKY @ 0.07278 (23.10 €, apertura)
- 2026-09-30 12:45 [macd_momentum] ENTRADA XMR @ 477.28 (23.09 €, apertura)
- 2026-09-30 12:45 [macd_sin_salida] ENTRADA XMR @ 477.28 (23.10 €, apertura)
- 2026-09-30 12:45 [macd_momentum_regimen] ENTRADA XMR @ 477.28 (23.09 €, apertura)
- 2026-09-30 12:45 [ruptura_volumen] ENTRADA APT @ 0.7164 (23.06 €, apertura)
- 2026-09-30 12:45 [ruptura_estricta] ENTRADA APT @ 0.7164 (23.10 €, apertura)
- 2026-09-30 12:45 [ruptura_volumen_regimen] ENTRADA APT @ 0.7164 (23.06 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
