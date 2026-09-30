# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 07:31 UTC · vueltas 237 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.84 € (-3.51%) | 138 | 28 | 25% | -0.319% | -1.008% | -1.138% | -31.75 € |
| reversion_bb | 914.69 € (-1.03%) | 39 | 7 | 41% | +0.017% | -1.083% | -1.195% | -9.72 € |
| ruptura_volumen | 884.88 € (-4.26%) | 176 | 4 | 17% | -0.329% | -0.978% | -1.106% | -39.04 € |
| rebote_extremo | 923.28 € (-0.10%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.879% | -1.33 € |
| pullback_tendencia | 902.71 € (-2.33%) | 119 | 1 | 24% | -0.072% | -0.791% | -0.916% | -21.55 € |
| macd_momentum | 874.52 € (-5.38%) | 323 | 7 | 16% | -0.103% | -0.684% | -0.794% | -49.85 € |
| estocastico_rebote | 887.48 € (-3.98%) | 217 | 15 | 34% | -0.140% | -0.760% | -0.893% | -37.56 € |
| ruptura_estricta | 901.29 € (-2.48%) | 76 | 5 | 21% | -0.471% | -1.315% | -1.460% | -22.87 € |
| macd_sin_salida | 886.00 € (-4.14%) | 199 | 16 | 27% | -0.210% | -0.841% | -0.965% | -38.01 € |
| c_banda_atr_tope | 909.40 € (-1.61%) | 41 | 5 | 17% | -0.500% | -1.600% | -1.726% | -15.06 € |
| ruptura_volumen_tope | 907.72 € (-1.79%) | 63 | 3 | 16% | -0.208% | -1.127% | -1.246% | -16.28 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.963% | -38.90 € |
| ruptura_volumen_regimen | 895.33 € (-3.13%) | 124 | 2 | 17% | -0.309% | -1.019% | -1.152% | -28.81 € |
| c_banda_atr_evento | 894.88 € (-3.18%) | 106 | 28 | 22% | -0.436% | -1.185% | -1.315% | -28.71 € |
| macd_momentum_evento | 886.81 € (-4.05%) | 203 | 7 | 13% | -0.184% | -0.814% | -0.920% | -37.55 € |
| ruptura_volumen_evento | 890.33 € (-3.67%) | 117 | 4 | 9% | -0.535% | -1.261% | -1.390% | -33.59 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 07:30 | ruptura_volumen_evento | BCH | timeout | -0.24% | -0.74% | -0.17 |
| 2026-09-30 07:30 | macd_momentum_evento | XDC | momentum perdido | +0.37% | -0.13% | -0.03 |
| 2026-09-30 07:30 | macd_momentum | XDC | momentum perdido | +0.37% | -0.13% | -0.03 |
| 2026-09-30 07:30 | ruptura_volumen | BCH | timeout | -0.24% | -0.74% | -0.16 |
| 2026-09-30 07:25 | macd_momentum_evento | KAS | momentum perdido | -0.08% | -0.58% | -0.13 |
| 2026-09-30 07:25 | macd_sin_salida | VIRTUAL | timeout | -0.62% | -1.12% | -0.25 |
| 2026-09-30 07:25 | ruptura_estricta | VIRTUAL | timeout | -0.62% | -1.12% | -0.25 |
| 2026-09-30 07:25 | macd_momentum | KAS | momentum perdido | -0.08% | -0.58% | -0.13 |
| 2026-09-30 07:20 | macd_sin_salida | OP | timeout | -0.70% | -1.20% | -0.27 |
| 2026-09-30 07:20 | macd_sin_salida | SOL | timeout | -1.00% | -1.50% | -0.33 |
| 2026-09-30 07:15 | ruptura_volumen_evento | XLM | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 07:15 | ruptura_volumen_regimen | WLD | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 07:15 | macd_sin_salida | PEPE | timeout | -0.66% | -1.16% | -0.26 |
| 2026-09-30 07:15 | macd_sin_salida | SUI | timeout | -0.66% | -1.16% | -0.26 |
| 2026-09-30 07:15 | macd_sin_salida | XRP | timeout | -0.59% | -1.09% | -0.24 |

## Eventos de la última vuelta

- 2026-09-30 07:25 [c_banda_atr] ENTRADA SOL @ 104.52 (22.31 €, apertura)
- 2026-09-30 07:25 [c_banda_atr_evento] ENTRADA SOL @ 104.52 (22.39 €, apertura)
- 2026-09-30 07:25 [c_banda_atr] ENTRADA ADA @ 0.215143 (22.31 €, apertura)
- 2026-09-30 07:25 [c_banda_atr_evento] ENTRADA ADA @ 0.215143 (22.39 €, apertura)
- 2026-09-30 07:25 [c_banda_atr] ENTRADA XLM @ 0.1966 (22.31 €, apertura)
- 2026-09-30 07:25 [macd_momentum] ENTRADA XLM @ 0.1966 (21.86 €, apertura)
- 2026-09-30 07:25 [c_banda_atr_evento] ENTRADA XLM @ 0.1966 (22.39 €, apertura)
- 2026-09-30 07:25 [macd_momentum_evento] ENTRADA XLM @ 0.1966 (22.17 €, apertura)
- 2026-09-30 07:25 [c_banda_atr] ENTRADA UNI @ 7.7665 (22.31 €, apertura)
- 2026-09-30 07:25 [c_banda_atr_evento] ENTRADA UNI @ 7.7665 (22.39 €, apertura)
- 2026-09-30 07:25 [ruptura_volumen] ENTRADA PUMP @ 0.005088 (22.13 €, apertura)
- 2026-09-30 07:25 [ruptura_volumen_tope] ENTRADA PUMP @ 0.005088 (22.70 €, apertura)
- 2026-09-30 07:25 [ruptura_volumen_evento] ENTRADA PUMP @ 0.005088 (22.27 €, apertura)
- 2026-09-30 07:30 [macd_momentum] CIERRE XDC momentum perdido bruto +0.37% neto -0.13%
- 2026-09-30 07:30 [macd_momentum_evento] CIERRE XDC momentum perdido bruto +0.37% neto -0.13%
- 2026-09-30 07:25 [macd_momentum] ENTRADA DOT @ 1.0605 (21.86 €, apertura)
- 2026-09-30 07:25 [macd_sin_salida] ENTRADA DOT @ 1.0605 (22.16 €, apertura)
- 2026-09-30 07:25 [macd_momentum_evento] ENTRADA DOT @ 1.0605 (22.17 €, apertura)
- 2026-09-30 07:25 [macd_momentum] ENTRADA MON @ 0.02362 (21.86 €, apertura)
- 2026-09-30 07:25 [macd_sin_salida] ENTRADA MON @ 0.02362 (22.16 €, apertura)
- 2026-09-30 07:25 [macd_momentum_evento] ENTRADA MON @ 0.02362 (22.17 €, apertura)
- 2026-09-30 07:30 [ruptura_volumen] CIERRE BCH timeout bruto -0.24% neto -0.74%
- 2026-09-30 07:30 [ruptura_volumen_evento] CIERRE BCH timeout bruto -0.24% neto -0.74%
- 2026-09-30 07:25 [macd_momentum] ENTRADA ATOM @ 1.5116 (21.86 €, apertura)
- 2026-09-30 07:25 [macd_sin_salida] ENTRADA ATOM @ 1.5116 (22.16 €, apertura)
- 2026-09-30 07:25 [macd_momentum_evento] ENTRADA ATOM @ 1.5116 (22.17 €, apertura)
- 2026-09-30 07:25 [c_banda_atr] ENTRADA WLD @ 0.44 (22.31 €, apertura)
- 2026-09-30 07:25 [c_banda_atr_evento] ENTRADA WLD @ 0.44 (22.39 €, apertura)
- 2026-09-30 07:25 [c_banda_atr] ENTRADA USELESS @ 0.20776 (22.31 €, apertura)
- 2026-09-30 07:25 [c_banda_atr_evento] ENTRADA USELESS @ 0.20776 (22.39 €, apertura)
- 2026-09-30 07:25 [c_banda_atr] ENTRADA OP @ 0.1141 (22.31 €, apertura)
- 2026-09-30 07:25 [c_banda_atr_evento] ENTRADA OP @ 0.1141 (22.39 €, apertura)
- 2026-09-30 07:25 [c_banda_atr] ENTRADA PENGU @ 0.008643 (22.31 €, apertura)
- 2026-09-30 07:25 [c_banda_atr_evento] ENTRADA PENGU @ 0.008643 (22.39 €, apertura)
- 2026-09-30 07:25 [c_banda_atr] ENTRADA TRUMP @ 1.798 (22.31 €, apertura)
- 2026-09-30 07:25 [c_banda_atr_evento] ENTRADA TRUMP @ 1.798 (22.39 €, apertura)
- 2026-09-30 07:25 [c_banda_atr] ENTRADA ASTER @ 0.66802 (22.31 €, apertura)
- 2026-09-30 07:25 [macd_momentum] ENTRADA ASTER @ 0.66802 (21.86 €, apertura)
- 2026-09-30 07:25 [macd_sin_salida] ENTRADA ASTER @ 0.66802 (22.16 €, apertura)
- 2026-09-30 07:25 [c_banda_atr_evento] ENTRADA ASTER @ 0.66802 (22.39 €, apertura)
- 2026-09-30 07:25 [macd_momentum_evento] ENTRADA ASTER @ 0.66802 (22.17 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
