# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 15:26 UTC · vueltas 252 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.26 € (-3.57%) | 208 | 22 | 34% | -0.085% | -0.710% | -0.835% | -33.68 € |
| reversion_bb | 916.68 € (-0.82%) | 37 | 10 | 38% | +0.028% | -1.072% | -1.174% | -9.13 € |
| ruptura_volumen | 879.31 € (-4.86%) | 240 | 7 | 22% | -0.230% | -0.839% | -0.947% | -45.59 € |
| rebote_extremo | 922.24 € (-0.22%) | 11 | 2 | 45% | +0.049% | -1.051% | -1.228% | -2.67 € |
| pullback_tendencia | 893.13 € (-3.37%) | 143 | 2 | 13% | -0.280% | -0.965% | -1.066% | -31.39 € |
| macd_momentum | 875.43 € (-5.28%) | 357 | 16 | 20% | -0.042% | -0.615% | -0.724% | -49.53 € |
| estocastico_rebote | 878.72 € (-4.93%) | 276 | 11 | 31% | -0.146% | -0.740% | -0.853% | -46.24 € |
| ruptura_estricta | 885.33 € (-4.21%) | 137 | 4 | 23% | -0.562% | -1.254% | -1.376% | -39.15 € |
| macd_sin_salida | 881.68 € (-4.61%) | 256 | 17 | 33% | -0.149% | -0.751% | -0.867% | -43.66 € |
| c_banda_atr_tope | 912.33 € (-1.29%) | 49 | 5 | 27% | -0.057% | -1.095% | -1.209% | -12.33 € |
| ruptura_volumen_tope | 908.12 € (-1.74%) | 78 | 5 | 24% | -0.088% | -0.926% | -1.042% | -16.57 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 897.19 € (-2.93%) | 175 | 22 | 34% | -0.043% | -0.693% | -0.811% | -27.75 € |
| macd_momentum_evento | 880.28 € (-4.76%) | 310 | 16 | 17% | -0.053% | -0.638% | -0.743% | -44.68 € |
| ruptura_volumen_evento | 891.82 € (-3.51%) | 190 | 7 | 23% | -0.126% | -0.765% | -0.862% | -33.07 € |
| rebote_desplome | 924.78 € (+0.06%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.78 € (+0.06%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 15:25 | macd_momentum_evento | TON | take-profit | +2.25% | +1.75% | +0.39 |
| 2026-10-01 15:25 | c_banda_atr_evento | TON | take-profit | +2.17% | +1.67% | +0.38 |
| 2026-10-01 15:25 | macd_sin_salida | TON | take-profit | +2.25% | +1.75% | +0.39 |
| 2026-10-01 15:25 | estocastico_rebote | TON | take-profit | +2.17% | +1.67% | +0.37 |
| 2026-10-01 15:25 | estocastico_rebote | PEPE | take-profit | +1.83% | +1.33% | +0.29 |
| 2026-10-01 15:25 | macd_momentum | TON | take-profit | +2.25% | +1.75% | +0.39 |
| 2026-10-01 15:25 | c_banda_atr | TON | take-profit | +2.17% | +1.67% | +0.38 |
| 2026-10-01 15:20 | reversion_bb | APT | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-10-01 15:15 | macd_momentum_evento | BCH | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-10-01 15:15 | macd_momentum_evento | AVAX | momentum perdido | -0.44% | -0.94% | -0.21 |
| 2026-10-01 15:15 | c_banda_atr_evento | ADA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 15:15 | macd_sin_salida | MINA | timeout | -0.30% | -0.80% | -0.18 |
| 2026-10-01 15:15 | macd_sin_salida | ADA | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 15:15 | macd_momentum | BCH | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-10-01 15:15 | macd_momentum | AVAX | momentum perdido | -0.44% | -0.94% | -0.21 |

## Eventos de la última vuelta

- 2026-10-01 15:20 [ruptura_volumen] ENTRADA XRP @ 1.32466 (21.97 €, apertura)
- 2026-10-01 15:20 [ruptura_estricta] ENTRADA XRP @ 1.32466 (22.13 €, apertura)
- 2026-10-01 15:20 [ruptura_volumen_tope] ENTRADA XRP @ 1.32466 (22.69 €, apertura)
- 2026-10-01 15:20 [ruptura_volumen_evento] ENTRADA XRP @ 1.32466 (22.28 €, apertura)
- 2026-10-01 15:20 [c_banda_atr] ENTRADA SOL @ 104.64 (22.25 €, apertura)
- 2026-10-01 15:20 [macd_momentum] ENTRADA SOL @ 104.64 (21.86 €, apertura)
- 2026-10-01 15:20 [c_banda_atr_evento] ENTRADA SOL @ 104.64 (22.40 €, apertura)
- 2026-10-01 15:20 [macd_momentum_evento] ENTRADA SOL @ 104.64 (21.98 €, apertura)
- 2026-10-01 15:20 [macd_momentum] ENTRADA ADA @ 0.219536 (21.86 €, apertura)
- 2026-10-01 15:20 [macd_sin_salida] ENTRADA ADA @ 0.219536 (22.01 €, apertura)
- 2026-10-01 15:20 [macd_momentum_evento] ENTRADA ADA @ 0.219536 (21.98 €, apertura)
- 2026-10-01 15:20 [c_banda_atr] ENTRADA XLM @ 0.195384 (22.25 €, apertura)
- 2026-10-01 15:20 [c_banda_atr_evento] ENTRADA XLM @ 0.195384 (22.40 €, apertura)
- 2026-10-01 15:20 [c_banda_atr] ENTRADA TAO @ 275.309 (22.25 €, apertura)
- 2026-10-01 15:20 [ruptura_volumen_tope] ENTRADA TAO @ 275.309 (22.69 €, apertura)
- 2026-10-01 15:20 [c_banda_atr_evento] ENTRADA TAO @ 275.309 (22.40 €, apertura)
- 2026-10-01 15:20 [ruptura_volumen] ENTRADA ZRO @ 1.499 (21.97 €, apertura)
- 2026-10-01 15:20 [macd_momentum] ENTRADA ZRO @ 1.499 (21.86 €, apertura)
- 2026-10-01 15:20 [ruptura_estricta] ENTRADA ZRO @ 1.499 (22.13 €, apertura)
- 2026-10-01 15:20 [macd_sin_salida] ENTRADA ZRO @ 1.499 (22.01 €, apertura)
- 2026-10-01 15:20 [macd_momentum_evento] ENTRADA ZRO @ 1.499 (21.98 €, apertura)
- 2026-10-01 15:20 [ruptura_volumen_evento] ENTRADA ZRO @ 1.499 (22.28 €, apertura)
- 2026-10-01 15:20 [macd_momentum] ENTRADA DOGE @ 0.0841764 (21.86 €, apertura)
- 2026-10-01 15:20 [macd_momentum_evento] ENTRADA DOGE @ 0.0841764 (21.98 €, apertura)
- 2026-10-01 15:20 [c_banda_atr] ENTRADA ICP @ 2.911 (22.25 €, apertura)
- 2026-10-01 15:20 [c_banda_atr_evento] ENTRADA ICP @ 2.911 (22.40 €, apertura)
- 2026-10-01 15:20 [ruptura_volumen] ENTRADA TRX @ 0.296557 (21.97 €, apertura)
- 2026-10-01 15:20 [ruptura_volumen_evento] ENTRADA TRX @ 0.296557 (22.28 €, apertura)
- 2026-10-01 15:20 [c_banda_atr] ENTRADA WLD @ 0.4426 (22.25 €, apertura)
- 2026-10-01 15:20 [c_banda_atr_evento] ENTRADA WLD @ 0.4426 (22.40 €, apertura)
- 2026-10-01 15:20 [c_banda_atr] ENTRADA BCH @ 273.63 (22.25 €, apertura)
- 2026-10-01 15:20 [macd_momentum] ENTRADA BCH @ 273.63 (21.86 €, apertura)
- 2026-10-01 15:20 [c_banda_atr_evento] ENTRADA BCH @ 273.63 (22.40 €, apertura)
- 2026-10-01 15:20 [macd_momentum_evento] ENTRADA BCH @ 273.63 (21.98 €, apertura)
- 2026-10-01 15:25 [estocastico_rebote] CIERRE PEPE take-profit bruto +1.84% neto +1.34%
- 2026-10-01 15:20 [macd_momentum] ENTRADA MON @ 0.02889 (21.86 €, apertura)
- 2026-10-01 15:20 [macd_sin_salida] ENTRADA MON @ 0.02889 (22.01 €, apertura)
- 2026-10-01 15:20 [macd_momentum_evento] ENTRADA MON @ 0.02889 (21.98 €, apertura)
- 2026-10-01 15:20 [macd_momentum] ENTRADA RENDER @ 1.701 (21.86 €, apertura)
- 2026-10-01 15:20 [macd_momentum_evento] ENTRADA RENDER @ 1.701 (21.98 €, apertura)
- 2026-10-01 15:20 [c_banda_atr] ENTRADA INJ @ 6.661 (22.25 €, apertura)
- 2026-10-01 15:20 [macd_momentum] ENTRADA INJ @ 6.661 (21.86 €, apertura)
- 2026-10-01 15:20 [macd_sin_salida] ENTRADA INJ @ 6.661 (22.01 €, apertura)
- 2026-10-01 15:20 [c_banda_atr_evento] ENTRADA INJ @ 6.661 (22.40 €, apertura)
- 2026-10-01 15:20 [macd_momentum_evento] ENTRADA INJ @ 6.661 (21.98 €, apertura)
- 2026-10-01 15:20 [c_banda_atr] ENTRADA OP @ 0.1148 (22.25 €, apertura)
- 2026-10-01 15:20 [macd_momentum] ENTRADA OP @ 0.1148 (21.86 €, apertura)
- 2026-10-01 15:20 [macd_sin_salida] ENTRADA OP @ 0.1148 (22.01 €, apertura)
- 2026-10-01 15:20 [c_banda_atr_evento] ENTRADA OP @ 0.1148 (22.40 €, apertura)
- 2026-10-01 15:20 [macd_momentum_evento] ENTRADA OP @ 0.1148 (21.98 €, apertura)
- 2026-10-01 15:20 [c_banda_atr] ENTRADA FIL @ 0.899 (22.25 €, apertura)
- 2026-10-01 15:20 [c_banda_atr_evento] ENTRADA FIL @ 0.899 (22.40 €, apertura)
- 2026-10-01 15:20 [c_banda_atr] ENTRADA WLFI @ 0.049 (22.25 €, apertura)
- 2026-10-01 15:20 [c_banda_atr_evento] ENTRADA WLFI @ 0.049 (22.40 €, apertura)
- 2026-10-01 15:25 [c_banda_atr] CIERRE TON take-profit bruto +2.17% neto +1.67%
- 2026-10-01 15:25 [macd_momentum] CIERRE TON take-profit bruto +2.25% neto +1.75%
- 2026-10-01 15:25 [estocastico_rebote] CIERRE TON take-profit bruto +2.17% neto +1.67%
- 2026-10-01 15:25 [macd_sin_salida] CIERRE TON take-profit bruto +2.25% neto +1.75%
- 2026-10-01 15:25 [c_banda_atr_evento] CIERRE TON take-profit bruto +2.17% neto +1.67%
- 2026-10-01 15:25 [macd_momentum_evento] CIERRE TON take-profit bruto +2.25% neto +1.75%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
