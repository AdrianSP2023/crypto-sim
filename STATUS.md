# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 15:56 UTC · vueltas 258 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.65 € (-3.74%) | 215 | 20 | 33% | -0.086% | -0.707% | -0.832% | -34.63 € |
| reversion_bb | 915.97 € (-0.89%) | 38 | 9 | 39% | +0.067% | -1.033% | -1.133% | -9.04 € |
| ruptura_volumen | 879.62 € (-4.83%) | 241 | 7 | 23% | -0.219% | -0.827% | -0.935% | -45.15 € |
| rebote_extremo | 922.23 € (-0.22%) | 11 | 2 | 45% | +0.049% | -1.051% | -1.228% | -2.67 € |
| pullback_tendencia | 892.97 € (-3.38%) | 145 | 5 | 13% | -0.284% | -0.966% | -1.067% | -31.87 € |
| macd_momentum | 874.73 € (-5.36%) | 364 | 19 | 20% | -0.042% | -0.614% | -0.722% | -50.35 € |
| estocastico_rebote | 878.64 € (-4.93%) | 277 | 10 | 31% | -0.145% | -0.739% | -0.852% | -46.34 € |
| ruptura_estricta | 885.76 € (-4.16%) | 137 | 5 | 23% | -0.562% | -1.254% | -1.376% | -39.15 € |
| macd_sin_salida | 882.32 € (-4.54%) | 257 | 24 | 33% | -0.140% | -0.741% | -0.858% | -43.29 € |
| c_banda_atr_tope | 912.50 € (-1.27%) | 50 | 5 | 28% | -0.015% | -1.043% | -1.156% | -11.99 € |
| ruptura_volumen_tope | 907.87 € (-1.77%) | 80 | 5 | 25% | -0.069% | -0.899% | -1.014% | -16.50 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 895.58 € (-3.10%) | 182 | 20 | 34% | -0.045% | -0.690% | -0.808% | -28.70 € |
| macd_momentum_evento | 879.58 € (-4.83%) | 317 | 19 | 17% | -0.053% | -0.636% | -0.740% | -45.51 € |
| ruptura_volumen_evento | 892.13 € (-3.47%) | 191 | 7 | 24% | -0.112% | -0.751% | -0.847% | -32.63 € |
| rebote_desplome | 925.25 € (+0.11%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 925.25 € (+0.11%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 15:55 | ruptura_volumen_evento | SKY | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 15:55 | ruptura_volumen | SKY | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-01 15:50 | macd_momentum_evento | SKY | take-profit | +2.17% | +1.67% | +0.37 |
| 2026-10-01 15:50 | macd_momentum_evento | ASTER | momentum perdido | -0.61% | -1.11% | -0.24 |
| 2026-10-01 15:50 | c_banda_atr_evento | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 15:50 | ruptura_volumen_tope | SKY | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 15:50 | c_banda_atr_tope | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 15:50 | macd_sin_salida | SKY | take-profit | +2.17% | +1.67% | +0.37 |
| 2026-10-01 15:50 | macd_momentum | SKY | take-profit | +2.17% | +1.67% | +0.36 |
| 2026-10-01 15:50 | macd_momentum | ASTER | momentum perdido | -0.61% | -1.11% | -0.24 |
| 2026-10-01 15:50 | reversion_bb | SUI | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-10-01 15:50 | c_banda_atr | ZRO | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 15:45 | macd_momentum_evento | USELESS | momentum perdido | +0.19% | -0.31% | -0.07 |
| 2026-10-01 15:45 | macd_momentum_evento | ARB | momentum perdido | -0.51% | -1.00% | -0.22 |
| 2026-10-01 15:45 | macd_momentum_evento | LINK | momentum perdido | -0.71% | -1.21% | -0.27 |

## Eventos de la última vuelta

- 2026-10-01 15:50 [macd_sin_salida] ENTRADA BTC @ 74969.6 (22.02 €, apertura)
- 2026-10-01 15:50 [c_banda_atr_tope] ENTRADA BTC @ 74969.6 (22.81 €, apertura)
- 2026-10-01 15:50 [macd_momentum] ENTRADA SOL @ 104.52 (21.85 €, apertura)
- 2026-10-01 15:50 [macd_momentum_evento] ENTRADA SOL @ 104.52 (21.97 €, apertura)
- 2026-10-01 15:50 [c_banda_atr] ENTRADA SUI @ 1.0233 (22.24 €, apertura)
- 2026-10-01 15:50 [c_banda_atr_evento] ENTRADA SUI @ 1.0233 (22.39 €, apertura)
- 2026-10-01 15:50 [macd_momentum] ENTRADA AAVE @ 149.8 (21.85 €, apertura)
- 2026-10-01 15:50 [macd_sin_salida] ENTRADA AAVE @ 149.8 (22.02 €, apertura)
- 2026-10-01 15:50 [macd_momentum_evento] ENTRADA AAVE @ 149.8 (21.97 €, apertura)
- 2026-10-01 15:50 [c_banda_atr] ENTRADA UNI @ 8.1545 (22.24 €, apertura)
- 2026-10-01 15:50 [c_banda_atr_evento] ENTRADA UNI @ 8.1545 (22.39 €, apertura)
- 2026-10-01 15:50 [ruptura_volumen_tope] ENTRADA ZRO @ 1.526 (22.69 €, apertura)
- 2026-10-01 15:50 [macd_momentum] ENTRADA ARB @ 0.1794 (21.85 €, apertura)
- 2026-10-01 15:50 [macd_momentum_evento] ENTRADA ARB @ 0.1794 (21.97 €, apertura)
- 2026-10-01 15:55 [ruptura_volumen] CIERRE SKY take-profit bruto +2.50% neto +2.00%
- 2026-10-01 15:55 [ruptura_volumen_evento] CIERRE SKY take-profit bruto +2.50% neto +2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
