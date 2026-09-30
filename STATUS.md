# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 16:01 UTC · vueltas 45 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 915.22 € (-0.98%) | 30 | 12 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| reversion_bb | 924.19 € (-0.01%) | 2 | 2 | 50% | +0.000% | -1.100% | -1.219% | -0.51 € |
| ruptura_volumen | 905.43 € (-2.04%) | 50 | 2 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| rebote_extremo | 924.13 € (-0.01%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 912.41 € (-1.28%) | 33 | 1 | 18% | -0.461% | -1.561% | -1.697% | -11.86 € |
| macd_momentum | 912.07 € (-1.32%) | 52 | 10 | 27% | -0.089% | -1.091% | -1.231% | -13.08 € |
| estocastico_rebote | 916.66 € (-0.82%) | 46 | 28 | 37% | -0.178% | -1.135% | -1.310% | -12.04 € |
| ruptura_estricta | 902.91 € (-2.31%) | 38 | 2 | 11% | -1.302% | -2.402% | -2.549% | -21.08 € |
| macd_sin_salida | 908.96 € (-1.65%) | 48 | 12 | 29% | -0.413% | -1.451% | -1.596% | -16.07 € |
| c_banda_atr_tope | 923.71 € (-0.06%) | 8 | 5 | 50% | +0.252% | -0.849% | -1.012% | -1.57 € |
| ruptura_volumen_tope | 921.36 € (-0.31%) | 9 | 2 | 22% | -0.373% | -1.473% | -1.564% | -3.06 € |
| c_banda_atr_regimen | 914.07 € (-1.10%) | 30 | 6 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| macd_momentum_regimen | 912.10 € (-1.31%) | 49 | 4 | 29% | -0.039% | -1.072% | -1.211% | -12.12 € |
| ruptura_volumen_regimen | 904.97 € (-2.09%) | 51 | 1 | 16% | -0.638% | -1.650% | -1.799% | -19.38 € |
| c_banda_atr_evento | 925.58 € (+0.15%) | 0 | 9 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 922.51 € (-0.19%) | 5 | 10 | 0% | -1.191% | -2.291% | -2.449% | -2.65 € |
| ruptura_volumen_evento | 924.43 € (+0.02%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 15:55 | ruptura_volumen_regimen | XDC | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 15:55 | estocastico_rebote | USELESS | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-30 15:55 | estocastico_rebote | UNI | take-profit | +1.86% | +1.06% | +0.24 |
| 2026-09-30 15:50 | macd_momentum_evento | ASTER | momentum perdido | -0.85% | -1.95% | -0.45 |
| 2026-09-30 15:50 | estocastico_rebote | MINA | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-30 15:50 | estocastico_rebote | XDC | take-profit | +2.48% | +1.68% | +0.39 |
| 2026-09-30 15:50 | estocastico_rebote | TRX | timeout | -0.29% | -1.09% | -0.25 |
| 2026-09-30 15:50 | estocastico_rebote | SUI | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-30 15:50 | macd_momentum | ASTER | momentum perdido | -0.85% | -1.35% | -0.31 |
| 2026-09-30 15:45 | macd_sin_salida | XMR | timeout | -0.69% | -1.49% | -0.34 |
| 2026-09-30 15:45 | ruptura_estricta | WLFI | timeout | -1.20% | -2.30% | -0.53 |
| 2026-09-30 15:45 | pullback_tendencia | ASTER | rotura de tendencia | -0.46% | -1.56% | -0.36 |
| 2026-09-30 15:40 | macd_sin_salida | BNB | timeout | -0.69% | -1.49% | -0.34 |
| 2026-09-30 15:40 | ruptura_estricta | TRUMP | timeout | +0.05% | -1.05% | -0.24 |
| 2026-09-30 15:35 | macd_sin_salida | WLFI | timeout | -1.00% | -1.80% | -0.42 |

## Eventos de la última vuelta

- 2026-09-30 15:55 [c_banda_atr] ENTRADA ONDO @ 0.44205 (22.86 €, apertura)
- 2026-09-30 15:55 [c_banda_atr_regimen] ENTRADA ONDO @ 0.44205 (22.86 €, apertura)
- 2026-09-30 15:55 [c_banda_atr_evento] ENTRADA ONDO @ 0.44205 (23.11 €, apertura)
- 2026-09-30 15:55 [macd_momentum] ENTRADA VVV @ 24.725 (22.78 €, apertura)
- 2026-09-30 15:55 [macd_sin_salida] ENTRADA VVV @ 24.725 (22.70 €, apertura)
- 2026-09-30 15:55 [macd_momentum_regimen] ENTRADA VVV @ 24.725 (22.80 €, apertura)
- 2026-09-30 15:55 [macd_momentum_evento] ENTRADA VVV @ 24.725 (23.04 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
