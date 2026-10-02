# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 03:41 UTC · vueltas 379 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.57 € (-4.29%) | 295 | 24 | 35% | -0.002% | -0.590% | -0.711% | -39.54 € |
| reversion_bb | 919.04 € (-0.56%) | 70 | 2 | 60% | +0.530% | -0.343% | -0.445% | -5.55 € |
| ruptura_volumen | 865.89 € (-6.31%) | 339 | 26 | 25% | -0.171% | -0.748% | -0.856% | -56.98 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.90 € (-3.82%) | 198 | 10 | 16% | -0.171% | -0.804% | -0.893% | -36.15 € |
| macd_momentum | 858.84 € (-7.08%) | 555 | 13 | 21% | +0.011% | -0.536% | -0.638% | -66.44 € |
| estocastico_rebote | 872.86 € (-5.56%) | 348 | 18 | 32% | -0.086% | -0.661% | -0.770% | -51.88 € |
| ruptura_estricta | 881.65 € (-4.61%) | 175 | 24 | 26% | -0.422% | -1.073% | -1.189% | -42.66 € |
| macd_sin_salida | 874.43 € (-5.39%) | 371 | 31 | 35% | -0.047% | -0.617% | -0.728% | -51.80 € |
| c_banda_atr_tope | 912.13 € (-1.31%) | 68 | 5 | 32% | +0.108% | -0.780% | -0.894% | -12.20 € |
| ruptura_volumen_tope | 903.23 € (-2.27%) | 113 | 4 | 26% | -0.076% | -0.810% | -0.926% | -20.94 € |
| c_banda_atr_regimen | 896.29 € (-3.02%) | 142 | 30 | 30% | -0.202% | -0.886% | -1.018% | -28.75 € |
| macd_momentum_regimen | 881.83 € (-4.59%) | 318 | 13 | 19% | -0.022% | -0.604% | -0.709% | -43.46 € |
| ruptura_volumen_regimen | 870.36 € (-5.83%) | 264 | 24 | 22% | -0.284% | -0.883% | -0.996% | -52.54 € |
| c_banda_atr_evento | 890.45 € (-3.66%) | 262 | 24 | 36% | +0.037% | -0.564% | -0.680% | -33.65 € |
| macd_momentum_evento | 863.59 € (-6.56%) | 508 | 13 | 19% | +0.009% | -0.543% | -0.641% | -61.69 € |
| ruptura_volumen_evento | 878.21 € (-4.98%) | 289 | 26 | 26% | -0.092% | -0.683% | -0.784% | -44.64 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 03:40 | macd_momentum_evento | SPX | momentum perdido | -0.33% | -0.83% | -0.18 |
| 2026-10-02 03:40 | ruptura_volumen_regimen | OP | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 03:40 | macd_momentum_regimen | SPX | momentum perdido | -0.33% | -0.83% | -0.18 |
| 2026-10-02 03:40 | estocastico_rebote | PEPE | take-profit | +1.85% | +1.35% | +0.29 |
| 2026-10-02 03:40 | macd_momentum | SPX | momentum perdido | -0.33% | -0.83% | -0.18 |
| 2026-10-02 03:40 | reversion_bb | TRUMP | timeout | +0.77% | +0.27% | +0.06 |
| 2026-10-02 03:35 | ruptura_volumen_evento | VVV | timeout | +0.17% | -0.33% | -0.07 |
| 2026-10-02 03:35 | ruptura_volumen_evento | OP | timeout | +0.52% | +0.02% | +0.01 |
| 2026-10-02 03:35 | macd_momentum_evento | MINA | momentum perdido | +0.65% | +0.15% | +0.03 |
| 2026-10-02 03:35 | macd_momentum_evento | JUP | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 03:35 | macd_momentum_evento | UNI | momentum perdido | +0.42% | -0.08% | -0.02 |
| 2026-10-02 03:35 | macd_momentum_evento | ZEC | momentum perdido | -0.28% | -0.78% | -0.17 |
| 2026-10-02 03:35 | macd_momentum_regimen | MINA | momentum perdido | +0.65% | +0.15% | +0.03 |
| 2026-10-02 03:35 | macd_momentum_regimen | JUP | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-02 03:35 | macd_momentum_regimen | UNI | momentum perdido | +0.42% | -0.08% | -0.02 |

## Eventos de la última vuelta

- 2026-10-02 03:35 [estocastico_rebote] ENTRADA SUI @ 1.0522 (21.80 €, apertura)
- 2026-10-02 03:35 [estocastico_rebote] ENTRADA LTC @ 61.1 (21.80 €, apertura)
- 2026-10-02 03:35 [estocastico_rebote] ENTRADA BCH @ 274.41 (21.80 €, apertura)
- 2026-10-02 03:40 [estocastico_rebote] CIERRE PEPE take-profit bruto +1.85% neto +1.35%
- 2026-10-02 03:35 [estocastico_rebote] ENTRADA MON @ 0.03025 (21.81 €, apertura)
- 2026-10-02 03:40 [ruptura_volumen_regimen] CIERRE OP stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 03:40 [reversion_bb] CIERRE TRUMP timeout bruto +0.77% neto +0.27%
- 2026-10-02 03:40 [macd_momentum] CIERRE SPX momentum perdido bruto -0.33% neto -0.83%
- 2026-10-02 03:40 [macd_momentum_regimen] CIERRE SPX momentum perdido bruto -0.33% neto -0.83%
- 2026-10-02 03:40 [macd_momentum_evento] CIERRE SPX momentum perdido bruto -0.33% neto -0.83%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
