# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 01:46 UTC · vueltas 193 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.30 € (-2.27%) | 94 | 23 | 29% | -0.289% | -1.067% | -1.213% | -23.02 € |
| reversion_bb | 919.60 € (-0.50%) | 26 | 8 | 50% | +0.198% | -0.902% | -1.000% | -5.42 € |
| ruptura_volumen | 899.67 € (-2.66%) | 124 | 18 | 23% | -0.141% | -0.852% | -0.977% | -24.16 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.17 € (-1.95%) | 97 | 2 | 26% | -0.049% | -0.818% | -0.940% | -18.20 € |
| macd_momentum | 885.92 € (-4.15%) | 240 | 17 | 17% | -0.124% | -0.733% | -0.845% | -39.90 € |
| estocastico_rebote | 894.59 € (-3.21%) | 177 | 7 | 34% | -0.107% | -0.755% | -0.888% | -30.56 € |
| ruptura_estricta | 908.58 € (-1.69%) | 55 | 9 | 27% | -0.215% | -1.189% | -1.324% | -15.04 € |
| macd_sin_salida | 899.19 € (-2.71%) | 149 | 15 | 30% | -0.105% | -0.780% | -0.906% | -26.57 € |
| c_banda_atr_tope | 912.47 € (-1.27%) | 30 | 4 | 20% | -0.556% | -1.656% | -1.801% | -11.43 € |
| ruptura_volumen_tope | 912.77 € (-1.24%) | 44 | 4 | 18% | -0.038% | -1.117% | -1.238% | -11.31 € |
| c_banda_atr_regimen | 902.81 € (-2.32%) | 68 | 8 | 24% | -0.518% | -1.401% | -1.535% | -21.87 € |
| macd_momentum_regimen | 887.21 € (-4.01%) | 193 | 1 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.02 € (-2.30%) | 100 | 8 | 21% | -0.152% | -0.913% | -1.039% | -20.91 € |
| c_banda_atr_evento | 906.79 € (-1.89%) | 62 | 23 | 24% | -0.475% | -1.372% | -1.525% | -19.54 € |
| macd_momentum_evento | 898.37 € (-2.80%) | 120 | 17 | 12% | -0.281% | -1.001% | -1.111% | -27.46 € |
| ruptura_volumen_evento | 905.21 € (-2.06%) | 65 | 18 | 14% | -0.341% | -1.247% | -1.372% | -18.61 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 01:45 | c_banda_atr_evento | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:45 | c_banda_atr_tope | BCH | timeout | -0.41% | -1.51% | -0.35 |
| 2026-09-30 01:45 | c_banda_atr | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:40 | ruptura_volumen_tope | USELESS | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 01:35 | macd_sin_salida | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:35 | pullback_tendencia | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:30 | pullback_tendencia | NEAR | take-profit | +2.27% | +1.77% | +0.40 |
| 2026-09-30 01:30 | reversion_bb | FIL | take-profit | +1.93% | +0.83% | +0.19 |
| 2026-09-30 01:25 | macd_momentum_evento | PENGU | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:25 | macd_momentum_evento | RAY | take-profit | +2.13% | +1.63% | +0.36 |
| 2026-09-30 01:25 | macd_momentum_evento | DOT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:25 | macd_momentum_evento | ZEC | momentum perdido | -0.39% | -0.89% | -0.20 |
| 2026-09-30 01:25 | macd_momentum_evento | QNT | momentum perdido | -0.70% | -1.20% | -0.27 |
| 2026-09-30 01:25 | c_banda_atr_evento | RAY | take-profit | +2.37% | +1.87% | +0.42 |
| 2026-09-30 01:25 | macd_sin_salida | RAY | take-profit | +2.13% | +1.63% | +0.36 |

## Eventos de la última vuelta

- 2026-09-30 01:40 [pullback_tendencia] ENTRADA SOL @ 105.11 (22.65 €, apertura)
- 2026-09-30 01:45 [c_banda_atr] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:45 [c_banda_atr_evento] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-30 01:45 [c_banda_atr_tope] CIERRE BCH timeout bruto -0.41% neto -1.51%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
