# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 07:56 UTC · vueltas 165 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.17 € (-2.71%) | 158 | 10 | 37% | +0.014% | -0.652% | -0.775% | -23.62 € |
| reversion_bb | 919.46 € (-0.52%) | 20 | 9 | 40% | +0.134% | -0.966% | -1.078% | -4.46 € |
| ruptura_volumen | 885.72 € (-4.17%) | 204 | 0 | 23% | -0.203% | -0.831% | -0.940% | -38.53 € |
| rebote_extremo | 924.20 € (-0.00%) | 3 | 3 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 898.13 € (-2.83%) | 119 | 1 | 16% | -0.244% | -0.965% | -1.071% | -26.23 € |
| macd_momentum | 885.11 € (-4.23%) | 288 | 2 | 22% | -0.006% | -0.597% | -0.704% | -39.00 € |
| estocastico_rebote | 887.85 € (-3.94%) | 205 | 36 | 34% | -0.084% | -0.711% | -0.829% | -33.31 € |
| ruptura_estricta | 892.27 € (-3.46%) | 114 | 8 | 27% | -0.430% | -1.161% | -1.287% | -30.34 € |
| macd_sin_salida | 889.94 € (-3.71%) | 207 | 9 | 37% | -0.068% | -0.694% | -0.807% | -32.84 € |
| c_banda_atr_tope | 914.75 € (-1.03%) | 35 | 2 | 26% | -0.052% | -1.152% | -1.273% | -9.28 € |
| ruptura_volumen_tope | 912.66 € (-1.25%) | 57 | 0 | 28% | +0.080% | -0.884% | -0.999% | -11.58 € |
| c_banda_atr_regimen | 903.62 € (-2.23%) | 103 | 6 | 36% | -0.077% | -0.831% | -0.972% | -19.68 € |
| macd_momentum_regimen | 894.23 € (-3.25%) | 202 | 1 | 22% | -0.022% | -0.652% | -0.763% | -30.01 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 905.15 € (-2.07%) | 125 | 10 | 38% | +0.099% | -0.612% | -0.727% | -17.62 € |
| macd_momentum_evento | 890.02 € (-3.70%) | 241 | 2 | 19% | -0.013% | -0.623% | -0.724% | -34.09 € |
| ruptura_volumen_evento | 898.32 € (-2.80%) | 154 | 0 | 24% | -0.065% | -0.736% | -0.833% | -25.91 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 07:55 | ruptura_volumen_evento | BTC | timeout | -0.85% | -1.35% | -0.30 |
| 2026-10-01 07:55 | ruptura_volumen_regimen | BTC | timeout | -0.85% | -1.35% | -0.30 |
| 2026-10-01 07:55 | macd_sin_salida | SEI | timeout | -0.90% | -1.40% | -0.32 |
| 2026-10-01 07:55 | macd_sin_salida | LTC | timeout | -0.75% | -1.25% | -0.28 |
| 2026-10-01 07:55 | ruptura_estricta | VVV | timeout | +0.38% | -0.12% | -0.03 |
| 2026-10-01 07:55 | ruptura_volumen | BTC | timeout | -0.85% | -1.35% | -0.30 |
| 2026-10-01 07:50 | ruptura_volumen_evento | ASTER | timeout | -0.38% | -0.88% | -0.20 |
| 2026-10-01 07:50 | ruptura_volumen_regimen | ASTER | timeout | -0.38% | -0.88% | -0.20 |
| 2026-10-01 07:50 | ruptura_volumen_tope | ASTER | timeout | -0.38% | -0.88% | -0.20 |
| 2026-10-01 07:50 | ruptura_estricta | BCH | timeout | -0.77% | -1.27% | -0.28 |
| 2026-10-01 07:50 | ruptura_estricta | HBAR | timeout | -0.73% | -1.23% | -0.28 |
| 2026-10-01 07:50 | estocastico_rebote | SKY | timeout | -0.58% | -1.08% | -0.24 |
| 2026-10-01 07:50 | estocastico_rebote | ALGO | timeout | -0.72% | -1.22% | -0.28 |
| 2026-10-01 07:50 | estocastico_rebote | ENA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 07:50 | estocastico_rebote | PUMP | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-10-01 07:55 [ruptura_volumen] CIERRE BTC timeout bruto -0.85% neto -1.35%
- 2026-10-01 07:55 [ruptura_volumen_regimen] CIERRE BTC timeout bruto -0.85% neto -1.35%
- 2026-10-01 07:55 [ruptura_volumen_evento] CIERRE BTC timeout bruto -0.85% neto -1.35%
- 2026-10-01 07:50 [c_banda_atr] ENTRADA QNT @ 265.11 (22.52 €, apertura)
- 2026-10-01 07:50 [macd_momentum] ENTRADA QNT @ 265.11 (22.13 €, apertura)
- 2026-10-01 07:50 [macd_sin_salida] ENTRADA QNT @ 265.11 (22.30 €, apertura)
- 2026-10-01 07:50 [c_banda_atr_tope] ENTRADA QNT @ 265.11 (22.87 €, apertura)
- 2026-10-01 07:50 [c_banda_atr_evento] ENTRADA QNT @ 265.11 (22.67 €, apertura)
- 2026-10-01 07:50 [macd_momentum_evento] ENTRADA QNT @ 265.11 (22.25 €, apertura)
- 2026-10-01 07:55 [macd_sin_salida] CIERRE LTC timeout bruto -0.75% neto -1.25%
- 2026-10-01 07:55 [ruptura_estricta] CIERRE VVV timeout bruto +0.38% neto -0.12%
- 2026-10-01 07:55 [macd_sin_salida] CIERRE SEI timeout bruto -0.90% neto -1.40%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
