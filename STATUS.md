# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 18:47 UTC · vueltas 286 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 892.16 € (-3.47%) | 235 | 20 | 36% | -0.020% | -0.631% | -0.754% | -33.78 € |
| reversion_bb | 916.93 € (-0.79%) | 46 | 2 | 50% | +0.324% | -0.730% | -0.827% | -7.74 € |
| ruptura_volumen | 879.23 € (-4.87%) | 264 | 25 | 26% | -0.166% | -0.765% | -0.874% | -45.70 € |
| rebote_extremo | 922.00 € (-0.24%) | 13 | 0 | 54% | +0.355% | -0.745% | -0.915% | -2.24 € |
| pullback_tendencia | 893.24 € (-3.35%) | 161 | 7 | 16% | -0.199% | -0.863% | -0.960% | -31.62 € |
| macd_momentum | 873.58 € (-5.48%) | 423 | 14 | 22% | +0.020% | -0.542% | -0.647% | -51.60 € |
| estocastico_rebote | 878.14 € (-4.99%) | 289 | 6 | 31% | -0.125% | -0.716% | -0.827% | -46.80 € |
| ruptura_estricta | 887.64 € (-3.96%) | 144 | 20 | 25% | -0.476% | -1.159% | -1.281% | -38.07 € |
| macd_sin_salida | 885.89 € (-4.15%) | 292 | 24 | 37% | -0.020% | -0.609% | -0.724% | -40.51 € |
| c_banda_atr_tope | 912.24 € (-1.30%) | 55 | 5 | 31% | +0.014% | -0.966% | -1.084% | -12.21 € |
| ruptura_volumen_tope | 909.06 € (-1.64%) | 89 | 5 | 29% | +0.038% | -0.759% | -0.873% | -15.49 € |
| c_banda_atr_regimen | 903.20 € (-2.28%) | 112 | 16 | 35% | -0.105% | -0.838% | -0.978% | -21.56 € |
| macd_momentum_regimen | 893.95 € (-3.28%) | 226 | 11 | 23% | +0.018% | -0.597% | -0.709% | -30.77 € |
| ruptura_volumen_regimen | 882.85 € (-4.48%) | 196 | 27 | 20% | -0.315% | -0.948% | -1.066% | -42.16 € |
| c_banda_atr_evento | 898.09 € (-2.83%) | 202 | 20 | 37% | +0.028% | -0.603% | -0.720% | -27.85 € |
| macd_momentum_evento | 878.42 € (-4.96%) | 376 | 14 | 20% | +0.019% | -0.551% | -0.653% | -46.77 € |
| ruptura_volumen_evento | 891.74 € (-3.52%) | 214 | 25 | 27% | -0.058% | -0.682% | -0.781% | -33.18 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 18:45 | reversion_bb | DOT | take-profit | +1.55% | +0.76% | +0.17 |
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

## Eventos de la última vuelta

- 2026-10-01 18:40 [macd_momentum] ENTRADA XRP @ 1.34066 (21.82 €, apertura)
- 2026-10-01 18:40 [macd_sin_salida] ENTRADA XRP @ 1.34066 (22.09 €, apertura)
- 2026-10-01 18:40 [macd_momentum_regimen] ENTRADA XRP @ 1.34066 (22.34 €, apertura)
- 2026-10-01 18:40 [macd_momentum_evento] ENTRADA XRP @ 1.34066 (21.94 €, apertura)
- 2026-10-01 18:40 [macd_momentum] ENTRADA ETH @ 2412.5 (21.82 €, apertura)
- 2026-10-01 18:40 [macd_momentum_regimen] ENTRADA ETH @ 2412.5 (22.34 €, apertura)
- 2026-10-01 18:40 [macd_momentum_evento] ENTRADA ETH @ 2412.5 (21.94 €, apertura)
- 2026-10-01 18:40 [ruptura_volumen] ENTRADA LINK @ 12.8376 (21.96 €, apertura)
- 2026-10-01 18:40 [ruptura_volumen_regimen] ENTRADA LINK @ 12.8376 (22.05 €, apertura)
- 2026-10-01 18:40 [ruptura_volumen_evento] ENTRADA LINK @ 12.8376 (22.28 €, apertura)
- 2026-10-01 18:40 [macd_momentum] ENTRADA XLM @ 0.196654 (21.82 €, apertura)
- 2026-10-01 18:40 [macd_momentum_regimen] ENTRADA XLM @ 0.196654 (22.34 €, apertura)
- 2026-10-01 18:40 [macd_momentum_evento] ENTRADA XLM @ 0.196654 (21.94 €, apertura)
- 2026-10-01 18:40 [macd_momentum] ENTRADA UNI @ 8.1351 (21.82 €, apertura)
- 2026-10-01 18:40 [c_banda_atr_tope] ENTRADA UNI @ 8.1351 (22.80 €, apertura)
- 2026-10-01 18:40 [macd_momentum_regimen] ENTRADA UNI @ 8.1351 (22.34 €, apertura)
- 2026-10-01 18:40 [macd_momentum_evento] ENTRADA UNI @ 8.1351 (21.94 €, apertura)
- 2026-10-01 18:45 [reversion_bb] CIERRE DOT take-profit bruto +1.55% neto +0.75%
- 2026-10-01 18:40 [ruptura_volumen] ENTRADA ALGO @ 0.11272 (21.96 €, apertura)
- 2026-10-01 18:40 [ruptura_estricta] ENTRADA ALGO @ 0.11272 (22.15 €, apertura)
- 2026-10-01 18:40 [ruptura_volumen_regimen] ENTRADA ALGO @ 0.11272 (22.05 €, apertura)
- 2026-10-01 18:40 [ruptura_volumen_evento] ENTRADA ALGO @ 0.11272 (22.28 €, apertura)
- 2026-10-01 18:40 [c_banda_atr] ENTRADA ONDO @ 0.44295 (22.26 €, apertura)
- 2026-10-01 18:40 [c_banda_atr_tope] ENTRADA ONDO @ 0.44295 (22.80 €, apertura)
- 2026-10-01 18:40 [c_banda_atr_regimen] ENTRADA ONDO @ 0.44295 (22.57 €, apertura)
- 2026-10-01 18:40 [c_banda_atr_evento] ENTRADA ONDO @ 0.44295 (22.41 €, apertura)
- 2026-10-01 18:40 [c_banda_atr] ENTRADA WLD @ 0.4432 (22.26 €, apertura)
- 2026-10-01 18:40 [c_banda_atr_regimen] ENTRADA WLD @ 0.4432 (22.57 €, apertura)
- 2026-10-01 18:40 [c_banda_atr_evento] ENTRADA WLD @ 0.4432 (22.41 €, apertura)
- 2026-10-01 18:40 [c_banda_atr] ENTRADA BCH @ 274.24 (22.26 €, apertura)
- 2026-10-01 18:40 [c_banda_atr_regimen] ENTRADA BCH @ 274.24 (22.57 €, apertura)
- 2026-10-01 18:40 [c_banda_atr_evento] ENTRADA BCH @ 274.24 (22.41 €, apertura)
- 2026-10-01 18:40 [c_banda_atr_regimen] ENTRADA PEPE @ 3.97e-06 (22.57 €, apertura)
- 2026-10-01 18:40 [c_banda_atr] ENTRADA OP @ 0.1155 (22.26 €, apertura)
- 2026-10-01 18:40 [macd_momentum] ENTRADA OP @ 0.1155 (21.82 €, apertura)
- 2026-10-01 18:40 [macd_sin_salida] ENTRADA OP @ 0.1155 (22.09 €, apertura)
- 2026-10-01 18:40 [c_banda_atr_regimen] ENTRADA OP @ 0.1155 (22.57 €, apertura)
- 2026-10-01 18:40 [macd_momentum_regimen] ENTRADA OP @ 0.1155 (22.34 €, apertura)
- 2026-10-01 18:40 [c_banda_atr_evento] ENTRADA OP @ 0.1155 (22.41 €, apertura)
- 2026-10-01 18:40 [macd_momentum_evento] ENTRADA OP @ 0.1155 (21.94 €, apertura)
- 2026-10-01 18:40 [c_banda_atr] ENTRADA ASTER @ 0.66208 (22.26 €, apertura)
- 2026-10-01 18:40 [macd_momentum] ENTRADA ASTER @ 0.66208 (21.82 €, apertura)
- 2026-10-01 18:40 [macd_sin_salida] ENTRADA ASTER @ 0.66208 (22.09 €, apertura)
- 2026-10-01 18:40 [c_banda_atr_regimen] ENTRADA ASTER @ 0.66208 (22.57 €, apertura)
- 2026-10-01 18:40 [macd_momentum_regimen] ENTRADA ASTER @ 0.66208 (22.34 €, apertura)
- 2026-10-01 18:40 [c_banda_atr_evento] ENTRADA ASTER @ 0.66208 (22.41 €, apertura)
- 2026-10-01 18:40 [macd_momentum_evento] ENTRADA ASTER @ 0.66208 (21.94 €, apertura)
- 2026-10-01 18:40 [estocastico_rebote] ENTRADA BNB @ 686.08 (21.94 €, apertura)
- 2026-10-01 18:40 [estocastico_rebote] ENTRADA APT @ 0.6915 (21.94 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
