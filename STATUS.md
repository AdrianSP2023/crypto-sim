# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 03:56 UTC · vueltas 382 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.39 € (-4.31%) | 296 | 25 | 35% | +0.004% | -0.585% | -0.705% | -39.31 € |
| reversion_bb | 919.45 € (-0.52%) | 70 | 3 | 60% | +0.530% | -0.343% | -0.445% | -5.55 € |
| ruptura_volumen | 865.91 € (-6.31%) | 341 | 25 | 25% | -0.173% | -0.750% | -0.858% | -57.46 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.40 € (-3.77%) | 199 | 11 | 16% | -0.160% | -0.793% | -0.881% | -35.81 € |
| macd_momentum | 858.26 € (-7.14%) | 561 | 10 | 21% | +0.011% | -0.536% | -0.637% | -67.04 € |
| estocastico_rebote | 872.97 € (-5.55%) | 348 | 24 | 32% | -0.086% | -0.661% | -0.770% | -51.88 € |
| ruptura_estricta | 881.74 € (-4.60%) | 179 | 21 | 27% | -0.379% | -1.026% | -1.143% | -41.77 € |
| macd_sin_salida | 874.33 € (-5.40%) | 373 | 31 | 35% | -0.049% | -0.619% | -0.729% | -52.17 € |
| c_banda_atr_tope | 912.24 € (-1.30%) | 68 | 5 | 32% | +0.108% | -0.780% | -0.894% | -12.20 € |
| ruptura_volumen_tope | 902.94 € (-2.30%) | 114 | 4 | 25% | -0.076% | -0.807% | -0.922% | -21.05 € |
| c_banda_atr_regimen | 896.58 € (-2.99%) | 142 | 32 | 30% | -0.202% | -0.886% | -1.018% | -28.75 € |
| macd_momentum_regimen | 881.24 € (-4.65%) | 324 | 10 | 19% | -0.021% | -0.602% | -0.705% | -44.08 € |
| ruptura_volumen_regimen | 870.57 € (-5.81%) | 266 | 23 | 21% | -0.287% | -0.885% | -0.997% | -53.01 € |
| c_banda_atr_evento | 890.28 € (-3.67%) | 263 | 25 | 36% | +0.043% | -0.558% | -0.673% | -33.42 € |
| macd_momentum_evento | 863.01 € (-6.62%) | 514 | 10 | 19% | +0.009% | -0.542% | -0.640% | -62.30 € |
| ruptura_volumen_evento | 878.23 € (-4.98%) | 291 | 25 | 26% | -0.096% | -0.686% | -0.787% | -45.12 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 03:55 | ruptura_volumen_evento | ZEC | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 03:55 | ruptura_volumen_evento | ETH | timeout | +0.01% | -0.48% | -0.11 |
| 2026-10-02 03:55 | macd_momentum_evento | AAVE | momentum perdido | -1.03% | -1.53% | -0.33 |
| 2026-10-02 03:55 | c_banda_atr_evento | VVV | timeout | +1.57% | +1.07% | +0.24 |
| 2026-10-02 03:55 | ruptura_volumen_regimen | ZEC | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 03:55 | ruptura_volumen_regimen | ETH | timeout | +0.01% | -0.48% | -0.11 |
| 2026-10-02 03:55 | macd_momentum_regimen | AAVE | momentum perdido | -1.03% | -1.53% | -0.34 |
| 2026-10-02 03:55 | ruptura_volumen_tope | ETH | timeout | +0.01% | -0.48% | -0.11 |
| 2026-10-02 03:55 | macd_sin_salida | MON | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 03:55 | macd_sin_salida | TAO | timeout | +0.80% | +0.30% | +0.06 |
| 2026-10-02 03:55 | ruptura_estricta | HYPE | timeout | +0.59% | +0.09% | +0.02 |
| 2026-10-02 03:55 | macd_momentum | AAVE | momentum perdido | -1.03% | -1.53% | -0.33 |
| 2026-10-02 03:55 | pullback_tendencia | SOL | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 03:55 | ruptura_volumen | ZEC | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 03:55 | ruptura_volumen | ETH | timeout | +0.01% | -0.48% | -0.10 |

## Eventos de la última vuelta

- 2026-10-02 03:55 [ruptura_volumen] CIERRE ETH timeout bruto +0.01% neto -0.49%
- 2026-10-02 03:55 [ruptura_volumen_tope] CIERRE ETH timeout bruto +0.01% neto -0.49%
- 2026-10-02 03:55 [ruptura_volumen_regimen] CIERRE ETH timeout bruto +0.01% neto -0.49%
- 2026-10-02 03:55 [ruptura_volumen_evento] CIERRE ETH timeout bruto +0.01% neto -0.49%
- 2026-10-02 03:55 [pullback_tendencia] CIERRE SOL take-profit bruto +2.00% neto +1.50%
- 2026-10-02 03:55 [macd_momentum] CIERRE AAVE momentum perdido bruto -1.03% neto -1.53%
- 2026-10-02 03:55 [macd_momentum_regimen] CIERRE AAVE momentum perdido bruto -1.03% neto -1.53%
- 2026-10-02 03:55 [macd_momentum_evento] CIERRE AAVE momentum perdido bruto -1.03% neto -1.53%
- 2026-10-02 03:55 [ruptura_volumen] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 03:55 [ruptura_volumen_regimen] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 03:55 [ruptura_volumen_evento] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 03:55 [ruptura_estricta] CIERRE HYPE timeout bruto +0.59% neto +0.09%
- 2026-10-02 03:55 [macd_sin_salida] CIERRE TAO timeout bruto +0.80% neto +0.30%
- 2026-10-02 03:50 [c_banda_atr] ENTRADA XDC @ 0.03027 (22.12 €, apertura)
- 2026-10-02 03:50 [c_banda_atr_regimen] ENTRADA XDC @ 0.03027 (22.39 €, apertura)
- 2026-10-02 03:50 [c_banda_atr_evento] ENTRADA XDC @ 0.03027 (22.26 €, apertura)
- 2026-10-02 03:55 [macd_sin_salida] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 03:55 [c_banda_atr] CIERRE VVV timeout bruto +1.57% neto +1.07%
- 2026-10-02 03:55 [c_banda_atr_evento] CIERRE VVV timeout bruto +1.57% neto +1.07%
- 2026-10-02 03:50 [macd_momentum] ENTRADA BNB @ 688.91 (21.43 €, apertura)
- 2026-10-02 03:50 [macd_sin_salida] ENTRADA BNB @ 688.91 (21.80 €, apertura)
- 2026-10-02 03:50 [macd_momentum_regimen] ENTRADA BNB @ 688.91 (22.00 €, apertura)
- 2026-10-02 03:50 [macd_momentum_evento] ENTRADA BNB @ 688.91 (21.55 €, apertura)
- 2026-10-02 03:50 [macd_momentum] ENTRADA SPX @ 0.3925 (21.43 €, apertura)
- 2026-10-02 03:50 [macd_momentum_regimen] ENTRADA SPX @ 0.3925 (22.00 €, apertura)
- 2026-10-02 03:50 [macd_momentum_evento] ENTRADA SPX @ 0.3925 (21.55 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
