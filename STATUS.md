# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 16:01 UTC · vueltas 259 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.65 € (-3.74%) | 215 | 20 | 33% | -0.086% | -0.707% | -0.832% | -34.63 € |
| reversion_bb | 915.85 € (-0.91%) | 38 | 9 | 39% | +0.067% | -1.033% | -1.133% | -9.04 € |
| ruptura_volumen | 879.47 € (-4.84%) | 241 | 7 | 23% | -0.219% | -0.827% | -0.935% | -45.15 € |
| rebote_extremo | 922.04 € (-0.24%) | 12 | 1 | 50% | +0.217% | -0.883% | -1.057% | -2.45 € |
| pullback_tendencia | 892.83 € (-3.40%) | 145 | 5 | 13% | -0.284% | -0.966% | -1.067% | -31.87 € |
| macd_momentum | 874.84 € (-5.34%) | 364 | 21 | 20% | -0.042% | -0.614% | -0.722% | -50.35 € |
| estocastico_rebote | 878.62 € (-4.94%) | 277 | 10 | 31% | -0.145% | -0.739% | -0.852% | -46.34 € |
| ruptura_estricta | 885.61 € (-4.18%) | 137 | 6 | 23% | -0.562% | -1.254% | -1.376% | -39.15 € |
| macd_sin_salida | 882.39 € (-4.53%) | 258 | 24 | 34% | -0.131% | -0.732% | -0.849% | -42.94 € |
| c_banda_atr_tope | 912.43 € (-1.28%) | 50 | 5 | 28% | -0.015% | -1.043% | -1.156% | -11.99 € |
| ruptura_volumen_tope | 907.73 € (-1.79%) | 80 | 5 | 25% | -0.069% | -0.899% | -1.014% | -16.50 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 895.58 € (-3.10%) | 182 | 20 | 34% | -0.045% | -0.690% | -0.808% | -28.70 € |
| macd_momentum_evento | 879.69 € (-4.82%) | 317 | 21 | 17% | -0.053% | -0.636% | -0.740% | -45.51 € |
| ruptura_volumen_evento | 891.99 € (-3.49%) | 191 | 7 | 24% | -0.112% | -0.751% | -0.847% | -32.63 € |
| rebote_desplome | 925.36 € (+0.12%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 925.36 € (+0.12%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 16:00 | macd_sin_salida | PEPE | take-profit | +2.06% | +1.56% | +0.34 |
| 2026-10-01 16:00 | rebote_extremo | PUMP | take-profit | +2.07% | +0.97% | +0.22 |
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

## Eventos de la última vuelta

- 2026-10-01 15:55 [macd_momentum] ENTRADA ETH @ 2389.16 (21.85 €, apertura)
- 2026-10-01 15:55 [macd_momentum_evento] ENTRADA ETH @ 2389.16 (21.97 €, apertura)
- 2026-10-01 16:00 [rebote_extremo] CIERRE PUMP take-profit bruto +2.07% neto +0.97%
- 2026-10-01 15:55 [macd_momentum] ENTRADA UNI @ 8.0934 (21.85 €, apertura)
- 2026-10-01 15:55 [macd_sin_salida] ENTRADA UNI @ 8.0934 (22.02 €, apertura)
- 2026-10-01 15:55 [macd_momentum_evento] ENTRADA UNI @ 8.0934 (21.97 €, apertura)
- 2026-10-01 15:55 [ruptura_estricta] ENTRADA TRX @ 0.297432 (22.13 €, apertura)
- 2026-10-01 16:00 [macd_sin_salida] CIERRE PEPE take-profit bruto +2.06% neto +1.56%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
