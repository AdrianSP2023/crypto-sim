# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 11:51 UTC · vueltas 391 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.85 € (-3.83%) | 358 | 18 | 41% | +0.163% | -0.410% | -0.529% | -33.49 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 1 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 855.74 € (-7.41%) | 450 | 13 | 26% | -0.116% | -0.674% | -0.780% | -67.76 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 888.88 € (-3.83%) | 259 | 11 | 21% | -0.003% | -0.605% | -0.691% | -35.56 € |
| macd_momentum | 847.03 € (-8.35%) | 736 | 10 | 24% | +0.060% | -0.476% | -0.574% | -77.65 € |
| estocastico_rebote | 878.22 € (-4.98%) | 438 | 32 | 38% | +0.116% | -0.444% | -0.551% | -44.12 € |
| ruptura_estricta | 880.45 € (-4.74%) | 247 | 9 | 32% | -0.164% | -0.771% | -0.886% | -43.27 € |
| macd_sin_salida | 875.90 € (-5.23%) | 479 | 26 | 39% | +0.112% | -0.443% | -0.550% | -48.15 € |
| c_banda_atr_tope | 912.88 € (-1.23%) | 82 | 5 | 38% | +0.248% | -0.574% | -0.689% | -10.83 € |
| ruptura_volumen_tope | 898.87 € (-2.74%) | 135 | 4 | 23% | -0.118% | -0.813% | -0.925% | -25.05 € |
| c_banda_atr_regimen | 901.46 € (-2.47%) | 210 | 19 | 43% | +0.195% | -0.430% | -0.556% | -20.79 € |
| macd_momentum_regimen | 869.71 € (-5.90%) | 499 | 10 | 24% | +0.062% | -0.490% | -0.589% | -54.96 € |
| ruptura_volumen_regimen | 860.39 € (-6.91%) | 373 | 13 | 24% | -0.186% | -0.756% | -0.866% | -63.11 € |
| c_banda_atr_evento | 894.77 € (-3.19%) | 325 | 18 | 42% | +0.211% | -0.370% | -0.486% | -27.56 € |
| macd_momentum_evento | 851.73 € (-7.85%) | 689 | 10 | 23% | +0.062% | -0.477% | -0.572% | -72.96 € |
| ruptura_volumen_evento | 867.92 € (-6.09%) | 400 | 13 | 27% | -0.053% | -0.619% | -0.719% | -55.57 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 11:50 | ruptura_volumen_evento | ZEC | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 11:50 | macd_momentum_evento | KAS | momentum perdido | -0.71% | -1.21% | -0.26 |
| 2026-10-02 11:50 | macd_momentum_evento | PENGU | momentum perdido | -0.30% | -0.81% | -0.17 |
| 2026-10-02 11:50 | macd_momentum_evento | OP | momentum perdido | -0.42% | -0.92% | -0.20 |
| 2026-10-02 11:50 | macd_momentum_evento | ENA | momentum perdido | +0.50% | +0.00% | +0.00 |
| 2026-10-02 11:50 | macd_momentum_evento | TAO | momentum perdido | -0.52% | -1.02% | -0.22 |
| 2026-10-02 11:50 | macd_momentum_evento | SOL | momentum perdido | +0.03% | -0.47% | -0.10 |
| 2026-10-02 11:50 | macd_momentum_evento | ETH | momentum perdido | -0.10% | -0.60% | -0.13 |
| 2026-10-02 11:50 | c_banda_atr_evento | SKY | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-02 11:50 | c_banda_atr_evento | BCH | timeout | +0.54% | +0.04% | +0.01 |
| 2026-10-02 11:50 | c_banda_atr_evento | DOT | timeout | -0.28% | -0.78% | -0.17 |
| 2026-10-02 11:50 | ruptura_volumen_regimen | ZEC | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 11:50 | macd_momentum_regimen | KAS | momentum perdido | -0.71% | -1.21% | -0.26 |
| 2026-10-02 11:50 | macd_momentum_regimen | PENGU | momentum perdido | -0.30% | -0.81% | -0.17 |
| 2026-10-02 11:50 | macd_momentum_regimen | OP | momentum perdido | -0.42% | -0.92% | -0.20 |

## Eventos de la última vuelta

- 2026-10-02 11:50 [macd_momentum] CIERRE ETH momentum perdido bruto -0.10% neto -0.60%
- 2026-10-02 11:50 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto -0.10% neto -0.60%
- 2026-10-02 11:50 [macd_momentum_evento] CIERRE ETH momentum perdido bruto -0.10% neto -0.60%
- 2026-10-02 11:50 [macd_momentum] CIERRE SOL momentum perdido bruto +0.03% neto -0.47%
- 2026-10-02 11:50 [macd_momentum_regimen] CIERRE SOL momentum perdido bruto +0.03% neto -0.47%
- 2026-10-02 11:50 [macd_momentum_evento] CIERRE SOL momentum perdido bruto +0.03% neto -0.47%
- 2026-10-02 11:50 [ruptura_volumen] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 11:50 [ruptura_volumen_tope] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 11:50 [ruptura_volumen_regimen] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 11:50 [ruptura_volumen_evento] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 11:50 [macd_momentum] CIERRE TAO momentum perdido bruto -0.52% neto -1.02%
- 2026-10-02 11:50 [macd_momentum_regimen] CIERRE TAO momentum perdido bruto -0.52% neto -1.02%
- 2026-10-02 11:50 [macd_momentum_evento] CIERRE TAO momentum perdido bruto -0.52% neto -1.02%
- 2026-10-02 11:50 [macd_sin_salida] CIERRE ZRO timeout bruto -0.66% neto -1.16%
- 2026-10-02 11:50 [c_banda_atr] CIERRE DOT timeout bruto -0.28% neto -0.78%
- 2026-10-02 11:50 [c_banda_atr_regimen] CIERRE DOT timeout bruto -0.28% neto -0.78%
- 2026-10-02 11:50 [c_banda_atr_evento] CIERRE DOT timeout bruto -0.28% neto -0.78%
- 2026-10-02 11:50 [macd_momentum] CIERRE ENA momentum perdido bruto +0.50% neto +0.00%
- 2026-10-02 11:50 [macd_momentum_regimen] CIERRE ENA momentum perdido bruto +0.50% neto +0.00%
- 2026-10-02 11:50 [macd_momentum_evento] CIERRE ENA momentum perdido bruto +0.50% neto +0.00%
- 2026-10-02 11:45 [macd_momentum] ENTRADA WLD @ 0.4838 (21.18 €, apertura)
- 2026-10-02 11:45 [macd_momentum_regimen] ENTRADA WLD @ 0.4838 (21.75 €, apertura)
- 2026-10-02 11:45 [macd_momentum_evento] ENTRADA WLD @ 0.4838 (21.30 €, apertura)
- 2026-10-02 11:50 [c_banda_atr] CIERRE BCH timeout bruto +0.54% neto +0.04%
- 2026-10-02 11:50 [c_banda_atr_regimen] CIERRE BCH timeout bruto +0.54% neto +0.04%
- 2026-10-02 11:50 [c_banda_atr_evento] CIERRE BCH timeout bruto +0.54% neto +0.04%
- 2026-10-02 11:50 [macd_momentum] CIERRE OP momentum perdido bruto -0.42% neto -0.92%
- 2026-10-02 11:50 [macd_momentum_regimen] CIERRE OP momentum perdido bruto -0.42% neto -0.92%
- 2026-10-02 11:50 [macd_momentum_evento] CIERRE OP momentum perdido bruto -0.42% neto -0.92%
- 2026-10-02 11:45 [reversion_bb] ENTRADA DASH @ 53.103 (22.99 €, apertura)
- 2026-10-02 11:50 [macd_momentum] CIERRE PENGU momentum perdido bruto -0.31% neto -0.81%
- 2026-10-02 11:50 [macd_momentum_regimen] CIERRE PENGU momentum perdido bruto -0.31% neto -0.81%
- 2026-10-02 11:50 [macd_momentum_evento] CIERRE PENGU momentum perdido bruto -0.31% neto -0.81%
- 2026-10-02 11:50 [macd_momentum] CIERRE KAS momentum perdido bruto -0.71% neto -1.21%
- 2026-10-02 11:50 [ruptura_estricta] CIERRE KAS timeout bruto -0.89% neto -1.39%
- 2026-10-02 11:50 [macd_momentum_regimen] CIERRE KAS momentum perdido bruto -0.71% neto -1.21%
- 2026-10-02 11:50 [macd_momentum_evento] CIERRE KAS momentum perdido bruto -0.71% neto -1.21%
- 2026-10-02 11:50 [c_banda_atr] CIERRE SKY take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:50 [c_banda_atr_regimen] CIERRE SKY take-profit bruto +2.00% neto +1.50%
- 2026-10-02 11:50 [c_banda_atr_evento] CIERRE SKY take-profit bruto +2.00% neto +1.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
