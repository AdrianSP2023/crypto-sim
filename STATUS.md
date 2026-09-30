# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 15:51 UTC · vueltas 43 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 914.40 € (-1.06%) | 30 | 10 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| reversion_bb | 923.92 € (-0.03%) | 2 | 2 | 50% | +0.000% | -1.100% | -1.219% | -0.51 € |
| ruptura_volumen | 905.44 € (-2.03%) | 50 | 1 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| rebote_extremo | 924.11 € (-0.01%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 912.49 € (-1.27%) | 33 | 1 | 18% | -0.461% | -1.561% | -1.697% | -11.86 € |
| macd_momentum | 911.87 € (-1.34%) | 52 | 6 | 27% | -0.089% | -1.091% | -1.231% | -13.08 € |
| estocastico_rebote | 916.02 € (-0.89%) | 44 | 30 | 34% | -0.270% | -1.233% | -1.406% | -12.51 € |
| ruptura_estricta | 903.03 € (-2.29%) | 38 | 2 | 11% | -1.302% | -2.402% | -2.549% | -21.08 € |
| macd_sin_salida | 908.77 € (-1.67%) | 48 | 8 | 29% | -0.413% | -1.451% | -1.596% | -16.07 € |
| c_banda_atr_tope | 923.02 € (-0.13%) | 8 | 5 | 50% | +0.252% | -0.849% | -1.012% | -1.57 € |
| ruptura_volumen_tope | 921.37 € (-0.31%) | 9 | 1 | 22% | -0.373% | -1.473% | -1.564% | -3.06 € |
| c_banda_atr_regimen | 913.89 € (-1.12%) | 30 | 4 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| macd_momentum_regimen | 912.12 € (-1.31%) | 49 | 0 | 29% | -0.039% | -1.072% | -1.211% | -12.12 € |
| ruptura_volumen_regimen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| c_banda_atr_evento | 924.80 € (+0.06%) | 0 | 7 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 922.32 € (-0.21%) | 5 | 6 | 0% | -1.191% | -2.291% | -2.449% | -2.65 € |
| ruptura_volumen_evento | 924.44 € (+0.02%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-30 15:35 | macd_sin_salida | BTC | timeout | -0.32% | -1.12% | -0.26 |
| 2026-09-30 15:35 | ruptura_estricta | BNB | timeout | -0.73% | -1.83% | -0.42 |
| 2026-09-30 15:35 | ruptura_estricta | ETH | timeout | -1.31% | -2.41% | -0.56 |

## Eventos de la última vuelta

- 2026-09-30 15:50 [estocastico_rebote] CIERRE SUI take-profit bruto +1.80% neto +1.00%
- 2026-09-30 15:50 [estocastico_rebote] CIERRE TRX timeout bruto -0.29% neto -1.09%
- 2026-09-30 15:50 [estocastico_rebote] CIERRE XDC take-profit bruto +2.48% neto +1.68%
- 2026-09-30 15:50 [estocastico_rebote] CIERRE MINA take-profit bruto +1.80% neto +1.00%
- 2026-09-30 15:50 [macd_momentum] CIERRE ASTER momentum perdido bruto -0.85% neto -1.35%
- 2026-09-30 15:50 [macd_momentum_evento] CIERRE ASTER momentum perdido bruto -0.85% neto -1.95%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
