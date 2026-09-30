# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 03:01 UTC · vueltas 183 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.98 € (-2.63%) | 104 | 21 | 28% | -0.292% | -1.043% | -1.183% | -24.86 € |
| reversion_bb | 918.71 € (-0.60%) | 29 | 6 | 48% | +0.205% | -0.895% | -0.997% | -5.98 € |
| ruptura_volumen | 896.25 € (-3.03%) | 136 | 15 | 22% | -0.202% | -0.894% | -1.025% | -27.74 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.43 € (-2.04%) | 104 | 5 | 26% | -0.036% | -0.787% | -0.915% | -18.75 € |
| macd_momentum | 882.92 € (-4.47%) | 260 | 5 | 17% | -0.099% | -0.700% | -0.812% | -41.26 € |
| estocastico_rebote | 893.49 € (-3.33%) | 179 | 19 | 35% | -0.091% | -0.737% | -0.871% | -30.18 € |
| ruptura_estricta | 905.19 € (-2.06%) | 64 | 5 | 25% | -0.322% | -1.230% | -1.372% | -18.06 € |
| macd_sin_salida | 896.85 € (-2.96%) | 152 | 17 | 30% | -0.114% | -0.786% | -0.911% | -27.30 € |
| c_banda_atr_tope | 910.73 € (-1.46%) | 35 | 5 | 17% | -0.565% | -1.665% | -1.801% | -13.39 € |
| ruptura_volumen_tope | 911.37 € (-1.39%) | 49 | 5 | 18% | -0.084% | -1.123% | -1.247% | -12.65 € |
| c_banda_atr_regimen | 901.93 € (-2.41%) | 70 | 8 | 24% | -0.493% | -1.366% | -1.501% | -21.94 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 900.81 € (-2.54%) | 106 | 10 | 20% | -0.219% | -0.965% | -1.100% | -23.40 € |
| c_banda_atr_evento | 903.05 € (-2.29%) | 72 | 21 | 24% | -0.452% | -1.319% | -1.464% | -21.80 € |
| macd_momentum_evento | 895.33 € (-3.13%) | 140 | 5 | 14% | -0.214% | -0.902% | -1.011% | -28.84 € |
| ruptura_volumen_evento | 901.77 € (-2.43%) | 77 | 15 | 14% | -0.417% | -1.260% | -1.395% | -22.21 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 03:00 | macd_momentum_evento | HBAR | momentum perdido | -0.41% | -0.91% | -0.20 |
| 2026-09-30 03:00 | c_banda_atr_evento | WLD | stop-loss | -1.52% | -2.02% | -0.46 |
| 2026-09-30 03:00 | c_banda_atr_regimen | WLD | stop-loss | -1.52% | -2.02% | -0.46 |
| 2026-09-30 03:00 | ruptura_estricta | PENGU | stop-loss | -2.00% | -2.50% | -0.57 |
| 2026-09-30 03:00 | macd_momentum | HBAR | momentum perdido | -0.41% | -0.91% | -0.20 |
| 2026-09-30 03:00 | c_banda_atr | WLD | stop-loss | -1.52% | -2.02% | -0.46 |
| 2026-09-30 02:55 | ruptura_volumen_evento | PENGU | stop-loss | -1.56% | -2.06% | -0.47 |
| 2026-09-30 02:55 | estocastico_rebote | PEPE | timeout | +0.93% | +0.43% | +0.10 |
| 2026-09-30 02:55 | ruptura_volumen | PENGU | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-09-30 02:50 | pullback_tendencia | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 02:45 | ruptura_volumen_evento | SPX | timeout | +0.78% | +0.28% | +0.06 |
| 2026-09-30 02:45 | c_banda_atr_evento | TRX | timeout | -0.02% | -0.52% | -0.12 |
| 2026-09-30 02:45 | ruptura_volumen | SPX | timeout | +0.78% | +0.28% | +0.06 |
| 2026-09-30 02:45 | c_banda_atr | TRX | timeout | -0.02% | -0.52% | -0.12 |
| 2026-09-30 02:40 | macd_momentum_evento | DASH | momentum perdido | -0.21% | -0.71% | -0.16 |

## Eventos de la última vuelta

- 2026-09-30 03:00 [macd_momentum] CIERRE HBAR momentum perdido bruto -0.40% neto -0.90%
- 2026-09-30 03:00 [macd_momentum_evento] CIERRE HBAR momentum perdido bruto -0.40% neto -0.90%
- 2026-09-30 03:00 [c_banda_atr] CIERRE WLD stop-loss bruto -1.52% neto -2.02%
- 2026-09-30 03:00 [c_banda_atr_regimen] CIERRE WLD stop-loss bruto -1.52% neto -2.02%
- 2026-09-30 03:00 [c_banda_atr_evento] CIERRE WLD stop-loss bruto -1.52% neto -2.02%
- 2026-09-30 02:55 [estocastico_rebote] ENTRADA NIGHT @ 0.02862 (22.35 €, apertura)
- 2026-09-30 02:55 [macd_momentum] ENTRADA FIL @ 0.942 (22.07 €, apertura)
- 2026-09-30 02:55 [macd_sin_salida] ENTRADA FIL @ 0.942 (22.42 €, apertura)
- 2026-09-30 02:55 [macd_momentum_evento] ENTRADA FIL @ 0.942 (22.38 €, apertura)
- 2026-09-30 03:00 [ruptura_estricta] CIERRE PENGU stop-loss bruto -2.00% neto -2.50%
- 2026-09-30 02:55 [macd_momentum] ENTRADA BNB @ 672.52 (22.07 €, apertura)
- 2026-09-30 02:55 [macd_momentum_evento] ENTRADA BNB @ 672.52 (22.38 €, apertura)
- 2026-09-30 02:55 [estocastico_rebote] ENTRADA ASTER @ 0.65403 (22.35 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
