# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 15:31 UTC · vueltas 39 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 913.26 € (-1.19%) | 30 | 7 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| reversion_bb | 923.49 € (-0.08%) | 2 | 2 | 50% | +0.000% | -1.100% | -1.219% | -0.51 € |
| ruptura_volumen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| rebote_extremo | 924.05 € (-0.02%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 912.63 € (-1.26%) | 32 | 1 | 19% | -0.461% | -1.561% | -1.699% | -11.51 € |
| macd_momentum | 910.97 € (-1.44%) | 51 | 4 | 27% | -0.074% | -1.086% | -1.228% | -12.77 € |
| estocastico_rebote | 910.11 € (-1.53%) | 38 | 30 | 29% | -0.494% | -1.483% | -1.662% | -12.99 € |
| ruptura_estricta | 903.69 € (-2.22%) | 33 | 6 | 12% | -1.393% | -2.493% | -2.651% | -19.00 € |
| macd_sin_salida | 907.94 € (-1.76%) | 44 | 10 | 32% | -0.389% | -1.448% | -1.597% | -14.71 € |
| c_banda_atr_tope | 922.36 € (-0.20%) | 8 | 3 | 50% | +0.252% | -0.849% | -1.012% | -1.57 € |
| ruptura_volumen_tope | 921.18 € (-0.33%) | 9 | 0 | 22% | -0.373% | -1.473% | -1.564% | -3.06 € |
| c_banda_atr_regimen | 913.56 € (-1.16%) | 30 | 4 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| macd_momentum_regimen | 912.12 € (-1.31%) | 49 | 0 | 29% | -0.039% | -1.072% | -1.211% | -12.12 € |
| ruptura_volumen_regimen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| c_banda_atr_evento | 923.93 € (-0.03%) | 0 | 3 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 921.54 € (-0.29%) | 4 | 4 | 0% | -1.276% | -2.376% | -2.562% | -2.19 € |
| ruptura_volumen_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 15:30 | macd_momentum_evento | MINA | stop-loss | -1.62% | -2.72% | -0.63 |
| 2026-09-30 15:30 | macd_sin_salida | MINA | stop-loss | -1.62% | -2.12% | -0.48 |
| 2026-09-30 15:30 | macd_sin_salida | ETH | timeout | -1.08% | -1.88% | -0.43 |
| 2026-09-30 15:30 | ruptura_estricta | SHIB | stop-loss | -2.06% | -3.16% | -0.73 |
| 2026-09-30 15:30 | estocastico_rebote | ALGO | stop-loss | -1.72% | -2.52% | -0.58 |
| 2026-09-30 15:30 | estocastico_rebote | POL | stop-loss | -1.66% | -2.46% | -0.56 |
| 2026-09-30 15:30 | estocastico_rebote | NEAR | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 15:30 | macd_momentum | MINA | stop-loss | -1.62% | -2.12% | -0.48 |
| 2026-09-30 15:25 | macd_momentum_evento | SPX | momentum perdido | -0.23% | -1.33% | -0.31 |
| 2026-09-30 15:25 | estocastico_rebote | XMR | timeout | -0.57% | -1.37% | -0.32 |
| 2026-09-30 15:25 | macd_momentum | SPX | momentum perdido | -0.23% | -0.73% | -0.17 |
| 2026-09-30 15:25 | pullback_tendencia | HBAR | rotura de tendencia | -0.04% | -1.14% | -0.26 |
| 2026-09-30 15:20 | estocastico_rebote | NIGHT | stop-loss | -1.61% | -2.42% | -0.56 |
| 2026-09-30 15:20 | estocastico_rebote | WLD | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 15:20 | estocastico_rebote | ENA | stop-loss | -1.50% | -2.00% | -0.46 |

## Eventos de la última vuelta

- 2026-09-30 15:30 [macd_sin_salida] CIERRE ETH timeout bruto -1.08% neto -1.88%
- 2026-09-30 15:30 [estocastico_rebote] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 15:30 [estocastico_rebote] CIERRE POL stop-loss bruto -1.66% neto -2.46%
- 2026-09-30 15:30 [estocastico_rebote] CIERRE ALGO stop-loss bruto -1.72% neto -2.52%
- 2026-09-30 15:30 [macd_momentum] CIERRE MINA stop-loss bruto -1.62% neto -2.12%
- 2026-09-30 15:30 [macd_sin_salida] CIERRE MINA stop-loss bruto -1.62% neto -2.12%
- 2026-09-30 15:30 [macd_momentum_evento] CIERRE MINA stop-loss bruto -1.62% neto -2.72%
- 2026-09-30 15:30 [ruptura_estricta] CIERRE SHIB stop-loss bruto -2.06% neto -3.16%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
