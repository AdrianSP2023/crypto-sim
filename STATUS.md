# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 15:36 UTC · vueltas 40 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 914.17 € (-1.09%) | 30 | 7 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| reversion_bb | 923.71 € (-0.06%) | 2 | 2 | 50% | +0.000% | -1.100% | -1.219% | -0.51 € |
| ruptura_volumen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| rebote_extremo | 924.16 € (-0.01%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 912.90 € (-1.23%) | 32 | 1 | 19% | -0.461% | -1.561% | -1.699% | -11.51 € |
| macd_momentum | 911.57 € (-1.37%) | 51 | 4 | 27% | -0.074% | -1.086% | -1.228% | -12.77 € |
| estocastico_rebote | 914.77 € (-1.02%) | 40 | 28 | 30% | -0.441% | -1.421% | -1.598% | -13.11 € |
| ruptura_estricta | 903.33 € (-2.26%) | 36 | 3 | 11% | -1.343% | -2.443% | -2.591% | -20.31 € |
| macd_sin_salida | 908.68 € (-1.68%) | 46 | 8 | 30% | -0.401% | -1.449% | -1.596% | -15.38 € |
| c_banda_atr_tope | 923.00 € (-0.13%) | 8 | 3 | 50% | +0.252% | -0.849% | -1.012% | -1.57 € |
| ruptura_volumen_tope | 921.18 € (-0.33%) | 9 | 0 | 22% | -0.373% | -1.473% | -1.564% | -3.06 € |
| c_banda_atr_regimen | 913.84 € (-1.13%) | 30 | 4 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| macd_momentum_regimen | 912.12 € (-1.31%) | 49 | 0 | 29% | -0.039% | -1.072% | -1.211% | -12.12 € |
| ruptura_volumen_regimen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| c_banda_atr_evento | 924.57 € (+0.04%) | 0 | 3 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 922.15 € (-0.23%) | 4 | 4 | 0% | -1.276% | -2.376% | -2.562% | -2.19 € |
| ruptura_volumen_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 15:35 | macd_sin_salida | WLFI | timeout | -1.00% | -1.80% | -0.42 |
| 2026-09-30 15:35 | macd_sin_salida | BTC | timeout | -0.32% | -1.12% | -0.26 |
| 2026-09-30 15:35 | ruptura_estricta | BNB | timeout | -0.73% | -1.83% | -0.42 |
| 2026-09-30 15:35 | ruptura_estricta | ETH | timeout | -1.31% | -2.41% | -0.56 |
| 2026-09-30 15:35 | ruptura_estricta | BTC | timeout | -0.32% | -1.42% | -0.33 |
| 2026-09-30 15:35 | estocastico_rebote | TRUMP | timeout | +0.00% | -0.80% | -0.18 |
| 2026-09-30 15:35 | estocastico_rebote | KSM | timeout | +1.12% | +0.32% | +0.07 |
| 2026-09-30 15:30 | macd_momentum_evento | MINA | stop-loss | -1.62% | -2.72% | -0.63 |
| 2026-09-30 15:30 | macd_sin_salida | MINA | stop-loss | -1.62% | -2.12% | -0.48 |
| 2026-09-30 15:30 | macd_sin_salida | ETH | timeout | -1.08% | -1.88% | -0.43 |
| 2026-09-30 15:30 | ruptura_estricta | SHIB | stop-loss | -2.06% | -3.16% | -0.73 |
| 2026-09-30 15:30 | estocastico_rebote | ALGO | stop-loss | -1.72% | -2.52% | -0.58 |
| 2026-09-30 15:30 | estocastico_rebote | POL | stop-loss | -1.66% | -2.46% | -0.56 |
| 2026-09-30 15:30 | estocastico_rebote | NEAR | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-30 15:30 | macd_momentum | MINA | stop-loss | -1.62% | -2.12% | -0.48 |

## Eventos de la última vuelta

- 2026-09-30 15:35 [ruptura_estricta] CIERRE BTC timeout bruto -0.32% neto -1.42%
- 2026-09-30 15:35 [macd_sin_salida] CIERRE BTC timeout bruto -0.32% neto -1.12%
- 2026-09-30 15:35 [ruptura_estricta] CIERRE ETH timeout bruto -1.31% neto -2.41%
- 2026-09-30 15:35 [macd_sin_salida] CIERRE WLFI timeout bruto -1.00% neto -1.80%
- 2026-09-30 15:35 [estocastico_rebote] CIERRE KSM timeout bruto +1.12% neto +0.32%
- 2026-09-30 15:35 [estocastico_rebote] CIERRE TRUMP timeout bruto +0.00% neto -0.80%
- 2026-09-30 15:35 [ruptura_estricta] CIERRE BNB timeout bruto -0.73% neto -1.83%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
