# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 10:06 UTC · vueltas 6 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 924.82 € (+0.06%) | 0 | 6 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| reversion_bb | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen | 923.61 € (-0.07%) | 1 | 14 | 0% | -1.200% | -2.300% | -2.512% | -0.53 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 924.22 € (-0.00%) | 0 | 5 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum | 924.59 € (+0.04%) | 3 | 31 | 0% | -0.323% | -1.423% | -1.502% | -0.99 € |
| estocastico_rebote | 924.32 € (+0.01%) | 1 | 2 | 100% | +1.800% | +0.700% | +0.487% | +0.16 € |
| ruptura_estricta | 923.39 € (-0.09%) | 1 | 10 | 0% | -2.000% | -3.100% | -3.312% | -0.72 € |
| macd_sin_salida | 925.35 € (+0.12%) | 0 | 34 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| c_banda_atr_tope | 924.82 € (+0.06%) | 0 | 5 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen_tope | 923.67 € (-0.06%) | 1 | 5 | 0% | -1.200% | -2.300% | -2.512% | -0.53 € |
| c_banda_atr_regimen | 924.82 € (+0.06%) | 0 | 6 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_regimen | 924.59 € (+0.04%) | 3 | 31 | 0% | -0.323% | -1.423% | -1.502% | -0.99 € |
| ruptura_volumen_regimen | 923.61 € (-0.07%) | 1 | 14 | 0% | -1.200% | -2.300% | -2.512% | -0.53 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 10:05 | macd_momentum_regimen | SPX | momentum perdido | -0.16% | -1.26% | -0.29 |
| 2026-09-29 10:05 | macd_momentum_regimen | PENGU | momentum perdido | +0.07% | -1.03% | -0.24 |
| 2026-09-29 10:05 | macd_momentum_regimen | NEAR | momentum perdido | -0.88% | -1.98% | -0.46 |
| 2026-09-29 10:05 | macd_momentum | SPX | momentum perdido | -0.16% | -1.26% | -0.29 |
| 2026-09-29 10:05 | macd_momentum | PENGU | momentum perdido | +0.07% | -1.03% | -0.24 |
| 2026-09-29 10:05 | macd_momentum | NEAR | momentum perdido | -0.88% | -1.98% | -0.46 |
| 2026-09-29 09:55 | ruptura_volumen_regimen | PUMP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 09:55 | ruptura_volumen_tope | PUMP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 09:55 | ruptura_estricta | PUMP | stop-loss | -2.00% | -3.10% | -0.72 |
| 2026-09-29 09:55 | estocastico_rebote | QNT | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-29 09:55 | ruptura_volumen | PUMP | stop-loss | -1.20% | -2.30% | -0.53 |

## Eventos de la última vuelta

- 2026-09-29 10:00 [macd_momentum] ENTRADA QNT @ 231.17 (23.11 €, apertura)
- 2026-09-29 10:00 [macd_sin_salida] ENTRADA QNT @ 231.17 (23.11 €, apertura)
- 2026-09-29 10:00 [macd_momentum_regimen] ENTRADA QNT @ 231.17 (23.11 €, apertura)
- 2026-09-29 10:05 [macd_momentum] CIERRE NEAR momentum perdido bruto -0.88% neto -1.98%
- 2026-09-29 10:05 [macd_momentum_regimen] CIERRE NEAR momentum perdido bruto -0.88% neto -1.98%
- 2026-09-29 10:00 [ruptura_volumen] ENTRADA ONDO @ 0.46382 (23.09 €, apertura)
- 2026-09-29 10:00 [ruptura_estricta] ENTRADA ONDO @ 0.46382 (23.09 €, apertura)
- 2026-09-29 10:00 [ruptura_volumen_regimen] ENTRADA ONDO @ 0.46382 (23.09 €, apertura)
- 2026-09-29 10:00 [pullback_tendencia] ENTRADA INJ @ 6.728 (23.11 €, apertura)
- 2026-09-29 10:00 [ruptura_volumen] ENTRADA RAY @ 1.686 (23.09 €, apertura)
- 2026-09-29 10:00 [ruptura_volumen_regimen] ENTRADA RAY @ 1.686 (23.09 €, apertura)
- 2026-09-29 10:00 [macd_momentum] ENTRADA MINA @ 0.1358 (23.09 €, apertura)
- 2026-09-29 10:00 [macd_sin_salida] ENTRADA MINA @ 0.1358 (23.11 €, apertura)
- 2026-09-29 10:00 [macd_momentum_regimen] ENTRADA MINA @ 0.1358 (23.09 €, apertura)
- 2026-09-29 10:00 [macd_momentum] ENTRADA NIGHT @ 0.02582 (23.09 €, apertura)
- 2026-09-29 10:00 [macd_sin_salida] ENTRADA NIGHT @ 0.02582 (23.11 €, apertura)
- 2026-09-29 10:00 [macd_momentum_regimen] ENTRADA NIGHT @ 0.02582 (23.09 €, apertura)
- 2026-09-29 10:05 [macd_momentum] CIERRE PENGU momentum perdido bruto +0.07% neto -1.03%
- 2026-09-29 10:05 [macd_momentum_regimen] CIERRE PENGU momentum perdido bruto +0.07% neto -1.03%
- 2026-09-29 10:05 [macd_momentum] CIERRE SPX momentum perdido bruto -0.16% neto -1.26%
- 2026-09-29 10:05 [macd_momentum_regimen] CIERRE SPX momentum perdido bruto -0.16% neto -1.26%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
