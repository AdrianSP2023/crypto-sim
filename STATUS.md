# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 18:42 UTC · vueltas 285 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 892.89 € (-3.39%) | 235 | 15 | 36% | -0.020% | -0.631% | -0.754% | -33.78 € |
| reversion_bb | 917.24 € (-0.76%) | 45 | 3 | 49% | +0.297% | -0.763% | -0.860% | -7.91 € |
| ruptura_volumen | 880.11 € (-4.77%) | 264 | 23 | 26% | -0.166% | -0.765% | -0.874% | -45.70 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 893.59 € (-3.32%) | 161 | 7 | 16% | -0.199% | -0.863% | -0.960% | -31.62 € |
| macd_momentum | 874.16 € (-5.42%) | 423 | 8 | 22% | +0.020% | -0.542% | -0.647% | -51.60 € |
| estocastico_rebote | 878.26 € (-4.98%) | 289 | 4 | 31% | -0.125% | -0.716% | -0.827% | -46.80 € |
| ruptura_estricta | 888.43 € (-3.87%) | 144 | 19 | 25% | -0.476% | -1.159% | -1.281% | -38.07 € |
| macd_sin_salida | 886.93 € (-4.04%) | 292 | 21 | 37% | -0.020% | -0.609% | -0.724% | -40.51 € |
| c_banda_atr_tope | 912.60 € (-1.26%) | 55 | 3 | 31% | +0.014% | -0.966% | -1.084% | -12.21 € |
| ruptura_volumen_tope | 909.01 € (-1.65%) | 89 | 5 | 29% | +0.038% | -0.759% | -0.873% | -15.49 € |
| c_banda_atr_regimen | 903.90 € (-2.20%) | 112 | 10 | 35% | -0.105% | -0.838% | -0.978% | -21.56 € |
| macd_momentum_regimen | 894.33 € (-3.24%) | 226 | 5 | 23% | +0.018% | -0.597% | -0.709% | -30.77 € |
| ruptura_volumen_regimen | 883.85 € (-4.37%) | 196 | 25 | 20% | -0.315% | -0.948% | -1.066% | -42.16 € |
| c_banda_atr_evento | 898.84 € (-2.75%) | 202 | 15 | 37% | +0.028% | -0.603% | -0.720% | -27.85 € |
| macd_momentum_evento | 879.01 € (-4.89%) | 376 | 8 | 20% | +0.019% | -0.551% | -0.653% | -46.77 € |
| ruptura_volumen_evento | 892.63 € (-3.42%) | 214 | 23 | 27% | -0.058% | -0.682% | -0.781% | -33.18 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 18:40 | ruptura_volumen_evento | BNB | timeout | +0.64% | +0.14% | +0.03 |
| 2026-10-01 18:40 | macd_momentum_evento | RENDER | momentum perdido | +0.59% | +0.09% | +0.02 |
| 2026-10-01 18:40 | macd_momentum_regimen | RENDER | momentum perdido | +0.59% | +0.09% | +0.02 |
| 2026-10-01 18:40 | macd_momentum | RENDER | momentum perdido | +0.59% | +0.09% | +0.02 |
| 2026-10-01 18:40 | ruptura_volumen | BNB | timeout | +0.64% | +0.14% | +0.03 |
| 2026-10-01 18:35 | ruptura_volumen_evento | RENDER | timeout | +0.76% | +0.26% | +0.06 |
| 2026-10-01 18:35 | ruptura_volumen_evento | CRV | timeout | +0.33% | -0.17% | -0.04 |
| 2026-10-01 18:35 | ruptura_volumen_evento | SOL | timeout | +0.72% | +0.22% | +0.05 |
| 2026-10-01 18:35 | macd_momentum_evento | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 18:35 | macd_momentum_evento | DASH | momentum perdido | +0.30% | -0.20% | -0.04 |
| 2026-10-01 18:35 | macd_momentum_evento | ASTER | momentum perdido | +0.10% | -0.40% | -0.09 |
| 2026-10-01 18:35 | macd_momentum_evento | FIL | momentum perdido | +1.11% | +0.61% | +0.13 |
| 2026-10-01 18:35 | macd_momentum_evento | MINA | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-01 18:35 | c_banda_atr_evento | MINA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 18:35 | ruptura_volumen_regimen | RENDER | timeout | +0.76% | +0.26% | +0.06 |

## Eventos de la última vuelta

- 2026-10-01 18:35 [ruptura_volumen] ENTRADA HYPE @ 78.53 (21.96 €, apertura)
- 2026-10-01 18:35 [ruptura_volumen_tope] ENTRADA HYPE @ 78.53 (22.72 €, apertura)
- 2026-10-01 18:35 [ruptura_volumen_regimen] ENTRADA HYPE @ 78.53 (22.05 €, apertura)
- 2026-10-01 18:35 [ruptura_volumen_evento] ENTRADA HYPE @ 78.53 (22.28 €, apertura)
- 2026-10-01 18:40 [macd_momentum] CIERRE RENDER momentum perdido bruto +0.59% neto +0.09%
- 2026-10-01 18:40 [macd_momentum_regimen] CIERRE RENDER momentum perdido bruto +0.59% neto +0.09%
- 2026-10-01 18:40 [macd_momentum_evento] CIERRE RENDER momentum perdido bruto +0.59% neto +0.09%
- 2026-10-01 18:35 [ruptura_volumen] ENTRADA MINA @ 0.1345 (21.96 €, apertura)
- 2026-10-01 18:35 [ruptura_volumen_regimen] ENTRADA MINA @ 0.1345 (22.05 €, apertura)
- 2026-10-01 18:35 [ruptura_volumen_evento] ENTRADA MINA @ 0.1345 (22.28 €, apertura)
- 2026-10-01 18:40 [ruptura_volumen] CIERRE BNB timeout bruto +0.64% neto +0.14%
- 2026-10-01 18:40 [ruptura_volumen_evento] CIERRE BNB timeout bruto +0.64% neto +0.14%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
