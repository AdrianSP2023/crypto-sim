# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 21:46 UTC · vueltas 322 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.43 € (-4.31%) | 257 | 15 | 35% | -0.041% | -0.643% | -0.765% | -37.55 € |
| reversion_bb | 915.37 € (-0.96%) | 50 | 14 | 50% | +0.330% | -0.692% | -0.789% | -7.97 € |
| ruptura_volumen | 871.98 € (-5.65%) | 292 | 5 | 25% | -0.200% | -0.789% | -0.898% | -51.96 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.94 € (-3.82%) | 185 | 2 | 15% | -0.200% | -0.842% | -0.932% | -35.38 € |
| macd_momentum | 864.03 € (-6.52%) | 476 | 4 | 21% | -0.011% | -0.566% | -0.668% | -60.34 € |
| estocastico_rebote | 871.94 € (-5.66%) | 306 | 22 | 31% | -0.128% | -0.714% | -0.825% | -49.34 € |
| ruptura_estricta | 882.86 € (-4.48%) | 165 | 1 | 25% | -0.432% | -1.092% | -1.208% | -40.99 € |
| macd_sin_salida | 872.03 € (-5.65%) | 330 | 17 | 35% | -0.092% | -0.671% | -0.784% | -50.13 € |
| c_banda_atr_tope | 910.75 € (-1.46%) | 61 | 3 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.69 € (-2.01%) | 98 | 3 | 28% | -0.034% | -0.803% | -0.919% | -18.03 € |
| c_banda_atr_regimen | 896.47 € (-3.00%) | 128 | 10 | 31% | -0.195% | -0.899% | -1.035% | -26.33 € |
| macd_momentum_regimen | 885.24 € (-4.22%) | 273 | 3 | 19% | -0.037% | -0.633% | -0.738% | -39.17 € |
| ruptura_volumen_regimen | 875.20 € (-5.31%) | 225 | 5 | 20% | -0.343% | -0.959% | -1.074% | -48.73 € |
| c_banda_atr_evento | 890.32 € (-3.67%) | 224 | 15 | 36% | -0.002% | -0.619% | -0.736% | -31.64 € |
| macd_momentum_evento | 868.81 € (-6.00%) | 429 | 4 | 19% | -0.015% | -0.577% | -0.676% | -55.56 € |
| ruptura_volumen_evento | 884.38 € (-4.31%) | 242 | 5 | 26% | -0.112% | -0.721% | -0.821% | -39.54 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 21:45 | c_banda_atr_regimen | PEPE | stop-loss | -1.51% | -2.01% | -0.45 |
| 2026-10-01 21:45 | c_banda_atr_tope | UNI | stop-loss | -1.58% | -2.08% | -0.47 |
| 2026-10-01 21:45 | macd_sin_salida | PEPE | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 21:45 | macd_sin_salida | DOT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 21:45 | estocastico_rebote | SPX | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 21:45 | estocastico_rebote | FIL | stop-loss | -1.65% | -2.15% | -0.47 |
| 2026-10-01 21:45 | pullback_tendencia | LTC | rotura de tendencia | +0.10% | -0.40% | -0.09 |
| 2026-10-01 21:45 | reversion_bb | CRV | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 21:40 | macd_momentum_evento | BCH | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-01 21:40 | c_banda_atr_evento | LINK | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 21:40 | macd_momentum_regimen | BCH | momentum perdido | -0.24% | -0.74% | -0.17 |
| 2026-10-01 21:40 | c_banda_atr_regimen | LINK | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 21:40 | macd_sin_salida | ASTER | timeout | -1.02% | -1.52% | -0.34 |
| 2026-10-01 21:40 | macd_sin_salida | ALGO | stop-loss | -1.57% | -2.07% | -0.46 |
| 2026-10-01 21:40 | macd_sin_salida | TAO | stop-loss | -1.50% | -2.00% | -0.44 |

## Eventos de la última vuelta

- 2026-10-01 21:40 [reversion_bb] ENTRADA AVAX @ 9.681 (22.92 €, apertura)
- 2026-10-01 21:40 [reversion_bb] ENTRADA HYPE @ 77.23 (22.92 €, apertura)
- 2026-10-01 21:45 [c_banda_atr_tope] CIERRE UNI stop-loss bruto -1.58% neto -2.08%
- 2026-10-01 21:45 [pullback_tendencia] CIERRE LTC rotura de tendencia bruto +0.10% neto -0.40%
- 2026-10-01 21:45 [macd_sin_salida] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 21:45 [reversion_bb] CIERRE CRV stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 21:45 [macd_sin_salida] CIERRE PEPE stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 21:45 [c_banda_atr_regimen] CIERRE PEPE stop-loss bruto -1.51% neto -2.01%
- 2026-10-01 21:45 [estocastico_rebote] CIERRE FIL stop-loss bruto -1.65% neto -2.15%
- 2026-10-01 21:40 [reversion_bb] ENTRADA TRUMP @ 1.819 (22.91 €, apertura)
- 2026-10-01 21:45 [estocastico_rebote] CIERRE SPX timeout bruto +0.23% neto -0.27%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
