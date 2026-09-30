# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 03:31 UTC · vueltas 189 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 896.34 € (-3.02%) | 112 | 14 | 27% | -0.286% | -1.020% | -1.155% | -26.16 € |
| reversion_bb | 918.15 € (-0.66%) | 29 | 9 | 48% | +0.205% | -0.895% | -0.997% | -5.98 € |
| ruptura_volumen | 893.17 € (-3.36%) | 147 | 4 | 20% | -0.245% | -0.923% | -1.049% | -30.92 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.93 € (-2.09%) | 109 | 0 | 26% | -0.034% | -0.773% | -0.900% | -19.31 € |
| macd_momentum | 881.35 € (-4.64%) | 267 | 1 | 17% | -0.113% | -0.711% | -0.821% | -42.98 € |
| estocastico_rebote | 890.29 € (-3.67%) | 186 | 17 | 34% | -0.117% | -0.757% | -0.889% | -32.18 € |
| ruptura_estricta | 904.24 € (-2.16%) | 65 | 4 | 25% | -0.348% | -1.249% | -1.393% | -18.63 € |
| macd_sin_salida | 893.49 € (-3.33%) | 157 | 14 | 29% | -0.152% | -0.818% | -0.943% | -29.31 € |
| c_banda_atr_tope | 910.06 € (-1.53%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.24 € (-1.51%) | 52 | 2 | 17% | -0.153% | -1.161% | -1.284% | -13.86 € |
| c_banda_atr_regimen | 900.59 € (-2.56%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 898.95 € (-2.74%) | 112 | 4 | 19% | -0.249% | -0.982% | -1.112% | -25.12 € |
| c_banda_atr_evento | 899.40 € (-2.69%) | 80 | 14 | 22% | -0.429% | -1.259% | -1.397% | -23.10 € |
| macd_momentum_evento | 893.74 € (-3.30%) | 147 | 1 | 13% | -0.232% | -0.912% | -1.019% | -30.58 € |
| ruptura_volumen_evento | 898.66 € (-2.77%) | 88 | 4 | 12% | -0.462% | -1.262% | -1.389% | -25.41 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 03:30 | ruptura_volumen_evento | SHIB | timeout | -1.13% | -1.63% | -0.37 |
| 2026-09-30 03:30 | ruptura_volumen_evento | CRV | stop-loss | -1.44% | -1.94% | -0.44 |
| 2026-09-30 03:30 | ruptura_volumen_evento | HBAR | timeout | +0.10% | -0.40% | -0.09 |
| 2026-09-30 03:30 | ruptura_volumen_regimen | SHIB | timeout | -1.13% | -1.63% | -0.37 |
| 2026-09-30 03:30 | ruptura_volumen_regimen | HBAR | timeout | +0.10% | -0.40% | -0.09 |
| 2026-09-30 03:30 | ruptura_volumen_tope | CRV | stop-loss | -1.44% | -1.94% | -0.44 |
| 2026-09-30 03:30 | macd_sin_salida | SEI | timeout | -0.37% | -0.87% | -0.20 |
| 2026-09-30 03:30 | estocastico_rebote | PUMP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 03:30 | ruptura_volumen | SHIB | timeout | -1.13% | -1.63% | -0.37 |
| 2026-09-30 03:30 | ruptura_volumen | CRV | stop-loss | -1.44% | -1.94% | -0.44 |
| 2026-09-30 03:30 | ruptura_volumen | HBAR | timeout | +0.10% | -0.40% | -0.09 |
| 2026-09-30 03:25 | ruptura_volumen_evento | DOT | timeout | -0.65% | -1.15% | -0.26 |
| 2026-09-30 03:25 | ruptura_volumen_evento | XRP | timeout | -0.47% | -0.97% | -0.22 |
| 2026-09-30 03:25 | macd_momentum_evento | BNB | momentum perdido | -0.50% | -1.00% | -0.23 |
| 2026-09-30 03:25 | macd_momentum_evento | VVV | momentum perdido | -1.33% | -1.83% | -0.41 |

## Eventos de la última vuelta

- 2026-09-30 03:30 [ruptura_volumen] CIERRE HBAR timeout bruto +0.10% neto -0.40%
- 2026-09-30 03:30 [ruptura_volumen_regimen] CIERRE HBAR timeout bruto +0.10% neto -0.40%
- 2026-09-30 03:30 [ruptura_volumen_evento] CIERRE HBAR timeout bruto +0.10% neto -0.40%
- 2026-09-30 03:30 [estocastico_rebote] CIERRE PUMP stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 03:30 [ruptura_volumen] CIERRE CRV stop-loss bruto -1.44% neto -1.94%
- 2026-09-30 03:30 [ruptura_volumen_tope] CIERRE CRV stop-loss bruto -1.44% neto -1.94%
- 2026-09-30 03:30 [ruptura_volumen_evento] CIERRE CRV stop-loss bruto -1.44% neto -1.94%
- 2026-09-30 03:25 [estocastico_rebote] ENTRADA PEPE @ 3.757e-06 (22.30 €, apertura)
- 2026-09-30 03:30 [macd_sin_salida] CIERRE SEI timeout bruto -0.37% neto -0.87%
- 2026-09-30 03:30 [ruptura_volumen] CIERRE SHIB timeout bruto -1.13% neto -1.63%
- 2026-09-30 03:30 [ruptura_volumen_regimen] CIERRE SHIB timeout bruto -1.13% neto -1.63%
- 2026-09-30 03:30 [ruptura_volumen_evento] CIERRE SHIB timeout bruto -1.13% neto -1.63%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
