# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 14:27 UTC · vueltas 57 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 916.85 € (-0.80%) | 26 | 20 | 42% | +0.056% | -1.044% | -1.182% | -6.27 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 913.99 € (-1.11%) | 54 | 6 | 28% | +0.097% | -0.876% | -1.007% | -10.90 € |
| rebote_extremo | 924.34 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 915.03 € (-1.00%) | 43 | 11 | 30% | +0.138% | -0.941% | -1.048% | -9.33 € |
| macd_momentum | 905.16 € (-2.06%) | 119 | 7 | 20% | +0.019% | -0.701% | -0.816% | -19.15 € |
| estocastico_rebote | 918.42 € (-0.63%) | 53 | 31 | 53% | +0.577% | -0.359% | -0.476% | -4.39 € |
| ruptura_estricta | 919.15 € (-0.55%) | 26 | 11 | 35% | +0.148% | -0.952% | -1.082% | -5.72 € |
| macd_sin_salida | 914.48 € (-1.06%) | 61 | 21 | 38% | +0.258% | -0.645% | -0.768% | -9.04 € |
| c_banda_atr_tope | 920.20 € (-0.44%) | 11 | 4 | 27% | -0.397% | -1.497% | -1.686% | -3.80 € |
| ruptura_volumen_tope | 922.26 € (-0.21%) | 13 | 5 | 23% | +0.215% | -0.885% | -1.016% | -2.66 € |
| c_banda_atr_regimen | 916.85 € (-0.80%) | 26 | 20 | 42% | +0.056% | -1.044% | -1.182% | -6.27 € |
| macd_momentum_regimen | 905.16 € (-2.06%) | 119 | 7 | 20% | +0.019% | -0.701% | -0.816% | -19.15 € |
| ruptura_volumen_regimen | 913.99 € (-1.11%) | 54 | 6 | 28% | +0.097% | -0.876% | -1.007% | -10.90 € |
| c_banda_atr_evento | 923.53 € (-0.08%) | 0 | 7 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 924.00 € (-0.03%) | 0 | 6 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 14:25 | macd_momentum_regimen | ASTER | momentum perdido | -0.60% | -1.10% | -0.25 |
| 2026-09-29 14:25 | c_banda_atr_regimen | FET | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:25 | c_banda_atr_tope | FET | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:25 | macd_sin_salida | FIL | timeout | +0.21% | -0.59% | -0.14 |
| 2026-09-29 14:25 | estocastico_rebote | FET | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-29 14:25 | macd_momentum | ASTER | momentum perdido | -0.60% | -1.10% | -0.25 |
| 2026-09-29 14:25 | c_banda_atr | FET | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:20 | ruptura_volumen_regimen | SHIB | timeout | +0.51% | -0.29% | -0.07 |
| 2026-09-29 14:20 | macd_momentum_regimen | TAO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 14:20 | macd_momentum_regimen | NEAR | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:20 | c_banda_atr_regimen | TAO | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:20 | c_banda_atr_tope | TAO | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:20 | macd_sin_salida | NEAR | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 14:20 | macd_sin_salida | ZEC | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 14:20 | macd_momentum | TAO | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-29 14:20 [estocastico_rebote] ENTRADA BTC @ 74099.9 (23.01 €, apertura)
- 2026-09-29 14:20 [estocastico_rebote] ENTRADA LINK @ 13.3037 (23.01 €, apertura)
- 2026-09-29 14:20 [estocastico_rebote] ENTRADA ETH @ 2398.16 (23.01 €, apertura)
- 2026-09-29 14:20 [estocastico_rebote] ENTRADA SOL @ 106.66 (23.01 €, apertura)
- 2026-09-29 14:20 [pullback_tendencia] ENTRADA NEAR @ 4.4474 (22.87 €, apertura)
- 2026-09-29 14:20 [estocastico_rebote] ENTRADA ADA @ 0.221974 (23.01 €, apertura)
- 2026-09-29 14:20 [estocastico_rebote] ENTRADA AVAX @ 10.253 (23.01 €, apertura)
- 2026-09-29 14:20 [estocastico_rebote] ENTRADA HYPE @ 77.46 (23.01 €, apertura)
- 2026-09-29 14:20 [estocastico_rebote] ENTRADA ARB @ 0.1867 (23.01 €, apertura)
- 2026-09-29 14:20 [estocastico_rebote] ENTRADA DOGE @ 0.0843254 (23.01 €, apertura)
- 2026-09-29 14:20 [c_banda_atr] ENTRADA ENA @ 0.2286 (22.96 €, apertura)
- 2026-09-29 14:20 [estocastico_rebote] ENTRADA ENA @ 0.2286 (23.01 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_tope] ENTRADA ENA @ 0.2286 (23.03 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_regimen] ENTRADA ENA @ 0.2286 (22.96 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_evento] ENTRADA ENA @ 0.2286 (23.11 €, apertura)
- 2026-09-29 14:20 [c_banda_atr] ENTRADA JUP @ 0.29098 (22.96 €, apertura)
- 2026-09-29 14:20 [macd_momentum] ENTRADA JUP @ 0.29098 (22.63 €, apertura)
- 2026-09-29 14:20 [estocastico_rebote] ENTRADA JUP @ 0.29098 (23.01 €, apertura)
- 2026-09-29 14:20 [macd_sin_salida] ENTRADA JUP @ 0.29098 (22.88 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_tope] ENTRADA JUP @ 0.29098 (23.03 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_regimen] ENTRADA JUP @ 0.29098 (22.96 €, apertura)
- 2026-09-29 14:20 [macd_momentum_regimen] ENTRADA JUP @ 0.29098 (22.63 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_evento] ENTRADA JUP @ 0.29098 (23.11 €, apertura)
- 2026-09-29 14:20 [macd_momentum_evento] ENTRADA JUP @ 0.29098 (23.11 €, apertura)
- 2026-09-29 14:20 [macd_momentum] ENTRADA TRX @ 0.295458 (22.63 €, apertura)
- 2026-09-29 14:20 [macd_momentum_regimen] ENTRADA TRX @ 0.295458 (22.63 €, apertura)
- 2026-09-29 14:20 [macd_momentum_evento] ENTRADA TRX @ 0.295458 (23.11 €, apertura)
- 2026-09-29 14:20 [c_banda_atr] ENTRADA ATOM @ 1.5604 (22.96 €, apertura)
- 2026-09-29 14:20 [macd_momentum] ENTRADA ATOM @ 1.5604 (22.63 €, apertura)
- 2026-09-29 14:20 [macd_sin_salida] ENTRADA ATOM @ 1.5604 (22.88 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_regimen] ENTRADA ATOM @ 1.5604 (22.96 €, apertura)
- 2026-09-29 14:20 [macd_momentum_regimen] ENTRADA ATOM @ 1.5604 (22.63 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_evento] ENTRADA ATOM @ 1.5604 (23.11 €, apertura)
- 2026-09-29 14:20 [macd_momentum_evento] ENTRADA ATOM @ 1.5604 (23.11 €, apertura)
- 2026-09-29 14:20 [c_banda_atr] ENTRADA WLD @ 0.4435 (22.96 €, apertura)
- 2026-09-29 14:20 [macd_momentum] ENTRADA WLD @ 0.4435 (22.63 €, apertura)
- 2026-09-29 14:20 [macd_sin_salida] ENTRADA WLD @ 0.4435 (22.88 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_regimen] ENTRADA WLD @ 0.4435 (22.96 €, apertura)
- 2026-09-29 14:20 [macd_momentum_regimen] ENTRADA WLD @ 0.4435 (22.63 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_evento] ENTRADA WLD @ 0.4435 (23.11 €, apertura)
- 2026-09-29 14:20 [macd_momentum_evento] ENTRADA WLD @ 0.4435 (23.11 €, apertura)
- 2026-09-29 14:20 [c_banda_atr] ENTRADA USELESS @ 0.22087 (22.96 €, apertura)
- 2026-09-29 14:20 [pullback_tendencia] ENTRADA USELESS @ 0.22087 (22.87 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_regimen] ENTRADA USELESS @ 0.22087 (22.96 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_evento] ENTRADA USELESS @ 0.22087 (23.11 €, apertura)
- 2026-09-29 14:20 [c_banda_atr] ENTRADA MINA @ 0.1316 (22.96 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_regimen] ENTRADA MINA @ 0.1316 (22.96 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_evento] ENTRADA MINA @ 0.1316 (23.11 €, apertura)
- 2026-09-29 14:20 [macd_momentum_evento] ENTRADA OP @ 0.1182 (23.11 €, apertura)
- 2026-09-29 14:20 [macd_momentum] ENTRADA FIL @ 0.956 (22.63 €, apertura)
- 2026-09-29 14:25 [macd_sin_salida] CIERRE FIL timeout bruto +0.21% neto -0.59%
- 2026-09-29 14:20 [macd_momentum_regimen] ENTRADA FIL @ 0.956 (22.63 €, apertura)
- 2026-09-29 14:20 [c_banda_atr_evento] ENTRADA FIL @ 0.956 (23.11 €, apertura)
- 2026-09-29 14:20 [macd_momentum_evento] ENTRADA FIL @ 0.956 (23.11 €, apertura)
- 2026-09-29 14:20 [estocastico_rebote] ENTRADA SHIB @ 5.182e-06 (23.01 €, apertura)
- 2026-09-29 14:25 [macd_momentum] CIERRE ASTER momentum perdido bruto -0.60% neto -1.10%
- 2026-09-29 14:25 [macd_momentum_regimen] CIERRE ASTER momentum perdido bruto -0.60% neto -1.10%
- 2026-09-29 14:25 [c_banda_atr] CIERRE FET stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 14:25 [estocastico_rebote] CIERRE FET stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 14:25 [c_banda_atr_tope] CIERRE FET stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 14:25 [c_banda_atr_regimen] CIERRE FET stop-loss bruto -1.50% neto -2.60%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
