# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 15:46 UTC · vueltas 42 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 913.94 € (-1.11%) | 30 | 10 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| reversion_bb | 923.86 € (-0.04%) | 2 | 2 | 50% | +0.000% | -1.100% | -1.219% | -0.51 € |
| ruptura_volumen | 905.25 € (-2.06%) | 50 | 1 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| rebote_extremo | 924.29 € (+0.01%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 912.34 € (-1.29%) | 33 | 1 | 18% | -0.461% | -1.561% | -1.697% | -11.86 € |
| macd_momentum | 911.33 € (-1.40%) | 51 | 7 | 27% | -0.074% | -1.086% | -1.228% | -12.77 € |
| estocastico_rebote | 914.21 € (-1.09%) | 40 | 34 | 30% | -0.441% | -1.421% | -1.598% | -13.11 € |
| ruptura_estricta | 902.84 € (-2.32%) | 38 | 2 | 11% | -1.302% | -2.402% | -2.549% | -21.08 € |
| macd_sin_salida | 908.09 € (-1.75%) | 48 | 8 | 29% | -0.413% | -1.451% | -1.596% | -16.07 € |
| c_banda_atr_tope | 922.79 € (-0.16%) | 8 | 5 | 50% | +0.252% | -0.849% | -1.012% | -1.57 € |
| ruptura_volumen_tope | 921.18 € (-0.33%) | 9 | 1 | 22% | -0.373% | -1.473% | -1.564% | -3.06 € |
| c_banda_atr_regimen | 913.78 € (-1.13%) | 30 | 4 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| macd_momentum_regimen | 912.12 € (-1.31%) | 49 | 0 | 29% | -0.039% | -1.072% | -1.211% | -12.12 € |
| ruptura_volumen_regimen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| c_banda_atr_evento | 924.39 € (+0.02%) | 0 | 7 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 921.90 € (-0.25%) | 4 | 7 | 0% | -1.276% | -2.376% | -2.562% | -2.19 € |
| ruptura_volumen_evento | 924.24 € (+0.00%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 15:45 | macd_sin_salida | XMR | timeout | -0.69% | -1.49% | -0.34 |
| 2026-09-30 15:45 | ruptura_estricta | WLFI | timeout | -1.20% | -2.30% | -0.53 |
| 2026-09-30 15:45 | pullback_tendencia | ASTER | rotura de tendencia | -0.46% | -1.56% | -0.36 |
| 2026-09-30 15:40 | macd_sin_salida | BNB | timeout | -0.69% | -1.49% | -0.34 |
| 2026-09-30 15:40 | ruptura_estricta | TRUMP | timeout | +0.05% | -1.05% | -0.24 |
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

## Eventos de la última vuelta

- 2026-09-30 15:40 [pullback_tendencia] ENTRADA HBAR @ 0.0951 (22.82 €, apertura)
- 2026-09-30 15:40 [ruptura_volumen] ENTRADA XDC @ 0.03039 (22.63 €, apertura)
- 2026-09-30 15:40 [ruptura_estricta] ENTRADA XDC @ 0.03039 (22.59 €, apertura)
- 2026-09-30 15:40 [ruptura_volumen_tope] ENTRADA XDC @ 0.03039 (23.03 €, apertura)
- 2026-09-30 15:40 [ruptura_volumen_evento] ENTRADA XDC @ 0.03039 (23.11 €, apertura)
- 2026-09-30 15:45 [pullback_tendencia] CIERRE ASTER rotura de tendencia bruto -0.46% neto -1.56%
- 2026-09-30 15:45 [ruptura_estricta] CIERRE WLFI timeout bruto -1.20% neto -2.30%
- 2026-09-30 15:45 [macd_sin_salida] CIERRE XMR timeout bruto -0.69% neto -1.49%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
