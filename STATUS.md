# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 08:07 UTC · vueltas 183 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 893.58 € (-3.32%) | 142 | 29 | 26% | -0.297% | -0.981% | -1.110% | -31.79 € |
| reversion_bb | 915.21 € (-0.98%) | 39 | 7 | 41% | +0.017% | -1.083% | -1.197% | -9.72 € |
| ruptura_volumen | 885.66 € (-4.17%) | 177 | 13 | 17% | -0.330% | -0.977% | -1.108% | -39.24 € |
| rebote_extremo | 923.54 € (-0.08%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.889% | -1.33 € |
| pullback_tendencia | 902.70 € (-2.33%) | 119 | 2 | 24% | -0.072% | -0.791% | -0.918% | -21.55 € |
| macd_momentum | 875.09 € (-5.32%) | 325 | 18 | 16% | -0.097% | -0.678% | -0.788% | -49.68 € |
| estocastico_rebote | 887.97 € (-3.92%) | 220 | 14 | 34% | -0.128% | -0.747% | -0.880% | -37.42 € |
| ruptura_estricta | 901.64 € (-2.45%) | 78 | 8 | 22% | -0.442% | -1.277% | -1.425% | -22.80 € |
| macd_sin_salida | 886.73 € (-4.06%) | 203 | 22 | 27% | -0.187% | -0.816% | -0.939% | -37.60 € |
| c_banda_atr_tope | 909.92 € (-1.55%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.66 € (-1.69%) | 63 | 5 | 16% | -0.208% | -1.127% | -1.250% | -16.28 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 895.19 € (-3.14%) | 126 | 6 | 17% | -0.305% | -1.012% | -1.143% | -29.06 € |
| c_banda_atr_evento | 896.63 € (-2.99%) | 110 | 29 | 23% | -0.403% | -1.143% | -1.273% | -28.74 € |
| macd_momentum_evento | 887.39 € (-3.99%) | 205 | 18 | 13% | -0.174% | -0.803% | -0.910% | -37.38 € |
| ruptura_volumen_evento | 891.11 € (-3.58%) | 118 | 13 | 9% | -0.534% | -1.257% | -1.391% | -33.78 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 08:05 | macd_momentum_evento | CRV | momentum perdido | -0.23% | -0.73% | -0.16 |
| 2026-09-30 08:05 | c_banda_atr_evento | BNB | timeout | -0.58% | -1.08% | -0.24 |
| 2026-09-30 08:05 | c_banda_atr_evento | AAVE | timeout | -0.82% | -1.32% | -0.30 |
| 2026-09-30 08:05 | macd_sin_salida | TRX | timeout | +0.32% | -0.18% | -0.04 |
| 2026-09-30 08:05 | macd_sin_salida | XDC | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 08:05 | macd_sin_salida | LTC | timeout | -0.49% | -0.99% | -0.22 |
| 2026-09-30 08:05 | macd_momentum | CRV | momentum perdido | -0.23% | -0.73% | -0.16 |
| 2026-09-30 08:05 | c_banda_atr | BNB | timeout | -0.58% | -1.08% | -0.24 |
| 2026-09-30 08:05 | c_banda_atr | AAVE | timeout | -0.82% | -1.32% | -0.30 |
| 2026-09-30 07:55 | macd_momentum_evento | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 07:55 | c_banda_atr_evento | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 07:55 | c_banda_atr_tope | MON | take-profit | +2.00% | +0.90% | +0.20 |
| 2026-09-30 07:55 | macd_sin_salida | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 07:55 | macd_momentum | MON | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 07:55 | c_banda_atr | MON | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-09-30 08:05 [macd_sin_salida] CIERRE LTC timeout bruto -0.49% neto -0.99%
- 2026-09-30 08:05 [c_banda_atr] CIERRE AAVE timeout bruto -0.82% neto -1.32%
- 2026-09-30 08:05 [c_banda_atr_evento] CIERRE AAVE timeout bruto -0.82% neto -1.32%
- 2026-09-30 08:00 [macd_momentum] ENTRADA XDC @ 0.03014 (21.87 €, apertura)
- 2026-09-30 08:00 [ruptura_estricta] ENTRADA XDC @ 0.03014 (22.54 €, apertura)
- 2026-09-30 08:05 [macd_sin_salida] CIERRE XDC take-profit bruto +2.00% neto +1.50%
- 2026-09-30 08:00 [macd_momentum_evento] ENTRADA XDC @ 0.03014 (22.18 €, apertura)
- 2026-09-30 08:05 [macd_momentum] CIERRE CRV momentum perdido bruto -0.23% neto -0.73%
- 2026-09-30 08:05 [macd_momentum_evento] CIERRE CRV momentum perdido bruto -0.23% neto -0.73%
- 2026-09-30 08:05 [macd_sin_salida] CIERRE TRX timeout bruto +0.32% neto -0.18%
- 2026-09-30 08:00 [c_banda_atr] ENTRADA VIRTUAL @ 0.6931 (22.32 €, apertura)
- 2026-09-30 08:00 [c_banda_atr_tope] ENTRADA VIRTUAL @ 0.6931 (22.73 €, apertura)
- 2026-09-30 08:00 [c_banda_atr_evento] ENTRADA VIRTUAL @ 0.6931 (22.39 €, apertura)
- 2026-09-30 08:00 [macd_momentum] ENTRADA MINA @ 0.1262 (21.86 €, apertura)
- 2026-09-30 08:00 [macd_sin_salida] ENTRADA MINA @ 0.1262 (22.17 €, apertura)
- 2026-09-30 08:00 [macd_momentum_evento] ENTRADA MINA @ 0.1262 (22.17 €, apertura)
- 2026-09-30 08:00 [c_banda_atr] ENTRADA POL @ 0.10182 (22.32 €, apertura)
- 2026-09-30 08:00 [c_banda_atr_evento] ENTRADA POL @ 0.10182 (22.39 €, apertura)
- 2026-09-30 08:05 [c_banda_atr] CIERRE BNB timeout bruto -0.58% neto -1.08%
- 2026-09-30 08:05 [c_banda_atr_evento] CIERRE BNB timeout bruto -0.58% neto -1.08%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
