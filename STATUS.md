# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 02:56 UTC · vueltas 182 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 900.65 € (-2.55%) | 103 | 22 | 28% | -0.280% | -1.033% | -1.172% | -24.41 € |
| reversion_bb | 918.92 € (-0.58%) | 29 | 6 | 48% | +0.205% | -0.895% | -0.997% | -5.98 € |
| ruptura_volumen | 896.45 € (-3.01%) | 136 | 15 | 22% | -0.202% | -0.894% | -1.025% | -27.74 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.57 € (-2.02%) | 104 | 5 | 26% | -0.036% | -0.787% | -0.915% | -18.75 € |
| macd_momentum | 883.09 € (-4.45%) | 259 | 4 | 17% | -0.098% | -0.699% | -0.812% | -41.06 € |
| estocastico_rebote | 893.98 € (-3.27%) | 179 | 17 | 35% | -0.091% | -0.737% | -0.871% | -30.18 € |
| ruptura_estricta | 905.82 € (-1.99%) | 63 | 6 | 25% | -0.295% | -1.209% | -1.353% | -17.50 € |
| macd_sin_salida | 897.04 € (-2.94%) | 152 | 16 | 30% | -0.114% | -0.786% | -0.911% | -27.30 € |
| c_banda_atr_tope | 910.89 € (-1.44%) | 35 | 5 | 17% | -0.565% | -1.665% | -1.801% | -13.39 € |
| ruptura_volumen_tope | 911.52 € (-1.38%) | 49 | 5 | 18% | -0.084% | -1.123% | -1.247% | -12.65 € |
| c_banda_atr_regimen | 902.58 € (-2.34%) | 69 | 9 | 25% | -0.478% | -1.356% | -1.490% | -21.48 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 900.89 € (-2.53%) | 106 | 10 | 20% | -0.219% | -0.965% | -1.100% | -23.40 € |
| c_banda_atr_evento | 903.72 € (-2.22%) | 71 | 22 | 24% | -0.437% | -1.309% | -1.453% | -21.34 € |
| macd_momentum_evento | 895.51 € (-3.11%) | 139 | 4 | 14% | -0.212% | -0.902% | -1.012% | -28.64 € |
| ruptura_volumen_evento | 901.97 € (-2.41%) | 77 | 15 | 14% | -0.417% | -1.260% | -1.395% | -22.21 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 02:55 | ruptura_volumen_evento | PENGU | stop-loss | -1.56% | -2.06% | -0.47 |
| 2026-09-30 02:55 | estocastico_rebote | PEPE | timeout | +0.93% | +0.43% | +0.10 |
| 2026-09-30 02:55 | ruptura_volumen | PENGU | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-09-30 02:50 | pullback_tendencia | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 02:45 | ruptura_volumen_evento | SPX | timeout | +0.78% | +0.28% | +0.06 |
| 2026-09-30 02:45 | c_banda_atr_evento | TRX | timeout | -0.02% | -0.52% | -0.12 |
| 2026-09-30 02:45 | ruptura_volumen | SPX | timeout | +0.78% | +0.28% | +0.06 |
| 2026-09-30 02:45 | c_banda_atr | TRX | timeout | -0.02% | -0.52% | -0.12 |
| 2026-09-30 02:40 | macd_momentum_evento | DASH | momentum perdido | -0.21% | -0.71% | -0.16 |
| 2026-09-30 02:40 | ruptura_volumen_regimen | PENGU | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 02:40 | macd_momentum_regimen | DASH | momentum perdido | -0.21% | -0.71% | -0.16 |
| 2026-09-30 02:40 | macd_momentum | DASH | momentum perdido | -0.21% | -0.71% | -0.16 |
| 2026-09-30 02:40 | pullback_tendencia | PENGU | rotura de tendencia | -0.82% | -1.32% | -0.30 |
| 2026-09-30 02:35 | macd_momentum_evento | SPX | momentum perdido | +1.22% | +0.72% | +0.16 |
| 2026-09-30 02:35 | macd_momentum_evento | BNB | momentum perdido | +0.03% | -0.47% | -0.11 |

## Eventos de la última vuelta

- 2026-09-30 02:50 [pullback_tendencia] ENTRADA QNT @ 250.78 (22.64 €, apertura)
- 2026-09-30 02:50 [macd_momentum] ENTRADA HBAR @ 0.09144 (22.08 €, apertura)
- 2026-09-30 02:50 [macd_sin_salida] ENTRADA HBAR @ 0.09144 (22.42 €, apertura)
- 2026-09-30 02:50 [macd_momentum_evento] ENTRADA HBAR @ 0.09144 (22.39 €, apertura)
- 2026-09-30 02:50 [macd_momentum] ENTRADA ADA @ 0.216948 (22.08 €, apertura)
- 2026-09-30 02:50 [macd_momentum_evento] ENTRADA ADA @ 0.216948 (22.39 €, apertura)
- 2026-09-30 02:50 [pullback_tendencia] ENTRADA SUI @ 1.0242 (22.64 €, apertura)
- 2026-09-30 02:50 [c_banda_atr_tope] ENTRADA DOT @ 1.0721 (22.77 €, apertura)
- 2026-09-30 02:50 [c_banda_atr] ENTRADA ENA @ 0.2211 (22.50 €, apertura)
- 2026-09-30 02:50 [macd_momentum] ENTRADA ENA @ 0.2211 (22.08 €, apertura)
- 2026-09-30 02:50 [macd_sin_salida] ENTRADA ENA @ 0.2211 (22.42 €, apertura)
- 2026-09-30 02:50 [ruptura_volumen_tope] ENTRADA ENA @ 0.2211 (22.79 €, apertura)
- 2026-09-30 02:50 [c_banda_atr_evento] ENTRADA ENA @ 0.2211 (22.57 €, apertura)
- 2026-09-30 02:50 [macd_momentum_evento] ENTRADA ENA @ 0.2211 (22.39 €, apertura)
- 2026-09-30 02:50 [macd_momentum] ENTRADA VVV @ 23.993 (22.08 €, apertura)
- 2026-09-30 02:50 [macd_momentum_evento] ENTRADA VVV @ 23.993 (22.39 €, apertura)
- 2026-09-30 02:50 [c_banda_atr] ENTRADA TRX @ 0.295653 (22.50 €, apertura)
- 2026-09-30 02:50 [c_banda_atr_evento] ENTRADA TRX @ 0.295653 (22.57 €, apertura)
- 2026-09-30 02:55 [estocastico_rebote] CIERRE PEPE timeout bruto +0.93% neto +0.43%
- 2026-09-30 02:50 [c_banda_atr] ENTRADA FIL @ 0.942 (22.50 €, apertura)
- 2026-09-30 02:50 [c_banda_atr_evento] ENTRADA FIL @ 0.942 (22.57 €, apertura)
- 2026-09-30 02:55 [ruptura_volumen] CIERRE PENGU stop-loss bruto -1.56% neto -2.06%
- 2026-09-30 02:55 [ruptura_volumen_evento] CIERRE PENGU stop-loss bruto -1.56% neto -2.06%
- 2026-09-30 02:50 [estocastico_rebote] ENTRADA TRUMP @ 1.835 (22.35 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
