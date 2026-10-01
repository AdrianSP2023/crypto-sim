# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 15:46 UTC · vueltas 256 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.97 € (-3.92%) | 214 | 19 | 33% | -0.095% | -0.717% | -0.842% | -34.96 € |
| reversion_bb | 915.21 € (-0.98%) | 37 | 10 | 38% | +0.028% | -1.072% | -1.174% | -9.13 € |
| ruptura_volumen | 878.85 € (-4.91%) | 240 | 8 | 22% | -0.230% | -0.839% | -0.947% | -45.59 € |
| rebote_extremo | 921.70 € (-0.28%) | 11 | 2 | 45% | +0.049% | -1.051% | -1.228% | -2.67 € |
| pullback_tendencia | 892.43 € (-3.44%) | 145 | 3 | 13% | -0.284% | -0.966% | -1.067% | -31.87 € |
| macd_momentum | 873.05 € (-5.54%) | 362 | 18 | 20% | -0.047% | -0.619% | -0.727% | -50.47 € |
| estocastico_rebote | 877.77 € (-5.03%) | 277 | 10 | 31% | -0.145% | -0.739% | -0.852% | -46.34 € |
| ruptura_estricta | 885.03 € (-4.24%) | 137 | 5 | 23% | -0.562% | -1.254% | -1.376% | -39.15 € |
| macd_sin_salida | 879.67 € (-4.82%) | 256 | 23 | 33% | -0.149% | -0.751% | -0.867% | -43.66 € |
| c_banda_atr_tope | 911.79 € (-1.35%) | 49 | 5 | 27% | -0.057% | -1.095% | -1.209% | -12.33 € |
| ruptura_volumen_tope | 907.60 € (-1.80%) | 79 | 5 | 24% | -0.102% | -0.936% | -1.051% | -16.96 € |
| c_banda_atr_regimen | 902.02 € (-2.40%) | 110 | 0 | 34% | -0.143% | -0.880% | -1.020% | -22.23 € |
| macd_momentum_regimen | 893.82 € (-3.29%) | 206 | 0 | 22% | -0.021% | -0.648% | -0.761% | -30.42 € |
| ruptura_volumen_regimen | 883.79 € (-4.38%) | 185 | 0 | 19% | -0.322% | -0.963% | -1.078% | -40.45 € |
| c_banda_atr_evento | 893.88 € (-3.28%) | 181 | 19 | 34% | -0.056% | -0.702% | -0.821% | -29.04 € |
| macd_momentum_evento | 877.89 € (-5.02%) | 315 | 18 | 17% | -0.058% | -0.642% | -0.746% | -45.63 € |
| ruptura_volumen_evento | 891.36 € (-3.56%) | 190 | 8 | 23% | -0.126% | -0.765% | -0.862% | -33.07 € |
| rebote_desplome | 924.91 € (+0.07%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.91 € (+0.07%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 15:45 | macd_momentum_evento | USELESS | momentum perdido | +0.19% | -0.31% | -0.07 |
| 2026-10-01 15:45 | macd_momentum_evento | ARB | momentum perdido | -0.51% | -1.00% | -0.22 |
| 2026-10-01 15:45 | macd_momentum_evento | LINK | momentum perdido | -0.71% | -1.21% | -0.27 |
| 2026-10-01 15:45 | macd_momentum_evento | SOL | momentum perdido | -0.56% | -1.06% | -0.23 |
| 2026-10-01 15:45 | c_banda_atr_evento | SKY | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 15:45 | c_banda_atr_evento | WLD | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 15:45 | c_banda_atr_evento | TAO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 15:45 | macd_momentum | USELESS | momentum perdido | +0.19% | -0.31% | -0.07 |
| 2026-10-01 15:45 | macd_momentum | ARB | momentum perdido | -0.51% | -1.00% | -0.22 |
| 2026-10-01 15:45 | macd_momentum | LINK | momentum perdido | -0.71% | -1.21% | -0.26 |
| 2026-10-01 15:45 | macd_momentum | SOL | momentum perdido | -0.56% | -1.06% | -0.23 |
| 2026-10-01 15:45 | pullback_tendencia | BNB | rotura de tendencia | -0.20% | -0.70% | -0.15 |
| 2026-10-01 15:45 | pullback_tendencia | TAO | rotura de tendencia | -0.97% | -1.47% | -0.33 |
| 2026-10-01 15:45 | c_banda_atr | SKY | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 15:45 | c_banda_atr | WLD | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-10-01 15:45 [macd_momentum] CIERRE SOL momentum perdido bruto -0.56% neto -1.06%
- 2026-10-01 15:45 [macd_momentum_evento] CIERRE SOL momentum perdido bruto -0.56% neto -1.06%
- 2026-10-01 15:45 [macd_momentum] CIERRE LINK momentum perdido bruto -0.71% neto -1.21%
- 2026-10-01 15:45 [macd_momentum_evento] CIERRE LINK momentum perdido bruto -0.71% neto -1.21%
- 2026-10-01 15:45 [c_banda_atr] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 15:45 [pullback_tendencia] CIERRE TAO rotura de tendencia bruto -0.97% neto -1.47%
- 2026-10-01 15:45 [c_banda_atr_evento] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 15:45 [macd_momentum] CIERRE ARB momentum perdido bruto -0.51% neto -1.01%
- 2026-10-01 15:45 [macd_momentum_evento] CIERRE ARB momentum perdido bruto -0.51% neto -1.01%
- 2026-10-01 15:45 [c_banda_atr] CIERRE WLD stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 15:45 [c_banda_atr_evento] CIERRE WLD stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 15:45 [macd_momentum] CIERRE USELESS momentum perdido bruto +0.19% neto -0.31%
- 2026-10-01 15:45 [macd_momentum_evento] CIERRE USELESS momentum perdido bruto +0.19% neto -0.31%
- 2026-10-01 15:45 [pullback_tendencia] CIERRE BNB rotura de tendencia bruto -0.20% neto -0.70%
- 2026-10-01 15:45 [c_banda_atr] CIERRE SKY take-profit bruto +2.00% neto +1.50%
- 2026-10-01 15:45 [c_banda_atr_evento] CIERRE SKY take-profit bruto +2.00% neto +1.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
