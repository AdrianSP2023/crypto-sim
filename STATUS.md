# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 21:41 UTC · vueltas 144 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.55 € (-1.81%) | 61 | 16 | 34% | -0.168% | -1.095% | -1.244% | -15.40 € |
| reversion_bb | 917.86 € (-0.69%) | 18 | 2 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 903.10 € (-2.29%) | 103 | 7 | 23% | -0.137% | -0.890% | -1.021% | -21.01 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.69 € (-1.90%) | 79 | 4 | 24% | -0.152% | -0.982% | -1.102% | -17.80 € |
| macd_momentum | 892.61 € (-3.42%) | 187 | 0 | 18% | -0.102% | -0.742% | -0.858% | -31.64 € |
| estocastico_rebote | 892.98 € (-3.38%) | 153 | 7 | 31% | -0.228% | -0.898% | -1.019% | -31.41 € |
| ruptura_estricta | 910.01 € (-1.54%) | 45 | 6 | 29% | -0.233% | -1.307% | -1.439% | -13.54 € |
| macd_sin_salida | 901.58 € (-2.45%) | 104 | 26 | 32% | -0.095% | -0.846% | -0.978% | -20.17 € |
| c_banda_atr_tope | 914.55 € (-1.05%) | 24 | 5 | 25% | -0.585% | -1.685% | -1.845% | -9.32 € |
| ruptura_volumen_tope | 915.66 € (-0.93%) | 31 | 4 | 16% | -0.099% | -1.199% | -1.321% | -8.56 € |
| c_banda_atr_regimen | 907.70 € (-1.79%) | 53 | 9 | 30% | -0.300% | -1.292% | -1.431% | -15.78 € |
| macd_momentum_regimen | 893.80 € (-3.29%) | 173 | 0 | 17% | -0.120% | -0.771% | -0.886% | -30.44 € |
| ruptura_volumen_regimen | 906.22 € (-1.95%) | 86 | 6 | 24% | -0.091% | -0.894% | -1.026% | -17.65 € |
| c_banda_atr_evento | 912.72 € (-1.25%) | 29 | 16 | 31% | -0.429% | -1.529% | -1.699% | -10.23 € |
| macd_momentum_evento | 905.15 € (-2.07%) | 67 | 0 | 10% | -0.346% | -1.240% | -1.356% | -19.09 € |
| ruptura_volumen_evento | 909.00 € (-1.65%) | 44 | 7 | 14% | -0.426% | -1.492% | -1.631% | -15.10 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 21:40 | ruptura_volumen_evento | RENDER | timeout | +0.18% | -0.62% | -0.14 |
| 2026-09-29 21:40 | ruptura_volumen_regimen | RENDER | timeout | +0.18% | -0.32% | -0.07 |
| 2026-09-29 21:40 | ruptura_volumen | RENDER | timeout | +0.18% | -0.32% | -0.07 |
| 2026-09-29 21:35 | ruptura_volumen_evento | DOT | timeout | -0.27% | -1.07% | -0.24 |
| 2026-09-29 21:35 | macd_momentum_evento | SPX | momentum perdido | +0.19% | -0.61% | -0.14 |
| 2026-09-29 21:35 | macd_momentum_evento | SHIB | momentum perdido | -0.43% | -0.93% | -0.21 |
| 2026-09-29 21:35 | macd_momentum_evento | ATOM | momentum perdido | -0.49% | -1.29% | -0.29 |
| 2026-09-29 21:35 | ruptura_volumen_regimen | DOT | timeout | -0.27% | -0.77% | -0.17 |
| 2026-09-29 21:35 | macd_momentum_regimen | ATOM | momentum perdido | -0.49% | -0.99% | -0.22 |
| 2026-09-29 21:35 | macd_momentum | SPX | momentum perdido | +0.19% | -0.31% | -0.07 |
| 2026-09-29 21:35 | macd_momentum | SHIB | momentum perdido | -0.43% | -0.93% | -0.21 |
| 2026-09-29 21:35 | macd_momentum | ATOM | momentum perdido | -0.49% | -0.99% | -0.22 |
| 2026-09-29 21:35 | ruptura_volumen | DOT | timeout | -0.27% | -0.77% | -0.17 |
| 2026-09-29 21:30 | ruptura_volumen_evento | FET | stop-loss | -1.20% | -2.00% | -0.46 |
| 2026-09-29 21:30 | macd_momentum_evento | ASTER | momentum perdido | -0.42% | -0.93% | -0.21 |

## Eventos de la última vuelta

- 2026-09-29 21:35 [pullback_tendencia] ENTRADA QNT @ 237.23 (22.66 €, apertura)
- 2026-09-29 21:40 [ruptura_volumen] CIERRE RENDER timeout bruto +0.18% neto -0.32%
- 2026-09-29 21:40 [ruptura_volumen_regimen] CIERRE RENDER timeout bruto +0.18% neto -0.32%
- 2026-09-29 21:40 [ruptura_volumen_evento] CIERRE RENDER timeout bruto +0.18% neto -0.62%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
