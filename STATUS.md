# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 10:26 UTC · vueltas 195 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 896.14 € (-3.04%) | 173 | 7 | 35% | -0.044% | -0.695% | -0.817% | -27.51 € |
| reversion_bb | 918.23 € (-0.65%) | 24 | 9 | 38% | +0.050% | -1.050% | -1.157% | -5.81 € |
| ruptura_volumen | 884.47 € (-4.30%) | 210 | 5 | 23% | -0.205% | -0.829% | -0.939% | -39.55 € |
| rebote_extremo | 922.70 € (-0.17%) | 6 | 3 | 50% | +0.099% | -1.001% | -1.154% | -1.39 € |
| pullback_tendencia | 896.88 € (-2.96%) | 124 | 2 | 15% | -0.255% | -0.968% | -1.073% | -27.39 € |
| macd_momentum | 884.30 € (-4.32%) | 300 | 0 | 22% | -0.000% | -0.587% | -0.696% | -39.94 € |
| estocastico_rebote | 880.88 € (-4.69%) | 235 | 28 | 32% | -0.172% | -0.783% | -0.897% | -41.73 € |
| ruptura_estricta | 890.47 € (-3.65%) | 122 | 2 | 25% | -0.486% | -1.202% | -1.328% | -33.55 € |
| macd_sin_salida | 887.89 € (-3.93%) | 221 | 4 | 36% | -0.096% | -0.714% | -0.829% | -36.03 € |
| c_banda_atr_tope | 913.22 € (-1.19%) | 41 | 1 | 27% | -0.052% | -1.152% | -1.266% | -10.86 € |
| ruptura_volumen_tope | 911.75 € (-1.35%) | 62 | 3 | 27% | +0.067% | -0.859% | -0.976% | -12.25 € |
| c_banda_atr_regimen | 902.68 € (-2.33%) | 108 | 1 | 34% | -0.118% | -0.859% | -1.000% | -21.32 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 902.10 € (-2.40%) | 140 | 7 | 36% | +0.019% | -0.670% | -0.783% | -21.53 € |
| macd_momentum_evento | 889.20 € (-3.79%) | 253 | 0 | 19% | -0.006% | -0.610% | -0.713% | -35.04 € |
| ruptura_volumen_evento | 897.05 € (-2.94%) | 160 | 5 | 24% | -0.073% | -0.738% | -0.836% | -26.95 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 10:25 | reversion_bb | FET | take-profit | +1.50% | +0.40% | +0.09 |
| 2026-10-01 10:20 | macd_momentum_evento | MINA | momentum perdido | -0.39% | -0.89% | -0.20 |
| 2026-10-01 10:20 | macd_sin_salida | XMR | timeout | -1.01% | -1.51% | -0.34 |
| 2026-10-01 10:20 | ruptura_estricta | XMR | timeout | -1.01% | -1.51% | -0.34 |
| 2026-10-01 10:20 | estocastico_rebote | MON | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 10:20 | estocastico_rebote | QNT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 10:20 | macd_momentum | MINA | momentum perdido | -0.39% | -0.89% | -0.20 |
| 2026-10-01 10:15 | estocastico_rebote | BNB | timeout | +0.03% | -0.47% | -0.11 |
| 2026-10-01 10:10 | ruptura_volumen_evento | VVV | stop-loss | -1.66% | -2.16% | -0.48 |
| 2026-10-01 10:10 | ruptura_volumen_evento | MINA | stop-loss | -1.22% | -1.72% | -0.39 |
| 2026-10-01 10:10 | macd_momentum_evento | BCH | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-10-01 10:10 | macd_momentum_evento | HYPE | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-10-01 10:10 | c_banda_atr_evento | APT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 10:10 | c_banda_atr_evento | FIL | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 10:10 | c_banda_atr_evento | CRV | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-10-01 10:20 [pullback_tendencia] ENTRADA BTC @ 74132.2 (22.42 €, apertura)
- 2026-10-01 10:20 [estocastico_rebote] ENTRADA UNI @ 7.9476 (22.06 €, apertura)
- 2026-10-01 10:25 [reversion_bb] CIERRE FET take-profit bruto +1.50% neto +0.40%
- 2026-10-01 10:20 [estocastico_rebote] ENTRADA FET @ 0.2045 (22.06 €, apertura)
- 2026-10-01 10:20 [estocastico_rebote] ENTRADA ALGO @ 0.11241 (22.06 €, apertura)
- 2026-10-01 10:20 [estocastico_rebote] ENTRADA INJ @ 6.573 (22.06 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
