# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 07:16 UTC · vueltas 234 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.00 € (-3.70%) | 138 | 17 | 25% | -0.319% | -1.008% | -1.138% | -31.75 € |
| reversion_bb | 913.76 € (-1.13%) | 39 | 7 | 41% | +0.017% | -1.083% | -1.195% | -9.72 € |
| ruptura_volumen | 885.13 € (-4.23%) | 175 | 3 | 17% | -0.330% | -0.979% | -1.108% | -38.88 € |
| rebote_extremo | 922.69 € (-0.17%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.879% | -1.33 € |
| pullback_tendencia | 902.69 € (-2.33%) | 119 | 1 | 24% | -0.072% | -0.791% | -0.916% | -21.55 € |
| macd_momentum | 874.68 € (-5.36%) | 321 | 3 | 16% | -0.105% | -0.686% | -0.796% | -49.69 € |
| estocastico_rebote | 885.70 € (-4.17%) | 217 | 14 | 34% | -0.140% | -0.760% | -0.893% | -37.56 € |
| ruptura_estricta | 901.27 € (-2.49%) | 75 | 5 | 21% | -0.469% | -1.317% | -1.460% | -22.62 € |
| macd_sin_salida | 885.05 € (-4.24%) | 196 | 14 | 27% | -0.201% | -0.835% | -0.958% | -37.16 € |
| c_banda_atr_tope | 908.99 € (-1.65%) | 41 | 3 | 17% | -0.500% | -1.600% | -1.726% | -15.06 € |
| ruptura_volumen_tope | 908.11 € (-1.74%) | 63 | 1 | 16% | -0.208% | -1.127% | -1.246% | -16.28 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.963% | -38.90 € |
| ruptura_volumen_regimen | 895.17 € (-3.15%) | 124 | 2 | 17% | -0.309% | -1.019% | -1.152% | -28.81 € |
| c_banda_atr_evento | 893.04 € (-3.38%) | 106 | 17 | 22% | -0.436% | -1.185% | -1.315% | -28.71 € |
| macd_momentum_evento | 886.97 € (-4.03%) | 201 | 3 | 13% | -0.188% | -0.819% | -0.924% | -37.39 € |
| ruptura_volumen_evento | 890.58 € (-3.64%) | 116 | 3 | 9% | -0.538% | -1.265% | -1.395% | -33.42 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 07:15 | ruptura_volumen_evento | XLM | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 07:15 | ruptura_volumen_regimen | WLD | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 07:15 | macd_sin_salida | PEPE | timeout | -0.66% | -1.16% | -0.26 |
| 2026-09-30 07:15 | macd_sin_salida | SUI | timeout | -0.66% | -1.16% | -0.26 |
| 2026-09-30 07:15 | macd_sin_salida | XRP | timeout | -0.59% | -1.09% | -0.24 |
| 2026-09-30 07:15 | ruptura_estricta | KAS | timeout | -0.10% | -0.60% | -0.14 |
| 2026-09-30 07:15 | ruptura_estricta | MINA | stop-loss | -2.00% | -2.50% | -0.56 |
| 2026-09-30 07:15 | estocastico_rebote | TON | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 07:15 | ruptura_volumen | XLM | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 07:15 | reversion_bb | JUP | stop-loss | -1.83% | -2.93% | -0.67 |
| 2026-09-30 07:10 | c_banda_atr_evento | ASTER | timeout | -0.20% | -0.70% | -0.16 |
| 2026-09-30 07:10 | c_banda_atr_tope | ASTER | timeout | -0.20% | -1.30% | -0.30 |
| 2026-09-30 07:10 | macd_sin_salida | SHIB | timeout | -0.53% | -1.03% | -0.23 |
| 2026-09-30 07:10 | macd_sin_salida | RENDER | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 07:10 | macd_sin_salida | CRV | timeout | +0.53% | +0.03% | +0.01 |

## Eventos de la última vuelta

- 2026-09-30 07:15 [macd_sin_salida] CIERRE XRP timeout bruto -0.59% neto -1.09%
- 2026-09-30 07:15 [macd_sin_salida] CIERRE SUI timeout bruto -0.66% neto -1.16%
- 2026-09-30 07:15 [ruptura_volumen] CIERRE XLM stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 07:15 [ruptura_volumen_evento] CIERRE XLM stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 07:15 [reversion_bb] CIERRE JUP stop-loss bruto -1.83% neto -2.93%
- 2026-09-30 07:10 [pullback_tendencia] ENTRADA TRX @ 0.297253 (22.57 €, apertura)
- 2026-09-30 07:15 [ruptura_volumen_regimen] CIERRE WLD stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 07:15 [macd_sin_salida] CIERRE PEPE timeout bruto -0.66% neto -1.16%
- 2026-09-30 07:15 [ruptura_estricta] CIERRE MINA stop-loss bruto -2.00% neto -2.50%
- 2026-09-30 07:15 [estocastico_rebote] CIERRE TON stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 07:15 [ruptura_estricta] CIERRE KAS timeout bruto -0.10% neto -0.60%
- 2026-09-30 07:10 [c_banda_atr] ENTRADA SPX @ 0.3726 (22.31 €, apertura)
- 2026-09-30 07:10 [macd_momentum] ENTRADA SPX @ 0.3726 (21.86 €, apertura)
- 2026-09-30 07:10 [macd_sin_salida] ENTRADA SPX @ 0.3726 (22.18 €, apertura)
- 2026-09-30 07:10 [c_banda_atr_tope] ENTRADA SPX @ 0.3726 (22.73 €, apertura)
- 2026-09-30 07:10 [c_banda_atr_evento] ENTRADA SPX @ 0.3726 (22.39 €, apertura)
- 2026-09-30 07:10 [macd_momentum_evento] ENTRADA SPX @ 0.3726 (22.17 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
