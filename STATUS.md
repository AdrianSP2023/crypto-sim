# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 09:31 UTC · vueltas 403 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.43 € (-3.77%) | 341 | 23 | 40% | +0.136% | -0.441% | -0.561% | -34.27 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 860.35 € (-6.91%) | 423 | 22 | 27% | -0.097% | -0.659% | -0.769% | -62.45 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.47 € (-3.76%) | 244 | 8 | 20% | -0.028% | -0.636% | -0.723% | -35.23 € |
| macd_momentum | 851.61 € (-7.86%) | 686 | 11 | 23% | +0.061% | -0.477% | -0.578% | -72.74 € |
| estocastico_rebote | 879.87 € (-4.80%) | 416 | 25 | 37% | +0.088% | -0.475% | -0.582% | -44.80 € |
| ruptura_estricta | 882.05 € (-4.57%) | 237 | 8 | 32% | -0.154% | -0.765% | -0.882% | -41.27 € |
| macd_sin_salida | 879.38 € (-4.85%) | 443 | 35 | 40% | +0.105% | -0.454% | -0.565% | -45.75 € |
| c_banda_atr_tope | 913.32 € (-1.18%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 900.60 € (-2.56%) | 128 | 5 | 24% | -0.088% | -0.794% | -0.908% | -23.22 € |
| c_banda_atr_regimen | 902.05 € (-2.40%) | 193 | 23 | 40% | +0.146% | -0.489% | -0.617% | -21.72 € |
| macd_momentum_regimen | 874.41 € (-5.39%) | 449 | 11 | 24% | +0.065% | -0.493% | -0.596% | -49.92 € |
| ruptura_volumen_regimen | 865.02 € (-6.41%) | 346 | 22 | 25% | -0.168% | -0.743% | -0.858% | -57.77 € |
| c_banda_atr_evento | 895.35 € (-3.13%) | 308 | 23 | 41% | +0.183% | -0.402% | -0.518% | -28.35 € |
| macd_momentum_evento | 856.32 € (-7.35%) | 639 | 11 | 23% | +0.064% | -0.478% | -0.576% | -68.02 € |
| ruptura_volumen_evento | 872.60 € (-5.59%) | 373 | 22 | 28% | -0.027% | -0.597% | -0.701% | -50.18 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 09:30 | ruptura_volumen_evento | PEPE | stop-loss | -1.22% | -1.72% | -0.38 |
| 2026-10-02 09:30 | macd_momentum_evento | KAS | momentum perdido | +0.74% | +0.24% | +0.05 |
| 2026-10-02 09:30 | ruptura_volumen_regimen | PEPE | stop-loss | -1.22% | -1.72% | -0.37 |
| 2026-10-02 09:30 | macd_momentum_regimen | KAS | momentum perdido | +0.74% | +0.24% | +0.05 |
| 2026-10-02 09:30 | macd_sin_salida | ONDO | timeout | -0.68% | -1.18% | -0.26 |
| 2026-10-02 09:30 | macd_sin_salida | FET | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 09:30 | macd_momentum | KAS | momentum perdido | +0.74% | +0.24% | +0.05 |
| 2026-10-02 09:30 | pullback_tendencia | DOT | timeout | -0.27% | -0.77% | -0.17 |
| 2026-10-02 09:30 | pullback_tendencia | LTC | rotura de tendencia | -0.53% | -1.03% | -0.23 |
| 2026-10-02 09:30 | ruptura_volumen | PEPE | stop-loss | -1.22% | -1.72% | -0.37 |
| 2026-10-02 09:25 | macd_momentum_evento | MON | stop-loss | -1.50% | -2.00% | -0.43 |
| 2026-10-02 09:25 | c_banda_atr_evento | ENA | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-10-02 09:25 | macd_momentum_regimen | MON | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 09:25 | c_banda_atr_regimen | ENA | stop-loss | -1.63% | -2.13% | -0.48 |
| 2026-10-02 09:25 | macd_sin_salida | MON | stop-loss | -1.50% | -2.00% | -0.44 |

## Eventos de la última vuelta

- 2026-10-02 09:25 [pullback_tendencia] ENTRADA AVAX @ 9.861 (22.24 €, apertura)
- 2026-10-02 09:25 [macd_momentum] ENTRADA AAVE @ 162.04 (21.29 €, apertura)
- 2026-10-02 09:25 [macd_sin_salida] ENTRADA AAVE @ 162.04 (21.98 €, apertura)
- 2026-10-02 09:25 [macd_momentum_regimen] ENTRADA AAVE @ 162.04 (21.86 €, apertura)
- 2026-10-02 09:25 [macd_momentum_evento] ENTRADA AAVE @ 162.04 (21.40 €, apertura)
- 2026-10-02 09:30 [pullback_tendencia] CIERRE LTC rotura de tendencia bruto -0.53% neto -1.03%
- 2026-10-02 09:30 [pullback_tendencia] CIERRE DOT timeout bruto -0.27% neto -0.77%
- 2026-10-02 09:25 [estocastico_rebote] ENTRADA DOT @ 1.0846 (21.99 €, apertura)
- 2026-10-02 09:25 [macd_momentum] ENTRADA ICP @ 2.925 (21.29 €, apertura)
- 2026-10-02 09:25 [macd_momentum_regimen] ENTRADA ICP @ 2.925 (21.86 €, apertura)
- 2026-10-02 09:25 [macd_momentum_evento] ENTRADA ICP @ 2.925 (21.40 €, apertura)
- 2026-10-02 09:30 [macd_sin_salida] CIERRE FET stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 09:30 [macd_sin_salida] CIERRE ONDO timeout bruto -0.68% neto -1.18%
- 2026-10-02 09:25 [macd_momentum] ENTRADA WLD @ 0.4783 (21.29 €, apertura)
- 2026-10-02 09:25 [macd_sin_salida] ENTRADA WLD @ 0.4783 (21.96 €, apertura)
- 2026-10-02 09:25 [macd_momentum_regimen] ENTRADA WLD @ 0.4783 (21.86 €, apertura)
- 2026-10-02 09:25 [macd_momentum_evento] ENTRADA WLD @ 0.4783 (21.40 €, apertura)
- 2026-10-02 09:30 [ruptura_volumen] CIERRE PEPE stop-loss bruto -1.22% neto -1.72%
- 2026-10-02 09:30 [ruptura_volumen_regimen] CIERRE PEPE stop-loss bruto -1.22% neto -1.72%
- 2026-10-02 09:30 [ruptura_volumen_evento] CIERRE PEPE stop-loss bruto -1.22% neto -1.72%
- 2026-10-02 09:30 [macd_momentum] CIERRE KAS momentum perdido bruto +0.74% neto +0.24%
- 2026-10-02 09:30 [macd_momentum_regimen] CIERRE KAS momentum perdido bruto +0.74% neto +0.24%
- 2026-10-02 09:30 [macd_momentum_evento] CIERRE KAS momentum perdido bruto +0.74% neto +0.24%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
