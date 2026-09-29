# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 14:06 UTC · vueltas 54 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 919.34 € (-0.53%) | 22 | 18 | 50% | +0.354% | -0.746% | -0.881% | -3.79 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 913.98 € (-1.11%) | 52 | 8 | 29% | +0.114% | -0.871% | -1.005% | -10.44 € |
| rebote_extremo | 924.28 € (+0.00%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 914.93 € (-1.01%) | 42 | 4 | 31% | +0.135% | -0.957% | -1.065% | -9.27 € |
| macd_momentum | 907.13 € (-1.85%) | 108 | 10 | 21% | +0.085% | -0.657% | -0.769% | -16.33 € |
| estocastico_rebote | 920.41 € (-0.41%) | 49 | 22 | 57% | +0.726% | -0.227% | -0.342% | -2.57 € |
| ruptura_estricta | 919.90 € (-0.47%) | 24 | 13 | 38% | +0.333% | -0.767% | -0.898% | -4.25 € |
| macd_sin_salida | 915.45 € (-0.95%) | 54 | 22 | 41% | +0.373% | -0.571% | -0.695% | -7.09 € |
| c_banda_atr_tope | 922.09 € (-0.23%) | 8 | 5 | 38% | +0.019% | -1.081% | -1.255% | -2.00 € |
| ruptura_volumen_tope | 921.99 € (-0.24%) | 13 | 5 | 23% | +0.215% | -0.885% | -1.016% | -2.66 € |
| c_banda_atr_regimen | 919.34 € (-0.53%) | 22 | 18 | 50% | +0.354% | -0.746% | -0.881% | -3.79 € |
| macd_momentum_regimen | 907.13 € (-1.85%) | 108 | 10 | 21% | +0.085% | -0.657% | -0.769% | -16.33 € |
| ruptura_volumen_regimen | 913.98 € (-1.11%) | 52 | 8 | 29% | +0.114% | -0.871% | -1.005% | -10.44 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 14:05 | ruptura_volumen_regimen | USELESS | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 14:05 | ruptura_volumen_regimen | ZRO | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 14:05 | macd_momentum_regimen | SOL | momentum perdido | +0.90% | +0.40% | +0.09 |
| 2026-09-29 14:05 | c_banda_atr_regimen | JUP | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:05 | ruptura_estricta | AVAX | stop-loss | -2.00% | -3.10% | -0.72 |
| 2026-09-29 14:05 | estocastico_rebote | JUP | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-29 14:05 | estocastico_rebote | ARB | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-29 14:05 | macd_momentum | SOL | momentum perdido | +0.90% | +0.40% | +0.09 |
| 2026-09-29 14:05 | pullback_tendencia | SPX | rotura de tendencia | -0.43% | -1.24% | -0.28 |
| 2026-09-29 14:05 | pullback_tendencia | ARB | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:05 | pullback_tendencia | AVAX | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:05 | ruptura_volumen | USELESS | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 14:05 | ruptura_volumen | ZRO | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 14:05 | c_banda_atr | JUP | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 14:00 | macd_momentum_regimen | ENA | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-09-29 14:05 [macd_momentum] CIERRE SOL momentum perdido bruto +0.90% neto +0.40%
- 2026-09-29 14:05 [macd_momentum_regimen] CIERRE SOL momentum perdido bruto +0.90% neto +0.40%
- 2026-09-29 14:00 [macd_momentum] ENTRADA ZEC @ 1284.04 (22.70 €, apertura)
- 2026-09-29 14:00 [macd_sin_salida] ENTRADA ZEC @ 1284.04 (22.93 €, apertura)
- 2026-09-29 14:00 [macd_momentum_regimen] ENTRADA ZEC @ 1284.04 (22.70 €, apertura)
- 2026-09-29 14:05 [pullback_tendencia] CIERRE AVAX stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 14:05 [ruptura_estricta] CIERRE AVAX stop-loss bruto -2.00% neto -3.10%
- 2026-09-29 14:05 [pullback_tendencia] CIERRE ARB stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 14:05 [estocastico_rebote] CIERRE ARB stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 14:00 [c_banda_atr] ENTRADA DASH @ 54.513 (23.03 €, apertura)
- 2026-09-29 14:00 [c_banda_atr_regimen] ENTRADA DASH @ 54.513 (23.03 €, apertura)
- 2026-09-29 14:05 [c_banda_atr] CIERRE JUP stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 14:05 [estocastico_rebote] CIERRE JUP stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 14:05 [c_banda_atr_regimen] CIERRE JUP stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 14:00 [macd_momentum] ENTRADA INJ @ 6.807 (22.70 €, apertura)
- 2026-09-29 14:00 [macd_momentum_regimen] ENTRADA INJ @ 6.807 (22.70 €, apertura)
- 2026-09-29 14:00 [ruptura_volumen] ENTRADA ZRO @ 1.473 (22.86 €, apertura)
- 2026-09-29 14:05 [ruptura_volumen] CIERRE ZRO stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 14:00 [ruptura_volumen_regimen] ENTRADA ZRO @ 1.473 (22.86 €, apertura)
- 2026-09-29 14:05 [ruptura_volumen_regimen] CIERRE ZRO stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 14:00 [macd_momentum] ENTRADA VIRTUAL @ 0.7227 (22.70 €, apertura)
- 2026-09-29 14:00 [macd_sin_salida] ENTRADA VIRTUAL @ 0.7227 (22.93 €, apertura)
- 2026-09-29 14:00 [macd_momentum_regimen] ENTRADA VIRTUAL @ 0.7227 (22.70 €, apertura)
- 2026-09-29 14:00 [ruptura_volumen] ENTRADA USELESS @ 0.2206 (22.85 €, apertura)
- 2026-09-29 14:05 [ruptura_volumen] CIERRE USELESS stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 14:00 [ruptura_estricta] ENTRADA USELESS @ 0.2206 (23.00 €, apertura)
- 2026-09-29 14:00 [ruptura_volumen_regimen] ENTRADA USELESS @ 0.2206 (22.85 €, apertura)
- 2026-09-29 14:05 [ruptura_volumen_regimen] CIERRE USELESS stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 14:00 [macd_momentum] ENTRADA XPL @ 0.0888 (22.70 €, apertura)
- 2026-09-29 14:00 [macd_sin_salida] ENTRADA XPL @ 0.0888 (22.93 €, apertura)
- 2026-09-29 14:00 [macd_momentum_regimen] ENTRADA XPL @ 0.0888 (22.70 €, apertura)
- 2026-09-29 14:05 [pullback_tendencia] CIERRE SPX rotura de tendencia bruto -0.43% neto -1.23%
- 2026-09-29 14:00 [macd_momentum] ENTRADA FET @ 0.2092 (22.70 €, apertura)
- 2026-09-29 14:00 [macd_sin_salida] ENTRADA FET @ 0.2092 (22.93 €, apertura)
- 2026-09-29 14:00 [macd_momentum_regimen] ENTRADA FET @ 0.2092 (22.70 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
