# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 01:56 UTC · vueltas 170 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.78 € (-2.21%) | 95 | 24 | 29% | -0.278% | -1.052% | -1.198% | -22.95 € |
| reversion_bb | 919.85 € (-0.48%) | 26 | 8 | 50% | +0.198% | -0.902% | -1.006% | -5.42 € |
| ruptura_volumen | 900.26 € (-2.59%) | 124 | 19 | 23% | -0.141% | -0.852% | -0.977% | -24.16 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.12 € (-1.96%) | 97 | 4 | 26% | -0.049% | -0.818% | -0.947% | -18.20 € |
| macd_momentum | 886.39 € (-4.10%) | 242 | 15 | 17% | -0.114% | -0.722% | -0.836% | -39.67 € |
| estocastico_rebote | 894.67 € (-3.20%) | 178 | 6 | 34% | -0.097% | -0.743% | -0.878% | -30.27 € |
| ruptura_estricta | 909.00 € (-1.65%) | 55 | 11 | 27% | -0.215% | -1.189% | -1.321% | -15.04 € |
| macd_sin_salida | 899.57 € (-2.67%) | 149 | 15 | 30% | -0.105% | -0.780% | -0.906% | -26.57 € |
| c_banda_atr_tope | 912.43 € (-1.28%) | 30 | 5 | 20% | -0.556% | -1.656% | -1.801% | -11.43 € |
| ruptura_volumen_tope | 912.96 € (-1.22%) | 44 | 5 | 18% | -0.038% | -1.117% | -1.236% | -11.31 € |
| c_banda_atr_regimen | 903.17 € (-2.28%) | 68 | 9 | 24% | -0.518% | -1.401% | -1.536% | -21.87 € |
| macd_momentum_regimen | 887.21 € (-4.01%) | 193 | 1 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.21 € (-2.28%) | 100 | 8 | 21% | -0.152% | -0.913% | -1.039% | -20.91 € |
| c_banda_atr_evento | 907.20 € (-1.84%) | 63 | 24 | 25% | -0.454% | -1.349% | -1.503% | -19.53 € |
| macd_momentum_evento | 898.85 € (-2.75%) | 122 | 15 | 13% | -0.260% | -0.976% | -1.088% | -27.23 € |
| ruptura_volumen_evento | 905.81 € (-1.99%) | 65 | 19 | 14% | -0.341% | -1.247% | -1.372% | -18.61 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 01:55 | macd_momentum_evento | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:55 | macd_momentum | QNT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 01:50 | macd_momentum_evento | ONDO | momentum perdido | +0.06% | -0.44% | -0.10 |
| 2026-09-30 01:50 | c_banda_atr_evento | ZEC | timeout | +0.84% | +0.04% | +0.01 |
| 2026-09-30 01:50 | estocastico_rebote | NIGHT | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 01:50 | macd_momentum | ONDO | momentum perdido | +0.06% | -0.44% | -0.10 |
| 2026-09-30 01:50 | c_banda_atr | ZEC | timeout | +0.84% | +0.34% | +0.08 |
| 2026-09-30 01:45 | c_banda_atr_evento | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:45 | c_banda_atr_tope | BCH | timeout | -0.41% | -1.51% | -0.35 |
| 2026-09-30 01:45 | c_banda_atr | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:40 | ruptura_volumen_tope | USELESS | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 01:35 | macd_sin_salida | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:35 | pullback_tendencia | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:30 | pullback_tendencia | NEAR | take-profit | +2.27% | +1.77% | +0.40 |
| 2026-09-30 01:30 | reversion_bb | FIL | take-profit | +1.93% | +0.83% | +0.19 |

## Eventos de la última vuelta

- 2026-09-30 01:55 [macd_momentum] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:55 [macd_momentum_evento] CIERRE QNT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:50 [pullback_tendencia] ENTRADA NEAR @ 4.4269 (22.65 €, apertura)
- 2026-09-30 01:50 [ruptura_estricta] ENTRADA RENDER @ 1.721 (22.73 €, apertura)
- 2026-09-30 01:50 [c_banda_atr] ENTRADA WLD @ 0.4397 (22.53 €, apertura)
- 2026-09-30 01:50 [c_banda_atr_regimen] ENTRADA WLD @ 0.4397 (22.56 €, apertura)
- 2026-09-30 01:50 [c_banda_atr_evento] ENTRADA WLD @ 0.4397 (22.62 €, apertura)
- 2026-09-30 01:50 [pullback_tendencia] ENTRADA BNB @ 671.13 (22.65 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
