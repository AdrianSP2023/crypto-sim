# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 05:06 UTC · vueltas 396 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.84 € (-3.51%) | 321 | 14 | 39% | +0.118% | -0.464% | -0.584% | -33.95 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.382% | -4.66 € |
| ruptura_volumen | 870.88 € (-5.77%) | 364 | 38 | 26% | -0.119% | -0.691% | -0.799% | -56.52 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 892.26 € (-3.46%) | 209 | 8 | 19% | -0.078% | -0.704% | -0.792% | -33.46 € |
| macd_momentum | 862.79 € (-6.65%) | 584 | 36 | 23% | +0.058% | -0.487% | -0.588% | -63.55 € |
| estocastico_rebote | 879.24 € (-4.87%) | 372 | 10 | 35% | +0.021% | -0.549% | -0.658% | -46.28 € |
| ruptura_estricta | 890.32 € (-3.67%) | 191 | 39 | 30% | -0.244% | -0.883% | -0.998% | -38.44 € |
| macd_sin_salida | 884.00 € (-4.35%) | 407 | 21 | 40% | +0.109% | -0.455% | -0.565% | -42.27 € |
| c_banda_atr_tope | 912.83 € (-1.23%) | 71 | 4 | 34% | +0.148% | -0.724% | -0.833% | -11.81 € |
| ruptura_volumen_tope | 903.79 € (-2.21%) | 117 | 5 | 26% | -0.045% | -0.771% | -0.885% | -20.64 € |
| c_banda_atr_regimen | 904.41 € (-2.15%) | 174 | 13 | 40% | +0.127% | -0.523% | -0.651% | -20.97 € |
| macd_momentum_regimen | 885.89 € (-4.15%) | 347 | 36 | 22% | +0.060% | -0.515% | -0.619% | -40.49 € |
| ruptura_volumen_regimen | 875.61 € (-5.26%) | 287 | 38 | 23% | -0.210% | -0.801% | -0.913% | -51.81 € |
| c_banda_atr_evento | 897.77 € (-2.86%) | 288 | 14 | 40% | +0.166% | -0.425% | -0.541% | -28.02 € |
| macd_momentum_evento | 867.57 € (-6.13%) | 537 | 36 | 22% | +0.061% | -0.489% | -0.587% | -58.79 € |
| ruptura_volumen_evento | 883.27 € (-4.43%) | 314 | 38 | 27% | -0.038% | -0.622% | -0.723% | -44.17 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 05:05 | ruptura_volumen_evento | KAS | timeout | +0.88% | +0.38% | +0.08 |
| 2026-10-02 05:05 | ruptura_volumen_evento | RENDER | timeout | +1.50% | +1.00% | +0.22 |
| 2026-10-02 05:05 | ruptura_volumen_evento | BTC | timeout | +1.27% | +0.77% | +0.17 |
| 2026-10-02 05:05 | macd_momentum_evento | QNT | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 05:05 | c_banda_atr_evento | BNB | timeout | +1.11% | +0.61% | +0.14 |
| 2026-10-02 05:05 | c_banda_atr_evento | ICP | timeout | +0.07% | -0.43% | -0.10 |
| 2026-10-02 05:05 | c_banda_atr_evento | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 05:05 | ruptura_volumen_regimen | KAS | timeout | +0.88% | +0.38% | +0.08 |
| 2026-10-02 05:05 | ruptura_volumen_regimen | RENDER | timeout | +1.50% | +1.00% | +0.22 |
| 2026-10-02 05:05 | ruptura_volumen_regimen | BTC | timeout | +1.27% | +0.77% | +0.17 |
| 2026-10-02 05:05 | macd_momentum_regimen | QNT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 05:05 | c_banda_atr_regimen | BNB | timeout | +1.11% | +0.61% | +0.14 |
| 2026-10-02 05:05 | c_banda_atr_regimen | ICP | timeout | +0.07% | -0.43% | -0.10 |
| 2026-10-02 05:05 | c_banda_atr_regimen | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 05:05 | c_banda_atr_tope | BNB | timeout | +1.11% | +0.61% | +0.14 |

## Eventos de la última vuelta

- 2026-10-02 05:05 [ruptura_volumen] CIERRE BTC timeout bruto +1.27% neto +0.77%
- 2026-10-02 05:05 [ruptura_volumen_regimen] CIERRE BTC timeout bruto +1.27% neto +0.77%
- 2026-10-02 05:05 [ruptura_volumen_evento] CIERRE BTC timeout bruto +1.27% neto +0.77%
- 2026-10-02 05:05 [c_banda_atr] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:05 [macd_momentum] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:05 [macd_sin_salida] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:05 [c_banda_atr_regimen] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:05 [macd_momentum_regimen] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:05 [c_banda_atr_evento] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:05 [macd_momentum_evento] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 05:05 [c_banda_atr] CIERRE ICP timeout bruto +0.07% neto -0.43%
- 2026-10-02 05:05 [c_banda_atr_regimen] CIERRE ICP timeout bruto +0.07% neto -0.43%
- 2026-10-02 05:05 [c_banda_atr_evento] CIERRE ICP timeout bruto +0.07% neto -0.43%
- 2026-10-02 05:05 [ruptura_estricta] CIERRE PEPE stop-loss bruto -2.00% neto -2.50%
- 2026-10-02 05:05 [ruptura_volumen] CIERRE RENDER timeout bruto +1.50% neto +1.00%
- 2026-10-02 05:05 [ruptura_volumen_regimen] CIERRE RENDER timeout bruto +1.50% neto +1.00%
- 2026-10-02 05:05 [ruptura_volumen_evento] CIERRE RENDER timeout bruto +1.50% neto +1.00%
- 2026-10-02 05:05 [macd_sin_salida] CIERRE TRUMP timeout bruto +1.74% neto +1.24%
- 2026-10-02 05:05 [c_banda_atr] CIERRE BNB timeout bruto +1.11% neto +0.61%
- 2026-10-02 05:05 [c_banda_atr_tope] CIERRE BNB timeout bruto +1.11% neto +0.61%
- 2026-10-02 05:05 [c_banda_atr_regimen] CIERRE BNB timeout bruto +1.11% neto +0.61%
- 2026-10-02 05:05 [c_banda_atr_evento] CIERRE BNB timeout bruto +1.11% neto +0.61%
- 2026-10-02 05:05 [ruptura_volumen] CIERRE KAS timeout bruto +0.88% neto +0.38%
- 2026-10-02 05:05 [ruptura_volumen_regimen] CIERRE KAS timeout bruto +0.88% neto +0.38%
- 2026-10-02 05:05 [ruptura_volumen_evento] CIERRE KAS timeout bruto +0.88% neto +0.38%
- 2026-10-02 05:00 [ruptura_volumen] ENTRADA SPX @ 0.4008 (21.69 €, apertura)
- 2026-10-02 05:00 [ruptura_volumen_regimen] ENTRADA SPX @ 0.4008 (21.81 €, apertura)
- 2026-10-02 05:00 [ruptura_volumen_evento] ENTRADA SPX @ 0.4008 (22.00 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
