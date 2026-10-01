# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 23:51 UTC · vueltas 347 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.77 € (-4.27%) | 263 | 27 | 35% | -0.046% | -0.646% | -0.768% | -38.59 € |
| reversion_bb | 917.60 € (-0.72%) | 52 | 16 | 50% | +0.317% | -0.685% | -0.782% | -8.21 € |
| ruptura_volumen | 871.74 € (-5.68%) | 297 | 4 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.90 € (-3.82%) | 187 | 5 | 15% | -0.194% | -0.836% | -0.925% | -35.47 € |
| macd_momentum | 863.11 € (-6.61%) | 488 | 12 | 20% | -0.012% | -0.565% | -0.669% | -61.76 € |
| estocastico_rebote | 872.19 € (-5.63%) | 327 | 14 | 31% | -0.130% | -0.709% | -0.819% | -52.33 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 0 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 871.29 € (-5.73%) | 346 | 11 | 34% | -0.099% | -0.674% | -0.785% | -52.70 € |
| c_banda_atr_tope | 911.05 € (-1.43%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.81 € (-1.99%) | 101 | 4 | 27% | -0.042% | -0.803% | -0.920% | -18.58 € |
| c_banda_atr_regimen | 896.42 € (-3.01%) | 132 | 6 | 30% | -0.211% | -0.909% | -1.043% | -27.45 € |
| macd_momentum_regimen | 885.23 € (-4.22%) | 276 | 0 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 874.82 € (-5.35%) | 230 | 0 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 890.66 € (-3.63%) | 230 | 27 | 35% | -0.009% | -0.624% | -0.741% | -32.69 € |
| macd_momentum_evento | 867.89 € (-6.10%) | 441 | 12 | 19% | -0.016% | -0.576% | -0.676% | -56.99 € |
| ruptura_volumen_evento | 884.14 € (-4.34%) | 247 | 4 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 23:50 | macd_momentum_evento | DASH | momentum perdido | -0.65% | -1.15% | -0.25 |
| 2026-10-01 23:50 | c_banda_atr_evento | SUI | timeout | -0.51% | -1.01% | -0.23 |
| 2026-10-01 23:50 | macd_momentum | DASH | momentum perdido | -0.65% | -1.15% | -0.25 |
| 2026-10-01 23:50 | c_banda_atr | SUI | timeout | -0.51% | -1.01% | -0.22 |
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

## Eventos de la última vuelta

- 2026-10-01 23:50 [c_banda_atr] CIERRE SUI timeout bruto -0.51% neto -1.01%
- 2026-10-01 23:50 [c_banda_atr_evento] CIERRE SUI timeout bruto -0.51% neto -1.01%
- 2026-10-01 23:50 [macd_momentum] CIERRE DASH momentum perdido bruto -0.65% neto -1.15%
- 2026-10-01 23:50 [macd_momentum_evento] CIERRE DASH momentum perdido bruto -0.65% neto -1.15%
- 2026-10-01 23:45 [macd_momentum] ENTRADA SPX @ 0.3905 (21.56 €, apertura)
- 2026-10-01 23:45 [macd_momentum_evento] ENTRADA SPX @ 0.3905 (21.68 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
