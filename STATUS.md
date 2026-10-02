# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 07:01 UTC · vueltas 373 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.06 € (-3.70%) | 330 | 18 | 39% | +0.130% | -0.449% | -0.570% | -33.81 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 863.05 € (-6.62%) | 404 | 9 | 27% | -0.110% | -0.675% | -0.782% | -61.12 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 890.98 € (-3.60%) | 223 | 14 | 20% | -0.042% | -0.660% | -0.746% | -33.46 € |
| macd_momentum | 854.40 € (-7.56%) | 633 | 9 | 22% | +0.044% | -0.497% | -0.598% | -70.11 € |
| estocastico_rebote | 879.33 € (-4.86%) | 382 | 33 | 36% | +0.045% | -0.523% | -0.632% | -45.33 € |
| ruptura_estricta | 886.45 € (-4.09%) | 210 | 24 | 34% | -0.168% | -0.793% | -0.908% | -38.01 € |
| macd_sin_salida | 881.75 € (-4.60%) | 415 | 29 | 40% | +0.115% | -0.448% | -0.559% | -42.42 € |
| c_banda_atr_tope | 913.44 € (-1.17%) | 75 | 4 | 37% | +0.236% | -0.616% | -0.732% | -10.63 € |
| ruptura_volumen_tope | 902.28 € (-2.38%) | 122 | 5 | 25% | -0.066% | -0.783% | -0.895% | -21.84 € |
| c_banda_atr_regimen | 902.49 € (-2.35%) | 183 | 18 | 40% | +0.149% | -0.494% | -0.624% | -20.82 € |
| macd_momentum_regimen | 877.28 € (-5.08%) | 396 | 9 | 22% | +0.038% | -0.528% | -0.631% | -47.22 € |
| ruptura_volumen_regimen | 867.74 € (-6.11%) | 327 | 9 | 24% | -0.188% | -0.768% | -0.880% | -56.44 € |
| c_banda_atr_evento | 895.98 € (-3.06%) | 297 | 18 | 40% | +0.179% | -0.410% | -0.527% | -27.88 € |
| macd_momentum_evento | 859.13 € (-7.04%) | 586 | 9 | 21% | +0.045% | -0.500% | -0.598% | -65.38 € |
| ruptura_volumen_evento | 875.33 € (-5.29%) | 354 | 9 | 28% | -0.037% | -0.612% | -0.713% | -48.83 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 07:00 | ruptura_volumen_evento | SPX | timeout | -0.23% | -0.72% | -0.16 |
| 2026-10-02 07:00 | ruptura_volumen_evento | WLD | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:00 | macd_momentum_evento | SHIB | momentum perdido | -0.17% | -0.67% | -0.14 |
| 2026-10-02 07:00 | macd_momentum_evento | FET | momentum perdido | -0.47% | -0.97% | -0.21 |
| 2026-10-02 07:00 | macd_momentum_evento | PUMP | momentum perdido | -0.63% | -1.13% | -0.24 |
| 2026-10-02 07:00 | ruptura_volumen_regimen | SPX | timeout | -0.23% | -0.72% | -0.16 |
| 2026-10-02 07:00 | ruptura_volumen_regimen | WLD | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:00 | macd_momentum_regimen | SHIB | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-10-02 07:00 | macd_momentum_regimen | FET | momentum perdido | -0.47% | -0.97% | -0.21 |
| 2026-10-02 07:00 | macd_momentum_regimen | PUMP | momentum perdido | -0.63% | -1.13% | -0.25 |
| 2026-10-02 07:00 | ruptura_estricta | TON | timeout | -1.50% | -2.00% | -0.44 |
| 2026-10-02 07:00 | macd_momentum | SHIB | momentum perdido | -0.17% | -0.67% | -0.14 |
| 2026-10-02 07:00 | macd_momentum | FET | momentum perdido | -0.47% | -0.97% | -0.21 |
| 2026-10-02 07:00 | macd_momentum | PUMP | momentum perdido | -0.63% | -1.13% | -0.24 |
| 2026-10-02 07:00 | pullback_tendencia | HBAR | rotura de tendencia | +0.42% | -0.08% | -0.02 |

## Eventos de la última vuelta

- 2026-10-02 07:00 [pullback_tendencia] CIERRE HBAR rotura de tendencia bruto +0.42% neto -0.08%
- 2026-10-02 07:00 [macd_momentum] CIERRE PUMP momentum perdido bruto -0.63% neto -1.13%
- 2026-10-02 07:00 [macd_momentum_regimen] CIERRE PUMP momentum perdido bruto -0.63% neto -1.13%
- 2026-10-02 07:00 [macd_momentum_evento] CIERRE PUMP momentum perdido bruto -0.63% neto -1.13%
- 2026-10-02 07:00 [macd_momentum] CIERRE FET momentum perdido bruto -0.47% neto -0.97%
- 2026-10-02 07:00 [macd_momentum_regimen] CIERRE FET momentum perdido bruto -0.47% neto -0.97%
- 2026-10-02 07:00 [macd_momentum_evento] CIERRE FET momentum perdido bruto -0.47% neto -0.97%
- 2026-10-02 06:55 [ruptura_volumen] ENTRADA ALGO @ 0.11522 (21.59 €, apertura)
- 2026-10-02 06:55 [macd_momentum] ENTRADA ALGO @ 0.11522 (21.36 €, apertura)
- 2026-10-02 06:55 [macd_momentum_regimen] ENTRADA ALGO @ 0.11522 (21.93 €, apertura)
- 2026-10-02 06:55 [ruptura_volumen_regimen] ENTRADA ALGO @ 0.11522 (21.71 €, apertura)
- 2026-10-02 06:55 [macd_momentum_evento] ENTRADA ALGO @ 0.11522 (21.48 €, apertura)
- 2026-10-02 06:55 [ruptura_volumen_evento] ENTRADA ALGO @ 0.11522 (21.90 €, apertura)
- 2026-10-02 07:00 [ruptura_volumen] CIERRE WLD stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:00 [ruptura_volumen_regimen] CIERRE WLD stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:00 [ruptura_volumen_evento] CIERRE WLD stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 07:00 [macd_momentum] CIERRE SHIB momentum perdido bruto -0.17% neto -0.67%
- 2026-10-02 07:00 [macd_momentum_regimen] CIERRE SHIB momentum perdido bruto -0.17% neto -0.67%
- 2026-10-02 07:00 [macd_momentum_evento] CIERRE SHIB momentum perdido bruto -0.17% neto -0.67%
- 2026-10-02 07:00 [ruptura_estricta] CIERRE TON timeout bruto -1.50% neto -2.00%
- 2026-10-02 07:00 [ruptura_volumen] CIERRE SPX timeout bruto -0.22% neto -0.72%
- 2026-10-02 07:00 [ruptura_volumen_regimen] CIERRE SPX timeout bruto -0.22% neto -0.72%
- 2026-10-02 07:00 [ruptura_volumen_evento] CIERRE SPX timeout bruto -0.22% neto -0.72%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
