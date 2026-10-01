# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 23:46 UTC · vueltas 346 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.24 € (-4.22%) | 262 | 28 | 35% | -0.045% | -0.644% | -0.767% | -38.37 € |
| reversion_bb | 917.68 € (-0.71%) | 52 | 16 | 50% | +0.317% | -0.685% | -0.782% | -8.21 € |
| ruptura_volumen | 871.69 € (-5.69%) | 297 | 4 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.03 € (-3.81%) | 187 | 5 | 15% | -0.194% | -0.836% | -0.925% | -35.47 € |
| macd_momentum | 863.33 € (-6.59%) | 487 | 12 | 20% | -0.011% | -0.564% | -0.667% | -61.52 € |
| estocastico_rebote | 872.41 € (-5.61%) | 327 | 14 | 31% | -0.130% | -0.709% | -0.819% | -52.33 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 871.51 € (-5.71%) | 346 | 11 | 34% | -0.099% | -0.674% | -0.785% | -52.70 € |
| c_banda_atr_tope | 911.11 € (-1.42%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.75 € (-2.00%) | 101 | 4 | 27% | -0.042% | -0.803% | -0.920% | -18.58 € |
| c_banda_atr_regimen | 896.48 € (-3.00%) | 132 | 6 | 30% | -0.211% | -0.909% | -1.043% | -27.45 € |
| macd_momentum_regimen | 885.23 € (-4.22%) | 276 | 0 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 874.82 € (-5.35%) | 230 | 0 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 891.13 € (-3.58%) | 229 | 28 | 35% | -0.007% | -0.622% | -0.739% | -32.47 € |
| macd_momentum_evento | 868.11 € (-6.07%) | 440 | 12 | 19% | -0.015% | -0.575% | -0.674% | -56.74 € |
| ruptura_volumen_evento | 884.09 € (-4.34%) | 247 | 4 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 23:45 | macd_momentum_evento | WLFI | momentum perdido | +0.40% | -0.10% | -0.02 |
| 2026-10-01 23:45 | c_banda_atr_evento | WLD | timeout | +1.78% | +1.28% | +0.29 |
| 2026-10-01 23:45 | macd_momentum | WLFI | momentum perdido | +0.40% | -0.10% | -0.02 |
| 2026-10-01 23:45 | reversion_bb | ONDO | take-profit | +1.50% | +1.00% | +0.23 |
| 2026-10-01 23:45 | c_banda_atr | WLD | timeout | +1.78% | +1.28% | +0.28 |
| 2026-10-01 23:40 | estocastico_rebote | TRX | timeout | -0.23% | -0.73% | -0.16 |
| 2026-10-01 23:40 | pullback_tendencia | SKY | timeout | +0.65% | +0.15% | +0.03 |
| 2026-10-01 23:35 | macd_sin_salida | FET | timeout | -0.24% | -0.74% | -0.16 |
| 2026-10-01 23:25 | macd_momentum_evento | BCH | momentum perdido | -0.12% | -0.62% | -0.14 |
| 2026-10-01 23:25 | macd_momentum_evento | NIGHT | momentum perdido | -0.38% | -0.88% | -0.19 |
| 2026-10-01 23:25 | macd_sin_salida | BTC | timeout | -0.08% | -0.58% | -0.13 |
| 2026-10-01 23:25 | macd_momentum | BCH | momentum perdido | -0.12% | -0.62% | -0.13 |
| 2026-10-01 23:25 | macd_momentum | NIGHT | momentum perdido | -0.38% | -0.88% | -0.19 |
| 2026-10-01 23:20 | macd_momentum_evento | TRUMP | momentum perdido | -0.49% | -0.99% | -0.21 |
| 2026-10-01 23:20 | macd_sin_salida | XMR | timeout | +0.06% | -0.44% | -0.10 |

## Eventos de la última vuelta

- 2026-10-01 23:40 [macd_momentum] ENTRADA SUI @ 1.0434 (21.57 €, apertura)
- 2026-10-01 23:40 [macd_sin_salida] ENTRADA SUI @ 1.0434 (21.79 €, apertura)
- 2026-10-01 23:40 [macd_momentum_evento] ENTRADA SUI @ 1.0434 (21.69 €, apertura)
- 2026-10-01 23:45 [reversion_bb] CIERRE ONDO take-profit bruto +1.50% neto +1.00%
- 2026-10-01 23:40 [ruptura_volumen] ENTRADA ONDO @ 0.43947 (21.79 €, apertura)
- 2026-10-01 23:40 [ruptura_volumen_tope] ENTRADA ONDO @ 0.43947 (22.64 €, apertura)
- 2026-10-01 23:40 [ruptura_volumen_evento] ENTRADA ONDO @ 0.43947 (22.10 €, apertura)
- 2026-10-01 23:45 [c_banda_atr] CIERRE WLD timeout bruto +1.78% neto +1.28%
- 2026-10-01 23:45 [c_banda_atr_evento] CIERRE WLD timeout bruto +1.78% neto +1.28%
- 2026-10-01 23:45 [macd_momentum] CIERRE WLFI momentum perdido bruto +0.40% neto -0.10%
- 2026-10-01 23:45 [macd_momentum_evento] CIERRE WLFI momentum perdido bruto +0.40% neto -0.10%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
